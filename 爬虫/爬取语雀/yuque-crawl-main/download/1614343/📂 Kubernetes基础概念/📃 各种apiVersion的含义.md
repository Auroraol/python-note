查看当前 Kubernetes 版本

```bash
$ kubelet --version
Kubernetes v1.14.2
```

查看当前可用的 API 版本

```bash
kubectl api-versions
```

<a name="alpha"></a>
## alpha

- 该软件可能包含错误。启用一个功能可能会导致 bug
- 随时可能会丢弃对该功能的支持，恕不另行通知

<a name="beta"></a>
## beta

- 软件经过很好的测试。启用功能被认为是安全的。
- 默认情况下功能是开启的
- 细节可能会改变，但功能在后续版本不会被删除

<a name="stable"></a>
## stable

- 该版本名称命名方式：vX 这里 X 是一个整数
- 稳定版本、放心使用
- 将出现在后续发布的软件版本中

<a name="v1"></a>
## v1

Kubernetes API 的稳定版本，包含很多核心对象：pod、service 等

<a name="926eea4e"></a>
## apps/v1beta2

在 kubernetes1.8 版本中，新增加了 apps/v1beta2 的概念，apps/v1beta1 同理<br />DaemonSet，Deployment，ReplicaSet 和 StatefulSet 的当时版本迁入 apps/v1beta2，兼容原有的 extensions/v1beta1

<a name="17fa9b98"></a>
## apps/v1

在 kubernetes1.9 版本中，引入 apps/v1，deployment 等资源从 extensions/v1beta1, apps/v1beta1 和 apps/v1beta2 迁入 apps/v1，原来的 v1beta1 等被废弃。

apps/v1 代表：包含一些通用的应用层的 api 组合，如：Deployments, RollingUpdates, and ReplicaSets

<a name="34dfe83d"></a>
## batch/v1

代表 job 相关的 api 组合

在 kubernetes1.8 版本中，新增了 batch/v1beta1，后 CronJob 已经迁移到了 batch/v1beta1，然后再迁入 batch/v1

<a name="622d91dd"></a>
## autoscaling/v1

代表自动扩缩容的 api 组合，kubernetes1.8 版本中引入。<br />这个组合中后续的 alpha 和 beta 版本将支持基于 memory 使用量、其他监控指标进行扩缩容

<a name="f1462ed2"></a>
## extensions/v1beta1

deployment 等资源在 1.6 版本时放在这个版本中，后迁入到 apps/v1beta2,再到 apps/v1 中统一管理

<a name="d83d602b"></a>
## certificates.k8s.io/v1beta1

安全认证相关的 api 组合

<a name="f37692be"></a>
## authentication.k8s.io/v1

资源鉴权相关的 api 组合

<a name="13d6bd2b"></a>
## 查看当前可用的 API 版本

使用 `kubectl api-versions`

```bash
$ kubectl api-versions
admissionregistration.k8s.io/v1beta1
apiextensions.k8s.io/v1beta1
apiregistration.k8s.io/v1
apiregistration.k8s.io/v1beta1
apps/v1
apps/v1beta1
apps/v1beta2
authentication.k8s.io/v1
authentication.k8s.io/v1beta1
authorization.k8s.io/v1
authorization.k8s.io/v1beta1
autoscaling/v1
autoscaling/v2beta1
autoscaling/v2beta2
batch/v1
batch/v1beta1
certificates.k8s.io/v1beta1
coordination.k8s.io/v1
coordination.k8s.io/v1beta1
events.k8s.io/v1beta1
extensions/v1beta1
greenplum.pivotal.io/v1
metrics.k8s.io/v1beta1
monitoring.coreos.com/v1
networking.k8s.io/v1
networking.k8s.io/v1beta1
node.k8s.io/v1beta1
pingcap.com/v1alpha1
policy/v1beta1
rbac.authorization.k8s.io/v1
rbac.authorization.k8s.io/v1beta1
scheduling.k8s.io/v1
scheduling.k8s.io/v1beta1
storage.k8s.io/v1
storage.k8s.io/v1beta1
v1
```
