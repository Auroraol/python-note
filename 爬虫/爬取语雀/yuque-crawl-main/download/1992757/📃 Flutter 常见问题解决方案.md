<a name="owb3I"></a>
## 安装Dart出错
安装 Dart 的时候提示：
```
Downloading Dart SDK from Flutter engine 9bfa4f53cdbec57b0c3badc47bc13da145816c8d...
Unknown operating system. Cannot install Dart SDK.
```

解决方案: 到 flutter 的 bin 目录下执行：
```bash
flutter.bat doctor
```

如果是网络问题，导致无法下载Dart，可以手动到镜像站或GitHub下载最新的Dart安装包，手动解压到Flutter安装路径下的 `bin/cache/dart-sdk` 下。

<a name="SuTly"></a>
## Error connecting to the service protocol
错误详情：
```dart
Error connecting to the service protocol: failed to connect to http://127.0.0.1:58820
```

或者错误如下：
```
Error connecting to the service protocol: HttpException: Connection closed before full header was received
```

模拟器的Android版本太高，我的是Android Q，降为Android 9就正常了。

<a name="rIy7I"></a>
## This is taking an unexpectedly long time
错误详情：
```dart
(This is taking an unexpectedly long time.)
```

很大概率是Gradle下载太慢，手动下载zip包，将其复制到Gradle对应版本的文件夹。再次运行 `flutter run` 即可，Gradle会自动解压。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608087757369-f8057989-a8b0-44d2-8270-f936ad55ad4b.png#align=left&display=inline&height=89&originHeight=177&originWidth=731&size=33511&status=done&style=none&width=365.5)

<a name="QR1p4"></a>
## Waiting for another flutter command to release the startup lock…

解决办法：

1. 打开任务管理器，看看有没有Dart.exe运行着，有的话全部结束了，然后重启试试
2. 还是不行的话就删除掉flutter SDK中 `bin\cache` 目录下的 `lockfile` 文件

<a name="7efe2eb9"></a>
## flutter_swiper 的问题
错误信息：
```
══╡ EXCEPTION CAUGHT BY WIDGETS LIBRARY ╞═══════════════════════════════════════════════════════════
I/flutter (21956): The following assertion was thrown building NotificationListener:
I/flutter (21956): ScrollController not attached to any scroll views.
I/flutter (21956): 'package:flutter/src/widgets/scroll_controller.dart': Failed assertion: line 110 pos 12:
I/flutter (21956): '_positions.isNotEmpty'
I/flutter (21956):
I/flutter (21956): Either the assertion indicates an error in the framework itself, or we should provide substantially
```

解决方案: 给 [flutter_swiper](https://github.com/best-flutter/flutter_swiper) 设置 `key: ValueKey(items.length)`
```dart
Swiper(
  key: ValueKey(carouselList.length),
  itemBuilder: (BuildContext context,int index){
    return new Image.network(carouselList[index],fit: BoxFit.fill,);
  },
  itemCount: carouselList.length,
  pagination: new SwiperPagination(),
),
```

参考: [swiper item can't be hot add?](https://github.com/best-flutter/flutter_swiper/issues/64)

<a name="0abbbcea"></a>
## Entry point isn't within current project
解决方式：在 Android Studio 中找到 `File -> Project Structure -> Module` 然后添加项目的根文件夹，然后它将再次检测到它是一个flutter的应用程序，然后再次构建和工作。

参考: [Flutter 集成到Android项目中遇到的坑](https://blog.csdn.net/l707941510/article/details/98513208)

<a name="7e639e8c"></a>
## MediaQuery.of() called with a context that does not contain a MediaQuery
解决方案：想让界面跑起来，需要 `runApp()`，需要再写个 `MyApp()` 里面使用 `MaterialApp()` 包裹写好的界面，这样才可以运行。

参考: [Flutter: MediaQuery.of() called with a context that does not contain a MediaQuery](https://blog.csdn.net/qq_31017737/article/details/83069435)

<a name="d17a0f0b"></a>
## 参考资料

- [Flutter完整开发实战详解(三、 打包与填坑篇)](https://www.jianshu.com/p/29ba30d1ee57)

