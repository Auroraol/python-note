将卷指定为 **空目录(emptyDir)** ，将会为Pod分配临时存储目录，会随着Pod删除而删除。无法持久化。

**应用场景：**

- 临时空间，例如基于磁盘的合并排序
- 设置检查点以从崩溃事件中恢复未执行完毕的长计算
- 保存内容管理器容器从Web服务器容器提供数据时所获取的文件

默认情况下，emptyDir可以使用任何类型的由node节点提供的后端存储。如果你有特殊的场景，需要使用tmpfs作为emptyDir的可用存储资源也是可以的，只需要在创建emptyDir卷时增加一个emptyDir.medium字段的定义，并赋值为"Memory"即可。

:::info
_注：在使用tmpfs文件系统作为emptyDir的存储后端时，如果遇到node节点重启，则emptyDir中的数据也会全部丢失。同时，你编写的任何文件也都将计入Container的内存使用限制。_
:::

使用redis的示例：

```yaml
# emptydir.yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    name: redis
    role: master
  name: redis-master
spec:
  containers:
    - name: master
      image: redis:latest
      env:
        - name: MASTER
          value: "true"
      ports: # 容器内端口
        - containerPort: 6379
      volumeMounts: # 容器内挂载点
        - mountPath: /data
          name: redis-data # 必须取个名字
  volumes:
    - name: redis-data # 跟上面卷的名字对应
      emptyDir: {} # 宿主机挂载点为空
```

创建 Pod：

```bash
kubectl create -f emptydir.yaml
```

此时 Emptydir 已经创建成功，在宿主机上的访问路径为 `/var/lib/kubelet/pods/<pod uid>/volumes/kubernetes.io~empty-dir/redis-data`,如果在此目录中创建删除文件，都将对容器中的`/data `目录有影响，如果删除 Pod，文件将全部删除，即使是在宿主机上创建的文件也是如此，在宿主机上删除容器则 k8s 会再自动创建一个容器，此时文件仍然存在。

