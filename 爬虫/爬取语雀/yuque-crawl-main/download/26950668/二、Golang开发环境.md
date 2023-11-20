
本文基于`go version go1.14.2 linux/amd64`

<a name="d4daa7c5"></a>
### 1.下载安装包

Go官网下载地址：`https://golang.org/dl/`

Go官方镜像站（推荐）：`https://golang.google.cn/dl/`

根据自己系统，自行选择安装。

如果是window系统 推荐下载可执行文件版,一路 Next

这里以linux为例。

![](https://img2020.cnblogs.com/blog/1441611/202004/1441611-20200416112615826-2133135972.png#id=zvroP&originHeight=464&originWidth=1164&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

复制tar包连接,然后下载

```bash
cd /usr/src
wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
```

<a name="35ae0872"></a>
### 2.解压安装包

Linux 从 `https://golang.org/dl/` 下载tar⽂件，并将其解压到 `/usr/local`。

将/usr/local/go/bin添加到PATH环境变量中。

```bash
[root@iZ2ze505h9bgsbp83ct28pZ src]# ll
总用量 131008
drwxr-xr-x. 2 root root         6 5月  11 2019 debug
-rw-r--r--  1 root root 123658438 4月   9 06:12 go1.14.2.linux-amd64.tar.gz
drwxr-xr-x. 3 root root        41 3月  29 12:13 kernels
[root@iZ2ze505h9bgsbp83ct28pZ src]# tar -xvf go1.14.2.linux-amd64.tar.gz -C /usr/local/
[root@iZ2ze505h9bgsbp83ct28pZ src]# cd /usr/local/
[root@iZ2ze505h9bgsbp83ct28pZ local]# ls
aegis  bin  etc  games  go  include  lib  lib64  libexec  mysql  sbin  share  src
```

<a name="87dd8d47"></a>
### 3. 在/home下新建go文件夹

```bash
cd /home
mkdir go
```

在/home/go目录里新建下面三个文件夹：

bin / src / pkg

```
cd /home/go
mkdir bin
mkdir src
mkdir pkg
```

![](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650470398898-b212fc73-7077-430d-bdee-7c04e15af23c.png#clientId=ueb8534ac-7151-4&from=paste&id=u40f8ea27&originHeight=184&originWidth=548&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u1d28d98f-543b-4927-8a4d-4a121c89c93&title=)<br />![](https://img2018.cnblogs.com/blog/1441611/201912/1441611-20191218075148240-2006090421.png#id=WlaTd&originHeight=244&originWidth=571&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
<a name="32f3d0ab"></a>
### 4.配置GOROOT

把`/usr/local/go/bin`目录配置GOROOT 到环境变量里

```
sodu vim /etc/profile
```

![](https://img2018.cnblogs.com/blog/1441611/201912/1441611-20191218074620346-81544102.png#id=UjEbn&originHeight=553&originWidth=592&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

```
export GOROOT="/usr/local/go"
export GOPATH=$HOME/go
export GOBIN=$GOROOT/bin
export PATH=$PATH:$GOBIN
```

```
source /etc/profile
go version
go env
```

如果系统变量还是不能生效<br />每次新打开一个命令窗口都要重新输入 source /etc/profile 才能使go env 等配置文件生效：<br />那就加到用户变量,当前用户一登录就会加载到<br />解决方法：

在 `~/.bashrc` 中添加语句（在root账号和子账号里都加一次）

```
source /etc/profile
```

保存退出

```
source /etc/profile 
或者
source $HOME/.profile
```

<a name="5.GOPROXY"></a>
### 5.GOPROXY

Go1.14版本之后，都推荐使用`go mod`模式来管理依赖了，也不再强制我们把代码必须写在`GOPATH`下面的`src`目录了，你可以在你电脑的任意位置编写go代码。

默认GoPROXY配置是：`GOPROXY=https://proxy.golang.org,direct`，<br />由于国内访问不到 `https://proxy.golang.org` 所以我们需要换一个`PROXY`，这里推荐使用`https://goproxy.io` 或 `https://goproxy.cn`。

可以执行下面的命令修改`GOPROXY`：

```
`go env -w GOPROXY=https://goproxy.cn,direct`
```


<a name="dPw1V"></a>
### 6. 开发工具

vscode

![1-vscode.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650470534179-7c88e585-a397-4809-b4d0-9c34b9357bb0.png#clientId=ueb8534ac-7151-4&from=drop&id=u4ace4cdf&originHeight=546&originWidth=954&originalType=binary&ratio=1&rotation=0&showTitle=false&size=97118&status=done&style=none&taskId=u2d630541-3b77-43f9-8fee-6f5fe4ede99&title=)

Goland

![2-goland.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650470543264-9725a31a-047e-4ec0-9c78-84f26cf24541.png#clientId=ueb8534ac-7151-4&from=drop&id=u9cb0db7a&originHeight=512&originWidth=512&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13554&status=done&style=none&taskId=u6de22ae3-26f8-4d90-b39a-d9a1eb91406&title=)
> 本教程非入门级别教程，故开发者可以用自己喜好的IDE进行配置，这里不再梳理IDE的安装和配置，详细请参考其他教学资料

