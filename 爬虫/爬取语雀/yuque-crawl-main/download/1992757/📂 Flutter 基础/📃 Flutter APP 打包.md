<a name="8QEc9"></a>
## Android APP 打包
打包命令：
```bash
flutter build apk
```

打包路径: `build\app\outputs\apk\release\app-release.apk`

然后进入到打包路径，执行以下命令安装到模拟器或真机：
```bash
adb install app-release.apk
```

<a name="M8UPH"></a>
### 应用打包后不能进行网络请求
在以下两个文件中加入：

- `android\app\src\profile\AndroidManifest.xml`
- `android/src/main/AndroidManifest.xml`

```xml
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```

<a name="hw0gm"></a>
### 图标修改
这就涉及到 Android 资源文件了, 其实跟 Flutter 没什么关系, 我们到 Android 资源目录将各种 mipmap 目录的 `ic_launcher.png` 替换即可, 默认为 `android/app/src/main/res/mipmap-xxx`

<a name="ec63339a"></a>
## flutter 包名修改
修改 `pubspec.yaml` 下的 `name` 字段, 并使用命令 `flutter packages get` 进行更新
```yaml
name: flutter_app_bootstrapper
```

引入包的时候使用：
```dart
import 'package:flutter_app_bootstrapper/pages/test/state.dart';
```

<a name="bwjWz"></a>
## App更新策略

...

<a name="S7xFJ"></a>
## 参考资料

- [Flutter打包release版本安卓apk包真机安装无法请求网络的解决方法](https://www.cnblogs.com/joe235/p/11492273.html)<br />
- [【Flutter】修改图标、应用名称、包名等](https://www.jianshu.com/p/8488b334926d)<br />
- [Flutter项目之app升级方案](https://blog.csdn.net/weixin_34122810/article/details/88016417)
- [Flutter开发 APP版本更新](https://msd.misuland.com/pd/3127746505234976194)
