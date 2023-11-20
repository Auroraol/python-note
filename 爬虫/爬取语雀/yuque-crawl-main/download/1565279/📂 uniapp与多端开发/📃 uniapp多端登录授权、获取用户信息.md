<a name="NdmuZ"></a>
## 概述


<a name="CuIFk"></a>
## uniapp授权登录



<a name="GkbmA"></a>
## 微信小程序授权登录


参考：


<a name="GqPmS"></a>
## 支付宝小程序授权登录
<a name="To2aN"></a>
### 获取手机号
<a name="lo5jJ"></a>
#### 准备工作：配置获取手机号权限
获取手机号，需要先到支付宝小程序后台开通获取手机号的功能。<br />![Snipaste_2021-10-14_10-29-58.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1634178629516-b7642fbb-c294-472f-a5d1-d53d1178f4c0.png#clientId=u6063a06d-e211-4&from=drop&id=u1dc2701c&originHeight=813&originWidth=1626&originalType=binary&ratio=1&size=43487&status=done&style=none&taskId=ua1b59437-ac44-4d58-ab1f-ec1cd333e50)

<a name="ZqHix"></a>
#### 小程序端获取加密串
小程序端获取加密串具体流程如下。<br />将button的`open-type`设置为`getAuthorize`；scope设置为`phoneNumber`，然后绑定`onGetAuthorize`事件：
```html
<button
	open-type="getAuthorize"
  scope='phoneNumber'
  onGetAuthorize="onGetAuthorize"
  onError="onAuthError"
>授权手机号</button>
```
在`onGetAuthorize`方法中调用`my.getPhoneNumber`方法获取手机号加密数据：
```javascript
onGetAuthorize() {
  my.getPhoneNumber({
    success: (res) => {
      let encryptedData = res.response;
      console.log(encryptedData);
      // TODO: 请求后端接口获取解密数据
    },
    fail: (res) => {
      console.log('getPhoneNumber_fail');
      console.log(res);
    },
  });
},
onAuthError(e) {
  console.log(JSON.stringify(e.detail, '', 2));
},
```
点击后，触发获取手机号授权弹窗： <br />![Snipaste_2021-10-14_10-42-58.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1634179395115-02277140-b7ed-40a0-a180-f8298504d19d.png#clientId=u6063a06d-e211-4&from=drop&id=di94I&originHeight=682&originWidth=379&originalType=binary&ratio=1&size=6321&status=done&style=none&taskId=uecba3676-5e05-4d8e-b107-94ecdbea6fe)<br />如果用户点击“同意”按钮，触发`onGetAuthorize`事件，`encryptedData`格式如下：
```json
{"response":"Tl0z1mGJaPTsMQL4WfBs2Vh0TQnpJ28KQb291vOuwS/+mMz7MvpFIkDHP2r78X7gYue5YhoPOFbtwfN7hIFIpg==","sign":"pVfhUpYcVdCyLSrV4d+7GXSlgbBJdbLOOprOOx97fnGuqwAMATr5laXcQPNFMlix+4epPoqhlORS9uVFifwAvhP36Wa8aaUNJESBzbKNBA1rp9wxdXup81sdqLg2X4cYAGgdMrL2Ad57icO8/8RMGq93I0uOvfBIIx4K6MTv9OfiALL+OczsQlK7CMvjgI9v/Q2rhkXQxm6zDLsanyGXXAlKa+03ihuF36wR6mIhk/VQ8SBLF81pjFk6DFw3tQoE7TfCgJf5/hpf5gaPyZ0hQDHFqCe6T4NeFCvc9qTd9kAdJ+z+yaYrk1sV+87PZNjUDoZw5HI26mOtAvqzCIC1jA=="}
```
如果用户点击“拒绝”按钮，触发`onAuthError`事件：
```json
{
  "errorMessage": "用户取消授权",
  "type": "getAuthorize"
}
```

参考：

- [会员能力：获取会员手机号产品介绍](https://opendocs.alipay.com/mini/introduce/getphonenumber)
- [组件：button按钮 - open-type 有效值](https://opendocs.alipay.com/mini/component/button#open-type%20%E6%9C%89%E6%95%88%E5%80%BC)
- [小程序API：my.getPhoneNumber](https://opendocs.alipay.com/mini/api/getphonenumber)
- [内容加密指引](https://opendocs.alipay.com/mini/2019110100244259)
- [用户授权](https://opendocs.alipay.com/mini/introduce/authcode)
- [服务端SDK下载](https://opendocs.alipay.com/open/54/103419/)
- [蚂蚁金服开放平台 node sdk](https://www.yuque.com/chenqiu/alipay-node-sdk)

<a name="pXy1q"></a>
#### 服务端解析加密数据

<a name="gVHdQ"></a>
#### 报错：“无效的授权关系”
需要绑定button的`onGetAuthorize`事件，而不是`onTap`事件。

因为`onGetAuthorize`事件会在弹出授权手机号弹窗点击“同意”按钮触发；而`onTap`事件在点击按钮的是否就会触发，这将导致用户还没点击“同意”就已经拿到了加密串，解析此加密串会报“无效的授权关系”错误。<br />![Snipaste_2021-10-14_10-42-58.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1634179395115-02277140-b7ed-40a0-a180-f8298504d19d.png#clientId=u6063a06d-e211-4&from=drop&id=VEZRR&originHeight=682&originWidth=379&originalType=binary&ratio=1&size=6321&status=done&style=none&taskId=uecba3676-5e05-4d8e-b107-94ecdbea6fe)

<a name="xR2xh"></a>
### 获取用户信息
<a name="wZMbP"></a>
#### 小程序端获取加密串
要获取用户信息，需要先获取授权码code，必须用户手动触发，将其绑定到按钮的`onTap`中即可：
```html
<button type="primary" onTap="getAuthCode">
  获取授权码
</button>
```
在事件绑定函数中使用`my.getAuthCode`，并将`scopes`设置为`auth_user`，可以为数组，也可为单个字符串：
```javascript
getAuthCode() {
  my.getAuthCode({
    scopes: ['auth_user'],
    success: (res) => {
      console.log(res.authCode);
    },
  });
}
```
当点击按钮的时候，会弹出授权弹框：<br />![Snipaste_2021-10-14_11-51-34.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1634183512625-86e04c45-b4cb-4e5f-818e-cfa648b1821a.png#clientId=u6063a06d-e211-4&from=drop&id=u3e392092&originHeight=679&originWidth=381&originalType=binary&ratio=1&size=7027&status=done&style=none&taskId=uea27dd4c-6f90-4c0b-9adf-3f43f4e8427)<br />当点击“同意”按钮后，可以获取到授权码code，服务器端通过解析此code获取用户信息。
```javascript
c489f67044824c07ac15a4ca30b8NX83
```

<a name="qkByS"></a>
#### 服务端解析加密数据





<a name="EHEm7"></a>
## 头条小程序授权登录
<a name="XDKao"></a>
### 获取手机号
<a name="qQpRV"></a>
#### 准备工作：配置获取手机号权限
获取手机号，需要先到字节跳动小程序后台开通获取手机号的功能。但是需要先发布小程序成功才能开通。<br />![Snipaste_2021-10-12_10-36-27.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1634006252345-0d534f24-9fc5-43e8-8b58-daa4a5fda8a0.png#clientId=u809a74ef-219c-4&from=drop&id=u650f30bd&originHeight=632&originWidth=1722&originalType=binary&ratio=1&size=29297&status=done&style=none&taskId=ud3e08640-b748-4a19-a564-dc34560688a)<br />注意开通获取手机号权限的限制：

- 小程序主体信用分大于 90 分；且所属主体半年内，没有严重的违规记录；
- 小程序内使用获取用户手机号的场景，需满足平台要求
- 小程序开发者需用当前小程序真实的内容进行提交
- 若开通后，发现开发者在使用过程中，滥用此能力对用户或平台造成负面影响，平台将有权利随时对该功能进行收回，并视情况对违规的小程序进行处罚。
- 个人主体小程序和未上线的小程序均不支持申请

<a name="wJ9AG"></a>
#### 小程序端获取加密串
小程序端获取加密串具体流程如下。<br />将button的`open-type`设置为`getPhoneNumber`；然后绑定`bindgetphonenumber`事件：
```html
<button
  open-type="getPhoneNumber"
  bindgetphonenumber="getPhoneNumberHandler"
>授权手机号</button>
```
在事件对象中可以获取到以下信息：
```javascript
Page({
  getPhoneNumberHandler(e) {
    console.log(e.detail.errMsg);
    console.log(e.detail.iv);
    console.log(e.detail.encryptedData);
    // TODO: 后台解析手机号
  },
});
```
参数说明：

| errMsg | string | 错误信息 |
| --- | --- | --- |
| encryptedData | string | 包括敏感数据在内的完整用户信息的加密数据 |
| iv | string | 加密算法的初始向量 |


参考：

- [功能接入指南：获取用户手机号权限申请](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/functional-plug-in/mobile-phone-number-to-obtain-permission-application/)
- [组件：获取手机号](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/component/acquire-phone-number-acquire/)

<a name="cNVYA"></a>
#### 服务端解析加密数据


<a name="noDyg"></a>
### 获取用户信息
<a name="m2BEx"></a>
#### 小程序端获取加密串
获取用户信息必须用户手动触发，需要绑定button的点击事件。
```html
<button bindtap="getUserInfo">获取用户信息</button>
```
```javascript
getUserInfo() {
  tt.login({
    force: true,
    success: code => {
      console.log(`login：`, code)
      tt.getUserInfo({
        withCredentials: true, // 是否需要返回敏感数据
        success(info) {
          console.log('getUserInfo：', info)
          // 调用后端接口解析用户信息
          // TODO...
        }
      })
    },
    fail(err) {
      console.log('login 调用失败', err)
    }
  })
}
```
返回的数据：<br />login返回的数据示例：
```json
{
  "anonymousCode": "-N_MlQXZT47***UejN7DWZV1OgQovfSWo",
  "code": "U0u1S7ajp***X1wDkwSz7f0",
  "isLogin": true,
  "errMsg": "login:ok"
}
```
> 其中，code临时登录凭证, 有效期 5 分钟。开发者可以通过在服务器端调用 [登录凭证校验接口](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/server/log-in/code-2-session) 换取 openid 和 session_key 等信息。

getUserInfo返回的数据示例：
```json
{
  "userInfo": {
    "nickName": "xiaoyulive",
    "avatarUrl": "https://p26-passport.byteacctimg.com/img/mosaic-legacy/3795/30***2272~300x300.image",
    "gender": 0,
    "city": "",
    "province": "",
    "country": "中国",
    "language": ""
  },
  "rawData": "{\"nickName\":\"xiaoyulive\",\"avatarUrl\":\"https://p26-passport.byteacctimg.com/img/mosaic-legacy/3795/30***2272~300x300.image\",\"gender\":0,\"city\":\"\",\"province\":\"\",\"country\":\"中国\",\"language\":\"\"}",
  "signature": "16c86d310d8***46fb6608ed5",
  "encryptedData": "TphrlfyLEdfXMZvKkEkuaugP***Bvebhq0sgy7TtF4v+R37TAZcfQkwjgv5jvmw=",
  "iv": "p4DhlAJ***RSmCA==",
  "errMsg": "getUserInfo:ok"
}
```
可以看到，其实基础信息已经通过`tt.getUserInfo`获取到了，如果需要敏感数据，就需要后端解析`encryptedData`了。

参考：

- [API：tt.login](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/api/open-interface/log-in/tt-login)
- [API：tt.getUserInfo](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/api/open-interface/user-information/tt-get-user-info)
- [API：tt.checkSession](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/api/open-interface/log-in/tt-check-session/)


<a name="orzMS"></a>
#### 服务端解析加密数据
以node.js解析加密信息为例。<br />服务端通过express开启HTTP服务，通过crypto解密数据，通过node-fetch请求接口：
```json
const crypto = require("crypto")
const fetch = require('node-fetch')
const express = require("express")
const app = express();

// 解密信息
function decrypt({ sessionKey, encryptedData, iv }) {
  const decipher = crypto.createDecipheriv(
    "aes-128-cbc",
    Buffer.from(sessionKey, "base64"),
    Buffer.from(iv, "base64")
  );
  let ret = decipher.update(encryptedData, "base64");
  ret += decipher.final();
  return ret;
}

// 获取sessionKey
async function getSession({ appid, secret, code, anonymous_code }) {
  let url = 'https://developer.toutiao.com/api/apps/v2/jscode2session'
  let request = {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify({
      appid,
      secret,
      code,
      anonymous_code
    })
  }

  let res = await fetch(url, request)
  let dataJson = await res.json()
  return dataJson
}


;(() => {
  app.get('/', (req, res, next) => {
    console.log(req.query)
    let { code, anonymousCode, encryptedData, iv } = req.query
    getSession({
      appid: 'tt01***d6e01',
      secret: '50890***ff09a7bcb',
      code,
      anonymous_code: anonymousCode,
    }).then(ret => {
      let sessionKey = ret.data.session_key
      let info = decrypt({
        sessionKey,
        encryptedData,
        iv
      })
      res.send(info)
    })
  })

  app.listen(3000, function () {
    console.log("server start in http://127.0.0.1:3000");
  });
})()
```
小程序端获取用户信息：
```json
tt.login({
  force: true,
  success: code => {
    console.log(`login：`, JSON.stringify(code, '', 2))
    tt.getUserInfo({
      withCredentials: true,
      success(info) {
        console.log('getUserInfo：', JSON.stringify(info, '', 2))
        tt.request({
          url: `http://127.0.0.1:3000?code=${encodeURIComponent(code.code)}&anonymousCode=${encodeURIComponent(code.anonymousCode)}&encryptedData=${encodeURIComponent(info.encryptedData)}&iv=${encodeURIComponent(info.iv)}`, // 目标服务器url
          success: (res) => {
            console.log(res);
          },
          fail: (err) => {
            console.log(err);
          },
        });
      }
    })
  },
  fail(err) {
    console.log('login 调用失败', err)
  }
})
```

获取到的sessionKey示例：
```json
{
  err_no: 0,
  err_tips: 'success',
  data: {
    session_key: 'p9BQ3no***R/jC1pW+8g==',       
    openid: '30c4693f-***-c8ddec9b303a',
    anonymous_openid: 'm-AJmGWuL.pvBM0H',
    unionid: 'e98a5258-***-76da3ca13424',
    dopenid: ''
  }
}
```
解析后的用户信息：
```json
{
  "nickName": "xiaoyulive",
  "avatarUrl": "https://p26-passport.byteacctimg.com/img/mosaic-legacy/3795/303***72~300x300.image",
  "gender": 0,
  "city": "",
  "province": "",
  "country": "中国",
  "language": "",
  "openId": "30c4***c9b303a",
  "unionId": "e98a525***da3ca13424",
  "watermark": {
    "appid": "tt0***e01",
    "timestamp": 1634008408
  }
}
```

报错示例：
```json
{
  err_no: 40018,       
  err_tips: 'bad code',
  data: {
    session_key: '',
    openid: '',
    anonymous_openid: '',
    unionid: '',
    dopenid: ''
  }
}
```
错误码的对应关系如下：

| **错误码** | **描述** |
| --- | --- |
| 0 | 请求成功 |
| -1 | 系统错误 |
| 40014 | 未传必要参数，请检查 |
| 40015 | appid 错误 |
| 40017 | secret 错误 |
| 40018 | code 错误 |
| 40019 | acode 错误 |
| 其它 | 参数为空 |


参考：

- [服务端：code2Session](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/server/log-in/code-2-session/)
- [API：敏感数据处理](https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/api/open-interface/user-information/sensitive-data-process/)

