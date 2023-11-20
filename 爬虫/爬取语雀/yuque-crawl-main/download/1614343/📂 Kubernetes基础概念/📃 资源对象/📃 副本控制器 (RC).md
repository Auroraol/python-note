副本控制器 (RC, Replication Controller) 保证在同一时间能够运行指定数量的 Pod 副本，保证 Pod 总是可用。如果实际 Pod 数量比指定的多就结束掉多余的，如果实际数量比指定的少就启动缺少的。当 Pod 失败、被删除或被终结时 RC 会自动创建新的 Pod 来保证副本数量。所以即使只有一个 Pod 也应该使用 RC 来进行管理。

**确保 pod 数量**

RC 用来管理正常运行 Pod 数量，一个 RC 可以由一个或多个 Pod 组成，在 RC 被创建后，系统会根据定义好的副本数来创建 Pod 数量。在运行过程中，如果 Pod 数量小于定义的，就会重启停止的或重新分配 Pod，反之则杀死多余的。

**确保 pod 健康**

当 pod 不健康，运行出错或者无法提供服务时，RC 也会杀死不健康的 pod，重新创建新的。

<a name="100581cc"></a>
## 弹性伸缩

在业务高峰或者低峰期的时候，可以通过 RC 动态的调整 pod 的数量来提高资源的利用率。同时，配置相应的监控功能（Hroizontal Pod Autoscaler），会定时自动从监控平台获取 RC 关联 pod 的整体资源使用情况，做到自动伸缩。

弹性伸缩是指适应负载变化，以弹性可伸缩的方式提供资源。反映到 K8S 中，指的是可根据负载的高低动态调整 Pod 的副本数量。调整 Pod 的副本数是通过修改 RC 中 Pod 的副本是来实现的，示例命令如下：

扩容 Pod 的副本数目到 10

```bash
kubectl scale relicationcontroller lykops --replicas=10
```

缩容 Pod 的副本数目到 1

```bash
kubectl scale rc lykops --replicas=1
```

<a name="26eeea7f"></a>
## 滚动升级

滚动升级是一种平滑过渡的升级方式，通过逐步替换的策略，保证整体系统的稳定，在初始升级的时候就可以及时发现、调整问题，以保证问题影响度不会扩大。

<a name="bc363719"></a>
### 升级方式

**使用配置文件升级**

```bash
kubecl rolling-update lykops-rc-v1 -f lykops-rc.yaml --update-period=10s
```

**直接使用 images**

```bash
kubectl rolling-update lykops-rc --image=webapache:v3
```

<a name="2a9a2f7d"></a>
### 升级过程

升级开始后，首先依据提供的定义文件创建 v2 版本的 RC，然后每隔 10s（--update-period=10s）逐步的增加 v2 版本的 Pod 副本数，逐步减少 v1 版本 Pod 的副本数。升级完成之后，删除 v1 版本的 RC，保留 v2 版本的 RC，及实现滚动升级。

<a name="bbb08598"></a>
### 升级回滚

升级过程中，发生了错误中途退出时，可以选择继续升级。K8S 能够智能的判断升级中断之前的状态，然后紧接着继续执行升级。当然，也可以进行回退，命令如下：

```bash
kubectl rolling-update lykops-v1 -f lykops-v2-rc.yaml --update-period=10s -–rollback
```

<a name="c8e47354"></a>
## yaml 示例

升级之前的 yaml 文件为

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: lykops-rc
  labels:
    app: apache
    version: v1
spec:
  replicas: 5 # 副本数量
  selector: # 筛选要控制的Pod
    app: apache
    version: v1
  template: # Pod的定义
    metadata:
      labels: # Pod的label, spec.selector相同
        app: apache
        version: v1
    spec:
      containers:
        - name: apache-rc
          image: web:apache
          command: ["sh", "/etc/run.sh"]
          ports:
            - containerPort: 80
              name: http
              protocol: TCP
```

升级用的 yaml 文件内容为

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: test-rc-v2 # 名字修改了
  labels: # 与之前的labels一致
    app: apache
    version: v1
spec:
  replicas: 5
  selector: # 与下面的template.metadata.labels一致
    app: apache
    version: v2
  template:
    metadata:
      labels: # 至少修改了一项内容, 此处为version
        app: apache
        version: v2
    spec:
      containers:
        - name: apache-rc-v2
          image: web:apache
          command: ["sh", "/etc/run.sh"]
          ports:
            - containerPort: 80
              name: http
              protocol: TCP
```

**注意事项**

- 要求新的 RC 需要使用旧的 RC 的 Namespace。
- RC 的名字（name）不能与旧的 RC 的名字相同；
- 在 selector 中应至少有一个 Label 与旧的 RC 的 Label 不同，以标识其为新的 RC。
- metadata 与之前相同，否则升级后 service 无法对应上。
