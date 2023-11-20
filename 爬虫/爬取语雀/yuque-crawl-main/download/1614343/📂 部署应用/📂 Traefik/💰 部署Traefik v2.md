<a name="J5vbg"></a>
## 一、Traefik简介

- [traefik - GitHub](https://github.com/traefik/traefik)
- [traefik-helm-chart - GitHub ](https://github.com/traefik/traefik-helm-chart)

[Træfɪk](https://github.com/traefik/traefik) 是一个为了让部署微服务更加便捷而诞生的现代HTTP反向代理、负载均衡工具。 它支持多种后台 (Docker, Swarm, Kubernetes, Marathon, Mesos, Consul, Etcd, Zookeeper, BoltDB, Rest API, file…) 来自动化、动态的应用它的配置文件设置。

除了众多的功能之外，Traefik 的与众不同之处还在于它会自动发现适合你服务的配置。当 Traefik 在检查你的服务时，会找到服务的相关信息并找到合适的服务来满足对应的请求。

使用 Traefik，不需要维护或者同步一个独立的配置文件：因为一切都会自动配置，实时操作的（无需重新启动，不会中断连接）。使用 Traefik，你可以花更多的时间在系统的开发和新功能上面，而不是在配置和维护工作状态上面花费大量时间。

![aHR0cHM6Ly93d3cucWlrcWlhay5jb20vazhzdHJhaW4vYXNzZXRzL2ltZy9uZXR3b3JrL3RyYWVmaWstYXJjaGl0ZWN0dXJlLnBuZw.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601899804614-3af01d74-8cbb-4d73-859f-d108e1bfa1a0.png#align=left&display=inline&height=1501&originHeight=1501&originWidth=2875&size=463097&status=done&style=none&width=2875)

<a name="Crgnt"></a>
### 相关概念
Traefik 是一个边缘路由器，是你整个平台的大门，拦截并路由每个传入的请求：它知道所有的逻辑和规则，这些规则确定哪些服务处理哪些请求；传统的反向代理需要一个配置文件，其中包含路由到你服务的所有可能路由，而 Traefik 会实时检测服务并自动更新路由规则，可以自动服务发现。

![aHR0cHM6Ly93d3cucWlrcWlhay5jb20vazhzdHJhaW4vYXNzZXRzL2ltZy9uZXR3b3JrL3RyYWVmaWstYXJjaGl0ZWN0dXJlLW92ZXJ2aWV3LnBuZw.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601899857508-f4df1734-5d72-449d-8ab7-15d977513ea3.png#align=left&display=inline&height=1493&originHeight=1493&originWidth=3174&size=369529&status=done&style=none&width=3174)

首先，当启动 Traefik 时，需要定义 entrypoints（入口点），然后，根据连接到这些 entrypoints 的路由来分析传入的请求，来查看他们是否与一组规则相匹配，如果匹配，则路由可能会将请求通过一系列中间件转换过后再转发到你的服务上去。

在了解 Traefik 之前有几个核心概念我们必须要了解：

- `Providers` 用来自动发现平台上的服务，可以是编排工具、容器引擎或者 key-value 存储等，比如 Docker、Kubernetes、File
- `Entrypoints` 监听传入的流量（端口等…），是网络入口点，它们定义了接收请求的端口（HTTP 或者 TCP）。
- `Routers` 分析请求（host, path, headers, SSL, …），负责将传入请求连接到可以处理这些请求的服务上去。
- `Services` 将请求转发给你的应用（load balancing, …），负责配置如何获取最终将处理传入请求的实际服务。
- `Middlewares` 中间件，用来修改请求或者根据请求来做出一些判断（authentication, rate limiting, headers, …），中间件被附件到路由上，是一种在请求发送到你的服务之前（或者在服务的响应发送到客户端之前）调整请求的一种方法。

<a name="RmSQS"></a>
## 二、安装Traefik
<a name="c7gFo"></a>
### 使用Helm安装
添加仓库并更新：
```bash
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
```
先创建一个namespace，以免默认添加到default：
```bash
kubectl create ns traefik
```
部署[Traefik](https://artifacthub.io/packages/helm/traefik/traefik)：
```bash
helm install traefik traefik/traefik -n traefik
```

部署完，会在控制台中打印：
```bash
W1102 00:33:27.555359   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.561760   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.568528   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.584942   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.596107   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.618944   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:27.641876   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.647233   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.648860   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.651210   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.653531   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.655136   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.657001   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
W1102 00:33:29.658686   88295 warnings.go:67] apiextensions.k8s.io/v1beta1 CustomResourceDefinition is deprecated in v1.16+, unavailable in v1.22+; use apiextensions.k8s.io/v1 CustomResourceDefinition
NAME: traefik
LAST DEPLOYED: Mon Nov  2 00:33:29 2020
NAMESPACE: traefik
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

<a name="tXIiG"></a>
### 手动通过YAML部署
如果想要更加灵活地调整Traefik的参数，也可以创建以下一系列的YAML，手动部署。

`traefik-crd.yaml` 
```yaml
## IngressRoute
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ingressroutes.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: IngressRoute
    plural: ingressroutes
    singular: ingressroute
---
## IngressRouteTCP
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ingressroutetcps.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: IngressRouteTCP
    plural: ingressroutetcps
    singular: ingressroutetcp
---
## Middleware
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: middlewares.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: Middleware
    plural: middlewares
    singular: middleware
---
## TLSOption
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: tlsoptions.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: TLSOption
    plural: tlsoptions
    singular: tlsoption
---
## TraefikService
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: traefikservices.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: TraefikService
    plural: traefikservices
    singular: traefikservice
---
## TLSStore
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: tlsstores.traefik.containo.us
spec:
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: TLSStore
    plural: tlsstores
    singular: tlsstore
  scope: Namespaced
---
## IngressRouteUDP
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ingressrouteudps.traefik.containo.us
spec:
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: IngressRouteUDP
    plural: ingressrouteudps
    singular: ingressrouteudp
  scope: Namespaced
```

`traefik-rbac.yaml` 
```yaml
## ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: traefik
  name: traefik-ingress-controller
---
## ClusterRole
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress-controller
rules:
  - apiGroups: [""]
    resources: ["services","endpoints","secrets"]
    verbs: ["get","list","watch"]
  - apiGroups: ["extensions"]
    resources: ["ingresses"]
    verbs: ["get","list","watch"]
  - apiGroups: ["extensions"]
    resources: ["ingresses/status"]
    verbs: ["update"]
  - apiGroups: ["traefik.containo.us"]
    resources: ["middlewares","ingressroutes","ingressroutetcps","tlsoptions","ingressrouteudps","traefikservices","tlsstores"]
    verbs: ["get","list","watch"]
---
## ClusterRoleBinding
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

`traefik-config.yaml` 
```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: traefik-config
data:
  traefik.yaml: |-
    ping: ""                    ## 启用 Ping
    serversTransport:
      insecureSkipVerify: true  ## Traefik 忽略验证代理服务的 TLS 证书
    api:
      insecure: true            ## 允许 HTTP 方式访问 API
      dashboard: true           ## 启用 Dashboard
      debug: false              ## 启用 Debug 调试模式
    metrics:
      prometheus: ""            ## 配置 Prometheus 监控指标数据，并使用默认配置
    entryPoints:
      web:
        address: ":80"          ## 配置 80 端口，并设置入口名称为 web
      websecure:
        address: ":443"         ## 配置 443 端口，并设置入口名称为 websecure
    providers:
      kubernetesCRD: ""         ## 启用 Kubernetes CRD 方式来配置路由规则
      kubernetesIngress: ""     ## 启动 Kubernetes Ingress 方式来配置路由规则
    log:
      filePath: ""              ## 设置调试日志文件存储路径，如果为空则输出到控制台
      level: error              ## 设置调试日志级别
      format: json              ## 设置调试日志格式
    accessLog:
      filePath: ""              ## 设置访问日志文件存储路径，如果为空则输出到控制台
      format: json              ## 设置访问调试日志格式
      bufferingSize: 0          ## 设置访问日志缓存行数
      filters:
        #statusCodes: ["200"]   ## 设置只保留指定状态码范围内的访问日志
        retryAttempts: true     ## 设置代理访问重试失败时，保留访问日志
        minDuration: 20         ## 设置保留请求时间超过指定持续时间的访问日志
      fields:                   ## 设置访问日志中的字段是否保留（keep 保留、drop 不保留）
        defaultMode: keep       ## 设置默认保留访问日志字段
        names:                  ## 针对访问日志特别字段特别配置保留模式
          ClientUsername: drop  
        headers:                ## 设置 Header 中字段是否保留
          defaultMode: keep     ## 设置默认保留 Header 中字段
          names:                ## 针对 Header 中特别字段特别配置保留模式
            User-Agent: redact
            Authorization: drop
            Content-Type: keep
    #tracing:                     ## 链路追踪配置,支持 zipkin、datadog、jaeger、instana、haystack 等 
    #  serviceName:               ## 设置服务名称（在链路追踪端收集后显示的服务名）
    #  zipkin:                    ## zipkin配置
    #    sameSpan: true           ## 是否启用 Zipkin SameSpan RPC 类型追踪方式
    #    id128Bit: true           ## 是否启用 Zipkin 128bit 的跟踪 ID
    #    sampleRate: 0.1          ## 设置链路日志采样率（可以配置0.0到1.0之间的值）
    #    httpEndpoint: http://localhost:9411/api/v2/spans     ## 配置 Zipkin Server 端点
```

`traefik-deploy.yaml` 
```yaml
apiVersion: v1
kind: Service
metadata:
  name: traefik
spec:
  ports:
    - name: web
      port: 80
    - name: websecure
      port: 443
    - name: admin
      port: 8080
  selector:
    app: traefik
  type: LoadBalancer
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: traefik-ingress-controller
  labels:
    app: traefik
spec:
  selector:
    matchLabels:
      app: traefik
  template:
    metadata:
      name: traefik
      labels:
        app: traefik
    spec:
      serviceAccountName: traefik-ingress-controller
      terminationGracePeriodSeconds: 1
      containers:
        - image: traefik:v2.3.1
          name: traefik-ingress-lb
          ports:
            - name: web
              containerPort: 80
              hostPort: 80         ## 将容器端口绑定所在服务器的 80 端口
            - name: websecure
              containerPort: 443
              hostPort: 443        ## 将容器端口绑定所在服务器的 443 端口
            - name: admin
              containerPort: 8080  ## Traefik Dashboard 端口
          resources:
            limits:
              cpu: 2000m
              memory: 1024Mi
            requests:
              cpu: 1000m
              memory: 1024Mi
          securityContext:
            capabilities:
              drop:
                - ALL
              add:
                - NET_BIND_SERVICE
          args:
            - --configfile=/config/traefik.yaml
          volumeMounts:
            - mountPath: "/config"
              name: "config"
          readinessProbe:
            httpGet:
              path: /ping
              port: 8080
            failureThreshold: 3
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
          livenessProbe:
            httpGet:
              path: /ping
              port: 8080
            failureThreshold: 3
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 5
      volumes:
        - name: config
          configMap:
            name: traefik-config
      tolerations:              ## 设置容忍所有污点，防止节点被设置污点
        - operator: "Exists"
      nodeSelector:             ## 设置node筛选器，在特定label的节点上启动
        IngressProxy: "true"
```

`traefik-dashboard-route.yaml` 
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard-route
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.dashboard.com`)
      kind: Rule
      services:
        - name: traefik
          port: 8080

---

apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard-route-tls
  namespace: traefik
spec:
  entryPoints:
    - websecure
  routes:
    - match: Host(`traefik.dashboard.com`)
      kind: Rule
      services:
        - name: traefik
          port: 8080
  tls:
    secretName: traefik-dashboard-tls
```

所有文件都创建好之后，全部apply即可：
```yaml
kubectl apply -f . -n traefik
```

<a name="4k5HX"></a>
## 三、暴露Traefik Dashboard

默认情况下，为了安全，Traefik没有暴露Dashboard，我们可以使用Traefik自定义的IngressRoute资源，暴露Traefik Dashboard。<br />`dashboard.yaml` 如下：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard
  namespace: traefik
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.dashboard.com`)
      kind: Rule
      services:
        - name: api@internal
          kind: TraefikService
```
然后：
```yaml
kubectl apply -f dashboard.yaml
```
如果是本地测试环境，将 `127.0.0.1 traefik.dashboard.com` （若为虚拟机，换为自己虚拟机的IP）添加到hosts，如果是线上环境，将域名解析到指定服务器IP，当然，域名换为自己备案的域名。

<a name="WHbeu"></a>
## 四、访问Traefik Dashboard
经过前面的一通操作，我们可以直接在浏览器中输入 [http://traefik.dashboard.com](http://traefik.dashboard.com) 访问：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601899278048-7d0db1f4-ee64-4838-84c8-27677f3625b1.png#align=left&display=inline&height=985&originHeight=985&originWidth=1493&size=130284&status=done&style=none&width=1493)

<a name="BmyG3"></a>
## 五、使用IngressRoute进行路由控制
<a name="a85md"></a>
### 配置HTTP路由
这里以Nginx为例，创建一个HTTP的路由访问规则。

先创建一个Nginx服务：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nginx

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  namespace: nginx
  labels:
    nginx-app: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      nginx-app: nginx
  template:
    metadata:
      labels:
        nginx-app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 80
          volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: nginx-data
      volumes:
        - name: nginx-data
          emptyDir: {}

---

apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30002
  selector:
    nginx-app: nginx
```
再创建一个 `IngressRoute` 资源：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: nginx
  namespace: nginx
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`nginx.test.com`)
      kind: Rule
      services:
        - name: nginx
          port: 80
```
将 `nginx.test.com` 添加到hosts，或解析到服务器IP。

在Traefik Dashboard中可以看到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601901469734-82fc44ec-d58d-4c26-b17d-a280f8edc488.png#align=left&display=inline&height=692&originHeight=692&originWidth=1515&size=125952&status=done&style=none&width=1515)

在浏览器中输入 [http://nginx.test.com/](http://nginx.test.com/) 和 [http://localhost:30002/](http://localhost:30002/)，均可看到相同的内容，说明路由解析成功。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1601901372519-c225adff-d860-4339-9357-1249c65cd8e1.png#align=left&display=inline&height=137&originHeight=137&originWidth=788&size=11055&status=done&style=none&width=788)

<a name="Fs5rc"></a>
### 配置HTTPS路由
以Traefik Dashboard为例：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard-tls
  namespace: traefik
spec:
  entryPoints:
    - websecure
  routes:
    - match: Host(`traefik.dashboard.com`)
      kind: Rule
      services:
        - name: api@internal
          kind: TraefikService
  tls:
    secretName: traefik-dashboard-tls
```
注意到，entryPoints写为了websecure，并且新增一个证书 `traefik-dashboard-tls` 。

我在本地测试的，所以就不做CA证书了，自签名一个证书：
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=traefik.dashboard.com"
kubectl create secret tls traefik-dashboard-tls --key tls.key --cert tls.crt -n traefik
```

通过HTTPS访问，发现成功：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604395577188-4cc6ac63-a5f5-4d1c-ac97-a6a6b71bd6ca.png#align=left&display=inline&height=329&originHeight=329&originWidth=811&size=32770&status=done&style=none&width=811)<br />因为是自签证书，报“不安全”很正常，不用管它。

<a name="2kbft"></a>
### 强制HTTPS
创建一个中间件，将HTTP全部转向HTTPS：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: redirect-https
spec:
  redirectScheme:
    scheme: https
```
在需要重定向到HTTPS的路由中加入middlewares字段：
```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard
  namespace: traefik
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.dashboard.com`)
      kind: Rule
      middlewares:
        - name: redirect-https
      services:
        - name: api@internal
          kind: TraefikService
```
再次访问 [http://traefik.dashboard.com/](http://traefik.dashboard.com/dashboard/#/)，发现会自动重定向到 [https://traefik.dashboard.com/](https://traefik.dashboard.com/dashboard/#/)

<a name="ApQia"></a>
## 六、使用Ingress进行服务发现
<a name="VH7Yr"></a>
### 配置HTTP
当然，也可以不使用Traefik v2提供的IngressRoute这个自定义资源，而是使用Kubernetes自带的Ingress，这也完全没问题，不过可能会失去一些比较好的特性。<br />还是以Traefik Dashboard为例：
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: traefik-dashboard-ingress
  namespace: traefik
  annotations:
    kubernetes.io/ingress.class: traefik
    traefik.ingress.kubernetes.io/router.entrypoints: web
spec:
  rules:
  - host: traefik.dashboard.com
    http:
      paths:
      - path: /
        backend:
          serviceName: traefik
          servicePort: 8080
```
这里需要注意的是，需要添加两个注解：
```yaml
annotations:
  kubernetes.io/ingress.class: traefik
  traefik.ingress.kubernetes.io/router.entrypoints: web
```
很明了了，第一个注解表示使用traefik来做服务发现，第二个注解表示入口为web（HTTP）。

<a name="BQ2WG"></a>
### 配置HTTPS
如果要使用HTTPS访问，进行如下配置即可：
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: traefik-dashboard-ingress
  namespace: traefik
  annotations:
    kubernetes.io/ingress.class: traefik
    traefik.ingress.kubernetes.io/router.tls: "true"
    traefik.ingress.kubernetes.io/router.entrypoints: websecure
spec:
  tls:
  - secretName: traefik-dashboard-tls
  rules:
  - host: traefik.dashboard.com
    http:
      paths:
      - path: /
        backend:
          serviceName: traefik
          servicePort: 8080
```
注意到，比起HTTP的方式，这里增加了一个注解：
```yaml
traefik.ingress.kubernetes.io/router.tls: "true"
```
并且入口点选择了 `websecure` ，在spec下增加了tls证书配置。

<a name="nmiBz"></a>
## 七、关于自定义资源
Traefik为用户定义了几个自定义资源，从Dashboard中就可以看出：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603890979236-0a332746-9f17-499b-b4f9-9f4b0c135de2.png#align=left&display=inline&height=864&originHeight=864&originWidth=1909&size=129917&status=done&style=none&width=1909)<br />我们上面定义路由时已经用到了 `IngressRoute` ，这是一个Kubernetes中内置Ingress的替代品，编写YAML时感觉清爽了不少。

点进自定义资源，可以看到以创建的资源对象：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603891197040-a0342733-32b0-4f5d-a5d9-cd10b064a1c0.png#align=left&display=inline&height=844&originHeight=844&originWidth=1900&size=122008&status=done&style=none&width=1900)

<a name="CPOpI"></a>
### 路由规则

<a name="34TbF"></a>
### 中间件

<a name="XotL4"></a>
## 参考资料

- [Kubernetes 部署 Ingress 控制器 Traefik v2.1](http://www.mydlq.club/article/58/)
- [Kubernetes 部署 Ingress 控制器 Traefik v2.2](http://www.mydlq.club/article/72/)
- [kubernetes部署traefik](https://blog.csdn.net/networken/article/details/85953346)
- [Traefik 2 使用指南，愉悦的开发体验](https://zhuanlan.zhihu.com/p/104224442)
- [一文搞懂 Traefik2.1 的使用](https://www.qikqiak.com/post/traefik-2.1-101/)

