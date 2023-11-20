<a name="lFeJc"></a>
## 一、Grafana简介



<a name="8gr4f"></a>
## 二、安装Grafana
<a name="fV5p9"></a>
### 通过Helm安装
添加仓库并更新：
```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create namespace grafana
```
部署Grafana：
```bash
helm install grafana grafana/grafana -n grafana
```
部署完成，看到控制台打印：
```bash
NAME: grafana
LAST DEPLOYED: Fri Oct 30 17:38:22 2020
NAMESPACE: grafana
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:

   kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

   grafana.grafana.svc.cluster.local

   Get the Grafana URL to visit by running these commands in the same shell:

     export POD_NAME=$(kubectl get pods --namespace grafana -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}")
     kubectl --namespace grafana port-forward $POD_NAME 3000

3. Login with the password from step 1 and the username: admin
#################################################################################
######   WARNING: Persistence is disabled!!! You will lose your data when   #####
######            the Grafana pod is terminated.                            #####
#################################################################################
```

<a name="wdRKG"></a>
### 通过Docker安装（仅供了解）
```bash
docker pull grafana/grafana
docker run -d -p 3000:3000 --name grafana --restart=always grafana/grafana

# or
docker run -d -p 3000:3000 --name grafana grafana/grafana
docker update --restart=always grafana
```

<a name="7ljo1"></a>
### 通过yum安装（仅供了解）
```bash
yum install https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-6.3.3-1.x86_64.rpm -y
systemctl start grafana-server
systemctl enable grafana-server
```

<a name="t3XnW"></a>
### 通过yaml文件部署（仅供了解）
```yaml
apiVersion: v1
kind: Service
metadata:
  name: grafana-dashboard
spec:
  template:
    metadata:
      labels:
        name: grafana-dashboard
        namespace: grafana-dashboard
  selector:
    run: grafana-dashboard-pod
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
---
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: grafana-dashboard-pod
  namespace: kube-system
spec:
  replicas: 4
  template:
    metadata:
      labels:
        run: grafana-dashboard-pod
    spec:
      containers:
        - name: grafana
          image: grafana/grafana:latest
          ports:
            - containerPort: 3000
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: grafana-dashboard-ing
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: grafana.test.com
      http:
        paths:
          - backend:
              serviceName: grafana-dashboard
              servicePort: 3000
```

<a name="4k5HX"></a>
## 三、暴露Grafana管理界面
首先在hosts中添加：
```bash
127.0.0.1    grafana.dashboard.com
```
创建一个 IngressRoute：
```bash
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: grafana-route
  namespace: grafana
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`grafana.dashboard.com`)
      kind: Rule
      services:
        - name: grafana
          port: 80
```
应用即可：
```bash
kubectl apply -f route.yaml -n grafana
```

<a name="iy3eS"></a>
## 四、访问Prometheus管理界面
经过前面的一通操作，我们可以直接在浏览器中输入 [http://grafana.dashboard.com](http://grafana.dashboard.com/) 访问：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604051853166-e7815ee2-f83f-472b-bd37-bacb3d521f88.png#align=left&display=inline&height=694&originHeight=694&originWidth=1176&size=180249&status=done&style=none&width=1176)<br />第一次访问的时候，通过以下命令获取密码：
```bash
$ kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
C0RUtQQajyLEqJ5pyfNXvtvLgYMEYOSIukFlngjf
```
用户名为 admin，用刚刚获取到的密码登录：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604051982668-62d68cb3-ad68-45bc-b9e5-df9d123fc7a3.png#align=left&display=inline&height=963&originHeight=963&originWidth=1899&size=307649&status=done&style=none&width=1899)

<a name="YmZUh"></a>
## 五、配置 DataSource
添加一个数据源<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813793386-0577a2f4-6e03-445c-af5a-ae1c2b7b5288.png#align=left&display=inline&height=671&originHeight=671&originWidth=1538&size=0&status=done&style=none&width=1538)

把 Prometheus 的地址填上<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813811484-0c3c50b8-ee79-40da-94ef-bcebab0db939.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)

导入 prometheus 的模板<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813827259-0892a388-c419-4ca2-bd9d-933b135682d6.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)

打开左上角选择已经导入的模板会看到已经有各种图<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813844391-d99a5c13-823a-4ce9-b498-9ad987017fd7.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)

导入模板：文件路径 `k8s-ha-install/heapster/grafana-dashboard`<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813862802-3f7d950e-86f5-451b-aece-d32ca8f2db06.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813888767-18909ccb-f5bd-4e83-9d20-c24962cf0bf4.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)

