如果是H5，通过uniapp的web-view可以直接嵌入PDF进行预览（一般浏览器都支持，这是浏览器的原生功能）；但是编译到APP，iOS倒是可以（因为iOS使用的是内嵌的Safari，支持PDF预览）；Android不行，Android使用的是内嵌的web-view，不支持PDF预览，有些手机会打开浏览器进行下载。

Android手机通过web-view嵌入PDF预览时报错：<br />![GYVRJH`}~6~]MJDGTX2W(X8.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/2213540/1671071075694-15959691-03fd-419c-9284-0cc11fba669f.jpeg#averageHue=%23747474&clientId=u87e5157f-80ce-4&from=drop&height=701&id=u66ffbd76&originHeight=2280&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=78134&status=done&style=none&taskId=u776a680c-a12b-44bc-9fa9-7947791c715&title=&width=332)

解决方案：通过[pdf.js](https://mozilla.github.io/pdf.js/)实现APP中PDF的预览（Android和iOS均测试通过）

首先下载older browsers版本（因为不能保证Android内嵌web-view支持最新的js语法）<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671071257088-54d6af13-1e78-4ba4-9663-9fc52e3e4354.png#averageHue=%23faf9f8&clientId=u87e5157f-80ce-4&from=paste&height=219&id=u3777ed16&originHeight=219&originWidth=1184&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28110&status=done&style=none&taskId=u988bc5c8-0d91-447f-b470-5c8aa0d41e1&title=&width=1184)

以下为下载好的pdfjs 3.1.81版本：

- [pdfjs-3.1.81-legacy-dist.zip](https://www.yuque.com/attachments/yuque/0/2022/zip/2213540/1671071334878-7f8f7337-33bb-4550-aacf-079a057b81b5.zip?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fzip%2F2213540%2F1671071334878-7f8f7337-33bb-4550-aacf-079a057b81b5.zip%22%2C%22name%22%3A%22pdfjs-3.1.81-legacy-dist.zip%22%2C%22size%22%3A5943793%2C%22type%22%3A%22application%2Fx-zip-compressed%22%2C%22ext%22%3A%22zip%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u7725de20-e2f3-4b33-9371-57f2a3c6400%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u5212e8c8%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D) （older browsers）
- [pdfjs-3.1.81-dist.zip](https://www.yuque.com/attachments/yuque/0/2022/zip/2213540/1671071334520-d6aef57e-df1e-4011-9d85-5eaf95b9eb0d.zip?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fzip%2F2213540%2F1671071334520-d6aef57e-df1e-4011-9d85-5eaf95b9eb0d.zip%22%2C%22name%22%3A%22pdfjs-3.1.81-dist.zip%22%2C%22size%22%3A5726937%2C%22type%22%3A%22application%2Fx-zip-compressed%22%2C%22ext%22%3A%22zip%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u70a8a420-0a68-4cfe-a2be-941ec62665d%22%2C%22taskType%22%3A%22upload%22%2C%22__spacing%22%3A%22both%22%2C%22id%22%3A%22u0923d138%22%2C%22margin%22%3A%7B%22top%22%3Atrue%2C%22bottom%22%3Atrue%7D%2C%22card%22%3A%22file%22%7D)（modern browsers）

将其解压后，上传到OSS：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671071451662-cc1ab1b3-312a-4626-87ae-6411eea6689f.png#averageHue=%23edecec&clientId=u87e5157f-80ce-4&from=paste&height=661&id=u685d829d&originHeight=661&originWidth=1205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38894&status=done&style=none&taskId=u66c97f32-71c5-4937-a3f3-dc353c5dea1&title=&width=1205)

上传完成后，通过浏览器测试是否正常。<br />浏览器访问路径：
```json
https://你的域名/pdfjs存放到OSS的路径/web/viewer.html?file=https://你的域名/backend/xxx.pdf
```
比如我上传到OSS的路径为
```json
https://你的域名/frontend/pdfjs-3.1.81-legacy-dist/web/viewer.html?file=https://你的域名/backend/xxx.pdf
```
其中`xxx.pdf`就是要预览的PDF路径：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671071563654-ef1c0ba1-4fda-4f97-af19-f017e7bfa049.png#averageHue=%23a9c37e&clientId=u87e5157f-80ce-4&from=paste&height=1032&id=ub762568c&originHeight=1032&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=313749&status=done&style=none&taskId=ud55b6c39-4660-4ffc-af51-32adf2bc281&title=&width=1920)

在uniapp中，通过web-view嵌入此链接即可：
```json
Layout
  web-view(src="https://你的域名/frontend/pdfjs-3.1.81-legacy-dist/web/viewer.html?file=https://你的域名/backend/xxx.pdf")
```

在Android中的预览效果：<br />![Screenshot_2022-12-15-10-37-20-662_com.greenrecyc.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/2213540/1671071859057-a7845e4e-c35e-408d-aeac-2d4549159362.jpeg#averageHue=%23f6f6f6&clientId=u87e5157f-80ce-4&from=drop&height=1138&id=u84547609&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=618602&status=done&style=none&taskId=uc03fc47f-6aae-473a-9b6d-c1b5f2a0419&title=&width=512)

如果报跨域错误，需要配置OSS（阿里云）允许跨域访问，配置如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671072029553-d63860fd-3b8c-4704-a796-ddeb9bc9be9a.png#averageHue=%23fcfcfb&clientId=uf6d9532a-960a-4&from=paste&height=531&id=u2c92a280&originHeight=531&originWidth=1672&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69107&status=done&style=none&taskId=ucf72add6-5b0f-47ac-9051-08e3956c2cf&title=&width=1672)


