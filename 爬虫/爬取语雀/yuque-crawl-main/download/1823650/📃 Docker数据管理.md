在Docker的使用过程中往往需要对数据进行持久化，或者需要在多个容器之间进行数据共享，所以这就涉及到Docker容器的数据操作。 容器中数据管理主要有两种方式：数据卷和数据卷容器。

1. **数据卷（Data Volumes）** 容器内数据直接映射到本地宿主机。<br />
2. **数据卷容器（Data Volume Containers）**使用特定容器维护数据卷。<br />

<a name="HVCAH"></a>
## 数据卷

数据卷（Data Volume）是一个经过特殊设计的目录，它将主机目录直接映射进容器。可以绕过联合文件系统（UFS），为一个或多个容器提供访问。

数据卷设计的目的，在于数据的永久化，它完全独立于容器的生存周期，因此，**Docker 不会再容器删除时删除其挂载的数据卷，也不会存在类似的垃圾回收机制对容器应用的数据卷进行删除处理。**<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601027337857-5fbe70a9-69ce-4db5-ac3f-ec119509779e.png#align=left&display=inline&height=470&originHeight=667&originWidth=872&size=0&status=done&style=none&width=614)

数据卷的特点：

- 数据卷在容器启动时初始化，如果容器使用的镜像在挂载点包含了数据，这些数据会拷贝到新初始化的数据卷中
- 数据卷存在于宿主机中，可宿主机与容器进行共享
- 数据卷可以在容器间共享和重用
- 可以对数据卷里的内容直接进行修改，修改回马上生效，无论是容器内操作还是本地操作
- 数据卷的变化不会影响镜像的更新
- 卷会一直存在，即使挂载数据卷的容器已经被删除

<a name="f5edff6e"></a>
### 添加数据卷

使用 -v（--volume） 选项为容器添加数据卷，格式如下：
```bash
docker run -it -v hostDirectory:containerDirectory imageName /bin/bash
```
举个例子：
```bash
docker run --name server -v ~/data_volume:/data -it ubuntu /bin/bash
```

其中 `~/data_volume` 为宿主机上的目录，`/data` 为容器中要映射的目录。

<a name="2ffMV"></a>

### 指定访问权限

```bash
$ docker run --name server -v ~/data_volume:/data:ro -it ubuntu /bin/bash
```

在创建容器的时候，可以在数据卷映射参数后面加上访问权限，比如上面的 `ro`，是只读权限。

- `ro` read only
- `rw` read write

<a name="9e416de2"></a>
### 删除数据卷

默认情况下，删除挂载了数据卷的容器并不会删除数据卷，但可以使用以下命令来达到删除容器的同时并删除数据卷的目的：

```bash
docker rm -v [container name]
```

<a name="EErDP"></a>
### Dockerfile 配置数据卷

在使用 Dockerfile 构建包含数据卷的镜像：

```
VOLUME["volumePath1"]
```

:::info
使用 VOLUME 指令需要提供一个数组，指定的都是容器中的路径，在容器启动时不需要添加 -v 指令，系统会自动分配一个宿主机的目录映射到指定的数据卷目录。
:::

<a name="kCz7V"></a>
## 数据卷容器

命名的容器挂载数据卷，其他容器通过挂载这个容器实现数据共享，挂载数据卷的容器就叫做数据卷容器。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601027387561-70d317d3-5fa4-4962-b196-5b4554ee0013.png#align=left&display=inline&height=359&originHeight=607&originWidth=1188&size=0&status=done&style=none&width=703)

挂载数据卷容器的方法：

```bash
$ docker run --volumes-from [CONTAINER NAME]
```

通过数据卷容器，可以在不暴露宿主机映射目录的情况下，使用已知容器创建的数据卷。

数据卷的生命周期一直持续到没有容器使用它为止。

<a name="8yHxI"></a>

### 数据卷备份还原

通过以下命令进行数据卷备份：

```bash
docker run \
  --volumes-from [CONTAINER NAME] \
  -v $(pwd):/backup \
  ubuntu \
  tar cvf /backup/backup.tar [CONTAINER DATA VOLUME]
```
![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601027463441-5987bbab-dde4-4bde-99b4-73caf2573bac.png#align=left&display=inline&height=315&originHeight=315&originWidth=570&size=0&status=done&style=none&width=570)

示例：

```bash
$ docker run \
	--name ubuntu_backup
  --volumes-from container_from \
  -v ~/backup:/backup \
  ubuntu \
  tar cvf /backup/backup.tar /data_volume
```

对以上命令的解释：

1. 使用ubuntu镜像创建一个容器，取名为ubuntu_backup
2. 从container_from容器中所有的数据卷挂载到ubuntu_backup容器中(假设数据卷为`/data_volume`)
3. 将ubuntu_backup容器中的`/backup`目录挂载到宿主机中的`~/backup`目录
4. 使用ubuntu_backup容器中的 `tar cvf` 命令将数据卷目录 `/data_volume` 打包到 `/backup/backup.tar`，达到备份的目的
5. 在宿主机中的`~/backup`下即可看到此tar文件

同样地，使用 `tar xvf` 命令以相同的格式还原一个数据卷：

```bash
$ docker run \
  --volumes-from [CONTAINER NAME] \
  -v $(pwd):/backup \
  ubuntu \
  tar xvf /backup/backup.tar [CONTAINER DATA VOLUME]
```

参考：[Backup, restore, or migrate data volumes](https://docs.docker.com/storage/volumes/#backup-restore-or-migrate-data-volumes)

<a name="PO5an"></a>
### 数据卷容器实例1

1. 拉一个centos的容器镜像
```bash
docker pull centos
```

2. 然后运行这个镜像并创建一个数据卷挂载到/mydata
```bash
docker run -it -v /data:/mydata --name mycentos centos
```

3. 再运行一个容器，在这两个容器中使用--volumes-from来挂载mycentos容器中的数据卷
```bash
docker run -it --volumes-from mycentos --name soncentos1 centos
docker run -it --volumes-from mycentos --name soncentos2 centos
```
此时，容器soncentos1和soncentos2都挂载同一个数据卷到相同的/mydata 目录。三个容器任何一方在该目录下的写入数据，其他容器都可以看到。

<a name="sy6EW"></a>
### 数据卷容器实例2

下面以jenkins为例，示例数据卷容器的创建。

1. 创建一个jenkins容器
```bash
docker run --name jenkins -p 50000:50000 -p 8080:8080 -v /datas/jenkins_home:/var/jenkins_home jenkinsci/blueocean
```

2. 创建数据卷容器
```bash
docker run -it --name jenkins-data --volumes-from jenkins centos
[root@97e52c9ad535 /]# cd /var
[root@97e52c9ad535 var]# ls
adm    crash  empty  games   jenkins_home  lib    lock  mail  opt       run    tmp
cache  db     ftp    gopher  kerberos      local  log   nis   preserve  spool  yp   
[root@97e52c9ad535 var]# exit
```

3. 数据备份
```bash
docker run --volumes-from jenkins-data -v /buckup:/home centos tar cvf /home/jenkins.tar /var/jenkins_home
```

