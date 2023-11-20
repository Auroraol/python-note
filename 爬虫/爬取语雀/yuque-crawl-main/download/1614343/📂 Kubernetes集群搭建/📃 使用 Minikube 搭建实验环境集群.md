本来不打算写这一篇的, 但是可能有童鞋只是想了解一下 Kubernetes 的使用而不是搭建生产环境使用的集群, 那么, 这可以用到 minikube 这个工具搭建实验环境的 Kubernetes 集群(说是集群, 其实只有一个 master 节点)

准备工作:

- BIOS 中开启 VT-X (如果是虚拟机注意设置)
- 科学上网 (由于 GFW)

<a name="virtualbox"></a>
## 一、virtualbox

Minikube 可以方便的在本地运行 Kubernetes 集群，方便日常开发，需要先安装 virtualBox 虚拟机。

**安装编译工具：**

```bash
yum update kernel -y # 升级内核
yum install kernel-headers kernel-devel-$(uname -r) gcc make perl -y # 安装编译工具
init 6 # 重启系统

# 重启后
uname -r # 查看内核
$ rpm -qa kernel\*
kernel-3.10.0-957.el7.x86_64
kernel-tools-3.10.0-957.el7.x86_64
kernel-tools-libs-3.10.0-957.el7.x86_64
kernel-headers-3.10.0-957.10.1.el7.x86_64
kernel-devel-3.10.0-957.10.1.el7.x86_64
kernel-devel-3.10.0-957.el7.x86_64
```

参考: [解决 centos7 找不到 kernel header](https://www.cnblogs.com/mylinux/p/5612168.html)

**安装 virtualbox：**

```bash
$ cat <<EOF > /etc/yum.repos.d/virtualbox.repo
[virtualbox]
name=Oracle Linux / RHEL / CentOS-\$releasever / \$basearch - VirtualBox
baseurl=http://download.virtualbox.org/virtualbox/rpm/el/\$releasever/\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=http://www.virtualbox.org/download/oracle_vbox.asc
EOF

# 安装virtualbox
yum install -y --enablerepo=virtualbox VirtualBox-5.2

# 设置virtualbox
sudo /sbin/vboxconfig
```

<a name="minikube"></a>
## 二、minikube

Kubernetes 提供了一个轻量级的 [Minikube](https://github.com/kubernetes/minikube) 应用，利用它我们可以很容器的创建一个只包含一个 Node 节点的 Kubernetes Cluster 用于日常的开发测试。

**方法一：直接使用 curl 安装**

```bash
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64 && \
  chmod +x minikube && \
  sudo mv minikube /usr/local/bin/
```

**方法二：使用 wget 先下载再安装**

下载地址：[GitHub binary](https://github.com/kubernetes/minikube/releases)

```bash
wget https://storage.googleapis.com/minikube/releases/v0.35.0/minikube-linux-amd64
mv minikube-linux-amd64 minikube && chmod +x minikube && cp minikube /usr/local/bin/
```

验证安装

```bash
minikube version
```

<a name="kubectl"></a>
## 三、kubectl

Minikube 要正常使用，还必须安装 kubectl，并且放在 PATH 里面。kubectl 是一个通过 Kubernetes API 和 Kubernetes 集群交互的命令行工具。

**方法一：使用 yum 安装**

官方镜像

```bash
$ cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
yum install -y --enablerepo=kubernetes kubectl
```

阿里云镜像

```bash
$ cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
yum install -y --enablerepo=kubernetes kubectl
```

**方法二：使用 wget 先下载再安装**

```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.5.1/bin/linux/amd64/kubectl
chmod +x kubectl
mv kubectl /usr/local/bin/kubectl
```

验证安装

```bash
kubectl version
```

<a name="b92650fb"></a>
## 四、换源拉取镜像

在进行下一步部署具体应用前我们先要做一件事情。Kubernetes 在部署容器应用的时候会先拉一个 pause 镜像，这个是一个基础容器，主要是负责网络部分的功能的，具体这里不展开讨论。最关键的是 Kubernetes 里面镜像默认都是从 Google 的镜像仓库拉的（就跟 docker 默认从 docker hub 拉的一样），但是因为 GFW 的原因，中国用户是访问不了 Google 的镜像仓库 gcr.io 的（如果你可以 ping 通，那恭喜你）。庆幸的是这个镜像被传到了 docker hub 上面，虽然中国用户访问后者也非常艰难，但通过一些加速器之类的还是可以 pull 下来的。如果没有 VPN 等科学上网的工具的话，可以先从 aliyuncs.com 中拉取 pause, 将其打上标签, 这样 Kubernetes VM 就不会从 gcr.io 拉镜像了，而是会直接使用本地的镜像。

```bash
minikube ssh # 登录到我们的Kubernetes VM里面去

# 从阿里云拉取容器
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.13.4
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:v1.13.4
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:v1.13.4
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:v1.13.4
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:3.2.24
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:1.2.6

# 将阿里云拉取的容器打标签
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.13.4 k8s.gcr.io/kube-apiserver:v1.13.4
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:v1.13.4 k8s.gcr.io/kube-controller-manager:v1.13.4
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:v1.13.4 k8s.gcr.io/kube-scheduler:v1.13.4
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:v1.13.4 k8s.gcr.io/kube-proxy:v1.13.4
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1 k8s.gcr.io/pause:3.1
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:3.2.24 k8s.gcr.io/etcd:3.2.24
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:1.2.6 k8s.gcr.io/coredns:1.2.6

# 删除阿里云拉取的容器
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver:v1.13.4
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager:v1.13.4
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler:v1.13.4
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy:v1.13.4
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.1
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/etcd:3.2.24
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:1.2.6

# 退出 minikube
exit
```

以后这种操作将成为常态，其实套路无非就是：

`换源(阿里云)拉取镜像`  - `重新打标签以符合k8s版本要求` - `删除之前换源拉取的镜像` 

<a name="dba6ef75"></a>
## 五、启动 minikube

启动 Kubernetes Cluster，这里使用的 driver 是 Virtualbox

```bash
$ minikube start --vm-driver=virtualbox
o   minikube v0.34.1 on linux (amd64)
>   Configuring local host environment ...
>   Creating none VM (CPUs=2, Memory=2048MB, Disk=20000MB) ...
-   "minikube" IP address is 172.17.0.70
-   Configuring Docker as the container runtime ...
-   Preparing Kubernetes environment ...
@   Downloading kubeadm v1.13.3
@   Downloading kubelet v1.13.3
-   Pulling images required by Kubernetes v1.13.3 ...
-   Launching Kubernetes v1.13.3 using kubeadm ...
-   Configuring cluster permissions ...
-   Verifying component health .....
+   kubectl is now configured to use "minikube"
=   Done! Thank you for using minikube!
```

<a name="925d4871"></a>
## 六、测试集群

查看集群信息

```bash
$ kubectl cluster-info
Kubernetes master is running at https://172.17.0.21:8443
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

查看当前可用的 Node, 使用 Minikube 创建的 cluster 只有一个 Node 节点

```bash
$ kubectl get nodes
NAME       STATUS   ROLES    AGE     VERSION
minikube   Ready    <none>   7m24s   v1.13.3
```

至此，我们已经用 Minikube 创建了一个简易的 Kubernetes Cluster。


