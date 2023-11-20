Dockerfile是一个包含用于组合映像的命令的文本文档。可以使用在命令行中调用任何命令。 Docker通过读取Dockerfile中的指令自动生成映像。

<a name="5bf987ab"></a>
## 文件格式

Dockerfile 一般分为四部分：基础镜像信息、维护者信息、镜像操作指令和容器启动时执行指令，’#’ 为 Dockerfile 中的注释。

- 注释: 以 # 开头的是注释语句
- 指令: `INSTRUCTION argument`

<a name="3906998d"></a>
## 常用指令
<a name="FROM"></a>
### FROM
指定基础镜像。
```
FROM [image] # 使用 latest 版本
FROM [image:tag] # 使用指定版本
```

- 必须是已经存在的基础镜像
- 必须是第一条非注释指令

<a name="MAINTAINER"></a>
### MAINTAINER
指定镜像的作者信息，包括镜像的所有者和联系信息。
```
MAINTAINER [name]
```

示例:
```
MAINTAINER quanzaiyu
MAINTAINER 731734107@qq.com
MAINTAINER quanzaiyu <731734107@qq.com>
```

<a name="RUN"></a>
### RUN
指定当前镜像中运行的命令。
```bash
RUN [command] # shell 模式
RUN ["executable", "param1", "param2"] # exec 模式
```

在 shell 模式下，是以 `/bin/sh -c command` 开始执行命令。

比如：
```
RUN echo hello
```

在 exec 模式下，可以使用其他的 shell 执行命令。

RUN指令创建的中间镜像会被缓存，并会在下次构建中使用 (因此, 不要过多书写 RUN 指令，尽量将多个命令合并)。如果不想使用这些缓存镜像，可以在构建时指定--no-cache参数，如：docker build --no-cache

<a name="EXPOSE"></a>
### EXPOSE
指定运行该镜像的容器使用的端口。
```
EXPOSE [port1] [port2] ...
```

但是运行时Docker并不会自动开启对应服务，还需要手动开启对应的服务并添加端口的映射指令，比如：
```bash
$ docker run --name nginx-server -p 80 -d ubuntu:latest nginx -g "daemon off;"
```

<a name="CMD"></a>
### CMD
跟 RUN 命令使用方法类似，也是运行一个指令：
```
CMD [command] # shell 模式
CMD ["executable", "param1", "param2"] # exec 模式
CMD ["param1", "param2"] # 作为 ENTRYPOINT 指令的默认参数
```

与 RUN 命令的区别：

- RUN 命令时在镜像构建时运行
- CMD 命令是在容器启动时运行

比如:
```
CMD ['/usr/sbin/nginx', '-g', 'deamon off;']
```

指定 CMD 命令之后，运行容器的时候就不需要在后面加上运行参数了，不过还是得指定端口映射：
```bash
$ docker run --name nginx-server -p 80 -d ubuntu:latest
```

:::info
如果在启动一个容器时，指定了运行时命令，则 CMD 中的命令会被覆盖。
:::

<a name="ENTRYPOINT"></a>
### ENTRYPOINT
也是运行一个命令，与 RUN 不同的是，ENTRYPOINT 中的指令不会被运行容器时覆盖。
```
ENTRYPOINT [command] # shell 模式
ENTRYPOINT ["executable", "param1", "param2"] # exec 模式
```

运行容器时如果必须覆盖 ENTRYPOINT 中的命令，需要使用以下命令进行覆盖：
```bash
$ docker run --entrypoint [command]
```

<a name="b22d50de"></a>
### ADD 和 COPY
ADD 和 COPY 都是复制文件。
```
ADD [src]...  [dest]
ADD ["src"... "dest"] # 适用于文件路径中有空格的情况

COPY [src]...  [dest]
COPY ["src"... "dest"] # 适用于文件路径中有空格的情况
```

区别为：ADD 包含了类似 tar 的解压功能。

- ADD: 将本地文件添加到容器中，tar类型文件会自动解压(网络压缩资源不会被解压)，可以访问网络资源，类似wget
- COPY: 功能类似ADD，但是是不会自动解压文件，也不能访问网络资源

如果只是简单的复制文件，推荐使用 COPY。

<a name="VOLUME"></a>
### VOLUME
用于指定持久化目录。

格式：
```
VOLUME ["/path/to/dir"]
```

示例：
```
VOLUME ["/data"]
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"
```

注：一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能：

- 卷可以容器间共享和重用
- 容器并不一定要和其它容器共享卷
- 修改卷后会立即生效
- 对卷的修改不会对镜像产生影响
- 卷会一直存在，直到没有任何容器在使用它

<a name="WORKDIR"></a>
### WORKDIR
设置工作目录，即创建容器后进入的目录，类似于cd命令。

格式：
```
WORKDIR /path/to/dir
```

示例：
```
WORKDIR /a  (这时工作目录为/a)
WORKDIR b  (这时工作目录为/a/b)
WORKDIR c  (这时工作目录为/a/b/c)
```

注：通过WORKDIR设置工作目录后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY等命令都会在该目录下执行。在使用 `docker run` 运行容器时，可以通过`-w`参数覆盖构建时所设置的工作目录。

<a name="ENV"></a>
### ENV
设置环境变量。

格式：
```bash
ENV <key> <value>  # <key>之后的所有内容均会被视为其<value>的组成部分，因此，一次只能设置一个变量
ENV <key>=<value> ...  # 可以设置多个变量，每个变量为一个"<key>=<value>"的键值对，如果<key>中包含空格，可以使用\来进行转义，也可以通过""来进行标示；另外，反斜线也可以用于续行
```

示例：
```bash
ENV myName John Doe
ENV myDog Rex The Dog
ENV myCat=fluffy myDog=Rex
```

<a name="USER"></a>
### USER
指定容器为哪个用户运行，可以使用uid（用户）和gid（用户组），以及其组合。默认使用 root 用户。
```bash
USER daemon
```

有以下几种组合：
```
USER user
USER user:group
USER user:gid
USER uid
USER uid:group
USER uid:gid
```

<a name="ONBUILD"></a>
### ONBUILD
ONBUILD 用于设置镜像触发器。当所构建的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被触发。

格式：
```
ONBUILD [INSTRUCTION]
```

示例：
```
ONBUILD ADD . /app/src
ONBUILD RUN /usr/local/bin/python-build --dir /app/src
```

<a name="LABEL"></a>
### LABEL
用于为镜像添加元数据。

格式：
```
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

示例：
```bash
LABEL version="1.0" description="这是一个Web服务器" by="IT笔录"
```

注：使用LABEL指定元数据时，一条LABEL指定可以指定一或多条元数据，指定多条元数据时不同元数据之间通过空格分隔。推荐将所有的元数据通过一条LABEL指令指定，以免生成过多的中间镜像。

<a name="ARG"></a>
### ARG
用于指定传递给构建运行时的变量。

格式：
```
ARG <name>[=<default value>]
```

示例：
```
ARG site
ARG build_user=www
```

<a name="9b4ef702"></a>
## Dockerfile 示例
使用Ubuntu构建一个nginx容器
```
FROM ubuntu:14.04
MAINTAINER quanzaiyu "quanzaiyu@163.com"
ENV REFERSH_DATE 2015-04-01
RUN apt-get update && apt-get install -y nginx
COPY index.html /usr/share/nginx/html # 将宿主机的文件覆盖到容器中
EXPOSE 80
ENTRYPOINT ['/usr/sbin/nginx', '-g', 'deamon off;']
CMD echo 'created'
```

为 CentOS 安装常用工具
```
FROM centos:latest
RUN yum update -y && yum install net-tools.x86_64 -y
EXPOSE 80
CMD /bin/bash
```

<a name="50d2f5d6"></a>
## Dockerfile 构建过程

1. 从基础镜像运行一个容器
2. 执行一条指令，对容器做出修改
3. 执行类似 docker commit 的操作，提交一个新的镜像层
4. 再基于刚提交的镜像运行一个新容器
5. 执行 Dockerfile 中的下一条指令，直至所有指令执行完毕

构建过程中，会生成一些中间层镜像，可以使用中间层镜像进行调试，便于定位错误的位置。

正常情况下，构建镜像会用到缓存，这样可以提升构建速度，但有的时候不想用缓存，可以在构建命令中加入 `--no-cache` 选项。

另外，修改环境变量也可以刷新缓存，比如上面的 Dockerfile 示例中，改变 REFERSH_DATE 的值即可。

可以使用 `docker history` 命令查看镜像的构建过程。

<a name="65296f63"></a>
## 使用 Dockerfile 构建镜像
docker build 命令用于从 Dockerfile 构建镜像

可以在 docker build 命令中使用 -f 标志指向文件系统中任何位置的 Dockerfile, 加上 -t 为构建的镜像打标签

```bash
docker build -t '731734107/test' -f /path/to/a/Dockerfile # 以指定路径的Dockerfile进行构建
```

如果 Docker 文件就在当前目录，则不需要显式指定Dockerfile的路径：

```bash
docker build -t "731734107/test" .
```

