<a name="8a8e77a0"></a>
## 当前运行环境无法运行启用“自定义组件模式”的uni-app应用
HBuilderX1.9.0及以上版本uni-app项目启用“自定义组件模式”，运行为APP时做了底层性能优化，可能出现兼容性问题引起白屏现象。

HBuilderX1.9.4及以上版本会自动检查基座环境是否支持启用“自定义组件模式”，如果不支持则会弹出以下提示框

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069773139-c34a7b1f-f4f6-4b42-b851-4ebd4da95dec.png#averageHue=%233f3f3f&clientId=u765cde56-2c30-4&from=paste&height=300&id=u7522b712&originHeight=300&originWidth=476&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56502&status=done&style=none&taskId=ucbda9746-eb86-4f3f-9ce0-cf8f7daad64&title=&width=476)

Android端解决方案：<br />将`uniapp-release.aar`放于`app/libs`目录下，并在`app/build.gradle`中添加以下依赖：
```groovy
dependencies {
    implementation fileTree(include: ['*.jar'], dir: 'libs')
    implementation fileTree(include: ['*.aar'], dir: 'libs')
    implementation 'com.android.support:appcompat-v7:26.1.0'
    implementation 'com.android.support.constraint:constraint-layout:1.1.3'
    /*uniapp所需库-----------------------开始*/
    implementation 'com.android.support:recyclerview-v7:26.1.0'
    implementation 'com.facebook.fresco:fresco:1.13.0'
    implementation "com.facebook.fresco:animated-gif:1.13.0"
    /*uniapp所需库-----------------------结束*/
    // 基座需要，必须添加
    implementation 'com.github.bumptech.glide:glide:4.9.0' // 基座依赖
    implementation 'com.alibaba:fastjson:1.1.46.android'
}
```

参考：

- [当前运行环境无法运行启用“自定义组件模式”的uni-app应用问题](https://ask.dcloud.net.cn/article/35877)
- [uni-app离线打包Android平台注意事项](https://ask.dcloud.net.cn/article/35139)

<a name="8e4e7a0b"></a>
## uni-app运行环境版本和编译器版本不一致
HBuilderX1.7.0及以上版本uni-app添加了运行环境版本和编译环境版本的校验机制，当两个版本不一致时会弹出以下提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069790926-3650512a-414b-4875-af53-8995d62514d1.png#averageHue=%23474747&clientId=u765cde56-2c30-4&from=paste&height=317&id=u9c3879bb&originHeight=317&originWidth=416&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55070&status=done&style=none&taskId=ue084422d-b96e-4238-b970-059a90ee8ba&title=&width=416)

名词解释：<br />**手机端SDK版本：**是指5+Runtime的版本号。云打包提交云端打包时确定的，也就是说生成apk/ipa之后，APP运行环境就不会改变了。离线打包时是你下载的sdk的版本。只有默认真机运行基座、云打包机的引擎是和HBuilderX升级而自动升级的。如果你使用了自定义基座、sdk离线打包，需要手动升级，或者重新用新版制作自定义基座，或者下载最新版sdk。

下图为离线打包时的SDK版本号：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069806795-987bed9c-7cb4-471d-a7d4-4e0d1e4bd226.png#averageHue=%23faf9f8&clientId=u765cde56-2c30-4&from=paste&height=296&id=ue0c964e4&originHeight=296&originWidth=719&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28169&status=done&style=none&taskId=uc1a27a84-b029-40dc-b197-378fab5dec4&title=&width=719)

**HBuilderX版本：**如果项目是HBuilderX创建的，则是HBuilderX的版本号，更新HBuilderX会改变；如果是cli创建的项目，即根目录是`package.json`，那么编译环境版本号是创建cli时生成的，或者上一次执行`npm update`生成的。不管HBuilderX如何升级，cli项目的编译器并不会跟随HBuilderX升级而升级，需手动升级。

下图为HBuilderX的版本号<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069818254-00693fd7-b304-45bc-9bcf-5a7adc8b9655.png#averageHue=%23ebeae8&clientId=u765cde56-2c30-4&from=paste&height=178&id=u848d813a&originHeight=178&originWidth=323&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6671&status=done&style=none&taskId=u2ed9efc1-74b9-4a0b-82d9-60f30e5d393&title=&width=323)

找了半天cli的版本，不知道在哪，经过仔细观察，应该是这个了：[@dcloudio/vue-cli-plugin-uni](https://www.npmjs.com/package/@dcloudio/vue-cli-plugin-uni)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069830267-f2942263-5c76-485e-8ada-e9a05c2ce6e9.png#averageHue=%23fbfaf9&clientId=u765cde56-2c30-4&from=paste&height=244&id=u288b2426&originHeight=244&originWidth=688&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35622&status=done&style=none&taskId=u4bb19d8e-d435-465f-85df-51f68693ea2&title=&width=688)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671069843383-80d8d7fc-3e33-41ee-b397-6d50e26ab396.png#averageHue=%23332f2e&clientId=u765cde56-2c30-4&from=paste&height=327&id=u11ce72a1&originHeight=327&originWidth=756&originalType=binary&ratio=1&rotation=0&showTitle=false&size=171921&status=done&style=none&taskId=u822317a3-1d6c-4f9b-a65a-445b750c7df&title=&width=756)

将其拆一下，就成了：
```
2.6.9.20200424005
```

吐槽：uni-app的版本是个迷，版本号不规范到了极点，哎，脑阔疼。

解决方案：<br />如果使用本地打包，确保本地的SDK的版本号与cli或HX的版本号一致。

如果使用云端打包，如果正式打包，版本号将与云端SDK版本号一致；如果使用自定义基座，版本号将与你系统中的HX版本号一致）。

如果想要忽略提示，可以在`manifest.json`中配置：
```json
{
    ...
    "app-plus" : {
        ...
        "compatible": {
            "ignoreVersion": true //true表示忽略版本检查提示框，HBuilderX1.9.0及以上版本支持
        },
    },
}
```

以下方法可针对指定版本避免弹出提示框。
```json
{
  "app-plus": {  
    "compatible": {  
      "runtimeVersion": "1.7.0", //根据实际情况填写  
      "compilerVersion": "1.7.1" //根据实际情况填写  
    }
  }
}
```

- `"runtimeVersion"`字段值表示应用兼容的uni-app运行环境版本号，可以配置多个版本号（使用英文字符,分隔）
- `"compilerVersion"`字段值表示编译环境版本号，通常配置当前HBuilderX的版本号或cli编译器版本即可（不可以配置多个）

参考：

- [uni-app运行环境版本和编译器版本不一致的问题](https://ask.dcloud.net.cn/article/id-35627)

<a name="465b47a0"></a>
## exception function:createInstance
错误详情：
```
[ERROR] reportJSException >>>> exception function:createInstance, exception:Exception: TypeError: undefined is not an object (evaluating 'location.host')
```

错误原因：在浏览器端，使用window、location等浏览器对象（BOM）是允许的，但是在Android端，并不能使用这些API，可以使用条件编译进行处理。

网上看到一个类似的错误是：在uni-app中,props是无法访问this的，而在h5中是可以的，所以这个错误会在uni-app的APP端出现，而h5是正常的。详情参见：[[ERROR] reportJSException >>>> exception function:createInstance, exception:Exception: TypeError: undefined is not an object (evaluating 'this.$tokenInfoObj')](https://blog.csdn.net/weixin_43343144/article/details/98085487)

<a name="nFjJh"></a>
## 定位居中问题
发现如果在模板中使用了定位居中，在APP中是不生效的：
```javascript
view(class="fixed z-200 top-0 left-0 right-0 bottom-0 bg-red")
	view(class="absolute w-500 h-400 center top-50% left-50% translate--50% bg-white") 123
```
（样式使用了UnoCSS/Tailwindcss，其中center包括了flex、justify-center、items-center）<br />这样写，编译到H5/小程序均无问题，但是在APP上定位就失效了（这是魔法吗？）


解决方案：把居中元素的定位去掉，改用flex让子元素居中
```javascript
view(class="fixed z-200 top-0 left-0 right-0 bottom-0 center" style="background: rgba(0,0,0,.8);")
  view(class="w-500 h-400 center bg-white") 123
```

如果是一个遮罩，可以与其他元素同级放置：
```javascript
// 遮罩
view(class="fixed z-200 top-0 left-0 right-0 bottom-0 center" style="background: rgba(0,0,0,.8);")
  view(class="w-500 h-400 center bg-white") 123
// 页面内容
Layout
  view(class="w-100 h-100 bg-red") 456
```

<a name="UFTpD"></a>
## 打包时缺少xxx模块
错误提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1671072913494-7f9c644b-e04f-49b5-bc87-628fa72068e2.png#averageHue=%23c8c8c8&clientId=ua3cc31ec-cdb3-4&from=paste&height=995&id=u5b6edb46&originHeight=995&originWidth=462&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71572&status=done&style=none&taskId=u2bed0664-6616-4f3d-bece-530a0770543&title=&width=462)

如果是离线工程打包App，iOS 工程请参考这个[教程](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/iOSModuleConfig/common) ，Android 工程参考这个 [教程](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/android)。

参考链接：[5+App模块配置错误处理 - DCloud问答](https://ask.dcloud.net.cn/article/283)




