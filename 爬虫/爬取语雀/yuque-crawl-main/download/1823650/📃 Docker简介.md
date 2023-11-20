<a name="NBDUB"></a>
## 为什么要使用容器

传统的应用部署方式是通过插件或脚本来安装应用。这样做的缺点是应用的运行、配置、管理、所有生存周期将与当前操作系统绑定，这样做并不利于应用的升级更新/回滚等操作，当然也可以通过创建虚机的方式来实现某些功能，但是虚拟机非常重，并不利于可移植性。<br />新的方式是通过部署容器方式实现，每个容器之间互相隔离，每个容器有自己的文件系统 ，容器之间进程不会相互影响，能区分计算资源。相对于虚拟机，容器能快速部署，由于容器与底层设施、机器文件系统解耦的，所以它能在不同云、不同版本操作系统间进行迁移。<br />容器占用资源少、部署快，每个应用可以被打包成一个容器镜像，每个应用与容器间成一对一关系也使容器有更大优势，使用容器可以在build或release 的阶段，为应用创建容器镜像，因为每个应用不需要与其余的应用堆栈组合，也不依赖于生产环境基础结构，这使得从研发到测试、生产能提供一致环境。类似地，容器比虚机轻量、更“透明”，这更便于监控和管理。

容器优势总结：

- **快速创建/部署应用：**与VM虚拟机相比，容器镜像的创建更加容易。
- **持续开发、集成和部署：**提供可靠且频繁的容器镜像构建/部署，并使用快速和简单的回滚(由于镜像不可变性)。
- **开发和运行相分离：**在build或者release阶段创建容器镜像，使得应用和基础设施解耦。
- **开发，测试和生产环境一致性：**在本地或外网（生产环境）运行的一致性。
- **云平台或其他操作系统：**可以在 Ubuntu、RHEL、 CoreOS、on-prem、Google Container Engine或其它任何环境中运行。
- **Loosely coupled，分布式，弹性，微服务化：**应用程序分为更小的、独立的部件，可以动态部署和管理。
- **资源隔离**
- **资源利用：**更高效

<a name="U8Ahq"></a>
## 什么是Docker

[Docker](https://www.docker.com) 提供了一个可以运行你的运行程序的封套（envelope），或者说容器。它最初是用Go语言编写的，它就相当于是加在LXC（Linux Containers）上的管道，允许开发者在更高层次的概念上工作。

Docker 也是一个云计算平台，它利用 Linux 的 LXC、AUFU、Go语言、cgroup实现了资源的独立，可以很轻松地实现文件、资源、网络等隔离，其最终的目标是实现类似 PaaS 平台的应用隔离。

Docker 会像一个可移植引擎那样工作。它把应用程序以及所有应用程序的依赖环境打包到一个虚拟容器中，这个虚拟容器可以运行在任何一种Linux服务器上。这大大地提高了程序运行的灵活性和可移植性，无论需不需要许可、是在公共云还是私密云、是不是裸机环境等等。

- 一种虚拟化解决方案
- 操作系统级别的虚拟化
- 只能运行相同或类似内核的操作系统
- 依赖于Linux内核特性：Namespace和Cgroups（Control Group）

---

- 中文社区：[www.docker.org.cn](http://www.docker.org.cn)
- Docker Hub：[hub.docker.com](https://hub.docker.com)
- Document：[docs.docker.com](https://docs.docker.com)
- GitHub：[github.com/docker/docker](https://github.com/docker/docker)

<a name="qu4sh"></a>
## Docker 的诞生

Docker 是 Docker.Inc（前身dotCloud）公司开源的一个基于 LXC 技术之上构建的 Container 容器引擎，它原本是dotCloud启动的一个业余项目，源代码托管在 GitHub 上，基于 Go 语言并遵从 Apache2.0 协议，于2013年3月27日作为 public 项目发布。它吸引了大量的关注和讨论，导致 dotCloud 把它重命名到 Docker Inc。

Docker 是通过内核虚拟化技术（namespaces 及 cgroup等）来提供容器的资源隔离与安全保障等，由于 Docker 通过操作系统层的虚拟化实现隔离，所以 Docker 所以 Docker 容器在运行时，不需要类似虚拟机（VM）额外的操作系统开销，提高资源利用率。

<a name="cUyxF"></a>
## Docker 可以做什么

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

- Docker 是一个开源的软件部署解决方案
- Docker 是一个轻量级的应用容器框架
- Docker 可以打包、发布、运行任何应用
- build once，run anywhere

<a name="cFZEo"></a>
## Docker 与虚拟机的区别

| **传统虚拟机** | **Docker** |
| :---: | :---: |
| 依赖物理CPU和内存，是硬件级别的。 | 在操作系统上，利用操作系统的containerization（集装箱化）技术，可以在虚拟机上运行。 |
| 一般都是指操作系统镜像，比较复杂。 | docker开源而且轻量，成为“容器”，单个容器适合部署少量应用。 |
| 使用快照来保存状态。 | 引入了类似源代码管理机制，将容器的快照历史版本一一记录。 |
| 在构建系统的时候较为复杂，需要大量的人力。 | docker可以通过Dockfile来构建整个容器，重启和构建速度很快，更重要的是Dockfile可以手动编写，这样应用程序开发人员可以通过发布Dockfile来指导系统环境和依赖，这样对于持续交付十分有利。 |


传统虚拟机与Docker的区别图：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601026542135-b4b2511b-b9f3-4e29-b8a3-d6c9f703cf10.png#align=left&display=inline&height=261&originHeight=261&originWidth=692&size=0&status=done&style=none&width=692)

<a name="qERBB"></a>
## Docker 使用场景

- 使用Docker容器开发、测试、部署服务
- 创建隔离的运行环境
- 搭建测试环境
- 构建多用户的平台即服务（PaaS）基础设施
- 提供软件即服务（SaaS）应用程序
- 高性能、超大规模的宿主机部署

<a name="eDrNA"></a>
## Docker 特性与能力

1. **文件系统隔离** 每个进程容器运行在完全独立的根（root）文件系统里
2. **进程隔离** 每个容器都运行在自己的进程环境中
3. **资源隔离和分组** 可以使用 cgroup 为每个进程容器分配不同的系统资源，例如 CPU 和内存
4. **网络隔离** 每个进程容器运行在自己的网络命名空间里，拥有自己的虚拟接口和IP地址
5. **写时复制** 采用写时复制创建根文件系统，这让部署变得极其快捷，并且节省内存和硬盘空间
6. **日志记录** Docker 将会搜集和记录没跟进程容器的标准流（stdout、stderr、stdin），用于实时检索或批量检索
7. **变更管理** 容器文件系统的变更可以提交到新的映像中，并可重复使用以创建更多的容器，无需使用模板或手动配置
8. **交互式shell** Docker 可以分配一个虚拟终端并关联到任何容器的标准输入上，例如运行一个一次性交互shell

<a name="8PP1J"></a>
## Docker 工作原理

Docker 使用客户端-服务器（C/S）架构模式。Docker客户端会与Docker守护进程进行通讯。Docker守护进程会处理复杂繁重的任务，例如建立、运行、发布你的Docker容器。Docker客户端和守护进程可以运行在同一个系统上，当然你也可以使用Docker客户端去连接一个远程的Docker守护进程。Docker客户端和守护进程之间通过socket或者RESTful API进行通信。

- **Docker守护进程** Docker守护进程运行在一台主机上。用户并不直接和守护进程进行交互，而是通过Docker客户端简介和其通信。
- **Docker客户端** Docker客户端实际上是Docker的二进制程序，是主要的用户与Docker交互方式。它接收用户指令并且与背后的Docker守护进程通讯，如此来回往复。

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601026606008-e54bbfc1-dd7c-47c8-a58a-cb067e1f1774.png#align=left&display=inline&height=554&originHeight=554&originWidth=1554&size=0&status=done&style=none&width=1554)

<a name="8019ba6a"></a>
## Docker 核心概念
<a name="993785af"></a>
### Docker 镜像 (Docker Image)

我们都知道，操作系统分为内核和用户空间。对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持。而 Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:16.04 就包含了完整的一套 Ubuntu 16.04 最小系统的 root 文件系统。

Docker 镜像是Docker容器运行时的只读模板，每一个镜像有一些列的层（layers）组成。Docker使用UnionFS来将这些层联合到单独的镜像中。UnionFS允许独立于文件系统中的文件和文件夹（称之为分支）被透明覆盖，形成一个单独连贯的文件系统。正因为有了这些层的存在，Docker是如此的轻量。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601026664998-fecd4688-dd7b-4456-ac18-878b6e147839.png#align=left&display=inline&height=187&originHeight=187&originWidth=624&size=0&status=done&style=none&width=624)

当你改变了一个Docker镜像，比如升级到某个程序到新的版本，一个新的层就会被创建。因此，不用替换整个原先的镜像或者重新建立（在使用虚拟机的时候你可能会这么做），只是一个新的层被添加或者升级了。现在你不用重新发布整个镜像，只需要升级，层使得分发Docker镜像变得简单和快速。

在 Docker Store 上有非常多的高质量的官方镜像，有可以直接拿来使用的服务类的镜像，如 nginx、redis、mongo、mysql、httpd、php、tomcat 等；也有一些方便开发、构建、运行各种语言应用的镜像，如 node、openjdk、python、ruby、golang 等。可以在其中寻找一个最符合我们最终目标的镜像为基础镜像进行定制。

如果没有找到对应服务的镜像，官方镜像中还提供了一些更为基础的操作系统镜像，如 ubuntu、debian、centos、fedora、alpine 等，这些操作系统的软件库为我们提供了更广阔的扩展空间。

除了选择现有镜像为基础镜像外，Docker 还存在一个特殊的镜像，名为 scratch。这个镜像是虚拟的概念，并不实际存在，它表示一个空白的镜像。

<a name="a3106bed"></a>
### Docker 容器 (Docker Containers)

Docker容器和文件夹很类似，一个Docker容器包含了所有的某个应用运行所需要的环境。每一个Docker容器都是从Docker镜像创建的。Docker容器可以运行、开始、停止、移动和删除。每一个Docker容器都是单独和安全的应用平台，Docker容器是Docker的运行部分。

镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。也因为这种隔离的特性，很多人初学 Docker 时常常会混淆容器和虚拟机。

每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，我们可以称这个为容器运行时读写而准备的存储层为容器存储层。

容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡。因此，任何保存于容器存储层的信息都会随容器删除而丢失。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601026766159-c830e869-fe0d-4d72-a9f2-f43530fbe778.png#align=left&display=inline&height=174&originHeight=174&originWidth=651&size=0&status=done&style=none&width=651)

要点：容器 = 镜像 + 读写层。并且容器的定义并没有提及是否要运行容器。

**运行态容器**

一个运行态容器（running container）被定义为一个可读写的统一文件系统加上隔离的进程空间和包含其中的进程。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601026809098-f9ec041f-5d0c-4fb2-be75-36ed8dd0e1f9.png#align=left&display=inline&height=198&originHeight=198&originWidth=622&size=0&status=done&style=none&width=622)

<a name="61007794"></a>
### Docker 仓库 (Docker Registeries)

镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，Docker 仓库就是这样的服务。

Docker 仓库用来保存镜像，可以理解为代码控制中的代码仓库。同样的，Docker仓库也有公有和私有的概念。共有的Docker仓库名字是Docker Hub。Docker Hub提供了庞大的镜像集合供使用。这些镜像可以是自己创建，或者在别人的镜像基础上创建。Docker仓库是Docker的分发部分。

一个 Docker 仓库中可以包含多个仓库（Repository）；每个仓库可以包含多个标签（Tag）；每个标签对应一个镜像。

<a name="3b9e5eef"></a>
## Docker 依赖的相关技术
<a name="8ce36dbd"></a>
### Namespaces 命名空间

- PID（Process ID） 进程隔离
- NET（Network） 管理网络接口
- IPC（InterProcess Communication） 管理跨进程通信的访问
- MNT（Mount） 管理挂载点
- UTS（Unix Timesharing System） 隔离内核和版本标识

<a name="8f731ea4"></a>
### Control Groups 控制组

Control Groups 用来分配资源，此技术来源于 Google，在2007年整合进 Linux Kernel 2.6.24 。

Control Groups 有以下作用：

- 资源限制
- 优先级设定
- 资源计量
- 资源控制

<a name="1e0333e2"></a>
### C/S 模式
![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601027524707-8d23c858-d4ae-4413-bf4b-a2ec970a45cb.png#align=left&display=inline&height=188&originHeight=188&originWidth=706&size=0&status=done&style=none&width=706)

连接方式：<br />

- unix://var/run/docker.sock
- tcp://host:port
- fd://socketfd

