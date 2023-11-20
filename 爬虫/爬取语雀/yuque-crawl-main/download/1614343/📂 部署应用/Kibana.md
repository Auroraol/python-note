```bash
git clone https://github.com/dotbalo/k8s.git dotbalo-k8s
cd /opt/k8s/dotbalo-k8s/k8s-efk
kubectl apply -f .
```

```bash
$ vim kibana-logging-ingress.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: kibana
  namespace: logging
  annotations:
    kubernetes.io/ingress.class: traefik
spec:
  rules:
  - host: kibana.k8s.net
    http:
      paths:
      - backend:
          serviceName: kibana-logging
          servicePort: 5601

$ kubectl create -f kibana-logging-ingress.yaml -n logging
ingress.extensions/kibana created
```
