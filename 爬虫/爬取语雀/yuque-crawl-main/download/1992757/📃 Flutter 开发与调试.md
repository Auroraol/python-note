<a name="9e6adf50"></a>
## 一、开发环境搭建
<a name="teSF1"></a>
### Windows环境配置

1. 首先设置两个环境变量

```bash
setx PUB_HOSTED_URL https://pub.flutter-io.cn
setx FLUTTER_STORAGE_BASE_URL https://storage.flutter-io.cn
```

2. [点击下载](https://flutter.io/sdk-archive/#windows) 最新可用的 flutter 安装包, 或者克隆Flutter代码仓库：
```bash
git clone --depth=1 https://github.com/flutter/flutter.git -b stable

# or 换源拉取
git clone --depth=1 https://hub.fastgit.org/flutter/flutter.git -b stable
```

3. 下载完成后，解压并将 bin 目录添加到 PATH 环境变量

<a name="8Hx9H"></a>
## 二、换源
官方提供的国内镜像
```bash
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```

上海交大镜像
```bash
export PUB_HOSTED_URL=https://dart-pub.mirrors.sjtug.sjtu.edu.cn/
export FLUTTER_STORAGE_BASE_URL=https://mirrors.sjtug.sjtu.edu.cn/
```

清华镜像
```bash
export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub"
export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"
```

相关的镜像站点如下：

- [dart-pub 清华镜像](https://mirror.tuna.tsinghua.edu.cn/help/dart-pub/)
- [dart-pub 上海交大镜像](https://dart-pub.mirrors.sjtug.sjtu.edu.cn/)
- [flutter 清华镜像](https://mirror.tuna.tsinghua.edu.cn/help/flutter/)
- [pub.dev](https://pub.flutter-io.cn/)

<a name="39da6755"></a>
## 三、创建项目
使用以下命令创建项目：
```bash
flutter create flutterTest
```

项目名称只能有小写字母及下划线

<a name="fa4aa1b9"></a>
## 四、运行项目
运行前先检查是否有可用的模拟器：
```bash
$ flutter devices
1 connected device:

M2004J7AC (mobile) • on7hd64lhunzvwl7 • android-arm64 • Android 10 (API 29)
```

显示以上的信息说明有可用的设备。

使用以下命令运行项目：
```bash
flutter run
flutter run --trace-startup --profile # 统计应用启动时间
```

注意以下热更新的提示：
```
To hot reload changes while running, press "r". To hot restart (and rebuild state), press "R".
For a more detailed help message, press "h". To detach, press "d"; to quit, press "q".
```

热更新输入 `r`，热重启输入 `R`。<br />![001.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605079608093-23d04391-d26d-4efa-96f6-89cd9e0e3d88.png#align=left&display=inline&height=624&originHeight=835&originWidth=455&size=22993&status=done&style=none&width=340)

<a name="e2db3b96"></a>
## 五、开发工具
<a name="7hf3y"></a>
### 使用VSCode开发与调试

1. 在 VSCode 中安装 Dart 和 Flutter 插件

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605062629501-4b16037b-242c-4834-8ae6-246305e272fe.png#align=left&display=inline&height=156&originHeight=156&originWidth=750&size=23299&status=done&style=none&width=750)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605062606639-72845dfd-0291-4269-b06f-c5dbc5b2c005.png#align=left&display=inline&height=153&originHeight=153&originWidth=746&size=22982&status=done&style=none&width=746)

2. 按 F5 键或调用 `Debug>Start Debugging` 运行调试

![002.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605079663436-bccd145d-80f3-4d01-bcbf-5f84594dd7cd.png#align=left&display=inline&height=680&originHeight=680&originWidth=1408&size=103205&status=done&style=none&width=1408)

3. 变更 `lib/main.dart` 文件，将可以看到热更新效果

<a name="OZy4z"></a>
### 使用Android Studio开发与调试

1. 安装 Flutter 和 Dart 插件

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605062543773-bad5c6b5-1f32-4daf-8df6-d54af27374f6.png#align=left&display=inline&height=250&originHeight=250&originWidth=971&size=46143&status=done&style=none&width=971)

2. 创建Flutter项目

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608081105546-ca58d927-6fec-43af-9d73-264d920fb6ca.png#align=left&display=inline&height=112&originHeight=223&originWidth=522&size=35812&status=done&style=none&width=261)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608081363325-7b8df86e-f974-4f00-a869-ff8a7679ddcf.png#align=left&display=inline&height=325&originHeight=650&originWidth=900&size=58358&status=done&style=none&width=450)

3. 可以看到工具栏有相关的调试选项

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605062727027-71265d49-2d88-4d69-8981-149501c12f2d.png#align=left&display=inline&height=375&originHeight=375&originWidth=1914&size=128339&status=done&style=none&width=1914)

<a name="b2b4597c"></a>
## 六、问题检测
如果不能够正常运行, 可以通过以下命令检测问题：
```bash
$ flutter doctor --verbose
[√] Flutter (Channel stable, v1.7.8+hotfix.4, on Microsoft Windows [Version 10.0.17134.950], locale zh-CN)
    • Flutter version 1.7.8+hotfix.4 at D:\Software\flutter
    • Framework revision 20e59316b8 (5 weeks ago), 2019-07-18 20:04:33 -0700
    • Engine revision fee001c93f
    • Dart version 2.4.0

[√] Android toolchain - develop for Android devices (Android SDK version 28.0.3)
    • Android SDK at D:/Software/android-sdk
    • Android NDK location not configured (optional; useful for native profiling support)
    • Platform android-Q, build-tools 28.0.3
    • ANDROID_HOME = D:/Software/android-sdk
    • Java binary at: C:\Program Files\Android\Android Studio\jre\bin\java
    • Java version OpenJDK Runtime Environment (build 1.8.0_152-release-1343-b01)
    • All Android licenses accepted.

[√] Android Studio (version 3.4)
    • Android Studio at C:\Program Files\Android\Android Studio
    • Flutter plugin version 38.1.1
    • Dart plugin version 183.6270
    • Java version OpenJDK Runtime Environment (build 1.8.0_152-release-1343-b01)

[√] IntelliJ IDEA Ultimate Edition (version 2018.3)
    • IntelliJ at C:\Program Files\JetBrains\IntelliJ IDEA 2018.3.4
    • Flutter plugin version 38.1.1
    • Dart plugin version 183.6270

[√] VS Code (version 1.37.1)
    • VS Code at C:\Users\quanzaiyu\AppData\Local\Programs\Microsoft VS Code
    • Flutter extension version 3.3.0

[√] Connected device (1 available)
    • Android SDK built for x86 • emulator-5554 • android-x86 • Android 7.0 (API 24) (emulator)

• No issues found!
```

有的时候，通过此命令运行，会看到以下警告，但自己的Android Studio明明已经安装好了相关插件，这时就不用理他了，能正常使用。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605062446726-81a0568f-31b8-4e7d-8474-72431e910832.png#align=left&display=inline&height=330&originHeight=330&originWidth=1185&size=615409&status=done&style=none&width=1185)

<a name="b7c0bfff"></a>
## 七、调试技巧
<a name="debugger"></a>
### debugger
```dart
import 'dart:developer';
debugger();

// 带条件调试
void someFunction(double offset) {
  debugger(when: offset > 30.0);
  // ...
}
```

<a name="print"></a>
### print
```dart
print()
debugPrint()
```

<a name="c7ee60cc"></a>
### Dart DevTools
在 Android Studio 的 Run 中可以看到:<br />打开后可以在浏览器看到：<br />![003.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608025791916-39a7575e-1ddc-4168-af8e-536c2e455580.png#align=left&display=inline&height=375&originHeight=375&originWidth=836&size=21748&status=done&style=none&width=836)

Dart DevTools<br />![001.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608025805868-19df50d0-fd1f-4531-810d-566ad7ac2b4f.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1918&size=113397&status=done&style=none&width=1918)

Dart VM Observatory<br />![002.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608025817697-4ede7fce-f4a1-4cc8-94fe-5857a41fd2bf.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1918&size=90231&status=done&style=none&width=1918)

<a name="f0f38ebd"></a>
### 其他调试相关的命令
```bash
flutter analyze # 代码分析
flutter logs # 查看控制台输出的日志
```

