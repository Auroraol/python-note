<a name="46149248"></a>
## 第三方支付
在使用第三方支付之前，需要先配置`manifest.json`：
```json
{
    "app-plus" : {
        "distribute" : {
            "sdkConfigs" : {
                "payment" : {
                    "alipay" : {},
                    "weixin" : {
                        "appid" : "your appid",
                        "UniversalLinks" : ""
                    }
                }
            }
        }
    }
}
```

或者直接在HBuilder中可视化配置：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086155963-b36708ae-30e6-4634-b6a6-fad493e0a6c7.png#averageHue=%23fbf5e4&clientId=ud1939f76-ae5c-4&from=paste&height=349&id=u691ea161&originHeight=349&originWidth=611&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26449&status=done&style=none&taskId=u7f76b784-5746-4935-80f8-db53a5f3bd6&title=&width=611)

一个uni-app的支付示例如下：
```vue
<template>
	<view>
		<button @click="requestPayment('alipay')">支付宝支付</button>
		<button @click="requestPayment('wxpay')">微信支付</button>
	</view>
</template>

<script>
export default {
  methods: {
    requestPayment(provider) {
      uni.getProvider({
        service: 'payment',
        success: function (res) {
          console.log(res);
          if (~res.provider.indexOf(provider)) {
            uni.requestPayment({
              provider: provider,
              orderInfo: 'orderInfo', //微信、支付宝订单数据
              success: function (res) {
                console.log('success:' + JSON.stringify(res));
              },
              fail: function (err) {
                console.log('fail:' + JSON.stringify(err));
              }
            });
          }
        }
      });
    }
  }
}
</script>
```

通过`uni.requestPayment`唤起支付，需要在唤起支付前获取相应的支付参数（orderInfo），以及配置provider，需要先通过`uni.getProvider`检测是否支持对应的支付方式。

微信支付参数（orderInfo）如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086175853-382753e2-ec67-44ab-9492-4009945f83f6.png#averageHue=%23fbf9f9&clientId=ud1939f76-ae5c-4&from=paste&height=254&id=ueed43a01&originHeight=254&originWidth=565&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29880&status=done&style=none&taskId=ud10b0837-ee1b-4dbe-bc32-d7e4caf8a3a&title=&width=565)

支付宝支付参数（orderInfo）如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086228958-0c4d6912-3619-4a5d-bfa5-80b0c1a2dcf5.png#averageHue=%23f9f5f5&clientId=ud1939f76-ae5c-4&from=paste&height=109&id=uc86c6eda&originHeight=109&originWidth=736&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50472&status=done&style=none&taskId=u240f610a-f2c2-42a9-9893-449666b2341&title=&width=736)

其中provider取值如下：

- **alipay** 支付宝支付
- **wxpay** 微信支付
- **baidu** 百度收银台
- **appleiap** 苹果应用内支付

<a name="0f004c4c"></a>
## 第三方登录
一个uni-app的第三方登录示例如下：
```vue
<template>
	<view>
		<button @click="oauth('qq')">QQ登录</button>
		<button @click="oauth('weixin')">微信登录</button>
		<button @click="oauth('sinaweibo')">微博登录</button>
	</view>
</template>

<script>
export default {
  methods: {
    oauth(provider) {
      uni.getProvider({
        service: 'oauth',
        success: function (res) {
          console.log(res);
          if (~res.provider.indexOf(provider)) {
            uni.login({
              provider: provider,
              success: function (loginRes) {
                console.log(JSON.stringify(loginRes));
              }
            });
          }
        }
      });
    }
  }
}
</script>
```

同样地，在调取登录之前，需要先通过`uni.getProvider`检测是否拥有对应的登录方式。

其中provider取值如下：

- **weixin** 微信登录
- **qq** QQ登录
- **sinaweibo** 新浪微博登录
- **xiaomi** 小米登录
- **apple** Apple登录

<a name="ac8d6dc8"></a>
## 原生Android工程的配置

如果是离线打包，需要进行如下配置
<a name="e3b2064e"></a>
### 支付宝支付

1. 需要引入工程的jar/aar文件

需要将以下jar/aar文件（[下载地址点这里](https://nativesupport.dcloud.net.cn/AppDocs/download/android)）放到工程的libs目录下

| 路径 | 文件 |
| --- | --- |
| SDK\\libs | payment-alipay-release.aar, alipayutdid.jar, alipaySdk-15.6.5-20190718211159-noUtdid.aarr |


2. 在`AndroidManifest.xml`中配置

application节点前：
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

3. 在`dcloud_properties.xml`中添加：
```xml
<feature name="Payment" value="io.dcloud.feature.payment.PaymentFeatureImpl">
    <module name="AliPay" value="io.dcloud.feature.payment.alipay.AliPay"/>
</feature>
```

<a name="bffe28c8"></a>
### 微信支付

1. 申请appkey，详情查看[微信appkey申请方法](http://ask.dcloud.net.cn/article/208)
2. 需要引入工程的jar/aar文件

需要将以下jar/aar文件（[下载地址点这里](https://nativesupport.dcloud.net.cn/AppDocs/download/android)）放到工程的libs目录下

| 路径 | 文件 |
| --- | --- |
| SDK\\libs | payment-weixin-release.aar, wechat-sdk-android-with-mta-5.1.4.jar |


3. 将`WXPayEntryActivity.java`添加到`$你的包名.wxapi`下，内容如下（注意将包名改为自己的）：
```java
package com.xiaoyulive.test.wxapi;

import io.dcloud.feature.payment.weixin.AbsWXPayCallbackActivity;

public class WXPayEntryActivity extends AbsWXPayCallbackActivity{
}
```

4. 在`AndroidManifest.xml`中配置

application节点前：
```xml
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
```

application节点下：
```xml
<meta-data android:name="WX_APPID" android:value="$微信APPID" />
<meta-data android:name="WX_SECRET" android:value="$微信SECRET"/>
<activity
    android:name="$你的包名.wxapi.WXPayEntryActivity"
    android:exported="true"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:launchMode="singleTop" />
```

5. 在`dcloud_properties.xml`中添加：
```xml
<feature name="Payment" value="io.dcloud.feature.payment.PaymentFeatureImpl">
    <module name="Payment-Weixin" value="io.dcloud.feature.payment.weixin.WeiXinPay"/>
</feature>
```

<a name="35808e79"></a>
## 参考资料

- [获取服务提供商 uni.getProvider(OBJECT)](https://uniapp.dcloud.io/api/plugins/provider)
- [支付 uni.requestPayment(OBJECT)](https://uniapp.dcloud.io/api/plugins/payment)
- [登录 uni.login(OBJECT)](https://uniapp.dcloud.io/api/plugins/login?id=login)
- [uniapp离线打包之支付模块的配置](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/pay)
