<a name="JBBLB"></a>
## 一、Kubernetes Dashboard 简介

Kubernetes Dashboard是k8s的管理工具，先引用官方的文档说明：
> Dashboard is a web-based Kubernetes user interface. You can use Dashboard to deploy containerized applications to a Kubernetes cluster, troubleshoot your containerized application, and manage the cluster resources. You can use Dashboard to get an overview of applications running on your cluster, as well as for creating or modifying individual Kubernetes resources (such as Deployments, Jobs, DaemonSets, etc). For example, you can scale a Deployment, initiate a rolling update, restart a pod or deploy new applications using a deploy wizard.


大意就是：
> Dashboard 是基于 Web 的 Kubernetes 用户界面。您可以使用 Dashboard 将容器化应用程序部署到 Kubernetes 群集、对容器化应用程序进行故障排除以及管理群集资源。您可以使用 Dashboard 获取群集上运行的应用程序的概述，以及创建或修改单个 Kubernetes 资源（如部署、作业、守护进程集等）。例如，您可以缩放部署、启动滚动更新、重新启动窗格或使用部署向导部署新应用程序。
> 
> 仪表板还提供有关群集中 Kubernetes 资源的状态以及可能发生的任何错误的信息。


简单地说，Kubernetes Dashboard 就是管理 k8s 集群的 WebUI，集合了所有命令行可以操作的所有命令。

<a name="Bebg5"></a>
## 二、部署Kubernetes Dashboard
<a name="bDvSb"></a>
### 通过Helm部署
添加仓库并更新：
```json
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm repo update
```
先创建一个namespace，以免默认添加到default：
```json
kubectl create ns kubernetes-dashboard
```
部署[Kubernetes Dashboard](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard)：
```json
helm install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard -n kubernetes-dashboard
```

刚部署完，会在控制台中打印：
```bash
NAME: kubernetes-dashboard
LAST DEPLOYED: Sun Nov  1 23:25:10 2020
NAMESPACE: kubernetes-dashboard
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
*********************************************************************************
*** PLEASE BE PATIENT: kubernetes-dashboard may take a few minutes to install ***
*********************************************************************************

Get the Kubernetes Dashboard URL by running:
  export POD_NAME=$(kubectl get pods -n kubernetes-dashboard -l "app.kubernetes.io/name=kubernetes-dashboard,app.kubernetes.io/instance=kubernetes-dashboard" -o jsonpath="{.items[0].metadata.name}")
  echo https://127.0.0.1:8443/
  kubectl -n kubernetes-dashboard port-forward $POD_NAME 8443:8443
```

<a name="qRPBI"></a>
### 通过YAML部署
部署方式如下:

```bash
# https方式访问(推荐)
kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended/kubernetes-dashboard.yaml

# http方式访问
kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/alternative/kubernetes-dashboard.yaml   
```

:::success
小技巧

由于将Kubernetes Dashboard部署到了kube-system命名空间下，后面的操作都是在 kube-system 命名空间中进行，可以设置个别名 `ksys=kubectl -n kube-system` 这样就可以使用 ksys 操作该名称空间了。

命令：`alias ksys='kubectl -n kube-system'` ，注意此命令重启后无效。

可以修改 `~/.bashrc`, 加入 `alias ksys='kubectl -n kube-system'`, 然后 `source ~/.bashrc` 使其生效, 这样重启后仍然有效
:::

安装完后查看 pod 信息：

```bash
$ ksys get po
NAME                                      READY   STATUS    RESTARTS   AGE
kubernetes-dashboard-57df4db6b-5j2gv      1/1     Running   0          4h8m
```

可以看到多了一个 kubernetes-dashboard-57df4db6b-bn5vn，并且已经正常启动。
<a name="1ed63a74"></a>
## 三、使用Proxy访问
先看看官方的 `kubernetes-dashboard.yaml`配置如下：
```yaml
# ------------------- Dashboard Secrets ------------------- #

apiVersion: v1
kind: Secret
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard-certs
  namespace: kube-system
type: Opaque

---
apiVersion: v1
kind: Secret
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard-csrf
  namespace: kube-system
type: Opaque
data:
  csrf: ""

---
# ------------------- Dashboard Service Account ------------------- #

apiVersion: v1
kind: ServiceAccount
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kube-system

---
# ------------------- Dashboard Role & Role Binding ------------------- #

kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: kubernetes-dashboard-minimal
  namespace: kube-system
rules:
  # Allow Dashboard to create 'kubernetes-dashboard-key-holder' secret.
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["create"]
    # Allow Dashboard to create 'kubernetes-dashboard-settings' config map.
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["create"]
    # Allow Dashboard to get, update and delete Dashboard exclusive secrets.
  - apiGroups: [""]
    resources: ["secrets"]
    resourceNames:
      [
        "kubernetes-dashboard-key-holder",
        "kubernetes-dashboard-certs",
        "kubernetes-dashboard-csrf",
      ]
    verbs: ["get", "update", "delete"]
    # Allow Dashboard to get and update 'kubernetes-dashboard-settings' config map.
  - apiGroups: [""]
    resources: ["configmaps"]
    resourceNames: ["kubernetes-dashboard-settings"]
    verbs: ["get", "update"]
    # Allow Dashboard to get metrics from heapster.
  - apiGroups: [""]
    resources: ["services"]
    resourceNames: ["heapster"]
    verbs: ["proxy"]
  - apiGroups: [""]
    resources: ["services/proxy"]
    resourceNames: ["heapster", "http:heapster:", "https:heapster:"]
    verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: kubernetes-dashboard-minimal
  namespace: kube-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: kubernetes-dashboard-minimal
subjects:
  - kind: ServiceAccount
    name: kubernetes-dashboard
    namespace: kube-system

---
# ------------------- Dashboard Deployment ------------------- #

kind: Deployment
apiVersion: apps/v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kube-system
spec:
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      k8s-app: kubernetes-dashboard
  template:
    metadata:
      labels:
        k8s-app: kubernetes-dashboard
    spec:
      containers:
        - name: kubernetes-dashboard
          image: k8s.gcr.io/kubernetes-dashboard-amd64:v2.0.0-alpha0 # kubernetes-dashboard-amd64 的版本
          ports:
            - containerPort: 8443
              protocol: TCP
          args:
            - --auto-generate-certificates
          volumeMounts:
            - name: kubernetes-dashboard-certs
              mountPath: /certs
            - mountPath: /tmp
              name: tmp-volume
          livenessProbe:
            httpGet:
              scheme: HTTPS
              path: /
              port: 8443
            initialDelaySeconds: 30
            timeoutSeconds: 30
      volumes:
        - name: kubernetes-dashboard-certs
          secret:
            secretName: kubernetes-dashboard-certs
        - name: tmp-volume
          emptyDir: {}
      serviceAccountName: kubernetes-dashboard
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule

---
# ------------------- Dashboard Service ------------------- #

kind: Service
apiVersion: v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kube-system
spec:
  ports:
    - port: 443
      targetPort: 8443
  selector:
    k8s-app: kubernetes-dashboard
```

可以看出，并未暴露外部访问的端口。此时需要使用proxy访问。

启动proxy：
```bash
$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```

然后在本机浏览器中输入：[http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601435032504-c11c9c68-8ba2-48ae-afbc-1882a0365a4b.png#align=left&display=inline&height=565&originHeight=565&originWidth=1257&size=60832&status=done&style=none&width=1257)<br />即可成功访问。

<a name="472c8f95"></a>
## 四、使用NodePort访问
出于安全性考虑，dashboard 是不提供外部访问的，所以我们这边需要添加一个 service，并且指定为 NodePort 类型，以供外部访问。

通过以下命令可以暴露其端口：
```bash
kubectl patch svc kubernetes-dashboard -n kubernetes-dashboard -p '{"spec":{"type":"NodePort","ports":[{"port":443,"targetPort":8443,"nodePort":30443}]}}'
```

也可以修改 service 配置，以暴露服务端口，具体修改如下：

`kubernetes-dashboard.yaml`
```yaml
# ------------------- Dashboard Service ------------------- #
kind: Service
apiVersion: v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kube-system
spec:
  ports:
    - port: 443
      targetPort: 8443
      nodePort: 30443
    - port: 80
      targetPort: 9090
      nodePort: 30080
  type: NodePort
  selector:
    k8s-app: kubernetes-dashboard
```

重新加载配置:
```bash
kubectl apply -f kubernetes-dashboard.yaml
```

dashboard 应用的默认端口是 8443，这边我们指定一个 30443 端口进行映射，提供外部访问入口。这时候我们就可以通过 `http://host-ip:30443` 来访问 dashboard 了。

注意, 直接使用官方的 yaml，证书将不可用，在 Firefox 中可以看到证书的时效不对：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599808528669-1d326864-c375-4b0f-8471-f7fe75e60b4d.png#align=left&display=inline&height=456&originHeight=639&originWidth=725&size=0&status=done&style=none&width=517)<br />目前也只能在 Firefox 中可以忽略此错误, 其他浏览器直接打不开, 我们在火狐中选择继续：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599808595664-a68ed223-3f5b-447d-bb91-788521af8aa2.png#align=left&display=inline&height=837&originHeight=837&originWidth=1078&size=0&status=done&style=none&width=1078)

<a name="dQC0u"></a>
## 五、登录Kubernetes Dashboard<br />
用官方的 yaml 创建出来的 servcie account 登录的话，是啥权限都没有的，全部是 forbidden，因为官方的给了一个 minimal 的 role。为了方便，直接创建一个超级管理员的账号，配置如下：
```yaml
cat > dashboard-adminuser.yaml << EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard  
EOF
```

创建登录用户：
```
kubectl apply -f dashboard-adminuser.yaml
```

创建完了之后，系统会自动创建该用户的 secret，通过如下命令获取 secret：
```bash
$ kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
Name:         admin-user-token-btrhm
Namespace:    kubernetes-dashboard
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: admin-user
              kubernetes.io/service-account.uid: e4a370ec-8373-4332-8f24-7841205e0959

Type:  kubernetes.io/service-account-token

Data
====
ca.crt:     1066 bytes
namespace:  20 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6ImRvTDIzZlJYWXp1dW83ZGRUdW5Sc0MzbDBiTDMxeXYyc084aDU1RFU5Qm8ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWJ0cmhtIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJlNGEzNzBlYy04MzczLTQzMzItOGYyNC03ODQxMjA1ZTA5NTkiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.QNeAnSlGkTvTwpYdiZ4Zjq7c_WCUU79_cx6e0C1WiTdr7CdX1-xx9lY4-kOB5KQ-C4uolPcMTcW68rtDVw6J9qU5Ss112N8FGllH2n1gAISQsBfK40zKzMwNep9t2mMtuC67xl-cdFdjzkkPCjx0iuP4RJSg3tIj-aRYUUeemGrkrn6t8gU0tHcIPVCpaadntwMV9aPiJGYVIV8mODLFUORahFO8LwKWs3COcgR-kL-cxVUqcBlLAjLfLxT47YJbVEjcllaMUHJwG59aRb9OUYZGxOeZTPNNfigU63y_HvttVb3mBGqETmEPVj8zNA4_mBGngEVr-QdV_xv-PSz7vQ
```

如果只想打印出token，使用以下命令：
```bash
$ kubectl get secrets -n kubernetes-dashboard
NAME                                         TYPE                                  DATA   AGE
admin-user-token-btrhm                       kubernetes.io/service-account-token   3      16m
default-token-z4g86                          kubernetes.io/service-account-token   3      37m
kubernetes-dashboard-certs                   Opaque                                0      37m
kubernetes-dashboard-csrf                    Opaque                                1      37m
kubernetes-dashboard-key-holder              Opaque                                2      37m
kubernetes-dashboard-token-wdf8j             kubernetes.io/service-account-token   3      37m
sh.helm.release.v1.kubernetes-dashboard.v1   helm.sh/release.v1                    1      37m

$ kubectl describe secrets -n kubernetes-dashboard admin-user-token-btrhm  | grep token | awk 'NR==3{print $2}'
eyJhbGciOiJSUzI1NiIsImtpZCI6ImRvTDIzZlJYWXp1dW83ZGRUdW5Sc0MzbDBiTDMxeXYyc084aDU1RFU5Qm8ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWJ0cmhtIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJlNGEzNzBlYy04MzczLTQzMzItOGYyNC03ODQxMjA1ZTA5NTkiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.QNeAnSlGkTvTwpYdiZ4Zjq7c_WCUU79_cx6e0C1WiTdr7CdX1-xx9lY4-kOB5KQ-C4uolPcMTcW68rtDVw6J9qU5Ss112N8FGllH2n1gAISQsBfK40zKzMwNep9t2mMtuC67xl-cdFdjzkkPCjx0iuP4RJSg3tIj-aRYUUeemGrkrn6t8gU0tHcIPVCpaadntwMV9aPiJGYVIV8mODLFUORahFO8LwKWs3COcgR-kL-cxVUqcBlLAjLfLxT47YJbVEjcllaMUHJwG59aRb9OUYZGxOeZTPNNfigU63y_HvttVb3mBGqETmEPVj8zNA4_mBGngEVr-QdV_xv-PSz7vQ
```

将该 token 填入登陆界面中的 token 位置，即可登陆，并具有全部权限。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599808650531-f403e17d-157d-40a4-b4d9-5be400ceb27a.png#align=left&display=inline&height=837&originHeight=837&originWidth=1078&size=0&status=done&style=none&width=1078)

登录成功：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599808716512-b0dda02a-7f2a-4bb9-8927-979c065d883a.png#align=left&display=inline&height=1048&originHeight=1048&originWidth=1920&size=0&status=done&style=none&width=1920)<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599808723863-14973dea-c0ac-4f1b-b82d-fbbb823baff3.png#align=left&display=inline&height=1048&originHeight=1048&originWidth=1920&size=0&status=done&style=none&width=1920)

<a name="30c8d05d"></a>
## 六、Dashboard 提供的功能

在默认情况下，Dashboard 显示默认(default)命名空间下的对象，也可以通过命名空间选择器选择其他的命名空间。在 Dashboard 用户界面中能够显示集群大部分的对象类型。

<a name="74ea72bb"></a>
### 集群管理

集群管理视图用于对节点、命名空间、持久化存储卷、角色和存储类进行管理。 节点视图显示 CPU 和内存的使用情况，以及此节点的创建时间和运行状态。 命名空间视图会显示集群中存在哪些命名空间，以及这些命名空间的运行状态。角色视图以列表形式展示集群中存在哪些角色，这些角色的类型和所在的命名空间。 持久化存储卷以列表的方式进行展示，可以看到每一个持久化存储卷的存储总量、访问模式、使用状态等信息；管理员也能够删除和编辑持久化存储卷的 YAML 文件。

<a name="c3bc562e"></a>
### 工作负载

工作负载视图显示部署、副本集、有状态副本集等所有的工作负载类型。在此视图中，各种工作负载会按照各自的类型进行组织。 工作负载的详细信息视图能够显示应用的详细信息和状态信息，以及对象之间的关系。

<a name="9557a5c8"></a>
### 服务发现和负载均衡

服务发现视图能够将集群内容的服务暴露给集群外的应用，集群内外的应用可以通过暴露的服务调用应用，外部的应用使用外部的端点，内部的应用使用内部端点。

<a name="a39cf1ca"></a>
### 存储

存储视图显示被应用用来存储数据的持久化存储卷申明资源。

<a name="224e2ccd"></a>
### 配置

配置视图显示集群中应用运行时所使用配置信息，Kubernetes 提供了配置字典（ConfigMaps）和秘密字典（Secrets），通过配置视图，能够编辑和管理配置对象，以及查看隐藏的敏感信息。

<a name="b375cafc"></a>
### 日志视图

Pod 列表和详细信息页面提供了查看日志视图的链接，通过日志视图不但能够查看 Pod 的日志信息，也能够查看 Pod 容器的日志信息。通过 Dashboard 能够根据向导创建和部署一个容器化的应用，当然也可以通过手工的方式输入指定应用信息，或者通过上传 YAML 和 JSON 文件来创建和不受应用。

<a name="gTQkx"></a>
## 七、部署时常见问题解决
<a name="lNB13"></a>
### ImagePullBackOff

如果 kubernetes-dashboard-57df4db6b-5j2gv 状态为 `ImagePullBackOff`, 查看错误具体原因:

```bash
kubectl describe pod kubernetes-dashboard-57df4db6b-5j2gv --namespace=kube-system
```

不出意外肯定是拉取镜像时出错，考虑到国内网络的问题，使用换源拉取的方式解决。

方式一：拉取后更名

```bash
# 1.x
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:v1.10.1
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:v1.10.1 k8s.gcr.io/kubernetes-dashboard-amd64:v1.10.1
docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:v1.10.1

# 2.x
docker pull kubernetesdashboarddev/kubernetes-dashboard-amd64:v2.0.0-alpha0
docker tag kubernetesdashboarddev/kubernetes-dashboard-amd64:v2.0.0-alpha0 k8s.gcr.io/kubernetes-dashboard-amd64:v2.0.0-alpha0
docker rmi kubernetesdashboarddev/kubernetes-dashboard-amd64:v2.0.0-alpha0
```

方式二：修改 `kubernetes-dashboard.yaml`

```bash
# 修改源前
$ grep image kubernetes-dashboard.yaml
  image: k8s.gcr.io/kubernetes-dashboard-amd64:v1.10.1

# 修改源后
$ grep image kubernetes-dashboard.yaml
  image: registry.cn-hangzhou.aliyuncs.com/google_containers/kubernetes-dashboard-amd64:v1.10.1
```

<a name="s12ci"></a>
### node(s) had taint
如果在部署的时候，发现pod一直厨艺Pending状态，很有可能是节点有污点标记：
```bash
$ kubectl get po -n kubernetes-dashboard
NAME                                    READY   STATUS    RESTARTS   AGE
kubernetes-dashboard-675cdd5b7f-bw4m5   0/1     Pending   0          3m35s

$ kubectl describe po kubernetes-dashboard-675cdd5b7f-bw4m5 -n kubernetes-dashboard
Name:           kubernetes-dashboard-675cdd5b7f-bw4m5
Namespace:      kubernetes-dashboard
...
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  4m4s  default-scheduler  0/1 nodes are available: 1 node(s) had taint {node-role.kubernetes.io/master: }, that the pod didn't tolerate.
  Warning  FailedScheduling  4m4s  default-scheduler  0/1 nodes are available: 1 node(s) had taint {node-role.kubernetes.io/master: }, that the pod didn't tolerate.
```
将此标记删除即可：
```bash
$ kubectl taint nodes --all node-role.kubernetes.io/master-
node/localhost.localdomain untainted
```

<a name="FV79d"></a>
## 八、相关配置
<a name="SDN0c"></a>
### 设置登录超时时间
默认dashboard登录超时时间是15min，可以为dashboard容器增加-- token-ttl参数自定义超时时间。

修改Deployment配置超时时间12h：
```bash
args:
  - '--namespace=kubernetes-dashboard'
  - '--auto-generate-certificates'
  - '--token-ttl=43200'
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604305765408-e9f50d48-1680-412f-9db7-40583fd327bc.png#align=left&display=inline&height=266&originHeight=266&originWidth=802&size=24696&status=done&style=none&width=802)

参考：[Dashboard arguments](https://github.com/kubernetes/dashboard/blob/master/docs/common/dashboard-arguments.md)

<a name="9hbrV"></a>
## 参考资料

- [Web UI (Dashboard)](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
- [kubernetes-dashboard(1.8.3)部署与踩坑](https://www.cnblogs.com/RainingNight/p/deploying-k8s-dashboard-ui.html)
- [Kubernates DashBoard - GitHub](https://github.com/kubernetes/dashboard)
- [Heapster - GitHub](https://github.com/kubernetes-retired/heapster)


