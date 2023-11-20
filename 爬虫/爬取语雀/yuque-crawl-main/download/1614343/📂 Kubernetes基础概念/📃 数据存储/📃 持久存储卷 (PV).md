持久存储卷 (PV, Persistent Volume) 是集群内，由管理员提供的网络存储的一部分。就像集群中的节点一样，PV也是集群中的一种资源。它也像Volume一样，是一种volume插件，但是它的生命周期却是和使用它的Pod相互独立的。PV这个API对象，捕获了诸如NFS、ISCSI、或其他云存储系统的实现细节。

<a name="b91da886"></a>
## PV 配置文件

`persistent-volume.yaml`

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: test-pv
  labels:
    type: nfs #指定类型是NFS
spec:
  capacity: #指定访问空间是15G
    storage: 15Gi
  accessModes: #指定访问模式是能在多节点上挂载，并且访问权限是读写执行
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Recycle #指定回收模式是自动回收，当空间被释放时，K8S自动清理，然后可以继续绑定使用
  storageClassName: slow
  nfs:
    server: 172.18.50.200
    path: /test
```

<a name="e64141fa"></a>
## 创建 PV

```bash
kubectl create -f persistent-volume.yaml
```

<a name="00c29bbc"></a>
## 获取 pv 信息

pv 没有命名空间的限制

```bash
$ kubectl get pv
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM           STORAGECLASS   REASON   AGE
test-pv   15Gi       RWX            Recycle          Bound    test/nfs-data                           51s
```

查看 pv 详情

```bash
$ kubectl describe pv test-pv
Name:            test-pv
Labels:          type=nfs
Annotations:     pv.kubernetes.io/bound-by-controller: yes
Finalizers:      [kubernetes.io/pv-protection]
StorageClass:
Status:          Bound
Claim:           test/nfs-data
Reclaim Policy:  Recycle
Access Modes:    RWX
VolumeMode:      Filesystem
Capacity:        15Gi
Node Affinity:   <none>
Message:
Source:
    Type:      NFS (an NFS mount that lasts the lifetime of a pod)
    Server:    192.168.126.130
    Path:      /test
    ReadOnly:  false
Events:        <none>
```

可以看到, test-pv 被 PVC `test/nfs-data` 声明, 挂载到 `192.168.126.130/test` 下

<a name="e4fe520c"></a>
## 映射选项

当PV被映射到一个node上时，Kubernetes管理员可以指定额外的映射选项。可以通过使用标注`volume.beta.kubernetes.io/mount-options`来指定PV的映射选项。

比如：

```yaml
apiVersion: "v1"
kind: "PersistentVolume"
metadata:
  name: gce-disk-1
  annotations:
    volume.beta.kubernetes.io/mount-options: "discard"
spec:
  capacity:
    storage: "10Gi"
  accessModes:
    - "ReadWriteOnce"
  gcePersistentDisk:
    fsType: "ext4"
    pdName: "gce-disk-1
```

映射选项是当映射PV到磁盘时，一个可以被递增地添加和使用的字符串。

注意，并非所有的PV类型都支持映射选项。在Kubernetes v1.6中，以下的PV类型支持映射选项。

- GCEPersistentDisk
- AWSElasticBlockStore
- AzureFile
- AzureDisk
- NFS
- iSCSI
- RBD (Ceph Block Device)
- CephFS
- Cinder (OpenStack block storage)
- Glusterfs
- VsphereVolume
- Quobyte Volumes
- VMware Photon
