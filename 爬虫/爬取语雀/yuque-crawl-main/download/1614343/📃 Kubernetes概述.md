![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599806751765-35d84049-3f73-47d4-985c-235f3d2a5f22.png#align=left&display=inline&height=600&originHeight=1500&originWidth=1000&size=0&status=done&style=none&width=400)<br />

- [Kubernetes 官网](https://kubernetes.io/)
- [Kubernetes 中文网](https://kubernetes.io/zh/)
- [Kubernetes 中文文档](http://docs.kubernetes.org.cn/)
- [Kubernetes 中文社区](https://www.kubernetes.org.cn/docs)

<a name="dcqEc"></a>
## 一、什么是Kubernetes

**Kubernetes**的名字来自希腊语，意思是“_舵手” _或 “_领航员”_。_K8s_是将8个字母“ubernete”替换为“8”的缩写。

Kubernetes是容器集群管理系统，是一个开源的平台，可以实现容器集群的自动化部署、自动扩缩容、维护等功能。

通过Kubernetes你可以：

- 快速部署应用
- 快速扩展应用
- 无缝对接新的应用功能
- 节省资源，优化硬件资源的使用

我们的目标是促进完善组件和工具的生态系统，以减轻应用程序在公有云或私有云中运行的负担。

<a name="HdBqf"></a>
## 二、Kubernetes 特点
<br />

- **可移植**: 支持公有云，私有云，混合云，多重云（multi-cloud）
- **可扩展**: 模块化, 插件化, 可挂载, 可组合
- **自动化**: 自动部署，自动重启，自动复制，自动伸缩/扩展

Kubernetes是Google 2014年创建管理的，是Google 10多年大规模容器管理技术Borg的开源版本。

<a name="nnkJO"></a>
## 三、使用Kubernetes能做什么

可以在物理或虚拟机的Kubernetes集群上运行容器化应用，Kubernetes能提供一个以“**容器为中心的基础架构**”，满足在生产环境中运行应用的一些常见需求，如：

- 多个进程（作为容器运行）协同工作。（Pod）
- 存储系统挂载
- Distributing secrets
- 应用健康检测
- 应用实例的复制
- Pod自动伸缩/扩展
- Naming and discovering
- 负载均衡
- 滚动更新
- 资源监控
- 日志访问
- 调试应用程序
- 提供认证和授权

<a name="c77bb373"></a>
## 四、Kubernetes 的架构

![](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1597324062823-8e70963a-b06f-42d7-b6f4-6c0618b85aad.jpeg#align=left&display=inline&height=1080&originHeight=1080&originWidth=1785&size=0&status=done&style=none&width=1785)<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597324086697-712d7868-8560-47af-9b7c-c4cfd6a74d79.png#align=left&display=inline&height=1984&originHeight=1984&originWidth=2409&size=0&status=done&style=none&width=2409)

<a name="deugJ"></a>
### Master 和 Node

Kubernetes 将集群中的机器划分为一个 Master 节点和一群工作节点（Node）。其中，Master 节点上运行着集群管理相关的一组进程 etcd、API Server、Controller Manager、Scheduler，后三个组件构成了 Kubernetes 的总控中心，这些进程实现了整个集群的资源管理、Pod 调度、弹性伸缩、安全控制、系统监控和纠错等管理功能，并且全都是自动完成。在每个 Node 上运行 Kubelet、Proxy、Docker daemon 三个组件，负责对本节点上的 Pod 的生命周期进行管理，以及实现服务代理的功能。

<a name="QU9Or"></a>
### etcd

用于持久化存储集群中所有的资源对象，如 Node、Service、Pod、RC、Namespace 等；API Server 提供了操作 etcd 的封装接口 API，这些 API 基本上都是集群中资源对象的增删改查及监听资源变化的接口。

<a name="Cyn2v"></a>
### API Server

提供了资源对象的唯一操作入口，其他所有组件都必须通过它提供的 API 来操作资源数据，通过对相关的资源数据“全量查询”+“变化监听”，这些组件可以很“实时”地完成相关的业务功能。

API Server 内部有一套完备的安全机制，包括认证、授权和准入控制等相关模块

<a name="DYmbF"></a>
### Controller Manager

集群内部的管理控制中心，其主要目的是实现 Kubernetes 集群的故障检测和恢复的自动化工作，比如根据 RC 的定义完成 Pod 的复制或移除，以确保 Pod 实例数符合 RC 副本的定义；根据 Service 与 Pod 的管理关系，完成服务的 Endpoints 对象的创建和更新；其他诸如 Node 的发现、管理和状态监控、死亡容器所占磁盘空间及本地缓存的镜像文件的清理等工作也是由 Controller Manager 完成的。

<a name="2I6wh"></a>
### Scheduler

Scheduler 是集群分发调度器，负责 Pod 在集群节点中的调度分配。具体工作包括:

- Scheduler 收集和分析当前 Kubernetes 集群中所有 Minion/Node 节点的资源(内存、CPU)负载情况，然后依此分发新建的 Pod 到 Kubernetes 集群中可用的节点。
- 实时监测 Kubernetes 集群中未分发和已分发的所有运行的 Pod。
- Scheduler 也监测 Minion/Node 节点信息，由于会频繁查找 Minion/Node 节点，Scheduler 会缓存一份最新的信息在本地。
- Scheduler 在分发 Pod 到指定的 Minion/Node 节点后，会把 Pod 相关的信息 Binding 写回 API Server。

<a name="GH5Zl"></a>
### Kubelet

Kubelet 可以看做节点上的 Pod 管家, 负责本 Node 节点上的 Pod 的创建、修改、监控、删除等全生命周期管理，同时 Kubelet 定时“上报”本 Node 的状态信息到 API Server 里。

kubelet 是 Master API Server 和 Node 之间的桥梁，接收 Master API Server 分配给它的 commands 和 work，通过 kube-apiserver 间接与 Etcd 集群交互，读取配置信息。

具体的工作如下：

- 设置容器的环境变量、给容器绑定 Volume、给容器绑定 Port、根据指定的 Pod 运行一个单一容器、给指定的 Pod 创建 network 容器。
- 同步 Pod 的状态、同步 Pod 的状态、从 cAdvisor 获取 container info、 pod info、 root info、 machine info。
- 在容器中运行命令、杀死容器、删除 Pod 的所有容器。

<a name="ac14W"></a>
### Proxy

实现了 Service 的代理与软件模式的负载均衡器。

客户端通过 Kubectl 命令行工具或 Kubectl Proxy 来访问 Kubernetes 系统，在 Kubernetes 集群内部的客户端可以直接使用 Kuberctl 命令管理集群。Kubectl Proxy 是 API Server 的一个反向代理，在 Kubernetes 集群外部的客户端可以通过 Kubernetes Proxy 来访问 API Server。

Proxy 是为了解决外部网络能够访问跨机器集群中容器提供的应用服务而设计的，运行在每个 Minion 上。Proxy 提供 TCP/UDP sockets 的 proxy，每创建一种 Service，Proxy 主要从 etcd 获取 Services 和 Endpoints 的配置信息（也可以从 file 获取），然后根据配置信息在 Minion 上启动一个 Proxy 的进程并监听相应的服务端口，当外部请求发生时，Proxy 会根据 Load Balancer 将请求分发到后端正确的容器处理。

所以 Proxy 不但解决了同一主宿机相同服务端口冲突的问题，还提供了 Service 转发服务端口对外提供服务的能力，Proxy 后端使用了随机、轮循负载均衡算法。

<a name="9aWkt"></a>
## 参考资料

- [Kubernetes 是什么](http://docs.kubernetes.org.cn/227.html)
- [Kubernetes 组件](http://docs.kubernetes.org.cn/230.html)

