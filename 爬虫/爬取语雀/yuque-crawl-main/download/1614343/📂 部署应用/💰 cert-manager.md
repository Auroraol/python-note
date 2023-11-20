<a name="En1ss"></a>
## 一、cert-manager简介

我们知道，在k8s中通常可以使用 `easyrsa`、`openssl` 、 `cfssl` 来生成手动证书，但还是比较麻烦，有如下一些缺点：

1. 如果k8s集群上部署的应用较多，要为每个应用的不同域名生成https证书，操作太麻烦。
2. 上述这些手动操作没有跟k8s的deployment描述文件放在一起记录下来，很容易遗忘。
3. 证书过期后，又得手动执行命令重新生成证书。

对于这些问题，cert-manager就很好地解决了这些痛点。cert-manager是Kubernetes上一个管理SSL证书的插件，配合ingress可以对网站配置https访问，在加上letsencrypt提供免费的SSL证书，所有就产生了cert-manager+ingress（nginx/traefik）+letsencrypt的免费套餐。 

- [cert-manager - GitHub](https://github.com/jetstack/cert-manager)
- [cert-manager - 官网](https://cert-manager.io/)

<a name="d5hFT"></a>
### cert-manager 的架构
cert-manager 架构图：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603934871517-677ce1ad-26c1-41e1-b487-0530dd90e1b1.png#align=left&display=inline&height=997&originHeight=997&originWidth=1891&size=126514&status=done&style=none&width=1891)

上面是官方给出的架构图，可以看到cert-manager在k8s中定义了两个自定义类型资源：`Issuer`和`Certificate`。

其中`Issuer`代表的是证书颁发者，可以定义各种提供者的证书颁发者，当前支持基于`Letsencrypt`、`vault`和`CA`的证书颁发者，还可以定义不同环境下的证书颁发者。<br />而`Certificate`代表的是生成证书的请求，一般其中存入生成证书的元信息，如域名等等。

一旦在k8s中定义了上述两类资源，部署的`cert-manager`则会根据`Issuer`和`Certificate`生成TLS证书，并将证书保存进k8s的`Secret`资源中，然后在`Ingress`资源中就可以引用到这些生成的`Secret`资源。对于已经生成的证书，还是定期检查证书的有效期，如即将超过有效期，还会自动续期。

<a name="rsC5I"></a>
## 二、安装cert-manager
添加仓库并更新：
```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create namespace cert-manager
kubectl label namespace cert-manager certmanager.k8s.io/disable-validation=true
```
部署cert-manager：
```bash
helm install cert-manager jetstack/cert-manager -n cert-manager --version v1.0.3 --set installCRDs=true
```
注意上面需要加上 `--set installCRDs=true` ，否则不会创建自定义资源。如果忘记加上了，可以使用以下命令创建自定义资源：<br />
```bash
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.0.3/cert-manager.crds.yaml
```

部署完成，看到控制台打印：
```bash
NAME: cert-manager
LAST DEPLOYED: Wed Oct 28 16:19:57 2020
NAMESPACE: cert-manager
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
cert-manager has been deployed successfully!

In order to begin issuing certificates, you will need to set up a ClusterIssuer
or Issuer resource (for example, by creating a 'letsencrypt-staging' issuer).

More information on the different types of issuers and how to configure them
can be found in our documentation:

https://cert-manager.io/docs/configuration/

For information on how to configure cert-manager to automatically provision
Certificates for Ingress resources, take a look at the `ingress-shim`
documentation:

https://cert-manager.io/docs/usage/ingress/
```

完成后，在Kubernetes Dashboard中可以看到自定义资源：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603935951084-2d0a2029-03bc-4785-85d5-b30afe2e5a9c.png#align=left&display=inline&height=301&originHeight=301&originWidth=1643&size=34204&status=done&style=none&width=1643)

<a name="ds9xr"></a>
## 三、创建Issuer资源
<a name="01CAT"></a>
### 使用ClusterIssuer创建letsencrypt的证书颁发者
创建ClusterIssuer类型的Issuer如下：
```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    email: xxx@qq.com
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-staging
    solvers:
    - http01:
        ingress:
          class: traefik

---

apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: xxx@qq.com
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: traefik
```
注意这里创建的资源类型是`ClusterIssuer`，这样这个证书颁发者就可以为整个集群中任意命名空间颁发证书。<br />如果创建的资源类型为`Issuer`，则只能在当前命名空间下使用。

要使用此Issuer，在创建Ingress的时候添加以下三个注解即可：
```yaml
  annotations:
    kubernetes.io/ingress.class: traefik
    kubernetes.io/tls-acme: "true"
    cert-manager.io/cluster-issuer: letsencrypt-staging
```
注意 `cert-manager.io/cluster-issuer` 与上面创建的ClusterIssuer名称对应。

先开启一个nginx的web服务，然后创建Ingress，完整的YAML如下：
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx
  namespace: nginx
  annotations:
    kubernetes.io/ingress.class: traefik
    kubernetes.io/tls-acme: "true"
    cert-manager.io/cluster-issuer: letsencrypt-staging
spec:
  rules:
  - host: nginx.test.com
    http:
      paths:
      - path: /
        backend:
          serviceName: nginx
          servicePort: 80
  tls:
  - hosts:
      - nginx.test.com
    secretName: nginx
```
创建成功后，就可以使用 [https://nginx.test.com](https://nginx.test.com) 访问此服务了。

---


由于我是在Windows Desktop本地环境进行的测试，不能被公网访问，所以证书颁发并不会成功，HTTPS服务也不能正常访问，使用以下命令可以看到证书的状态，发现创建证书出了问题：
```yaml
$ kubectl describe certificate nginx -n nginx
Name:         nginx
Namespace:    nginx
Labels:       <none>
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
...
Status:
  Conditions:
    Last Transition Time:        2020-10-28T09:16:46Z
    Message:                     Issuing certificate as Secret does not exist
    Reason:                      DoesNotExist
    Status:                      False
    Type:                        Ready
    Last Transition Time:        2020-10-28T09:16:46Z
    Message:                     Issuing certificate as Secret does not exist
    Reason:                      DoesNotExist
    Status:                      True
    Type:                        Issuing
  Next Private Key Secret Name:  nginx-zh82k
Events:
  Type    Reason     Age   From          Message
  ----    ------     ----  ----          -------
  Normal  Issuing    14m   cert-manager  Issuing certificate as Secret does not exist
  Normal  Generated  14m   cert-manager  Stored new private key in temporary Secret resource "nginx-zh82k"
  Normal  Requested  14m   cert-manager  Created new CertificateRequest resource "nginx-ljtbx"
```

<a name="lgNWY"></a>
## 四、创建Certificate资源
有了签发机构，接下来我们就可以生成免费证书了，cert-manager 给我们提供了 Certificate 这个用于生成证书的自定义资源对象，它必须局限在某一个 namespace 下，证书最终会在这个 namespace 下以 Secret 的资源对象存储。



<a name="8LhTW"></a>
## 参考资料

- [在 Kubernetes 中安装cert-manager](https://cert-manager.io/docs/installation/kubernetes/)
- [k8s如何加入TLS安全访问，技术发烧友为你探路](https://cloud.tencent.com/developer/article/1199190)
- [k8s中使用cert-manager玩转证书](https://cloud.tencent.com/developer/article/1402451)
- [使用 KubeSphere 在 Kubernetes 安装 cert-manager 为网站启用 HTTPS](https://www.kubernetes.org.cn/8289.html)

