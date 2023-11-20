Kubectl 是集群管理命令行工具集, 通过客户端的 kubectl 命令集操作，API Server 响应对应的命令结果，从而达到对 kubernetes 集群的管理。

本文仍然使用 `ksys` 命令作为 `kubectl -n kube-system` 的缩写 (`alias ksys='kubectl -n kube-system'`)

<a name="fa6c7a72"></a>
## 格式化输出

要以特定的格式向终端窗口输出详细信息，可以在 `kubectl` 命令中添加 `-o` 或者 `-output` 标志。

| 输出格式 | 描述 |
| :--- | :--- |
| `-o=custom-columns=<spec>` | 使用逗号分隔的自定义列列表打印表格 |
| `-o=custom-columns-file=<filename>` | 使用 文件中的自定义列模板打印表格 |
| `-o=json` | 输出 JSON 格式的 API 对象 |
| `-o=jsonpath=<template>` | 打印 [jsonpath](https://kubernetes.io/docs/user-guide/jsonpath) 表达式中定义的字段 |
| `-o=jsonpath-file=<filename>` | 打印由 文件中的 [jsonpath](https://kubernetes.io/docs/user-guide/jsonpath) 表达式定义的字段 |
| `-o=name` | 仅打印资源名称 |
| `-o=wide` | 以纯文本格式输出任何附加信息，对于 Pod ，包含节点名称 |
| `-o=yaml` | 输出 YAML 格式的 API 对象 |


<a name="9f40b5d3"></a>
## Kubectl 详细输出和调试

使用 `-v` 或 `--v` 标志跟着一个整数来指定日志级别。[这里](https://github.com/kubernetes/community/blob/master/contributors/devel/logging.md) 描述了通用的 kubernetes 日志约定和相关的日志级别。

| 详细等级 | 描述 |
| :--- | :--- |
| `--v=0` | 总是对操作人员可见。 |
| `--v=1` | 合理的默认日志级别，如果您不需要详细输出。 |
| `--v=2` | 可能与系统的重大变化相关的，有关稳定状态的信息和重要的日志信息。这是对大多数系统推荐的日志级别。 |
| `--v=3` | 有关更改的扩展信息。 |
| `--v=4` | 调试级别详细输出。 |
| `--v=6` | 显示请求的资源。 |
| `--v=7` | 显示 HTTP 请求的 header。 |
| `--v=8` | 显示 HTTP 请求的内容。 |


<a name="e1dc7e3a"></a>
## 查看集群信息

```bash
$ kubectl cluster-info
Kubernetes master is running at https://172.18.13.115:8443
Heapster is running at https://172.18.13.115:8443/api/v1/namespaces/kube-system/services/heapster/proxy
KubeDNS is running at https://172.18.13.115:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
monitoring-grafana is running at https://172.18.13.115:8443/api/v1/namespaces/kube-system/services/monitoring-grafana/proxy
monitoring-influxdb is running at https://172.18.13.115:8443/api/v1/namespaces/kube-system/services/monitoring-influxdb/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

相关命令

```bash
kubectl cluster-info dump # 将当前集群状态输出到 stdout
kubectl cluster-info dump --output-directory=/path/to/cluster-state   # 将当前集群状态输出到 /path/to/cluster-state
```

<a name="h3P65"></a>
## 查看帮助信息

通过在命令后添加 `-h` 查看具体命令的帮助信息：
```bash
$ kubectl apply -h 
Apply a configuration to a resource by filename or stdin. The resource name must be specified. This resource will be
created if it doesn't exist yet. To use 'apply', always create the resource initially with either 'apply' or 'create
--save-config'.

 JSON and YAML formats are accepted.

 Alpha Disclaimer: the --prune functionality is not yet complete. Do not use unless you are aware of what the current
state is. See https://issues.k8s.io/34274.

Examples:
  # Apply the configuration in pod.json to a pod.
  kubectl apply -f ./pod.json

  # Apply resources from a directory containing kustomization.yaml - e.g. dir/kustomization.yaml.
  kubectl apply -k dir/

  # Apply the JSON passed into stdin to a pod.
  cat pod.json | kubectl apply -f -

  # Note: --prune is still in Alpha
  # Apply the configuration in manifest.yaml that matches label app=nginx and delete all the other resources that are
not in the file and match label app=nginx.
  kubectl apply --prune -f manifest.yaml -l app=nginx

  # Apply the configuration in manifest.yaml and delete all the other configmaps that are not in the file.
  kubectl apply --prune -f manifest.yaml --all --prune-whitelist=core/v1/ConfigMap

Available Commands:
  edit-last-applied Edit latest last-applied-configuration annotations of a resource/object
  set-last-applied  Set the last-applied-configuration annotation on a live object to match the contents of a file.
  view-last-applied 显示最后的 resource/object 的 last-applied-configuration annotations

Options:
      --all=false: Select all resources in the namespace of the specified resource types.
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or map key is missing in
the template. Only applies to golang and jsonpath output formats.
      --cascade=true: If true, cascade the deletion of the resources managed by this resource (e.g. Pods created by a
ReplicationController).  Default true.
      --dry-run='none': Must be "none", "server", or "client". If client strategy, only print the object that would be
sent, without sending it. If server strategy, submit server-side request without persisting the resource.
      --field-manager='kubectl': Name of the manager used to track field ownership.
  -f, --filename=[]: that contains the configuration to apply
      --force=false: If true, immediately remove resources from API and bypass graceful deletion. Note that immediate
deletion of some resources may result in inconsistency or data loss and requires confirmation.
      --force-conflicts=false: If true, server-side apply will force the changes against conflicts.
      --grace-period=-1: Period of time in seconds given to the resource to terminate gracefully. Ignored if negative.
Set to 1 for immediate shutdown. Can only be set to 0 when --force is true (force deletion).
  -k, --kustomize='': Process a kustomization directory. This flag can't be used together with -f or -R.
      --openapi-patch=true: If true, use openapi to calculate diff when the openapi presents and the resource can be
found in the openapi spec. Otherwise, fall back to use baked-in types.
  -o, --output='': Output format. One of:
json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-file.
      --overwrite=true: Automatically resolve conflicts between the modified and live configuration by using values from
the modified configuration
      --prune=false: Automatically delete resource objects, including the uninitialized ones, that do not appear in the
configs and are created by either apply or create --save-config. Should be used with either -l or --all.
      --prune-whitelist=[]: Overwrite the default whitelist with <group/version/kind> for --prune
      --record=false: Record current kubectl command in the resource annotation. If set to false, do not record the
command. If set to true, record the command. If not set, default to updating the existing annotation value only if one
already exists.
  -R, --recursive=false: Process the directory used in -f, --filename recursively. Useful when you want to manage
related manifests organized within the same directory.
  -l, --selector='': Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2)
      --server-side=false: If true, apply runs in the server instead of the client.
      --template='': Template string or path to template file to use when -o=go-template, -o=go-template-file. The
template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].
      --timeout=0s: The length of time to wait before giving up on a delete, zero means determine a timeout from the
size of the object
      --validate=true: If true, use a schema to validate the input before sending it
      --wait=false: If true, wait for resources to be gone before returning. This waits for finalizers.

Usage:
  kubectl apply (-f FILENAME | -k DIRECTORY) [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
```

通过 `kubectl explain` 命令可以查看指定资源的详细帮助信息：
```bash
$ kubectl explain Deployment.spec
KIND:     Deployment
VERSION:  apps/v1      

RESOURCE: spec <Object>

DESCRIPTION:
     Specification of the desired behavior of the Deployment.

     DeploymentSpec is the specification of the desired behavior of the
     Deployment.

FIELDS:
   minReadySeconds      <integer>
     Minimum number of seconds for which a newly created pod should be ready
     without any of its container crashing, for it to be considered available.
     Defaults to 0 (pod will be considered available as soon as it is ready)

   paused       <boolean>
     Indicates that the deployment is paused.

   progressDeadlineSeconds      <integer>
     The maximum time in seconds for a deployment to make progress before it is
     considered to be failed. The deployment controller will continue to process
     failed deployments and a condition with a ProgressDeadlineExceeded reason
     will be surfaced in the deployment status. Note that progress will not be
     estimated during the time a deployment is paused. Defaults to 600s.

   replicas     <integer>
     Number of desired pods. This is a pointer to distinguish between explicit
     zero and not specified. Defaults to 1.

   revisionHistoryLimit <integer>
     The number of old ReplicaSets to retain to allow rollback. This is a
     pointer to distinguish between explicit zero and not specified. Defaults to
     10.

   selector     <Object> -required-
     Label selector for pods. Existing ReplicaSets whose pods are selected by
     this will be the ones affected by this deployment. It must match the pod
     template's labels.

   strategy     <Object>
     The deployment strategy to use to replace existing pods with new ones.

   template     <Object> -required-
     Template describes the pods that will be created.
```

<a name="3b9b9be0"></a>
## 显示 kubeconfig 配置

显示合并后的 kubeconfig 配置

```bash
$ kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://172.18.50.200:6443
  name: kubernetes
contexts:
- context:
    cluster: kubernetes
    user: kubernetes-admin
  name: kubernetes-admin@kubernetes
current-context: kubernetes-admin@kubernetes
kind: Config
preferences: {}
users:
- name: kubernetes-admin
  user:
    client-certificate-data: REDACTED
    client-key-data: REDACTED
```

也可以 JSON 格式输出:

```bash
$ kubectl config view -o json
{
    "kind": "Config",
    "apiVersion": "v1",
    "preferences": {},
    "clusters": [
        {
            "name": "kubernetes",
            "cluster": {
                "server": "https://172.18.13.115:8443",
                "certificate-authority-data": "DATA+OMITTED"
            }
        }
    ],
    "users": [
        {
            "name": "kubernetes-admin",
            "user": {
                "client-certificate-data": "REDACTED",
                "client-key-data": "REDACTED"
            }
        }
    ],
    "contexts": [
        {
            "name": "kubernetes-admin@kubernetes",
            "context": {
                "cluster": "kubernetes",
                "user": "kubernetes-admin"
            }
        }
    ],
    "current-context": "kubernetes-admin@kubernetes"
}
```

<a name="e8928169"></a>
## 创建资源

Kubernetes 的清单文件可以使用 json 或 yaml 格式定义。可以以 .yaml、.yml、或者 .json 为扩展名, 通过 `create`/`apply` 命令创建。

- create: 没有创建则创建, 若已创建则报错
- apply: 创建和更新, 已创建也不会报错

```bash
kubectl create ns test # 创建命名空间test
kubectl create -f ./my-manifest.yaml # 创建资源
kubectl create -f ./my1.yaml -f ./my2.yaml # 使用多个文件创建资源
kubectl create -f ./dir # 使用目录下的所有清单文件来创建资源
kubectl create -f https://git.io/vPieo # 使用 url 来创建资源
```

从 stdin 输入中创建多个 YAML 对象

```bash
$ cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000000"
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep-less
spec:
  containers:
  - name: busybox
    image: busybox
    args:
    - sleep
    - "1000"
EOF

# 创建包含几个 key 的 Secret
$ cat <<EOF | kubectl create -f -
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  password: $(echo "s33msi4" | base64)
  username: $(echo "jane" | base64)
EOF
```

使用可视化管理后台创建资源:<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599815450912-54dd4bda-0f2f-4bc6-a4b5-9360874eebd0.png#align=left&display=inline&height=760&originHeight=760&originWidth=1902&size=0&status=done&style=none&width=1902)

<a name="a42312e5"></a>
## 显示和查找资源

- get 获取资源列表
- describe 查看资源详细信息

<a name="node"></a>
### node

查看当前可用的 node

```bash
$ ksys get nodes
NAME         STATUS   ROLES    AGE     VERSION
k8s-master   Ready    master   3h29m   v1.14.0
```

使用下面命令输出节点详细信息

```bash
ksys describe node k8s-node2
```

<a name="service"></a>
### service

查看 service

```bash
$ ksys get svc # 或 `ksys get service`
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                  AGE
kube-dns               ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP,9153/TCP   3h27m
kubernetes-dashboard   NodePort    10.100.16.166   <none>        443:30443/TCP            3h26m

$ ksys get services --sort-by=.metadata.name # List Services Sorted by Name
```

通过 `-o wide` 参数输出更多信息

```bash
$ ksys get services -o wide
NAME                   TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                                     AGE    SELECTOR
heapster               ClusterIP   10.100.63.129    <none>        80/TCP                                      4d4h   k8s-app=heapster
kube-dns               ClusterIP   10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP                      4d5h   k8s-app=kube-dns
kubernetes-dashboard   NodePort    10.106.213.160   <none>        443:30000/TCP                               4d4h   k8s-app=kubernetes-dashboard
metrics-server         ClusterIP   10.111.28.233    <none>        443/TCP                                     4d4h   k8s-app=metrics-server
monitoring-grafana     NodePort    10.101.173.240   <none>        80:30006/TCP                                4d4h   k8s-app=grafana
monitoring-influxdb    ClusterIP   10.102.109.50    <none>        8086/TCP                                    4d4h   k8s-app=influxdb
tiller-deploy          ClusterIP   10.103.22.243    <none>        44134/TCP                                   4d3h   app=helm,name=tiller
traefik-web-ui         NodePort    10.103.163.31    <none>        80:30751/TCP,443:30750/TCP,8080:30011/TCP   4d4h   k8s-app=traefik-ingress-lb
```

<a name="pod"></a>
### pod

查看 pod

```bash
$ ksys get po # 或 `ksys get pods`
NAME                                    READY   STATUS    RESTARTS   AGE
coredns-fb8b8dccf-5cxfw                 1/1     Running   0          3h32m
coredns-fb8b8dccf-dbzbf                 1/1     Running   0          3h32m
etcd-k8s-master                         1/1     Running   5          3h31m
kube-apiserver-k8s-master               1/1     Running   5          3h31m
kube-controller-manager-k8s-master      1/1     Running   4          3h31m
kube-flannel-ds-amd64-bq94z             1/1     Running   0          3h31m
kube-proxy-w4b6r                        1/1     Running   0          3h32m
kube-scheduler-k8s-master               1/1     Running   5          3h31m
kubernetes-dashboard-5f7b999d65-gw8tc   1/1     Running   0          3h31m

$ kubectl get pods --all-namespaces             # 列出所有 namespace 中的所有 pod
$ kubectl get pods --include-uninitialized      # 列出该 namespace 中的所有 pod 包括未初始化的
$ ksys get pods --sort-by='.status.containerStatuses[0].restartCount' # 根据重启次数排序列出 pod
```

通过 `-o wide` 参数输出更多信息

```bash
$ ksys get pods -o wide
NAME                                            READY     STATUS             RESTARTS   AGE       IP             NODE
coredns-78fcdf6894-m9kwr                        1/1       Running            1          20h       10.244.0.5     inspur2.ops.haodf.bj1
coredns-78fcdf6894-tgjn6                        1/1       Running            1          20h       10.244.0.4     inspur2.ops.haodf.bj1
etcd-inspur2.ops.haodf.bj1                      1/1       Running            1          20h       10.1.101.202   inspur2.ops.haodf.bj1
...
```

查看某一个 pod 的配置

```bash
kubectl get pods/podname -n test -o yaml
kubectl get pods/podname -n test -o json
```

查看某一个 pod 的信息

```bash
$ ksys describe pods etcd-k8s-master
Name:               etcd-k8s-master
Namespace:          kube-system
Priority:           2000000000
PriorityClassName:  system-cluster-critical
Node:               k8s-master/192.168.126.129
Start Time:         Sun, 31 Mar 2019 15:07:17 +0800
Labels:             component=etcd
                    tier=control-plane
Annotations:        kubernetes.io/config.hash: 783c7b37e5d9d9e5bf6d4b5fe18a4bc4
                    kubernetes.io/config.mirror: 783c7b37e5d9d9e5bf6d4b5fe18a4bc4
                    kubernetes.io/config.seen: 2019-03-31T15:07:17.623010149+08:00
                    kubernetes.io/config.source: file
Status:             Running
IP:                 192.168.126.129
Containers:
  etcd:
    Container ID:  docker://c25a8845bf0f773feeae78520e609bfa36dd30cdbca2fda6b6ff1101e4d1c582
    Image:         k8s.gcr.io/etcd:3.3.10
    Image ID:      docker://sha256:2c4adeb21b4ff8ed3309d0e42b6b4ae39872399f7b37e0856e673b13c4aba13d
...
```

<a name="deployment"></a>
### deployment

查看 deployment

```bash
$ ksys get deployment
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
coredns                2/2     2            2           4d5h
heapster               1/1     1            1           4d4h
kubernetes-dashboard   1/1     1            1           4d4h
metrics-server         1/1     1            1           4d4h
monitoring-grafana     1/1     1            1           4d4h
monitoring-influxdb    1/1     1            1           4d4h
tiller-deploy          1/1     1            1           4d3h
```

<a name="3efbca73"></a>
## 弹性伸缩资源

```bash
kubectl scale --replicas=3 rs/foo                                 # Scale a replicaset named 'foo' to 3
kubectl scale --replicas=3 -f foo.yaml                            # Scale a resource specified in "foo.yaml" to 3
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql  # If the deployment named mysql's current size is 2, scale mysql to 3
kubectl scale --replicas=5 rc/foo rc/bar rc/baz                   # Scale multiple replication controllers
```

<a name="8a2a35a5"></a>
## 删除资源

```bash
kubectl delete -f ./pod.json # 删除 pod.json 文件中定义的类型和名称的 pod
kubectl delete pod,service baz foo # 删除 名为baz的pod 和 名为foo的service
kubectl delete pods,services -l name=myLabel # 删除具有 name=myLabel 标签的 pod 和 serivce
kubectl delete pods,services -l name=myLabel --include-uninitialized # 删除具有 name=myLabel 标签的 pod 和 service，包括尚未初始化的
kubectl -n my-ns delete po,svc --all # 删除 my-ns namespace 下的所有 pod 和 serivce，包括尚未初始化的
ksys delete pod foo # 删除kube-system命名空间下的名为foo的pod
```

<a name="60fe90d3"></a>
## 更新资源

```bash
kubectl rolling-update frontend-v1 -f frontend-v2.json # 滚动更新 pod frontend-v1
kubectl rolling-update frontend-v1 frontend-v2 --image=image:v2 # 更新资源名称并更新镜像
kubectl rolling-update frontend --image=image:v2 # 更新 frontend pod 中的镜像
kubectl rolling-update frontend-v1 frontend-v2 --rollback # 退出已存在的进行中的滚动更新
cat pod.json | kubectl replace -f - # 基于 stdin 输入的 JSON 替换 pod
kubectl replace --force -f ./pod.json # 强制替换，删除后重新创建资源。会导致服务中断。
kubectl expose rc nginx --port=80 --target-port=8000 # 为 nginx RC 创建服务，启用本地 80 端口连接到容器上的 8000 端口
kubectl get pod mypod -o yaml | sed 's/\(image: myimage\):.*$/\1:v4/' | kubectl replace -f - # 更新单容器 pod 的镜像版本（tag）到 v4
kubectl label pods my-pod new-label=awesome # 添加标签
kubectl annotate pods my-pod icon-url=http://goo.gl/XXBTWq # 添加注解
kubectl autoscale deployment foo --min=2 --max=10 # 自动扩展 deployment “foo”
```

<a name="ebbf504b"></a>
## 修补资源

使用策略合并补丁并修补资源

```bash
kubectl patch node k8s-node-1 -p '{"spec":{"unschedulable":true}}' # 部分更新节点
# 更新容器镜像； spec.containers[*].name 是必须的，因为这是合并的关键字
kubectl patch pod valid-pod -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'
# 使用具有位置数组的 json 补丁更新容器镜像
kubectl patch pod valid-pod --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'
# 使用具有位置数组的 json 补丁禁用 deployment 的 livenessProbe
kubectl patch deployment valid-deployment --type json -p='[{"op": "remove", "path": "/spec/template/spec/containers/0/livenessProbe"}]'
```

<a name="7ae95cbc"></a>
## 编辑资源

在编辑器中编辑任何 API 资源。

```bash
kubectl edit svc/docker-registry                      # 编辑名为 docker-registry 的 service
KUBE_EDITOR="nano" kubectl edit svc/docker-registry   # 使用其它编辑器
```

<a name="eafa11dd"></a>
## 与运行中的 Pod 交互

日志

```bash
kubectl logs my-pod # dump 输出 pod 的日志（stdout）
kubectl logs my-pod -c my-container # dump 输出 pod 中容器的日志（stdout，pod 中有多个容器的情况下使用）
kubectl logs -f my-pod # 流式输出 pod 的日志（stdout）
kubectl logs -f my-pod -c my-container # 流式输出 pod 中容器的日志（stdout，pod 中有多个容器的情况下使用）
```

运行

```bash
kubectl run -i --tty busybox --image=busybox -- sh  # 交互式 shell 的方式运行 pod
kubectl run nginx --image=nginx # 启动一个 nginx 实例
kubectl exec my-pod -- ls / # 在已存在的容器中执行命令（只有一个容器的情况下）
kubectl exec my-pod -c my-container -- ls / # 在已存在的容器中执行命令（pod 中有多个容器的情况下）
kubectl attach my-pod -i # 连接到运行中的容器
```

其他

```bash
kubectl explain pods,svc # 获取 pod 和 svc 的文档
kubectl port-forward my-pod 5000:6000 # 转发 pod 中的 6000 端口到本地的 5000 端口
kubectl top pod POD_NAME --containers # 显示指定 pod 和容器的指标度量
```

<a name="fbdefa4f"></a>
## 与节点和集群交互

```bash
kubectl cordon my-node # 标记 my-node 不可调度
kubectl drain my-node # 清空 my-node 以待维护
kubectl uncordon my-node # 标记 my-node 可调度
kubectl top node my-node # 显示 my-node 的指标度量
kubectl taint nodes foo dedicated=special-user:NoSchedule # 如果该键和影响的污点（taint）已存在，则使用指定的值替换
```
