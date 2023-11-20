<a name="071703d1"></a>
## 一、第一个Flutter程序
创建好Flutter项目后，修改入口文件。

`main.dart`
```dart
import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Flutter Demo',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new Scaffold(
        appBar: new AppBar(
          title: new Text('Welcome to Flutter'),
        ),
        body: new Center(
          child: new Text('Hello World'),
        ),
      ),
    );
  }
}
```

第一句：
```dart
void main() => runApp(new MyApp());
```
是以下简写：
```dart
void main() {
  runApp(new MyApp());
}
```

`main` 函数使用了 `=>` 符号, 这是Dart中单行函数或方法的简写。

`MyApp` 继承自 `StatelessWidget`，widget的主要工作是提供一个 `build()` 方法来描述如何根据其他较低级别的widget来显示自己。

![001.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608082047792-ffce281b-051a-42f4-8790-f8149f80d53a.png#align=left&display=inline&height=504&originHeight=826&originWidth=487&size=18501&status=done&style=none&width=297)

<a name="3d32e0d9"></a>
## 二、框架
<a name="5b0520a9"></a>
### 应用
创建一个 [MaterialApp](https://docs.flutter.io/flutter/material/MaterialApp-class.html) 应用程序, 常用的属性有：

- `debugShowCheckedModeBanner: false` 是否显示 Debug 字样, 默认 true
- `theme: ThemeData.dark()` 应用程序主题
- `title: title` 应用程序标题
- `home: Scaffold(...)` 应用程序首页, 通常使用 Scaffold 脚手架搭建

<a name="9970ad07"></a>
### 主题
[ThemeData](https://api.flutter.dev/flutter/material/ThemeData-class.html) 用于定义主题样式(背景颜色、字体大小、字体颜色等)。<br />
```dart
MaterialApp(
  ...
  theme: new ThemeData(
    primaryColor: Color(0xff1ABC9C),
    appBarTheme: AppBarTheme(
      color: Color(0xff1ABC9C),
      actionsIconTheme: IconThemeData(
        color: Colors.white
      ),
      iconTheme: IconThemeData(
        color: Colors.white
      ),
      textTheme: TextTheme(
        title: TextStyle(
          color: Colors.white,
          fontSize: 20
        )
      )
    ),
  ),
);
```

也可使用内置主题：
```dart
theme: ThemeData.dark()
```

<a name="9213c50a"></a>
### 页面骨架
一个完整的数路由页可能会包含导航栏、抽屉菜单(Drawer)以及底部 Tab 导航菜单等。如果每个路由页面都需要开发者自己手动去实现这些，这会是一件非常麻烦且无聊的事。幸运的是，Flutter Material [Scaffold](https://api.flutter.dev/flutter/material/Scaffold-class.html) 是一个路由页的骨架，我们使用它可以很容易地拼装出一个完整的页面。

常用的属性有：

- `appBar: AppBar()` 导航栏
- `body: Widget...` 主要内容
- `drawer: Drawer()` 抽屉
- `floatingActionButton: FloatingActionButton()` 悬浮按钮
- `bottomNavigationBar: BottomAppBar()` 底部导航栏

<a name="feaa969c"></a>
### 导航栏
[AppBar](https://api.flutter.dev/flutter/material/AppBar-class.html)：定义导航栏。

AppBar 的定义：
```dart
AppBar({
  Key key,
  this.leading, // 导航栏左侧Widget
  this.actions, // 导航栏右侧Widget
  this.title,// 页面标题
  this.bottom, // 导航栏底部菜单，通常为Tab按钮组
  this.elevation = 4.0, // 导航栏阴影
  this.centerTitle, //标题是否居中
  this.automaticallyImplyLeading = true, //如果leading为null，是否自动实现默认的leading按钮
  this.backgroundColor,
  ...   //其它属性见源码注释
})
```

比如：<br />![005.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608082265242-c09e0cb2-fe9c-4334-898e-a67f76f3a757.png#align=left&display=inline&height=179&originHeight=179&originWidth=429&size=27220&status=done&style=none&width=429)
```dart
appBar: new AppBar(
  title: new Text(title),
  leading: IconButton(icon: Icon(Icons.dashboard), onPressed: () {}),
  actions: <Widget>[ //导航栏右侧菜单
    IconButton(icon: Icon(Icons.share), onPressed: () {}),
  ],
),
```

<a name="232c80ff"></a>
### 悬浮按钮
[FloatingActionButton](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html) 是 Material 设计规范中的一种特殊 Button，通常悬浮在页面的某一个位置作为某种常用动作的快捷入口<br />![004.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608082285971-c460cf42-175c-4091-8c9e-1be1e90244ae.png#align=left&display=inline&height=262&originHeight=262&originWidth=463&size=29078&status=done&style=none&width=463)
```dart
floatingActionButton: new FloatingActionButton(
  onPressed: _incrementCounter,
  tooltip: 'Increment',
  child: new Icon(Icons.add),
),
// 指定 floatingActionButton 的位置
floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
```

<a name="39c69dc7"></a>
### 侧边抽屉
[Drawer](https://api.flutter.dev/flutter/material/Drawer-class.html)：侧边抽屉<br />![007.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1608082354470-2b97c2cd-a3f0-40e0-8fa2-c1c29d44a898.gif#align=left&display=inline&height=537&originHeight=869&originWidth=419&size=219807&status=done&style=none&width=259)
```dart
drawer: Drawer(
  child: Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: <Widget>[
      Padding(
        padding: const EdgeInsets.only(top: 38.0),
        child: Row(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0),
              child: ClipOval(
                child: Image.asset(
                  "assets/imgs/avatar.png",
                  width: 80,
                  height: 80,
                ),
              ),
            ),
            Text(
              "Quanzaiyu",
              style: TextStyle(fontWeight: FontWeight.bold),
            )
          ],
        ),
      ),
      Expanded(
        child: ListView(
          children: <Widget>[
            ListTile(
              leading: const Icon(Icons.add),
              title: const Text('Add account'),
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: const Text('Manage accounts'),
            ),
          ],
        ),
      ),
    ],
  ),
),
```

<a name="e62e6501"></a>
### 底部导航栏
[BottomAppBar](https://api.flutter.dev/flutter/material/BottomAppBar-class.html)<br />![005.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608082403946-184d1a30-9cfc-40ad-903f-80db74e05a61.png#align=left&display=inline&height=82&originHeight=82&originWidth=416&size=6438&status=done&style=none&width=416)
```dart
bottomNavigationBar: BottomAppBar(
  color: Colors.grey, // 背景色
  child: Container(
    height: 50.0,
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: <Widget>[
        IconButton(
          iconSize: 24,
          icon: Icon(Icons.home, size: 36, color: Colors.blue,),
          tooltip: 'home',
          onPressed: () {},
        ),
        IconButton(
          iconSize: 24,
          icon: Icon(Icons.settings, size: 36, color: Colors.green,),
          tooltip: 'settings',
          onPressed: () {},
        )
      ],
    ),
  ),
),
```

[BottomNavigationBar](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html)<br />![006.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1608082442603-488c2409-24a2-4d2d-acbe-0d53fb3a59da.gif#align=left&display=inline&height=70&originHeight=70&originWidth=398&size=15004&status=done&style=none&width=398)
```dart
int _selectedIndex = 0;

bottomNavigationBar: BottomNavigationBar(
  items: const <BottomNavigationBarItem>[
    BottomNavigationBarItem(
      icon: Icon(Icons.home),
      title: Text('Home'),
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.business),
      title: Text('Business'),
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.school),
      title: Text('School'),
    ),
  ],
  currentIndex: _selectedIndex,
  selectedItemColor: Colors.amber[800],
  onTap: (int index) {
    setState(() {
      _selectedIndex = index;
    });
  },
),
```

参考：

- [Flutter 30: 图解自定义底部状态栏 ACEBottomNavigationBar (一)](https://yq.aliyun.com/articles/689186)

<a name="0d98c747"></a>
### 其他

- [FlutterLogo](https://api.flutter.dev/flutter/material/FlutterLogo-class.html) 一个flutter的图标

<a name="fa352143"></a>
## 三、使用外部包
在 `pubspec.yaml` 中加入 `english_words` 包
```yaml
dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^0.1.0
  english_words: ^3.1.0
```

使用以下命令更新包：
```bash
flutter packages get
```

修改 `main.dart`：
```dart
import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() {
  runApp(new MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Flutter Demo',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new Scaffold(
        appBar: new AppBar(
          title: new Text('Welcome to Flutter'),
        ),
        body: new Center(
          child: new RandomWordsWidget(),
        ),
      ),
    );
  }
}

class RandomWordsWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // 生成随机字符串
    final wordPair = new WordPair.random();
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: new Text(wordPair.toString()),
    );
  }
}
```

以上, 使用 `new WordPair.random()` 随机生成英文单词, 通过 `wordPair.toString()` 将之转化为字符串

还可使用 `wordPair.asPascalCase` 生成驼峰形式的单词

<a name="b8a6f91d"></a>
### Pub仓库
[Pub](https://pub.dartlang.org/) 是Google官方的Dart Packages仓库，类似于node中的npm仓库，android中的jcenter。我们可以在Pub上面查找我们需要的包和插件，也可以向Pub发布我们的包和插件。我们将在后面的章节中介绍如何向Pub发布我们的包和插件。

<a name="fc75e721"></a>
## 四、事件处理
<a name="09358e40"></a>
### 单击

- onTapDown 指针已经在特定位置与屏幕接触
- onTapUp 指针停止在特定位置与屏幕接触
- onTap tap事件触发
- onTapCancel 先前指针触发的onTapDown不会在触发tap事件

<a name="efb486ca"></a>
### 双击

- onDoubleTap 用户快速连续两次在同一位置轻敲屏幕.

<a name="3466d5f4"></a>
### 长按

- onLongPress 指针在相同位置长时间保持与屏幕接触

<a name="92d4d8ef"></a>
### 垂直拖动

- onVerticalDragStart 指针已经与屏幕接触并可能开始垂直移动
- onVerticalDragUpdate 指针与屏幕接触并已沿垂直方向移动.
- onVerticalDragEnd 先前与屏幕接触并垂直移动的指针不再与屏幕接触，并且在停止接触屏幕时以特定速度移动

<a name="7f057ba5"></a>
### 水平拖动

- onHorizontalDragStart 指针已经接触到屏幕并可能开始水平移动
- onHorizontalDragUpdate 指针与屏幕接触并已沿水平方向移动
- onHorizontalDragEnd 先前与屏幕接触并水平移动的指针不再与屏幕接触，并在停止接触屏幕时以特定速度移动

<a name="3879443e"></a>
### [GestureDetector](https://docs.flutter.io/flutter/widgets/GestureDetector-class.html)
很多组件都包含一些事件处理的属性, 比如 GestureDetector、ListView 等。

示例：GestureDetector 的使用
```dart
new GestureDetector(
  onTapDown: _handleTapDown, // 处理按下事件
  onTapUp: _handleTapUp, // 处理抬起事件
  onTap: () {
    // ...
  },
  onTapCancel: _handleTapCancel,
  child: new Text('Click me!'),
);
```

<a name="ThEt8"></a>
## 参考资料

- [Flutter之MaterialApp使用详解](https://www.jianshu.com/p/1d44ae246652)
- [Flutter之WidgetsApp使用详解&与MaterialApp的纠缠](https://www.jianshu.com/p/57c7d66c7688)

