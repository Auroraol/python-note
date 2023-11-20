<a name="MRjof"></a>
## 高德地图H5的配置
需要到高德开放平台获取到key和securityJsCode，在`manifest.json`中配置
```javascript
{
  "h5": {
    "sdkConfigs": {
      "maps": {
        "amap": {
          "key": "xxx",
          "securityJsCode": "xxx"
        }
      }
    }
  }
}
```
需要到 [高德开放平台](https://console.amap.com/dev/key/app) 申请供Web调用的key<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671084441884-bcdb4da5-654a-421e-b582-bfe7650c5da8.png#averageHue=%23fbfbfb&clientId=u91c8dfc8-5614-4&from=paste&height=570&id=bctXt&originHeight=570&originWidth=737&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41432&status=done&style=none&taskId=u58415b8d-1e91-48f3-b5e3-371df517c1f&title=&width=737)<br />创建好后，获取到key和securityJsCode，填写到`manifest.json`<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671084525274-1d365eb4-8c6d-471e-8f8d-fceb0921d727.png#averageHue=%23d7e6e5&clientId=u91c8dfc8-5614-4&from=paste&height=360&id=S3zPb&originHeight=360&originWidth=1679&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30562&status=done&style=none&taskId=ue27e8e2e-8b82-4534-b79a-eb271de3a97&title=&width=1679)

调用时常见的错误码：

- `USERKEY_PLAT_NOMATCH`：配置的key与目标平台不匹配，比如配置了Web服务的key
- `INVALID_USER_SCODE`：需要将目标域名添加到 `域名白名单`中

<a name="cvZVW"></a>
## 微信小程序配置
如果是微信小程序，需要在`manifest.json`中，`permission`和`requiredPrivateInfos`节点添加：
```json
{
  "mp-weixin": {
    "appid": "xxx",
    "usingComponents": true,
    "permission": {
      "scope.userLocation": {
        "desc": "你的位置信息将用于小程序位置接口的效果展示"
      }
    },
    "requiredPrivateInfos": [
      "getLocation",
      "chooseLocation"
    ]
  }
}
```

<a name="L2Rba"></a>
## 地图选点
地图选点查考文档：[uni.getLocation(OBJECT)](https://uniapp.dcloud.net.cn/api/location/location.html#chooselocation)<br />地图选点调用示例：
```javascript
uni.chooseLocation({
  longitude: uni.$store.currentLocation.longitude,
  latitude: uni.$store.currentLocation.latitude,
  success: async function (res) {
    console.log('位置名称：' + res.name)
    console.log('详细地址：' + res.address)
    console.log('纬度：' + res.latitude)
    console.log('经度：' + res.longitude)
  }
})
```

在微信小程序调用的是内置的地图选点API，看起来会比H5端的好看些，具体的样式差异如下：

| 微信小程序 | H5 |
| --- | --- |
| ![Screenshot_2022-12-15-14-12-00-320_com.tencent.mm.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/2213540/1671084802484-6cffe499-fe49-4d6c-be29-64826dca0fc2.jpeg#averageHue=%23ebe8e4&clientId=u91c8dfc8-5614-4&from=drop&height=829&id=Lpyab&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=822182&status=done&style=none&taskId=ue16dbb20-5cb9-4d96-ac2a-d8ec866acd1&title=&width=373) | ![Screenshot_2022-12-15-14-14-54-223_com.tencent.mm.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/2213540/1671084924139-f3cd496d-f559-43e0-99e2-e0b9509acbd8.jpeg#averageHue=%23f2f0f0&clientId=u91c8dfc8-5614-4&from=drop&id=u8021cb06&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=614957&status=done&style=none&taskId=u4265d2fc-d2cf-41c7-b020-0447f1d89e3&title=) |





