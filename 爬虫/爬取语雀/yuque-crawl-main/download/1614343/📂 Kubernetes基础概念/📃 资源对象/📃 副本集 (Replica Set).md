副本集 (RS, Replica Set) 被认为 是 "升级版" 的 RC。

RS 也是用于保证与 label selector 匹配的 pod 数量维持在期望状态。副本集对象一般不单独使用，而是作为 Deployment 的理想状态参数使用。

在新版本的 Kubernetes 中建议使用 ReplicaSet 来取代 ReplicationController。ReplicaSet 跟 ReplicationController 没有本质的不同，只是名字不一样，并且 ReplicaSet 支持集合式的 selector。

虽然 ReplicaSet 可以独立使用，但一般还是建议使用 Deployment 来自动管理 ReplicaSet，这样就无需担心跟其他机制的不兼容问题（比如 ReplicaSet 不支持 rolling-update 但 Deployment 支持）。

<a name="efaf622a"></a>
## RS 与 RC 的区别

RC 只支持基于等式的 selector（env=dev 或 environment!=qa），但 RS 还支持新的，基于集合的 selector（version in (v1.0, v2.0)或 env notin (dev, qa)），这对复杂的运维管理很方便。

升级方式

- RS 不能使用 kubectlrolling-update 进行升级
- kubectl rolling-update 专用于 rc
- RS 升级使用 deployment 或者 kubectl replace 命令

社区引入这一 API 的初衷是用于取代 vl 中的 RC，也就是说当 v1 版本被废弃时，RC 就完成了它的历史使命，而由 RS 来接管其工作。

<a name="c8e47354"></a>
## yaml 示例

```yaml
apiVersion: extensions/v1beta1
kind: ReplicaSet
metadata:
  name: lykops-rs
  labels:
    software: apache
    project: lykops
    app: lykops-rs
    version: v1
spec:
  replicas: 2
  selector:
    matchLabels:
      name: lykops-rs
      software: apache
      project: lykops
      app: lykops-rs
      version: v1
  template:
    metadata:
      labels:
        name: lykops-rs
        software: apache
        project: lykops
        app: lykops-rs
        version: v1
    spec:
      containers:
        - name: lykops-rs
          image: web:apache
          command: ["sh", "/etc/run.sh"]
          ports:
            - containerPort: 80
              name: http
```
