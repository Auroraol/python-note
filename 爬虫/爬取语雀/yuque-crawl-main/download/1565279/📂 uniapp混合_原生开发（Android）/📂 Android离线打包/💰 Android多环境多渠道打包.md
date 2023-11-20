很多时候，会有以下需求：<br />同一个项目生成不同的APK，比如说一个正式版、一个测试版，他们会拥有不同的包名，打包出来后两个APK都能同时安装到同一个Android设备。<br />甚至有更复杂的需求：比如说，为每一个省/城市打包为具有不同包名的APK，每个APK的桌面图标、应用名称均不相同。

不一定每个开发者都会遇到这种奇葩需求，但是我的确是遇到了。

以下演示，同一个项目打包为两个APK，一个正式版，一个测试版，

正式版包名： `com.example.www` <br />测试版包名： `com.example.www.test` 

接下来就说一下具体的方法。
<a name="7AsUb"></a>
## 从环境变量入手
在cli生成的项目， `package.json` 中的 `scripts` 中，可以看到一堆的环境变量配置，比如：
```json
{
    "dev:h5": "cross-env NODE_ENV=development UNI_PLATFORM=h5 vue-cli-service uni-serve",
}
```
使用 `cross-env` 配置环境变量，这里，传入了：

- NODE_ENV
- UNI_PLATFORM

通过 `process.env` 取出环境变量，我们可以做很多事情，比如根据不同的环境变量设置不同的接口地址：
```json
// #ifdef H5
let baseApi = ""
switch (process.env.NODE_ENV) {
  case 'development':
    baseApi = "https://api.example.com/"
    break
  case 'production':
    baseApi = "https://api.example.com/"
    break
  case 'test':
    baseApi = "https://testapi.example.com/"
    break
}
// #endif
```

那么，我们是不是可以通过环境变量，编写一个自动化打包脚本，分别用于不同环境、不同渠道？答案肯定是可以的。

<a name="kXDH1"></a>
## 手动配置Android原生工程
在进行自动化打包之前，我们需要知道手动如何进行多环境、多渠道打包。以便我们后续编写自动化打包脚本，模拟开发者手动执行打包操作。

我们知道，包名配置于`build.gradle` ：
```groovy
defaultConfig {
    applicationId "com.example.www"
    minSdkVersion 19
    targetSdkVersion 28
    versionCode 300
    versionName "1.0.0"
}
```

如果我们想要快速地添加一个打包环境 `debug` ，在默认包名的基础上生成一个新的包名，比如在默认包名后添加一个后缀 `.test` ，也就是：`com.example.www.test` 。直接修改 `build.gradle` ，配置两个打包环境：
```groovy
buildTypes {
    release {
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        signingConfig signingConfigs.release
        resValue "string", "app_name", "My APP"
    }
    debug {
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        signingConfig signingConfigs.release
        applicationIdSuffix ".test"
        resValue "string", "app_name", "My APP 测试"
    }
}
```
其中：

- `applicationIdSuffix` 应用包名后缀，测试包名在正常包名后添加后缀
- `resValue` 配置的 `string` 资源，相当于在 `strings.xml` 中添加资源：
```xml
 <string name="app_name">My APP</string>
```

不过需要注意，在`build.gradle` 中添加过 `resValue` 后，对应的资源应该删掉，否则编译会报错，提示有重复的资源。

<a name="lnI4D"></a>
## 自动化打包脚本
当然，不可能每次打包的时候都去开一个Android Studio，然后手动去点击签名打包。一两次还好，每次都去搞就会很烦。于是，我们可以将打包过程做成一个脚本，自动匹配环境，自动使用命令打包，无需可视化。

具体做法是：<br />先修改 `package.json`，在scripts节点下添加一些相关的命令：
```json
{
    "dev:android-resource": "cross-env NODE_ENV=development UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=./platforms/android/app/src/main/assets/apps/<your appid>/www vue-cli-service uni-build --watch",
    "build:android-resource": "cross-env NODE_ENV=production UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=./platforms/android/app/src/main/assets/apps/<your appid>/www vue-cli-service uni-build",
    "build:android-apk-prod-only": "yarn build:android-resource && cd platforms/android && gradle assembleRelease",
    "build:android-apk-prod-and-push-to-oss": "cross-env NODE_ENV=production node deploy/scripts/build-apk.js",
    "build:android-apk-test-only": "yarn build:android-resource && cd platforms/android && gradle assembleDebug",
    "build:android-apk-test-and-push-to-oss": "cross-env NODE_ENV=test node deploy/scripts/build-apk.js",
    "build:android-wgt-prod-and-push-to-oss": "cross-env NODE_ENV=production node deploy/scripts/build-wgt.js",
    "build:android-wgt-test-and-push-to-oss": "cross-env NODE_ENV=test node deploy/scripts/build-wgt.js",
}
```

简单说明一下，这里使用环境变量区分是测试环境还是生产环境，然后指定打包脚本 `build-apk.js` 和 `build-wgt.js` ，还有打包命令：

- `gradle assembleDebug` 测试环境打包，打包后路径为 `app/build/outputs/apk/release/app-release.apk` 
- `gradle assembleRelease` 生产环境打包，打包后路径为 `app/build/outputs/apk/debug/app-debug.apk` 

打包资源直接输出到 Android原生项目的资源目录，节省下复制资源的操作。

重点来了，说说打包APK脚本 `build-apk.js` 的具体思路：

1. 修改应用版本号
2. 打包APK
3. 推送到OSS和应用商店

修改应用版本号是常规操作，具体的做法有很多。我的思路是读取 `build.gradle` ，然后正则匹配到版本名 `versionName` ，将其转为数字，截取最后一位，加一即可。

这里重点说一下第二步：打包APK。还是通过环境变量 `NODE_ENV` 指定打包过程：
```javascript
const { execSync } = require('child_process')

switch (process.env.NODE_ENV) {
  case 'production':
    console.log(execSync(`yarn build:android-apk-prod-only`, { encoding: 'utf-8'}))
    break
  case 'test':
    console.log(execSync(`yarn build:android-apk-test-only`, { encoding: 'utf-8'}))
    break
}
```

推送到OSS也是常规操作，这里还是得根据打包环境区分推送到哪个位置。大概流程如下：
```javascript
let OSS = require('ali-oss');

function upToOss() {
  let client = new OSS({
    region: 'oss-cn-shenzhen',
    accessKeyId: 'your accessKeyId',
    accessKeySecret: 'your accessKeySecret'
  });

  client.useBucket('your bucket');

  let ossBasePath = `apk`

  switch (process.env.NODE_ENV) {
    case 'production':
      put(`${ossBasePath}/app.json`, 'app.json')
      put(`${ossBasePath}/myapp.apk`, 'platforms/android/app/build/outputs/apk/release/app-release.apk')
      put(`${ossBasePath}/apks/${app.versionName}/app-release.apk`, 'platforms/android/app/build/outputs/apk/release/app-release.apk')
      put(`${ossBasePath}/apks/${app.versionName}/output.json`, 'platforms/android/app/build/outputs/apk/release/output.json')
      break
    case 'test':
      put(`${ossBasePath}/app-test.json`, 'app.json')
      put(`${ossBasePath}/myapp-test.apk`, 'platforms/android/app/build/outputs/apk/debug/app-debug.apk')
      put(`${ossBasePath}/apks-test/${app.versionName}/app-debug.apk`, 'platforms/android/app/build/outputs/apk/debug/app-debug.apk')
      put(`${ossBasePath}/apks-test/${app.versionName}/output.json`, 'platforms/android/app/build/outputs/apk/debug/output.json')
      break
  }

  async function put (ossPath, localFile) {
    try {
      await client.put(ossPath, localFile);
      console.log(`${localFile}上传成功：${ossPath}`);
    } catch (err) {
      console.log(err);
    }
  }
}

upToOss()
```

<a name="IcON2"></a>
## 通过包名调用不同的API
通常情况下，不同环境可能会调用到不同的API，这里我们可以通过读取不同的包名，来改变不同环境下的API。

举个例子：
```javascript
// #ifdef APP-PLUS
let baseApi = "https://api.example.com/"
let packageName = plus.android.runtimeMainActivity().getPackageName()
if (packageName === 'com.example.www.test') {
  baseApi = "https://testapi.example.com/"
}
// #endif
```

<a name="OpolL"></a>
## 通过包名接收不同的更新包
同样地，如果要接收不同的热更新包和整包更新，也可以通过包名判断实现。

```javascript
let appUrl = "https://file.your_oss_domain.cn/apk/app.json"

let packageName = plus.android.runtimeMainActivity().getPackageName()
if (packageName === 'com.example.www.test') {
  appUrl = "https://file.your_oss_domain.cn/apk/app-test.json"
}

let appInfo = this.getVersion()
uni.request({
  url: appUrl,
  success: async (result) => {
    let { versionCode, versionName, appPath, wgtPath, appTestPath, wgtTestPath } = result.data
    if (packageName === 'com.example.www.test') {
      appPath = appTestPath
      wgtPath = wgtTestPath
    }
    let versionInfo = {
      appPath,
      wgtPath,
      newestVersion: `${versionName}.${versionCode}`,
      newestVersionCode: versionCode,
      newestVersionName: versionName,
      currentVersion: appInfo.version,
      currentVersionCode: appInfo.versionCode,
      currentVersionName: appInfo.versionName
    }
    
    // 热更新和整包更新的实现...
  }
})
```
其中 `app.json` 和 `app-test.json` 举例如下：
```json
{
  "versionName": "1.0.0",
  "versionCode": 300,
  "appPath": "https://file.your_oss_domain.cn/apk/sa-learn.apk",
  "wgtPath": "https://file.your_oss_domain.cn/apk/www.wgt",
  "appTestPath": "https://file.your_oss_domain.cn/apk/sa-learn-test.apk",
  "wgtTestPath": "https://file.your_oss_domain.cn/apk/www-test.wgt"
}
```

具体的整包更新实现参考文章：<br />[uniapp热更新和整包更新](https://www.yuque.com/go/doc/11288112?view=doc_embed)

