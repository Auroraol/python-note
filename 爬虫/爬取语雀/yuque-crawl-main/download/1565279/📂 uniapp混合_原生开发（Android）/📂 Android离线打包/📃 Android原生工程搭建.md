<a name="VaqeV"></a>
## 准备工作

1. 到 [Android 离线SDK - 正式版](https://nativesupport.dcloud.net.cn/AppDocs/download/android) 下载最新的SDK
2. 解压后看到以下目录结构：

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603421652963-0f862425-2c85-4830-9ed2-cd9bb99d0d61.png#averageHue=%23faf8f7&height=253&id=QPsjo&originHeight=253&originWidth=644&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24964&status=done&style=none&title=&width=644)

3. 将 HBuilder-Hello 项目复制一份放到其他地方，使用Android Studio打开

<a name="f5050010"></a>
## 创建工程
<a name="DKaND"></a>
### 从示例项目中启动
可以直接将 `HBuilder-Hello`项目导入Android Studio，注意修改包名、Appid、AppKey等配置。

<a name="Stpww"></a>
### 从空项目中启动
参考：[Android离线打包配置](https://nativesupport.dcloud.net.cn/AppDocs/usesdk/android)

首先创建一个空的Android工程：

File | New | New Project...<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669182467382-057cc17b-93f1-455d-b9cb-ac675a1cedd8.png#averageHue=%23189889&clientId=u961b0b71-893c-4&from=paste&height=675&id=u300e1915&originHeight=675&originWidth=900&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74399&status=done&style=none&taskId=ua441b8ab-c8df-4dd3-84af-970d56d2f95&title=&width=900)

选择Empty Activity<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669182495354-fd8dedf4-5abb-471b-bbc1-ae07b1a3e711.png#averageHue=%233d4243&clientId=u961b0b71-893c-4&from=paste&height=680&id=u90a74fd5&originHeight=680&originWidth=899&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81819&status=done&style=none&taskId=u087501a0-a130-45d7-8eaf-8ff5ddcbe55&title=&width=899)

为自己的工程取个名字，并配置包名、工程路径等，点击Finish。创建好的工程结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669182621199-a5bb76d5-b911-421b-94d9-2816e2ff2a5f.png#averageHue=%233f464d&clientId=u961b0b71-893c-4&from=paste&height=338&id=u221216a7&originHeight=338&originWidth=336&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26538&status=done&style=none&taskId=ue91067f9-c8d1-4a55-aab8-d4ad38d3104&title=&width=336)

修改 `app/build.gradle`
```groovy
apply plugin: 'com.android.application'

android {
    compileSdkVersion 28
    buildToolsVersion '28.0.3'
    defaultConfig {
        applicationId "com.lizhiboxue.test"
        minSdkVersion 23
        targetSdkVersion 28

        versionCode 100
        versionName "1.0.0"
        multiDexEnabled true
        ndk {
            abiFilters 'x86','armeabi-v7a'
        }
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
    //使用uniapp时，需复制下面代码
    /*代码开始*/
    aaptOptions {
        additionalParameters '--auto-add-overlay'
        //noCompress 'foo', 'bar'
        ignoreAssetsPattern "!.svn:!.git:.*:!CVS:!thumbs.db:!picasa.ini:!*.scc:*~"
    }
    /*代码结束*/
}
repositories {
    flatDir {
        dirs 'libs'
    }
}
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.aar', '*.jar'], exclude: [])
    implementation "com.android.support:support-v4:28.0.0"
    implementation "com.android.support:appcompat-v7:28.0.0"
    /*uniapp所需库-----------------------开始*/
    implementation 'com.android.support:recyclerview-v7:28.0.0'
    implementation 'com.facebook.fresco:fresco:1.13.0'
    implementation "com.facebook.fresco:animated-gif:1.13.0"
    /*uniapp所需库-----------------------结束*/
    // 基座需要，必须添加
    implementation 'com.github.bumptech.glide:glide:4.9.0'
    implementation 'com.alibaba:fastjson:1.1.46.android'
}
```

包含以下改动：

1. 将其 targetSdkVersion 配置为28以下（为了适配Android Q，详见[适配Android10 / Android Q（API 29）](https://ask.dcloud.net.cn/article/36199)）
2. 将其 targetSdkVersion 配置为21以上，建议此属性值设为23，`io.dcloud.PandoraEntry` 作为apk入口时 必须设置 `targetSDKVersion>=21` 沉浸式才生效
3. minSdkVersion必须是19以上，uniapp才起作用
4. 添加 `ndk.abiFilters`，以支持指定的架构
5. 添加`aaptOptions`节点
6. 修改`dependencies`

<a name="xWEFe"></a>
#### 引入依赖
首先导入`HBuilder-Integrate-AS`项目中的`simpleDemo`模块<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194701119-2a353f7f-b809-43a7-accb-ae8a4b0268b3.png#averageHue=%233e444a&clientId=u17dba0d0-937d-4&from=paste&height=371&id=ub0b75f6c&originHeight=371&originWidth=600&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38638&status=done&style=none&taskId=ud581bfd1-f9d1-4130-9433-658c43ed990&title=&width=600)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194676669-fa179aaa-e626-4822-b496-ef0768d327c5.png#averageHue=%233c4042&clientId=u17dba0d0-937d-4&from=paste&height=570&id=u79f0806c&originHeight=570&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36330&status=done&style=none&taskId=u17c702f2-8b87-43b7-b484-9bcff027ded&title=&width=760)

可以看到以下结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194662529-e720faf8-9105-4aca-b3e7-2b47596d9d3e.png#averageHue=%233b4043&clientId=u17dba0d0-937d-4&from=paste&height=418&id=uc25c3ebd&originHeight=418&originWidth=354&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16483&status=done&style=none&taskId=ua0388eab-8c04-44a2-9239-a6460b22786&title=&width=354)

然后将`simpleDemo`模块中的`libs`复制到`app`模块中

<a name="INkhd"></a>
#### 引入资源
先将我们自己创建的项目中的src删掉，再将`simpleDemo`中的src复制覆盖到app模块中，可以看到以下目录结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194618755-2e7109bc-749c-44bd-8aad-a01081b10abb.png#averageHue=%233c4144&clientId=u17dba0d0-937d-4&from=paste&height=804&id=u16bf1d3b&originHeight=804&originWidth=388&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29928&status=done&style=none&taskId=u95bb0ba8-2b68-42f9-9490-b4c788de640&title=&width=388)

<a name="zLLHk"></a>
## 应用配置
<a name="PUWEI"></a>
### uniapp打包资源
在`assets`中，apps下存放了所有的应用，通过uniapp打包得到，以 `应用名/www` 的目录结构存放。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194554980-f64bb63f-b392-4255-99e0-0a75af08d378.png#averageHue=%233e4345&clientId=u17dba0d0-937d-4&from=paste&height=275&id=u9aa0dfd7&originHeight=275&originWidth=237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8651&status=done&style=none&taskId=ub1a6fcf9-76a0-40ce-a06b-e76adb1532a&title=&width=237)

可以看出，`www`目录存放的都是一些编译后的网页资源（没有编译也行，资源是由manifest.json指定）

其中 `data` 目录中的 `dcloud_control.xml` 可以指定特定的应用：

```xml
<hbuilder>
<apps>
    <app appid="HelloH5" appver=""/>
</apps>
</hbuilder>
```

注意这三处的对应：

- `assets/app`下的资源名
- `dcloud_control.xml`中的appid
- `manifest.json`中的id

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669182963034-4377312d-52da-4886-b2af-3d7255cfb9b7.png#averageHue=%23869975&clientId=u961b0b71-893c-4&from=paste&height=1036&id=u6dfa5bfc&originHeight=1036&originWidth=1267&originalType=binary&ratio=1&rotation=0&showTitle=false&size=147464&status=done&style=none&taskId=u456a60e1-184a-47a0-a5b9-3d99a5f0759&title=&width=1267)

<a name="AndroidManifest.xml"></a>
### AndroidManifest.xml
`AndroidManifest.xml`为应用程序清单，需要将启动页面指定为`io.dcloud.PandoraEntry`
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="io.dcloud.simple">

    <application
        android:allowBackup="true"
        android:allowClearUserData="true"
        android:icon="@drawable/icon"
        android:label="@string/app_name"
        android:largeHeap="true"
        android:supportsRtl="true">
        <activity
            android:name="io.dcloud.PandoraEntry"
            android:configChanges="orientation|keyboardHidden|keyboard|navigation"
            android:label="@string/app_name"
            android:launchMode="singleTask"
            android:hardwareAccelerated="true"
            android:theme="@style/TranslucentTheme"
            android:screenOrientation="user"
            android:windowSoftInputMode="adjustResize" >
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity
            android:name="io.dcloud.PandoraEntryActivity"
            android:launchMode="singleTask"
            android:configChanges="orientation|keyboardHidden|screenSize|mcc|mnc|fontScale|keyboard"
            android:hardwareAccelerated="true"
            android:permission="com.miui.securitycenter.permission.AppPermissionsEditor"
            android:screenOrientation="user"
            android:theme="@style/DCloudTheme"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <action android:name="android.intent.action.VIEW" />
                <data android:scheme="h56131bcf" />
            </intent-filter>
        </activity>

    </application>

</manifest>
```

之后集成各种资源的时候，还需要在 `AndroidManifest.xml` 中进行权限配置等操作。

<a name="geGQo"></a>
### 修改启动图
位于 `res`下的目录结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194796157-32ed26cc-7900-41ee-b3e2-d2aefe65734c.png#averageHue=%233e4244&clientId=ua4b79e3f-1eb5-4&from=paste&height=233&id=uefe5254f&originHeight=233&originWidth=283&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7077&status=done&style=none&taskId=u1e84b951-01b6-4768-b0fe-8cdada07300&title=&width=283)

在`drawable`下：

- `icon.png` 为应用的图标。
- `push.png` 为推送消息的图标。
- `splash.png` 为应用启动页的图标。

<a name="zhY4t"></a>
### 修改应用名
修改 `res/values/strings.xml` 的 app_name 字段为应用名称，比如：
```xml
<resources>
    <string name="app_name">uniapp-android</string>
</resources>
```

注意查看 `AndroidManifest.xml` 中 activity 的 `android:label` 属性值是否为 `@string/app_name`：
```xml
<activity
    android:name="io.dcloud.PandoraEntry"
    android:label="@string/app_name"
>
    ...
```

<a name="yRcb6"></a>
### 修改包名及应用版本
修改 `app/build.gradle` 中的 `applicationId` 字段：
```groovy
android {
    compileSdkVersion 26
    buildToolsVersion '28.0.3'
    defaultConfig {
        applicationId "com.example.test.Hello"
        minSdkVersion 19
        targetSdkVersion 26
        versionCode 100
        versionName "0.0.1"
    }
    ...
```

修改 `AndroidManifest.xml` 文件中的 package 属性值为应用包名，versionCode versionName 为版本, 比如:
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.example.test.Hello"
    android:versionCode="100"
    android:versionName="0.0.1"
>
    ...
```

修改 `AndroidManifest.xml` 中的 provider 节点下的 `android:authorities` 属性值为 `${applicationId}.<xxx>`，比如
```xml
<provider
    android:name="io.dcloud.common.util.DCloud_FileProvider"
    android:authorities="${applicationId}.fileprovider"
</provider>
```
可以使用替换：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422911726-a03c6b4a-30e1-46a4-83d3-59172dc2716a.png#averageHue=%233f464b&height=63&id=FMXEg&originHeight=63&originWidth=951&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11105&status=done&style=none&title=&width=951)
```
from： android:authorities="io.dcloud.HelloH5
to： android:authorities="${applicationId}
```

参考：[INSTALL FAILED CONFLICTING PROVIDER问题完美解决方案](https://www.jianshu.com/p/ad8c066e9166)

<a name="M02Jx"></a>
### 模块权限配置
模块权限配置参考：[模块配置 | uni小程序SDK](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/android.html#)、[VideoPlayer（视频播放） | uni小程序SDK](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/others.html)<br />[🎈 Feature-Android](https://www.yuque.com/xiaoyulive/uniapp/ebpug99seysz2b1s?view=doc_embed)

<a name="qyaZi"></a>
## AppKey、证书及打包配置
<a name="ne6NJ"></a>
### 通过Android Studio生成证书

1. 选择 `Build->Generate Signed Bundle/APK...`

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423363090-03687284-011a-4e1d-b1b8-fa58a26650d7.png#averageHue=%233e454d&height=309&id=OLAww&originHeight=309&originWidth=262&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14856&status=done&style=none&title=&width=262)

2. 选择APK

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423378046-e493784a-cb50-44fb-bd9f-bf9f52fb1164.png#averageHue=%233c4043&height=388&id=x6CY2&originHeight=388&originWidth=527&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18309&status=done&style=none&title=&width=527)

3. 选择“创建证书”

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423390668-ed63c6f9-4520-4042-9133-fce67df2368c.png#averageHue=%233e4245&height=393&id=sseWq&originHeight=393&originWidth=530&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16198&status=done&style=none&title=&width=530)

4. 输入证书内容，创建证书

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669183295397-7c87c7a6-fcbc-4925-bafc-5249c7cf1509.png#averageHue=%233f4345&clientId=u961b0b71-893c-4&from=paste&height=530&id=u6edd05b5&originHeight=530&originWidth=511&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21451&status=done&style=none&taskId=u0a87e02b-a555-439b-9cea-950151c77e1&title=&width=511)

:::info
注意记住证书密码
:::

<a name="lrUbR"></a>
### 通过命令创建证书
使用`keytool -genkey`命令生成证书：
```
keytool -genkey -alias testalias -keyalg RSA -keysize 2048 -validity 36500 -keystore test.keystore
```

参数说明：

- `testalias` 是证书别名，可修改为自己想设置的字符，建议使用英文字母和数字
- `test.keystore` 是证书文件名称，可修改为自己想设置的文件名称，也可以指定完整文件路径
- `36500` 是证书的有效期，表示100年有效期，单位天，建议时间设置长一点，避免证书过期

回车后会提示：
```bash
Enter keystore password:  //输入证书文件密码，输入完成回车  
Re-enter new password:   //再次输入证书文件密码，输入完成回车  
What is your first and last name?  
[Unknown]:  //输入名字和姓氏，输入完成回车  
What is the name of your organizational unit?  
[Unknown]:  //输入组织单位名称，输入完成回车  
What is the name of your organization?  
[Unknown]:  //输入组织名称，输入完成回车  
What is the name of your City or Locality?  
[Unknown]:  //输入城市或区域名称，输入完成回车  
What is the name of your State or Province?  
[Unknown]:  //输入省/市/自治区名称，输入完成回车  
What is the two-letter country code for this unit?  
[Unknown]:  //输入国家/地区代号（两个字母），中国为CN，输入完成回车  
Is CN=XX, OU=XX, O=XX, L=XX, ST=XX, C=XX correct?  
[no]:  //确认上面输入的内容是否正确，输入y，回车  

Enter key password for <testalias>  
(RETURN if same as keystore password):  //确认证书密码与证书文件密码一样（HBuilder|HBuilderX要求这两个密码一致），直接回车就可以
```

以上命令运行完成后就会生成证书，路径为命令行所在路径。

**注意：上述信息填写要规范，乱填有可能会影响应用上架应用市场。**

> 生成的证书扩展名为jks或keystore

:::info
注意记住证书密码
:::

<a name="ONL5N"></a>
### 在项目中配置证书签名
打开app模块下的 `build.gradle`，证书配置在 `buildTypes`选项中：
```groovy
signingConfigs {
    config {
        keyAlias 'key0'
        keyPassword '123456'
        storeFile file('test.jks')
        storePassword '123456'
        v1SigningEnabled true
        v2SigningEnabled true
    }
}
buildTypes {
    debug {
        signingConfig signingConfigs.config
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
    }
    release {
        signingConfig signingConfigs.config
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
    }
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669183727471-5da7a894-b882-4efe-8cbc-e713c68f16f0.png#averageHue=%23707a57&clientId=u961b0b71-893c-4&from=paste&height=870&id=ubbda9146&originHeight=870&originWidth=1224&originalType=binary&ratio=1&rotation=0&showTitle=false&size=142504&status=done&style=none&taskId=ue410d0d5-61b8-40a8-b2e7-b1030e62054&title=&width=1224)

这里通过`signingConfig`指向 `signingConfigs.config`节点的配置。

其中 `storeFile`可以是相对路径，也可以是绝对路径

- 相对路径是相对于`build.gradle`的路径
```
storeFile file('test.jks')
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669183981465-e672eae4-0c01-4487-b1ac-af658a8dde22.png#averageHue=%23fbfaf9&clientId=u961b0b71-893c-4&from=paste&height=380&id=ud51f8172&originHeight=380&originWidth=663&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26787&status=done&style=none&taskId=u68ce436a-8e81-43b7-aa32-19a5c7664c9&title=&width=663)

- 绝对路径是磁盘路径，如
```
storeFile file('D:/test.jks')
```
或：
```
storeFile file('D:\\test.jks')
```

<a name="njEMG"></a>
### 查看证书内容
<a name="ZK8s8"></a>
#### 通过命令行查看证书内容
```
keytool -v -list -keystore keystore.jks
```
输出示例：
```
Keystore type: PKCS12  
Keystore provider: SUN  

Your keystore contains 1 entry  

Alias name: android  
Creation date: 2021-4-12  
Entry type: PrivateKeyEntry  
Certificate chain length: 1  
Certificate[1]:  
Owner: CN=Android Debug, OU=Android, O=Android, L=HD, ST=BJ, C=CN  
Issuer: CN=Android Debug, OU=Android, O=Android, L=HD, ST=BJ, C=CN  
Serial number: 363bc393  
Valid from: Mon Apr 12 16:27:53 CST 2021 until: Wed Mar 19 16:27:53 CST 2121  
Certificate fingerprints:  
         MD5:  06:83:8C:C8:40:09:3B:9D:46:89:FC:41:9B:A1:A3:F3  
         SHA1: 97:C8:41:01:B9:14:1C:13:0D:D7:5D:74:28:A2:92:25:18:C3:6D:CD  
         SHA256: B0:1D:06:18:0D:00:3E:79:C7:B9:08:89:93:B8:E5:AE:7A:19:B0:DA:11:61:AA:09:7C:7F:39:8A:6F:51:4F:A7  
Signature algorithm name: SHA256withRSA  
Subject Public Key Algorithm: 2048-bit RSA key  
Version: 3
```

:::info
通过运行上面命令可能会缺少MD5信息，可以通过下面运行gradle命令的方式查看
:::

<a name="rG2NK"></a>
#### 通过gradle命令查看证书内容
运行 `signingReport`命令：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669184383890-28fcef41-d908-430d-9537-8601498459c0.png#averageHue=%233b4043&clientId=u5d604d98-1ed5-4&from=paste&height=535&id=ubdd5821e&originHeight=535&originWidth=517&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31411&status=done&style=none&taskId=u11a7ff80-c463-4736-8ff1-7f9c6ad9a50&title=&width=517)<br />输出：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669184461058-1dc9ad5d-3193-4a6a-ba39-6874d54eca3b.png#averageHue=%232e2d2c&clientId=u5d604d98-1ed5-4&from=paste&height=468&id=u3549b5ba&originHeight=468&originWidth=867&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59304&status=done&style=none&taskId=u935a5a4a-c77c-4115-9afc-dcebca80caf&title=&width=867)

如果没有`signingReport`命令，需要在设置中取消勾选"Do not build Gradle..."<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669184516348-5a3102f2-296d-4eb5-baab-fed808367543.png#averageHue=%233d4045&clientId=u5d604d98-1ed5-4&from=paste&height=712&id=u700c30fd&originHeight=712&originWidth=982&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39896&status=done&style=none&taskId=uf2aa8aae-81d1-4365-ac12-cc3010f95bd&title=&width=982)

<a name="fLNz7"></a>
### 获取离线打包AppKey
> 重要：**3.1.10版本起需要申请Appkey，否则运行后会报**
> <a name="Q45sG"></a>
#### "未配置AppKey或配置错误"
> 
> 参考：
> - [https://nativesupport.dcloud.net.cn/AppDocs/usesdk/appkey](https://nativesupport.dcloud.net.cn/AppDocs/usesdk/appkey)
> - [Android平台云端打包 - 公共测试证书 - DCloud问答](https://ask.dcloud.net.cn/article/36522)
> - [Android平台签名证书(.keystore)生成指南 - DCloud问答](https://ask.dcloud.net.cn/article/35777)


具体步骤如下：

1. 登录[开发者中心](https://dev.dcloud.net.cn/)
2. 在左侧菜单中选择我创建的应用，点击需要申请的应用

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669186397314-244cec27-a1dd-4d96-9bf9-7d2653aac85a.png#averageHue=%23fcfbfa&clientId=u5d604d98-1ed5-4&from=paste&height=255&id=u87dcfd36&originHeight=255&originWidth=1845&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34506&status=done&style=none&taskId=u1d0911f7-54ad-4ae3-ad5d-fcc5b0e2e2f&title=&width=1845)

3. 进入应用详情，打开“各平台信息”，新建一个配置，填写下面的信息

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669186509615-d2ac9002-7cb3-4dfe-ac5a-277b2f86fa00.png#averageHue=%23fcfbfb&clientId=u5d604d98-1ed5-4&from=paste&height=811&id=uf774e70f&originHeight=811&originWidth=878&originalType=binary&ratio=1&rotation=0&showTitle=false&size=65738&status=done&style=none&taskId=ubc34a180-e3cc-4e38-9812-0a7910496d7&title=&width=878)<br />其中，包名从`build.gradle`中获取<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669186583185-85d72847-2c76-4ab9-bd09-fc85ab010905.png#averageHue=%236c7a57&clientId=u5d604d98-1ed5-4&from=paste&height=647&id=u907d3b67&originHeight=647&originWidth=1085&originalType=binary&ratio=1&rotation=0&showTitle=false&size=105550&status=done&style=none&taskId=u4257c3f7-f081-4e3f-86ca-37e6cd070d0&title=&width=1085)<br />MD5、SHA1、SHA256签名从[上一步：查看证书内容](#njEMG)中获取。

4. 查看“离线打包Key”

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669186449463-2ad4a200-1496-4256-9d7d-755880367a33.png#averageHue=%23fdfcfc&clientId=u5d604d98-1ed5-4&from=paste&height=351&id=uee223a8b&originHeight=351&originWidth=1604&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32911&status=done&style=none&taskId=ub97c1b9f-ffe1-4324-bd69-714303d4a2f&title=&width=1604)<br />复制Android的你先打包App Key<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669186746411-0939ee0b-7d26-4c79-8d7d-3f96c314c0a7.png#averageHue=%23f0eeee&clientId=u5d604d98-1ed5-4&from=paste&height=547&id=u6c09b6bd&originHeight=547&originWidth=686&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29904&status=done&style=none&taskId=uce37f4cb-f48c-4cfc-91d6-02d2de285ba&title=&width=686)

5. 获取到android平台的AppKey后！打开Android项目 配置主APP的`Androidmanifest.xml`文件， 导航到Application节点，创建meta-data节点，name为dcloud_appkey，value为申请的AppKey如下：
```xml
<application
  ...>
  <meta-data
    android:name="dcloud_appkey"
    android:value="替换为自己申请的Appkey" />
```

<a name="imuPx"></a>
## 连接模拟器或真机
可以在Android Studio中启动模拟器<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669184699157-0630893e-67f2-4f6c-bfb1-d4709766ca2c.png#averageHue=%23404753&clientId=u5d604d98-1ed5-4&from=paste&height=315&id=u9554fea2&originHeight=315&originWidth=512&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21032&status=done&style=none&taskId=ue13e8752-c562-4483-a713-611e81983ed&title=&width=512)

连接真机：在开发者选项中勾选“USB调试”和“USB安装”<br />![20242d7552eef5563f4ae5539ab0761.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1669185022553-f6bc407d-6779-4d35-842c-32f1a6a7fc2a.webp#averageHue=%23fafafa&clientId=u5d604d98-1ed5-4&from=drop&height=907&id=uef78e666&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=98046&status=done&style=none&taskId=u2e15eecb-0fc5-458f-a667-df029701675&title=&width=408)<br />用USB数据线连接电脑后，弹出“允许USB调试”的选项，勾选确定<br />![c3c387764e9a4d103567b017ce31c69.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1669185189438-a71ab0a9-c32b-4b9d-8226-aa30e65767b7.webp#averageHue=%23828282&clientId=u5d604d98-1ed5-4&from=drop&height=927&id=Vwsvx&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=57646&status=done&style=none&taskId=u7d7f6210-813f-4c0e-a42d-69d6566ca8d&title=&width=417)<br />连接真机后，可以通过一下命令查看：
```
$ adb devices
List of devices attached
on7hd64lhunzvwl7        device
```
也可以在Android Studio的“Device Manager”中看到<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669185276915-f8b07a12-03f3-43f1-975b-4df8c243b615.png#averageHue=%233e4347&clientId=u5d604d98-1ed5-4&from=paste&height=200&id=udf60e292&originHeight=200&originWidth=494&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14644&status=done&style=none&taskId=u577bae2e-fa37-4636-bd33-3cd6dd0b1f9&title=&width=494)

<a name="PVpvT"></a>
### 安卓签名获取工具
直接通过一个apk，获取安装到手机的第三方应用签名的apk包。 详情：[https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html](https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html)


<a name="bbb46f49"></a>
## 启动程序
一切配置完毕，直接运行即可

模拟器：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194811454-93f994cd-ddf8-4904-8ced-0a4bcd2b1e40.png#averageHue=%23537963&clientId=ua4b79e3f-1eb5-4&from=paste&height=57&id=u0674d30c&originHeight=57&originWidth=501&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4629&status=done&style=none&taskId=u24fb37d6-9946-4ca5-a137-38b78525844&title=&width=501)

真机：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669185346628-89c2274a-0b8f-4a76-9fb0-244d0d8c8b76.png#averageHue=%23404446&clientId=u5d604d98-1ed5-4&from=paste&height=33&id=u215b2d82&originHeight=33&originWidth=668&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6574&status=done&style=none&taskId=u8ab90dd0-05df-4e54-836c-36a261db735&title=&width=668)

启动后：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669194842378-296e00ee-8666-4c7d-8062-ded9c68e3589.png#averageHue=%23f8edea&clientId=ua4b79e3f-1eb5-4&from=paste&height=808&id=u94a8e7c8&originHeight=808&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59245&status=done&style=none&taskId=ubdc3d670-c957-4b0d-abfa-57cb9861541&title=&width=408)

通过调试启动的应用在 `app\build\outputs\apk\debug\app-debug.apk`下

<a name="tKlv7"></a>
## 打包uniapp资源
首先，需要将本地cli项目升级到跟最新版SDK相同的版本：
```bash
yarn upgrade
```

打包本地项目，默认可以使用以下命令：
```bash
yarn build:app-plus
```
实际上是调用了：
```bash
cross-env NODE_ENV=production UNI_PLATFORM=app-plus vue-cli-service uni-build
```
如果需要指定资源生成路径，可以手动指定 `UNI_OUTPUT_DIR` 
```bash
cross-env NODE_ENV=production UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=./platforms/android/app/src/main/assets/apps/<appid>/www vue-cli-service uni-build
```

打包好的资源长这样：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422204187-c47fcbc8-6287-445c-ae55-46f94c38d5fe.png#averageHue=%236d8755&height=545&id=VEDUi&originHeight=545&originWidth=796&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94212&status=done&style=none&title=&width=796)

记住 `mainfest.json` 中的 appid，在Android原生工程的 `assets/apps` 中创建相同appid名称的目录，并创建一个www目录，结构如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422269525-82ae5815-267d-4191-a6dd-a223a6e13be9.png#averageHue=%233e444a&height=449&id=Cut8R&originHeight=449&originWidth=343&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16859&status=done&style=none&title=&width=343)

将打包好的资源全部拷到 `<appid>/www` 目录下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422304481-aa37ab85-9e6b-40f7-85ef-7714518c94ff.png#averageHue=%23faf9f7&height=435&id=RszJL&originHeight=435&originWidth=730&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52844&status=done&style=none&title=&width=730)

修改data/dcloud_control.xml文件中的appid为项目的appid：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422326045-2b65aebc-ea43-41a4-a726-cddb3f6c07e5.png#averageHue=%237b956c&height=367&id=r0qz8&originHeight=367&originWidth=1030&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34802&status=done&style=none&title=&width=1030)

如果不嫌麻烦，也可以通过HBuilderX打包资源（不推荐）：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603422542590-9c19da1f-a977-457a-878d-05e38d739d1d.png#averageHue=%23fcf9ee&height=379&id=aZR84&originHeight=379&originWidth=478&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30005&status=done&style=none&title=&width=478)

<a name="Lrszg"></a>
## 签名打包发行

1. 选择 `Build->Generate Signed Bundle/APK...`

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423363090-03687284-011a-4e1d-b1b8-fa58a26650d7.png#averageHue=%233e454d&height=309&id=sCsDF&originHeight=309&originWidth=262&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14856&status=done&style=none&title=&width=262)

2. 选择APK

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423378046-e493784a-cb50-44fb-bd9f-bf9f52fb1164.png#averageHue=%233c4043&height=388&id=WZNlx&originHeight=388&originWidth=527&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18309&status=done&style=none&title=&width=527)

3. 如果没有证书，选择“创建证书”，如果已经有了证书，则可以选择已有证书

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423390668-ed63c6f9-4520-4042-9133-fce67df2368c.png#averageHue=%233e4245&height=393&id=gpzUY&originHeight=393&originWidth=530&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16198&status=done&style=none&title=&width=530)

4. 选择证书后，选择打包类型为release或debug，Signature Versions建议都选，点击Finish

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423407165-a027edc6-1aca-4b2e-800b-c0590d73683d.png#averageHue=%233d4247&height=393&id=QzqZK&originHeight=393&originWidth=528&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17373&status=done&style=none&title=&width=528)

5. 打包成功后的apk：

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423419182-6176ae74-c145-4904-b289-315a875f407a.png#averageHue=%23f8f7f7&height=126&id=k5DDN&originHeight=126&originWidth=613&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10451&status=done&style=none&title=&width=613)<br />默认apk生成路径为 `app/release` ，如果是debug版本为 `app/debug`

参考：

- [Android打包发行配置](https://nativesupport.dcloud.net.cn/AppDocs/package/android)
- [Android平台云端打包 - 公共测试证书 - DCloud问答](https://ask.dcloud.net.cn/article/36522)


<a name="Prg3X"></a>
## 关于自定义基座
在调试的时候，我们通产会使用自定义基座进行调试，如果使用默认基座，在调试多个应用的时候会出现应用相互覆盖的情况。

自定义基座可以使用上面打包好的APK，将其复制到 `dist\debug\android_debug.apk` 即可：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423314626-f898d7af-84e1-4712-8a13-340524970f71.png#averageHue=%23262729&height=132&id=zxFSx&originHeight=132&originWidth=219&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6459&status=done&style=none&title=&width=219)

实际上，自定义基座的作用是为了区分不同包名的应用，因为默认基座的包名是确定的：`io.dcloud.HBuilder`, 因此才会出现相互覆盖的情况。

说到这，其实使用HBuilderX在线打包的话，有一个非常不错的地方：可以任意修改包名。而离线打包可能改包名就比较麻烦了。

<a name="Y8F4u"></a>
## 安装apk时的错误处理
我在安装打包好的apk时，出现了以下错误：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603423546279-c8dc8294-e862-463d-bd09-8126687a248f.png#averageHue=%232456b0&height=515&id=ojxMK&originHeight=515&originWidth=1414&originalType=binary&ratio=1&rotation=0&showTitle=false&size=909428&status=done&style=none&title=&width=1414)

<a name="FNewB"></a>
### more than one device/emulator
错误原因：有多个真机/模拟器连接到电脑。<br />解决方案：断开多余的真机/ 模拟器，只留一个。

<a name="DrfMf"></a>
### INSTALL_FAILED_UPDATE_INCOMPATIBLE
错误原因：模拟器中包含一个相同的应用，但签名不同。一般是由于之前安装过测试版本的apk，导致安装正式版本的apk时签名不一致。<br />解决方案：卸载掉之前安装的测试版本。

<a name="wWWD3"></a>
### INSTALL_FAILED_DUPLICATE_PERMISSION
错误原因：已经有其他app申请过这个权限，导致权限重复。一般是由于之前安装过默认项目中的 HBuilder-Hello。<br />解决方案：卸载掉HBuilder-Hello。

<a name="trZH4"></a>
### INSTALL_FAILED_ALREADY_EXISTS
错误原因：重新签名后再次安装会出错。<br />解决方案：使用 `adb install -r xxx.apk` 进行安装。

<a name="VwPBY"></a>
### INSTALL_FAILED_TEST_ONLY
错误详情：
```
$ adb install app-debug.apk
Performing Streamed Install
adb: failed to install app-debug.apk: Failure [INSTALL_FAILED_TEST_ONLY: installPackageLI]
```

错误原因：Android Studio 3.0会在debug apk的manifest文件application标签里自动添加 `android:testOnly="true"`属性。


解决方法一：在项目中的gradle.properties全局配置中设置：
```
android.injected.testOnly=false
```
解决方法二：安装时加 `-t`： 
```
adb install -t app-debug.apk
```

参考：

- [INSTALL_FAILED_TEST_ONLY的原因_fuchenxuan的博客-CSDN博客_install_failed_test_only](https://blog.csdn.net/vfush/article/details/80320596)


<a name="mPuVs"></a>
### 未配置appkey或配置错误
运行时报错：<br />![510bf652c5c0560e3e8fd7cf5df3485.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1669255111549-0c7e6837-124b-4e64-8d87-3ed059b2610d.webp#averageHue=%2369988e&clientId=ua54df096-dd82-4&from=drop&height=858&id=udac227f8&originHeight=2400&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13574&status=done&style=none&taskId=u8d0d49bc-2471-4484-8e61-0c338d47406&title=&width=386)

解决方案：参考[获取离线打包AppKey](#fLNz7)


<a name="RpqzA"></a>
### HBuilderX打包的app安装时报毒
安装时报毒详情：<br />![30{5GC)]7TK}VBI)MR3EX8K.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/2213540/1669253018640-b19334c0-cdf0-4c66-95b5-d5d719893b7a.jpeg#averageHue=%23ebebe2&clientId=ua54df096-dd82-4&from=drop&height=889&id=u7b090e39&originHeight=1920&originWidth=864&originalType=binary&ratio=1&rotation=0&showTitle=false&size=133076&status=done&style=none&taskId=u73615973-ccc1-407e-932a-1eaaf846665&title=&width=400)

原因：使用了DCloud的公测证书。公共测试证书一旦被某个非法app使用过，某些不靠谱的检测平台，就会把所有使用公共测试证书的app都报病毒。

rom弹风险软件的原理：某个app被确定为非法软件，rom会把它的包名、证书、权限清单列入观察名单，在相似的app安装时弹框提醒用户。

解决方案：不要使用公共测试证书发正式应用。公共测试证书一旦被某个非法app使用过，某些不靠谱的检测平台，就会把所有使用公共测试证书的app都报病毒。请使用自己的证书。

参考：

- [关于android 应用在手机安装提示存在风险问题的解决方案 - DCloud问答](https://ask.dcloud.net.cn/article/37501)
- [HBuilderX打包的app腾讯手机管家报毒问题,打包总是提示报毒_weixin_42220130的博客-CSDN博客](https://blog.csdn.net/weixin_42220130/article/details/118090214)

<a name="GGmay"></a>
### uni-app运行环境版本和编译器版本不一致的问题
HBuilderX1.7.0及以上版本uni-app添加了运行环境版本和编译环境版本的校验机制，当两个版本不一致时会弹出以下提示：<br />![11de0789ae46a4ea0afcef2fb292715d.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669253881571-9d319fa4-4092-415b-b6ea-88ee00edb56f.png#averageHue=%23373737&clientId=ua54df096-dd82-4&from=drop&id=u4b7e7dc3&originHeight=304&originWidth=400&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49480&status=done&style=none&taskId=ub71136c5-460e-42c4-8afe-651556c60f4&title=)

- “手机端SDK版本”：是指5+Runtime的版本号。云打包提交云端打包时确定的，也就是说生成apk/ipa之后，APP运行环境就不会改变了。离线打包时是你下载的sdk的版本。只有默认真机运行基座、云打包机的引擎是和HBuilderX升级而自动升级的。如果你使用了自定义基座、sdk离线打包，需要手动升级，或者重新用新版制作自定义基座，或者下载最新版sdk。
- “HBuilderX版本”：如果项目是HBuilderX创建的，则是HBuilderX的版本号，更新HBuilderX会改变；如果是cli创建的项目，即根目录是package.json，那么编译环境版本号是创建cli时生成的，或者上一次执行npm update生成的。不管HBuilderX如何升级，cli项目的编译器并不会跟随HBuilderX升级而升级，需手动升级。

**什么时候会出现这种问题？**

- 情况1：HBuilderX版本很老，或cli编译器一直没升级，而云打包服务器已经升级，此时编译环境版本低，而运行环境版本高，就会报错。
- 情况2：使用老版HBuilderX打包了App后，后来使用新版HBuilderX或新版cli制作了wgt升级包。此时编译环境会高于运行环境，也会报错。
- 情况3：使用了cli或自定义基座或本地打包，虽然HBuilderX升级了，但这些配套并没有手动升级，也是报错。
- 情况4：如果HBuilderX版本高于SDK版本，有可能是HBuilderX在升级时出现问题，手机端基座没有升级成功。如果是这种情况，在插件管理里卸载“真机运行插件”，然后重新安装这个插件。

**出现问题该怎么办？**

1. 比较简单的就是全部升级，保持HBuilderX、自定义基座、cli项目编译器都是最新版。
2. wgt升级时遇到这个问题，首先你可以自测，看老的运行引擎和新版编译器编的wgt是否搭配，如果测试有问题，那不能使用wgt升级，请使用整包升级。如果测试正常，可以在manifest.json文件的源码视图中配置忽略这个提醒，在“app-plus”->"compatible" 节点下添加配置 方式如下：

<br />HBuilderX1.9.0及以上版本新增以下配置避免弹出提示框：
```json
//...  
"app-plus": {  
  "compatible": {  
    "ignoreVersion": true //true表示忽略版本检查提示框，HBuilderX1.9.0及以上版本支持  
  },  
  //....  
},  
//...
```
以下方法可针对指定版本避免弹出提示框：
```json
//...  
"app-plus": {  
  "compatible": {  
    "runtimeVersion": "1.7.0", //根据实际情况填写  
    "compilerVersion": "1.7.1" //根据实际情况填写  
  },  
  //....  
},  
//...
```

- "runtimeVersion"字段值表示应用兼容的uni-app运行环境版本号，可以配置多个版本号（使用英文字符,分隔）
- "compilerVersion"字段值表示编译环境版本号，通常配置当前HBuilderX的版本号或cli编译器版本即可（不可以配置多个）

参考：[uni-app运行环境版本和编译器版本不一致的问题 - DCloud问答](https://ask.dcloud.net.cn/article/35627)

<a name="D22EL"></a>
## 参考资料

- [App离线打包：Android 原生工程配置](https://nativesupport.dcloud.net.cn/AppDocs/usesdk/android)
- [HBuilderX生成本地打包App资源](https://ask.dcloud.net.cn/question/60254)
- [DCloud appid 用途/作用/使用说明](https://ask.dcloud.net.cn/article/35907)
