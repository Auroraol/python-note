<a name="3AuwY"></a>
## 一、Jenkins简介
引用官方的话来说：<br />[Jenkins](https://www.jenkins.io/zh/)是开源CI&CD软件领导者， 提供超过1000个插件来支持构建、部署、自动化， 满足任何项目的需要。

<a name="n78wr"></a>
## 二、安装Jenkins
<a name="FQdYW"></a>
### 使用Helm安装
添加仓库并更新：
```bash
helm repo add jenkins https://charts.jenkins.io
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create ns jenkins

```
部署[Jenkins](https://artifacthub.io/packages/helm/jenkinsci/jenkins)：
```bash
helm install jenkins jenkins/jenkins -n jenkins
```

部署完，会在控制台中打印：
```yaml
NAME: jenkins
LAST DEPLOYED: Sun Nov  1 15:26:12 2020
NAMESPACE: jenkins
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:
  printf $(kubectl get secret --namespace jenkins jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode);echo
2. Get the Jenkins URL to visit by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace jenkins -l "app.kubernetes.io/component=jenkins-master" -l "app.kubernetes.io/instance=jenkins" -o jsonpath="{.items[0].metadata.name}")
  echo http://127.0.0.1:8080
  kubectl --namespace jenkins port-forward $POD_NAME 8080:8080

3. Login with the password from step 1 and the username: admin

4. Use Jenkins Configuration as Code by specifying configScripts in your values.yaml file, see documentation: http:///configuration-as-code and examples: https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos

For more information on running Jenkins on Kubernetes, visit:
https://cloud.google.com/solutions/jenkins-on-container-engine
For more information about Jenkins Configuration as Code, visit:
https://jenkins.io/projects/jcasc/
```


<a name="D8xD5"></a>
### 使用YAML安装
<a name="AWhT2"></a>
#### 创建命名空间
首先创建一个命名空间，命名为jenkins：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: jenkins
```

<a name="yBzBT"></a>
#### 创建服务
创建一个服务：
```yaml
apiVersion: v1
kind: Service
metadata:
  name: jenkins
  namespace: jenkins
spec:
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
  selector:
    jenkins-app: jenkins
```
<a name="K0pRK"></a>
#### 创建部署
这里，我们使用Deployment部署
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jenkins
  namespace: jenkins
  labels:
    jenkins-app: jenkins
spec:
  replicas: 1
  selector:
    matchLabels:
      jenkins-app: jenkins
  template:
    metadata:
      labels:
        jenkins-app: jenkins
    spec:
      containers:
        - name: jenkins
          image: jenkinsci/blueocean
          ports:
            - containerPort: 8080
            - containerPort: 50000
          volumeMounts:
            - mountPath: /var/jenkins_home
              name: jenkins-home
      volumes:
        - name: jenkins-home
          hostPath:
            path: /run/desktop/mnt/host/d/Users/quanzaiyu/.docker/datas/jenkins
            type: Directory
```
说明：

- `replicas: 1` 指定为1个副本
- 镜像选择 `jenkinsci/blueocean`
- 暴露容器中的 `8080` 和 `50000` 端口
- 打个标签 `jenkins-app: jenkins`
- 将卷 `/var/jenkins_home` 命名为 `jenkins-home`
- 将 `jenkins-home` 挂载到宿主机 `D:\Users\quanzaiyu\.docker\datas\jenkins` 目录下
- `type: Directory` 表示目录必须先存在，若不存在则会报错

打开Kubernetes Dashboard，可以看到Jenkins已经成功启动：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601430354448-9ed22bf3-5d4e-41ff-8311-583d9da8ce2c.png#align=left&display=inline&height=979&originHeight=979&originWidth=1903&size=149082&status=done&style=none&width=1903)

<a name="RPp8L"></a>
## 四、暴露Jenkins管理界面
首先在hosts中添加：
```bash
127.0.0.1    jenkins.dashboard.com
```
创建一个 IngressRoute：
```bash
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: jenkins-route
  namespace: jenkins
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`jenkins.dashboard.com`)
      kind: Rule
      services:
        - name: jenkins
          port: 8080
```
应用即可：
```bash
kubectl apply -f jenkins/route.yaml
```

<a name="DrHD9"></a>
## 五、访问Jenkins管理界面
在浏览器输入 [http://jenkins.dashboard.com/](http://jenkins.dashboard.com/)  即可访问Jenkins：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603856566203-f6473ec6-abb8-41bd-84fb-40cf0a1e952a.png#align=left&display=inline&height=345&originHeight=345&originWidth=1916&size=61296&status=done&style=none&width=1916)

