<a name="4e6320a8"></a>
## 定位并解析地理位置的封装

根据uniapp暴露的[定位API：uni.getLocation](https://uniapp.dcloud.io/api/location/location)，以及 [高德开放平台文档：地理/逆地理编码](https://lbs.amap.com/api/webservice/guide/api/georegeo)。为了方便调用，我想到了将其进行合并封装。

思路为：先通过 `uni.getLocation` 进行定位，然后获取到经纬度，通过经纬度进行逆地理编码查询。

通过测试，在Web端逆地理编码并不存在跨域问题，但是有调用次数限制，日调用次数为3000000次，足以满足大部分需求。

```javascript
class Utils {
  constructor () {}

  ...

  // 获取地理位置详情信息
  async getLocationInfo() {
    // Reference：https://lbs.amap.com/api/webservice/guide/api/georegeo/
    return new Promise((resolve, reject) => {
      uni.getLocation({
        success: (res) => {
          console.log('获取定位成功')
          console.log(res)
          uni.request({
            url: 'https://restapi.amap.com/v3/geocode/regeo',
            data: {
              output: 'json',
              location: `${res.longitude},${res.latitude}`,
              key: 'your key',
              extensions: 'base',
              batch: false
            },
            success: (res) => {
              console.log(res)
              if (res.data && res.data.status === "1") {
                console.log('解析地理位置成功')
                console.log(res.data.regeocode.addressComponent.adcode)
                resolve(res.data)
              } else {
                console.log('解析地理位置失败')
                reject('解析地理位置失败')
              }
            },
            fail: (e) => {
              console.log('解析地理位置失败')
              console.log(e)
              reject('解析地理位置失败')
            }
          })
        },
        fail: err => {
          // this.toast('定位失败：' + JSON.stringify(err))
          console.log('获取定位失败')
          console.log(err)
          reject('获取定位失败')
        }
      });
    })
  }
}
```

我将其挂载到了Vue的原型中，使用的时候：

```javascript
let locationInfo = await this.$utils.getLocationInfo()
console.log(locationInfo)
```

如果响应正确，其格式应为：

```json
{
  "status": "1",
  "regeocode": {
    "addressComponent": {
      "city": "昆明市",
      "province": "云南省",
      "adcode": "530114",
      "district": "呈贡区",
      "towncode": "530114002000",
      "streetNumber": {
        "number": "1号",
        "location": "102.833659,24.8784011",
        "direction": "南",
        "distance": "141.125",
        "street": "锦绣大街"
      },
      "country": "中国",
      "township": "洛龙街道",
      "businessAreas": [
        []
      ],
      "building": {
        "name": [],
        "type": []
      },
      "neighborhood": {
        "name": [],
        "type": []
      },
      "citycode": "0871"
    },
    "formatted_address": "云南省昆明市呈贡区洛龙街道吉安街昆明市人民政府"
  },
  "info": "OK",
  "infocode": "10000"
}
```

<a name="443686ea"></a>
## 关于APP端离线打包后定位失效的问题

我在本地打包后遇到这样一个问题：使用HBuilderX真机调试的时候，能够正常获取到定位。但离线打包后，就不可以获取到正确的定位信息，永远走的都是fail。经过一系列排查，发现需要在Android原生工程中进行相关配置才能正确获取到定位。

官方文档中提到：

Android由于谷歌服务被墙，或者手机上没有GMS，想正常定位就需要向高德等三方服务商申请SDK资质，获取AppKey。否则打包后定位就会不准。云打包时需要在manifest的SDK配置中填写Appkey。在manifest可视化界面有详细申请指南，详见：[https://ask.dcloud.net.cn/article/29](https://ask.dcloud.net.cn/article/29)。离线打包自行在原生工程中配置。注意包名、appkey、证书信息必须匹配。真机运行可以正常定位，是因为真机运行基座使用了DCloud向高德申请的sdk配置，打包后必须由开发者自己申请。如果手机自带GMS且网络环境可以正常访问google定位服务器，此时无需在manifest填写高德定位的sdk配置。

我使用的是高德定位，具体流程如下：

<a name="8674cb09"></a>
### 1. 到高德开放平台申请应用
首先注册高德开放平台的账号，到控制台中<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671085999090-dc44b376-8f3b-4a9f-b0be-c64f9c48d789.png#averageHue=%23d0d4cf&clientId=u4ff550d2-68ed-4&from=paste&height=411&id=u488f2b39&originHeight=411&originWidth=1914&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61916&status=done&style=none&taskId=u9ccd9e7c-4c5b-4518-b142-87fe71bf02b&title=&width=1914)


添加应用<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086012743-f07a2311-b4e7-4b2c-be29-cf60b167c1a1.png#averageHue=%23f0f0f0&clientId=u4ff550d2-68ed-4&from=paste&height=325&id=u21657a3a&originHeight=325&originWidth=642&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13602&status=done&style=none&taskId=uec8829e5-1850-4bd7-93da-b0290a7c5d9&title=&width=642)

然后在应用下添加key<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086024358-57bd9495-cd9b-4dc7-90b1-91f924899758.png#averageHue=%23fbfbfb&clientId=u4ff550d2-68ed-4&from=paste&height=715&id=ubdb6fd7c&originHeight=715&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88196&status=done&style=none&taskId=u5d1c5923-de6d-4a71-b8cf-bdb16c7f0a7&title=&width=761)

其中：<br />SHA1码的获取方式：在命令行中输入以下命令获取
```
keytool -list -v -keystore test.keystore
Enter keystore password: // 输入密码，回车
```

PackageName为`build.gradle`中配置的包名

创建好应用及key后，记住此key

<a name="ee9da8ea"></a>
### 2. 需要引入工程的jar/aar文件
需要将以下jar/aar文件（[下载地址点这里](https://nativesupport.dcloud.net.cn/AppDocs/download/android)）放到工程的libs目录下

| 路径 | 文件 |
| --- | --- |
| SDK\\libs | amap-libs-release.aar, geolocation-amap-release.aar |


<a name="b484da13"></a>
### 3. 在AndroidManifest.xml中配置
application节点前：
```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
<uses-permission android:name="android.permission.READ_LOGS"/>
<uses-permission android:name="android.permission.WRITE_SETTINGS"/>
```

application节点下：
```xml
<meta-data android:name="com.amap.api.v2.apikey" android:value=\"%用户申请的APPkey%\"></meta-data>
<service android:name="com.amap.api.location.APSService"></service>
```

<a name="fc2df2c7"></a>
### 4. 在manifest.json中配置
在`manifest.json`中将key进行配置<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671086113880-7b0545ad-6a75-4be9-b846-4b42334d39eb.png#averageHue=%23fbf6e5&clientId=u15a2770e-2971-4&from=paste&height=290&id=u4d062f26&originHeight=290&originWidth=754&originalType=binary&ratio=1&rotation=0&showTitle=false&size=50885&status=done&style=none&taskId=u7a097110-426b-48db-afc3-0ddbe4fca96&title=&width=754)

<a name="35808e79"></a>
## 参考资料

- [uniapp官方文档：获取位置](https://uniapp.dcloud.io/api/location/location)
- [地图插件配置](https://ask.dcloud.net.cn/article/29)
- [uniapp离线打包之定位模块的配置](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/geolocation)
- [Android平台签名证书(.keystore)生成指南](https://ask.dcloud.net.cn/article/35777#keyinfo)
