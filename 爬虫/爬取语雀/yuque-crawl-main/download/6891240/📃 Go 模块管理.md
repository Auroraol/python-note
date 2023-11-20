<a name="xxyrn"></a>
## 一、模块管理基础命令
<a name="Pfeif"></a>
### 初始化模块
```bash
go mod init <模块名>
```
比如：
```bash
go mod init demo
```
初始化后，会在工程目录生成一个 `go.mod` 和 `go.sum` 文件。

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608516872787-0b142527-1e57-453d-990a-7d2bfdacebd6.png#align=left&display=inline&height=40&originHeight=80&originWidth=293&size=7010&status=done&style=none&width=146.5)

<a name="VXdRw"></a>
### 获取模块
使用 `get` 命令获取模块。<br />比如获取gin：
```bash
go get github.com/gin-gonic/gin
```
模块将安装到 `%GOPATH%` 的 `pkg` 下。

安装好之后，打开  `go.mod` 看到：
```go
module demo

go 1.15

require github.com/gin-gonic/gin v1.6.3
```
`go get` 命令的常用标记：

- `-d`：只执行下载动作，而不执行安装动作
- `-fix`：在下载代码包后先执行修正动作，而后再进行编译和安装
- `-u`：利用网络来更新已有的代码包及其依赖包

可以到 [https://pkg.go.dev/](https://pkg.go.dev/) 搜索需要获取的模块

<a name="Qacf1"></a>
### 查看依赖图
使用以下命令查看当前项目的依赖图：
```bash
$ go mod graph
demo github.com/gin-gonic/gin@v1.6.3
```

<a name="v71fo"></a>
### 安装依赖图
如果是从远程仓库克隆的项目，里面包含依赖图，我们需要手动执行以下命令安装依赖图中的模块：
```bash
go mod download
```

<a name="cR2oZ"></a>
## 二、换源

如果拉取依赖缓慢，可以换源到**Goproxy中国**：

- [Goproxy中国 - GitHub](https://github.com/goproxy)
- [Goproxy中国 - 官网](https://goproxy.cn/)

执行以下命令即可：
```go
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```

查看所有已经配置的环境变量：
```go
$ go env
set GO111MODULE=on
set GOARCH=amd64
set GOBIN=
set GOCACHE=C:\Users\quanzaiyu\AppData\Local\go-build
set GOENV=C:\Users\quanzaiyu\AppData\Roaming\go\env
set GOEXE=.exe
set GOFLAGS=
set GOHOSTARCH=amd64
set GOHOSTOS=windows
set GOINSECURE=
set GOMODCACHE=D:\Users\quanzaiyu\go\pkg\mod
set GONOPROXY=
set GONOSUMDB=
set GOOS=windows
set GOPATH=D:\Users\quanzaiyu\go
set GOPRIVATE=
set GOPROXY=https://goproxy.cn,direct
set GOROOT=D:\Development\Go
set GOSUMDB=sum.golang.org
set GOTMPDIR=
set GOTOOLDIR=D:\Development\Go\pkg\tool\windows_amd64
set GCCGO=gccgo
set AR=ar
set CC=gcc
set CXX=g++
set CGO_ENABLED=1
set GOMOD=D:\Workplace\temp\go_learn\go.mod
set CGO_CFLAGS=-g -O2
set CGO_CPPFLAGS=
set CGO_CXXFLAGS=-g -O2
set CGO_FFLAGS=-g -O2
set CGO_LDFLAGS=-g -O2
set PKG_CONFIG=pkg-config
set GOGCCFLAGS=-m64 -mthreads -fmessage-length=0 -fdebug-prefix-map=C:\Users\QUANZA~1\AppData\Local\Temp\go-build015280026=/tmp/go-build -gno-record-gcc-s
witches
```

除此之外，还可以使用包管理工具：[gopm](https://github.com/gpmgo/gopm)

<a name="dJ73s"></a>
## 三、构建和安装
使用以下命令将在工程目录下构建一个 `exe` 文件：
```go
go build
```
使用以下命令将在 `%GOPAHT%/bin` 下安装构建好的 `exe` 文件：
```go
go install
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608518436620-e69f241b-9631-4f4b-827a-e34656168dc1.png#align=left&display=inline&height=48&originHeight=95&originWidth=686&size=14771&status=done&style=none&width=343)

<a name="KilLm"></a>
## 四、其他命令
<a name="3INyP"></a>
### go mod tidy
整理依赖，比如清理掉无用的模块，添加用到的依赖。
```go
go mod tidy
```

<a name="wamH3"></a>
### go mod verify
验证依赖，比如在依赖中包含了错误的版本号，会给出错误提示。
```go
// 未通过验证的情况
$ go mod verify
go: github.com/gin-gonic/gin@v1.6.4: reading github.com/gin-gonic/gin/go.mod at revision v1.6.4: unknown revision v1.6.4

// 通过验证的情况
$ go mod verify
all modules verified
```
`verify` 还会检查依赖包中的文件是否被修改，若被修改也会给出错误提示。

<a name="xglBH"></a>
### go mod why
询问某个依赖在项目中使用与否：
```go
go mod why -m github.com/gin-gonic/gin
```
此命令使用频率不高。

<a name="QbshI"></a>
### go mod edit
先查看一下 `go mod edit` 的用法：
```go
$ go help mod edit
usage: go mod edit [editing flags] [go.mod]
...
```
修改当前模块的名字为test：
```go
go mod edit -module test
```
修改go的版本号：
```go
go mod edit -go=1.12
```
格式化 `go.mod` 文件：
```go
go mod edit -fmt
```
将某个依赖添加到项目中：
```go
go mod edit -require github.com/gin-gonic/gin@v1.6.3
```
排除某个依赖，被排除的依赖不能被拉取和安装：
```go
go mod edit -exclude github.com/gin-gonic/gin@v1.6.3
```

<a name="lOm3U"></a>
### go mod vendor
将项目中的依赖在 `vendor` 文件夹中复制一份
```go
go mod vendor
```

<a name="CBRm3"></a>
### go list
列出当前项目用到的所有依赖：
```go
go list -m all
```

