[ListView](https://api.flutter.dev/flutter/widgets/ListView-class.html) 是最常用的可滚动组件之一，它可以沿一个方向线性排布所有子组件，并且它也支持基于 Sliver 的延迟构建模型。
```dart
ListView({
  ...
  // 可滚动widget公共参数
  Axis scrollDirection = Axis.vertical,
  bool reverse = false,
  ScrollController controller,
  bool primary,
  ScrollPhysics physics,
  EdgeInsetsGeometry padding,

  // ListView各个构造函数的共同参数
  double itemExtent,
  bool shrinkWrap = false,
  bool addAutomaticKeepAlives = true,
  bool addRepaintBoundaries = true,
  double cacheExtent,

  // 子widget列表
  List<Widget> children = const <Widget>[],
})
```

**itemExtent**<br />该参数如果不为 null，则会强制 children 的“长度”为 itemExtent 的值；这里的“长度”是指滚动方向上子组件的长度，也就是说如果滚动方向是垂直方向，则 itemExtent 代表子组件的高度；如果滚动方向为水平方向，则 itemExtent 就代表子组件的宽度。在 ListView 中，指定 itemExtent 比让子组件自己决定自身长度会更高效，这是因为指定 itemExtent 后，滚动系统可以提前知道列表的长度，而无需每次构建子组件时都去再计算一下，尤其是在滚动位置频繁变化时（滚动系统需要频繁去计算列表高度）。

**shrinkWrap**<br />该属性表示是否根据子组件的总长度来设置 ListView 的长度，默认值为 false 。默认情况下，ListView 的会在滚动方向尽可能多的占用空间。当 ListView 在一个无边界(滚动方向上)的容器中时，shrinkWrap 必须为 true。

**addAutomaticKeepAlives**<br />该属性表示是否将列表项（子组件）包裹在 AutomaticKeepAlive 组件中；典型地，在一个懒加载列表中，如果将列表项包裹在 AutomaticKeepAlive 中，在该列表项滑出视口时它也不会被 GC（垃圾回收），它会使用 KeepAliveNotification 来保存其状态。如果列表项自己维护其 KeepAlive 状态，那么此参数必须置为 false。

**addRepaintBoundaries**<br />该属性表示是否将列表项（子组件）包裹在 RepaintBoundary 组件中。当可滚动组件滚动时，将列表项包裹在 RepaintBoundary 中可以避免列表项重绘，但是当列表项重绘的开销非常小（如一个颜色块，或者一个较短的文本）时，不添加 RepaintBoundary 反而会更高效。和 addAutomaticKeepAlive 一样，如果列表项自己维护其 KeepAlive 状态，那么此参数必须置为 false。

示例：
```dart
ListView(
  shrinkWrap: true,
  padding: const EdgeInsets.all(20.0),
  children: "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map((c) => Text(c, textScaleFactor: 2.0,)).toList(),
)
```

<a name="ListView.builder"></a>
## ListView.builder
[ListView.builder](https://api.flutter.dev/flutter/widgets/ListView/ListView.builder.html) 适合列表项比较多（或者无限）的情况，因为只有当子组件真正显示的时候才会被创建，也就说通过该构造函数创建的 ListView 是支持基于 Sliver 的懒加载模型的。
```dart
ListView.builder({
  ...
  @required IndexedWidgetBuilder itemBuilder,
  int itemCount,
  ...
})
```

**itemBuilder**<br />它是列表项的构建器，类型为 `IndexedWidgetBuilder`，返回值为一个 widget。当列表滚动到具体的 index 位置时，会调用该构建器构建列表项。

**itemCount**<br />列表项的数量，如果为 null，则为无限列表。

可滚动组件的构造函数如果需要一个列表项 Builder，那么通过该构造函数构建的可滚动组件通常就是支持基于 Sliver 的懒加载模型的，反之则不支持，这是个一般规律。我们在后面在介绍可滚动组件的构造函数时将不再专门说明其是否支持基于 Sliver 的懒加载模型了。

示例：<br />
```dart
ListView.builder(
  itemCount: 100,
  itemExtent: 50.0, //强制高度为50.0
  itemBuilder: (BuildContext context, int index) {
    return ListTile(title: Text("$index"));
  }
)
```

<a name="ListView.separated"></a>
## ListView.separated
[ListView.separated](https://api.flutter.dev/flutter/widgets/ListView/ListView.separated.html) 可以在生成的列表项之间添加一个分割组件，它比 ListView.builder 多了一个 separatorBuilder 参数，该参数是一个分割组件生成器。

示例：<br />
```dart
ListView.separated(
  itemCount: 100,
  //列表项构造器
  itemBuilder: (BuildContext context, int index) {
    return ListTile(title: Text("$index"));
  },
  //分割器构造器
  separatorBuilder: (BuildContext context, int index) {
    return index%2 == 0 ? Divider(color: Colors.blue,) : Divider(color: Colors.green,);
  },
)
```

<a name="ListView.custom"></a>
## ListView.custom

参考：[ListView.custom](https://api.flutter.dev/flutter/widgets/ListView/ListView.custom.html)

<a name="ff26c6c6"></a>
## 无限加载列表

假设我们要从数据源异步分批拉取一些数据，然后用 ListView 展示，当我们滑动到列表末尾时，判断是否需要再去拉取数据，如果是，则去拉取，拉取过程中在表尾显示一个 loading，拉取成功后将数据插入列表；如果不需要再去拉取，则在表尾提示"没有更多"。代码如下：

示例：
```dart
class InfiniteListView extends StatefulWidget {
  @override
  _InfiniteListViewState createState() => new _InfiniteListViewState();
}

class _InfiniteListViewState extends State<InfiniteListView> {
  static const loadingTag = "##loading##"; // 表尾标记
  var _words = <String>[loadingTag];

  @override
  void initState() {
    super.initState();
    _retrieveData();
  }

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      itemCount: _words.length,
      itemBuilder: (context, index) {
        // 如果到了表尾
        if (_words[index] == loadingTag) {
          // 不足100条，继续获取数据
          if (_words.length - 1 < 100) {
            // 获取数据
            _retrieveData();
            // 加载时显示loading
            return Container(
              padding: const EdgeInsets.all(16.0),
              alignment: Alignment.center,
              child: SizedBox(
                  width: 24.0,
                  height: 24.0,
                  child: CircularProgressIndicator(strokeWidth: 2.0)
              ),
            );
          } else {
            // 已经加载了100条数据，不再获取数据。
            return Container(
                alignment: Alignment.center,
                padding: EdgeInsets.all(16.0),
                child: Text("没有更多了", style: TextStyle(color: Colors.grey),)
            );
          }
        }
        // 显示单词列表项
        return ListTile(title: Text(_words[index]));
      },
      separatorBuilder: (context, index) => Divider(height: .0),
    );
  }

  void _retrieveData() {
    Future.delayed(Duration(seconds: 2)).then((e) {
      _words.insertAll(_words.length - 1,
          // 每次生成20个单词
          generateWordPairs().take(20).map((e) => e.asPascalCase).toList()
      );
      setState(() {
        // 重新构建列表
      });
    });
  }
}
```
效果：<br />![009.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1608104900968-6f99764a-4f1a-465f-9fea-3cdc6fb458f5.gif#align=left&display=inline&height=577&originHeight=869&originWidth=419&size=99646&status=done&style=none&width=278)

<a name="6d36b415"></a>
## 自定义列表
```dart
class HomePage extends StatefulWidget {
  @override
  createState() => new _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: new AppBar(title: Text('首页')),
        body: new Builder(builder: (BuildContext context) {
          return ListView(
            padding: const EdgeInsets.all(8.0),
            itemExtent: 106.0,
            children: <CustomListItem>[
              CustomListItem(
                user: 'Flutter',
                viewCount: 999000,
                thumbnail: Container(
                  decoration: const BoxDecoration(color: Colors.blue),
                ),
                title: 'The Flutter YouTube Channel',
              ),
              CustomListItem(
                user: 'Dash',
                viewCount: 884000,
                thumbnail: Container(
                  decoration: const BoxDecoration(color: Colors.yellow),
                ),
                title: 'Announcing Flutter 1.0',
              ),
            ],
          );
        }));
  }
}

class CustomListItem extends StatelessWidget {
  const CustomListItem({
    this.thumbnail,
    this.title,
    this.user,
    this.viewCount,
  });

  final Widget thumbnail;
  final String title;
  final String user;
  final int viewCount;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 5.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Expanded(
            flex: 1,
            child: thumbnail,
          ),
          Expanded(
            flex: 3,
            child: _VideoDescription(
              title: title,
              user: user,
              viewCount: viewCount,
            ),
          ),
          const Icon(
            Icons.more_vert,
            size: 20.0,
          ),
        ],
      ),
    );
  }
}

class _VideoDescription extends StatelessWidget {
  const _VideoDescription({
    Key key,
    this.title,
    this.user,
    this.viewCount,
  }) : super(key: key);

  final String title;
  final String user;
  final int viewCount;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(10.0, 0.0, 0.0, 0.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text(
            title,
            style: const TextStyle(
              fontWeight: FontWeight.w500,
              fontSize: 16.0,
            ),
          ),
          const Padding(padding: EdgeInsets.symmetric(vertical: 6.0)),
          Text(
            user,
            style: const TextStyle(fontSize: 14.0),
          ),
          const Padding(padding: EdgeInsets.symmetric(vertical: 1.0)),
          Text(
            '$viewCount views',
            style: const TextStyle(fontSize: 14.0),
          ),
        ],
      ),
    );
  }
}
```
效果：<br />![017.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608105001142-32da4229-eab2-4933-8300-07630121baf3.png#align=left&display=inline&height=303&originHeight=303&originWidth=362&size=11467&status=done&style=none&width=362)

