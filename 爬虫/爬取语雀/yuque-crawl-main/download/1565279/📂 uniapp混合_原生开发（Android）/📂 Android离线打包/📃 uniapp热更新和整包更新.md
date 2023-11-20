我们知道，在打包Android App之前，我们需要先通过HX生成打包资源。如果是通过cli创建的项目，则通过以下命令生成打包资源：

```
yarn build:app-plus
```

生成打包资源后的目录长这样：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259872885-bdf879bc-f0fb-4798-b4b4-3aca48f59f55.png#averageHue=%23fbf9f8&clientId=ue9346dd3-484a-4&from=paste&height=468&id=u57d38194&originHeight=468&originWidth=750&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56786&status=done&style=none&taskId=uf511d214-de34-42b2-9cf8-0b933b188df&title=&width=750)

然后将整个目录中的所有文件拷贝到Android项目的 `assets/apps/<appid>/www` 中：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259889715-81761d9a-f6d9-46e8-8123-dff23ade1246.png#averageHue=%23fbf9f8&clientId=ue9346dd3-484a-4&from=paste&height=473&id=u869b4224&originHeight=473&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57919&status=done&style=none&taskId=ud3f51a82-0ff0-4d46-a140-490afa7fcb9&title=&width=760)

可以看出，所有生成的文件，其实只是一个资源目录。

热更新的原理就是：**替换资源目录中的所有打包资源**

<a name="55f8c02b"></a>
## 热更新包分析

我们通过HX生成的热更新包：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259911623-b75da3da-c9f3-40bc-90ad-99406b266a2d.png#averageHue=%23fcf8f1&clientId=ue9346dd3-484a-4&from=paste&height=429&id=ubd736930&originHeight=429&originWidth=297&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20070&status=done&style=none&taskId=u33c4be38-0f59-4745-ac72-57e58f8c77c&title=&width=297)

生成的热更新包长这样：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259926842-99491193-49b5-423d-bc72-b52a86f1d508.png#averageHue=%23b2af85&clientId=ue9346dd3-484a-4&from=paste&height=584&id=udd744f74&originHeight=584&originWidth=764&originalType=binary&ratio=1&rotation=0&showTitle=false&size=164593&status=done&style=none&taskId=u871a2a51-a0d9-4797-a717-439233a7883&title=&width=764)

可以看出，wgt其实就是一个压缩文件，将生成的资源文件全部打包。

知道原理后，我们就不一定需要通过HX创建wgt了，我们可以使用`yarn build:app-plus`命令先生成打包资源目录，再将其压缩为zip包，修改扩展名为wgt即可：

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259945795-f37bf981-84f7-4075-9ed4-ab784488269c.png#averageHue=%23b8b087&clientId=ue9346dd3-484a-4&from=paste&height=528&id=u83204dbe&originHeight=528&originWidth=763&originalType=binary&ratio=1&rotation=0&showTitle=false&size=160813&status=done&style=none&taskId=u4a25a44d-687e-43d7-8a0b-bd90639aa8b&title=&width=763)

注意到我两次都将`manifest.json`圈红，目的是强调：**wgt包中，必须将manifest,json所在路径当做根节点进行打包**。

打完包后，我们可以将其上传到OSS。

<a name="c3fa2b6a"></a>
## 热更新方案

热更新方案：通过增加当前APP资源的版本号（versionCode），跟上一次打包时的APP资源版本号进行对比，如果比之前的资源版本号高，即进行热更新。

热更新原理：uniapp的热更新，其实是将build后的APP资源，打包为一个zip压缩包（扩展名改为wgt）。

涉及到的版本信息文件：

- src/manifest.json
- app.json (自己创建，用于版本对比)
- platforms/android/app/build.gradle

注意事项：

保证以上文件的`versionName`和`versionCode`均保持一致。

<a name="5ca1096b"></a>
## 热更新核心代码

以下为热更新的核心代码：

```javascript
// #ifdef APP-PLUS
let downloadPath = "https://xxx.cn/apk/app.wgt"
uni.downloadFile({
    url: downloadPath,
    success: (downloadResult) => {
        if (downloadResult.statusCode === 200) {
            plus.runtime.install(downloadResult.tempFilePath, {
                force: true // 强制更新
            }, function() {
                console.log('install success...');
                plus.runtime.restart();
            }, function(e) {
                console.error(e);
                console.error('install fail...');
            });
        }
    }
})
// #endif
```

这里是下载wgt包，并进行安装的代码。以上代码无论如何都会下载wgt进行安装。

<a name="20fca111"></a>
## 更新接口

实际上，在这之前，我们还需要判断是否需要更新，这就涉及到接口的部分。在此，只讲讲思路：

1. 获取安装的版本名、版本号等信息，将其当做参数调用对应的更新接口；
2. 接口取到这些信息，与最新版本进行对比，如果版本已经更新，返回需要更新的信息；
3. 接口可以自行约定，怎么方便这么来。

我自己做的话，根本没写什么接口，只是创建了一个`app.json`文件，用于存放最新版本信息：

```json
{
  "versionCode": "100",
  "versionName": "1.0.0"
}
```

将其上传到OSS，然后在下载wgt包之前进行版本检查即可：

```javascript
// #ifdef APP-PLUS
plus.runtime.getProperty(plus.runtime.appid, function(widgetInfo) {
    console.log(widgetInfo);
    uni.request({
        url: 'https://xxx.cn/apk/app.json',
        success: (result) => {
            let { versionCode, versionName } = result.data
            console.log({ versionCode, versionName });
            // 判断版本名是否一致
            if (versionName === widgetInfo.version) {
                // 如果安装的版本号小于最新发布的版本号，则进行更新
                if (parseInt(widgetInfo.versionCode) < parseInt(versionCode)) {
                    // 下载wgt更新包
                    let downloadPath = "https://xxx.cn/apk/app.wgt"
                    uni.downloadFile({
                        url: downloadPath,
                        success: (downloadResult) => {
                            if (downloadResult.statusCode === 200) {
                                plus.runtime.install(downloadResult.tempFilePath, {
                                    force: true // 强制更新
                                }, function() {
                                    console.log('热更新成功');
                                    plus.runtime.restart();
                                }, function(e) {
                                    console.error('热更新失败，错误原因：' + e);
                                });
                            }
                        }
                    })
                } else {
                    console.log('你的版本为最新，不需要热更新');
                }
            } else {
                console.log('版本名不一致，请使用整包更新');
            }
        }
    });
});
// #endif
```

OK，至此，热更新就完成了。

<a name="4e001262"></a>
## Android整包更新

看到上面更新逻辑，如果版本名不一致，则需要下载最新的apk进行安装，在下载之前，建议给用户一个更新提示：

```javascript
console.log('版本名不一致，请使用整包更新');
let url = "https://xxx.cn/apk/app.apk"
uni.showModal({ //提醒用户更新
    title: "更新提示",
    content: "有新的更新可用，请升级",
    success: (res) => {
        if (res.confirm) {
            plus.runtime.openURL(url);
        }
    }
})
```

以上代码是官方提供的，其实也可以下载apk成功后，直接调用`install`进行安装：

```javascript
console.log('版本名不一致，请使用整包更新');
let downloadPath = "https://zys201811.boringkiller.cn/shianonline/apk/app.apk"
uni.showModal({ //提醒用户更新
    title: "更新提示",
    content: "有新的更新可用，请升级",
    success: (res) => {
        if (res.confirm) {
            // plus.runtime.openURL(downloadPath);
            uni.downloadFile({
                url: downloadPath,
                success: (downloadResult) => {
                    if (downloadResult.statusCode === 200) {
                        console.log('正在更新...');
                        plus.runtime.install(downloadResult.tempFilePath, {
                            force: true // 强制更新
                        }, function() {
                            console.log('整包更新成功');
                            plus.runtime.restart();
                        }, function(e) {
                            console.error('整包更新失败，错误原因：' + e);
                        });
                    }
                }
            })
        }
    }
})
```

<a name="fb85af9e"></a>
## 热更新的自动化处理

知道原理后，就好办了，我们可以将其繁杂的工作自动化，以减少重复劳动。

修改`package.json`的相关打包脚本：

```json
{
  "name": "shianaonline",
  "version": "0.1.224",
  "private": true,
  "scripts": {
    "apk": "node deploy/scripts/build-apk.js",
    "wgt": "node deploy/scripts/build-wgt.js",
    "build:app-plus-android": "cross-env NODE_ENV=production UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=./platforms/android/app/src/main/assets/apps/your appid/www vue-cli-service uni-build",
    "build:app-plus-ios": "cross-env NODE_ENV=production UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=./platforms/iOS/apps/your appid/www vue-cli-service uni-build",
  }
}
```

其中，需要替换的地方是`your appid`，换为自己的uniapp appid

创建`app.json`，用于存储当前app的版本信息：

```json
{
  "versionName": "1.0.27",
  "versionCode": 336,
  "appPath": "https://xxx.oss.com/apk/app-release.apk",
  "wgtPath": "https://xxx.oss.com/apk/www.wgt"
}
```

创建自动化打包脚本`build-wgt.js`：

```javascript
const fs = require('fs')
const { execSync } = require('child_process')
const join = require('path').join

// 修改版本号
let app = require('../../app.json')
let manifest = require('../../src/manifest.json')

if (app.versionName !== manifest.versionName) {
  console.info('manifest.json和app.json的versionName不一致，请检查')
  return
}

if (app.versionCode !== manifest.versionCode) {
  console.info('manifest.json和app.json的versionCode不一致，请检查')
  return
}

// 获取build.gradle的版本名
let gradleFilePath = '../../platforms/android/app/build.gradle'
let data = fs.readFileSync(__dirname + '/' + gradleFilePath, {
  encoding: 'utf-8'
})

let reg = new RegExp(`versionCode ${app.versionCode}`, "gm")

if (!reg.test(data)) {
  console.log('platforms/android/app/build.gradle的versionCode不一致，请检查')
  return
}

app.versionCode += 1
manifest.versionCode += 1

console.log('====================');
console.log('newVersion：' + app.versionName + "." + app.versionCode);
console.log('====================');

let appJSON = JSON.stringify(app, null, 2)
let manifestJSON = JSON.stringify(manifest, null, 2)

let replaceFiles = [{
  path: '../../app.json',
  name: 'app.json',
  content: appJSON
}, {
  path: '../../src/manifest.json',
  name: 'manifest.json',
  content: manifestJSON
}]

replaceFiles.forEach(file => {
  fs.writeFileSync(__dirname + '/' + file.path, file.content, {
    encoding: 'utf-8'
  })
  console.log(file.name + ': 替换成功');
})


// 替换build.gradle的版本名
let result = data.replace(reg, `versionCode ${app.versionCode}`)
fs.writeFileSync(__dirname + '/' + gradleFilePath, result, {
  encoding: 'utf-8'
})
console.log('platforms/android/build.gradle: 替换成功')

console.log('====================');

// 编译
console.log(execSync('yarn build:app-plus-android', { encoding: 'utf-8'}))

// 打包
const compressing = require('compressing');

const tarStream = new compressing.zip.Stream();

const targetPath = './platforms/android/app/src/main/assets/apps/your appid/www'
const targetFile = './www.wgt'

let paths = fs.readdirSync(targetPath);
paths.forEach(function (item) {
  let fPath = join(targetPath, item);
  tarStream.addEntry(fPath);
});

tarStream
  .pipe(fs.createWriteStream(targetFile))
  .on('finish', upToOss)

// 上传至OSS
let OSS = require('ali-oss');

function upToOss() {
  let client = new OSS({
    region: 'oss-cn-shenzhen',
    accessKeyId: 'your accessKeyId',
    accessKeySecret: 'your accessKeySecret'
  });

  client.useBucket('your bucketName');

  let ossBasePath = `apk`

  put(`${ossBasePath}/www.wgt`, 'www.wgt')
  put(`${ossBasePath}/wgts/${app.versionCode}/www.wgt`, 'www.wgt')
  put(`webview/vod.html`, 'src/hybrid/html/vod.html')
  put(`${ossBasePath}/app.json`, 'app.json')

  async function put (ossPath, localFile) {
    try {
      await client.put(ossPath, localFile);
      console.log(`${localFile}上传成功：${ossPath}`);
    } catch (err) {
      console.log(err);
    }
  }
}

console.log('====================');
console.log('更新完毕，newVersion：' + app.versionName + "." + app.versionCode);
console.log('====================');
```

以上打包脚本，做了以下工作：

1. 验证版本号和版本名是否正确，如果不正确，终止脚本
2. 修改当前APP版本号
3. 生成APP打包资源
4. 将打包资源做成zip包（扩展名改为wgt）
5. 上传wgt资源包到OSS

一键式操作，打包为wgt只需要执行：

```
yarn wgt
```

<a name="02b9ca25"></a>
## Android整包更新的自动化处理

Android整包更新需要在`AndroidManifest.xml`中配置：

```xml
<uses-permission android:name="android.permission.INSTALL_PACKAGES"/>
<uses-permission android:name="android.permission.REQUEST_INSTALL_PACKAGES"/>
```

Android整包更新的业务代码跟热更新一样，都可以调用`plus.runtime.install`来实现。

主要还是说一下打包apk的自动化脚本`build-apk.js`

```javascript
const fs = require('fs')
const { execSync } = require('child_process')

let app = require('../../app.json')
let manifest = require('../../src/manifest.json')

if (app.versionName !== manifest.versionName) {
  console.log('manifest.json和app.json的versionName不一致，请检查')
  return
}

if (app.versionCode !== manifest.versionCode) {
  console.log('manifest.json和app.json的versionCode不一致，请检查')
  return
}

// 获取build.gradle的版本名
let gradleFilePath = '../../platforms/android/app/build.gradle'
let data = fs.readFileSync(__dirname + '/' + gradleFilePath, {
  encoding: 'utf-8'
})

let reg = new RegExp(`versionName "${app.versionName}"`, "gm")

if (!reg.test(data)) {
  console.info('platforms/android/app/build.gradle的versionName不一致，请检查')
  return
}

let regCode = new RegExp(`versionCode ${app.versionCode}`, "gm")
if (!regCode.test(data)) {
  console.info('platforms/android/app/build.gradle的versionCode不一致，请检查')
  return
}

// 修改版本名
let appVersionName = app.versionName.split('.')
let manifestVersionName = manifest.versionName.split('.')

let appVersionLast = Number(appVersionName[2])
let manifestVersionLast = Number(manifestVersionName[2])

appVersionLast += 1
manifestVersionLast += 1

app.versionName = appVersionName[0] + '.' + appVersionName[1] + '.'  + appVersionLast
manifest.versionName = manifestVersionName[0] + '.'  + manifestVersionName[1] + '.'  + manifestVersionLast

console.log('====================');
console.log('newVersion：' + app.versionName + "." + app.versionCode);
console.log('====================');

let appJSON = JSON.stringify(app, null, 2)
let manifestJSON = JSON.stringify(manifest, null, 2)

// 替换项目版本名
let replaceFiles = [{
  path: '../../app.json',
  name: 'app.json',
  content: appJSON
}, {
  path: '../../src/manifest.json',
  name: 'manifest.json',
  content: manifestJSON
}]

replaceFiles.forEach(file => {
  fs.writeFileSync(__dirname + '/' + file.path, file.content, {
    encoding: 'utf-8'
  })
  console.log(file.name + ': 替换成功');
})

// 替换build.gradle的版本名
let result = data.replace(reg, `versionName "${app.versionName}"`)
fs.writeFileSync(__dirname + '/' + gradleFilePath, result, {
  encoding: 'utf-8'
})
console.log('platforms/android/build.gradle: 替换成功')

console.log('====================');

// 打包资源
console.log(execSync(`yarn build:app-plus-android`, { encoding: 'utf-8'}))

// 打包apk
console.log(execSync(`cd platforms/android && gradle assembleRelease`, { encoding: 'utf-8'}))

// 上传至OSS
let OSS = require('ali-oss');

function upToOss() {
  let client = new OSS({
    region: 'oss-cn-shenzhen',
    accessKeyId: 'your accessKeyId',
    accessKeySecret: 'your accessKeySecret'
  });

  client.useBucket('your bucketName');

  let ossBasePath = `apk`

  put(`${ossBasePath}/app-release.apk`, 'platforms/android/app/build/outputs/apk/release/app-release.apk')
  put(`${ossBasePath}/apks/${app.versionName}/app-release.apk`, 'platforms/android/app/build/outputs/apk/release/app-release.apk')
  put(`${ossBasePath}/apks/${app.versionName}/output.json`, 'platforms/android/app/build/outputs/apk/release/output.json')
  put(`webview/vod.html`, 'src/hybrid/html/vod.html')
  put(`${ossBasePath}/app.json`, 'app.json')

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

console.log('====================');
console.log('更新完毕，newVersion：' + app.versionName + "." + app.versionCode);
console.log('====================');
```

以上打包脚本，做了以下工作：

1. 验证版本号和版本名是否正确，如果不正确，终止脚本
2. 修改当前APP版本名
3. 生成APP打包资源
4. 打包Android APP（扩展名apk）
5. 上传apk到OSS

一键式操作，打包为apk只需要执行：

```
yarn apk
```

<a name="9fad6a62"></a>
## 安装更新

我们看看`plus.runtime.install`的官方文档：

```javascript
void plus.runtime.install(filePath, options, installSuccessCB, installErrorCB);
```

支持以下类型安装包：

1. 应用资源安装包（wgt），扩展名为'.wgt'；
2. 应用资源差量升级包（wgtu），扩展名为'.wgtu'；
3. 系统程序安装包（apk），要求使用当前平台支持的安装包格式。 注意：仅支持本地地址，调用此方法前需把安装包从网络地址或其他位置放置到运行时环境可以访问的本地目录。

知道了调用方式就好办了，我们封装一个检测更新的方法：

```javascript
class Utils {
  ...

  // 获取APP版本信息
  getVersion() {
    let {versionName, versionCode} = manifest
    return {
      versionName,
      versionCode,
      version: `${versionName}.${versionCode}`
    }
  }

  // 检测更新
  detectionUpdate(needRestartHotTip = false, needRestartFullTip = false) {
    return new Promise(async (resolve, reject) => {
      let appInfo = this.getVersion()
      uni.request({
          url: 'https://xxx.oss.com/apk/app.json',
          success: async (result) => {
            let { versionCode, versionName, appPath, wgtPath } = result.data
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

            // 判断版本名是否一致
            try {
              if (versionName === appInfo.versionName) {
                // 如果安装的版本号小于最新发布的版本号，则进行更新
                if (appInfo.versionCode < versionCode) {
                  // 下载wgt更新包
                  if (needRestartHotTip) {
                    uni.showModal({
                      title: '提示',
                      content: `检测到新版本 ${versionInfo.newestVersion} (当前版本：${versionInfo.currentVersion})，是否立即更新并重启应用，以使更新生效？`,
                      success: async (res) => {
                        if (res.confirm) {
                          await this.downloadAndInstallPackage(wgtPath)
                          plus.runtime.restart();
                          resolve({code: 1, data: versionInfo})
                        } else if (res.cancel) {
                          await this.downloadAndInstallPackage(wgtPath)
                          resolve({code: 1, data: versionInfo})
                        }
                      }
                    })
                  } else {
                    await this.downloadAndInstallPackage(wgtPath)
                    resolve({code: 1, data: versionInfo})
                  }
                } else {
                  resolve({code: 0, data: versionInfo})
                  console.log('你的版本为最新，不需要热更新');
                }
              } else {
                // 整包更新
                console.log('版本名不一致，请使用整包更新');
                if (needRestartFullTip) {
                  uni.showModal({
                    title: '提示',
                    content: `检测到新版本 ${versionInfo.newestVersion} (当前版本：${versionInfo.currentVersion})，是否立即更新应用？`,
                    success: async (res) => {
                      if (res.confirm) {
                        // await this.downloadAndInstallPackage(appPath)
                        plus.runtime.openURL(appPath)
                        resolve({code: 2, data: versionInfo})
                      } else if (res.cancel) {}
                    }
                  })
                } else {
                  // await this.downloadAndInstallPackage(appPath)
                  plus.runtime.openURL(appPath)
                  resolve({code: 2, data: versionInfo})
                }
              }
            } catch (e) {
              reject(e)
            }
          }
      });
    })
  }

  // 下载并安装更新包
  downloadAndInstallPackage(url) {
    console.log('开始下载更新包：' + url)
    return new Promise((resolve, reject) => {
      uni.downloadFile({
        url: url,
        success: (downloadResult) => {
          if (downloadResult.statusCode === 200) {
            console.log('正在更新...');
            plus.runtime.install(downloadResult.tempFilePath, {
              force: true // 强制更新
            }, function() {
              console.log('更新成功');
              resolve()
            }, function(e) {
              console.error('更新失败，错误原因：' + JSON.stringify(e));
              reject(e)
            });
          }
        }
      })
    })
  }
}

...
```

创建Utils的实例，并挂载到Vue的原型中，调用起来非常方便：

```javascript
  ...

  let res = await this.$utils.detectionUpdate(false, true)
  if (res.code === 1) {
    uni.showModal({
      title: '提示',
      content: `发现新的热更新包，是否立即重启APP以使更新生效？`,
      success: async (res) => {
        if (res.confirm) {
          plus.runtime.restart()
        } else if (res.cancel) {}
      }
    })
  }
```

```javascript
  ...

  let res = await this.$utils.detectionUpdate(true, true)
  if (res.code === 0) {
    let {currentVersion} = res.data
    uni.showModal({
      title: '提示',
      content: `你的APP为最新版本 ${currentVersion}，不需要更新！`,
      showCancel: false,
      success: async (res) => {
        if (res.confirm) {
        } else if (res.cancel) {}
      }
    })
  }
```

<a name="35808e79"></a>
## 参考资料

- [uni-app 资源在线升级/热更新](https://ask.dcloud.net.cn/article/35667)
- [uni-app 整包升级/更新方案](https://ask.dcloud.net.cn/article/34972)
- [app升级项目，新增强制更新（可静默），支持热更新（wgt），可支持高版本安卓系统](https://ext.dcloud.net.cn/plugin?id=237)
- [Android平台云端打包权限配置](https://ask.dcloud.net.cn/article/36982)
- [H5+：plus.runtime.install](http://www.html5plus.org/doc/zh_cn/runtime.html#plus.runtime.install)
