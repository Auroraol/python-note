<a name="xzTHl"></a>
## 一、Helm 简介

[Helm](https://www.kubernetes.org.cn/tags/helm)是 Kubernetes 的一个包管理工具，用来简化 Kubernetes 应用的部署和管理。可以把 Helm 比作 CentOS 的 yum 工具。

使用 Helm 可以完成以下事情：

- 管理 Kubernetes manifest files
- 管理 Helm 安装包 charts
- 基于 chart 的 Kubernetes 应用分发

Helm 可以使用 Charts 启动 Kubernetes 集群，提供可用的工作流：

- 一个 Redis 集群<br />
- 一个 Postgres 数据库<br />
- 一个 HAProxy 边界负载均衡<br />

Helm 基本架构如下图：<br />![c5d01266eef21038b43b2666c29decf9.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1601780663636-54c14366-49c0-40d5-9db6-99c629cd83f8.jpeg#align=left&display=inline&height=553&originHeight=553&originWidth=1162&size=73255&status=done&style=none&width=1162)

<a name="yTC95"></a>
### Helm 产生原因

利用Kubernetes部署一个应用，需要Kubernetes原生资源文件如deployment、replicationcontroller、service或pod 等。而对于一个复杂的应用，会有很多类似上面的资源描述文件，如果有更新或回滚应用的需求，可能要修改和维护所涉及的大量资源文件，且由于缺少对发布过的应用版本管理和控制，使Kubernetes上的应用维护和更新等面临诸多的挑战，而Helm可以帮我们解决这些问题。

<a name="1ce344a2"></a>
### Helm 的基本概念

- Chart: 是 Helm 管理的安装包，里面包含需要部署的安装包资源。可以把 Chart 比作 CentOS yum 使用的 rpm 文件。每个 Chart 包含下面两部分：
   - 包的基本描述文件 Chart.yaml
   - 放在 templates 目录中的一个或多个 Kubernetes manifest 文件模板
- Release：是 chart 的部署实例，一个 chart 在一个 Kubernetes 集群上可以有多个 release，即这个 chart 可以被安装多次
- Repository：chart 的仓库，用于发布和存储 chart

<a name="dUci1"></a>
### Helm 的用途

做为Kubernetes的一个包管理工具，Helm具有如下功能：

- 创建新的chart<br />
- chart打包成tgz格式<br />
- 上传chart到chart仓库或从仓库中下载chart<br />
- 在Kubernetes集群中安装或卸载chart<br />
- 管理用Helm安装的chart的发布周期

<a name="WUJHW"></a>
### Helm 的特性

- 查找并使用流行的软件，将其打包为 Helm Charts，以便在 Kubernetes 中运行<br />
- 以 Helm Charts 的形式共享您自己的应用程序<br />
- 为您的 Kubernetes 应用程序创建可复制的构建<br />
- 智能地管理 Kubernetes 清单文件
- 管理 Helm 包的发行版<br />

<a name="NXRFl"></a>
### Helm 的组成

Helm 由两部分组成，客户端 helm 和服务端 tiller。

- tiller 运行在 Kubernetes 集群上，管理 chart 安装的 release
- helm 是一个命令行工具，可在本地运行，一般运行在 CI/CD Server 上。

<a name="ogDuj"></a>
### Helm 的实现

**Helm client**

- Helm client采用go语言编写，采用gRPC协议与Tiller server交互。

**Helm server**

- Tiller server也同样采用go语言编写，提供了gRPC server与client进行交互，利用Kubernetes client 库与Kubernetes进行通信，当前库使用了REST+JSON格式。
- Tiller server 没有自己的数据库，目前使用Kubernetes的ConfigMaps存储相关信息

<a name="x8Mp2"></a>
### Helm 组件及相关术语

- **Helm** Helm 是一个命令行下的客户端工具。主要用于 Kubernetes 应用程序 Chart 的创建、打包、发布以及创建和管理本地和远程的 Chart 仓库。
- **Tiller** Tiller 是 Helm 的服务端，部署在 Kubernetes 集群中。Tiller 用于接收 Helm 的请求，并根据 Chart 生成 Kubernetes 的部署文件（ Helm 称为 Release ），然后提交给 Kubernetes 创建应用。Tiller 还提供了 Release 的升级、删除、回滚等一系列功能。
- **Chart** Helm 的软件包，采用 TAR 格式。类似于 APT 的 DEB 包或者 YUM 的 RPM 包，其包含了一组定义 Kubernetes 资源相关的 YAML 文件。
- **Repoistory** Helm 的软件仓库，Repository 本质上是一个 Web 服务器，该服务器保存了一系列的 Chart 软件包以供用户下载，并且提供了一个该 Repository 的 Chart 包的清单文件以供查询。Helm 可以同时管理多个不同的 Repository。
- **Release** 使用 helm install 命令在 Kubernetes 集群中部署的 Chart 称为 Release。

注：需要注意的是：Helm 中提到的 Release 和我们通常概念中的版本有所不同，这里的 Release 可以理解为 Helm 使用 Chart 包部署的一个应用实例。

<a name="98Lwp"></a>
### Helm 工作原理

**Chart Install 过程**

- Helm 从指定的目录或者 tgz 文件中解析出 Chart 结构信息
- Helm 将指定的 Chart 结构和 Values 信息通过 gRPC 传递给 Tiller
- Tiller 根据 Chart 和 Values 生成一个 Release
- Tiller 将 Release 发送给 Kubernetes 用于生成 Release

**Chart Update 过程**

- Helm 从指定的目录或者 tgz 文件中解析出 Chart 结构信息
- Helm 将要更新的 Release 的名称和 Chart 结构，Values 信息传递给 Tiller
- Tiller 生成 Release 并更新指定名称的 Release 的 History
- Tiller 将 Release 发送给 Kubernetes 用于更新 Release

**Chart Rollback 过程**

- Helm 将要回滚的 Release 的名称传递给 Tiller
- Tiller 根据 Release 的名称查找 History
- Tiller 从 History 中获取上一个 Release
- Tiller 将上一个 Release 发送给 Kubernetes 用于替换当前 Release

<a name="f522aedc"></a>
## 二、Helm 安装

最新版二进制文件下载地址：[https://github.com/helm/helm/releases](https://github.com/helm/helm/releases)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603954873619-36e9431d-0e03-4f3d-a12b-d352c0ce228f.png#align=left&display=inline&height=394&originHeight=394&originWidth=1004&size=62500&status=done&style=none&width=1004)


方式一：使用官方提供的脚本一键安装
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
chmod 744 get_helm.sh
./get_helm.sh
```

方式二：手动下载安装（以v2为例，安装的时候换为最新版本）
```bash
wget https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-amd64.tar.gz
tar -zxvf helm-v2.9.1-linux-amd64.tar.gz
mv helm-v2.9.1-linux-amd64/helm /usr/local/bin/helm
```

或者：
```bash
wget https://get.helm.sh/helm-v3.4.0-linux-amd64.tar.gz
tar xf helm-v3.4.0-linux-amd64.tar.gz
cd linux-amd64
cp helm /usr/local/bin/
```

检测安装：<br />
```bash
$ helm version
Client: &version.Version{SemVer:"v2.9.1", GitCommit:"20adb27c7c5868466912eebdf6664e7390ebe710", GitTreeState:"clean"}
Error: could not find tiller

$ helm help
```
因为没有安装 tillerServer 所以会报找不到 tiller

初始化:
```bash
helm init
```

先在 K8S 集群上每个节点安装 socat 软件 (`yum install -y socat`)，不然会报如下错误：
```bash
E0522 22:22:15.492436   24409 portforward.go:331] an error occurred forwarding 38398 -> 44134: error forwarding port 44134 to pod dc6da4ab99ad9c497c0cef1776b9dd18e0a612d507e2746ed63d36ef40f30174, uid : unable to do port forwarding: socat not found.
Error: cannot connect to Tiller
```

由于 Helm 默认会去 `storage.googleapis.com` 拉取镜像，如果你当前执行的机器不能访问该域名的话可以使用以下命令来安装：
```bash
helm init --client-only --stable-repo-url https://aliacs-app-catalog.oss-cn-hangzhou.aliyuncs.com/charts/
```

:::info
如果是Windows，直接到[https://github.com/helm/helm/releases](https://github.com/helm/helm/releases)下载最新版本即可（本文写作时最新版为v3.4.0），然后解压，将 `helm.exe` 所在路径添加到PATH环境变量。
:::
其他安装方式：

- [Homebrew](https://brew.sh/) 用户使用 `brew install kubernetes-helm`<br />
- [Chocolatey](https://chocolatey.org/) 用户使用 `choco install kubernetes-helm`<br />
- [Scoop](https://scoop.sh/) 用户使用 `scoop install helm`<br />
- [GoFish](https://gofi.sh/) 用户使用 `gofish install helm`<br />
- [Snap](https://snapcraft.io/) 用户使用 `sudo snap install helm --classic`<br />

<a name="83da323d"></a>
## 三、Helm 换源

若遇到以下错误：<br />
```
Unable to get an update from the “stable” chart repository (https://kubernetes-charts.storage.googleapis.com)
```

手动更换 stable 存储库为阿里云的存储库即可：<br />
```bash
helm repo remove stable # 先移除原先的仓库
helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts # 添加新的仓库地址
helm repo update # 更新仓库
```

添加源：<br />
```bash
helm repo add incubator https://aliacs-app-catalog.oss-cn-hangzhou.aliyuncs.com/charts-incubator/
helm repo update
```

<a name="a8f37d90"></a>
## 四、Helm 服务端 Tiller

tiller server 是helm的服务端，是k8s apiserver的客户端。helm 通过tiller server 获取chart仓库的chart模板文件，通过对value文件的复制，使用tiller server 向apiserver发送资源管理请求，从而生成release。

<a name="vyb1F"></a>
### 安装 TillerServer
所有节点下载 `tiller:v[helm-version]` 镜像，helm-version 为 helm 的版本 2.9.1
```bash
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.9.1
yum install socat -y
```

使用 helm init 安装 tiller：
```bash
$ helm init --tiller-image registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.9.1
$HELM_HOME has been configured at /root/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
```

再次检测：
```bash
$ helm version
Client: &version.Version{SemVer:"v2.9.1", GitCommit:"20adb27c7c5868466912eebdf6664e7390ebe710", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.9.1", GitCommit:"20adb27c7c5868466912eebdf6664e7390ebe710", GitTreeState:"clean"}
```

查看集群：<br />
```bash
$ ksys get pod,svc | grep tiller
pod/tiller-deploy-57fb6f4785-8l9dn          1/1     Running             0          10m
service/tiller-deploy          ClusterIP   10.104.198.59    <none>        44134/TCP                10m
```

创建服务端：<br />
```bash
helm init --service-account tiller --upgrade -i registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.13.1  --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
```

创建 TLS 认证服务端，参考地址：[https://github.com/gjmzj/kubeasz/blob/master/docs/guide/helm.md](https://github.com/gjmzj/kubeasz/blob/master/docs/guide/helm.md)

```bash
helm init --service-account tiller --upgrade -i registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.13.1 --tiller-tls-cert /etc/kubernetes/ssl/tiller001.pem --tiller-tls-key /etc/kubernetes/ssl/tiller001-key.pem --tls-ca-cert /etc/kubernetes/ssl/ca.pem --tiller-namespace kube-system --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
```

在 Kubernetes 中安装 Tiller 服务，因为官方的镜像因为某些原因无法拉取，使用-i 指定自己的镜像，可选镜像：registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.13.1（阿里云），该镜像的版本与 helm 客户端的版本相同，使用 helm version 可查看 helm 客户端版本。

如果在用 helm init 安装 tiller server 时一直部署不成功,检查 deployment，根据描述解决问题。

<a name="8abe6ecb"></a>
### 卸载 Helm 服务器端 Tiller

如果你需要在 Kubernetes 中卸载已部署的 Tiller，可使用以下命令完成卸载。

```bash
helm reset 或
helm reset --force
```

<a name="6b67c31b"></a>
### 给 Tiller 授权
因为 Helm 的服务端 Tiller 是一个部署在 Kubernetes 中 kube-system 命名空间下的 Deployment，它会去连接 Kube-Api 在 Kubernetes 里创建和删除应用。

而从 Kubernetes 1.6 版本开始，API Server 启用了 RBAC 授权。目前的 Tiller 部署时默认没有定义授权的 ServiceAccount，这会导致访问 API Server 时被拒绝。所以我们需要明确为 Tiller 部署添加授权。

创建 Kubernetes 的服务帐号和绑定角色：
```bash
kubectl create serviceaccount tiller -n kube-system
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
```

为 Tiller 设置帐号：
```bash
# 使用 kubectl patch 更新 API 对象
$ kubectl patch deploy -n kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
deployment.extensions "tiller-deploy" patched
```

查看是否授权成功：<br />
```bash
$ kubectl get deploy -n kube-system tiller-deploy -o yaml | grep serviceAccount
serviceAccount: tiller
serviceAccountName: tiller
```

验证 Tiller 是否安装成功：<br />
```bash
$ kubectl -n kube-system get pods | grep tiller
tiller-deploy-6d68f5c78f-nql2z          1/1       Running   0          5m

$ helm version
Client: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5d39fbb4", GitTreeState:"clean"}
```

<a name="a7c3ef0c"></a>
## 五、Helm 使用
<a name="jNBrE"></a>
### 查看帮助
使用 `helm -h` 查看Helm的帮助信息：
```bash
$ helm -h
The Kubernetes package manager

Common actions for Helm:

- helm search:    search for charts
- helm pull:      download a chart to your local directory to view
- helm install:   upload the chart to Kubernetes
- helm list:      list releases of charts

Environment variables:

| Name                               | Description                                                                       |
|------------------------------------|-----------------------------------------------------------------------------------|
| $HELM_CACHE_HOME                   | set an alternative location for storing cached files.                             |
| $HELM_CONFIG_HOME                  | set an alternative location for storing Helm configuration.                       |
| $HELM_DATA_HOME                    | set an alternative location for storing Helm data.                                |
| $HELM_DRIVER                       | set the backend storage driver. Values are: configmap, secret, memory, postgres   |
| $HELM_DRIVER_SQL_CONNECTION_STRING | set the connection string the SQL storage driver should use.                      |
| $HELM_NO_PLUGINS                   | disable plugins. Set HELM_NO_PLUGINS=1 to disable plugins.                        |
| $KUBECONFIG                        | set an alternative Kubernetes configuration file (default "~/.kube/config")       |

Helm stores cache, configuration, and data based on the following configuration order:

- If a HELM_*_HOME environment variable is set, it will be used
- Otherwise, on systems supporting the XDG base directory specification, the XDG variables will be used
- When no other location is set a default location will be used based on the operating system

By default, the default directories depend on the Operating System. The defaults are listed below:

| Operating System | Cache Path                | Configuration Path             | Data Path               |
|------------------|---------------------------|--------------------------------|-------------------------|
| Linux            | $HOME/.cache/helm         | $HOME/.config/helm             | $HOME/.local/share/helm |
| macOS            | $HOME/Library/Caches/helm | $HOME/Library/Preferences/helm | $HOME/Library/helm      |
| Windows          | %TEMP%\helm               | %APPDATA%\helm                 | %APPDATA%\helm          |

Usage:
  helm [command]

Available Commands:
  completion  generate autocompletions script for the specified shell
  create      create a new chart with the given name
  dependency  manage a chart's dependencies
  env         helm client environment information
  get         download extended information of a named release
  help        Help about any command
  history     fetch release history
  install     install a chart
  lint        examine a chart for possible issues
  list        list releases
  package     package a chart directory into a chart archive
  plugin      install, list, or uninstall Helm plugins
  pull        download a chart from a repository and (optionally) unpack it in local directory
  repo        add, list, remove, update, and index chart repositories
  rollback    roll back a release to a previous revision
  search      search for a keyword in charts
  show        show information of a chart
  status      display the status of the named release
  template    locally render templates
  test        run tests for a release
  uninstall   uninstall a release
  upgrade     upgrade a release
  verify      verify that a chart at the given path has been signed and is valid
  version     print the client version information

Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
  -h, --help                             help for helm
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging

Use "helm [command] --help" for more information about a command.
```

<a name="5lOnL"></a>
### 仓库操作
使用 `helm repo` 可以进行仓库的添加、删除等操作。
```bash
$ helm repo -h

This command consists of multiple subcommands to interact with chart repositories.

It can be used to add, remove, list, and index chart repositories.

Usage:
  helm repo [command]

Available Commands:
  add         add a chart repository
  index       generate an index file given a directory containing packaged charts
  list        list chart repositories
  remove      remove one or more chart repositories
  update      update information of available charts locally from chart repositories

Flags:
  -h, --help   help for repo

Global Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging

Use "helm repo [command] --help" for more information about a command.
```

使用 `helm repo add` 添加仓库：<br />
```bash
$ helm repo add aliyun https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
"aliyun" has been added to your repositories
```

使用 `helm repo list` 列出所有仓库：
```bash
$ helm repo list
NAME     	URL
incubator	https://aliacs-app-catalog.oss-cn-hangzhou.aliyuncs.com/charts-incubator/
stable   	https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
bitnami  	https://charts.bitnami.com/bitnami
monocular	https://helm.github.io/monocular
aliyun   	https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
```

使用 `helm repo remove` 移除仓库：
```bash
helm repo remove aliyun
```

更新仓库：
```bash
helm repo update
```

<a name="yM5AP"></a>
### 查找 Chart
Helm 初始化完成之后，默认配置为使用官方的 k8s chart 仓库。

使用 `helm search` 命令介意查找Chart所在hub和repo。
```bash
$ helm search -h

Search provides the ability to search for Helm charts in the various places
they can be stored including the Helm Hub and repositories you have added. Use
search subcommands to search different locations for charts.

Usage:
  helm search [command]

Available Commands:
  hub         search for charts in the Helm Hub or an instance of Monocular
  repo        search repositories for a keyword in charts

Flags:
  -h, --help   help for search

Global Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging

Use "helm search [command] --help" for more information about a command.
```
通过 `helm search repo` 和 `helm search hub gitlab` 查找可用的 Chart
```bash
$ helm search repo traefik 
NAME            CHART VERSION   APP VERSION     DESCRIPTION
stable/traefik  1.24.1          1.5.3           A Traefik based Kubernetes ingress controller w...
traefik/traefik 9.8.2           2.3.1           A Traefik based Kubernetes ingress controller

$ helm search hub traefik  
URL                                                     CHART VERSION   APP VERSION     DESCRIPTION
https://hub.helm.sh/charts/traefik/traefik              9.8.2           2.3.1           A Traefik based Kubernetes ingress controller
https://hub.helm.sh/charts/kube-ops/traefik             1.0.2           2.3.2           A Traefik based Kubernetes ingress controller
https://hub.helm.sh/charts/itscontained/traefik         9.5.1           2.3.1           A Traefik based Kubernetes ingress controller
https://hub.helm.sh/charts/wener/traefik                9.1.1           2.2.8           A Traefik based Kubernetes ingress controller
https://hub.helm.sh/charts/helm-stable/traefik          1.87.5          1.7.26          A Traefik based Kubernetes ingress controller w...
https://hub.helm.sh/charts/banzaicloud-stable/t...      1.75.1          1.7.12          A Traefik based Kubernetes ingress controller w...
https://hub.helm.sh/charts/dniel/traefik                7.2.6           2.2.0           A Traefik based Kubernetes ingress controller
https://hub.helm.sh/charts/traefik-mesh/traefik...      3.0.5           v1.4.0          Traefik Mesh - Simpler Service Mesh
https://hub.helm.sh/charts/itscontained/traefik...      1.0.2           2.2.0           A minimal forward authentication service that p...
https://hub.helm.sh/charts/k8s-at-home/traefik-...      1.0.1           2.2.0           A minimal forward authentication service that p...
https://hub.helm.sh/charts/platydev/traefik-cer...      0.1.6           1.0             Traefik pre-configured with cert-manager and Le...
https://hub.helm.sh/charts/traefik-mesh/maesh           2.1.2           v1.3.2          Maesh - Simpler Service Mesh
https://hub.helm.sh/charts/kiwigrid/error-pages         0.1.2           1.0             A Helm chart for Kubernetes error pages for tra...
https://hub.helm.sh/charts/dniel/forwardauth            2.0.8           2.0-rc1         A Helm chart for Kubernetes to install Auth0 Au...
```

如果条目太多，可以使用 more 查看更多所有可用的 Chart
```bash
helm search hub traefik | more
```

<a name="2sUK8"></a>
### 安装 Chart
通过 `helm install` 可以安装指定的Chart。
```bash
$ helm install -h                        

This command installs a chart archive.

The install argument must be a chart reference, a path to a packaged chart,
a path to an unpacked chart directory or a URL.

To override values in a chart, use either the '--values' flag and pass in a file
or use the '--set' flag and pass configuration from the command line, to force
a string value use '--set-string'. In case a value is large and therefore
you want not to use neither '--values' nor '--set', use '--set-file' to read the
single large value from file.

    $ helm install -f myvalues.yaml myredis ./redis

or

    $ helm install --set name=prod myredis ./redis

or

    $ helm install --set-string long_int=1234567890 myredis ./redis

or

    $ helm install --set-file my_script=dothings.sh myredis ./redis

You can specify the '--values'/'-f' flag multiple times. The priority will be given to the
last (right-most) file specified. For example, if both myvalues.yaml and override.yaml
contained a key called 'Test', the value set in override.yaml would take precedence:

    $ helm install -f myvalues.yaml -f override.yaml  myredis ./redis

You can specify the '--set' flag multiple times. The priority will be given to the
last (right-most) set specified. For example, if both 'bar' and 'newbar' values are
set for a key called 'foo', the 'newbar' value would take precedence:

    $ helm install --set foo=bar --set foo=newbar  myredis ./redis


To check the generated manifests of a release without installing the chart,
the '--debug' and '--dry-run' flags can be combined.

If --verify is set, the chart MUST have a provenance file, and the provenance
file MUST pass all verification steps.

There are five different ways you can express the chart you want to install:

1. By chart reference: helm install mymaria example/mariadb
2. By path to a packaged chart: helm install mynginx ./nginx-1.2.3.tgz
3. By path to an unpacked chart directory: helm install mynginx ./nginx
4. By absolute URL: helm install mynginx https://example.com/charts/nginx-1.2.3.tgz
5. By chart reference and repo url: helm install --repo https://example.com/charts/ mynginx nginx

CHART REFERENCES

A chart reference is a convenient way of referencing a chart in a chart repository.

When you use a chart reference with a repo prefix ('example/mariadb'), Helm will look in the local
configuration for a chart repository named 'example', and will then look for a
chart in that repository whose name is 'mariadb'. It will install the latest stable version of that chart
until you specify '--devel' flag to also include development version (alpha, beta, and release candidate releases), or
supply a version number with the '--version' flag.

To see the list of chart repositories, use 'helm repo list'. To search for
charts in a repository, use 'helm search'.

Usage:
  helm install [NAME] [CHART] [flags]

Flags:
      --atomic                       if set, the installation process deletes the installation on failure. The --wait flag will be set automatically if --atomic is used
      --ca-file string               verify certificates of HTTPS-enabled servers using this CA bundle
      --cert-file string             identify HTTPS client using this SSL certificate file
      --create-namespace             create the release namespace if not present
      --dependency-update            run helm dependency update before installing the chart
      --description string           add a custom description
      --devel                        use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is ignored
      --disable-openapi-validation   if set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema
      --dry-run                      simulate an install
  -g, --generate-name                generate the name (and omit the NAME parameter)
  -h, --help                         help for install
      --insecure-skip-tls-verify     skip tls certificate checks for the chart download
      --key-file string              identify HTTPS client using this SSL key file
      --keyring string               location of public keys used for verification (default "C:\\Users\\quanzaiyu\\.gnupg\\pubring.gpg")
      --name-template string         specify template used to name the release
      --no-hooks                     prevent hooks from running during install
  -o, --output format                prints the output in the specified format. Allowed values: table, json, yaml (default table)
      --password string              chart repository password where to locate the requested chart
      --post-renderer postrenderer   the path to an executable to be used for post rendering. If it exists in $PATH, the binary will be used, otherwise it will try to look for the executable at the given path (default exec)
      --render-subchart-notes        if set, render subchart notes along with the parent
      --replace                      re-use the given name, only if that name is a deleted release which remains in the history. This is unsafe in production
      --repo string                  chart repository url where to locate the requested chart
      --set stringArray              set values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --set-file stringArray         set values from respective files specified via the command line (can specify multiple or separate values with commas: key1=path1,key2=path2)
      --set-string stringArray       set STRING values on the command line (can specify multiple or separate values with commas: key1=val1,key2=val2)
      --skip-crds                    if set, no CRDs will be installed. By default, CRDs are installed if not already present
      --timeout duration             time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)
      --username string              chart repository username where to locate the requested chart
  -f, --values strings               specify values in a YAML file or a URL (can specify multiple)
      --verify                       verify the package before using it
      --version string               specify the exact chart version to use. If this is not specified, the latest version is used
      --wait                         if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet are in a ready state before marking the release as successful. It will wait for as long as --timeout

Global Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
```

示例：
```bash
helm install traefik traefik/traefik -n traefik
```
解释：

- 从traefik/traefik这个repo获取最新的traefik镜像
- 安装的应用名称为traefik
- 将应用安装到traefik这个命名空间下


查看所有已安装的Chart：<br />
```bash
$ helm list

NAME                REVISION    UPDATED                     STATUS      CHART               NAMESPACE
amber-seal          1           Mon Jul  2 17:29:25 2018    DEPLOYED    nginx-ingress-0.9.5 default
my-release          1           Mon Jul  2 15:19:44 2018    DEPLOYED    spark-0.1.10        default
nonplussed-panther  1           Mon Jul  2 17:27:41 2018    FAILED      nginx-ingress-0.9.5 default
turbulent-tuatara   1           Mon Jul  2 17:31:33 2018    DEPLOYED    monocular-0.6.2     default
```

<a name="aafb440e"></a>
### 删除 Chart
使用 `helm uninstall, del, delete, un` 可以删除已安装的Chart。
```bash
$ helm delete -h

This command takes a release name and uninstalls the release.

It removes all of the resources associated with the last release of the chart
as well as the release history, freeing it up for future use.

Use the '--dry-run' flag to see which releases will be uninstalled without actually
uninstalling them.

Usage:
  helm uninstall RELEASE_NAME [...] [flags]

Aliases:
  uninstall, del, delete, un

Flags:
      --description string   add a custom description
      --dry-run              simulate a uninstall
  -h, --help                 help for uninstall
      --keep-history         remove all associated resources and mark the release as deleted, but retain the release history
      --no-hooks             prevent hooks from running during uninstallation
      --timeout duration     time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)

Global Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging
```
示例：
```bash
# helm delete <chartsName>
helm delete amber-seal
```

<a name="i6HJE"></a>
### 下载 Chart
使用 `helm pull/fetch` 可以将指定的Chart下载到本地，扩展名为 `tgz` 。<br />比如：
```bash
helm fetch traefik/traefik
```
将下载 `gitlab-ce-0.2.1.tgz` 到当前文件夹。<br />将其解压，可以修改里面的yaml再安装，达到自定义的目的。
```bash
tar xf traefik-9.4.3.tgz
```

解压后，可以看到释放了一个 `traefik` 的文件夹，在 `traefik` 的父目录执行：
```bash
helm install traefik traefik -n traefik
```
第一个traefik为安装后的资源名称，第二个traefik为Chart名称，此处即为解压后目录的名称，第三个traefik为命名空间名称。

当然，可以自行修改chart （主要是`values.yaml` ）再进行安装：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603956271531-1654ed07-c0e0-4dbe-aadb-348e670ee94e.png#align=left&display=inline&height=221&originHeight=221&originWidth=245&size=12431&status=done&style=none&width=245)

<a name="9hUZj"></a>
### 查看信息
使用 `helm show/inspect` 可以查看Chart的详细信息
```bash
$ helm show -h
This command consists of multiple subcommands to display information about a chart

Usage:
  helm show [command]

Aliases:
  show, inspect

Available Commands:
  all         show all information of the chart
  chart       show the chart's definition
  readme      show the chart's README
  values      show the chart's values

Flags:
  -h, --help   help for show

Global Flags:
      --add-dir-header                   If true, adds the file directory to the header
      --alsologtostderr                  log to standard error as well as files
      --debug                            enable verbose output
      --kube-apiserver string            the address and the port for the Kubernetes API server
      --kube-context string              name of the kubeconfig context to use
      --kube-token string                bearer token used for authentication
      --kubeconfig string                path to the kubeconfig file
      --log-backtrace-at traceLocation   when logging hits line file:N, emit a stack trace (default :0)
      --log-dir string                   If non-empty, write log files in this directory
      --log-file string                  If non-empty, use this log file
      --log-file-max-size uint           Defines the maximum size a log file can grow to. Unit is megabytes. If the value is 0, the maximum file size is unlimited. (default 1800)
      --logtostderr                      log to standard error instead of files (default true)
  -n, --namespace string                 namespace scope for this request
      --registry-config string           path to the registry config file (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\registry.json")
      --repository-cache string          path to the file containing cached repository indexes (default "C:\\Users\\QUANZA~1\\AppData\\Local\\Temp\\helm\\repository")
      --repository-config string         path to the file containing repository names and URLs (default "C:\\Users\\quanzaiyu\\AppData\\Roaming\\helm\\repositories.yaml")
      --skip-headers                     If true, avoid header prefixes in the log messages
      --skip-log-headers                 If true, avoid headers when opening log files
      --stderrthreshold severity         logs at or above this threshold go to stderr (default 2)
  -v, --v Level                          number for the log level verbosity
      --vmodule moduleSpec               comma-separated list of pattern=N settings for file-filtered logging

Use "helm show [command] --help" for more information about a command.
```
举例：
```bash
$ helm version
version.BuildInfo{Version:"v3.3.4", GitCommit:"a61ce5633af99708171414353ed49547cf05013d", GitTreeState:"clean", GoVersion:"go1.14.9"}

E:\OneDrive\配置\Docker & Kubernetes\deploy\traefik>helm inspect chart traefik/traefik
apiVersion: v2
appVersion: 2.3.1
description: A Traefik based Kubernetes ingress controller
home: https://traefik.io/
icon: https://raw.githubusercontent.com/traefik/traefik/v2.3/docs/content/assets/img/traefik.logo.png
keywords:
- traefik
- ingress
maintainers:
- email: emile@vauge.com
  name: emilevauge
- email: daniel.tomcej@gmail.com
  name: dtomcej
- email: ldez@traefik.io
  name: ldez
name: traefik
sources:
- https://github.com/traefik/traefik
- https://github.com/traefik/traefik-helm-chart
type: application
version: 9.8.2
```

<a name="6Tfft"></a>
## 六、应用示例
<a name="fJepj"></a>
### 安装 Monocular

- [GitHub](https://github.com/helm/monocular)

Monocular 是一个开源软件，用于管理 kubernetes 上以 Helm Charts 形式创建的服务，可以通过它的 web 页面来安装 helm Charts

首先需要安装 `Nginx Ingress controller`，安装的 k8s 集群启用了 RBAC，则一定要加 rbac.create=true 参数, 比如

```bash
helm install stable/nginx-ingress -n nginx-ingress --set controller.hostNetwork=true,rbac.create=true
```

安装 Monocular

```bash
helm repo add monocular https://helm.github.io/monocular
helm install monocular/monocular
```

<a name="TSsQS"></a>
### 安装 Kubeapps

- [kubeapps 官网](https://kubeapps.com/)
- [GitHub](https://github.com/kubeapps/kubeapps/blob/master/docs/user/getting-started.md)

<a name="35808e79"></a>
## 参考资料

- [Helm 官网](https://helm.sh/)
- [Helm中文文档](http://www.coderdocument.com/docs/helm/v2/index.html)
- [Helm GitHub](https://github.com/helm/helm)
- [Helm Releasees](https://github.com/kubernetes/helm/releases)
- [是时候使用 Helm 了：Helm, Kubernetes 的包管理工具](https://www.kubernetes.org.cn/3435.html)
- [kubernetes 之 helm 简介、安装、配置、使用指南](https://blog.csdn.net/bbwangj/article/details/81087911)

