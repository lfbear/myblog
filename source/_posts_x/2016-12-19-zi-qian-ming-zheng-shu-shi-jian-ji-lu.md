---
layout: post
status: publish
published: true
title: 自签名证书实践记录
author:
  display_name: 小飞熊
  login: fbbear
  email: fbbear@sina.com
  url: 'https://lfbear.com'
author_login: fbbear
author_email: fbbear@sina.com
author_url: 'https://lfbear.com'
wordpress_id: 534
wordpress_url: 'https://lfbear.com/?p=534'
date: '2016-12-19 16:22:01 +0800'
date_gmt: '2016-12-19 08:22:01 +0800'
categories:
  - 工作心语
tags:
  - ca
  - 根证书
  - https
  - 多域名
comments: []
abbrlink: 24308
---
<blockquote>非常感谢如下资料，提供了极为帮助的参考</p>
<p>https://jamielinux.com/docs/openssl-certificate-authority/index.html</p>
<p>http://colinzhouyj.blog.51cto.com/2265679/1566438</p></blockquote>
<p><!--more--></p>
<h3>准备：</h3>
<p>使用工具&nbsp;openssl</p>
<h3>第一步：根证书</h3>
<p>一切证书签署的源泉，需要拥有根证书，才能给其他证书签名。通俗的说就是这个跟证书给所签署的其他证书做背书，用他的拥有的地位来让其他证书变得可信。一般的os中会内置一些国际上的可信根证书，当然本文说的是自签名证书，与『合法』证书的原理一致，区别在于自己生成的跟证书需要手工导入并信任，并不是天然内嵌在os中的。</p>
<p>openssl工具可以提供不同的配置文件，以生成不同用途和类型的证书。生产跟证书请下载并使用这个配置文件&nbsp;https://jamielinux.com/docs/openssl-certificate-authority/_downloads/root-config.txt</p>
<h4>1.1 准备目录和配置文件</h4>
<pre class="brush:bash">mkdir /root/ca
cd /root/ca
#下载root配置文件
curl https://jamielinux.com/docs/openssl-certificate-authority/_downloads/root-config.txt > root-ca.cnf
mkdir certs crl newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
</pre>
<h4>1.2 &nbsp;生成私钥和证书</h4>
<pre class="brush:other">cd /root/ca

# 生成私钥
openssl genrsa -aes256 -out private/ca.key.pem 4096
#需要给私钥设置一个密码
#Enter pass phrase for ca.key.pem: secretpassword
#Verifying - Enter pass phrase for ca.key.pem: secretpassword
chmod 400 private/ca.key.pem

# 生成证书
cd /root/ca
openssl req -config root-ca.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem

#Enter pass phrase for ca.key.pem: secretpassword
# 然后需要填写证书的一些内容 下面是样例 可以根据自己的实际情况填写
#Country Name (2 letter code) [XX]:CN
#State or Province Name []:Beijing
#Locality Name []:Beijing
#Organization Name []:Your Company
#Organizational Unit Name []: Your Department
#Common Name []: Your Company Root CA
#Email Address []: admin@none.com
chmod 444 certs/ca.cert.pem

#验证证书
openssl x509 -noout -text -in certs/ca.cert.pem
</pre>
<h4>1.3 根证书完成</h4>
<p>验证证书后，看到证书信息以及X509v3扩展信息后，根证书的制作到此完成。</p>
<p>&nbsp;</p>
<h3>第二步：中级证书颁发机构</h3>
<p>也称作intermediate certificate authority (CA)，含义很简单，一般的CA不会直接拿跟证书来给最终证书签名，需要一个实体的代表来操作，然后这个代表就是intermediate CA。来个栗子，比如阿里云的证书，是由GlobalSign Organization Validation CA 代表GlobalSign Root来签发的，这个GlobalSign Organization Validation CA就是中级证书颁发机构。而中级证书颁发机构的证书会和根证书一同形成一个信任链，来证明他的有效性。</p>
<p><img class="aligncenter size-full wp-image-543" src="//lfbear.com/upload/2016/12/QQ20161219-0.png" alt="" width="487" height="378" /></p>
<p>这里依然需要一个配置文件，intermediate CA的配置。https://jamielinux.com/docs/openssl-certificate-authority/_downloads/intermediate-config.txt</p>
<p>2.1 准备目录和配置文件</p>
<pre class="brush:bash">mkdir /root/ca/intermediate
cd /root/ca/intermediate
#下载intermediate配置文件
curl https://jamielinux.com/docs/openssl-certificate-authority/_downloads/intermediate-config.txt > intermediate-ca.cnf
mkdir certs crl csr newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
echo 1000 > /root/ca/intermediate/crlnumber</pre>
<h4>&nbsp;2.2 生成私钥和证书</h4>
<pre class="brush:bash"># 生成intermediate私钥
cd /root/ca
openssl genrsa -aes256 -out intermediate/private/intermediate.key.pem 4096
# 设置一个密码
#Enter pass phrase for intermediate.key.pem: secretpassword
#Verifying - Enter pass phrase for intermediate.key.pem: secretpassword
chmod 400 intermediate/private/intermediate.key.pem

# 生成intermediate证书
cd /root/ca
openssl req -config intermediate/intermediate-ca.cnf -new -sha256 \
      -key intermediate/private/intermediate.key.pem \
      -out intermediate/csr/intermediate.csr.pem

# 注意这里填写的Common Name与根证书的要不同
#Country Name (2 letter code) [XX]:CN
#State or Province Name []:Beijing
#Locality Name []:Beijing
#Organization Name []:Your Company
#Organizational Unit Name []: Your Department
#Common Name []: Your Company Intermediate CA
#Email Address []: admin@none.com

# 用根证书给intermediate证书签名
cd /root/ca
openssl ca -config root-ca.cnf -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in intermediate/csr/intermediate.csr.pem \
      -out intermediate/certs/intermediate.cert.pem

#输入根证书密码
#Enter pass phrase for ca.key.pem: secretpassword
#确认签名
#Sign the certificate? [y/n]: y

chmod 444 intermediate/certs/intermediate.cert.pem
</pre>
<p>此时能够看到/root/ca/index.txt已经有类似如下的内容了，这个是根证书的签名记录</p>
<pre>V 250408122707Z 1000 unknown ... /CN=Alice Ltd Intermediate CA</pre>
<h4>2.3验证证书，合并证书</h4>
<pre class="brush:bash">#查看intermediate证书
openssl x509 -noout -text \
      -in intermediate/certs/intermediate.cert.pem

#验证intermediate证书的合法性
openssl verify -CAfile certs/ca.cert.pem \
      intermediate/certs/intermediate.cert.pem
#输出以下内容 代表验证成功
#intermediate.cert.pem: OK</pre>
<p>验证成功后，代表中间证书也制作完成了，这里需要把证书做一个合并</p>
<pre class="brush:bash">cat intermediate/certs/intermediate.cert.pem \
      certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem
chmod 444 intermediate/certs/ca-chain.cert.pem</pre>
<p>其实就是把中间证书和根证书的内容放在一起，目的是形成信任链。</p>
<p>&nbsp;</p>
<h3>第三步：签署最终证书（此处以签署nginx使用的ssl证书为例）</h3>
<h4>3.1&nbsp;生成证书，证书签名，证书验证</h4>
<pre class="brush:bash">#生成证书私钥（一切证书的制作之源）
cd /root/ca
#这里生成了2048位的私钥，而不是4096的，原因是 1.之前生成的根证书和中间证书已经是4096的了 足够安全了；2.4096的证书会大大降低网站的性能
openssl genrsa -aes256 \
      -out intermediate/private/www.example.com.key.pem 2048
chmod 400 intermediate/private/www.example.com.key.pem

#制作www证书
cd /root/ca
openssl req -config intermediate/intermediate-ca.cnf \
      -key intermediate/private/www.example.com.key.pem \
      -new -sha256 -out intermediate/csr/www.example.com.csr.pem
#这里依旧要求填写信息，特别注意：此处的Common Name要填写你证书服务器的域名 比如www.example.com
#Country Name (2 letter code) [XX]:CN
#State or Province Name []:Beijing
#Locality Name []:Beijing
#Organization Name []:Example Ltd
#Organizational Unit Name []:Example Ltd Web Services
#Common Name []:www.example.com
#Email Address []:

#使用中间证书为其签名
cd /root/ca
openssl ca -config intermediate/intermediate-ca.cnf \
      -extensions server_cert -days 375 -notext -md sha256 \
      -in intermediate/csr/www.example.com.csr.pem \
      -out intermediate/certs/www.example.com.cert.pem
chmod 444 intermediate/certs/www.example.com.cert.pem
</pre>
<p>签名完成后 依旧可以看到intermediate/index.txt中的签名记录，最后查看和验证证书</p>
<pre class="brush:bash">#查看证书
openssl x509 -noout -text \
      -in intermediate/certs/www.example.com.cert.pem

#验证证书
openssl verify -CAfile intermediate/certs/ca-chain.cert.pem \
      intermediate/certs/www.example.com.cert.pem
#以下显示为验证成功
#www.example.com.cert.pem: OK</pre>
<h4>3.2 证书部署</h4>
<p>由于我们是自签名的证书，所以需要pc信任根证书，将ca-chain.cert.pem文件分发给需要的pc，导入即可（windows可能需要将改文件拆分成跟证书和中间证书两个crt为扩展名的文件才可以）</p>
<p>nginx的ssl配置中 会有两行跟证书和秘钥相关的：</p>
<p>ssl_certificate &nbsp; &nbsp; /your_nginx_conf_dir/www.example.com.cert.pem;</p>
<p>ssl_certificate_key /your_nginx_conf_dir/www.example.com.nopass.key;</p>
<p>ssl_certificate很容易，就是上一步生成的证书文件，ssl_certificate_key是证书的私钥，这里建议导出一份不需要密码短语的私钥，以方便nginx的维护，否则每次nginx操作都会询问密码短语。</p>
<pre class="brush:bash">#导出无须密码短语的私钥
cd /root/ca
#方案1
openssl rsa -in intermediate/private/www.example.com.key.pem -out www.example.com.nopass.key
#方案2
openssl x509 -req -in intermediate/csr/www.example.com.csr.pem -CA intermediate/certs/www.example.com.cert.pem \
-CAkey intermediate/private/www.example.com.key.pem -CAcreateserial -out www.example.com.nopass.key
</pre>
<h4>3.3 多域名证书</h4>
<p>一般来讲，证书的Common Name部分就是域名，可以写www.example.com或者*.example.com 但是如果你有多个不同域名，这里就没办法解决了。看到下taobao的https证书，他使用了使用者备用名称（DNS）来解决这个问题的。<br />
同样加上操作方式，在本文第三步的基础上修改。<br />
<strong>a.</strong><strong>首先编辑 intermediate/intermediate-ca.cnf</strong></p>
<p>将 req 部分改为如下两行</p>
<pre class="brush:other">[ req ]
distinguished_name = req_distinguished_name
req_extensions = v3_req</pre>
<p><strong>b. 确保req_distinguished_name下没有 0.xxx 的标签</strong>，有的话把0.xxx的0. 去掉 最后新增</p>
<pre class="brush:other"> subjectAltName = @alt_names</pre>
<p><strong>c. 增加 v3_req 部分</strong></p>
<pre class="brush:other">[ v3_req ]
# Extensions to add to a certificate request
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names</pre>
<p><strong>d.添加具体的域名</strong></p>
<pre class="brush:other"># 新增 alt_names,注意括号前后的空格，DNS.x 的数量可以自己加
[ alt_names ]
DNS.1 = *.example.com
DNS.2 = www.example.org
DNS.3 = example.net</pre>
<p><strong>e.注意：生成证书时 Common Name必须在 DNS.x 中</strong><br />
<strong>f.签名证书时 与之前3.1的最后一步略有不同</strong></p>
<pre class="brush:other">openssl ca -config intermediate/intermediate-ca.cnf \
      -extensions v3_req -days 1825 \
      -in intermediate/csr/www.example.com.csr.pem \
      -cert intermediate/certs/ca-chain.cert.pem \
      -keyfile intermediate/private/intermediate.key.pem  \
      -out intermediate/certs/www.example.com.cert.pem
</pre>
<p>&nbsp;</p>
<p>最后：再次感谢文前所提及的两位提供的资料，才能让我的整个实践过程如此顺利。另外，对于证书这里，建议先把逻辑关系理清楚，然后再动手，这样比较不会掉到坑里。</p>
