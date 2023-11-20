<a name="8391730d"></a>
## 一、Label 的定义

Label 是 Kubernetes 系统中的一个核心概念。**Label 以 key/value 键值对的形式附加到任何对象上，如 Pod，Service，Node，RC（ReplicationController）/RS（ReplicaSet）等**。Label 可以在创建对象时就附加到对象上，也可以在对象创建后通过 API 进行额外添加或修改。

<a name="TLJzl"></a>
## 二、Label 的表示

在为对象定义好 Label 后，其他对象就可以通过 Label 来对对象进行引用。Label 的最常见的用法便是通过**spec.selector**来引用对象。下面是文章：[Kubernetes 对象之 ReplicaSet](https://www.jianshu.com/p/fd8d8d51741e) 中新建一个 RC 的例子：

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
  labels:
    app: nginx
    release: stable
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          ports:
            - containerPort: 80
```

上面的描述文件为名为 nginx 的 Pod 添加了两个 Label，分别为`app: nginx`和`release: stable`。

关于 Label 的用法重点在于这两步：

- 通过**template.metadata.labels**字段为即将新建的 Pod 附加 Label。
- 通过**spec.selector**字段来指定这个 RC 管理哪些 Pod。在上面的例子中，新建的 RC 会管理所有拥有`app:nginx`Label 的 Pod。这样的**spec.selector**在 Kubernetes 中被称作**Label Selector**。

<a name="caa1c5fe"></a>
### 常见的 Label

一般来说，我们会给一个 Pod（或其他对象）定义多个 Label，以便于配置，部署等管理工作。例如：部署不同版本的应用到不同的环境中；或者监控和分析应用（日志记录，监控，报警等）。通过多个 Label 的设置，我们就可以多维度的 Pod 或其他对象进行精细化管理。一些常用的 Label 示例如下：

```yaml
relase: stable
release: canary
environment: dev
environemnt: qa
environment: production
tier: frontend
tier: backend
tier: middleware
app: nginx
......
```

Label 是自定义的一些 key/value 对，你可以随心所欲的设置。

<a name="a4c4a757"></a>
## 三、Label Selector

Label selector是Kubernetes核心的分组机制，通过label selector客户端/用户能够识别一组有共同特征或属性的资源对象。

带有 Label 的对象创建好之后，我们就可以通过 Label Selector 来引用这些对象。

通常我们通过描述文件中的**spec.selector**字段来指定 Label，从而 Kubernetes 寻找到所有包含你指定 Label 的对象，进行管理。

Kubernetes 目前支持两种类型的 Label Selector：

- 基于等式的 Selector（Equality-based）
- 基于集合的 Selector（Set-based）

RC 只支持基于等式的 Selector，而 RS 两种 Selector 都支持。

<a name="7d5de745"></a>
### 基于等式的 Selector

上文中创建 RC 的例子中的使用的就是基于等式的 Selector。基于等式的 Selector 通过等式类的表达式来进行筛选。例如：

- app=nginx 选择所有 Label 中 key 为 app，value 为 nginx 的对象。
- env!=dev 选择所有 Label 中 key 为 env，value 不等于 dev 的对象。

<a name="4e89a1f4"></a>
### 基于集合的 Selector

基于集合的 Selector 通过集合操作的表达式来进行筛选。例如：

- name in (redis-master, redis-slave) 选择所有 Label 中 key 为 name，并且 value 为 redis-master 或 redis-slave 的对象。
- env not in (dev) 选择所有 Label 中 key 为 env，并且 value 不为 dev 的对象。

使用 Label 可以给对象创建一组或多组标签，Service，RC/RS 等组件则通过 Label Selector 来定位需要管理的对象，Label 和 Label Selector 共同构成了 Kubernetes 系统中最核心的应用模型，使得对象能够精细分组，同时实现了集群的高可用性。

<a name="1YML2"></a>
### Node Selector

Node Selector是指定pod分配到指定node上最简单的方法，使用Pod中的nodeSelector属性来实现。Node Selector会指定key-value pairs，pod会被分配到特定node上，该node具有所有指定key-value pairs对应labels。


<a name="snvHA"></a>
### matchLables 和 matchExpressions

新出现的管理对象如Deploment、ReplicaSet、DaemonSet和Job则可以在Selector中使用基于集合的筛选条件定义，例如：
```yaml
selector:
  matchLabels:
    app: nginx
  matchExpressions:
    - {key: tier, operator: In, values: [frontend]}
    - {key: environment, operator: NorIn, values: [dev]}
```

在使用这些资源的时候，需要注意以下几点：

- 在deployment中必须写spec.selector.matchLabels
- 在定义pod模板时，必须定义spec.template.metadata.lables，因为spec.selector.matchLabels是必须字段，而它又必须和spec.template.metadata.lables的键值一致。<br />
- spec.template.metadata.lables里面定义的内容，会应用到spec.template.spec下定义的所有pod副本中，在spec.template.spec.containers里面不能定义labels标签<br />

<a name="863e3b39"></a>
## 四、对 node 添加标签

使用以下格式的命令对指定的node添加标签：

```bash
kubectl label nodes <node-name> <label-key>=<label-value>
```

示例：

```bash
$ kubectl get nodes
NAME         STATUS   ROLES    AGE    VERSION
k8s-master   Ready    master   171m   v1.14.0
k8s-node1    Ready    <none>   169m   v1.14.0
k8s-node2    Ready    <none>   169m   v1.14.0


$ kubectl label nodes k8s-master traefik=proxy
node/k8s-master labeled

$ kubectl get nodes --show-labels
NAME         STATUS   ROLES    AGE    VERSION   LABELS
k8s-master   Ready    master   172m   v1.14.0   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,traefik=proxy,kubernetes.io/arch=amd64,kubernetes.io/hostname=k8s-master,kubernetes.io/os=linux,node-role.kubernetes.io/master=
k8s-node1    Ready    <none>   171m   v1.14.0   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=k8s-node1,kubernetes.io/os=linux
k8s-node2    Ready    <none>   171m   v1.14.0   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=k8s-node2,kubernetes.io/os=linux
```

可以看到，对 `k8s-master` 添加了 `traefik=proxy` 标签，再次显示所有节点的标签即可看到。

<a name="2e7d38de"></a>
## 五、Label 的其他操作

删除 label, 使用 key 与减号相连, 如:

```bash
kubectl label nodes k8s-master traefik-
```

为各种资源添加标签：

```bash
kubectl label svc test-svc test=svc -n test
kubectl label rc test-controller test=rc -n test
kubectl label rs test-rs test=rs -n test
```

<a name="1c90fbe5"></a>
## 六、污点标记

使用 Taint 规则，将拒绝 Pod 在 Node 上运行。

Taint 需要和 Tolerations 配合使用，让 Pod 避开那些不合适的 Node。在 Node 上设置一个或多个 Taint 之后，除非 Pod 明确声明能够容忍这些“污点”，否则无法在这些 Node 上运行。Toleration 是 Pod 的属性，让 Pod 能够运行在标注了 Taint 的 Node 节点上。

1. 使用 kubectl taint 命令为 Node 设置 Taint 信息：

```bash
kubectl taint nodes nodeName key=value:NoSchedule

# 比如: 禁止 k8s-master1 部署 pod
kubectl taint nodes k8s-master1 node-role.kubernetes.io/master=true:NoSchedule
```

为 node 节点的 k8s-master 加上一个 Taint, Taint 的键为 Key，值为 value, Taint 的效果是 NoSchedule。这里表示的含义是任何 Pod 都不能调度到这个节点，除非设置了 toleration。

2. 删除节点上的 taint

```bash
kubectl taint nodes --all key:NoSchedule-
```

默认的 master 节点是不能调度应用 pod 的，需要给 master 节点消除污点标记

```bash
kubectl taint nodes --all node-role.kubernetes.io/master-
```

<a name="5e361807"></a>
## 七、容忍标记

在 Pod 中定义容忍标记（Tolerate），使得 Pod 可以被调度到具有该污点标记（Taint）的 Node：

```yaml
tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
```

或者：

```yaml
tolerations:
  - key: "key"
    operator: "Exists"
    effect: "NoSchedule"
    tolerationSeconds: 6000
```

- value 的值可以为 NoSchedule、PreferNoSchedule 或 NoExecute。
- tolerationSeconds 是当 pod 需要被驱逐时，可以继续在 node 上运行的时间。

<a name="9z5Ib"></a>
## 八、常见错误
<a name="T2GHY"></a>
### node(s) didn't match node selector

报错如下:

```
0/3 nodes are available: 3 node(s) didn't match node selector.
```

如果指定的 label 在所有 node 上都无法匹配，则创建 Pod 失败，会提示无法调度

对应 yaml 的 nodeSelector 字段, 如:

```yaml
spec:
  nodeSelector:
    traefik: proxy
```

需要为 node 指定标签

```
kubectl label nodes <node-name> <label-key>=<label-value>
```

比如:

```bash
kubectl label nodes k8s-node1 traefik=proxy
```

如果要删除标签:

```bash
kubectl label nodes --all traefik-
```

<a name="xfjWQ"></a>
### missing required field selector

报错如下：
```
error validating data: ValidationError(Deployment.spec): missing required field "selector" in io.k8s.api.apps.v1.DeploymentSpec; if you choose to ignore these errors, turn validation off with --validate=false
```

错误原因：如果不写spec.selector.matchLabels字段的内容，直接创建则会报错：缺少必要字段selector。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

需要正确使用 `matchLabels` ：
```yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

<a name="eMGvN"></a>
### selector does not match template labels

报错如下：
```
spec.template.metadata.labels: Invalid value: map[string]string{"app":"nginx"}: `selector` does not match template `labels`
```
当 spec.selector.matchLabels 匹配的键值与 spec.template.metadata.lables 键值不相对应，会报此错：选择的和模板标签不匹配。

<a name="B5c5o"></a>
## 参考资料

- [Kubernetes Labels 和 Selectors](http://docs.kubernetes.org.cn/247.html)
