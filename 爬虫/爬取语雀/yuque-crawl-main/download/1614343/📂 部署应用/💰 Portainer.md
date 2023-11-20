<a name="5VIsS"></a>
## 一、Portainer简介

[Portainer](https://www.portainer.io/)是一个可视化的容器镜像的图形管理工具，利用Portainer可以轻松构建，管理和维护Docker环境。 而且完全免费，基于容器化的安装方式，方便高效部署。

<a name="rsC5I"></a>
## 二、安装Portainer
添加仓库并更新：
```bash
helm repo add portainer https://portainer.github.io/k8s/
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create namespace portainer
```
部署Portainer：
```bash
helm install -n portainer portainer portainer/portainer --set service.type=ClusterIP
```
部署完，可以在Dashboard中看到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603855616074-e9328e4c-7527-4be4-a64f-bb02cfb6ede0.png#align=left&display=inline&height=496&originHeight=496&originWidth=1737&size=51456&status=done&style=none&width=1737)

更多安装方式参考：[https://www.portainer.io/installation/](https://www.portainer.io/installation/)

<a name="RPp8L"></a>
## 三、暴露Portainer管理界面
首先在hosts中添加：
```bash
127.0.0.1    portainer.dashboard.com
```
创建一个 IngressRoute：
```bash
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: portainer-route
  namespace: portainer
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`portainer.dashboard.com`)
      kind: Rule
      services:
        - name: portainer
          port: 9000
```
应用即可：
```bash
kubectl apply -f portainer/route.yaml
```

<a name="WHbeu"></a>
## 四、用于管理Kubernetes
第一次访问 [http://portainer.dashboard.com/](http://portainer.dashboard.com/) 即可看到注册页面：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603855819735-b10b90ea-f674-4513-a90a-1149bbda9a62.png#align=left&display=inline&height=546&originHeight=546&originWidth=821&size=39016&status=done&style=none&width=821)<br />选择部署环境为Kubernetes：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603855862202-6d6e6317-2643-4168-b485-261246c2e3da.png#align=left&display=inline&height=457&originHeight=457&originWidth=1158&size=47789&status=done&style=none&width=1158)<br />完成后，可以进入到管理主页：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603856032851-62e7b1b6-1d14-404f-bc97-66e66baef938.png#align=left&display=inline&height=552&originHeight=552&originWidth=1897&size=141047&status=done&style=none&width=1897)

<a name="Ch1lP"></a>
## 五、Kubernetes管理界面概述
<a name="8PuQX"></a>
### 资源池
资源池就相当于在Kubernetes Dashboard中看到的命名空间，通过Portainer管理界面可以可视化创建资源池。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866332682-842461de-64f6-4a86-9d9d-c75ccf01a6d6.png#align=left&display=inline&height=421&originHeight=421&originWidth=1893&size=76353&status=done&style=none&width=1893)<br />比如我们创建一个test资源池，可以指定资源池的限额（分配内存和CPU）：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866369302-bbfe788c-2d61-4fd3-b955-6d2721e5df6e.png#align=left&display=inline&height=539&originHeight=539&originWidth=1914&size=81766&status=done&style=none&width=1914)<br />创建好后，在Kubernetes Dashboard和Portainer中同时可以看到这个命名空间（资源池）：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866404154-291e6802-a5c8-4bd0-991b-4b4029b0f2f0.png#align=left&display=inline&height=356&originHeight=356&originWidth=596&size=19022&status=done&style=none&width=596)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866429718-8dd9adcf-60ed-47b5-8119-5671692e4127.png#align=left&display=inline&height=109&originHeight=109&originWidth=453&size=6085&status=done&style=none&width=453)<br />通过命令也可以看到：
```bash
$ kubectl get ns
NAME                   STATUS   AGE
default                Active   31d
jenkins                Active   29d
kube-node-lease        Active   31d
kube-public            Active   31d
kube-system            Active   31d
kubernetes-dashboard   Active   29d
nginx                  Active   29d
portainer              Active   3h11m
test                   Active   99s
traefik                Active   21h
```

对于已存在的资源池，可以打开开关调整其限额：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866713383-694f450b-9195-4eea-b46b-3de2735387db.png#align=left&display=inline&height=625&originHeight=625&originWidth=1651&size=58683&status=done&style=none&width=1651)

<a name="9p6qJ"></a>
### 应用
在“应用”界面，可以看到集群中部署的所有应用程序：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603867101708-115094d0-0611-47d0-92f0-94383f36d038.png#align=left&display=inline&height=667&originHeight=667&originWidth=1907&size=132800&status=done&style=none&width=1907)<br />点击具体的应用，查看详情：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866961544-8801e5d2-0f4a-4131-97fc-d2e4177a2516.png#align=left&display=inline&height=340&originHeight=340&originWidth=1628&size=29131&status=done&style=none&width=1628)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866976733-b75e474b-752b-4006-a273-c757c5bfa4ad.png#align=left&display=inline&height=325&originHeight=325&originWidth=1636&size=31727&status=done&style=none&width=1636)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603866996043-8c3df770-4c6e-4b93-9599-6c6260834538.png#align=left&display=inline&height=618&originHeight=618&originWidth=1628&size=49876&status=done&style=none&width=1628)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603867017657-0eedc643-8c44-4f37-a618-a6962afda896.png#align=left&display=inline&height=694&originHeight=694&originWidth=1633&size=75951&status=done&style=none&width=1633)<br />查看所有应用暴露的端口：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603867184474-1b3b91ff-39e5-44d3-b015-80ad63292d69.png#align=left&display=inline&height=430&originHeight=430&originWidth=1640&size=57183&status=done&style=none&width=1640)

<a name="LylWL"></a>
### 配置
在“配置”界面，可以看到所有的配置列表：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603867329186-046b123a-f7e5-4d62-b6c9-44c2aaa0e58d.png#align=left&display=inline&height=551&originHeight=551&originWidth=1895&size=115215&status=done&style=none&width=1895)

<a name="ntiHA"></a>
### 卷与存储
管理所有的卷与存储：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603867408411-5ea24acd-afa0-485d-b7e8-fe1c98b7e482.png#align=left&display=inline&height=368&originHeight=368&originWidth=1905&size=51765&status=done&style=none&width=1905)

<a name="F07pH"></a>
## 六、用于管理Docker
注意到，在刚安装的时候会让选择接入点：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603887585942-00a7203a-a942-43be-a19b-745022be06c4.png#align=left&display=inline&height=561&originHeight=561&originWidth=1151&size=60827&status=done&style=none&width=1151)<br />如果选择Docker，提示在启动的时候需要挂载以下卷，在未使用Helm部署，而是使用 `docker run` 部署时需要添加以下选项：
```bash
-v "/var/run/docker.sock:/var/run/docker.sock" (Linux).
-v \\.\pipe\docker_engine:\\.\pipe\docker_engine (Windows).
```

我们第一次进去选择的是Kubernetes，进入管理界面后，这时我们想要切换到Docker管理该怎么办呢？

首先需要在Docker Desktop中暴露2375端口：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889159018-6ab51bf4-49e7-408e-a541-789000cd7d12.png#align=left&display=inline&height=720&originHeight=720&originWidth=1250&size=77764&status=done&style=none&width=1250)

然后到Endpoints中点击添加按钮：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889069360-6c147022-147d-468e-a0fc-a299840cfdf9.png#align=left&display=inline&height=103&originHeight=103&originWidth=272&size=4218&status=done&style=none&width=272)<br />选择Docker，输入以下信息：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889043331-1669a1ea-bb82-4320-ad9f-e029a97f67b9.png#align=left&display=inline&height=830&originHeight=830&originWidth=1899&size=118749&status=done&style=none&width=1899)<br />其中Endpoint URL 填写 `docker.for.win.localhost:2375` 即可。

创建成功后，即可看到接入点新增了Docker的管理。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889328264-8017a35b-d6bb-4f21-9398-f9a2b769c810.png#align=left&display=inline&height=450&originHeight=450&originWidth=1900&size=86676&status=done&style=none&width=1900)

<a name="pk6d5"></a>
## 七、Docker管理界面概述
<a name="dh7oL"></a>
### 镜像管理
在镜像管理界面，可以看到所有本地已拉取的镜像列表：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889510056-50b80dc4-4a1a-4f6c-824f-7360c2f49855.png#align=left&display=inline&height=650&originHeight=650&originWidth=1891&size=168972&status=done&style=none&width=1891)<br />还可以可视化地拉取镜像<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889571667-65822f28-46d6-463b-9103-68f193725bbf.png#align=left&display=inline&height=328&originHeight=328&originWidth=1630&size=23810&status=done&style=none&width=1630)

<a name="Mb8bz"></a>
### 容器管理
列举所有容器，可视化地对容器进行启停、删除等操作：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889623335-e697a623-1ff1-4f4a-989c-a786ebbc2dfb.png#align=left&display=inline&height=633&originHeight=633&originWidth=1906&size=157704&status=done&style=none&width=1906)<br />也可以可视化地创建容器：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603889703406-f1987af7-fbbd-47be-bb68-5426ccfbadaf.png#align=left&display=inline&height=902&originHeight=902&originWidth=1649&size=100071&status=done&style=none&width=1649)

<a name="MopRD"></a>
## 参考资料

- [可视化图形工具Portainer](http://www.yunweipai.com/34991.html)


