持久存储卷声明 (PVC, Persistent Volume Claim) 是用户的一种存储请求。它和 Pod 类似，Pod 消耗 Node 资源，而 PVC 消耗 PV 资源。Pod 能够请求特定的资源（如 CPU 和内存）。PVC 能够请求指定的大小和访问的模式（可以被映射为一次读写或者多次只读）。

<a name="d69394d7"></a>
## PVC 配置文件

`nfs-data.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nfs-data
spec:
  accessModes: ["ReadWriteOnce"]
  resources: # 指定请求的资源，存储3G
    requests:
      storage: 3Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - { key: environment, operator: In, values: [dev] }
```

**accessModes** 访问模式

当请求指定访问模式的存储时，PVC 使用的规则和 PV 相同。支持三种访问模式：

- ReadWriteOnce – PV 以 read-write 挂载到一个节点
- ReadOnlyMany – PV 以 read-only 方式挂载到多个节点
- ReadWriteMany – PV 以 read-write 方式挂载到多个节点

**resources** 资源

PVC，就像 pod 一样，可以请求指定数量的资源。请求资源时，PV 和 PVC 都使用相同的资源样式。

**selector** 选择器

PVC 可以指定标签选择器进行更深度的过滤 PV，只有匹配了选择器标签的 PV 才能绑定给 PVC。选择器包含两个字段：

- matchLabels（匹配标签） - PV 必须有一个包含该值得标签
- matchExpressions（匹配表达式） - 一个请求列表，包含指定的键、值的列表、关联键和值的操作符。合法的操作符包含 In，NotIn，Exists，和 DoesNotExist。

所有来自`matchLabels`和`matchExpressions`的请求，都是逻辑与关系的，它们必须全部满足才能匹配上。

**storageClassName** 等级

PVC 可以使用属性 `storageClassName` 来指定 `StorageClass` 的名称，从而请求指定的等级。只有满足请求等级的 PV，即那些包含了和 PVC 相同`storageClassName`的 PV，才能与 PVC 绑定。

PVC 并非必须要请求一个等级。设置 `storageClassName` 为 `''` 的 PVC 总是被理解为请求一个无等级的 PV，因此它只能被绑定到无等级的 PV（未设置对应的标注，或者设置为 `''`）。未设置`storageClassName`的 PVC 不太相同，`DefaultStorageClass` 的权限插件打开与否，集群也会区别处理 PVC。

- 如果权限插件被打开，管理员可能会指定一个默认的`StorageClass`。所有没有指定`StorageClassName`的 PVC 只能被绑定到默认等级的 PV。要指定默认的`StorageClass`，需要在`StorageClass`对象中将标注`storageclass.kubernetes.io/is-default-class`设置为“true”。如果管理员没有指定这个默认值，集群对 PVC 创建请求的回应就和权限插件被关闭时一样。如果指定了多个默认等级，那么权限插件禁止 PVC 创建请求。
- 如果权限插件被关闭，那么就没有默认`StorageClass`的概念。所有没有设置`StorageClassName`的 PVC 都只能绑定到没有等级的 PV。因此，没有设置`StorageClassName`的 PVC 就如同设置`StorageClassName`为 `''` 的 PVC 一样被对待。

根据安装方法的不同，默认的`StorageClass`可能会在安装过程中被插件管理默认的部署在 Kubernetes 集群中。

当 PVC 指定`selector`来请求`StorageClass`时，所有请求都是与操作的。只有满足了指定等级和标签的 PV 才可能绑定给 PVC。当前，一个非空 `selector` 的 PVC 不能使用 PV 动态供给。

<a name="cea66e60"></a>
## 创建 PVC

```bash
kubectl create -f nfs-data.yaml
```

<a name="365e2f20"></a>
## 创建 Pod 以使用 PVC

`pv-pod.yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis
  labels:
    app: redis
spec:
  containers:
    - name: redis
      image: redis
      imagePullPolicy: Never
      volumeMounts:
        - mountPath: "/data"
          name: data
      ports:
        - containerPort: 6379
  volumes:
    - name: data
      persistentVolumeClaim: # 指定使用的PVC
        claimName: nfs-data # 名字一定要正确
```

当前 Pod 可用空间为 3G，如果超过 3G，则需要再创建存储来满足需求，因为是网络数据卷，如果需要扩展空间，直接删除 Pod 再建立一个即可。

<a name="f6989bf2"></a>
## 获取 pvc 信息

pvc 可以指定命名空间, 默认为 default

```bash
$ kubectl get pvc --all-namespaces
NAMESPACE   NAME       STATUS   VOLUME    CAPACITY   ACCESS MODES   STORAGECLASS   AGE
test        nfs-data   Bound    test-pv   15Gi       RWX                           5m20s

$ kubectl get pvc -n test
NAME       STATUS   VOLUME    CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nfs-data   Bound    test-pv   15Gi       RWX                           44m
```

查看 pvc 详情

```bash
$ kubectl describe pvc nfs-data -n test
Name:          nfs-data
Namespace:     test
StorageClass:
Status:        Bound
Volume:        test-pv
Labels:        <none>
Annotations:   pv.kubernetes.io/bind-completed: yes
               pv.kubernetes.io/bound-by-controller: yes
Finalizers:    [kubernetes.io/pvc-protection]
Capacity:      15Gi
Access Modes:  RWX
VolumeMode:    Filesystem
Events:
  Type       Reason         Age                 From                         Message
  ----       ------         ----                ----                         -------
  Normal     FailedBinding  43m (x12 over 46m)  persistentvolume-controller  no persistent volumes available for this claim and no storage class is set
Mounted By:  <none>
```

可以看到, nfs-data 使用了持久卷 `test-pv`
