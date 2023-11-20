:::info
此文已归档，为几年前初次使用时记录的Traefik v1的安装部署，过程繁琐，现Traefik已升级为v2，使用Helm部署也更加方便了，本文不建议阅读。
:::

[traefik](https://docs.traefik.cn/user-guide/kubernetes) 是一个前端负载均衡器，对于微服务架构尤其是 kubernetes 等编排工具具有良好的支持；

相对于 nginx ingress，traefix 能够实时跟 Kubernetes API 交互，感知后端 Service、Pod 变化，自动更新配置并热重载。Traefik 更快速更方便，同时支持更多的特性，使反向代理、负载均衡更直接更高效。

<a name="1fe61843"></a>
## 一、使用 k8s-ha-install 部署
创建 k8s-master-lb 的证书
```bash
kubectl -n kube-system create secret generic traefik-cert --from-file=tls.key --from-file=tls.crt
```

把证书写入到 k8s 的 secret
```bash
kubectl -n kube-system create secret generic traefik-cert --from-file=tls.key --from-file=tls.crt
```

进入到 k8s-ha-install 目录执行
```bash
[root@k8s-master1 k8s-ha-install]# kubectl apply -f traefik/
serviceaccount/traefik-ingress-controller created
clusterrole.rbac.authorization.k8s.io/traefik-ingress-controller created
clusterrolebinding.rbac.authorization.k8s.io/traefik-ingress-controller created
configmap/traefik-conf created
daemonset.extensions/traefik-ingress-controller created
service/traefik-web-ui created
ingress.extensions/traefik-jenkins created
```

浏览器访问 `http://k8s-master-lb:30011/dashboard/` 即可看到：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813029895-20b070c2-b712-4e0f-897e-f9c572fd5c58.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)

<a name="1sQ8s"></a>
### 创建测试应用
`traefik-test.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  template:
    metadata:
      labels:
        name: nginx-svc
        namespace: traefix-test
  selector:
    run: ngx-pod
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
---
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: ngx-pod
spec:
  replicas: 4
  template:
    metadata:
      labels:
        run: ngx-pod
    spec:
      containers:
        - name: nginx
          image: nginx:1.10
          ports:
            - containerPort: 80
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ngx-ing
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: traefix-test.com
      http:
        paths:
          - backend:
              serviceName: nginx-svc
              servicePort: 80
```

部署资源:
```bash
kubectl create -f traefik-test.yaml
```

过一会儿即可看到：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599812983139-cfa20495-332f-4350-9c92-94c46f0fa143.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=0&status=done&style=none&width=1920)<br />将 `traefix-test.com` 绑定到任一 node 节点即可访问<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813033457-63a9b5e7-b45a-4175-aba7-a2333826fdbd.png#align=left&display=inline&height=339&originHeight=339&originWidth=943&size=0&status=done&style=none&width=943)

<a name="da04e15f"></a>
### HTTPS 访问
创建证书, 若是线上服务器使用申请的域名证书即可
```bash
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=traefix-test.com"
Generating a 2048 bit RSA private key
..................................+++
..........................................................+++
writing new private key to 'tls.key'
-----
```

创建保密字典:
```bash
kubectl -n default create secret tls nginx-test-tls --key=tls.key --cert=tls.crt
```

`traefik-test-https.yaml`
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-https-test
  namespace: default
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: traefix-test.com
      http:
        paths:
          - backend:
              serviceName: nginx-svc
              servicePort: 80
  tls:
    - secretName: nginx-test-tls
```

配置 `tls.secretName` 字段对应为保密字典即可

<a name="c2a2ee12"></a>
### 配置Path级别的路由
只需要在 `spec.rules..http.paths..path` 配置相应的路径即可：
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-https-test
  namespace: default
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: traefix-test.com
      http:
        paths:
          - path: /pc
            backend:
              serviceName: nginx-svc1
              servicePort: 80
          - path: /mp
            backend:
              serviceName: nginx-svc2
              servicePort: 80
  tls:
    - secretName: nginx-test-tls
```

访问的是否使用 `traefix-test.com/pc` 和 `traefix-test.com/mp` 实现相应服务的访问

<a name="078a83ff"></a>
## 二、手动部署
<a name="88210852"></a>
### 准备工作
**创建命名空间**<br />创建命名空间 traefik 用于测试
```bash
$ kubectl create ns traefik
```

**为 node 打标签**
```
kubectl label nodes k8s-master traefik=proxy
kubectl label nodes k8s-node1 traefik=proxy
kubectl label nodes k8s-node2 traefik=proxy
```

<a name="02e5f096"></a>
### 配置 ClusterRole
```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress-controller
rules:
  - apiGroups:
      - ""
    resources:
      - services
      - endpoints
      - secrets
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - extensions
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress-controller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: traefik-ingress-controller
subjects:
  - kind: ServiceAccount
    name: traefik-ingress-controller
    namespace: traefik
```

<a name="b9f5383f"></a>
### 创建 ServiceAccount
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: traefik-ingress-controller
  namespace: traefik
```

<a name="cb417970"></a>
### 使用 DaemonSet 的方式部署
```yaml
kind: DaemonSet
apiVersion: extensions/v1beta1
metadata:
  name: traefik-ingress-controller
  namespace: kube-system
  labels:
    k8s-app: traefik-ingress-lb
spec:
  template:
    metadata:
      labels:
        k8s-app: traefik-ingress-lb
        name: traefik-ingress-lb
    spec:
      serviceAccountName: traefik-ingress-controller
      terminationGracePeriodSeconds: 60
      hostNetwork: true
      containers:
        - image: traefik
          name: traefik-ingress-lb
          ports:
            - name: http
              containerPort: 80
              hostPort: 80
            - name: admin
              containerPort: 8080
          securityContext:
            capabilities:
              drop:
                - ALL
              add:
                - NET_BIND_SERVICE
          args:
            - --api
            - --kubernetes
            - --logLevel=INFO
```

<a name="52823afb"></a>
### 创建 Service 与 Ingress
```yaml
apiVersion: v1
kind: Service
metadata:
  name: traefik-web-ui
spec:
  selector:
    k8s-app: traefik-ingress-lb
  ports:
    - protocol: TCP
      targetPort: 8080
      port: 80
      name: web
    - protocol: TCP
      port: 8080
      nodePort: 30080
      name: admin
  type: NodePort
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: traefik-web-ui
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: ui.traefik.com
      http:
        paths:
          - backend:
              serviceName: traefik-web-ui
              servicePort: 80
```

以上, 暴露 30080 用于外部反向代理使用, 并将 `ui.traefik.com` 解析到 traefik-web-ui 服务

在物理机中将域名加入 hosts 进行访问 `[http://ui.traefik.com/](http://ui.traefik.com/)` 或 `[http://192.168.126.129:30080/](http://192.168.126.129:30080/)` 均可访问：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813083366-8b527478-95a2-430a-b516-fd5c91b6173f.png#align=left&display=inline&height=611&originHeight=611&originWidth=1719&size=0&status=done&style=none&width=1719)<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813099947-f8bd7822-e714-4af3-a1bf-b8d039e5ab36.png#align=left&display=inline&height=369&originHeight=369&originWidth=1716&size=0&status=done&style=none&width=1716)

<a name="55d391a2"></a>
## 三、使用 HTTPS
<a name="e5e8c96b"></a>
### 绑定证书
```bash
# 创建证书
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=k8s-master-lb"
# 绑定证书到k8s
kubectl -n traefik create secret generic traefik-cert --from-file=tls.key --from-file=tls.crt
```

- **-n** 指定命名空间
- **tls** 保密字典类型, 绑定证书则使用 tls
- **traefik-cert** 指定证书的名字
- **--key=/ssl/ssl.key** 证书 key 路径
- **--cert=/ssl/ssl.pem** 证书路径

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813134713-eb1dae81-f9a8-4878-996a-080b06fa9b31.png#align=left&display=inline&height=193&originHeight=193&originWidth=1641&size=0&status=done&style=none&width=1641)

<a name="d264c1a8"></a>
### 创建 ConfigMap
编辑 traefik 配置文件：<br />`traefik.toml`
```bash
defaultEntryPoints = ["http", "https"]
[entryPoints]
  [entryPoints.http]
  address = ":80"
    # [entryPoints.http.redirect]
    # entryPoint = "https"
  [entryPoints.https]
  address = ":443"
    [entryPoints.https.tls]
      [[entryPoints.https.tls.certificates]]
      certFile = "/ssl/tls.crt"
      keyFile = "/ssl/tls.key"
```

```bash
kubectl create configmap traefik-conf --from-file=traefik.toml -n traefik
```

也可使用 yaml 的形式创建：<br />
```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: traefik-conf
  namespace: traefik
data:
  traefik-config: |+
    defaultEntryPoints = ["http", "https"]
    [entryPoints]
      [entryPoints.http]
      address = ":80"
        # [entryPoints.http.redirect]
        # entryPoint = "https"
      [entryPoints.https]
      address = ":443"
        [entryPoints.https.tls]
          [[entryPoints.https.tls.certificates]]
          certFile = "/ssl/tls.crt"
          keyFile = "/ssl/tls.key"
```

<a name="5497b210"></a>
### 修改 DaemonSet
修改 DaemonSet 部署文件, apply 部署后直接删除原 traefik pod 进行配置更新：<br />
```yaml
kind: DaemonSet
apiVersion: extensions/v1beta1
metadata:
  name: traefik-ingress
  labels:
    k8s-app: traefik-ingress-lb
spec:
  template:
    metadata:
      labels:
        k8s-app: traefik-ingress-lb
        name: traefik-ingress-lb
    spec:
      terminationGracePeriodSeconds: 60
      restartPolicy: Always
      serviceAccountName: traefik-ingress-controller
      containers:
        - image: traefik:latest
          name: traefik-ingress-lb
          ports:
            - name: http
              containerPort: 80
              hostPort: 80
            - name: https
              containerPort: 443
              hostPort: 443
            - name: admin
              containerPort: 8080
          args:
            - --configFile=/root/kube-config/apps/traefik/traefik.toml
            - -d
            - --web
            - --kubernetes
            - --logLevel=DEBUG
          volumeMounts:
            - name: traefik-config-volume
              mountPath: /opt/conf/k8s/conf
            - name: traefik-ssl-volume
              mountPath: /opt/conf/k8s/ssl
      volumes:
        - name: traefik-config-volume
          configMap:
            name: traefik-conf
            items:
              - key: traefik-config
                path: traefik.toml
        - name: traefik-ssl-volume
          secret:
            secretName: traefik-cert
```

<a name="c4dd56aa"></a>
### 端口监听测试
查看更新后 node 上的端口监听：
```bash
$ ss -ntlp | grep traefik
LISTEN     0      128         :::8080                    :::*                   users:(("traefik",pid=18337,fd=6))
LISTEN     0      128         :::80                      :::*                   users:(("traefik",pid=18337,fd=3))
LISTEN     0      128         :::443                     :::*                   users:(("traefik",pid=18337,fd=5))
```

<a name="2cd073a8"></a>
## 示例: Kubernetes Dashboard (http 示例)
Dashboard 服务创建参考 [在 Kubernetes 集群中部署 DashBoard](./Dashboard)
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: kubernetes-dashboard-web-ui
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: ui.dashboard.com
      http:
        paths:
          - backend:
              serviceName: kubernetes-dashboard
              servicePort: 443
  tls:
    - secretName: traefik-cert # 证书名字, 若不指定则使用http方式访问
```

在物理机中将域名加入 hosts 进行访问 `[http://ui.dashboard.com/](http://ui.dashboard.com/)`:

<a name="7777455c"></a>
## 示例: 反向代理基于 nginx 的 web 容器 (https 示例)
有如下服务, 以 nginx 为例：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813170171-b4aa041d-a12b-465c-81be-b636ea3d8f9c.png#align=left&display=inline&height=214&originHeight=214&originWidth=1894&size=0&status=done&style=none&width=1894)

<a name="d207d56f"></a>
### 绑定到 traefik
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: traefik-ingress
  namespace: traefik
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
    - host: k8s.nginx.test.xiaoyulive.top
      http:
        paths:
          - backend:
              serviceName: nginx-service
              servicePort: 80
  tls:
    - secretName: traefik-cert
```

成功后, 可以在访问权中看到<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813194536-4801ef6d-13e3-4f9e-bb53-be5041f20d42.png#align=left&display=inline&height=190&originHeight=190&originWidth=1912&size=0&status=done&style=none&width=1912)

- **host** 指定的外部访问域名, 需要域名解析到 k8s-master 的 IP
- **tls** SSL 证书的名称, 为上面创建的证书, 如果指定 tls, 则可以使用 https 的方式访问, 不指定则只能使用 http 访问

<a name="3e84cc7c"></a>
### 在 Treafik 中查看
![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813219512-eb5b1f42-5549-4893-8929-13cdd36df049.png#align=left&display=inline&height=597&originHeight=597&originWidth=1735&size=0&status=done&style=none&width=1735)

<a name="cdbf0e15"></a>
### 浏览器测试访问
浏览器输入 `[http://k8s.nginx.test.xiaoyulive.top:30080/](http://k8s.nginx.test.xiaoyulive.top:30080/)` 即可：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599813248636-52c0b0ac-89bf-4979-ada6-96b1fbebf418.png#align=left&display=inline&height=755&originHeight=755&originWidth=1315&size=0&status=done&style=none&width=1315)

