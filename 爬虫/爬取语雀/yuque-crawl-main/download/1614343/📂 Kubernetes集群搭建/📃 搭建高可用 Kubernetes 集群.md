前面的文章，我们使用Kubeadm在虚拟机中搭建了实验环境的Kubernetes集群，而实际生产环境中，往往要求会比这高得多。下面我们需要在真实的物理机上搭建（本人使用了8台阿里云的服务器）。

先看看架构图：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599809147399-1b711a5f-20ad-4a8b-959e-2bbed628aeb8.png#align=left&display=inline&height=578&originHeight=578&originWidth=640&size=0&status=done&style=none&width=640)<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599809160857-19a4b724-455f-4c89-b475-803dad19cc6d.png#align=left&display=inline&height=560&originHeight=663&originWidth=883&size=0&status=done&style=none&width=746)
<a name="e3c2b7d4"></a>
## 一、部署准备

- BIOS 中开启 VT-X (如果是虚拟机注意设置)
- 科学上网 (由于 GFW)

在阿里云中配置 8 台 CentOS 物理机, 3 台 master, 4 台 node, 1台lb, （IP为我写文章时胡诌的，根据自己的机子IP来配置） 分别为：

- 192.168.1.140 k8s-master-lb (VIP)
- 192.168.1.128 k8s-master1 (4 核 8GB)
- 192.168.1.129 k8s-master2 (4 核 8GB)
- 192.168.1.130 k8s-master3 (4 核 8GB)
- 192.168.1.131 k8s-node1 (4 核 4GB)
- 192.168.1.132 k8s-node2 (4 核 4GB)
- 192.168.1.133 k8s-node3 (4 核 4GB)
- 192.168.1.134 k8s-node4 (4 核 4GB)

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599810137803-bc2edf13-9b0a-4188-827a-3613d8340d33.png#align=left&display=inline&height=881&originHeight=881&originWidth=1902&size=0&status=done&style=none&width=1902)

并在自己本地的客户机中将 `192.168.1.140 k8s-master-lb` 加入 hosts，以便访问。

<a name="4FEKn"></a>
### 主机互信

所有节点配置 hosts, 使三台机子能够互通

```bash
$ cat <<EOF >> /etc/hosts
192.168.1.128 k8s-master1
192.168.1.129 k8s-master2
192.168.1.130 k8s-master3
192.168.1.131 k8s-node1
192.168.1.132 k8s-node2
192.168.1.133 k8s-node3
192.168.1.134 k8s-node4
EOF
```

SSH 证书分发

```bash
ssh-keygen -t rsa
for i in k8s-master1 k8s-master2 k8s-master3 k8s-node1 k8s-node2 k8s-node3 k8s-node4 k8s-node5;do ssh-copy-id -i .ssh/id_rsa.pub $i;done
```

测试互通性:

```bash
ping k8s-master1
# 或
ssh k8s-master1
```

<a name="iEwIx"></a>
## 二、开始部署

<a name="mg0My"></a>
### 使用 k8s-ha-install

有大佬将部署高可用 k8s 写成了自动化脚本: [k8s-ha-install](https://github.com/dotbalo/k8s-ha-install)

```bash
git clone https://github.com/dotbalo/k8s-ha-install.git -b v1.13.x
```

以下的操作都在 `k8s-ha-install` 目录下执行

修改 `create-config.sh`, 将以下变量修改为自己的, 比如我自己的:

```bash
#!/bin/bash

#######################################
# set variables below to create the config files, all files will create at ./config directory
#######################################

# master keepalived virtual ip address
export K8SHA_VIP=192.168.1.140

# master1 ip address
export K8SHA_IP1=192.168.1.128

# master2 ip address
export K8SHA_IP2=192.168.1.129

# master3 ip address
export K8SHA_IP3=192.168.1.130

# master keepalived virtual ip hostname
export K8SHA_VHOST=k8s-master-lb

# master1 hostname
export K8SHA_HOST1=k8s-master1

# master2 hostname
export K8SHA_HOST2=k8s-master2

# master3 hostname
export K8SHA_HOST3=k8s-master3

# master1 network interface name
export K8SHA_NETINF1=ens33

# master2 network interface name
export K8SHA_NETINF2=ens33

# master3 network interface name
export K8SHA_NETINF3=ens33

# keepalived auth_pass config
export K8SHA_KEEPALIVED_AUTH=412f7dc3bfed32194d1600c483e10ad1d

# calico reachable ip address 服务器网关地址
export K8SHA_CALICO_REACHABLE_IP=192.168.1.1

# kubernetes CIDR pod subnet, if CIDR pod subnet is "172.168.0.0/16" please set to "172.168.0.0"
export K8SHA_CIDR=172.168.0.0
```

将 k8s 版本改为自己的版本(好几个地方, 全部都要改), 比如我的是 v1.14.2:

```bash
kubernetesVersion: v1.13.2

# 改为
kubernetesVersion: v1.14.2
```

修改完成之后执行:

```bash
$ ./create-config.sh
create kubeadm-config.yaml files success. config/k8s-master1/kubeadm-config.yaml
create kubeadm-config.yaml files success. config/k8s-master2/kubeadm-config.yaml
create kubeadm-config.yaml files success. config/k8s-master3/kubeadm-config.yaml
create keepalived files success. config/k8s-master1/keepalived/
create keepalived files success. config/k8s-master2/keepalived/
create keepalived files success. config/k8s-master3/keepalived/
create nginx-lb files success. config/k8s-master1/nginx-lb/
create nginx-lb files success. config/k8s-master2/nginx-lb/
create nginx-lb files success. config/k8s-master3/nginx-lb/
create calico.yaml file success. calico/calico.yaml
```

可以看到自动创建了很多文件, 然后将这些文件进行分发:

```bash
# 设置相关hostname变量
export HOST1=k8s-master1
export HOST2=k8s-master2
export HOST3=k8s-master3

# 把kubeadm配置文件放到各个master节点的/root/目录
scp -r config/$HOST1/kubeadm-config.yaml $HOST1:/root/
scp -r config/$HOST2/kubeadm-config.yaml $HOST2:/root/
scp -r config/$HOST3/kubeadm-config.yaml $HOST3:/root/

# 把keepalived配置文件放到各个master节点的/etc/keepalived/目录
scp -r config/$HOST1/keepalived/* $HOST1:/etc/keepalived/
scp -r config/$HOST2/keepalived/* $HOST2:/etc/keepalived/
scp -r config/$HOST3/keepalived/* $HOST3:/etc/keepalived/

# 把nginx负载均衡配置文件放到各个master节点的/root/目录
scp -r config/$HOST1/nginx-lb $HOST1:/root/
scp -r config/$HOST2/nginx-lb $HOST2:/root/
scp -r config/$HOST3/nginx-lb $HOST3:/root/
```

<a name="d1667ca9"></a>
### nginx-lb 配置

在所有 master 节点执行

```bash
cd
docker-compose --file=/root/nginx-lb/docker-compose.yaml up -d
docker-compose --file=/root/nginx-lb/docker-compose.yaml ps
```

<a name="9823T"></a>
### keepalived 配置

在所有 master 节点修改以下文件:

```bash
$ vim /etc/keepalived/keepalived.conf
! Configuration File for keepalived
global_defs {
    router_id LVS_DEVEL
}
#vrrp_script chk_apiserver {
#    script "/etc/keepalived/check_apiserver.sh"
#    interval 2
#    weight -5
#    fall 3
#    rise 2
#}
vrrp_instance VI_1 {
    state MASTER
    interface ens160
    mcast_src_ip 192.168.1.128
    virtual_router_id 51
    priority 102
    advert_int 2
    authentication {
        auth_type PASS
        auth_pass 412f7dc3bfed32194d1600c483e10ad1d
    }
    virtual_ipaddress {
        192.168.1.140
    }
    track_script {
       chk_apiserver
    }
}
```

修改的地方:

- 注释了 `vrrp_script` 部分
- `mcast_src_ip` 配置为各个 master 节点的 IP
- `virtual_ipaddress` 配置为 VIP

然后重启服务:

```bash
systemctl restart keepalived
```

测试 VIP 是否可以访问得通, 一定要通才能进行下一步:

```bash
ping 192.168.1.140 -c 4
```

注意步骤, 必须先执行 nginx-lb 相关的操作, 再注释`keepalived.conf`相关部分, 再重启 keepalived !!!

<a name="ei55s"></a>
### 启动主节点

配置好之后, 提前下载镜像(所有节点都需执行):

```bash
kubeadm config images pull --config /root/kubeadm-config.yaml
```

然后启动 k8s-master1:

```bash
kubeadm init --config /root/kubeadm-config.yaml
```

查看当前启动的节点

```bash
$ kubectl get nodes
NAME           STATUS     ROLES    AGE     VERSION
k8s-master1   NotReady   master   2m11s   v1.14.2
```

<a name="39mlS"></a>
### 证书分发
启动成功后, 分发 kubernetes 证书到各个 master 节点

```bash
USER=root
CONTROL_PLANE_IPS="k8s-master2 k8s-master3"
for host in $CONTROL_PLANE_IPS; do
    ssh "${USER}"@$host "mkdir -p /etc/kubernetes/pki/etcd"
    scp /etc/kubernetes/pki/ca.crt "${USER}"@$host:/etc/kubernetes/pki/ca.crt
    scp /etc/kubernetes/pki/ca.key "${USER}"@$host:/etc/kubernetes/pki/ca.key
    scp /etc/kubernetes/pki/sa.key "${USER}"@$host:/etc/kubernetes/pki/sa.key
    scp /etc/kubernetes/pki/sa.pub "${USER}"@$host:/etc/kubernetes/pki/sa.pub
    scp /etc/kubernetes/pki/front-proxy-ca.crt "${USER}"@$host:/etc/kubernetes/pki/front-proxy-ca.crt
    scp /etc/kubernetes/pki/front-proxy-ca.key "${USER}"@$host:/etc/kubernetes/pki/front-proxy-ca.key
    scp /etc/kubernetes/pki/etcd/ca.crt "${USER}"@$host:/etc/kubernetes/pki/etcd/ca.crt
    scp /etc/kubernetes/pki/etcd/ca.key "${USER}"@$host:/etc/kubernetes/pki/etcd/ca.key
    scp /etc/kubernetes/admin.conf "${USER}"@$host:/etc/kubernetes/admin.conf
done
```

<a name="DdoCF"></a>
### 安装网络插件 calico

之前我们是使用 `kube-flannel` 作为网络插件的, 这里使用 `calico`

换源拉取镜像:

```bash
docker login --username=xxx registry.cn-shenzhen.aliyuncs.com

docker pull registry.cn-shenzhen.aliyuncs.com/di_chen/calico-node:v3.3.2
docker pull registry.cn-shenzhen.aliyuncs.com/di_chen/calico-cni:v3.3.2

docker tag registry.cn-shenzhen.aliyuncs.com/di_chen/calico-node:v3.3.2 quay.io/calico/node:v3.3.2
docker tag registry.cn-shenzhen.aliyuncs.com/di_chen/calico-cni:v3.3.2 quay.io/calico/cni:v3.3.2
```

确保网络插件正常运行:

```bash
$ ksys get po
NAME                                   READY   STATUS    RESTARTS   AGE
calico-node-tp2dz                      2/2     Running   0          42s
coredns-89cc84847-2djpl                1/1     Running   0          66s
coredns-89cc84847-vt6zq                1/1     Running   0          66s
etcd-k8s-master01                      1/1     Running   0          27s
kube-apiserver-k8s-master01            1/1     Running   0          16s
kube-controller-manager-k8s-master01   1/1     Running   0          34s
kube-proxy-x497d                       1/1     Running   0          66s
kube-scheduler-k8s-master01            1/1     Running   0          17s
```

<a name="ec9d7a2d"></a>
## 三、加入节点
<a name="a769d2ad"></a>
### node 节点

```bash
kubeadm join 192.168.1.140:16443 --token wkqhux.026ij6fkmxr0bift \
     --discovery-token-ca-cert-hash sha256:fac9b56402c200a2f43a050d34b532b8d35c41735975e2b32562a6ca72e29f6b
```

<a name="ed9b4b83"></a>
### master 节点

```bash
kubeadm join 192.168.1.140:16443 --token wkqhux.026ij6fkmxr0bift \
     --discovery-token-ca-cert-hash sha256:fac9b56402c200a2f43a050d34b532b8d35c41735975e2b32562a6ca72e29f6b \
     --experimental-control-plane
```

其他 master 节点加入, 与 node 节点相差的参数就是 `--experimental-control-plane`

<a name="47434b27"></a>
## 四、查看节点

```bash
$ ksys get no
NAME          STATUS   ROLES    AGE     VERSION
k8s-master1   Ready    master   91m     v1.14.0
k8s-master2   Ready    master   33m     v1.14.0
k8s-master3   Ready    master   32m     v1.14.0
k8s-node1     Ready    <none>   3m59s   v1.14.0
k8s-node2     Ready    <none>   3m54s   v1.14.0
k8s-node3     Ready    <none>   3m52s   v1.14.0
k8s-node4     Ready    <none>   3m49s   v1.14.0
```

再部署 Dashboard, 访问 `https://k8s-master-lb:30443` 即可

OK, 至此, 高可用 Kubernetes 集群搭建完毕 🍻🍻🍻

在Kubernetes Dashboard中可以看到所有节点信息：

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599811489307-09b80092-63a4-4097-97ac-8fe1afb986a6.png#align=left&display=inline&height=1010&originHeight=1010&originWidth=1906&size=0&status=done&style=none&width=1906)

<a name="d7371b5d"></a>
## 五、集群稳定性测试
<a name="ffd78e37"></a>
### 关闭部分 master 节点

k8s-master1 关机, 在 k8s-master2 和 k8s-master3 中查看节点:

```bash
$ ksys get no
NAME          STATUS     ROLES    AGE   VERSION
k8s-master1   NotReady   master   23h   v1.14.0
k8s-master2   Ready      master   22h   v1.14.0
k8s-master3   Ready      master   22h   v1.14.0
k8s-node1     Ready      <none>   21h   v1.14.0
k8s-node2     Ready      <none>   21h   v1.14.0
k8s-node3     Ready      <none>   21h   v1.14.0
k8s-node4     Ready      <none>   21h   v1.14.0
```

在[dashboard](https://k8s-master-lb:30443/#!/overview?namespace=default)中查看也仍然通畅。

可以看到, VIP (192.168.1.140, k8s-master-lb) 已经转移到 k8s-master2:

```bash
[root@k8s-master2 ~]# ip a
...
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:c6:ea:aa brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global noprefixroute ens33
       valid_lft forever preferred_lft forever
    inet 192.168.1.140/32 scope global ens33
       valid_lft forever preferred_lft forever
    inet6 fe80::49c2:1a95:aab:494f/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
...
```

<a name="ec40f1ec"></a>
### 重启所有节点

将所有虚拟机(所有 master 及 node)进行关闭后再启动, 可以看到所有节点正常运行:

```bash
$ ksys get no
NAME          STATUS   ROLES    AGE   VERSION
k8s-master1   Ready    master   23h   v1.14.0
k8s-master2   Ready    master   22h   v1.14.0
k8s-master3   Ready    master   22h   v1.14.0
k8s-node1     Ready    <none>   21h   v1.14.0
k8s-node2     Ready    <none>   21h   v1.14.0
k8s-node3     Ready    <none>   21h   v1.14.0
k8s-node4     Ready    <none>   21h   v1.14.0
```

