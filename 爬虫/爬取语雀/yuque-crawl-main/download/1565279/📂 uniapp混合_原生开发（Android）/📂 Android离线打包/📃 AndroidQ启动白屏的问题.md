问题描述：<br />在签名打包为apk后，安装到手机系统版本为Android 10以上的时候，能够出现启动页（splash.png），但是一段时间之后，启动页消失，随之而来的是白屏。

在Android 7-9版本的手机中测试没问题。

解决方案：<br />将`build.gradle`中的`targetSdkVersion`字段属性设置为29以下，建议设置为26。

官方文档如此说：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671085618719-b3317329-a71d-4c9a-8c14-e64621df0ded.png#averageHue=%23f9f6f5&clientId=u09876ff8-ee51-4&from=paste&height=175&id=u4c1d4063&originHeight=175&originWidth=741&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71824&status=done&style=none&taskId=u0bf24684-7667-44e3-a939-0586f6a6a7e&title=&width=741)

<a name="35808e79"></a>
## 参考资料

- [适配Android10 / Android Q（API 29）](https://ask.dcloud.net.cn/article/36199)
