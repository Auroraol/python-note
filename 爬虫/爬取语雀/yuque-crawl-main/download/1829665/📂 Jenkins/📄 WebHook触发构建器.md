<a name="csDJg"></a>
## 在Jenkins中配置构建触发器
在“配置 -> 构建触发器”中配置：<br />![Snipaste_2022-11-12_21-52-28.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668261225659-020a3f34-b48a-412b-a977-88c7a3616b65.png#averageHue=%23f6f6f5&clientId=uc6fa9fa9-8f5a-4&from=drop&id=u0dd53ba7&originHeight=549&originWidth=1338&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19429&status=done&style=none&taskId=u5d231e99-7209-48ac-b9b5-66d8f6454f6&title=)

测试：浏览器访问 [http://192.168.31.170:30080/job/vite-vue3-free-style/build?token=123456](http://192.168.31.170:30080/job/vite-vue3-free-style/build?token=123456) 可触发构建。

格式为：
```bash
${JENKINS_URL}/job/vite-vue3-free-style/build?token=${TOKEN_NAME} 
```


---

参考：

- [Jenkins 进阶02 Generic Webhook 实践_富士康质检员张全蛋的博客-CSDN博客_jenkins generic webhook](https://blog.csdn.net/qq_34556414/article/details/119765166)

<a name="Zy7nY"></a>
## 报错信息：403 Authentication required
在Gitea的WebHook中报错：<br />![Snipaste_2022-11-14_23-34-00.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440099617-aa94cab4-c92e-47d2-bb8e-6df66cbf4f59.png#averageHue=%23f3f3f2&clientId=ucaf5b252-452b-4&from=drop&id=u9d447e8d&originHeight=650&originWidth=1153&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16138&status=done&style=none&taskId=ue8da1b97-4826-47ca-b94a-bc3a7ca3515&title=)

错误原因：Jenkins不允许未登录用户访问。

解决方案：<br />在 `系统管理 -> 安全 -> 全局安全配置`中勾选“**匿名用户具有可读权限**”<br />![Snipaste_2022-11-14_23-37-02.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440260863-652b1d4a-5aeb-4729-ad3a-55097d10dca2.png#averageHue=%23fdfdfd&clientId=ucaf5b252-452b-4&from=drop&id=ua766aa20&originHeight=518&originWidth=1357&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7207&status=done&style=none&taskId=u647005a2-31d3-4d82-807d-dc6227ab8ff&title=)


