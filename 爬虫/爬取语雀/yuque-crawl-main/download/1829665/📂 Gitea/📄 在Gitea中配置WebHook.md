如果需要使用构建工具，比如Jenkins，可以通过WebHook触发。

在Gitea中，添加Web钩子，选择“Gitea”<br />![Snipaste_2022-11-12_21-58-36.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668261597580-f016212e-8168-4248-b48b-99f322c5f188.png#averageHue=%23fbfbfa&clientId=uc6fa9fa9-8f5a-4&from=drop&id=ub0768b36&originHeight=250&originWidth=1204&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9485&status=done&style=none&taskId=u602d1f87-4405-42f7-911d-d599f4a5fb4&title=)<br />创建Web钩子：<br />![Snipaste_2022-11-12_21-57-02.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668261463775-7fde0c6c-b98c-4d5b-b469-de13c8fee315.png#averageHue=%23fcfbfb&clientId=uc6fa9fa9-8f5a-4&from=drop&id=u674128b2&originHeight=910&originWidth=1154&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21740&status=done&style=none&taskId=u508002d0-144c-445c-bf5a-7c0c50010a5&title=)

测试：本地推送代码到Gitea测试是否成功。

<a name="pa4cl"></a>
## 报错信息：webhook can only call allowed HTTP servers
报错详情：
```groovy
Delivery: Post "http://192.168.31.170:30080/job/vite-vue3-free-style/build?token=123456": dial tcp 192.168.31.170:30080: webhook can only call allowed HTTP servers (check your webhook.ALLOWED_HOST_LIST setting), deny '192.168.31.170(192.168.31.170:30080)'
```
![Snipaste_2022-11-14_23-22-55.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668439688815-a29b07a7-102b-4bff-a43a-23a2d87d5657.png#averageHue=%23faf9f9&clientId=ucaf5b252-452b-4&from=drop&id=Dm2ti&originHeight=286&originWidth=1151&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6623&status=done&style=none&taskId=u1ef4dd07-618c-44ab-9500-f1f44a39305&title=)

错误原因：没有将Jenkins服务IP添加到白名单。

解决方案：<br />打开容器卷中的 `data/gitea/conf/app.ini`，往最后添加：
```groovy
[webhook]
ALLOWED_HOST_LIST = 192.168.0.0/16
```

然后重启容器，重新测试即可成功。<br />![Snipaste_2022-11-14_23-27-47.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668439688827-c859232d-e3d6-492e-93d4-b401bd9f6cda.png#averageHue=%23faf9f9&clientId=ucaf5b252-452b-4&from=drop&id=u58727c1b&originHeight=103&originWidth=1145&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3205&status=done&style=none&taskId=ub6e50ec6-c648-4abd-a7ab-20efee81dc8&title=)

<a name="Zy7nY"></a>
## 报错信息：403 Authentication required
可能的问题：

1. Gitea的WebHook中，HTTP方法不正确，POST、GET更改试试
2. Jenkins的权限设置问题，参考 [📄 WebHook触发构建器](https://www.yuque.com/xiaoyulive/cicd/znqg3i7cni92yfqd?view=doc_embed&inner=Zy7nY)


