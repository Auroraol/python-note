<a name="495dd98d"></a>
## 一、Nginx简介
Nginx是一个常见的Web容器，也能做负载均衡器、反向代理工具，本文只讲述其作为Web容器的使用方式。

<a name="n78wr"></a>
## 二、安装Metrics Server
<a name="FQdYW"></a>
### 使用Helm安装
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install nginx bitnami/nginx -n test
```
部署完成，控制台打印：
```bash
NAME: nginx
LAST DEPLOYED: Sun Nov  1 21:28:17 2020
NAMESPACE: test
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
** Please be patient while the chart is being deployed **

NGINX can be accessed through the following DNS name from within your cluster:

    nginx.test.svc.cluster.local (port 80)

To access NGINX from outside the cluster, follow the steps below:

1. Get the NGINX URL by running these commands:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace test -w nginx'

    export SERVICE_PORT=$(kubectl get --namespace test -o jsonpath="{.spec.ports[0].port}" services nginx)
    export SERVICE_IP=$(kubectl get svc --namespace test nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    echo "http://${SERVICE_IP}:${SERVICE_PORT}"
```

<a name="D8xD5"></a>
### 使用YAML安装
<a name="vlI9V"></a>
#### 使用宿主机存储

1. 创建Deployment：

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
          hostPath:
            path: /run/desktop/mnt/host/d/Users/quanzaiyu/.docker/datas/nginx/html
            type: Directory

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
      protocol: TCP
      targetPort: 80
      name: http
      nodePort: 30088
  selector:
    nginx-app: nginx
```

2. 测试浏览器访问

在hostPath中录入一些数据:

```bash
Hello, Welcome to my website...
```

访问 `[http://localhost:30088/](http://localhost:30088/)` 即可。

Ingress或Traefik Route不多说了，比较简单。

<a name="gjuxH"></a>
#### 使用 PVC 存储

以下示例, 演示在 k8s 中配置 nginx 网页文件使用 PVC 持久化存储

1. 创建副本控制器, ReplicationController 配置如下:

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-test
  labels:
    name: nginx-test
spec:
  replicas: 2
  selector:
    name: nginx-test
  template:
    metadata:
      labels:
        name: nginx-test
    spec:
      containers:
        - name: nginx-test
          image: nginx
          volumeMounts:
            - mountPath: /usr/share/nginx/html
              name: nginx-data
          ports:
            - containerPort: 80
      volumes:
        - name: nginx-data
          persistentVolumeClaim: # 指定使用的PVC
            claimName: nfs-data
```

2. 创建服务, 配置如下:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  labels:
    name: nginx-service
spec:
  type: NodePort
  ports:
    - port: 80
      protocol: TCP
      targetPort: 80
      name: http
      nodePort: 30088
  selector:
    name: nginx-test
```

3. 查看存储卷的路径

选择 PVC<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814768860-50a0bc22-d45c-48f9-b94c-aa0b709b365d.png#align=left&display=inline&height=906&originHeight=906&originWidth=1899&size=0&status=done&style=none&width=1899)

选择 PV<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814793179-f2e6e4f6-3bee-4fd8-a170-be1a0d7338f2.png#align=left&display=inline&height=570&originHeight=570&originWidth=1489&size=0&status=done&style=none&width=1489)

找到 GlusterFS 中的路径<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814815206-06ea8188-fa27-419f-81b7-25604c956aaf.png#align=left&display=inline&height=936&originHeight=936&originWidth=1216&size=0&status=done&style=none&width=1216)

4. 将 PV 挂载到宿主机

使用上面看到的路径, 将 PV 挂载到宿主机 `/test1` 路径下

```bash
$ mount -t glusterfs 172.18.50.200:vol_17fbf7ad28666ccbf55e4d6fe5d9a8d8 /test1/
```

其中 172.18.50.200 是宿主机(k8s-master)的 IP, 也可为其他 node 的 IP

5. 往宿主机挂载点写点数据

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814856453-f4e864f9-da7e-429c-906e-a2149ff21c61.png#align=left&display=inline&height=102&originHeight=102&originWidth=1080&size=0&status=done&style=none&width=1080)

6. 进入到 pod 验证

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814885577-4dbd7a2c-e1fa-4d10-af61-3378ef903e88.png#align=left&display=inline&height=244&originHeight=244&originWidth=1104&size=0&status=done&style=none&width=1104)

看到, 在宿主机往 /test1 写入的数据, 进入 pod 依然能够看到

7. 浏览器测试

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1599814921721-31e7f2fd-222a-4fdf-9721-02ba063758e4.png#align=left&display=inline&height=755&originHeight=755&originWidth=1315&size=0&status=done&style=none&width=1315)

<a name="35808e79"></a>
## 参考资料

- [在 kubernetes 集群中运行 nginx](https://blog.51cto.com/ylw6006/2071845)
