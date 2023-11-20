从 kubernetes 1.2 版本开始，kubernetes 提供了 Ingress 对象来实现对外暴露服务；到目前为止 kubernetes 总共有三种暴露服务的方式:

- NodePort Service
- LoadBlancer Service
- Ingress

**LoadBlancer Service** 是 kubernetes 深度结合云平台的一个组件；当使用 LoadBlancer Service 暴露服务时，实际上是通过向底层云平台申请创建一个负载均衡器来向外暴露服务；目前 LoadBlancer Service 支持的云平台已经相对完善，比如国外的 GCE、DigitalOcean，国内的 阿里云，私有云 Openstack 等等，由于 LoadBlancer Service 深度结合了云平台，所以只能在一些云平台上来使用。

**访问权** (ing, ingresses) 就是 k8s 中用作反向代理和负载均衡的工具, 避免使用 service 的 NodePort 暴露宿主机过多端口而造成管理混乱的情况。

Ingress 是 1.2 后才出现的，通过 Ingress 用户可以实现使用 nginx 等开源的反向代理负载均衡器实现对外暴露服务，以下详细说一下 Ingress，毕竟 traefik 用的就是 Ingress。

在 service 之前加了一层 ingress, 外部通过路由规则(域名)进行不同服务的访问, 结构如下

```
            ingress      -> service      -> label selector -> pods
            www.app1.com -> app1-service -> app1 selector -> app1 1234
80/443  ->  www.app2.com -> app2-service -> app2 selector -> app2 3456
            www.app3.com -> app3-service -> app3 selector -> app3 4567
```

- **模式的优点** 增加了 7 层的识别能力，可以根据 http header, path 进行路由转发
- **模式缺点** 复杂度提升
<a name="98db4afc"></a>
## Ingress 实现

Ingress 的实现分为两个部分 Ingress Controller 和 Ingress

**使用 Ingress 时一般会有三个组件**

- **反向代理负载均衡器**
- **Ingress Controller** 是流量的入口，是一个实体软件， 一般是 Nginx 和 Haproxy、traefik
- **Ingress** 描述具体的路由规则

Ingress Controller 会监听 api server 上的 /ingresses 资源 并实时生效。

Ingerss 描述了一个或者多个 域名的路由规则，以 ingress 资源的形式存在。

简单说： Ingress 描述路由规则， Ingress Controller 实时实现规则。

**设计理念**

k8s 有一个贯穿始终的设计理念，即需求和供给的分离。 Ingress Controller 和 Ingress 的实现也很好的实践了这一点。 要理解 k8s ，时刻记住 需求供给分离的设计理念。

<a name="b288acce"></a>
## 反向代理负载均衡器

反向代理负载均衡器很简单，说白了就是 nginx、apache 什么的；在集群中反向代理负载均衡器可以自由部署，可以使用 Replication Controller、Deployment、DaemonSet 等等，不过个人喜欢以 DaemonSet 的方式部署，感觉比较方便。

<a name="a5765900"></a>
## Ingress Controller

Ingress Controller 实质上可以理解为是个监视器，Ingress Controller 通过不断地跟 kubernetes API 打交道，实时的感知后端 service、pod 等变化，比如新增和减少 pod，service 增加与减少等；当得到这些变化信息后，Ingress Controller 再结合下文的 Ingress 生成配置，然后更新反向代理负载均衡器，并刷新其配置，达到服务发现的作用。

**Ingress Controller 注意事项**

1. 一个集群中可以有多个 Ingress Controller， 在 Ingress 中可以指定使用哪一个 Ingress Controller
2. 多个 Ingress 规则可能出现竞争
3. Ingress Controller 本身需要以 hostport 或者 service 形式暴露出来。 云端可以使用云供应商 lb 服务。
4. Ingress 可以为多个命名空间服务

**Ingress Controller 做哪些设置**

我们以 nginx-ingress 为例. 我们可以设置如下几个全局参数

1. 全局 timeout 时间
2. 全局 gzip 压缩
3. https 和 http2
4. 全局 请求数量的 limit
5. vts 实时 nginx 状态，可以监控流量

**如何设置 Ingress Controller**

两种方式 configmap 和 custom template。

custom template 用来设置 configmap 不能设置的一些高级选项， 通常情况下，使用 configmap 已经够用。

使用 configmap 需要确保 Ingress Controller 时，启用了 configmap 参数

**Ingress Controller 总结**

1. Ingress Controller 负责实现路由需求， Ingress 负责描述路由需求
2. Ingress Controller 一个集群可以有多个
3. Ingress Controller 通过 Configmap 设置， Ingress 通过 Annotations 设置
4. Ingress Controller 设置全局规则， Ingress 设置局部规则
5. Ingress Controller 可为多个命名空间服务。
6. 需求供给分离可以做到权限隔离，又能提供配置能力。

<a name="Ingress"></a>
## Ingress

Ingress 简单理解就是个规则定义；比如说某个域名对应某个 service，即当某个域名的请求进来时转发给某个 service;这个规则将与 Ingress Controller 结合，然后 Ingress Controller 将其动态写入到负载均衡器配置中，从而实现整体的服务发现和负载均衡。

**Ingress 可以做哪些设置**

我们以 nginx-ingress 为例. 我们可以设置如下几参数

1. 基于 http-header 的路由
2. 基于 path 的路由
3. 单个 ingress 的 timeout (不影响其他 ingress 的 timeout 时间设置)
4. 登录验证
5. cros
6. 请求速率 limit
7. rewrite 规则
8. ssl

**如何设置 Ingress**

Ingress 只能通过 Annotations 进行设置。并且需要确保　 Ingress Controller 启动时， 启用了 Annotations 选项

**需求和供给分离的优点**

1. Ingress Controller 放在独立命名空间中， 由管理员来管理。
2. Ingress 放在各应用的命名空间中， 由应用运维来设置。

如此可以实现权限的隔离， 又可以提供配置能力。

<a name="8af8bc52"></a>
## Ingress 相关命令

获取 Ingress

```bash
kubectl get ing --all-namespace # 获取所有命名空间的Ingress
kubectl get ingress -n test # 获取test命名空间的Ingress
```


<a name="3yqDh"></a>
## 参考资料

- [K8s 工程师必懂的 10 种 Ingress 控制器](https://www.kubernetes.org.cn/5948.html)
