Secret 与 ConfigMap 类似，但是用来存储敏感信息。Secret 是用来保存和传递密码、密钥、认证凭证这些敏感信息的对象。使用 Secret 的好处是可以避免把敏感信息明文写在配置文件里。在 Kubernetes 集群中配置和使用服务不可避免的要用到各种敏感信息实现登录、认证等功能，例如访问 AWS 存储的用户名密码。为了避免将类似的敏感信息明文写在所有需要使用的配置文件中，可以将这些信息存入一个 Secret 对象，而在配置文件中通过 Secret 对象引用这些敏感信息。这种方式的好处包括：意图明确，避免重复，减少暴漏机会。

在 Master 节点上，secret 以非加密的形式存储（意味着我们要对 master 严加管理）。从 Kubernetes1.7 之后，etcd 以加密的形式保存 secret。secret 的大小被限制为 1MB。当 Secret 挂载到 Pod 上时，是以 tmpfs 的形式挂载，即这些内容都是保存在节点的内存中，而不是写入磁盘，通过这种方式来确保信息的安全性。

每个 Kubernetes 集群都有一个默认的 secrets

```bash
kubectl get secrets -n test
```

创建和调用的过程与 configmap 大同小异。

<a name="DFB6c"></a>
## 创建tls证书
一个tls的证书可以通过以下命令创建：
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=traefik.dashboard.com"
kubectl create secret tls traefik-dashboard-tls --key tls.key --cert tls.crt -n traefik
```
通过Kubernetes Dashboard可以观察到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604023507610-20c36e7f-198d-4c27-9c36-323a5ae96265.png#align=left&display=inline&height=812&originHeight=812&originWidth=772&size=101205&status=done&style=none&width=772)

