为了方便管理和集成jenkins，k8s、harbor、jenkins均使用openLDAP统一认证。

```bash
git clone https://github.com/dotbalo/k8s.git dotbalo-k8s
cd dotbalo-k8s/openldap
kubectl create ns public-service
kubectl apply -f .
```
