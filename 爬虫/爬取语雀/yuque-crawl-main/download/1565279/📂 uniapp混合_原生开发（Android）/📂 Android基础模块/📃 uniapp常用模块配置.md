<a name="PM9bK"></a>
## 拨打电话及通讯录权限配置
在`AndroidManifest.xml`中配置：
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <uses-permission android:name="android.permission.READ_CONTACTS"/>
  <uses-permission android:name="android.permission.WRITE_CONTACTS"/>
  <uses-permission android:name="android.permission.CALL_PHONE"/>
</manifest>
```

<a name="Cev6V"></a>
## 集成X5 Webview
| 路径 | 文件名 |
| --- | --- |
| SDK/libs | webview-x5-release.aar、weex_webview-x5-release.aar |

X5不需要单独添加配置，直接拷贝上述文件到libs下即可。

参考：

- [X5 Webview 配置 | uni小程序SDK](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/x5.html)
- [uni-app官网](https://uniapp.dcloud.net.cn/tutorial/app-android-x5.html#)



