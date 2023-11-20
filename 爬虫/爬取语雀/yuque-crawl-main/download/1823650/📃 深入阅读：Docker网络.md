在宿主机上执行 ifconfig，可以看到一个 docker0 的虚拟网桥。

```bash
$ ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 0.0.0.0
        inet6 fe80::42:52ff:fe31:9057  prefixlen 64  scopeid 0x20<link>
        ether 02:42:52:31:90:57  txqueuelen 0  (Ethernet)
        RX packets 8  bytes 536 (536.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 30  bytes 3054 (2.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

如果没有 ifconfig 命令，使用以下命令安装：

```bash
$ yum install net-tools.x86_64 -y
```

<a name="866a671c"></a>
## 安装网桥管理程序

```bash
$ yum install bridge-utils
# or
$ apt-get install bridge-utils
```

先运行一个容器，查看网桥设备状态

```bash
$ brctl show
bridge name	bridge id		STP enabled	interfaces
docker0		8000.024252319057	no		veth7bfa1b9
virbr0		8000.525400e0956a	yes		virbr0-nic
```

可以看到在 docker0 的网桥设备上连接了一个 interface，使用 ifconfig 可以看到：

```bash
$ ifconfig
veth7bfa1b9: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80bd:9fff:feb7:e5  prefixlen 64  scopeid 0x20<link>
        ether 82:bd:9f:b7:00:e5  txqueuelen 0  (Ethernet)
        RX packets 8  bytes 648 (648.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 38  bytes 3702 (3.6 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

<a name="18276118"></a>
## 网桥配置

<a name="bd5fc1ae"></a>
### 修改 docker 网桥配置

```bash
$ ifconfig docker0 192.168.40.100 netmask 255.255.255.0
$ systemctl reload docker # 重启docker服务生效
```

<a name="6555bd4f"></a>
### 添加 docker 虚拟网桥

```bash
$ brctl addbr br0
$ ifconfig br0 192.168.100.1 netmask 255.255.255.0
```

然后编辑 docker 配置文件，添加如下信息：

```bash
$ vim /etc/docker/daemon.json
{
  "bridge": "br0"
}
```

然后重启 docker，启动一个容器并进入：

```bash
$ systemctl restart docker
$ docker start -i server2
```

进入容器，可以看到已经分配了新的网桥给 docker：

```bash
root@c096b413dc42:/# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.100.2  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::42:c0ff:fea8:6402  prefixlen 64  scopeid 0x20<link>
        ether 02:42:c0:a8:64:02  txqueuelen 0  (Ethernet)
        RX packets 8  bytes 648 (648.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8  bytes 648 (648.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

:::warning
使用网桥管理工具创建的网桥会在下次物理机重启时失效。可以通过直接修改网桥配置文件达到重启不失效的目的。
:::

解决方案如下，创建一个网络配置文件：

```bash
$ vim /etc/sysconfig/network-scripts/ifcfg-br0
IPADDR=192.168.1.1
TYPE=Bridge
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
#IPV6INIT=yes
#IPV6_AUTOCONF=yes
#IPV6_DEFROUTE=yes
#IPV6_PEERDNS=yes
#IPV6_PEERROUTES=yes
#IPV6_FAILURE_FATAL=no
#NAME=eno16777736
#UUID=d0d3289e-9c2c-45f7-a569-c55aca9f0e8a
DEVICE=br0
ONBOOT=yes
```

重启网络服务，并配置网桥ip及子网掩码

```bash
$ service network restart
Restarting network (via systemctl):                        [  确定  ]
$ ifconfig br0 192.168.1.1 netmask 255.255.255.0
```

参考：[centos 7.2 网卡配置文件 及 linux bridge的静态配置](http://www.cnblogs.com/doscho/p/6225807.html)

<a name="06dc7504"></a>
## 容器互联

默认情况下，docker并不会阻止容器之间的通讯，容器之间可以通过ip相互进行访问。

但是，如果重启docker服务，ip会发生改变，如果是提供服务的容器，使用之前的ip就不能进行访问了，因此使用ip进行通讯的方式并不可靠。

因此，在运行容器时，可以使用 `--link` 参数来指定连接的容器，而不必担心ip地址的变化。

```bash
$ docker run --link=[CONTAINER_NAME]:[ALIAS] [IMAGE] [COMMOND]
```

首先创建一个 Dockerfile：

```
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y ping
RUN apt-get install -y nginx
RUN apt-get install -y curl
EXPOSE 80
CMD /bin/bash
```

执行此 Dockerfile 进行镜像构建：

```bash
$ docker build -t test/ubuntu:1.0 .
```

然后通过这个镜像创建一个容器：cct1。

使用 link 选项关联两个容器：

```bash
$ docker run -it --name cct2 --link=cct1:webtest test/ubuntu:1.0
```

进入 cct2，使用 ping 命令检查两个容器的互通性：

```bash
root@1d8c06b3dc25:$ ping webtest
```

注意到使用的是cct1容器的别名，发现网络是通畅的。

查看 `/etc/hosts` 文件，会发现虚拟主机 `webtest` 已经自动加上了。使用 `env` 命令也可看到很多关于 `WEBTEST` 的环境变量。

使用 `docker restart cct1 cct2` 重新启动容器，会发现 `ping webtest` 依然生效，而检查 `/etc/hosts` 文件会发现ip已经发生了改变，说明容器间通信不是基于 ip 的。

<a name="d35e2650"></a>
## Docker 跨主机连接: 使用网桥
![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601124742804-1634ffe7-e567-4ada-9fe2-a548f39c4b0c.png#align=left&display=inline&height=572&originHeight=572&originWidth=1030&size=0&status=done&style=none&width=1030)

原理：在两台主机上，配置可相互通讯的网桥，将不同主机中 Docker 的网桥连接到此网桥。

<a name="eeb60cdd"></a>
## Docker 跨主机连接: 使用 Open vSwitch

实验环境：两台虚拟机 (centOS)

A主机:

- 宿主机IP ：192.168.42.130
- Docker 容器中 IP : 192.168.1.2
- Docker 容器连接的网桥地址（br0） : 192.168.1.1

B主机:

- 宿主机IP ：192.168.42.131
- Docker 容器中 IP : 192.168.2.2
- Docker 容器连接的网桥地址（br0） : 192.168.2.1

使两部虚拟机中的 docker 能互通。

<a name="0f0186b3"></a>
### 什么是 Open VSwitch

ovs （Open VSwitch） 是一个高质量、多层虚拟交换机，使用开源Apache2.0许可协议，由 Nicira Networks 开发，主要实现代码为可移植的 C 代码。它的目的是让大规模网络自动化可以通过编程扩展，同时仍然支持标准的管理接口和协议（例如 NetFlow，SFlow，SPAN，RSPAN，CLI，LACP，802.lag）<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601124772504-63d94771-b18f-40e7-9d56-dca6959028a5.png#align=left&display=inline&height=715&originHeight=715&originWidth=1441&size=0&status=done&style=none&width=1441)

<a name="a5e8af67"></a>
### 什么是 GRE 隧道

GRE：通用路由协议封装。

隧道技术（Tunneling）是一种通过使用互联网络的基础设施在网络之间传递数据的方式。使用隧道传递的数据(或负载)可以是不同协议的数据帧或包。隧道协议将其它协议的数据帧或包重新封裝然后通过隧道发送。新的帧头提供路由信息,以便通过互联网传递被封装的负载数据。

<a name="63e4c688"></a>
### 使用 ovs 实现跨主机通讯

安装

```bash
$ apt-get install openvswitch-switch
// or
$ yum install openvswitch
```

检测安装

```bash
$ ovs-vsctl show
fdbecc9f-193a-45c0-b1b7-599d53e22df9
    ovs_version: "2.10.1"
```

A主机中的配置：

添加 ovs 网桥 obr0

```bash
$ ovs-vsctl add-br obr0
```

为 obr0 添加接口 gre0

```bash
$ ovs-vsctl add-port obr0 gre0
ovs-vsctl: Error detected while setting up 'gre0': could not add network device gre0 to ofproto (Invalid argument).  See ovs-vswitchd log for details.
ovs-vsctl: The default log directory is "/usr/local/var/log/openvswitch".

$ ovs-vsctl show
fdbecc9f-193a-45c0-b1b7-599d53e22df9
    Bridge "obr0"
        Port "gre0"
            Interface "gre0"
                error: "could not add network device gre0 to ofproto (Invalid argument)"
        Port "obr0"
            Interface "obr0"
                type: internal
    ovs_version: "2.10.1"
```

设置接口类型

```bash
$ ovs-vsctl set interface gre0 type=gre options:remote_ip=192.168.42.131

$ ovs-vsctl show
fdbecc9f-193a-45c0-b1b7-599d53e22df9
    Bridge "obr0"
        Port "gre0"
            Interface "gre0"
                type: gre
                options: {remote_ip="192.168.42.131"}
        Port "obr0"
            Interface "obr0"
                type: internal
    ovs_version: "2.10.1"
```

使用网桥管理工具在物理机新建一个 br0 的网桥，并设置其 ip

```bash
$ brctl addbr br0
$ ifconfig br0 192.168.1.1 netmask 255.255.255.0
```

为 br0 网桥添加 ovs 网桥的连接

```bash
$ brctl addif br0 obr0
$ brctl show
bridge name	bridge id		STP enabled	interfaces
br0		8000.aed32285704b	no		obr0
docker0		8000.0242a6aa2d07	no
virbr0		8000.525400e0956a	yes		virbr0-nic
```

在 docker 配置文件 `/etc/docker/daemon.json` 中添加：

```json
{
  "bridge": "br0"
}
```

重启 docker 服务：

```bash
$ systemctl restart docker
```

启动容器，进行连通性测试：

```bash
$ docker start -i centos
[root@ab6398eaa692 /]# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.2  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::42:c0ff:fea8:102  prefixlen 64  scopeid 0x20<link>
        ether 02:42:c0:a8:01:02  txqueuelen 0  (Ethernet)
        RX packets 17  bytes 1947 (1.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6  bytes 508 (508.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[root@ab6398eaa692 /]# ping 192.168.42.131
PING 192.168.42.131 (192.168.42.131) 56(84) bytes of data.
64 bytes from 192.168.42.131: icmp_seq=1 ttl=63 time=0.298 ms
64 bytes from 192.168.42.131: icmp_seq=2 ttl=63 time=0.310 ms
64 bytes from 192.168.42.131: icmp_seq=3 ttl=63 time=0.331 ms
^C
--- 192.168.42.131 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.298/0.313/0.331/0.013 ms
```

可以看到，进入容器使用 ping 命令连接另一台虚拟主机成功。

同样的步骤，在另一台虚拟机（B主机）中进行相同的配置：

```bash
$ ifconfig br0 192.168.2.1 netmask 255.255.255.0
$ ovs-vsctl set interface gre0 type=gre options:remote_ip=192.168.42.130
$ brctl addif br0 obr0
```

除此之外，还需要在两部虚拟机的路由表中相互配置对方的docker网段：

先查看路由表：

```bash
[root@node1 docker]# route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         gateway         0.0.0.0         UG    100    0        0 ens33
192.168.1.0     0.0.0.0         255.255.255.0   U     425    0        0 br0
192.168.42.0    0.0.0.0         255.255.255.0   U     100    0        0 ens33
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
```

```bash
# A 主机
$ ip route add 192.168.2.0/24 via 192.168.42.131 dev ens33

# B 主机
$ ip route add 192.168.1.0/24 via 192.168.42.130 dev ens33
```

使用 `route` 命令查看路由表，可以看到相关配置已经在路由表中了。

```bash
$ route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         gateway         0.0.0.0         UG    100    0        0 ens33
192.168.1.0     0.0.0.0         255.255.255.0   U     425    0        0 br0
192.168.2.0     192.168.42.131  255.255.255.0   UG    0      0        0 ens33
192.168.42.0    0.0.0.0         255.255.255.0   U     100    0        0 ens33
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
```

这时，即可实现两台虚拟主机中的 docker 互通。

```bash
# A主机中的 docker
[root@ab6398eaa692 /]# ping 192.168.2.2
PING 192.168.2.2 (192.168.2.2) 56(84) bytes of data.
64 bytes from 192.168.2.2: icmp_seq=1 ttl=62 time=0.400 ms
64 bytes from 192.168.2.2: icmp_seq=2 ttl=62 time=1.15 ms
^C
--- 192.168.2.2 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.400/0.775/1.150/0.375 ms


# B主机中的 docker
[root@ab6398eaa692 /]# ping 192.168.1.2
PING 192.168.1.2 (192.168.1.2) 56(84) bytes of data.
64 bytes from 192.168.1.2: icmp_seq=1 ttl=62 time=0.299 ms
64 bytes from 192.168.1.2: icmp_seq=2 ttl=62 time=0.338 ms
^C
--- 192.168.1.2 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.299/0.318/0.338/0.026 ms
```

<a name="41b41d5b"></a>
### 错误解决

`ovs-vsctl: unix:/usr/local/var/run/openvswitch/db.sock: database connection failed` 解决方案

```bash
$ ovsdb-server  --remote=punix:/usr/local/var/run/openvswitch/db.sock \
                --remote=db:Open_vSwitch,Open_vSwitch,manager_options \
                --private-key=db:Open_vSwitch,SSL,private_key \
                --certificate=db:Open_vSwitch,SSL,certificate \
                --bootstrap-ca-cert=db:Open_vSwitch,SSL,ca_cert \
                --pidfile --detach
$ ovs-vsctl --no-wait init
$ ovs-vswitchd --pidfile --detach
```

编写脚本，使其开机自启：

`/root/autorun.sh`

```bash
#!/bin/bash
ovsdb-server --remote=punix:/usr/local/var/run/openvswitch/db.sock --remote=db:Open_vSwitch,Open_vSwitch,manager_options --pidfile --detach
ovs-vsctl --no-wait init
ovs-vswitchd --pidfile --detach --log-file
```

修改其权限

```bash
$ chmod 777 autorun.sh
```

将其添加到开机自启列表，把路径添加到 `/etc/rc.d/rc.local` 中

```bash
source /root/autorun.sh
```

<a name="9c1abc15"></a>
## Docker 跨主机连接: 使用 weave

<a name="35808e79"></a>
## 参考资料

- [Docker 网络不通的解决方法](https://blog.csdn.net/knight_zhen/article/details/51733255)
- [OpenvSwitch完全使用手册](https://blog.csdn.net/tantexian/article/details/46707175)
- [ovs-vsctl: unix:/usr/local/var/run/openvswitch/db.sock: database connection failed](https://blog.csdn.net/xyq54/article/details/51371819)
