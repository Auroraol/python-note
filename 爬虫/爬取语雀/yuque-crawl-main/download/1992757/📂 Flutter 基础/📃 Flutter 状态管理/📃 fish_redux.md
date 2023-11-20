一直以来 Fish Redux 和 Flutter Redux 的最佳实践并不同，一个是 Page 级别的状态管理，一个是 App 级别状态管理，所以算是错位竞品。

- [fish-redux - GitHub](https://github.com/alibaba/fish-redux)
- [fish-redux - pub.dev](https://pub.dev/packages/fish_redux)
- [Flutter Architecture Samples](http://fluttersamples.com/)、[GitHub](https://github.com/brianegan/flutter_architecture_samples)
- [flutter_redux_sample](https://github.com/quanzaiyu/flutter_redux_sample)

引入:

```yaml
dependencies:
  fish_redux: ^0.2.4
```

<a name="d12e9ddd"></a>
## 推荐的目录结构
```bash
sample_page
-- action.dart
-- page.dart
-- view.dart
-- effect.dart
-- reducer.dart
-- state.dart
```

<a name="4fd26096"></a>
## 从一个简单的案例开始
<a name="page.dart"></a>
### page.dart
```dart
import 'package:fish_redux/fish_redux.dart';
import 'state.dart';
import 'view.dart';
import 'reducer.dart';

class TestPage extends Page<TestState, Map<String, dynamic>> {
  TestPage():
    super(
      initState: initState,
      view: buildView,
      reducer: buildReducer(),
    );
}
```

1. TestPage 继承自 Page
2. initState 其实是缩写, 完整的写法为: `initState: (Map<String, dynamic> args) => initState(args),`
3. view 也是缩写, 完整的写法为: `view: (TestState state, Dispatch dispatch, ViewService viewService) => buildView(state, dispatch, viewService),`
4. reducer 用于改变状态

<a name="state.dart"></a>
### state.dart
```dart
import 'package:fish_redux/fish_redux.dart';

class TestState implements Cloneable<TestState> {
  bool isLoading;
  String msg;

  @override
  TestState clone() {
    return TestState()
      ..isLoading = isLoading
      ..msg = msg;
  }
}

TestState initState(Map<String, dynamic> args) {
  final state = new TestState();
  state.msg = args['msg'];
  state.isLoading = false;
  return state;
}
```

1. 为什么要实现 clone 方法: 在之后的 reducer 需要使用
2. initState 接收一个 Map 类型的参数, 需要添加一个 msg 的 key

<a name="view.dart"></a>
### view.dart
```dart
import 'package:fish_redux/fish_redux.dart';
import 'package:flutter/material.dart';
import 'state.dart';

import 'action.dart';

Widget buildView(TestState state, Dispatch dispatch, ViewService viewService) {
  return Scaffold(
    appBar: AppBar(title: Text("Hello ${state.msg}")),
    body: Column(
      children: <Widget>[
        Center(
          child: state.isLoading ? Text('Loading') : Text("Hello ${state.msg}"),
        ),
        FlatButton(
          child: Text('click me'),
          onPressed: () {
            bool loading = !state.isLoading;
            dispatch(TestActionCreator.changeLoading(loading));
          },
        )
      ],
    ),
  );
}
```

1. 引入了 `action.dart`, 用来定义 Action 的
2. buildView 接收三个参数: `state` `dispatch` `viewService`
3. 返回值为一个 Widget, 跟普通 Widget 相同的写法
4. 使用状态时使用 `state.msg` `state.isLoading`
5. 修改状态时使用 `dispatch(TestActionCreator.changeLoading(loading))`

<a name="action.dart"></a>
### action.dart
```dart
import 'package:fish_redux/fish_redux.dart';

enum TestAction {
  changeLoading
}

class TestActionCreator {
  static Action changeLoading(bool loading) {
    return Action(TestAction.changeLoading, payload: loading);
  }
}
```

1. 通过 TestAction 枚举所有可能用到的 Action
2. 在 TestActionCreator 中定义所有的 Action
3. Action 接收两个参数, 第一个是 Action 名, 第二个是 payload

<a name="reducer.dart"></a>
### reducer.dart
```dart
import 'package:fish_redux/fish_redux.dart';

import 'action.dart';
import 'state.dart';

Reducer<TestState> buildReducer() {
  return asReducer<TestState>(<Object, Reducer<TestState>>{
    TestAction.changeLoading: _changeLoading,
  });
}

TestState _changeLoading(TestState state, Action action) {
  final TestState newState = state.clone();
  newState.isLoading = action.payload;
  return newState;
}
```

1. asReducer 指定了 Action 具体的操作
2. 操作 state 时需要使用深拷贝 `state.clone()`, 否则视图不会更新, 这里看出为什么 TestState 需要实现 Cloneable 接口了
3. action.payload 为传入的参数, 对应 `view.dart` 中的 `dispatch(TestActionCreator.changeLoading(loading))`, 其中 loading 就是这个 payload

<a name="a7293963"></a>
### 使用此带状态管理的页面
`main.dart`
```dart
TestPage().buildPage({'msg': 'world'})
```

前面讲到, initState 接收一个 Map 类型的参数, 需要添加一个 msg 的 key, 这里的参数 `{'msg': 'world'}` 便与之对应

完成代码：
```dart
import 'package:flutter/material.dart';
import 'package:flutter_app_bootstrapper/pages/test/page.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TestPage().buildPage({'msg': 'world'}),
    );
  }
}
```

<a name="Hp58y"></a>
## **路由管理**
fish_redux 还有一个很赞的功能, 可以方便地进行路由管理

<a name="3adaa69f"></a>
### 直接创建路由
创建路由管理: `app_route.dart`
```dart
import 'package:fish_redux/fish_redux.dart';
import 'package:flutter_app_bootstrapper/pages/test/page.dart';

final AbstractRoutes pageRoutes = PageRoutes(
  pages: <String, Page<Object, dynamic>>{
    'test': TestPage(),
  },
);
```

使用路由: `main.dart`, 在 MaterialApp -> home 参数中使用
```dart
pageRoutes.buildPage('test', {'msg': 'world'})
```

<a name="39beb2f0"></a>
### 使用 global 包装
看很多项目都使用以下方式创建路由, 我并不喜欢, 不过还是放出来看看。

创建路由管理：`app_route.dart`
```dart
import 'package:fish_redux/fish_redux.dart';
import 'package:flutter_app_bootstrapper/pages/test/page.dart';

class AppRoute {
  static AbstractRoutes _global;

  static AbstractRoutes get global {
    if (_global == null) {
      _global = PageRoutes(pages: <String, Page<Object, dynamic>>{
        RoutePath.test: TestPage(),
      });
    }
    return _global;
  }
}

class RoutePath {
  static const String test = 'test';
}
```

使用路由：`main.dart`, 在 MaterialApp -> home 参数中使用
```dart
AppRoute.global.buildPage(RoutePath.test, {'msg': 'world'}),
```

<a name="d17a0f0b"></a>
## 参考资料

- [刚刚，阿里宣布开源 Flutter 应用框架 Fish Redux！](https://yq.aliyun.com/articles/692549)
- [Fish Redux 全局 Store-AppRoute 使用指南](https://juejin.im/post/5cab73325188251b1542f974)
- [Flutter Redux 食用总结](https://juejin.im/post/5bf95aaa51882516e1542e31)
- [Fish Redux 使用指南](https://juejin.im/post/5c91a7cae51d45074f71afb5)
- [fish_redux 使用指北（这可能是比官方更友好的文档）](https://juejin.im/post/5cefb0f7f265da1bc07e1e59)
