<a name="wT4Xv"></a>
## 一、概述
| ![go128.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608370194961-929008e0-0f51-43af-8895-0ccb5adedee1.png#align=left&display=inline&height=128&originHeight=128&originWidth=128&size=7183&status=done&style=none&width=128) | Go 编程语言是一个开源项目，它使程序员更具生产力。<br />Go是从2007年末由Robert Griesemer, Rob Pike, Ken Thompson主持开发，后来还加入了Ian Lance Taylor, Russ Cox等人，并最终于2009年11月开源，在2012年早些时候发布了Go 1稳定版本。现在Go的开发已经是完全开放的，并且拥有一个活跃的社区。 |
| --- | --- |
| Go 语言具有很强的表达能力，它简洁、清晰而高效。得益于其并发机制，用它编写的程序能够非常有效地利用多核与联网的计算机，其新颖的类型系统则使程序结构变得灵活而模块化。 Go 代码编译成机器码不仅非常迅速，还具有方便的垃圾收集机制和强大的运行时反射机制。 它是一个快速的、静态类型的编译型语言，感觉却像动态类型的解释型语言。 |  |

Go语言自己的早期源码使用C语言和汇编语言写成。从 Go 1.5 版本后，完全使用Go语言自身进行编写。Go语言的源码对了解Go语言的底层调度有极大的参考意义。

- 官网：[https://golang.org](https://golang.org)
- GitHub：[https://github.com/golang/go](https://github.com/golang/go)
- 中文镜像：[https://golang.google.cn](https://golang.google.cn/)

<a name="El7NV"></a>
## 二、下载与安装
到如下地址下载安装：

- [https://golang.org/dl/](https://golang.org/dl/)
- [https://golang.google.cn/dl/](https://golang.google.cn/dl/)

安装完毕后，设置如下环境变量：

- **GOROOT** %DEV_PATH%\go
- **GOPATH** %USER_HOME%\Go
- **PATH** %GOPATH%\bin;%GOROOT%\bin;

假设上述环境变量中的两个路径为：

- **USER_HOME** D:\Users\quanzaiyu
- **DEV_PATH** D:\Development

根据自身安装的实际情况设置。

验证安装：
```go
$ go version
go version go1.15.6 windows/amd64
```

<a name="12ftH"></a>
## 三、第一个Go程序
一个经典的Hello World程序：
```go
package main

import "fmt"

func main() {
  fmt.Println("Hello, World!")
}
```
其中，`main`为入口函数，`package` 声明了包名，`import` 引入其他依赖包。

<a name="PCl5w"></a>
## 四、常用命令
<a name="VYxwM"></a>
### 运行程序
```bash
$ go run index.go
Hello, World!
```
`go run` 命令的常用标记：

- `-a`：强制编译相关代码，不论它们的编译结果是否已是最新的
- `-x`：打印编译过程中所需运行的命令，并执行它们
- `-n`：打印编译过程中所需运行的命令，但并不执行
- `-p n`：并行编译，其中n为并行的数量
- `-v`：列出被编译的代码包的名称
- `-a -v`：列出所有被编译的代码包的名称
   - `go v1.3 中的所有`：包含Go语言自带的标准库的代码包
   - `go v1.4 中的所有`：不包含Go语言自带的标准库的代码包
- `-work`：显示编译时创建的临时工作目录的路径，并且不删除它

<a name="m7ZF2"></a>
### 编译程序
```bash
$ go build index.go
```
在Windows下可以看到编译出了 `exe` 文件，可直接运行：
```bash
$ ./index.exe
Hello, World!
```

<a name="EDmle"></a>
## 参考资料

- [Go语言入门教程](http://c.biancheng.net/golang/)
- [Go语言中文网](https://studygolang.com/)
- [Golang标准库文档](https://studygolang.com/pkgdoc)
- [Golang文档中文版镜像](http://docscn.studygolang.com/)
- [Google公布实现Go 1.5自举的计划](https://studygolang.com/articles/2419)【[英文原文地址](https://www.infoq.com/news/2015/01/golang-15-bootstrapped/)】

