适用于 Flutter 的状态管理工具很多, 有 [Scoped](https://pub.dev/packages/scoped)、[Redux](https://pub.dev/packages/flutter_redux)、[Provider](https://pub.dev/packages/provider) 等, 不过本人最熟悉最常用的还是 Redux, 其他的也不作探究了。

- [flutter_redux - pub.dev](https://pub.dev/packages/flutter_redux)
- [flutter_redux - GitHub](https://github.com/brianegan/flutter_redux/)

依赖：
```yaml
dependencies:
  flutter_redux: ^0.5.3
```

官方示例：
```dart
import 'package:flutter/material.dart';
import 'package:flutter_redux/flutter_redux.dart';
import 'package:redux/redux.dart';

// 枚举 Actions
enum Actions { Increment }

// 创建 reducer
int counterReducer(int state, dynamic action) {
  if (action == Actions.Increment) {
    return state + 1;
  }

  return state;
}

void main() {
  // 创建store
  final store = new Store<int>(counterReducer, initialState: 0);

  // 将store传入根Widget
  runApp(new FlutterReduxApp(
    title: 'Flutter Redux Demo',
    store: store,
  ));
}

class FlutterReduxApp extends StatelessWidget {
  final Store<int> store;
  final String title;

  FlutterReduxApp({Key key, this.store, this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // 通过 StoreProvider 将之前的 MaterialApp 或 WidgetsApp 包裹住, 并传入store
    return new StoreProvider<int>(
      // 在 StoreConnector 中的 converter 可以使用此 Store
      store: store,
      child: new MaterialApp(
        theme: new ThemeData.dark(),
        title: title,
        home: new Scaffold(
          appBar: new AppBar(
            title: new Text(title),
          ),
          body: new Center(
            child: new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                new Text(
                  'You have pushed the button this many times:',
                ),
                // ① 使用StoreConnector连接到数据源, 并通过converter将源数据转换为string
                new StoreConnector<int, String>(
                  converter: (store) => store.state.toString(),
                  builder: (context, count) {
                    return new Text(
                      count,
                      style: Theme.of(context).textTheme.display1,
                    );
                  },
                )
              ],
            ),
          ),
          // ② 使用StoreConnector连接到数据源, 并通过converter返回一个回调方法, 传入 builder 的 callback
          floatingActionButton: new StoreConnector<int, VoidCallback>(
            converter: (store) {
              return () => store.dispatch(Actions.Increment);
            },
            builder: (context, callback) {
              return new FloatingActionButton(
                // callback 实际调用的是converter返回的 `store.dispatch(Actions.Increment)`
                onPressed: callback,
                tooltip: 'asdasdasd',
                child: new Icon(Icons.add),
              );
            },
          ),
        ),
      ),
    );
  }
}
```

上面的 Store 是通过 converter 转换过的数据, 其实也可以将 store 直接放出来使用：
```dart
// ① 处
new StoreConnector<int, int>(
  converter: (store) => store.state,
  builder: (context, count) {
    return new Text(
      count.toString(),
      style: Theme.of(context).textTheme.display1,
    );
  },
)

// ② 处
floatingActionButton: new StoreConnector<int, Store>(
  converter: (store) => store,
  builder: (context, store) {
    return new FloatingActionButton(
      onPressed: () {
        store.dispatch(Actions.Increment);
      },
      tooltip: 'asdasdasd',
      child: new Icon(Icons.add),
    );
  },
),
```

