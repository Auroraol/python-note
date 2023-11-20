<a name="Ngivj"></a>
## 一、GitLab简介

<a name="VxbDe"></a>
## 二、安装GitLab
<a name="B0wCf"></a>
### 添加helm源
```bash
helm repo add stable https://charts.helm.sh/stable
helm repo add aliyun https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo add  apphub https://apphub.aliyuncs.com/
```

<a name="HFJFU"></a>
### 拉取chart
通过helm拉取chart：
```bash
helm pull stable/gitlab-ce
```
查看一下拉取的chart，看到多了一个 `tgz` 文件：
```bash
$ ls
gitlab-ce-0.2.3.tgz
```
将其解压，并进入目录：
```bash
$ tar -zxvf gitlab-ce-0.2.3.tgz
$ ls
gitlab-4.5.3.tgz  gitlab-ce  gitlab-ce-0.2.3.tgz

$ cd gitlab-ce/
$ ls
charts  Chart.yaml  README.md  requirements.lock  requirements.yaml  templates  values.yaml
```

<a name="Yo9fw"></a>
### 修改values
修改 `values.yaml` 的相关配置：
```yaml
externalUrl: http://gitlab.vmware.com/
gitlabRootPassword: "123456"
serviceType: ClusterIP
```
其中：

- externalUrl 为之后需要配置的域名映射
- gitlabRootPassword 为管理员密码，也可以不设置，这样就会在第一次打开gitlab时提示设置
- serviceType 可以设置为NodePort或LoadBalancer，以暴露其内部/外部端口。如果使用Traefik等服务发现，可以设置为ClusterIP，后面不通过端口访问，只通过域名访问

<a name="Rbgx5"></a>
### 修改apiVersion
由于我的Kubernetes版本为v18.8，需要将 `extensions/v1beta1` 修改为 `extensions/v1`。<br />在 `gitlab-ce` 的外层目录执行：
```yaml
$ grep -irl "extensions/v1beta1" gitlab-ce | grep deployment
gitlab-ce/templates/deployment.yaml
gitlab-ce/charts/postgresql/templates/deployment.yaml
gitlab-ce/charts/redis/templates/deployment.yaml
```
可以看到有三个文件包含这样的apiVersion，使用下面的命令将其全部替换即可：
```yaml
$ grep -irl "extensions/v1beta1" gitlab-ce | grep deployment | xargs sed -i 's#extensions/v1beta1#apps/v1#g'
```

<a name="Allo3"></a>
### 添加selector
同样地，由于Kubernetes版本比较高，还需要添加selector。<br />xia先找出需要修改的文件：
```yaml
$ grep -irl "apps/v1" gitlab-ce | grep deployment
gitlab-ce/templates/deployment.yaml
gitlab-ce/charts/postgresql/templates/deployment.yaml
gitlab-ce/charts/redis/templates/deployment.yaml
```
然后只能一个一个地修改了。将 `selector` 添加到 `template` 的同级。<br />`gitlab-ce/templates/deployment.yaml` 
```yaml
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {{ template "gitlab-ce.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ template "gitlab-ce.fullname" . }}
```
`gitlab-ce/charts/postgresql/templates/deployment.yaml` 
```yaml
spec:
  selector:
    matchLabels:
      app: {{ template "postgresql.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ template "postgresql.fullname" . }}
```
`gitlab-ce/charts/redis/templates/deployment.yaml` 
```yaml
spec:
  selector:
    matchLabels:
      app: {{ template "redis.fullname" . }}
  template:
    metadata:
      labels:
        app: {{ template "redis.fullname" . }}
```
<a name="96Zlt"></a>
### 使用helm部署gitlab
一切修改完毕，既可以安装了：
```yaml
helm install gitlab gitlab-ce -n gitlab
```
安装完毕，控制台打印：
```yaml
WARNING: This chart is deprecated
NAME: gitlab
LAST DEPLOYED: Wed Nov  4 01:10:54 2020
NAMESPACE: gitlab
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
##############################################################################
This chart has been deprecated in favor of the official GitLab chart:
http://docs.gitlab.com/ce/install/kubernetes/gitlab_omnibus.html
##############################################################################

1. Get your GitLab URL by running:

  export NODE_IP=$(kubectl get nodes --namespace gitlab -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP/

2. Login as the root user:

  Username: root
  Password: 123456


3. Point a DNS entry at your install to ensure that your specified
   external URL is reachable:

   http://gitlab.vmware.com/
```

<a name="p1zzM"></a>
### 创建PV
刚创建好，所有POD均为Pending状态。这是因为GitLab需要的持久卷没有创建。<br />需要创建pv1到pv4，这里我们通过hostPath的方式创建。

先创建4个hostPath目录，用于存储gitlab的数据：
```bash
mkdir -p /data/gitlab/pv{1..4}
```
创建PV的YAML文件 `pv.yaml` ：
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: gitlab-pv1
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
  -  ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /data/gitlab/pv1

---

apiVersion: v1
kind: PersistentVolume
metadata:
  name: gitlab-pv2
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
  -  ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /data/gitlab/pv2

---

apiVersion: v1
kind: PersistentVolume
metadata:
  name: gitlab-pv3
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
  -  ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /data/gitlab/pv3

---

apiVersion: v1
kind: PersistentVolume
metadata:
  name: gitlab-pv4
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
  -  ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /data/gitlab/pv4
```

最后应用：
```yaml
kubectl apply -f pv.yaml
```

<a name="6i8iJ"></a>
### 创建自签证书
这个不多说了，常规操作：
```yaml
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=gitlab.vmware.com"
Generating a 2048 bit RSA private key
........+++
...........................................................................................................................................+++
writing new private key to 'tls.key'
-----

$ ls
tls.crt  tls.key

$ kubectl create secret tls gitlab-dashboard-tls --key tls.key --cert tls.crt -n gitlab
secret/gitlab-dashboard-tls created
```

<a name="4k5HX"></a>
## 三、暴露GitLab界面
还是使用Traefik暴露访问域名：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: gitlab-route
  namespace: gitlab
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`gitlab.vmware.com`)
      kind: Rule
      services:
        - name: gitlab-gitlab-ce
          port: 80

---

apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: gitlab-route-tls
  namespace: gitlab
spec:
  entryPoints:
    - websecure
  routes:
    - match: Host(`gitlab.vmware.com`)
      kind: Rule
      services:
        - name: gitlab-gitlab-ce
          port: 80
  tls:
    secretName: gitlab-dashboard-tls
```
这里我尝试将websecure的端口换为443，但没成功，暂时不知道解决方案。


<a name="WHbeu"></a>
## 四、访问GitLab界面
浏览器打开 [http://gitlab.vmware.com/](http://gitlab.vmware.com/) 以访问GitLab。<br />HTTP：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604537836357-8b59767d-4eca-4945-a76c-e99b99812f91.png#align=left&display=inline&height=533&originHeight=533&originWidth=1052&size=56025&status=done&style=none&width=1052)<br />HTTPS：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604544510199-fda3a07a-532f-49e9-b4f4-242db2704ce1.png#align=left&display=inline&height=519&originHeight=519&originWidth=1001&size=53323&status=done&style=none&width=1001)

<a name="aucp8"></a>
## 五、使用GitLab
<a name="ViLVe"></a>
### 创建项目
注册账号后登录，并创建一个项目：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604543833447-11d02127-20ce-4168-a591-1d0482584eeb.png#align=left&display=inline&height=644&originHeight=644&originWidth=1370&size=58737&status=done&style=none&width=1370)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604540031678-0fbccbf6-2d69-4101-959e-47666bc7b957.png#align=left&display=inline&height=296&originHeight=296&originWidth=1892&size=72858&status=done&style=none&width=1892)

查看项目：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604541482928-82b44317-8845-443d-b997-0f313d87ac73.png#align=left&display=inline&height=406&originHeight=406&originWidth=1895&size=94616&status=done&style=none&width=1895)

<a name="lJ7Ik"></a>
### 使用HTTP的方式访问
尝试clone此项目：
```bash
git clone http://gitlab.vmware.com/quanzaiyu/test.git
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604539967702-2cb35bc3-90bf-4761-a044-4b34ab3690c2.png#align=left&display=inline&height=176&originHeight=176&originWidth=878&size=250909&status=done&style=none&width=878)<br />clone成功：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604540185085-84311fae-b740-4775-8a7f-cd4cf34aad71.png#align=left&display=inline&height=114&originHeight=114&originWidth=528&size=11789&status=done&style=none&width=528)

<a name="X6g4F"></a>
### 使用HTTPS的方式访问
如果尝试使用HTTPS的方式clone，会报自签证书错误：
```yaml
SSL certificate problem: self signed certificate
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604543478114-c89f5ab2-254d-42f9-8c16-2edb95cd6661.png#align=left&display=inline&height=102&originHeight=102&originWidth=1459&size=229600&status=done&style=none&width=1459)<br />说明自签证书并不适用，可以使用Let's Encrypt，或者云服务器。

<a name="6bOuJ"></a>
## 参考资料

- [helm3安装gitlab](https://blog.51cto.com/14268033/2456991)

