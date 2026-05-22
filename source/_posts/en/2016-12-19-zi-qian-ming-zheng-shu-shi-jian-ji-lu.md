---
layout: post
status: publish
published: true
title: 'A Practical Guide to Creating Self-Signed Certificates with OpenSSL'
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
  - Professional Thoughts
tags:
  - ca
  - root-certificate
  - https
  - multi-domain
comments: []
abbrlink: 24308
lang: en
---

> Special thanks to the following resources for providing extremely helpful references:
> 
> * [https://jamielinux.com/docs/openssl-certificate-authority/index.html](https://jamielinux.com/docs/openssl-certificate-authority/index.html)
> * [http://colinzhouyj.blog.51cto.com/2265679/1566438](http://colinzhouyj.blog.51cto.com/2265679/1566438)

<!--more-->

### Preparation
Tool used: `openssl`

### Step 1: Root Certificate
The root certificate is the ultimate source of all certificate signings. You must have a root certificate in order to sign other certificates. Simply put, this root certificate acts as a guarantor for any certificates it signs, utilizing its authority to make those downstream certificates trusted. Standard operating systems come pre-installed with built-in globally trusted root certificates. Since this post describes self-signed certificates, the underlying cryptographic principles are identical to "official" certificates. The only difference is that root certificates you generate yourself must be manually imported and trusted on target machines, as they are not natively embedded in the OS.

OpenSSL allows for different configuration files to generate certificates for various purposes and types. For generating a root certificate, please download and use this configuration file: [https://jamielinux.com/docs/openssl-certificate-authority/_downloads/root-config.txt](https://jamielinux.com/docs/openssl-certificate-authority/_downloads/root-config.txt)

#### 1.1 Set Up Directories and Configuration File
```bash
mkdir /root/ca
cd /root/ca
# Download the root configuration file
curl https://jamielinux.com/docs/openssl-certificate-authority/_downloads/root-config.txt > root-ca.cnf
mkdir certs crl newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
```

#### 1.2 Generate Private Key and Certificate
```bash
cd /root/ca

# Generate the private key
openssl genrsa -aes256 -out private/ca.key.pem 4096
# You will be prompted to set a passphrase for the private key
# Enter pass phrase for ca.key.pem: secretpassword
# Verifying - Enter pass phrase for ca.key.pem: secretpassword
chmod 400 private/ca.key.pem

# Generate the self-signed root certificate
cd /root/ca
openssl req -config root-ca.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem

# Enter pass phrase for ca.key.pem: secretpassword
# Next, you will need to fill in details for the certificate. Here is an example:
# Country Name (2 letter code) [XX]:CN
# State or Province Name []:Beijing
# Locality Name []:Beijing
# Organization Name []:Your Company
# Organizational Unit Name []: Your Department
# Common Name []: Your Company Root CA
# Email Address []: admin@none.com
chmod 444 certs/ca.cert.pem

# Verify the certificate
openssl x509 -noout -text -in certs/ca.cert.pem
```

#### 1.3 Root Certificate Complete
After verifying the certificate and inspecting the certificate information along with the X509v3 extension details, your root certificate is officially complete.

### Step 2: Intermediate Certificate Authority (CA)
As the name implies, an intermediate CA represents the root CA to sign end-user certificates, since commercial root CAs almost never sign final certificates directly. For example, Aliyun's SSL certificate is typically issued by the `GlobalSign Organization Validation CA` on behalf of the `GlobalSign Root CA`; here, `GlobalSign Organization Validation CA` is the Intermediate CA. Intermediate CA certificates accompany the root certificate to form a chain of trust that validates the final certificate's authenticity.

![](//lfbear.com/upload/2016/12/QQ20161219-0.png)

Again, we need a configuration file specifically for the intermediate CA: [https://jamielinux.com/docs/openssl-certificate-authority/_downloads/intermediate-config.txt](https://jamielinux.com/docs/openssl-certificate-authority/_downloads/intermediate-config.txt)

#### 2.1 Set Up Directories and Configuration File
```bash
mkdir /root/ca/intermediate
cd /root/ca/intermediate
# Download the intermediate configuration file
curl https://jamielinux.com/docs/openssl-certificate-authority/_downloads/intermediate-config.txt > intermediate-ca.cnf
mkdir certs crl csr newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
echo 1000 > /root/ca/intermediate/crlnumber
```

#### 2.2 Generate Private Key and Certificate
```bash
# Generate the intermediate private key
cd /root/ca
openssl genrsa -aes256 -out intermediate/private/intermediate.key.pem 4096
# Set a passphrase
# Enter pass phrase for intermediate.key.pem: secretpassword
# Verifying - Enter pass phrase for intermediate.key.pem: secretpassword
chmod 400 intermediate/private/intermediate.key.pem

# Generate the Intermediate Certificate Signing Request (CSR)
cd /root/ca
openssl req -config intermediate/intermediate-ca.cnf -new -sha256 \
      -key intermediate/private/intermediate.key.pem \
      -out intermediate/csr/intermediate.csr.pem

# Note: The Common Name entered here MUST differ from the Root CA's Common Name.
# Country Name (2 letter code) [XX]:CN
# State or Province Name []:Beijing
# Locality Name []:Beijing
# Organization Name []:Your Company
# Organizational Unit Name []: Your Department
# Common Name []: Your Company Intermediate CA
# Email Address []: admin@none.com

# Use the root certificate to sign the intermediate certificate
cd /root/ca
openssl ca -config root-ca.cnf -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in intermediate/csr/intermediate.csr.pem \
      -out intermediate/certs/intermediate.cert.pem

# Enter root certificate passphrase:
# Enter pass phrase for ca.key.pem: secretpassword
# Confirm signing:
# Sign the certificate? [y/n]: y

chmod 444 intermediate/certs/intermediate.cert.pem
```
At this stage, you should see that `/root/ca/index.txt` now contains a record similar to the following, which is the signing entry from the root CA:

`V 250408122707Z 1000 unknown ... /CN=Alice Ltd Intermediate CA`

#### 2.3 Verify and Concatenate Certificates
```bash
# Inspect the intermediate certificate
openssl x509 -noout -text \
      -in intermediate/certs/intermediate.cert.pem

# Verify the legitimacy of the intermediate certificate
openssl verify -CAfile certs/ca.cert.pem \
      intermediate/certs/intermediate.cert.pem
# The following output indicates successful validation:
# intermediate.cert.pem: OK
```
Once verified, the intermediate certificate is complete. We now need to concatenate them to form the certificate chain:
```bash
cat intermediate/certs/intermediate.cert.pem \
      certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem
chmod 444 intermediate/certs/ca-chain.cert.pem
```
This simple command combines the intermediate certificate and the root certificate into a single file to build the full chain of trust.

### Step 3: Signing the Final Certificate (Nginx SSL Certificate Example)

#### 3.1 Generate Private Key, CSR, Sign, and Verify

# Generate the server private key (the root of all server-side certificates)
```bash
cd /root/ca
# Here, we generate a 2048-bit key instead of 4096-bit because:
# 1. The Root and Intermediate certificates are already 4096-bit, which is exceptionally secure.
# 2. A 4096-bit server key would severely degrade website SSL handshake performance.
openssl genrsa -aes256 \
      -out intermediate/private/www.example.com.key.pem 2048
chmod 400 intermediate/private/www.example.com.key.pem

# Generate the CSR for the website
cd /root/ca
openssl req -config intermediate/intermediate-ca.cnf \
      -key intermediate/private/www.example.com.key.pem \
      -new -sha256 -out intermediate/csr/www.example.com.csr.pem
# You will be prompted to fill in information. Note: The Common Name MUST match the domain name of your server, e.g. www.example.com
# Country Name (2 letter code) [XX]:CN
# State or Province Name []:Beijing
# Locality Name []:Beijing
# Organization Name []:Example Ltd
# Organizational Unit Name []:Example Ltd Web Services
# Common Name []:www.example.com
# Email Address []:

# Sign the server certificate using the intermediate CA
cd /root/ca
openssl ca -config intermediate/intermediate-ca.cnf \
      -extensions server_cert -days 375 -notext -md sha256 \
      -in intermediate/csr/www.example.com.csr.pem \
      -out intermediate/certs/www.example.com.cert.pem
chmod 444 intermediate/certs/www.example.com.cert.pem
```
Once signed, you will see a new entry added to `intermediate/index.txt`. Next, verify the generated certificate:
```bash
# View the certificate
openssl x509 -noout -text \
      -in intermediate/certs/www.example.com.cert.pem

# Verify the certificate against the certificate chain
openssl verify -CAfile intermediate/certs/ca-chain.cert.pem \
      intermediate/certs/www.example.com.cert.pem
# The following output indicates successful validation:
# www.example.com.cert.pem: OK
```

#### 3.2 Certificate Deployment
Because this is a self-signed certificate authority, clients (PCs/devices) must trust your root certificate. Distribute the `ca-chain.cert.pem` file to target machines and import it. (For Windows, you might need to split this chain file into separate root and intermediate certificates with `.crt` extensions for the certificate manager to accept them correctly).

In the Nginx SSL block, there are two primary lines relating to the certificate and key:
```nginx
ssl_certificate     /your_nginx_conf_dir/www.example.com.cert.pem;
ssl_certificate_key /your_nginx_conf_dir/www.example.com.nopass.key;
```
`ssl_certificate` is simply the certificate file generated in the previous step, while `ssl_certificate_key` is the server's private key. For convenience, it is highly recommended to export a version of the private key that does not require a passphrase. Otherwise, Nginx will prompt you for the passphrase every time the service starts or reloads.

# Export the private key without a passphrase
```bash
cd /root/ca
# Method 1
openssl rsa -in intermediate/private/www.example.com.key.pem -out www.example.com.nopass.key
# Method 2
openssl x509 -req -in intermediate/csr/www.example.com.csr.pem -CA intermediate/certs/www.example.com.cert.pem \
-CAkey intermediate/private/www.example.com.key.pem -CAcreateserial -out www.example.com.nopass.key
```

#### 3.3 Multi-Domain Certificates
Typically, a certificate's `Common Name` is the primary domain name, such as `www.example.com` or `*.example.com`. However, if you need the certificate to secure multiple completely different domains, the `Common Name` alone cannot solve this. If you examine Taobao's HTTPS certificate, you'll see they leverage the **Subject Alternative Name (SAN)** extension to resolve this.

To implement this, modify Step 3 as follows:

**a. First, edit `intermediate/intermediate-ca.cnf`**
Change the `[ req ]` block to include the following lines:
```ini
[ req ]
distinguished_name = req_distinguished_name
req_extensions = v3_req
```

**b. Ensure there are no `0.xxx` tags under `req_distinguished_name`**. If there are, strip the `0.` prefix, and then add this line at the bottom:
```ini
subjectAltName = @alt_names
```

**c. Add the `[ v3_req ]` block**
```ini
[ v3_req ]
# Extensions to add to a certificate request
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
```

**d. Append the list of domains**
```ini
# Add the alt_names section. Be mindful of formatting. You can add as many DNS.x entries as required.
[ alt_names ]
DNS.1 = *.example.com
DNS.2 = www.example.org
DNS.3 = example.net
```

**e. Note**: The `Common Name` used during CSR generation must also be included in the `DNS.x` list.

**f. When signing the certificate, the command differs slightly from step 3.1:**
```bash
openssl ca -config intermediate/intermediate-ca.cnf \
      -extensions v3_req -days 1825 \
      -in intermediate/csr/www.example.com.csr.pem \
      -cert intermediate/certs/ca-chain.cert.pem \
      -keyfile intermediate/private/intermediate.key.pem  \
      -out intermediate/certs/www.example.com.cert.pem
```

**Conclusion:** Again, many thanks to the authors of the two references mentioned at the beginning of this article. Their guides made my entire implementation process incredibly smooth. Lastly, when working with certificates, I highly recommend mapping out the exact logical hierarchy of keys and authorities in your head before touching the terminal. This keeps you from falling into common configuration traps.
