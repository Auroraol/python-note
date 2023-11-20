<a name="bOkCZ"></a>
## 一、命名空间简介
**命名空间 (NS, Namespace)** 为 Kubernetes 集群提供虚拟的隔离作用，Kubernetes 集群初始有两个命名空间，分别是默认命名空间 default 和系统命名空间 kube-system，除此以外，管理员可以可以创建新的命名空间满足需要。

在一个 Kubernetes 集群中可以使用 namespace 创建多个“虚拟集群”，这些 namespace 之间可以完全隔离，也可以通过某种方式，让一个 namespace 中的 service 可以访问到其他的 namespace 中的服务，这需要通过 RBAC 定义集群级别的角色来实现。

Kubernetes 集群在启动后，如果不特别指明 Namespace，则用户创建的 Pod、RC、Service 都被系统创建到 default 的 Namespace 中。

**哪些情况下适合使用多个 namespace**

因为 namespace 可以提供独立的命名空间，因此可以实现部分的环境隔离。当你的项目和人员众多的时候可以考虑根据项目属性，例如生产、测试、开发划分不同的 namespace。

<a name="39900cdd"></a>
## 二、获取集群中的所有命名空间
使用以下命令可以获取集群下的所有命名空间：
```bash
kubectl get namespaces

# or
kubectl get ns
```

`namespaces`可以简写为`ns`。

集群中默认会有`default`和`kube-system`这两个 namespace。

在执行`kubectl`命令时可以使用`-n`指定操作的 namespace。

用户的普通应用默认是在`default`下，与集群管理相关的为整个集群提供服务的应用一般部署在`kube-system`的 namespace 下，例如我们在安装 kubernetes 集群时部署的`kubedns`、`heapseter`、`EFK`等都是在这个 namespace 下面。

另外，并不是所有的资源对象都会对应 namespace，`node`和`persistentVolume`就不属于任何 namespace。

<a name="737f41e9"></a>
## 三、创建命名空间
比如创建一个名为 test 的命名空间, 首先撰写 yaml 文件, 如下:
```yaml
# test.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test
  labels:
    name: test
```

通过YAML文件创建：
```bash
kubectl create -f ./test.yaml

# or
kubectl apply -f ./test.yaml
```

也可直接使用命令创建：
```bash
kubectl create ns traefik

# or 
kubectl create namespace traefik
```

<a name="fedf4cdb"></a>
## 四、为资源指定命名空间
在创建资源(Pod/RC/Service 等)时使用 `namespace` 字段指定命名空间，若不指定默认使用 default 命名空间。

使用YAML文件创建Pod，并指定命名空间的示例：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-test
  namespace: test
spec:
  containers:
    - name: nginx
      image: nginx
      ports:
        - containerPort: 80
          hostPort: 80
```

<a name="7JU1a"></a>
## 五、查询命名空间中的资源
直接使用 `kubectl get` 时，默认使用的是查询 `namespace=default` 的，加上 `-n` 参数可查询指定命名空间中的资源。

比如查询test命名空间下的所有pods：
```bash
kubectl get pods -n test
```

如果要查询所有命名空间下的资源，则加上 `--all-namespaces` 参数：
```bash
kubectl get pods --all-namespaces
```

<a name="Mp6se"></a>
## 六、删除命名空间
有两种方法删除命名空间，一种是直接使用命令：
```bash
kubectl delete ns test
```

另一种是使用文件删除，比如有如下YAML：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test
```
再使用命令删除：
```bash
kubectl delete -f ./test.yaml
```

<a name="JKRr0"></a>
## 七、错误解决
<a name="SalCs"></a>
### 删除命名空间一直处于Terminating状态

在k8s中`namespace`有两种常见的状态，即Active和Terminating状态，其中后者一般会比较少见，只有当对应的命名空间下还存在运行的资源，但是该命名空间被删除时才会出现所谓的`terminating`状态，这种情况下只要等待k8s本身将命名空间下的资源回收后，该命名空间将会被系统自动删除。但是今天遇到命名空间下已没相关资源，但依然无法删除`terminating`状态的命名空间的情况。

以grafana空间为例：
```bash
$ kubectl delete ns grafana
namespace "grafana" deleted

$ kubectl get ns
NAME                   STATUS        AGE  
grafana                Terminating   4d21h
...

$ kubectl get all -n grafana
No resources found in grafana namespace.
```

先使用命令删除了命名空间grafana，提示删除成功，但是再次查看命名空间列表时，发现grafana仍然存在，并处于Terminating状态。查看其空间内资源，发现已经没有任何资源了。

再次尝试强制删除命名空间，发现仍然提示删除成功：
```bash
$ kubectl delete ns grafana --force --grace-period=0
warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may 
continue to run on the cluster indefinitely.
namespace "grafana" force deleted
```

但是发现其状态仍然处于Terminating：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604474940131-f6c990fd-05c8-42a6-80a5-b9313e8a23bd.png#align=left&display=inline&height=209&originHeight=209&originWidth=1644&size=17244&status=done&style=none&width=1644)

根据网络上的解决方案，尝试使用原生接口删除。<br />首先开启代理：
```bash
kubectl proxy
```
然后将命名空间资源输出：
```bash
kubectl get ns grafana -o json > delete-ns.json
```
然后使用curl进行原生接口请求：
```bash
curl -k -H "Content-Type: application/json" -X PUT --data-binary @delete-ns.json http://127.0.0.1:8001/api/v1/namespaces/grafana/finalize
```
最后终于删除成功了。


参考：

- [k8s删除Terminating状态的命名空间](https://www.jianshu.com/p/76a3a28af07c)
