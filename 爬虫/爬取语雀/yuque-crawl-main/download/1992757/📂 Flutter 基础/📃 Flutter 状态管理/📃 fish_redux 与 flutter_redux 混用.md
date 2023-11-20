fish_redux 的主要使用场景是单个页面的状态管理，虽然也可以用作全局状态管理，但我更喜欢把全局状态管理存放于 `flutter_redux` 中，以下示例将两个状态管理工具进行混用。

`stores/app_store.dart`
```dart
// 枚举 Actions
enum Actions { Increment, Decrease }

// 创建 reducer
Map<String, dynamic> appReducer(Map<String, dynamic> state, dynamic action) {
  print(state);
  print(action);
  if (action == Actions.Increment) {
     state['num'] += 1;
  } else if (action == Actions.Decrease) {
    state['num'] -= 1;
  }

  return state;
}
```

`main.dart`
```dart
import 'package:flutter/material.dart';
import 'package:flutter_app_bootstrapper/routes/app_route.dart';
import 'package:flutter_app_bootstrapper/stores/app_store.dart';
import 'package:flutter_redux/flutter_redux.dart';
import 'package:redux/redux.dart';

void main() {
  // 创建store
  final store = new Store<Map<String, dynamic>>(appReducer, initialState: {'num': 0});

  // 将store传入根Widget
  runApp(new MyApp(
    store: store,
  ));
}

class MyApp extends StatelessWidget {
  final Store<Map<String, dynamic>> store;

  MyApp({Key key, this.store}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return new StoreProvider<Map<String, dynamic>>(
      store: store,
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: AppRoute.global.buildPage(RoutePath.test, {'msg': 'world'}),
      )
    );
  }
}
```

`pages/test/view.dart`
```dart
import 'package:fish_redux/fish_redux.dart' hide Store;
import 'package:flutter/material.dart';
import 'package:flutter_app_bootstrapper/api/Api.dart';
import 'package:flutter_app_bootstrapper/api/HttpUtil.dart';
import 'package:flutter_redux/flutter_redux.dart';
import 'package:redux/redux.dart';

import 'package:flutter_app_bootstrapper/stores/app_store.dart' as AppStore;

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
        ),
        // 以下, 混用全局状态管理 flutter_redux
        new StoreConnector<Map<String, dynamic>, String>(
          converter: (store) => store.state['num'].toString(),
          builder: (context, count) {
            return new Text(
              count,
              style: Theme.of(context).textTheme.display1,
            );
          },
        ),
        new StoreConnector<Map<String, dynamic>, Store>(
          converter: (store) => store,
          builder: (context, store) {
            return Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  FlatButton(
                    onPressed: () => store.dispatch(AppStore.Actions.Increment),
                    child: new Icon(Icons.plus_one),
                  ),
                  FlatButton(
                    onPressed: () => store.dispatch(AppStore.Actions.Decrease),
                    child: new Icon(Icons.exposure_neg_1),
                  )
                ],
              );
          },
        ),
      ],
    ),
  );
}
```

