```bash
git clone https://github.com/goharbor/harbor-helm.git -b 0.3.0
```

进入到 harbor-helm 目录修改

```bash
$ vim requirements.yaml
dependencies:
  - name: redis
    version: 1.1.15
    repository: https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
    #repository: https://kubernetes-charts.storage.googleapis.com
```

修改完成后执行:

```bash
$ helm dependency update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "aliyun" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 1 charts
Downloading redis from repo https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
Deleting outdated charts
```

所有节点下载相关镜像

```bash
docker pull goharbor/chartmuseum-photon:v0.7.1-v1.6.0
docker pull goharbor/harbor-adminserver:v1.6.0
docker pull goharbor/harbor-jobservice:v1.6.0
docker pull goharbor/harbor-ui:v1.6.0
docker pull goharbor/harbor-db:v1.6.0
docker pull goharbor/registry-photon:v2.6.2-v1.6.0
docker pull goharbor/chartmuseum-photon:v0.7.1-v1.6.0
docker pull goharbor/clair-photon:v2.0.5-v1.6.0
docker pull goharbor/notary-server-photon:v0.5.1-v1.6.0
docker pull goharbor/notary-signer-photon:v0.5.1-v1.6.0
docker pull bitnami/redis:4.0.8-r2
```
