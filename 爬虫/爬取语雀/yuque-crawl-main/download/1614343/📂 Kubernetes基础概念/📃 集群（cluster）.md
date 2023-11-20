Kubernetes 将底层的计算资源连接在一起对外体现为一个计算集群，并将资源高度抽象化。部署应用时 Kubernetes 会以更高效的方式自动的将应用分发到集群内的机器上面，并调度运行。几个 Kubernetes 集群包含两种类型的资源：

- Master 节点：协调控制整个集群。
- Nodes 节点：运行应用的工作节点。

![](https://cdn.nlark.com/yuque/0/2020/svg/2213540/1597324442876-5da797ac-7506-42cf-bdff-137d60a75f5a.svg#align=left&display=inline&height=385&originHeight=385&originWidth=476&size=0&status=done&style=none&width=476)

**Master** 负责管理集群。 master 协调集群中的所有活动，例如调度应用程序、维护应用程序的所需状态、扩展应用程序和滚动更新。

**Node** 是 Kubernetes 集群中的工作机器，可以是物理机或虚拟机。 每个工作节点都有一个 Kubelet，它是管理 节点 并与 Kubernetes Master 节点进行通信的代理。节点 上还应具有处理容器操作的工作，例如 Docker 或 rkt。一个 Kubernetes 工作集群至少有三个节点。

当部署应用的时候，我们通知 Master 节点启动应用容器。然后 Master 会调度这些应用将它们运行在 Node 节点上面。Node 节点和 Master 节点通过 Master 节点暴露的 Kubernetes API 通信。当然我们也可以直接通过这些 API 和集群交互。

<a name="5c7af90e"></a>
## 节点 (Node)

Node 是 kubernetes 集群的工作节点，可以是物理机也可以是虚拟机。

Kubernetes 集群中的计算能力由 Node 提供，最初 Node 称为服务节点 Minion，后来改名为 Node。Kubernetes 集群中的 Node 也就等同于 Mesos 集群中的 Slave 节点，是所有 Pod 运行所在的工作主机，可以是物理机也可以是虚拟机。不论是物理机还是虚拟机，工作主机的统一特征是上面要运行 kubelet 管理节点上运行的容器。

<a name="c020f730"></a>
### Node 状态

Node 包括如下状态信息：

Node 作为集群中的工作节点，运行真正的应用程序，在 Node 上 Kubernetes 管理的最小运行单元是 Pod。Node 上运行着 Kubernetes 的 Kubelet、kube-proxy 服务进程，这些服务进程负责 Pod 的创建、启动、监控、重启、销毁、以及实现软件模式的负载均衡。

Node 包含的信息：

- Node 地址 (Address)：主机的 IP 地址，或 Node ID
   - HostName：可以被 kubelet 中的`--hostname-override`参数替代。
   - ExternalIP：可以被集群外部路由到的 IP 地址。
   - InternalIP：集群内部使用的 IP，集群外部无法访问。
- Condition
   - OutOfDisk：磁盘空间不足时为`True`
   - Ready：Node controller 40 秒内没有收到 node 的状态报告为`Unknown`，健康为`True`，否则为`False`。
   - MemoryPressure：当 node 有内存压力时为`True`，否则为`False`。
   - DiskPressure：当 node 有磁盘压力时为`True`，否则为`False`。
- Node 系统容量 (Capacity)：描述 Node 可用的系统资源，包括 CPU、内存、最大可调度 Pod 数量等
- Node 的运行状态 (Status)：Pending、Running、Terminated 三种状态
- Info：节点的一些版本信息，如 OS、kubernetes、docker 等
- 其他：内核版本号、Kubernetes 版本等。

<a name="1de382f8"></a>
### Node 管理

```bash
kubectl get nodes # 获取所有节点
kubectl describe node # 查看Node信息
kubectl cordon <node> # 禁止pod调度到该节点上
kubectl drain <node> # 驱逐该节点上的所有pod
```

`drain` 命令会删除该节点上的所有 Pod（DaemonSet 除外），在其他 node 上重新启动它们，通常该节点需要维护时使用该命令。直接使用该命令会自动调用`kubectl cordon <node>`命令。当该节点维护完成，启动了 kubelet 后，再使用`kubectl uncordon <node>`即可将该节点添加到 kubernetes 集群中。
