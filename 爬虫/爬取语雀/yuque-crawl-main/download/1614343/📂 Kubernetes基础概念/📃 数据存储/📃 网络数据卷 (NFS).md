**NFS（Network File System）即网络文件系统**，是FreeBSD支持的文件系统中的一种，它允许网络中的计算机之间共享资源。在NFS的应用中，本地NFS的客户端应用可以透明地读写位于远端NFS服务器上的文件，就像访问本地文件一样。

<a name="SfA1r"></a>
## 一、安装NFS

安装相关依赖：

```bash
yum install -y rpc-bind rpcbind nfs-utils
```

启动服务：

```bash
systemctl start rpcbind
systemctl enable rpcbind

systemctl start nfs-server
systemctl enable nfs-server
```

创建共享目录：

```bash
mkdir -p /nfs/es
cd /nfs/es
mkdir es{0..2}
```

编辑共享目录配置文件：

```bash
$ vim /etc/exports
/nfs/es 192.168.1.0/24(rw)
$ systemctl reload nfs
```

挂载与卸载测试：

```bash
$ showmount -e 192.168.1.128
Export list for 192.168.1.128:
/nfs/es 192.168.1.0/24

$ mkdir -p /mnt/nfs/es
$ mount -t nfs 192.168.1.128:/nfs/es /mnt/nfs/es
$ umount /mnt/nfs/es
```

用户与权限：

```
$ useradd -u 555 nfs
$ id nfs
uid=555(nfs) gid=1001(nfs) 组=1001(nfs)

$ chown -R nfs nfs /nfs
$ chmod a+w -R /nfs
```


<a name="2c32b15d"></a>
## 二、在Pod中使用NFS

编辑一个使用 NFS 的 Pod 的配置文件

```yaml
# nfs.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nfs-web
spec:
  containers:
    - name: web
      image: nginx
      imagePullPolicy: Never # 如果已经有镜像，就不需要再拉取镜像
      ports:
        - name: web
          containerPort: 80
          hostPort: 80 # 将容器的80端口映射到宿主机的80端口
      volumeMounts:
        - name: nfs # 指定名称必须与下面一致
          mountPath: "/usr/share/nginx/html" # 容器内的挂载点
  volumes:
    - name: nfs # 指定名称必须与上面一致
      nfs: # nfs存储
        server: 192.168.61.128 # nfs服务器ip或是域名
        path: "/test" # nfs服务器共享的目录
```

创建 Pod

```bash
kubectl create -f nfs.yaml
```

在节点端可以用 `mount` 命令查询挂载情况

因为我映射的是代码目录，在 /test 目录中创建 index.html 文件后，这个文件也将在容器中生效，当 Pod 删除时，文件不受影响，实现了数据持久化。

<a name="mP1HS"></a>
## 参考资料

- [NFS原理详解](https://blog.51cto.com/atong/1343950)
- [NFS服务器搭建与配置](https://blog.csdn.net/qq_38265137/article/details/83146421)
- [【实战】多台NFS客户机挂载同一台NFS服务器时，每台客户机都能对共享文件进行读写操作](https://blog.51cto.com/12058118/1862975)
