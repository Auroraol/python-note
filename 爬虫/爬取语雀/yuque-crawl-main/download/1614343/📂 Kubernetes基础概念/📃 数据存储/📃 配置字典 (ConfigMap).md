<a name="9aadcf3b"></a>
## 向容器传递参数

| Docker | Kubernetes | 描述 |
| --- | --- | --- |
| ENTRYPOINT | command | 容器中的可执行文件 |
| CMD | args | 需要传递给可执行文件的参数 |


如果需要向容器传递参数，可以在 Yaml 文件中通过 command 和 args 或者环境变量的方式实现。

```yaml
kind: Pod
spec:
  containers:
    - image: docker.io/nginx
      command: ["/bin/command"]
      args: ["arg1", "arg2", "arg3"]
      env:
        - name: INTERVAL
          value: "30"
        - name: FIRST_VAR
          value: "foo"
        - name: SECOND_VAR
          value: "$(FIRST_VAR)bar"
```

可以看到，我们可以利用 env 标签向容器中传递环境变量，环境变量还可以相互引用。这种方式的问题在于配置文件和部署是绑定的，那么对于同样的应用，测试环境的参数和生产环境是不一样的，这样就要求写两个部署文件，管理起来不是很方便。

<a name="6ab1b4f6"></a>
## 什么是 ConfigMap

上面提到的例子，利用 ConfigMap 可以解耦部署与配置的关系，对于同一个应用部署文件，可以利用`valueFrom`字段引用一个在测试环境和生产环境都有的 ConfigMap（当然配置内容不相同，只是名字相同），就可以降低环境管理和部署的复杂度。

ConfigMap 有三种用法：

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597327024502-f6827898-b6a8-46d5-8f2a-06a34873bbe6.png#align=left&display=inline&height=460&originHeight=460&originWidth=800&size=0&status=done&style=none&width=800)

- 生成为容器内的环境变量
- 设置容器启动命令的参数
- 挂载为容器内部的文件或目录

<a name="1eb9ba92"></a>
## ConfigMap 的缺点

- ConfigMap 必须在 Pod 之前创建
- ConfigMap 属于某个 NameSpace，只有处于相同 NameSpace 的 Pod 才可以应用它
- ConfigMap 中的配额管理还未实现
- 如果是 volume 的形式挂载到容器内部，只能挂载到某个目录下，该目录下原有的文件会被覆盖掉
- 静态 Pod 不能用 ConfigMap

<a name="7519104d"></a>
## ConfigMap 的创建

```bash
kubectl create configmap <map-name> --from-literal=<parameter-name>=<parameter-value>
kubectl create configmap <map-name> --from-literal=<parameter1>=<parameter1-value> --from-literal=<parameter2>=<parameter2-value> --from-literal=<parameter3>=<parameter3-value>
kubectl create configmap <map-name> --from-file=<file-path>
kubectl apply -f <configmap-file.yaml>
# 还可以从一个文件夹创建configmap
kubectl create configmap <map-name> --from-file=/path/to/dir
```

<a name="1118bd17"></a>
## yaml 的声明方式

```yaml
apiVersion: v1
data:
  my-nginx-config.conf: |
    server {
      listen              80;
      server_name         www.kubia-example.com;

      gzip on;
      gzip_types text/plain application/xml;

      location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
      }
    }
  sleep-interval: |
    25
kind: ConfigMap
```

<a name="97428b30"></a>
## ConfigMap 的调用

<a name="3ff373b0"></a>
### 环境变量的方式

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
    - image: nginx
      env:
        - name: INTERVAL
          valueFrom:
            configMapKeyRef:
              name: <map-name>
              key: sleep-interval
```

:::warning
如果引用了一个不存在的 ConfigMap，则创建 Pod 时会报错，直到能够正常读取 ConfigMap 后，Pod 会自动创建。
:::

一次传递所有的环境变量

```yaml
spec:
  containers:
    - image: nginx
      envFrom:
        - prefix: CONFIG_
          configMapRef:
            name: <map-name>
```

<a name="6eb8a7be"></a>
### 命令行参数的方式

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
    - image: nginx
      env:
        - name: INTERVAL
          valueFrom:
            configMapKeyRef:
              name: <map-name>
              key: sleep-interval
      args: ["$(INTERVAL)"]
```

<a name="a7867b73"></a>
### 以配置文件的方式

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-test
spec:
  containers:
    - image: nginx
      name: web-server
      volumeMounts:
        - name: config
          mountPath: /etc/nginx/conf.d
          readOnly: true
  volumes:
    - name: config
      configMap:
        name: <map-name>
```

将 Configmap 挂载为一个文件夹后，原来在镜像中的文件夹里的内容就看不到，这是什么原理？这是因为原来文件夹下的内容无法进入，所以显示不出来。为了避免这种挂载方式影响应用的正常运行，可以将 configmap 挂载为一个配置文件。

```yaml
spec:
  containers:
    - image: nginx
      volumeMounts:
        - name: config
          mountPath: /etc/someconfig.conf
          subPath: myconfig.conf
```

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597326915315-a781d5e2-df07-4d22-a6a2-808d18cb9bc4.png#align=left&display=inline&height=446&originHeight=446&originWidth=880&size=0&status=done&style=none&width=880)

<a name="CrFO5"></a>
## Configmap 的更新

```bash
kubectl edit configmap <map-name>
```

confgimap 更新后，如果是以文件夹方式挂载的，会自动将挂载的 Volume 更新。如果是以文件形式挂载的，则不会自动更新。<br />但是对多数情况的应用来说，配置文件更新后，最简单的办法就是重启 Pod（杀掉再重新拉起）。如果是以文件夹形式挂载的，可以通过在容器内重启应用的方式实现配置文件更新生效。即便是重启容器内的应用，也要注意 configmap 的更新和容器内挂载文件的更新不是同步的，可能会有延时，因此一定要确保容器内的配置也已经更新为最新版本后再重新加载应用。

如果是以文件创建的, 使用:

```bash
kubectl replace -f k8s-configmap.yaml
```
