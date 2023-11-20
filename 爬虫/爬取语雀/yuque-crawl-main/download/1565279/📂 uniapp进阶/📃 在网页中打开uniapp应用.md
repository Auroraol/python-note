<a name="HOYxY"></a>
## Android 原生工程配置

在`AndroidManifest.xml`入口的Activity中加入以下`intent-filter`：

```xml
<!-- 应用入口 -->
<activity
    android:name="io.dcloud.PandoraEntry"
    android:theme="@style/TranslucentTheme"
    android:screenOrientation="portrait"
    android:configChanges="orientation|keyboardHidden|screenSize|mcc|mnc|fontScale"
    android:hardwareAccelerated="true"
    android:windowSoftInputMode="adjustResize">

    ......

    <intent-filter>
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:scheme="test" android:host="abc.com" android:path="/entry"/>
    </intent-filter>
</activity>
```

其中，scheme就相当于协议，host就相当于域名，path就相当于路径，以上配置完整的URI为：

```
test://abc.com/entry
```

<a name="f3a9be40"></a>
## 在网页中跳转到APP

直接上代码：

```html
<!doctype html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black"/>

  <title>唤醒APP</title>
  <meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,minimal-ui">
</head>
  <body>
    <div>
      <a id="J-call-app" href="javascript:;" class="label">立即打开&gt;&gt;</a>
      <input id="J-download-app" type="hidden" name="storeurl" value="https://file.lizhiboxue.com/shianonline/apk/sa-learn.apk">
    </div>

    <script>
      (function(){
        /*获取UA标识，并转为小写*/
        let ua = navigator.userAgent.toLowerCase();
        let config = {
          /*scheme:必须*/
          scheme_IOS: 'test://abc.com/entry',
          scheme_Adr: 'test://abc.com/entry',
          download_url: document.getElementById('J-download-app').value,
          timeout: 600
        };

        function openclient() {
          let startTime = Date.now();

          let ifr = document.createElement('iframe');

          /*通过UA标识，判断是否是苹果系统*/
          ifr.src = ua.indexOf('os') > 0 ? config.scheme_IOS : config.scheme_Adr;
          ifr.style.display = 'none';
          document.body.appendChild(ifr);

          let t = setTimeout(function() {
            let endTime = Date.now();
            if (!startTime || endTime - startTime < config.timeout + 200) {
              window.location = config.download_url;
            }
          }, config.timeout);

          window.onblur = function() {
            clearTimeout(t);
          }
        }
        window.addEventListener("DOMContentLoaded", function(){
          document.getElementById("J-call-app").addEventListener('click',openclient,false);
        }, false);
      })()
    </script>
  </body>
</html>
```

以上，先判断平台类型（iOS、Android），如果应用存在，打开应用，若不存在，通过URL下载应用。

<a name="fc72a3c5"></a>
## 跳转到APP并传参

TODO...

<a name="5e845e98"></a>
## 跳转到指定的uniapp页面

TODO...

<a name="35808e79"></a>
## 参考资料

- [安卓：从网页唤醒APP](https://www.jianshu.com/p/2eb757c9c90c)
- [JS唤醒Android APP(包括在外部浏览器和WebView)](https://www.jianshu.com/p/fd040859dab5)
- [iOS平台设置UrlSchemes，实现被第三方应用调用](https://ask.dcloud.net.cn/article/64)
- [android中的scheme](https://www.jianshu.com/p/8e13860cb6da)
- [H5网页唤醒App有哪些做法](https://cloud.tencent.com/developer/article/1515181)
