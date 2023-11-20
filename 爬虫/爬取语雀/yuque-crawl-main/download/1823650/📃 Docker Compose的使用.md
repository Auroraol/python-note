Docker Compose是Docker官方编排（Orchestration）项目之一，负责快速的部署分布式应用。其代码目前在 [https://github.com/docker/compose](https://github.com/docker/compose) 上开源。Compose 定位是 「定义和运行多个 Docker 容器的应用（Defining and running multi-container Docker applications）」，其前身是开源项目Fig。

前面我们已经学习过使用一个Dockerfile模板文件，可以很方便的定义一个单独的应用容器。然而，在日常工作中，经常会碰到需要多个容器相互配合来完成某项任务的情况。例如要实现一个 Web 项目，除了 Web 服务容器本身，往往还需要再加上后端的数据库服务容器或者缓存服务容器，甚至还包括负载均衡容器等。Compose 恰好满足了这样的需求。它允许用户通过一个单独的 `docker-compose.yml` 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

Compose 中有两个重要的概念：

- 服务 (service)：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
- 项目 (project)：由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。

Compose 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。Compose 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。所以只要所操作的平台支持 Docker API，就可以在其上利用 Compose 来进行编排管理。

**使用 Docker Compose 可以轻松、高效的管理容器，它是一个用于定义和运行多容器 Docker 的应用程序工具**

<a name="3abfeb61"></a>
## Docker Compose 安装

安装很简单
```python
$ yum -y install docker-compose
```

或者
```bash
$ yum -y install epel-release
$ yum -y install python-pip
$ pip install docker-compose
$ docker-compose version
docker-compose version 1.24.0, build 0aa5906
docker-py version: 3.7.2
CPython version: 2.7.5
OpenSSL version: OpenSSL 1.0.2k-fips  26 Jan 2017
```

<a name="204407fa"></a>
## Docker Compose 的使用

Docker Compose 部署应用依赖于一个叫 `docker-compose.yml` 的文件

部署应用

```bash
$ docker-compose up -d
$ docker-compose -f docker-compose.yml up -d
```

查看服务的运行状态

```bash
$ docker-compose ps
     Name                    Command               State                     Ports
-----------------------------------------------------------------------------------------------------
traefik_proxy_1   /traefik --web --docker -- ...   Up      0.0.0.0:80->80/tcp, 0.0.0.0:8080->8080/tcp
```

<a name="f1e2eb7c"></a>
## 示例: Python 完成页面统计

下面我们用 Python 来建立一个能够记录页面访问次数的 web 网站。 新建文件夹，在该目录中编写`app.py`文件

```python
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

接着编写`Dockerfile`文件，内容为:

```
FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install redis flask
CMD ["python", "app.py"]
```

然后是编写`docker-compose.yml`文件，这个是 Compose 使用的主模板文件。

```yaml
version: '3'
services:
  web:
  build: .
  ports:
  - "5000:5000"
  volumes:
       - .:/code
  redis:
  image: "redis:alpine"
```

运行 compose 项目:

```bash
$ docker-compose up
```

此时访问本地 5000 端口，每次刷新页面，计数就会加 1。

<a name="a5352176"></a>
## Docker Compose 常用命令

docker-compose 命令的基本的使用格式是:

```bash
docker-compose [-f=<arg>...] [options] [COMMAND] [ARGS...]
```

**命令选项**

- **-f**, **--file** FILE 指定使用的 Compose 模板文件，默认为 docker-compose.yml，可以多次指定。
- **-p**, **--project-name** NAME 指定项目名称，默认将使用所在目录名称作为项目名。
- **--x-networking** 使用 Docker 的可拔插网络后端特性
- **--x-network-driver** DRIVER 指定网络后端的驱动，默认为 bridge
- **--verbose** 输出更多调试信息。
- **-v**, **--version** 打印版本并退出。

<a name="build"></a>
### build

构建（重新构建）项目中的服务容器。服务容器一旦构建后，将会带上一个标记名，例如对于 web 项目中的一个 db 容器，可能是 web_db。可以随时在项目目录下运行`docker-compose build`来重新构建服务。

```bash
$ docker-compose build [options] [SERVICE...]
```

选项：

- **--force-rm** 删除构建过程中的临时容器。
- **--no-cache** 构建镜像过程中不使用 cache（这将加长构建过程）。
- **--pull** 始终尝试通过 pull 来获取更新版本的镜像。

<a name="kill"></a>
### kill

```bash
$ docker-compose kill [options] [SERVICE...]
```

通过发送`SIGKILL`信号来强制停止服务容器。支持通过`-s`参数来指定发送的信号，例如通过如下指令发送`SIGINT`信号。

```shell
$ docker-compose kill -s SIGINT
```

<a name="port"></a>
### port

打印某个容器端口所映射的公共端口。

```bash
$ docker-compose port [options] SERVICE PRIVATE_PORT
```

选项：

- **--protocol=proto** 指定端口协议，tcp（默认值）或者 udp。
- **--index=index** 如果同一服务存在多个容器，指定命令对象容器的序号（默认为 1）。

<a name="ps"></a>
### ps

列出项目中目前的所有容器。

```bash
$ docker-compose ps [options] [SERVICE...]
```

选项：

- `-q`只打印容器的 ID 信息。

<a name="pull"></a>
### pull

拉取服务依赖的镜像。

```bash
$ docker-compose pull [options] [SERVICE...]
```

选项：

- --ignore-pull-failures 忽略拉取镜像过程中的错误。

<a name="push"></a>
### push

推送服务依赖的镜像到 Docker 镜像仓库。

<a name="restart"></a>
### restart

重启项目中的服务。

```bash
$ docker-compose restart [options] [SERVICE...]
```

选项：

- -t, --timeout TIMEOUT 指定重启前停止容器的超时（默认为 10 秒）。

<a name="rm"></a>
### rm

```bash
$ docker-compose rm [options] [SERVICE...]
```

删除所有（停止状态的）服务容器。推荐先执行 `docker-compose stop`命令来停止容器。选项：

- **-f**, **--force** 强制直接删除，包括非停止状态的容器。一般尽量不要使用该选项。
- **-v** 删除容器所挂载的数据卷。

<a name="run"></a>
### run

在指定服务上执行一个命令。

```bash
$ docker-compose run [options] [-p PORT...] [-e KEY=VAL...] SERVICE [COMMAND] [ARGS...]
```

例如：

```bash
$ docker-compose run ubuntu ping docker.com
```

将会启动一个 ubuntu 服务容器，并执行 ping docker.com 命令。默认情况下，如果存在关联，则所有关联的服务将会自动被启动，除非这些服务已经在运行中。

该命令类似启动容器后运行指定的命令，相关卷、链接等等都将会按照配置自动创建。

给定命令将会覆盖原有的自动运行命令； 不会自动创建端口，以避免冲突。

如果不希望自动启动关联的容器，可以使用`--no-deps`选项，例如:

```bash
$ docker-compose run --no-deps web python manage.py shell
```

这将不会启动 web 容器所关联的其它容器,

选项：

- -d 后台运行容器。
- --name NAME 为容器指定一个名字。
- --entrypoint CMD 覆盖默认的容器启动指令。
- -e KEY=VAL 设置环境变量值，可多次使用选项来设置多个环境变量。
- -u, --user="" 指定运行容器的用户名或者 uid。
- --no-deps 不自动启动关联的服务容器。
- --rm 运行命令后自动删除容器，d 模式下将忽略。
- -p, --publish=[] 映射容器端口到本地主机。
- --service-ports 配置服务端口并映射到本地主机。
- -T 不分配伪 tty，意味着依赖 tty 的指令将无法运行。

<a name="scale"></a>
### scale

设置指定服务运行的容器个数。 通过 service=num 的参数来设置数量。

```bash
$ docker-compose scale [options] [SERVICE=NUM...]
```

例如：

```shell
$ docker-compose scale web=3 db=2
```

将启动 3 个容器运行 web 服务，2 个容器运行 db 服务。

一般的，当指定数目多于该服务当前实际运行容器，将新创建并启动容器；反之，将停止容器。选项：

- -t, --timeout TIMEOUT 停止容器时候的超时（默认为 10 秒）。

<a name="start"></a>
### start

启动已经存在的服务容器。

```bash
$ docker-compose start [SERVICE...]
```

<a name="73e71763"></a>
### stop

停止已经处于运行状态的容器，但不删除它。
```dockerfile
docker-compose stop [options] [SERVICE...]
```
通过`docker-compose start`可以再次启动这些容器。选项：

- -t, --timeout TIMEOUT 停止容器时候的超时（默认为 10 秒）。

<a name="logs"></a>
### logs

查看服务容器的输出。默认情况下，docker-compose 将对不同的服务输出使用不同的颜色来区分。可以通过 `--no-color`来关闭颜色。该命令在调试问题的时候十分有用。

```bash
$ docker-compose logs [options] [SERVICE...]
```

<a name="pause"></a>
### pause

暂停一个服务容器。

```bash
docker-compose pause [SERVICE...]
```

<a name="0c2ded9d"></a>
### 其他命令

- **config** 验证 Compose 文件格式是否正确，若正确则显示配置，若格式错误显示错误原因。
- **down** 此命令将会停止 up 命令所启动的容器，并移除网络
- **exec** 进入指定的容器。
- **help** 获得一个命令的帮助。
- **images** 列出 Compose 文件中包含的镜像。
- **top** 查看各个服务容器内运行的进程。
- **unpause **格式为`**docker-compose unpause [SERVICE...]**`，恢复处于暂停状态中的服务。
- **up** 格式为`**docker-compose up [options] [SERVICE...]**`，该命令十分强大，它将尝试自动完成包括构建镜像，（重新）创建服务，启动服务，并关联服务相关容器的一系列操作。链接的服务都将会被自动启动，除非已经处于运行状态。 可以说，大部分时候都可以直接通过该命令来启动一个项目。

<a name="35808e79"></a>
## 参考资料

- [Docker Compose - 阳明的博客](https://www.qikqiak.com/k8s-book/docs/8.Docker%20Compose.html)
- [Docker：Docker Compose 详解](https://www.jianshu.com/p/658911a8cff3)
- [Docker ---- Docker-Compose 详解](https://blog.csdn.net/u011781521/article/details/80464826)
