要查看某个命令的帮助文档，跟上 `--help` 即可。比如 `docker search --help`

<a name="rmCA9"></a>
## 查看Docker是否在运行

```bash
$ ps -ef | grep docker
# or
$ ps aux | grep docker
```

<a name="amXMZ"></a>
## 复制容器内文件到本地

```bash
$ docker cp [container:path] [loaclPath] # 从容器中复制文件到宿主机
$ docker cp [loaclPath] [container:path] # 从宿主机中复制文件到容器

# 示例
$ docker cp server1:/etc/hosts ./ # 从容器中复制文件到宿主机
$ docker cp ./hosts server1:/opt # 从宿主机中复制文件到容器
```

<a name="B6q2O"></a>
## 查看镜像或容器详细信息

```bash
$ docker inspect [image:tag or container]
```

可以使用管道过滤出有用的信息，如：

```bash
$ docker inspect server | grep IPAddress
    "SecondaryIPAddresses": null,
    "IPAddress": "172.17.0.2",
            "IPAddress": "172.17.0.2",
```

<a name="SSeWh"></a>
## 查看容器内进程

使用 `docker top [container]` 命令查看容器内进程：

```bash
$ docker top server
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                4932                4917                0                   00:28               ?                   00:00:00            /bin/sh -c while true; do echo Hello world; sleep 1;done
root                5708                4932                0                   00:38               ?                   00:00:00            sleep 1
```

<a name="48q4e"></a>
## 查看日志

使用 logs 命令可以查看容器运行日志

```bash
$ docker logs -f -t --tail [container]
```

- -f: --follows=true|false 默认false，一直跟踪log的变化并返回结果
- -t: --timestamps=true|false 在返回的日志中添加时间戳
- --tail="all" 默认all，返回结尾处多少数量的日志

直接使用，打印出当前时间点之前的日志，比如运行一个每隔一秒输出一段话的脚本：

```bash
$ docker run --name server1 -d ubuntu /bin/sh -c "while true; do echo Hello world; sleep 1;done"
e1306e60672a152de4a38d2541279124c98347a13c2e612c386694c442db0708
$ docker logs server1
Hello world
Hello world
Hello world
```

以下日志会不断更新：

```bash
$ docker logs server2 --tail 10 -tf
2018-10-14T16:35:38.188534000Z Hello world
2018-10-14T16:35:39.189464000Z Hello world
2018-10-14T16:35:40.191417000Z Hello world
```

<a name="X6d1j"></a>
## 清理磁盘空间
命令：
```
docker system prune
```
用于清理磁盘，删除关闭的容器、无用的数据卷和网络，以及dangling镜像（即无tag的镜像）。 

命令：
```
docker system prune -a
```
清理得更加彻底，可以将没有容器使用Docker镜像都删掉。注意，这两个命令会把你暂时关闭的容器，以及暂时没有用到的Docker镜像都删掉。

