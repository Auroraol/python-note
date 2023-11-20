Docker官方安装源：

- [https://hub.docker.com/search?type=edition&offering=community&q=](https://hub.docker.com/search?type=edition&offering=community&q=)

<a name="G8sZG"></a>
## CentOS下安装Docker

官方文档：[Get Docker for CentOS](https://docs.docker.com/v1.13/engine/installation/linux/centos/)

在 CentOS7 中安装 Dokcer：

```bash
yum install docker -y
```

或者使用 curl 拉取 shell 脚本安装，shell 脚本地址：[https://get.docker.com](https://get.docker.com)

```bash
curl https://get.docker.com | sh
```

启动和设置开机自启：

```bash
$ systemctl start docker # 启动 Docker
$ systemctl stop docker # 关闭 Docker
$ systemctl enable docker # 开机启动
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
$ docker info # 查看关于 Docker 的一些信息
```

查看docker是否启动：

```bash
$ ps aux | grep docker
$ systemctl status docker
```

Docker 相关路径：

- Docker 镜像存储位置：`/var/lib/docker/containers`
- Docker 默认卷存放位置 `/var/lib/docker/volumes`

<a name="pNSiy"></a>
## Windows下安装Docker

参见本人另一篇文章：[Docker Desktop的安装和使用 - 搭建Docker环境](https://www.yuque.com/xiaoyulive/wsl/vchahd)

