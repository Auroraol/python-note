<a name="wIyCh"></a>
## 一、状态管理概述
以下是管理状态的最常见的方法：

- Widget 管理自己的状态。
- Widget 管理子 Widget 状态。
- 混合管理（父 Widget 和子 Widget 都管理状态）。

如何决定使用哪种管理方法？下面是官方给出的一些原则可以帮助你做决定：

- 如果状态是用户数据，如复选框的选中状态、滑块的位置，则该状态最好由父 Widget 管理。
- 如果状态是有关界面外观效果的，例如颜色、动画，那么状态最好由 Widget 本身来管理。
- 如果某一个状态是不同 Widget 共享的则最好由它们共同的父 Widget 管理。
- 在 Widget 内部管理状态封装性会好一些，而在父 Widget 中管理会比较灵活。

两种组件的继承：

- `StatefulWidget` 有状态组件
- `StatelessWidget` 无状态组件

一个典型的有状态组件结构如下：
```dart
import 'package:flutter/material.dart';
import 'package:flutter_statusbarcolor/flutter_statusbarcolor.dart';

void main() {
  runApp(new StartApp());
}

class StartApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return new _StartAppState();
  }
}

class _StartAppState extends State<StartApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '首页',
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

<a name="setState"></a>
## 
<a name="b9b9fea5"></a>
## 二、Widget 管理自身状态
**setState**：Flutter 中, 有状态组件通过 setState 设置自身状态, 传入一个匿名函数, 在函数内部的操作(比如赋值、往列表里面添加元素等)将会触发视图更新。

示例一：点击单词重新生成
```dart
import 'package:english_words/english_words.dart';

class RandomWords extends StatefulWidget {
  @override
  createState() => new _RandomWordsState();
}

class _RandomWordsState extends State<RandomWords> {
  var wordPair = new WordPair.random();
  _handlerTap () {
    setState(() {
      wordPair = new WordPair.random();
    });
  }

  @override
  Widget build(BuildContext context) {
    return new GestureDetector(
      onTap: _handlerTap,
      child: Center(
        child: Text(wordPair.asPascalCase),
      ),
    );
  }
}
```

示例二：点击切换屏幕颜色
```dart
class TapboxA extends StatefulWidget {
  TapboxA({Key key}) : super(key: key);

  @override
  createState() => new _TapboxAState();
}

class _TapboxAState extends State<TapboxA> {
  bool _active = false;

  void _handleTap() {
    setState(() {
      _active = !_active;
    });
  }

  Widget build(BuildContext context) {
    return new GestureDetector(
      onTap: _handleTap,
      child: new Container(
        child: new Center(
          child: new Text(
            _active ? 'Active' : 'Inactive',
            style: new TextStyle(fontSize: 32.0, color: Colors.white),
          ),
        ),
        width: 200.0,
        height: 200.0,
        decoration: new BoxDecoration(
          color: _active ? Colors.lightGreen[700] : Colors.grey[600],
        ),
      ),
    );
  }
}
```

<a name="a97e32cf"></a>
## 三、父 Widget 管理子 Widget 的状态
先上示例：
```dart
// ParentWidget 为 TapboxB 管理状态.

//------------------------ ParentWidget --------------------------------

class ParentWidget extends StatefulWidget {
  @override
  _ParentWidgetState createState() => new _ParentWidgetState();
}

class _ParentWidgetState extends State<ParentWidget> {
  bool _active = false;

  void _handleTapboxChanged(bool newValue) {
    setState(() {
      _active = newValue;
    });
  }

  @override
  Widget build(BuildContext context) {
    return new Container(
      child: new TapboxB(
        active: _active,
        onChanged: _handleTapboxChanged,
      ),
    );
  }
}

//------------------------- TapboxB ----------------------------------

class TapboxB extends StatelessWidget {
  TapboxB({Key key, this.active: false, @required this.onChanged})
      : super(key: key);

  final bool active;
  final ValueChanged<bool> onChanged;

  void _handleTap() {
    onChanged(!active);
  }

  Widget build(BuildContext context) {
    return new GestureDetector(
      onTap: _handleTap,
      child: new Container(
        child: new Center(
          child: new Text(
            active ? 'Active' : 'Inactive',
            style: new TextStyle(fontSize: 32.0, color: Colors.white),
          ),
        ),
        width: 200.0,
        height: 200.0,
        decoration: new BoxDecoration(
          color: active ? Colors.lightGreen[700] : Colors.grey[600],
        ),
      ),
    );
  }
}
```

父 Widget 将 `active` 和 `onChanged` 传入子 Widget, 分别使用本身的 `_active` 和 `_handleTapboxChanged` 作映射, 当点击子 Widget 时, 触发 `_handleTapboxChanged` 并改变 `_active` 的值。

<a name="7ae210fb"></a>
## 四、混合状态管理
_ParentWidgetStateC 类：

- 管理_active 状态。
- 实现 _handleTapboxChanged() ，当盒子被点击时调用。
- 当点击盒子并且_active 状态改变时调用 setState()更新 UI。

_TapboxCState 对象：

- 管理_highlight 状态。
- GestureDetector 监听所有 tap 事件。当用户点下时，它添加高亮（深绿色边框）；当用户释放时，会移除高亮。
- 当按下、抬起、或者取消点击时更新_highlight 状态，调用 setState()更新 UI。
- 当点击时，将状态的改变传递给父组件。

```dart
//---------------------------- ParentWidget ----------------------------

class ParentWidgetC extends StatefulWidget {
  @override
  _ParentWidgetCState createState() => new _ParentWidgetCState();
}

class _ParentWidgetCState extends State<ParentWidgetC> {
  bool _active = false;

  // 处理子Widget的点击事件
  void _handleTapboxChanged(bool newValue) {
    setState(() {
      _active = newValue;
    });
  }

  @override
  Widget build(BuildContext context) {
    return new Container(
      child: new TapboxC(
        active: _active,
        onChanged: _handleTapboxChanged,
      ),
    );
  }
}

//----------------------------- TapboxC ------------------------------

class TapboxC extends StatefulWidget {
  // 接收父Widget传入的状态
  TapboxC({Key key, this.active: false, @required this.onChanged})
      : super(key: key);

  final bool active;
  final ValueChanged<bool> onChanged;

  @override
  _TapboxCState createState() => new _TapboxCState();
}

class _TapboxCState extends State<TapboxC> {
  bool _highlight = false;

  // 自己处理本Widget的按下、抬起事件
  void _handleTapDown(TapDownDetails details) {
    setState(() {
      this._highlight = true;
    });
  }

  void _handleTapUp(TapUpDetails details) {
    setState(() {
      _highlight = false;
    });
  }

  void _handleTapCancel() {
    setState(() {
      _highlight = false;
    });
  }

  // 交由父 Widget 处理点击事件
  void _handleTap() {
    // 使用Widget中的状态(此处为父Widget传入的状态)时, 不能用this, 而是直接用widget
    widget.onChanged(!widget.active);
  }

  @override
  Widget build(BuildContext context) {
    // 在按下时添加绿色边框，当抬起时，取消高亮
    return new GestureDetector(
      onTapDown: _handleTapDown, // 处理按下事件
      onTapUp: _handleTapUp, // 处理抬起事件
      onTap: _handleTap,
      onTapCancel: _handleTapCancel,
      child: new Container(
        child: new Center(
          child: new Text(widget.active ? 'Active' : 'Inactive',
              style: new TextStyle(fontSize: 32.0, color: Colors.white)),
        ),
        width: 200.0,
        height: 200.0,
        decoration: new BoxDecoration(
          color: widget.active ? Colors.lightGreen[700] : Colors.grey[600],
          border: _highlight
              ? new Border.all(
            color: Colors.teal[700],
            width: 10.0,
          ) : null,
        ),
      ),
    );
  }
}
```

<a name="3e7844e7"></a>
## 五、全局状态管理

以下部分选读, 可能在项目中根本不需要用到，参见：

- [flutter_redux](/books/flutter/flutter_redux.html)
- [fish_redux](/books/flutter/fish_redux.html)

