守护进程集 (DS, DaemonSet) 确保全部（或者一些）Node 上运行一个 Pod 的副本。当有 Node 加入集群时，也会为他们新增一个 Pod 。当有 Node 从集群移除时，这些 Pod 也会被回收。删除 DaemonSet 将会删除它创建的所有 Pod。

使用 DaemonSet 一些典型使用场景:

- 运行集群存储 daemon，例如在每个 Node 上运行 `glusterd`、`ceph`。
- 在每个 Node 上运行日志收集 daemon，例如`fluentd`、`logstash`。
- 在每个 Node 上运行监控 daemon，例如 [Prometheus Node Exporter](https://github.com/prometheus/node_exporter)、`collectd`、Datadog 代理、New Relic 代理，或 Ganglia `gmond`。

一个简单的用法是，在所有的 Node 上都存在一个 DaemonSet，将被作为每种类型的 daemon 使用。 一个稍微复杂的用法可能是，对单独的每种类型的 daemon 使用多个 DaemonSet，但具有不同的标志，和/或对不同硬件类型具有不同的内存、CPU 要求。

<a name="c8e47354"></a>
## yaml 示例

下面的描述文件创建了一个运行着 fluentd-elasticsearch 镜像的 DaemonSet 对象：

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels: # 与spec.template.metadata.labels一致
      name: fluentd-elasticsearch
  template: # pod模板
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers: # 容器模板
        - name: fluentd-elasticsearch
          image: k8s.gcr.io/fluentd-elasticsearch:1.20
          resources:
            limits:
              memory: 200Mi
            requests:
              cpu: 100m
              memory: 200Mi
          volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: varlibdockercontainers
              mountPath: /var/lib/docker/containers
              readOnly: true
      terminationGracePeriodSeconds: 30
      volumes: # 对外暴露的卷
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```

在 Kubernetes 1.8 之后，必须指定.spec.selector 来确定这个 DaemonSet 对象管理的 Pod，通常与.spec.template.metadata.labels 中定义的 Pod 的 label 一致。

<a name="dcef7cb3"></a>
## Pod 模板

`.spec` 唯一必需的字段是 `.spec.template`。

`.spec.template` 是一个 [Pod 模板](https://kubernetes.io/docs/user-guide/replication-controller/#pod-template)。 它与 [Pod](https://kubernetes.io/docs/user-guide/pods) 具有相同的 schema，除了它是嵌套的，而且不具有 `apiVersion` 或 `kind` 字段。

Pod 除了必须字段外，在 DaemonSet 中的 Pod 模板必须指定合理的标签（查看 [pod selector](https://jimmysong.io/kubernetes-handbook/concepts/daemonset.html#pod-selector)）。

在 DaemonSet 中的 Pod 模板必需具有一个值为 `Always` 的 [`RestartPolicy`](https://kubernetes.io/docs/user-guide/pod-states)，或者未指定它的值，默认是 `Always`。

<a name="c6eb24b0"></a>
## Daemon Pods 的调度特性

默认情况下，Pod 被分配到具体哪一台 Node 上运行是由 Scheduler（负责分配调度 Pod 到集群内的 Node 上，它通过监听 ApiServer，查询还未分配 Node 的 Pod，然后根据调度策略为这些 Pod 分配 Node）决定的。但是，DaemonSet 对象创建的 Pod 却拥有一些特殊的特性：

- Node 的 [`unschedulable`](https://kubernetes.io/docs/admin/node/#manual-node-administration)属性会被 DaemonSet Controller 忽略。
- 即使 Scheduler 还未启动，DaemonSet Controller 也能够创建并运行 Pod。
