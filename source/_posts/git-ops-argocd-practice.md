---
title: GitOps之ArgoCD实践
abbrlink: 11197
date: 2021-07-06 15:48:58
tags: [GitLab,CI,CD,Argo,Kustomize,primary]
---

## 背景

本文旨在通过基于GitLab+ArgoCD的案例来介绍GitOps的一种可行的实践方案。
这个案例可以满足对轻量，快速的容器部署需求。如果你部署在K8s中的项目正在寻找一个轻量快捷的部署方式，相信GitOps是一个很好的选择。
一般来说，我们的代码都交由GitLab等CVS工具管理，近些年随着GitLab对CI的支持越来越友好，GitOps得以更加容易的落地。

<!--more-->

## 基础知识

### 组成部分

- CI: 由 [GitLab pipeline](https://docs.gitlab.com/ee/ci/pipelines/) 实现
- CD: 由 [ArgoCD](https://argoproj.github.io/argo-cd/) 实现
- Artifact: 也称为制品，可以理解将各自独立的CI和CD连接到一起的东西

*本文的CI和CD均为侠义含义，可以简单理解为构建和部署。*

### CI

核心： 在GitLab中，我们用 `.gitlab-ci.yml` 文件用来定义GitLab的CI Pipeline。除去日常的代码检查，单元测试外，比较关键的就是可以对项目做编译，当然也可以直接在gitlab-ci中直接做部署，后面会提及为什么不这么做。

### CD

这个阶段有两个重点，一是要部署的制品，一般是项目编译的产物，常见的是二进制或包；二是部署指引，就是这些东西要怎么部署，比如放在哪个目录下，如何启动等。因为这个部署指引一般来说比较复杂，包括各种步骤，check point等，因此一般交由单独的系统来负责，因此除非部署过程及其简单，我们一般不使用gitlab-ci来做部署过程，但可以由它来触发部署行为。


## 有图有真相

下图是本文案例的整体实现过程

![GitOps-Argocd](/assets/images/gitops-argocd.png)

### CI 阶段 --- 交付物: docker镜像

*说在前面：由于GitLab的版本迭代较快，变化较大，如果不清楚目前使用的GitLab版本，请使用help页面中的文档而不是官方文档*

#### User Story

开发者根据各自的开发需求，分别向A项目提交代码。特定的分支(图例中为test_branch)提交会触发`.gitlab-ci.yml`定义的stage(图例中为build-image)，并执行该stage中声明的脚本，这部分脚本将会根据项目中的Dockerfile打出一个docker镜像，并将镜像推送到指定repo

#### `.gitlab-ci.yml`

图例中的gitlab-ci中构建镜像部分的定义如下：
 - `variables`和`stages`为公共部分，后面不会赘述。
 - 在`build-image`的`before_script`中，会有一个docker register登录的动作，`script`中仅做了docker build和docker push，将产物推送到镜像仓库
 - 触发条件：`only`中定义了触发条件，仅test_branch分支有变化的时候触发（由only字段声的多个条件为’或‘的关系）。`except`排除条件中对commit标题（也就是commit中的首行）和tag做了排除。至于为什么要排除提定的commit，后面会说到。


```
variables:
  REGISTRY_HOST: hub.docker.com
  REGISTRY_IMAGE_TAG: $REGISTRY_HOST/your-repo/your-app:$CI_COMMIT_SHA

stages:
  - build
  - deploy

build-image:
  image: docker:20.10
  tags:
    - runner-tag
  stage: build
  before_script:
    - docker login $REGISTRY_HOST -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD
  script:
    - docker build -t $REGISTRY_IMAGE_TAG .
    - docker push $REGISTRY_IMAGE_TAG
  except:
    variables:
      - $CI_COMMIT_TITLE == "SkipCI"
    refs:
      - tags
  only:
    - test_branch
```

关于gitlab-ci的详细语法，请参照文档使用。

#### GitLab Runner

必须，也就是`.gitlab-ci.yml`具体的执行者，gitlab-runner有[很多种安装方式](https://docs.gitlab.com/runner/install/)，安装完成后记得给它们打tag分组，在`.gitlab-ci.yml`中可以按照stage纬度指定执行的runner。

### CD 阶段 --- 关键词: Kustomize

#### Kustomize

在聊ArgoCD之前，先引入[Kustomize](https://kustomize.io/)这个东西，它是K8s原生的配置管理工具。由它来管理K8s的配置是比较方便的选择。

设想这样一个场景，你有一个deployment需要部署到2个集群，通常你的作法可能是切到一个集群apply然后再切到另外一个集群apply一下，操作复杂度应该还ok。
但是如果有人告诉你不同集群的镜像或启动参数有差异，那又要怎么搞呢。复制出来一份，修改一下差异的地方？操作起来略复杂呢。如果这种deployment有10个或者100个呢。
在抓狂前，可以先了解一下Kustomize。部署到不同环境的时候，难免会有差异，至少deployment名字或者label会有差异吧，所以可以选择它来cover这个。

如果你不知道我在说什么也没关系，你就把这part当做K8s的deployment的yaml就可以了。反正就是用来部署的配置嘛。

#### ArgoCD

下面我们来介绍ArgoCD，它本质上只是一个工具，如图中所示，可以理解为Argo一边监控着GitLab指定repo和分支上面的Kustomize文件，另外一边watch着k8s中的资源，对比两边是否有变化，如果有变化可以自动或手工的发起k8s向的同步。

可能会有人发问了，为什么要监控GitLab上的Kustomize文件呢？
- 如果你在使用Kustomize文件，而并不想使用GitLab来存储，那就不是GitOps了，其实也是可以的，但不是本文讨论的方向。从我个人的使用体感觉得，少借助一个外部工具不是一件很好的事儿么。
- 如果你使用GitLab来存储这些部署配置，那为什么是Kustomize文件呢？其实的确不必须是Kustomize文件，ArgoCD提供了很多种部署配置方式，比如helm, ksonnet, jsonnet等

#### 小结

概括一下CD部分，首先部署需要配置（上文的Kustomize文件），把配置放到git里面，使用CD工具监控这些部署配置与真实部署情况的差异，同样以申明式的方式来管理部署就是我们说的GitOps了。

最后说一下，因为CD是以git项目中的部署配置（Kustomize文件）为准，如果它刚好跟要部署的项目在同一个git的repo中，就需要在GitLab的pipeline中做一个特殊处理，也就是CI在提交镜像的同时需要去修改git项目中的Kustomize文件，但本次修改又不能再次触发ci的pipeline，所以有了上文的`$CI_COMMIT_TITLE == "SkipCI"`这个排除条件（适用于10以上版本的GitLab，较高版本有[更优雅的方式](https://docs.gitlab.com/ee/ci/yaml/#skip-pipeline)处理跳过触发），可以看下我的demo项目的这部分pipeline配置

```
deploy-by-argo:
  image: alpine/git # 这里需要一个含有git的镜像
  stage: deploy
  cache: {}
  script:
    - git config --global user.email "youremail@youremail.org"
    - git config --global user.name "your-name"
    - git checkout test_branch
    - git pull
    - git status
    - sed -i "s#/your-repo/your-app:\w*#/your-repo/your-app:$CI_COMMIT_SHA#" ./hack/deploy/test_branch/patch.yaml
    - git add ./hack/deploy/test_branch/patch.yaml
    - git commit -m "SkipCI"
    - git status
    - git push https://git-user:$GIT_PASSWORD@gitlab.com/your-repo/your-app.git --all
  tags:
    - runner-tag
  except:
    variables:
      - $CI_COMMIT_TITLE == "SkipCI"
  only:
    - test_branch
  dependencies:
    - build-image
```

./hack/deploy/test_branch/patch.yaml 文件内容

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-app
  namespace: default
spec:
  replicas: 1
  template:
    spec:
      containers:
        - name: instance
          image: hub.docker.com/your-repo/your-app:abcd123 # Don't edit the tag, ci will auto replace it
```

**以上就是GitOps之ArgoCD的实践全部内容，任何问题可以在文后留言交流。**
