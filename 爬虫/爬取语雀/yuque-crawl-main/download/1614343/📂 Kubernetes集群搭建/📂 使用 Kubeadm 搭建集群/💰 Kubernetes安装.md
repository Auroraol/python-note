<a name="oVLx4"></a>
## 一、设置Kubernetes安装源
```bash
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup # 备份
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/docker-ce.repo https://download.docker.com/linux/centos/docker-ce.repo

$ cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```

执行下列命令刷新 yum 源缓存：
```bash
yum clean all
yum makecache
yum repolist
```

<a name="JIYrB"></a>
## 二、安装kubectl、kubelet、kubeadm
安装命令：
```bash
yum install -y kubectl kubelet kubeadm
```

系统会帮我们自动安装最新版的 kubeadm，包括 kubelet、kubeadm、kubectl、kubernetes-cni 这四个程序。

- **kubeadm**: k8s 集群的一键部署工具，通过把 k8s 的各类核心组件和插件以 pod 的方式部署来简化安装过程
- **kubelet**: 运行在每个节点上的 node agent，k8s 集群通过 kubelet 真正的去操作每个节点上的容器，由于需要直接操作宿主机的各类资源，所以没有放在 pod 里面，还是通过服务的形式装在系统里面
- **kubectl**: kubernetes 的命令行工具，通过连接 api-server 完成对于 k8s 的各类操作
- **kubernetes-cni**: k8s 的虚拟网络设备，通过在宿主机上虚拟一个 cni0 网桥，来完成 pod 之间的网络通讯，作用和 docker0 类似。

设置kubelet为开机启动：
```bash
systemctl enable kubelet
```

<a name="aae73512"></a>
## 三、部署 master 节点
<a name="3bdb3985"></a>
### 初始化 kubeadm
执行 `kubeadm init` 开始 master 节点的初始化工作
```bash
kubeadm init --pod-network-cidr=10.244.0.0/16
```

注意这边的 `--pod-network-cidr=10.244.0.0/16`，是 k8s 的网络插件所需要用到的配置信息，用来给 node 分配子网段，上面用到的网络插件是 [flannel](https://github.com/coreos/flannel/blob/master/Documentation/kubernetes.md)，就是这么配，其他的插件也有相应的配法，官网上都有详细的说明，具体参考[这个网页](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)。

如果卡在 `kubeadm config images pull` 这一步，说明k8s相关的镜像没有拉取成功。
```bash
[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
```
可以事先拉取好镜像，或者设置 `--image-repository`  从阿里源拉取镜像（网络插件为 calico）：
```bash
kubeadm init --kubernetes-version=1.19.3  \
--apiserver-advertise-address=192.168.34.128   \
--image-repository registry.aliyuncs.com/google_containers  \
--service-cidr=10.10.0.0/16 --pod-network-cidr=10.122.0.0/16
```

<a name="87c8281c"></a>
### 初始化检测
初始化的时候 kubeadm 会做一系列的校验，以检测你的服务器是否符合 kubernetes 的安装条件，检测结果分为[WARNING]和[ERROR]两种，类似如下的信息:
```bash
CGROUPS_MEMORY: enabled
  [WARNING Hostname]: hostname "k8s-master" could not be reached
  [WARNING Hostname]: hostname "k8s-master": lookup k8s-master on 192.168.126.2:53: no such host
  [WARNING Service-Kubelet]: kubelet service is not enabled, please run 'systemctl enable kubelet.service'
error execution phase preflight: [preflight] Some fatal errors occurred:
  [ERROR CRI]: container runtime is not running: output: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
, error: exit status 1
  [ERROR Service-Docker]: docker service is not active, please run 'systemctl start docker.service'
  [ERROR FileContent--proc-sys-net-bridge-bridge-nf-call-iptables]: /proc/sys/net/bridge/bridge-nf-call-iptables does not exist
  [ERROR FileContent--proc-sys-net-ipv4-ip_forward]: /proc/sys/net/ipv4/ip_forward contents are not set to 1
  [ERROR Swap]: running with swap on is not supported. Please disable swap
  [ERROR SystemVerification]: failed to get docker info: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
[preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`
```

- `[WARNING]` 的有比如 docker 服务没设置成自动启动啦，docker 版本不符合兼容性要求啦，hostname 设置不规范之类，这些一般问题不大，不影响安装，当然尽量你按照它提示的要求能改掉是最好。
- `[ERROR]` 的话就要重视，虽然可以通过 `--ignore-preflight-errors` 忽略错误强制安装，但为了不出各种奇怪的毛病，所以强烈建议 error 的问题一定要解决了再继续执行下去。

第一次启动时基本都不能顺利启动, 修复好所有的错误后, 再次执行就可以了。我将大部分常用的错误列举成单独的一个部分, 参考 [启动时常见错误修复](https://www.yuque.com/xiaoyulive/kubernetes/amf0gt)

<a name="47259151"></a>
### 初始化成功
重新执行 `kubeadm init`, 初始化成功后，会提示：
```bash
$ kubeadm init --pod-network-cidr=10.244.0.0/16
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.34.128:6443 --token ebpu3f.pl7roaj6n18ht4at \
    --discovery-token-ca-cert-hash sha256:2479b3359f98641fabe7557f1fb82683d01aab5150c7862ebefb3d3e7361ae7b
```

可以看到终于初始化成功了，kudeadm 帮你做了大量的工作，包括 kubelet 配置、各类证书配置、kubeconfig 配置、插件安装等等（这些东西自己搞不知道要搞多久，反正估计用过 kubeadm 没人会再愿意手工安装了）。注意最后一行，kubeadm 提示你，其他节点需要加入集群的话，只需要执行这条命令就行了，里面包含了加入集群所需要的 token。同时 kubeadm 还提醒你，要完成全部安装，还需要安装一个网络插件 `kubectl apply -f [podnetwork].yaml`。

同时也提示需要执行：
```bash
mkdir -p $HOME/.kube
sudo \cp /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

把相关配置信息拷贝入.kube 的目录，这个是用来配置 kubectl 和 api-server 之间的认证，其他 node 节点的话需要将此配置信息拷贝入 node 节点的对应目录。此时我们执行一下：
```bash
$ kubectl get nodes
NAME         STATUS     ROLES    AGE    VERSION
k8s-master   NotReady   master   9m8s   v1.19.3
```

显示目前节点是 notready 状态，因为还缺少网络插件。

如果初始化过程出现问题，使用如下命令重置：
```bash
kubeadm reset
rm -rf /var/lib/cni/ $HOME/.kube/config
```

默认的 master 节点是不能调度应用 pod 的，所以我们还需要给 master 节点打一个污点标记
```bash
kubectl taint nodes --all node-role.kubernetes.io/master-
```

<a name="afweb"></a>
### 脚本封装
操作很繁琐，将基本的命令封装成一个脚本：<br />`start-k8s.sh`
```bash
$ touch start-k8s.sh && chmod 744 start-k8s.sh && vim start-k8s.sh
systemctl enable docker
systemctl start docker
rm -rf /etc/kubernetes/manifests
rm -rf /var/lib/etcd
systemctl stop firewalld
systemctl disable firewalld
swapoff -a
echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
echo 1 > /proc/sys/net/ipv4/ip_forward
kubeadm reset
kubeadm init --pod-network-cidr=10.244.0.0/16
kubectl taint nodes --all node-role.kubernetes.io/master-
```

初始化后的操作也可封装为一个脚本：<br />`k8s-init.sh`
```bash
$ touch k8s-init.sh && chmod 744 k8s-init.sh && vim k8s-init.sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

<a name="dBepf"></a>
## 四、安装网络插件
上面说到，由于还缺少网络插件，因此节点当前还不可用，处于NotReady状态。

根据初始化集群的时候说选择的网络插件，安装对应的网络插件即可。

下面简单说一下上文中提及的calico和flannel插件的安装。

<a name="Rn2Vr"></a>
### calico
安装命令：
```
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

稍等几分钟，再次查看节点，发现已经处于Ready状态了：
```bash
$ kubectl get node
NAME                STATUS   ROLES    AGE     VERSION
master01.paas.com   Ready    master   5m47s   v1.19.3

$ kubectl get pods -n kube-system
NAME                                            READY   STATUS    RESTARTS   AGE
calico-kube-controllers-7d569d95-9rcmr          1/1     Running   0          3h16m
calico-node-hpl8x                               1/1     Running   0          3h16m
coredns-6d56c8448f-d2jhc                        1/1     Running   0          3h26m
coredns-6d56c8448f-qj4hc                        1/1     Running   0          3h26m
etcd-localhost.localdomain                      1/1     Running   0          3h27m
kube-apiserver-localhost.localdomain            1/1     Running   1          3h27m
kube-controller-manager-localhost.localdomain   1/1     Running   6          3h27m
kube-proxy-pjt2n                                1/1     Running   0          3h26m
kube-scheduler-localhost.localdomain            1/1     Running   7          3h27m
```

<a name="10c71d3d"></a>
### flannel
换源拉取镜像：
```bash
docker pull registry.cn-shenzhen.aliyuncs.com/cp_m/flannel:v0.10.0-amd64
docker tag registry.cn-shenzhen.aliyuncs.com/cp_m/flannel:v0.10.0-amd64 quay.io/coreos/flannel:v0.10.0-amd64
docker rmi registry.cn-shenzhen.aliyuncs.com/cp_m/flannel:v0.10.0-amd64
```

安装 flannel
```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml
```

安装完之后我们再看一下 pod 的状态
```bash
$ kubectl get pods -n kube-system
NAME                                 READY   STATUS    RESTARTS   AGE
coredns-86c58d9df4-284kz             1/1     Running   0          24m
coredns-86c58d9df4-mlxjl             1/1     Running   0          24m
etcd-k8s-master                      1/1     Running   0          23m
kube-apiserver-k8s-master            1/1     Running   0          23m
kube-controller-manager-k8s-master   1/1     Running   0          23m
kube-flannel-ds-amd64-d4bbn          1/1     Running   0          24m
kube-proxy-fcjtg                     1/1     Running   0          24m
kube-scheduler-k8s-master            1/1     Running   0          23m
```

可以看到 coredns 的两个 pod 都已经启动，同时还多了一个 kube-flannel-ds-amd64-d4bbn，这正是我们刚才安装的网络插件 flannel。

如果 kube-flannel-ds-amd64-d4bbn 的状态为 `ImagePullBackOff`, 则说明拉取镜像失败, 需要换源拉取, 参看上面的 "换源拉取镜像" 解决。

这时候我们再来看一下核心组件的状态：
```bash
$ kubectl get componentstatus
NAME                 STATUS    MESSAGE              ERROR
scheduler            Healthy   ok
controller-manager   Healthy   ok
etcd-0               Healthy   {"health": "true"}
```

可以看到组件的状态都已经 ok 了，我们再看看 node 的状态
```bash
$ kubectl get node
NAME         STATUS   ROLES    AGE   VERSION
k8s-master   Ready    master   32m   v1.14.2
```

node 的状态是 Ready，说明我们的 master 安装成功，至此大功告成！

如果在配置过程中有任何错误, 比如 `kube-flannel-ds-amd64-d4bbn` 出错, 可以使用以下命令查看错误 (比如会有拉取镜像错误):
```bash
kubectl describe pod kube-flannel-ds-amd64-d4bbn --namespace=kube-system
```

<a name="b01b051a"></a>
## 五、k8s 核心组件介绍

前面介绍过，kudeadm 的思路，是通过把 k8s 主要的组件容器化，来简化安装过程。这时候你可能就有一个疑问，这时候 k8s 集群还没起来，如何来部署 pod？难道直接执行 docker run？当然是没有那么 low，其实在 kubelet 的运行规则中，有一种特殊的启动方法叫做“静态 pod”（static pod），只要把 pod 定义的 yaml 文件放在指定目录下，当这个节点的 kubelet 启动时，就会自动启动 yaml 文件中定义的 pod。从这个机制你也可以发现，为什么叫做 static pod，因为这些 pod 是不能调度的，只能在这个节点上启动，并且 pod 的 ip 地址直接就是宿主机的地址。在 k8s 中，放这些预先定义 yaml 文件的位置是 `/etc/kubernetes/manifests`，我们来看一下：
```bash
$ ll
总用量 16
-rw-------. 1 root root 1999 1月  12 01:35 etcd.yaml
-rw-------. 1 root root 2674 1月  12 01:35 kube-apiserver.yaml
-rw-------. 1 root root 2547 1月  12 01:35 kube-controller-manager.yaml
-rw-------. 1 root root 1051 1月  12 01:35 kube-scheduler.yaml
```

以下四个就是 k8s 的核心组件了，以静态 pod 的方式运行在当前节点上

- **etcd**: k8s 的数据库，所有的集群配置信息、密钥、证书等等都是放在这个里面
- **kube-apiserver**: 提供了 HTTP restful api 接口的关键服务进程, 是 kubernetes 里所有资源的增删改查等操作的唯一入口, 也是集群的入口进程，所有其他的组件都是通过 apiserver 来操作 kubernetes 的各类资源
- **kube-controller-manager**: 负责管理容器 pod 的生命周期, kubernetes 里的所有资源对象的自动化控制中心, 可以理解为资源对象的"大总管"
- **kube-scheduler**: 负责 pod 在集群中的调度, 相当于公交公司的"调度室"

具体操作来说，在之前的文章中已经介绍过，docker 架构调整后，已经拆分出 containerd 组件，所以现在是 kubelet 直接通过 cri-containerd 来调用 containerd 进行容器的创建（不走 docker daemon 了），从进程信息里面可以看出

```bash
$ ps -ef | grep containerd
root      3075     1  0 00:29 ?        00:00:55 /usr/bin/containerd
root      4740  3075  0 01:35 ?        00:00:01 containerd-shim -namespace moby -workdir /var/lib/containerd/io.containerd.runtime.v1.linux/moby/ec93247aeb737218908557f825344b33dd58f0c098bd750c71da1bc0ec9a49b0 -address /run/containerd/containerd.sock -containerd-binary /usr/bin/containerd -runtime-root /var/run/docker/runtime-runc
root      4754  3075  0 01:35 ?        00:00:01 containerd-shim -namespace moby -workdir /var/lib/containerd/io.containerd.runtime.v1.linux/moby/f738d56f65b9191a63243a1b239bac9c3924b5a2c7c98e725414c247fcffbb8f -address /run/containerd/containerd.sock -containerd-binary /usr/bin/containerd -runtime-root /var/run/docker/runtime-runc
root      4757  3
```

其中 3075 这个进程就是由 docker 服务启动时带起来的 containerd daemon，4740 和 4754 是由 containerd 进程创建的 cotainerd-shim 子进程，用来真正的管理容器进程。多说一句，之前的 docker 版本这几个进程名字分别叫 docker-containerd，docker-cotainerd-shim，docker-runc, 现在的进程名字里面已经完全看不到 docker 的影子了，去 docker 化越来越明显了。

<a name="7c543542"></a>
### k8s 插件(addon)

- **CoreDNS**: cncf 项目，主要是用来做服务发现，目前已经取代 kube-dns 作为 k8 默认的服务发现组件
- **kube-proxy**: 基于 iptables 来做的负载均衡，service 会用到，这个性能不咋地，知道一下就好

我们执行一下

```bash
$ kubectl get pods -n kube-system
NAME                                      READY   STATUS    RESTARTS   AGE
coredns-86c58d9df4-284kz                  0/1     Pending   0          5m28s
coredns-86c58d9df4-mlxjl                  0/1     Pending   0          5m28s
etcd-miwifi-r1cm-srv                      1/1     Running   0          4m40s
kube-apiserver-miwifi-r1cm-srv            1/1     Running   0          4m52s
kube-controller-manager-miwifi-r1cm-srv   1/1     Running   0          5m3s
kube-proxy-fcjtg                          1/1     Running   0          5m28s
kube-scheduler-miwifi-r1cm-srv            1/1     Running   0          4m45s
```

可以看到 kubeadm 帮我们安装的，就是我上面提到的那些组件，并且都是以 pod 的形式安装。同时你也应该注意到了，coredns 的两个 pod 都是 pending 状态，这是因为网络插件还没有安装。我们根据前面提到的官方页面的说明安装网络插件，这边我用到的是 flannel，安装方式也很简单，标准的 k8s 式的安装

<a name="5a2524a7"></a>
## 六、部署其他节点
其他节点同样地安装 `docker-ce` 与 `kubeadm`, 并执行 `kubeadm join` (`k8s-master` 中 `kubeadm init` 正确初始化后可以看到) 即可加入到 `k8s-master` 所在的集群中

node 节点加入：
```bash
kubeadm join 192.168.1.128:6443 --token xmjhe9.vfhu0lt3a4cf8xnb --discovery-token-ca-cert-hash sha256:9b39f76a0eddd78c3ffa193b16ae579763f4e99f3301b53aaab1b39386dd0851
```

其中 token 是创建的时候生成的, 如果忘记了 token，可以使用以下命令找回：
```bash
$ kubeadm token list
TOKEN                     TTL       EXPIRES                     USAGES                   DESCRIPTION                                                EXTRA GROUPS
x98t7l.u0xh25qeuxcvkgi2   23h       2019-08-15T21:46:52+08:00   authentication,signing   The default bootstrap token generated by 'kubeadm init'.   system:bootstrappers:kubeadm:default-node-token
```

部署好所有节点，在 k8s-master 节点查看部署情况：
```bash
$ ksys get nodes
NAME         STATUS   ROLES    AGE     VERSION
k8s-master1   Ready    master   75d    v1.14.2
k8s-node1     Ready    <none>   75d    v1.14.2
k8s-node2     Ready    <none>   75d    v1.14.2
k8s-node3     Ready    <none>   75d    v1.14.2
k8s-node4     Ready    <none>   75d    v1.14.2
```

<a name="CTn84"></a>
## 七、相关配置
<a name="31516ba3"></a>
### token过期后重新生成
如果后期有更多节点加入，token 可能会过期, 通过以下方式重新生成 token 即可
```bash
$ kubeadm token create
[kubeadm] WARNING: starting in 1.8, tokens expire after 24 hours by default (if you require a non-expiring token use --ttl 0)
aa78f6.8b4cafc8ed26c34f

$ kubeadm token list
TOKEN                     TTL       EXPIRES                     USAGES                   DESCRIPTION   EXTRA GROUPS
aa78f6.8b4cafc8ed26c34f   23h       2017-12-26T16:36:29+08:00   authentication,signing   <none>        system:bootstrappers:kubeadm:default-node-token
```

获取 ca 证书 sha256 编码 hash 值
```bash
$ openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
0fd95a9bc67a7bf0ef42da968a0d55d92e52898ec37c971bd77ee501d845b538
```

之后使用 `kubeadm join` 的时候带上最新的 token 和 ca 证书即可。

<a name="EF3xE"></a>
## 参考资料

- [使用kubeadm在Centos8上部署kubernetes1.18](https://www.kubernetes.org.cn/7189.html)
- [kubernetes部署dashboard可视化插件](https://blog.csdn.net/networken/article/details/85607593)

