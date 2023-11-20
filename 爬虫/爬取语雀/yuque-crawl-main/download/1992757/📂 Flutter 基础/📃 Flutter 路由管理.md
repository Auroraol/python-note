<a name="41b634c7"></a>
## 一、直接跳转路由
<a name="push"></a>
### push
使用 `Navigator.push` 跳转到新页面：
```dart
Navigator.push(context,
  new MaterialPageRoute(builder: (context) {
    return new NewRoute(); // 将给定的路由入栈
  }));
```

- **context**: build 中传入的 content
- **Navigator**: Navigator 是一个路由管理的组件，它提供了打开和退出路由页方法。Navigator 通过一个栈来管理活动路由集合。通常当前屏幕显示的页面就是栈顶的路由。
- **MaterialPageRoute**: MaterialPageRoute 继承自 PageRoute 类，PageRoute 类是一个抽象类，表示占有整个屏幕空间的一个模态路由页面，它还定义了路由构建及切换时过渡动画的相关接口及属性。

MaterialPageRoute 的定义：
```dart
MaterialPageRoute({
  WidgetBuilder builder,
  RouteSettings settings,
  bool maintainState = true,
  bool fullscreenDialog = false,
})
```

如果要替换当前页面，可以使用: `Navigator.pushReplacement`

<a name="pop"></a>
### pop
回退到前一个页面使用 `Navigator.pop`：
```dart
Navigator.pop(context); // 将栈顶路由出栈
```

<a name="of"></a>
### of
还可以通过 `Navigator.of(context).push` 进行页面跳转：
```dart
Navigator.of(context).push(
  new MaterialPageRoute(
    builder: (context) {
      return new Scaffold(
        appBar: new AppBar(
          title: new Text('NewPage'),
        ),
        body: new Text('...'),
      );
    },
  ),
);
```

同样，可以使用以下方式返回前一个页面：
```dart
Navigator.of(context).pop();
```

<a name="d624dec0"></a>
### 示例：两个页面之间的跳转
```dart
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(context,
              new MaterialPageRoute(builder: (context) {
                return new NewPage();
              }));
        },
        child: Icon(Icons.forward),
      ),
      // ...
    );
  }
}

class NewPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.pop(context);
        },
        child: Icon(Icons.arrow_back),
      ),
      // ...
    );
  }
}
```

<a name="5463c23e"></a>
## 二、命名路由
<a name="2a57695d"></a>
### 路由表
通过 MaterialApp 的 routes 参数指定路由表
```dart
import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter_ScreenUtil',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      // 注册路由表
      routes: {
        "HomePage": (context) => HomePage(),
        "NewPage": (context) => NewPage(),
      },
      home: new HomePage(),
    );
  }
}
```

通过 `Navigator.pushNamed` 跳转到命名路由
```dart
Navigator.pushNamed(context, 'NewPage');
```

同样，可以使用 of 指定 context：
```dart
Navigator.of(context).pushNamed('NewPage');
```

如果要替换当前页面，可以使用: `Navigator.pushReplacementNamed`

<a name="0d0a259f"></a>
### 多级路由
可以使用以下方式定多级路由：
```dart
return new MaterialApp(
  // ...
  routes: <String, WidgetBuilder> {
    // 这里可以定义静态路由，不能传递参数
    '/router/second': (_) => new SecondPage(),
    '/router/home': (_) => new RouterHomePage(),
  },
);
```

使用：
```dart
Navigator.of(context).pushNamed('/router/second');
```

<a name="28fbbfed"></a>
## 三、路由传参
<a name="09f23766"></a>
### 构造器传参
通过 push 方法传递参数：
```dart
Navigator.push(context,
    new MaterialPageRoute(builder: (context) {
      return new NewPage(text: 'Hello'); // 传入text参数
    }));
```

然后通过类的构造器接收参数：
```dart
class NewPage extends StatelessWidget {
  NewPage({
    Key key,
    @required this.text,  // 接收一个text参数
  }) : super(key: key);
  final String text;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('New Page'),
      ),
      body: Text(text), // 显示传入的参数
    );
  }
}
```

<a name="f134a22c"></a>
### 通过路由参数传递
在 MaterialPageRoute 中接收第二参数 settings，可以通过 arguments 指定要传入的参数：
```dart
Navigator.push(context,
    new MaterialPageRoute(
        builder: (context) {
          return new NewPage();
        },
        settings: RouteSettings(
          arguments: {'name': 'postbird'}, // 传入参数
        ),
    ),
);
```

接收参数：
```dart
class NewPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var args = ModalRoute.of(context).settings.arguments;
    return Scaffold(
      // ...
    );
  }
}
```

<a name="1b80c35b"></a>
### 回传参数
在 pop 方法中可以携带返回参数，通过 push 的 then 接收：
```dart
Navigator.push(context,
    new MaterialPageRoute(builder: (context) {
        return new NewPage();
      }
    ),
).then((res) { // 接收返回时传过来的参数
  print(res);
});
```

接收参数：
```dart
// 接参
class NewPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.pop(context, '这个是要返回给上一个页面的数据'); // 返回时传递参数
        },
        child: Icon(Icons.arrow_back),
      ),
      // ...
    );
  }
}
```

<a name="516185a9"></a>
### 命名路由传参
通过 pushNamed 可以携带第三参数：
```dart
Navigator.pushNamed(context, 'NewPage', arguments: 'Hello world');
```

接收参数：
```dart
// 接参
class NewPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var args = ModalRoute.of(context).settings.arguments; // 获取传入的参数
    return Scaffold(
      // ...
    );
  }
}
```

返回时传参同样用 then 接收：
```dart
// NewPage
Navigator.of(context).pop('返回的数据');
```

```dart
// 返回的页面
Navigator.pushNamed(context, 'NewPage').then((res) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return new AlertDialog(
        content: new Text("res: $res"),
      );
    });
});
```




