**本地存储 (HostDir)**，在宿主机上指定一个目录，挂载到 Pod 的容器中，当 pod 删除时，本地仍然保留文件。可以方便地进行数据备份。

**使用场景：**<br />**

- 当运行的容器需要访问Docker内部结构时，如使用hostPath映射/var/lib/docker到容器。
- 当在容器中运行cAdvisor时，可以使用hostPath映射/dev/cgroups到容器中。

**注意事项：**<br />**

- 配置相同的pod（如通过podTemplate创建），可能在不同的Node上表现不同，因为不同节点上映射的文件内容不同。
- 当Kubernetes增加了资源敏感的调度程序，hostPath使用的资源不会被计算在内。
- 宿主机下创建的目录只有root有写权限。你需要让你的程序运行在privileged container上，或者修改宿主机上的文件权限。

使用nginx的示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: nginx
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
        path: /data
        type: Directory
```

以上配置，将Pod中的 `/usr/share/nginx/html` 卷挂载到了宿主机中的 `/data` 目录。需要注意的是，此种方式只在pod所处node中生效。

<a name="3IIzX"></a>
## hostpath的 type 属性

hostpath支持的 `type` 值如下：

| DirectoryOrCreate | 如果在给定路径上什么都不存在，那么将根据需要创建空目录，权限设置为 0755，具有与 Kubelet 相同的组和所有权。 |
| --- | --- |
| Directory | 在给定路径上必须存在的目录。 |
| FileOrCreate | 如果在给定路径上什么都不存在，那么将在那里根据需要创建空文件，权限设置为 0644，具有与 Kubelet 相同的组和所有权。 |
| File | 在给定路径上必须存在的文件。 |
| Socket | 在给定路径上必须存在的 UNIX 套接字。 |
| CharDevice | 在给定路径上必须存在的字符设备。 |
| BlockDevice | 在给定路径上必须存在的块设备。 |


<a name="GFScV"></a>
## emptyDir和hostPath在功能上的异同分析

- 二者都是node节点的本地存储卷方式；
- emptyDir可以选择把数据存到tmpfs类型的本地文件系统中去，hostPath并不支持这一点；
- hostPath除了支持挂载目录外，还支持File、Socket、CharDevice和BlockDevice，既支持把已有的文件和目录挂载到容器中，也提供了“如果文件或目录不存在，就创建一个”的功能；
- emptyDir是临时存储空间，完全不提供持久化支持；
- hostPath的卷数据是持久化在node节点的文件系统中的，即便pod已经被删除了，volume卷中的数据还会留存在node节点上。

