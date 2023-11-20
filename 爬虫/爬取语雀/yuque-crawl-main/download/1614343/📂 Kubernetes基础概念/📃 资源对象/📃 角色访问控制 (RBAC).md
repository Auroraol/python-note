角色访问控制 (RBAC) 使用 `rbac.authorization.k8s.io` API Group 来实现授权决策，允许管理员通过 Kubernetes API 动态配置策略，要启用 RBAC ，需要在 apiserver 中添加参数 --authorization-mode=RBAC ，如果使用的 kubeadm 安装的集群，1.6 版本以上的都默认开启了 RBAC ，可以通过查看 Master 节点上 apiserver 的静态 Pod 定义文件：

```bash
$ cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep authorization-mode
    - --authorization-mode=Node,RBAC
```

如果是二进制的方式搭建的集群，添加这个参数过后，记得要重启 apiserver 服务。

<a name="a006794f"></a>
## RBAC API 对象

`Kubernetes` 有一个很基本的特性就是它的 [所有资源对象都是模型化的 API 对象](https://www.colabug.com/goto/aHR0cHM6Ly9rdWJlcm5ldGVzLmlvL2RvY3MvY29uY2VwdHMvb3ZlcnZpZXcvd29ya2luZy13aXRoLW9iamVjdHMva3ViZXJuZXRlcy1vYmplY3RzLw==) ，允许执行 CRUD(Create、Read、Update、Delete)操作(也就是我们常说的增、删、改、查操作)，比如下面的这下资源：

- Pods
- ConfigMaps
- Deployments
- Nodes
- Secrets
- Namespaces

上面这些资源对象的可能存在的操作有：

- create
- get
- delete
- list
- update
- edit
- watch
- exec

在更上层，这些资源和 API Group 进行关联，比如 `Pods` 属于 Core API Group，而 `Deployements` 属于 apps API Group，要在 `Kubernetes` 中进行 `RBAC` 的管理，除了上面的这些资源和操作以外，我们还需要另外的一些对象：

- **Rule**：规则，规则是一组属于不同 API Group 资源上的一组操作的集合
- **Subject**：主题，对应在集群中尝试操作的对象
- **Role 和 ClusterRole**：角色和集群角色，这两个对象都包含上面的 Rules 元素，二者的区别在于，在 Role 中，定义的规则只适用于单个命名空间，也就是和 namespace 关联的，而 ClusterRole 是集群范围内的，因此定义的规则不受命名空间的约束。另外 Role 和 ClusterRole 在 `Kubernetes` 中都被定义为集群内部的 API 资源，和我们前面学习过的 Pod、ConfigMap 这些类似，都是我们集群的资源对象，所以同样的可以使用我们前面的 `kubectl` 相关的命令来进行操作
- **RoleBinding 和 ClusterRoleBinding**：角色绑定和集群角色绑定，简单来说就是把声明的 Subject 和我们的 Role 进行绑定的过程(给某个用户绑定上操作的权限)，二者的区别也是作用范围的区别：RoleBinding 只会影响到当前 namespace 下面的资源操作权限，而 ClusterRoleBinding 会影响到所有的 namespace。

<a name="5d78c5de"></a>
## 创建一个只能访问某个 namespace 的用户

我们来创建一个 User Account，只能访问 kube-system 这个命名空间：

- username: qzy
- group: xiaoyulive

<a name="d4db947c"></a>
### 1 创建用户凭证

我们前面已经提到过， `Kubernetes` 没有 User Account 的 API 对象，不过要创建一个用户帐号的话也是挺简单的，利用管理员分配给你的一个私钥就可以创建了，这个我们可以参考 [官方文档中的方法](https://www.colabug.com/goto/aHR0cHM6Ly9rdWJlcm5ldGVzLmlvL2RvY3MvYWRtaW4vYXV0aGVudGljYXRpb24=) ，这里我们来使用 `OpenSSL` 证书来创建一个 User，当然我们也可以使用更简单的 `cfssl` 工具来创建：

给用户 qzy 创建一个私钥，命名成 `qzy.key`

```bash
$ openssl genrsa -out qzy.key 2048
Generating RSA private key, 2048 bit long modulus
..................................................................................+++
..............................+++
e is 65537 (0x10001)
```

使用我们刚刚创建的私钥创建一个证书签名请求文件 `qzy.csr`，要注意需要确保在 `-subj` 参数中指定用户名和组(CN 表示用户名，O 表示组)：

```bash
openssl req -new -key qzy.key -out qzy.csr -subj "/CN=qzy/O=xiaoyulive"
```

然后找到我们的 `Kubernetes` 集群的 `CA`，我使用的是 `kubeadm` 安装的集群， `CA` 相关证书位于 `/etc/kubernetes/pki/` 目录下面，如果你是二进制方式搭建的，你应该在最开始搭建集群的时候就已经指定好了 `CA` 的目录，我们会利用该目录下面的 `ca.crt` 和 `ca.key` 两个文件来批准上面的证书请求

生成最终的证书文件，我们这里设置证书的有效期为 500 天：

```bash
$ openssl x509 -req -in qzy.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out qzy.crt -days 500
Signature ok
subject=/CN=qzy/O=xiaoyulive
Getting CA Private Key
```

现在查看我们当前文件夹下面是否生成了一个证书文件

```bash
$ ls
qzy.crt  qzy.csr  qzy.key
```

现在我们可以使用刚刚创建的证书文件和私钥文件在集群中创建新的凭证和上下文(Context)

```bash
$ kubectl config set-credentials qzy --client-certificate=qzy.crt  --client-key=qzy.key
User "qzy" set.
```

我们可以看到一个用户 `qzy` 创建了，然后为这个用户设置新的 Context:

```bash
$ kubectl config set-context qzy-context --cluster=kubernetes --namespace=test --user=qzy
Context "qzy-context" created.
```

到这里，我们的用户 `qzy` 就已经创建成功了，现在我们使用当前的这个配置文件来操作 `kubectl` 命令的时候，应该会出现错误，因为我们还没有为该用户定义任何操作的权限呢：

```bash
$ kubectl get pods --context=qzy-context
Error from server (Forbidden): pods is forbidden: User "haimaxy" cannot list pods in the namespace "default"
```

<a name="8721f66b"></a>
### 2 创建角色

用户创建完成后，接下来就需要给该用户添加操作权限，我们来定义一个 `YAML` 文件，创建一个允许用户操作 Deployment、Pod、ReplicaSets 的角色，如下定义

`qzy-role.yaml`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: qzy-role # 角色名
  namespace: test # 命名空间
rules:
  - apiGroups: ["", "extensions", "apps"] # API Group
    resources: ["deployments", "replicasets", "pods"] # 允许访问的资源, 若允许访问全部资源可使用 ["*"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"] # 允许的访问方式, 也可以使用["*"]
```

其中 `Pod` 属于 core 这个 API Group，在 `YAML` 中用空字符就可以，而 `Deployment` 属于 apps 这个 API Group， `ReplicaSets` 属于 `extensions` 这个 API Group，所以 rules 下面的 apiGroups 就综合了这几个资源的 API Group: `["", "extensions", "apps"]`，其中 `verbs` 就是我们上面提到的可以对这些资源对象执行的操作，我们这里需要所有的操作方法，所以我们也可以使用 `["*"]` 来代替。

然后创建这个 `Role`

```bash
$ kubectl create -f qzy-role.yaml
role.rbac.authorization.k8s.io/qzy-role created
```

注意这里我们没有使用上面的 `qzy-context` 这个上下文了，因为木有权限啦

<a name="a5b7bc58"></a>
### 3 创建角色权限绑定

Role 创建完成了，但是很明显现在我们这个 Role 和我们的用户 qzy 还没有任何关系, 这里我就需要创建一个 `RoleBinding` 对象，在 test 这个命名空间下面将上面的 qzy-role 角色和用户 qzy 进行绑定

`qzy-rolebinding.yaml`

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: qzy-rolebinding
  namespace: test # 要绑定的命名空间
subjects: # 要绑定的用户
  - kind: User
    name: qzy
    apiGroup: ""
roleRef: # 要绑定的角色
  kind: Role
  name: qzy-role
  apiGroup: ""
```

上面的 `YAML` 文件中我们看到了 `subjects` 关键字，这里就是我们上面提到的用来尝试操作集群的对象，这里对应上面的 User 帐号 qzy，使用 `kubectl` 创建上面的资源对象：

```bash
$ kubectl create -f qzy-rolebinding.yaml
rolebinding.rbac.authorization.k8s.io/qzy-rolebinding created
```

<a name="89203c5a"></a>
### 4 测试

现在我们应该可以上面的 `qzy-context` 上下文来操作集群了：

```bash
$ kubectl get pods --context=qzy-context # 允许访问 pods
NAME                     READY   STATUS    RESTARTS   AGE
nginx-test-229g8         1/1     Running   2          4d21h
nginx-test-hdxfs         1/1     Running   0          4d21h
nginx-test-ls69t         1/1     Running   1          4d22h
test1-567899468c-5lfgd   1/1     Running   0          4d14h

$ kubectl get svc --context=qzy-context # 禁止访问 service
Error from server (Forbidden): services is forbidden: User "qzy" cannot list resource "services" in API group "" in the namespace "test"
```

我们可以看到我们使用 `kubectl` 的使用并没有指定 namespace 了，这是因为我们已经为该用户分配了权限了，如果我们在后面加上一个 `-n default` 试看看呢？

```bash
$ kubectl --context=qzy-context get pods --namespace=default
Error from server (Forbidden): pods is forbidden: User "haimaxy" cannot list pods in the namespace "default"
```

权限不足, 因为该用户并没有 default 这个命名空间的操作权限

<a name="3dc4b584"></a>
## 创建一个只能访问某个 namespace 的 ServiceAccount

上面我们创建了一个只能访问某个命名空间下面的普通用户，我们前面也提到过 subjects 下面还有一个类型的主题资源：ServiceAccount，现在我们来创建一个集群内部的用户只能操作 test 这个命名空间下面的 pods 和 deployments，首先来创建一个 ServiceAccount 对象：

```bash
kubectl create sa qzy-sa -n test
```

当然我们也可以定义成 `YAML` 文件的形式来创建。

然后新建一个 Role 对象：(qzy-sa-role.yaml)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: qzy-sa-role
  namespace: test
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "watch", "list"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

可以看到我们这里定义的角色没有创建、删除、更新 Pod 的权限，待会我们可以重点测试一下，创建该 Role 对象：

```bash
kubectl create -f qzy-sa-role.yaml
```

然后创建一个 RoleBinding 对象，将上面的 qzy-sa 和角色 qzy-sa-role 进行绑定：(qzy-sa-rolebinding.yaml)

```yaml
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: qzy-sa-rolebinding
  namespace: test # 要绑定的命名空间
subjects: # 要绑定的 ServiceAccount
  - kind: ServiceAccount
    name: qzy-sa
    namespace: test
roleRef: # 要绑定的角色
  kind: Role
  name: qzy-sa-role
  apiGroup: rbac.authorization.k8s.io
```

添加这个资源对象：

```bash
kubectl create -f qzy-sa-rolebinding.yaml
```

然后我们怎么去验证这个 ServiceAccount 呢？我们前面的课程中是不是提到过一个 ServiceAccount 会生成一个 Secret 对象和它进行映射，这个 Secret 里面包含一个 token，我们可以利用这个 token 去登录 Dashboard，然后我们就可以在 Dashboard 中来验证我们的功能是否符合预期了：

```bash
$ kubectl get secret -n test | grep qzy-sa
qzy-sa-token-nxgqx                  kubernetes.io/service-account-token   3         47m

$ kubectl get secret qzy-sa-token-nxgqx -o jsonpath={.data.token} -n test | base64 -d
# 会生成一串很长的base64后的字符串
```

使用这里的 token 去 Dashboard 页面进行登录：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597326243799-e109d295-883f-488e-b2ab-06967e165ca8.png#align=left&display=inline&height=671&originHeight=671&originWidth=783&size=0&status=done&style=none&width=783)


我们可以看到上面的提示信息，这是因为我们登录进来后默认跳转到 default 命名空间，我们切换到 kube-system 命名空间下面就可以了：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597326334439-1ed2bbf8-5589-4de8-a92f-7ee6a8af03e7.png#align=left&display=inline&height=778&originHeight=778&originWidth=1050&size=0&status=done&style=none&width=1050)

我们可以看到可以访问 pod 列表了，但是也会有一些其他额外的提示：events is forbidden: User “system:serviceaccount:test:qzy-sa” cannot list events in the namespace "test"，这是因为当前登录用只被授权了访问 pod 和 deployment 的权限，同样的，访问下 deployment 看看可以了吗？

同样的，你可以根据自己的需求来对访问用户的权限进行限制，可以自己通过 Role 定义更加细粒度的权限，也可以使用系统内置的一些权限……

<a name="417de78d"></a>
## 创建一个可以访问所有 namespace 的 ServiceAccount

刚刚我们创建的 `qzy-sa` 这个 ServiceAccount 和一个 Role 角色进行绑定的，如果我们现在创建一个新的 ServiceAccount，需要他操作的权限作用于所有的 namespace，这个时候我们就需要使用到 ClusterRole 和 ClusterRoleBinding 这两种资源对象了。同样，首先新建一个 ServiceAcount 对象：

`qzy-sa2.yaml`

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: qzy-sa2
  namespace: test
```

创建 ServiceAccount：

```bash
kubectl create -f qzy-sa2.yaml
```

然后创建一个 ClusterRoleBinding 对象:

`qzy-clusterolebinding.yaml`

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: qzy-sa2-clusterrolebinding
subjects:
  - kind: ServiceAccount
    name: qzy-sa2
    namespace: test
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

从上面我们可以看到我们没有为这个资源对象声明 namespace，因为这是一个 ClusterRoleBinding 资源对象，是作用于整个集群的，我们也没有单独新建一个 ClusterRole 对象，而是使用的 cluster-admin 这个对象，这是 `Kubernetes` 集群内置的 ClusterRole 对象，我们可以使用 `kubectl get clusterrole` 和 `kubectl get clusterrolebinding` 查看系统内置的一些集群角色和集群角色绑定，这里我们使用的 cluster-admin 这个集群角色是拥有最高权限的集群角色，所以一般需要谨慎使用该集群角色。

创建上面集群角色绑定资源对象，创建完成后同样使用 ServiceAccount 对应的 token 去登录 Dashboard 验证下：

```bash
$ kubectl create -f qzy-clusterolebinding.yaml
$ kubectl get secret -n test | grep qzy-sa2
qzy-sa2-token-nxgqx                  kubernetes.io/service-account-token   3         47m
$ kubectl get secret qzy-sa2-token-nxgqx -o jsonpath={.data.token} -n test | base64 -d
# 会生成一串很长的base64后的字符串
```

我们在最开始接触到 `RBAC` 认证的时候，可能不太熟悉，特别是不知道应该怎么去编写 `rules` 规则，大家可以去分析系统自带的 clusterrole、clusterrolebinding 这些资源对象的编写方法，怎么分析？还是利用 kubectl 的 get、describe、 -o yaml 这些操作，所以 `kubectl` 最基本的用户一定要掌握好。

<a name="8009300c"></a>
## Service Account

Service Account (SA) 为 Pod 中的进程提供身份信息。

当您（真人用户）访问集群（例如使用`kubectl`命令）时，apiserver 会将您认证为一个特定的 User Account（目前通常是`admin`，除非您的系统管理员自定义了集群配置）。Pod 容器中的进程也可以与 apiserver 联系。当它们在联系 apiserver 的时候，它们会被认证为一个特定的 Service Account（例如`default`）。

<a name="e768b1f0"></a>
### 使用默认的 ServiceAccount 访问 API server

当您创建 pod 的时候，如果您没有指定一个 service account，系统会自动地在与该 pod 相同的 namespace 下为其指派一个`default` service account。如果您获取刚创建的 pod 的原始 json 或 yaml 信息（例如使用`kubectl get pods/podename -o yaml`命令），您将看到`spec.serviceAccountName`字段已经被设置为 `default`。

您可以在 pod 中使用自动挂载的 service account 凭证来访问 API，如 [Accessing the Cluster](https://kubernetes.io/docs/user-guide/accessing-the-cluster/#accessing-the-api-from-a-pod) 中所描述。

Service account 是否能够取得访问 API 的许可取决于您使用的 [授权插件和策略](https://kubernetes.io/docs/admin/authorization/#a-quick-note-on-service-accounts)。

在 1.6 以上版本中，您可以选择取消为 service account 自动挂载 API 凭证，只需在 service account 中设置 `automountServiceAccountToken: false`：

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
automountServiceAccountToken: false
```

在 1.6 以上版本中，您也可以选择只取消单个 pod 的 API 凭证自动挂载：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: build-robot
  automountServiceAccountToken: false
  ...
```

如果在 pod 和 service account 中同时设置了 `automountServiceAccountToken`, pod 设置中的优先级更高。

<a name="88d916da"></a>
### ServiceAccount 的常用操作

<a name="b9f5383f"></a>
#### 创建 ServiceAccount

通过命令方式创建 ServiceAccount:

```bash
kubectl create sa build-robot -n test
```

也可以像这样创建一个 ServiceAccount 对象：

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
  namespace: test
```

<a name="3955f60c"></a>
#### 获取 ServiceAccount 信息

如果您看到如下的 ServiceAccount 对象的完整输出信息：

```bash
$ kubectl get sa/build-robot -o yaml
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  annotations:
    kubernetes.io/service-account.name: build-robot
type: kubernetes.io/service-account-token
```

查看 ServiceAccount 的详细信息, 包括 token:

```bash
$ kubectl describe secrets/build-robot-secret
Name:   build-robot-secret
Namespace:  default
Labels:   <none>
Annotations:  kubernetes.io/service-account.name=build-robot,kubernetes.io/service-account.uid=870ef2a5-35cf-11e5-8d06-005056b45392

Type: kubernetes.io/service-account-token

Data
====
ca.crt: 1220 bytes
token: ...
namespace: 7 bytes
```

<a name="df2a07f3"></a>
#### 删除 ServiceAccount

```bash
kubectl delete sa/build-robot -n test
```
