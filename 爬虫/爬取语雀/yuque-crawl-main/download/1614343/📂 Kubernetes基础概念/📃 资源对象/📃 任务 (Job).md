Job 负责批处理任务，即仅执行一次的任务，它保证批处理任务的一个或多个 Pod 成功结束。

<a name="b03fabb7"></a>
## Job Spec 格式

- spec.template 格式同 Pod
- RestartPolicy 仅支持 Never 或 OnFailure
- 单个 Pod 时，默认 Pod 成功运行后 Job 即结束
- `.spec.completions`标志 Job 结束需要成功运行的 Pod 个数，默认为 1
- `.spec.parallelism`标志并行运行的 Pod 的个数，默认为 1
- `.spec.activeDeadlineSeconds`标志失败 Pod 的重试最大时间，超过这个时间不会继续重试

一个简单的例子：

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
  namespace: test
spec:
  template:
    metadata:
      name: pi
    spec:
      containers:
        - name: pi
          image: perl
          command: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
```

测试

```bash
$ kubectl create -f ./job.yaml
job "pi" created
$ pods=$(kubectl get pods --selector=job-name=pi --output=jsonpath={.items..metadata.name} -n test)
$ kubectl logs $pods -n test
3.141592653589793238462643383279502...
```

任务运行完后, 任务和 pod 呈现 Completed 状态

```bash
kubectl get po -n test
NAME                     READY   STATUS      RESTARTS   AGE
pi-7wbk4                 0/1     Completed   0          3m28s
```

<a name="a0fba4e2"></a>
## Bare Pods

所谓 Bare Pods 是指直接用 PodSpec 来创建的 Pod（即不在 ReplicaSets 或者 ReplicationController 的管理之下的 Pods）。这些 Pod 在 Node 重启后不会自动重启，但 Job 则会创建新的 Pod 继续任务。所以，推荐使用 Job 来替代 Bare Pods，即便是应用只需要一个 Pod。
