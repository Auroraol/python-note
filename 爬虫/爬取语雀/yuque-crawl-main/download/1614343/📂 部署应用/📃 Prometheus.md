<a name="bW9sf"></a>
## 一、Prometheus简介

Prometheus 是由 SoundCloud 开发的开源监控报警系统和时序列数据库(TSDB)。Prometheus 使用 Go 语言开发，是 Google BorgMon 监控系统的开源版本。

2016 年由 Google 发起 Linux 基金会旗下的原生云基金会(Cloud Native Computing Foundation), 将 Prometheus 纳入其下第二大开源项目。

Prometheus 目前在开源社区相当活跃。

Prometheus 和 Heapster (Heapster 是 K8S 的一个子项目，用于获取集群的性能数据。) 相比功能更完善、更全面。Prometheus 性能也足够支撑上万台规模的集群。

<a name="j8hZF"></a>
### Prometheus的特点

- 多维度数据模型。
- 灵活的查询语言。
- 不依赖分布式存储，单个服务器节点是自主的。
- 通过基于 HTTP 的 pull 方式采集时序数据。
- 可以通过中间网关进行时序列数据推送。
- 通过服务发现或者静态配置来发现目标服务对象。
- 支持多种多样的图表和界面展示，比如 Grafana 等。

<a name="65aa05f0"></a>
### Prometheus架构图
![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813683577-6c41d021-7b75-44d7-b0f4-14f641be0ab5.png#align=left&display=inline&height=801&originHeight=801&originWidth=1426&size=0&status=done&style=none&width=1426)

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813689855-3151d2c2-e594-4eea-8537-9d4032d164ef.png#align=left&display=inline&height=811&originHeight=811&originWidth=1351&size=0&status=done&style=none&width=1351)

<a name="1e079232"></a>
### Prometheus基本原理

Prometheus 的基本原理是通过 HTTP 协议周期性抓取被监控组件的状态，任意组件只要提供对应的 HTTP 接口就可以接入监控。不需要任何 SDK 或者其他的集成过程。这样做非常适合做虚拟化环境监控系统，比如 VM、Docker、Kubernetes 等。输出被监控组件信息的 HTTP 接口被叫做 exporter 。目前互联网公司常用的组件大部分都有 exporter 可以直接使用，比如 Varnish、Haproxy、Nginx、MySQL、Linux 系统信息(包括磁盘、内存、CPU、网络等等)。

<a name="8f543008"></a>
### Prometheus服务过程

- Prometheus Daemon 负责定时去目标上抓取 metrics(指标)数据，每个抓取目标需要暴露一个 http 服务的接口给它定时抓取。Prometheus 支持通过配置文件、文本文件、Zookeeper、Consul、DNS SRV Lookup 等方式指定抓取目标。Prometheus 采用 PULL 的方式进行监控，即服务器可以直接通过目标 PULL 数据或者间接地通过中间网关来 Push 数据。
- Prometheus 在本地存储抓取的所有数据，并通过一定规则进行清理和整理数据，并把得到的结果存储到新的时间序列中。
- Prometheus 通过 PromQL 和其他 API 可视化地展示收集的数据。Prometheus 支持很多方式的图表可视化，例如 Grafana、自带的 Promdash 以及自身提供的模版引擎等等。Prometheus 还提供 HTTP API 的查询方式，自定义所需要的输出。
- PushGateway 支持 Client 主动推送 metrics 到 PushGateway，而 Prometheus 只是定时去 Gateway 上抓取数据。
- Alertmanager 是独立于 Prometheus 的一个组件，可以支持 Prometheus 的查询语句，提供十分灵活的报警方式。

<a name="7288b976"></a>
### Prometheus三大套件

- Server 主要负责数据采集和存储，提供 PromQL 查询语言的支持。
- Alertmanager 警告管理器，用来进行报警。
- Push Gateway 支持临时性 Job 主动推送指标的中间网关。

<a name="xpQiW"></a>
## 二、安装Prometheus
添加仓库并更新：
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create namespace prometheus
```
部署Prometheus：
```bash
helm install prometheus prometheus-community/prometheus -n prometheus
```

部署完成，看到控制台打印：
```bash
NAME: prometheus
LAST DEPLOYED: Fri Oct 30 11:30:43 2020
NAMESPACE: prometheus
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The Prometheus server can be accessed via port 80 on the following DNS name from within your cluster:
prometheus-server.prometheus.svc.cluster.local


Get the Prometheus server URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace prometheus -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace prometheus port-forward $POD_NAME 9090


The Prometheus alertmanager can be accessed via port 80 on the following DNS name from within your cluster:
prometheus-alertmanager.prometheus.svc.cluster.local


Get the Alertmanager URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace prometheus -l "app=prometheus,component=alertmanager" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace prometheus port-forward $POD_NAME 9093
#################################################################################
######   WARNING: Pod Security Policy has been moved to a global property.  #####
######            use .Values.podSecurityPolicy.enabled with pod-based      #####
######            annotations                                               #####
######            (e.g. .Values.nodeExporter.podSecurityPolicy.annotations) #####
#################################################################################


The Prometheus PushGateway can be accessed via port 9091 on the following DNS name from within your cluster:
prometheus-pushgateway.prometheus.svc.cluster.local


Get the PushGateway URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace prometheus -l "app=prometheus,component=pushgateway" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace prometheus port-forward $POD_NAME 9091

For more information on running Prometheus, visit:
https://prometheus.io/
```

<a name="RPp8L"></a>
## 三、暴露Prometheus管理界面
首先在hosts中添加：
```bash
127.0.0.1    prometheus.dashboard.com
```
创建一个 IngressRoute：
```bash
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: prometheus-route
  namespace: prometheus
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`prometheus.dashboard.com`)
      kind: Rule
      services:
        - name: prometheus-server
          port: 80
```
应用即可：
```bash
kubectl apply -f prometheus/route.yaml
```
<br />
<a name="iy3eS"></a>
## 四、访问Prometheus管理界面
经过前面的一通操作，我们可以直接在浏览器中输入 [http://prometheus.dashboard.com](http://prometheus.dashboard.com/) 访问：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604048770461-76f2a5c8-72e8-46dd-bb99-7e47ed8e09e9.png#align=left&display=inline&height=518&originHeight=518&originWidth=1908&size=48153&status=done&style=none&width=1908)

[http://prometheus.dashboard.com/targets](http://prometheus.dashboard.com/targets)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604048844866-81616240-19d3-4c63-81e0-aa7e3713b001.png#align=left&display=inline&height=1001&originHeight=1001&originWidth=1911&size=150660&status=done&style=none&width=1911)

[http://prometheus.dashboard.com/service-discovery](http://prometheus.dashboard.com/service-discovery)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604049824579-14b4e673-b3d3-43d8-a2ac-9855d63698e2.png#align=left&display=inline&height=789&originHeight=789&originWidth=648&size=76129&status=done&style=none&width=648)

<a name="AlterManager"></a>
## AlterManager

Pormetheus 的警告由独立的两部分组成。

Prometheus 服务中的警告规则发送警告到 Alertmanager。

然后这个 Alertmanager 管理这些警告。包括 silencing, inhibition, aggregation，以及通过一些方法发送通知，例如：email，PagerDuty 和 HipChat。

建立警告和通知的主要步骤：

1. 创建和配置 Alertmanager
2. 启动 Prometheus 服务时，通过-alertmanager.url 标志配置 Alermanager 地址，以便 Prometheus 服务能和 Alertmanager 建立连接。

<a name="35808e79"></a>
## 参考资料

- [从零搭建 Prometheus 监控报警系统](https://www.cnblogs.com/chenqionghe/p/10494868.html)
- [Kubernetes学习之路（二十四）之Prometheus监控](https://www.cnblogs.com/linuxk/p/10582534.html)
