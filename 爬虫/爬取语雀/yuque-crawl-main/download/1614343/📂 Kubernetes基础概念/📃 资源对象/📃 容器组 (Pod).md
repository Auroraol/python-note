<a name="LPdm4"></a>
## 一、什么是Pod

Pod 直译是豆荚，是 Kubernetes 最基本的操作单元，包含一个或多个紧密相关的容器。可以把容器想像成豆荚里的豆子，把一个或多个关系紧密的豆子包在一起就是豆荚（一个 Pod）。在 k8s 中我们不会直接操作容器，而是把容器包装成 Pod 再进行管理。

一个 Pod 可以被一个容器化的环境看作应用层的“逻辑宿主机”；一个 Pod 中的多个容器应用通常是紧密耦合的，Pod 在 Node 上被创建、启动或者销毁；每个 Pod 里运行着一个特殊的被称之为 Pause 的容器，其他容器则为业务容器，这些业务容器共享 Pause 容器的网络栈和 Volume 挂载卷，因此他们之间通信和数据交换更为高效，在设计时我们可以充分利用这一特性将一组密切相关的服务进程放入同一个 Pod 中。

同一个 Pod 里的容器之间仅需通过 localhost 就能互相通信。

一个 Pod 中的应用容器共享同一组资源：

- PID 命名空间：Pod 中的不同应用程序可以看到其他应用程序的进程 ID；
- 网络命名空间：Pod 中的多个容器能够访问同一个 IP 和端口范围；
- IPC 命名空间：Pod 中的多个容器能够使用 SystemV IPC 或 POSIX 消息队列进行通信；
- UTS 命名空间：Pod 中的多个容器共享一个主机名；
- Volumes（共享存储卷）：Pod 中的各个容器可以访问在 Pod 级别定义的 Volumes；

Pod 的生命周期通过 Replication Controller 来管理；通过模板进行定义，然后分配到一个 Node 上运行，在 Pod 所包含容器运行结束后，Pod 结束。

Kubernetes 为 Pod 设计了一套独特的网络配置，包括：为每个 Pod 分配一个 IP 地址，使用 Pod 名作为容器间通信的主机名等。

<a name="4aaecd10"></a>
## 二、获取 Pod

```bash
kubectl get pods # 获取default命名空间的pods
kubectl get po -n test # 获取test命名空间的pods
```

在 Kubernetes 集群中 Pod 有如下两种使用方式：

- **一个 Pod 中运行一个容器**。“每个 Pod 中一个容器”的模式是最常见的用法；在这种使用方式中，你可以把 Pod 想象成是单个容器的封装，kuberentes 管理的是 Pod 而不是直接管理容器。
- **在一个 Pod 中同时运行多个容器**。一个 Pod 中也可以同时封装几个需要紧密耦合互相协作的容器，它们之间共享资源。这些在同一个 Pod 中的容器可以互相协作成为一个 service 单位——一个容器共享文件，另一个“sidecar”容器来更新这些文件。Pod 将这些容器的存储资源作为一个实体来管理。

每个 Pod 都是应用的一个实例。如果你想平行扩展应用的话（运行多个实例），你应该运行多个 Pod，每个 Pod 都是一个应用实例。在 Kubernetes 中，这通常被称为 replication。

<a name="bd9ac2e9"></a>
## 三、Pod 中管理多个容器

Pod 中可以同时运行多个进程（作为容器运行）协同工作。同一个 Pod 中的容器会自动的分配到同一个 node 上。同一个 Pod 中的容器共享资源、网络环境和依赖，它们总是被同时调度。

注意在一个 Pod 中同时运行多个容器是一种比较高级的用法。只有当你的容器需要紧密配合协作的时候才考虑用这种模式。例如，你有一个容器作为 web 服务器运行，需要用到共享的 volume，有另一个“sidecar”容器来从远端获取资源更新这些文件，如下图所示：

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597324782310-05d9bf59-ff37-4312-8585-bd882bc76285.png#align=left&display=inline&height=400&originHeight=400&originWidth=600&size=0&status=done&style=none&width=600)

Pod 中可以共享两种资源：网络和存储。

**网络**

每个 Pod 都会被分配一个唯一的 IP 地址。Pod 中的所有容器共享网络空间，包括 IP 地址和端口。Pod 内部的容器可以使用 localhost 互相通信。Pod 中的容器与外界通信时，必须分配共享网络资源（例如使用宿主机的端口映射）。

**存储**

可以为一个 Pod 指定多个共享的 Volume。Pod 中的所有容器都可以访问共享的 volume。Volume 也可以用来持久化 Pod 中的存储资源，以防容器重启后文件丢失。

<a name="f07b648c"></a>
## 四、Pod 的应用场景

实际应用场景中，很少会直接在 kubernetes 中创建单个 Pod。因为 Pod 的生命周期是短暂的，用后即焚的实体。当 Pod 被创建后（不论是由你直接创建还是被其他 Controller），都会被 Kubernetes 调度到集群的 Node 上。直到 Pod 的进程终止、被删掉、因为缺少资源而被驱逐、或者 Node 故障之前这个 Pod 都会一直保持在那个 Node 上。

:::warning
重启 Pod 中的容器跟重启 Pod 不是一回事。Pod 只提供容器的运行环境并保持容器的运行状态，重启容器不会造成 Pod 重启。
:::

Pod 不会自愈。如果 Pod 运行的 Node 故障，或者是调度器本身故障，这个 Pod 就会被删除。同样的，如果 Pod 所在 Node 缺少资源或者 Pod 处于维护状态，Pod 也会被驱逐。Kubernetes 使用更高级的称为 Controller 的抽象层，来管理 Pod 实例。虽然可以直接使用 Pod，但是在 Kubernetes 中通常是使用 Controller 来管理 Pod 的。

Pod 也可以用于垂直应用栈（例如 LAMP），这样使用的主要动机是为了支持共同调度和协调管理应用程序，例如：

- 内容管理系统、文件和数据加载器、本地换群管理器等。
- 日志和检查点备份、压缩、旋转、快照等。
- 数据变更观察者、日志和监控适配器、活动发布者等。
- 代理、桥接和适配器等。
- 控制器、管理器、配置器、更新器等。

通常单个 pod 中不会同时运行一个应用的多个实例。

<a name="80eec28c"></a>
## 五、Pod 的调度

在大部分情况下, Pod 只是容器的载体，虽然可以直接手动管理，但是这样维护起来特别麻烦，我们希望在 Pod 发生问题时自动恢复，而不是手动管理，因此有了以下几种管理 Pod 的方式：

- **副本与副本集 (RC、RS)** 用来管理正常运行 Pod 数量，系统会根据定义好的副本数来创建 Pod 数量。在运行过程中，如果 Pod 数量小于定义的，就会重启停止的或重新分配 Pod，反之则杀死多余的
- **部署 (Deployment)** 部署表示用户对 Kubernetes 集群的一次更新操作。部署是一个比 RS 应用模式更广的 API 对象，可以是创建一个新的服务，更新一个新的服务，也可以是滚动升级一个服务
- **守护进程集 (DaemonSet)** 一个 DaemonSet 对象能确保其创建的 Pod 在集群中的每一台（或指定）Node 上都运行一个副本

<a name="46a26348"></a>
## 六、Pod 的生命周期

下图是 Pod 的生命周期示意图，从图中可以看到 Pod 状态的变化。

![](https://cdn.nlark.com/yuque/0/2020/jpeg/2213540/1597324909484-800cf061-021d-4d22-8864-764d3018568a.jpeg#align=left&display=inline&height=638&originHeight=638&originWidth=1886&size=0&status=done&style=none&width=1886)

Pod 的生命周期包括:

- 挂起（Pending）：Pod 已被 Kubernetes 系统接受，但有一个或者多个容器镜像尚未创建。等待时间包括调度 Pod 的时间和通过网络下载镜像的时间，这可能需要花点时间。
- 运行中（Running）：该 Pod 已经绑定到了一个节点上，Pod 中所有的容器都已被创建。至少有一个容器正在运行，或者正处于启动或重启状态。
- 成功（Succeeded）：Pod 中的所有容器都被成功终止，并且不会再重启。
- 失败（Failed）：Pod 中的所有容器都已终止了，并且至少有一个容器是因为失败终止。也就是说，容器以非 0 状态退出或者被系统终止。
- 未知（Unknown）：因为某些原因无法取得 Pod 的状态，通常是因为与 Pod 所在主机通信失败。

<a name="9491c8ae"></a>
## 七、进入到 Pod

类同于进入 docker 容器:

```bash
docker exec -it <your-container-name> /bin/sh
```

进入 pod:

```bash
kubectl exec -it <your-pod-name> -n <your-namespace> -- /bin/sh
```

<a name="40f5ff6c"></a>
## 八、Pod hook

Pod hook（钩子）是由 Kubernetes 管理的 kubelet 发起的，当容器中的进程启动前或者容器中的进程终止之前运行，这是包含在容器的生命周期之中。可以同时为 Pod 中的所有容器都配置 hook。

Hook 的类型包括两种：

- exec：执行一段命令
- HTTP：发送 HTTP 请求。

参考下面的配置：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: lifecycle-demo
spec:
  containers:
    - name: lifecycle-demo-container
      image: nginx
      lifecycle:
        postStart:
          exec:
            command:
              [
                "/bin/sh",
                "-c",
                "echo Hello from the postStart handler > /usr/share/message",
              ]
        preStop:
          exec:
            command: ["/usr/sbin/nginx", "-s", "quit"]
```

在容器创建之后，容器的 Entrypoint 执行之前，这时候 Pod 已经被调度到某台 node 上，被某个 kubelet 管理了，这时候 kubelet 会调用 postStart 操作，该操作跟容器的启动命令是在异步执行的，也就是说在 postStart 操作执行完成之前，kubelet 会锁住容器，不让应用程序的进程启动，只有在 postStart 操作完成之后容器的状态才会被设置成为 RUNNING。

如果 postStart 或者 preStop hook 失败，将会终止容器。

<a name="576f423c"></a>
## 九、Pod Preset

Preset 就是预设，有时候想要让一批容器在启动的时候就注入一些信息，比如 secret、volume、volume mount 和环境变量，而又不想一个一个的改这些 Pod 的 template，这时候就可以用到 PodPreset 这个资源对象了。

Pod Preset 是用来在 Pod 被创建的时候向其中注入额外的运行时需求的 API 资源。

使用 Pod Preset 使得 pod 模板的作者可以不必为每个 Pod 明确提供所有信息。这样一来，pod 模板的作者就不需要知道关于该服务的所有细节。

<a name="04b6046e"></a>
## 十、Init 容器

Pod 能够具有多个容器，应用运行在容器里面，但是它也可能有一个或多个先于应用容器启动的 Init 容器。

Init 容器与普通的容器非常像，除了如下两点：

- Init 容器总是运行到成功完成为止。
- 每个 Init 容器都必须在下一个 Init 容器启动之前成功完成。

如果 Pod 的 Init 容器失败，Kubernetes 会不断地重启该 Pod，直到 Init 容器成功为止。然而，如果 Pod 对应的 restartPolicy 为 Never，它不会重新启动。

指定容器为 Init 容器，在 PodSpec 中添加 initContainers 字段，以 v1.Container 类型对象的 JSON 数组的形式，还有 app 的 containers 数组。 Init 容器的状态在 status.initContainerStatuses 字段中以容器状态数组的格式返回（类似 status.containerStatuses 字段）。

<a name="2c287dd7"></a>
### 使用 Init 容器

以下是 Kubernetes 1.6 版本的新语法，尽管老的 annotation 语法仍然可以使用。我们已经把 Init 容器的声明移到 `spec` 中：

`myapp.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
    - name: myapp-container
      image: busybox
      command: ["sh", "-c", "echo The app is running! && sleep 3600"]
  initContainers:
    - name: init-myservice
      image: busybox
      command:
        [
          "sh",
          "-c",
          "until nslookup myservice; do echo waiting for myservice; sleep 2; done;",
        ]
    - name: init-mydb
      image: busybox
      command:
        [
          "sh",
          "-c",
          "until nslookup mydb; do echo waiting for mydb; sleep 2; done;",
        ]
```

下面的 YAML 文件展示了包括 `mydb` 和 `myservice` 两个 Service：

`services.yaml`

```yaml
kind: Service
apiVersion: v1
metadata:
  name: myservice
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
---
kind: Service
apiVersion: v1
metadata:
  name: mydb
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9377
```

这个 Pod 可以使用下面的命令进行启动和调试：

```bash
$ kubectl create -f myapp.yaml
pod "myapp-pod" created
$ kubectl get -f myapp.yaml
NAME        READY     STATUS     RESTARTS   AGE
myapp-pod   0/1       Init:0/2   0          6m
$ kubectl describe -f myapp.yaml
$ kubectl logs myapp-pod -c init-myservice # Inspect the first init container
$ kubectl logs myapp-pod -c init-mydb      # Inspect the second init container
```

可以看到, 在 `mydb` 和 `myservice` 服务还未创建之前, STATUS 为 `Init:0/2`, 处于等待服务创建的阶段。

一旦我们启动了 `mydb` 和 `myservice` 这两个 Service，我们能够看到 Init 容器完成，并且 `myapp-pod` 被创建, 其状态为 `Running`：

```bash
$ kubectl create -f services.yaml
service "myservice" created
service "mydb" created
$ kubectl get -f myapp.yaml
NAME        READY     STATUS    RESTARTS   AGE
myapp-pod   1/1       Running   0          9m
```

这个例子非常简单，但是应该能够为我们创建自己的 Init 容器提供一些启发。

<a name="797df4a1"></a>
## 十一、Pod API Object

Pod 是 kubernetes REST API 中的顶级资源类型。

在 kuberentes1.6 的 V1 core API 版本中的 Pod 的数据结构如下图所示：

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597324974628-f7241a85-8ca3-4994-9e58-536ae47000f7.png#align=left&display=inline&height=5188&originHeight=5188&originWidth=3695&size=0&status=done&style=none&width=3695)

