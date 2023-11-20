<a name="8pLgx"></a>
## 一、Metrics Server简介
在以前，都是使用 [heapster](https://github.com/kubernetes-retired/heapster) 进行CUP、内存资源的监控。不过官方目前已经停止维护，并引导大家使用Metrics。

Heapster 的 GitHub 中提到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604157082063-ef9df5a8-4c86-45c3-b823-db8246d0da38.png#align=left&display=inline&height=209&originHeight=209&originWidth=870&size=20083&status=done&style=none&width=870)

[Metrics Server](https://github.com/kubernetes-sigs/metrics-server) 是Kubernetes集群资源使用情况的聚合器，Kubernetes中有些组件依赖资源指标API(metric API)的功能 ，如kubectl top 、hpa。如果没有资源指标API接口，这些组件无法运行。自kubernetes 1.8开始，资源使用指标通过 Metrics API 在 Kubernetes 中获取，从kubernetes1.11开始Heapster被废弃不再使用，metrics-server 替代了heapster。

<a name="n78wr"></a>
## 二、安装Metrics Server
<a name="FQdYW"></a>
### 使用Helm安装
添加仓库并更新：
```json
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```
先创建一个namespace，以免默认添加到default：
```json
kubectl create ns metrics
```
部署[Metrics Server](https://artifacthub.io/packages/helm/bitnami/metrics-server)：
```json
helm install metrics bitnami/metrics-server -n metrics
```

部署完，会在控制台中打印：
```bash
NAME: metrics
LAST DEPLOYED: Sat Oct 31 20:15:42 2020
NAMESPACE: metrics
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

The metric server has been deployed.

########################################################################################
### ERROR: The metrics.k8s.io/v1beta1 API service is not enabled in the cluster      ###
########################################################################################
You have disabled the API service creation for this release. As the Kubernetes version in the cluster
does not have metrics.k8s.io/v1beta1, the metrics API will not work with this release unless:

Option A:

  You complete your metrics-server release by running:

  helm upgrade metrics bitnami/metrics-server \
    --set apiService.create=true

Option B:

   You configure the metrics API service outside of this Helm chart
```
可以看到很明显的提示，需要进行以下设置：
```bash
helm upgrade metrics bitnami/metrics-server --set apiService.create=true -n metrics
```
更新完后，打印出以下内容就说明成功了：
```bash
Release "metrics" has been upgraded. Happy Helming!
NAME: metrics
LAST DEPLOYED: Sat Oct 31 20:18:30 2020
NAMESPACE: metrics
STATUS: deployed
REVISION: 2
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

The metric server has been deployed.

In a few minutes you should be able to list metrics using the following
command:

  kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
```
查看所有的API列表，发现多了个 `metrics.k8s.io/v1beta1` ：
```bash
$ kubectl api-versions
...
metrics.k8s.io/v1beta1
```

<a name="D8xD5"></a>
### 使用YAML安装（仅供了解）
另一种部署方式，通过YAML部署：
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.7/components.yaml
```

<a name="Rozpc"></a>
## 三、查看Metrics Server
打开Kubernetes Dashboard，可以看到指定空间CPU和内存信息消耗：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604156832080-a3ac9253-1d6b-4287-a146-f256e2d650cf.png#align=left&display=inline&height=815&originHeight=815&originWidth=1906&size=114705&status=done&style=none&width=1906)<br />Pods视图也能看到每个Pod的资源消耗：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604159404782-461cf633-0a91-4001-aac5-aefb037bffa4.png#align=left&display=inline&height=279&originHeight=279&originWidth=1637&size=38069&status=done&style=none&width=1637)
<a name="ScFrj"></a>
## 四、命令查看
<a name="dIJYb"></a>
### 查看集群节点资源使用情况（CPU，MEM）
```bash
❯ kubectl top nodes
NAME             CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
docker-desktop   224m         2%     3060Mi          12%

❯ kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
{"kind":"NodeMetricsList","apiVersion":"metrics.k8s.io/v1beta1","metadata":{"selfLink":"/apis/metrics.k8s.io/v1beta1/nodes"},"items":[{"metadata":{"name":"docker-desktop","selfLink":"/apis/metrics.k8s.io/v1beta1/nodes/docker-desktop","creationTimestamp":"2020-10-31T15:44:26Z"},"timestamp":"2020-10-31T15:44:03Z","window":"30s","usage":{"cpu":"287447541n","memory":"3134192Ki"}}]}
```

<a name="nmQhe"></a>
### 查看pods资源使用情况
```bash
❯ kubectl -n metrics top pods
NAME                                     CPU(cores)   MEMORY(bytes)   
metrics-metrics-server-6754d985f-qzj7c   1m           15Mi
```

<a name="ZWFXL"></a>
### 查看指定pod资源使用情况
```bash
❯ kubectl -n metrics top pods metrics-metrics-server-6754d985f-qzj7c
NAME                                     CPU(cores)   MEMORY(bytes)   
metrics-metrics-server-6754d985f-qzj7c   2m           15Mi
```

<a name="Z869C"></a>
## 五、常见错误
<a name="6I1cZ"></a>
### error: metrics not available yet
执行命令时，报此错误：
```bash
❯ kubectl top nodes
error: metrics not available yet
❯ kubectl top pods -n kube-system
W1031 22:46:39.598768   11096 top_pod.go:265] Metrics not available for pod kube-system/coredns-66bff467f8-t7wvz, age: 816h59m47.5987688s
error: Metrics not available for pod kube-system/coredns-66bff467f8-t7wvz, age: 816h59m47.5987688s
```

解决方案：<br />然后修改部署文件：
```bash
kubectl edit deploy -n metrics metrics-metrics-server
```
在 **spec.template.spec.containers** 下添加：
```bash
args:
- --kubelet-insecure-tls
- --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
- --metric-resolution=30s
```
示例：
```bash
[...]
spec:
  [...]
  template:
    spec:
      containers:
      - args:
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-insecure-tls
        - --metric-resolution=30s
        image: 'docker.io/bitnami/metrics-server:0.3.7-debian-10-r144'
				[...]
[...]
```

参考：

- [How to troubleshoot metrics-server on kubeadm?](https://www.it1352.com/1535580.html)
- [error: metrics not available yet](https://github.com/kubernetes-sigs/metrics-server/issues/247)

<a name="h4pph"></a>
## 参考资料

- [Kubernetes实录-第一篇-集群部署配置(18) Kubernetes部署metrics-server 0.3.7](https://blog.csdn.net/oyym_mv/article/details/87166639)
