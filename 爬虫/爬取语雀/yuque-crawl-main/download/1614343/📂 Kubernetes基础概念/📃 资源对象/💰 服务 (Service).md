在 Kubernetes 的世界里，虽然每个 Pod 都会被分配一个单独的 IP 地址，但这个 IP 地址会随着 Pod 的销毁而消失，这就引出一个问题：如果有一组 Pod 组成一个集群来提供服务，那么如何来访问它呢？服务 (svc, Service)！

一个 Service 可以看作一组提供相同服务的 Pod 的对外访问接口，Service 作用于哪些 Pod 是通过 Label Selector 来定义的。

- 拥有一个指定的名字（比如 my-mysql-server）；
- 拥有一个虚拟 IP（ClusterIP、ServiceIP 或 VIP）和端口号，销毁之前不会改变，只能内网访问；
- 能够提供某种远程服务能力；
- 被映射到了提供这种服务能力的一组容器应用上；

如果 Service 要提供外网服务，需指定公共 IP 和 NodePort，或外部负载均衡器；
<a name="842d0a87"></a>
## 服务中的 3 种端口

- **port** 这里的 port 表示：service 暴露在 cluster ip 上的端口，`<cluster ip>:port` 是提供给集群内部客户访问 service 的入口。
- **nodePort** nodePort 是 kubernetes 提供给集群外部客户访问 service 入口的一种方式（另一种方式是 LoadBalancer），所以，`<nodeIP>:nodePort` 是提供给集群外部客户访问 service 的入口。
- **targetPort** targetPort 很好理解，targetPort 是 pod 上的端口，从 port 和 nodePort 上到来的数据最终经过 kube-proxy 流入到后端 pod 的 targetPort 上进入容器。

<a name="e0b6a599"></a>
## NodePort Service

NodePort Service 顾名思义，实质上就是通过在集群的每个 node 上暴露一个端口，然后将这个端口映射到某个具体的 service 来实现的，虽然每个 node 的端口有很多(0~65535)，但是由于安全性和易用性(服务多了就乱了，还有端口冲突问题)实际使用可能并不多。

service 是 k8s 暴露 http 服务的默认方式， 其中 NodePort 类型可以将 http 服务暴露在宿主机的端口上，以便外部可以访问。 service 模式的结构如下.

```
service -> label selector -> pods
31217 ->   app1 selector  -> app1 1234
31218 ->   app2 selector  -> app2 3456
31218 ->   app2 selector  -> app2 4567
```

**模式的优点**: 结构简单，容易理解。

**模式缺点**

1. 一个 app 需要占用一个主机端口
2. 端口缺乏管理
3. L4 转发， 无法根据 http header 和 path 进行路由转发

<a name="0da0237f"></a>
## 定义 Service

一个 `Service` 在 Kubernetes 中是一个 REST 对象，和 `Pod` 类似。 像所有的 REST 对象一样， `Service` 定义可以基于 POST 方式，请求 apiserver 创建新的实例。 例如，假定有一组 `Pod`，它们对外暴露了 9376 端口，同时还被打上 `"app=MyApp"` 标签。

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

上述配置将创建一个名称为 “my-service” 的 `Service` 对象，它会将请求代理到使用 TCP 端口 9376，并且具有标签 `"app=MyApp"` 的 `Pod` 上。 这个 `Service` 将被指派一个 IP 地址（通常称为 “Cluster IP”），它会被服务的代理使用（见下面）。 该 `Service` 的 selector 将会持续评估，处理结果将被 POST 到一个名称为 “my-service” 的 `Endpoints` 对象上。

需要注意的是， `Service` 能够将一个接收端口映射到任意的 `targetPort`。 默认情况下，`targetPort` 将被设置为与 `port` 字段相同的值。 可能更有趣的是，`targetPort` 可以是一个字符串，引用了 backend `Pod` 的一个端口的名称。 但是，实际指派给该端口名称的端口号，在每个 backend `Pod` 中可能并不相同。 对于部署和设计 `Service` ，这种方式会提供更大的灵活性。 例如，可以在 backend 软件下一个版本中，修改 Pod 暴露的端口，并不会中断客户端的调用。

Kubernetes `Service` 能够支持 `TCP` 和 `UDP` 协议，默认 `TCP` 协议。
