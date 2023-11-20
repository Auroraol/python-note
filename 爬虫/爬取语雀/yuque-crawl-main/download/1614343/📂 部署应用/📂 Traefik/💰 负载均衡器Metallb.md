<a name="nJ8Jq"></a>
## 一、Metallb简介
在本地安装的时候，不能直接安装Traefik，否则在将服务设置为LoadBalance后，服务不能正常启动。需要先安装一个负载均衡器，本文使用[Metallb](https://metallb.universe.tf/)作为负载均衡器。MetalLB是使用标准路由协议的裸机Kubernetes集群的软负载均衡器。

Kubernetes没有为裸机群集提供网络负载均衡器（类型为LoadBalancer的服务）的实现，如果你的kubernetes集群没有在公有云的IaaS平台（GCP，AWS，Azure …）上运行，则LoadBalancers将在创建时无限期地保持“挂起”状态，也就是说只有公有云厂商自家的kubernetes支持LoadBalancer。

裸机群集运营商留下了两个较小的工具来将用户流量带入其集群，“NodePort”和“externalIPs”服务。这两种选择都对生产使用产生了重大影响，这使得裸露的金属集群成为Kubernetes生态系统中的二等公民。

而在云服务器比如阿里的ECS中并不需要单独配置，里面自带了云服务提供商提供的默认负载均衡器。

<a name="4zGSi"></a>
### Metallb存在的意义
MetalLB旨在通过提供与标准网络设备集成的网络LB实现来纠正这种不平衡，以便裸机集群上的外部服务也“尽可能”地工作。即MetalLB能够帮助你在kubernetes中创建LoadBalancer类型的kubernetes服务。<br />**
<a name="kDZuh"></a>
### Metallb基本原理
Metallb 会在 Kubernetes 内运行，监控服务对象的变化，一旦察觉有新的 LoadBalancer 服务运行，并且没有可申请的负载均衡器之后，就会完成两部分的工作：

1. 地址分配：用户需要在配置中提供一个地址池，Metallb 将会在其中选取地址分配给服务。
2. 地址广播：根据不同配置，Metallb 会以二层（ARP/NDP）或者 BGP 的方式进行地址的广播。

关于Metallb集群的负载均衡方案介绍：[Bare-metal considerations](https://kubernetes.github.io/ingress-nginx/deploy/baremetal/)

<a name="yv53v"></a>
### **基本原理图**
在云服务器中，云服务提供商会提供一个负载均衡器：<br />![cloud_overview.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1604386952135-daac50a8-c80a-42fc-b73f-ab662025b8da.jpeg#align=left&display=inline&height=567&originHeight=567&originWidth=756&size=38777&status=done&style=none&width=756)<br />但是在裸机部署时，并不存在这个负载均衡器：<br />![baremetal_overview.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1604386985110-f0c0ff8b-f7a4-4663-b7f4-c8808b7ab461.jpeg#align=left&display=inline&height=484&originHeight=484&originWidth=756&size=30872&status=done&style=none&width=756)<br />而Metallb解决的就是这个问题，它虚拟出一个负载均衡器IP，并导向其他节点：<br />![metallb.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1604387005585-0734692f-2c02-48c5-8b17-9805368237bd.jpeg#align=left&display=inline&height=447&originHeight=447&originWidth=756&size=41835&status=done&style=none&width=756)<br />相关站点：

- [Metallb 官网](https://metallb.universe.tf/)
- [Metallb GitHub](https://github.com/metallb/metallb)

<a name="cK6Do"></a>
## 二、安装Metallb
首先创建一个命名空间：
```bash
kubectl create ns metallb-system
```
然后通过远程的YAML创建服务：
```bash
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.9.4/manifests/metallb.yaml
# On first install only

```
创建一个secret：
```bash
kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)"
```
最后创建一个ConfigMap：
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 192.168.34.0-192.168.34.255
```
其中addresses需要写为自己虚拟机的网段。<br />如果是VMWare可以从“虚拟网络编辑器”这个地方查看：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604389103494-7f9cc168-dcb9-43ce-ae10-23d19004ef4d.png#align=left&display=inline&height=557&originHeight=557&originWidth=609&size=97831&status=done&style=none&width=609)<br />如果还是不清楚，从SSH地址栏截取前三段即可：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604389179750-42884689-931c-4184-913c-0509a371a3e9.png#align=left&display=inline&height=26&originHeight=26&originWidth=291&size=3033&status=done&style=none&width=291)

官网安装教程：[Installation By Manifest](https://metallb.universe.tf/installation/#installation-by-manifest)

<a name="Bi8Pk"></a>
## 三、使用Metallb
部署Metallb和Traefik（见下一篇文章）后，使用LoadBalancer应该就没问题了。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604389297399-8da194c5-4297-4bef-a4d1-943d936062fc.png#align=left&display=inline&height=677&originHeight=677&originWidth=1649&size=83524&status=done&style=none&width=1649)

在宿主机hosts中添加域名与负载均衡器的IP的映射：
```yaml
192.168.34.50    traefik.dashboard.com
```
:::info
注意这里的IP，不是虚拟机的IP，而是负载均衡器暴露出的外部Endpoint。
:::

HTTP测试：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604389350089-61d07b03-8588-49ce-a01c-d49ed5dbdca7.png#align=left&display=inline&height=353&originHeight=353&originWidth=788&size=31929&status=done&style=none&width=788)<br />HTTPS测试：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604389360467-593002dd-fa14-4b1f-9c5e-79a3f6635d07.png#align=left&display=inline&height=354&originHeight=354&originWidth=796&size=33041&status=done&style=none&width=796)

<a name="tkPE1"></a>
## 参考资料

- [Metallb介绍：一个开源的k8s LB](https://zhuanlan.zhihu.com/p/103717169)

