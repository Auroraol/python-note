docker默认镜像拉取地址为国外仓库下载速度较慢，则会报错 `net/http: TLS handshake timeout`。此时，只需要将拉取地址改为国内镜像仓库即可。

<a name="cb5af38e"></a>
## 临时修改镜像源

格式为：

```bash
$ docker pull registry.docker-cn.com/myname/myrepo:mytag
例：
$ docker pull registry.docker-cn.com/library/ubuntu:16.04
```

<a name="8QHVf"></a>
## 全局修改镜像源

一些国内镜像源：

- Docker 官方中国区: [https://registry.docker-cn.com](https://registry.docker-cn.com)
- 网易: [https://hub-mirror.c.163.com](https://hub-mirror.c.163.com)
- ustc: [https://docker.mirrors.ustc.edu.cn](https://docker.mirrors.ustc.edu.cn)

修改docker 配置文件：`/etc/docker/daemon.json` 即可：

```json
{
  "registry-mirrors": [
    "https://xxx.mirror.aliyuncs.com",
    "https://registry.docker-cn.com",
    "https://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ]
}
```

备注：阿里云的镜像加速器地址，参见 [https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors) ，然后将 xxx 变更为你获取到的地址。

修改保存后重启 Docker 以使配置生效。

<a name="s2xlh"></a>
## 阿里镜像源加速

可以在阿里云控制台开通 "容器镜像服务", 在 "镜像加速器" 中可以看到镜像加速器地：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601027052669-776c960b-c0f6-47d0-8471-4622e9df3d04.png#align=left&display=inline&height=753&originHeight=928&originWidth=868&size=0&status=done&style=none&width=704)

使用以下命令生效:

```bash
$ sudo mkdir -p /etc/docker
$ sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://xxx.mirror.aliyuncs.com"]
}
EOF
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

<a name="fWuwR"></a>
## DaoCloud 加速

注册地址：[https://www.daocloud.io/mirror](https://www.daocloud.io/mirror)

使用以下命令即可将加速域名简单注册到本地Docker配置文件。

```bash
$ curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
```

注册之后，重启docker即可：

```bash
$ systemctl restart docker
```
