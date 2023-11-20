GridView 可以构建一个二维网格列表，其默认构造函数定义如下：

```dart
GridView({
  Axis scrollDirection = Axis.vertical,
  bool reverse = false,
  ScrollController controller,
  bool primary,
  ScrollPhysics physics,
  bool shrinkWrap = false,
  EdgeInsetsGeometry padding,
  @required SliverGridDelegate gridDelegate, // 控制子widget layout的委托
  bool addAutomaticKeepAlives = true,
  bool addRepaintBoundaries = true,
  double cacheExtent,
  List<Widget> children = const <Widget>[],
})
```

**gridDelegate**

类型是 SliverGridDelegate，它的作用是控制 GridView 子组件如何排列(layout)。

SliverGridDelegate 是一个抽象类，定义了 GridView Layout 相关接口，子类需要通过实现它们来实现具体的布局算法。Flutter 中提供了两个 SliverGridDelegate 的子类 SliverGridDelegateWithFixedCrossAxisCount 和 SliverGridDelegateWithMaxCrossAxisExtent，我们可以直接使用

<a name="SliverGridDelegateWithFixedCrossAxisCount"></a>
## SliverGridDelegateWithFixedCrossAxisCount
该子类实现了一个横轴为固定数量子元素的 layout 算法，其构造函数为：
```dart
SliverGridDelegateWithFixedCrossAxisCount({
  @required double crossAxisCount,
  double mainAxisSpacing = 0.0,
  double crossAxisSpacing = 0.0,
  double childAspectRatio = 1.0,
})
```

- **crossAxisCount** 横轴子元素的数量。此属性值确定后子元素在横轴的长度就确定了，即 ViewPort 横轴长度除以 crossAxisCount 的商。
- **mainAxisSpacing** 主轴方向的间距。
- **crossAxisSpacing** 横轴方向子元素的间距。
- **childAspectRatio** 子元素在横轴长度和主轴长度的比例。由于 crossAxisCount 指定后，子元素横轴长度就确定了，然后通过此参数值就可以确定子元素在主轴的长度。

示例：
```dart
GridView(
  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
      crossAxisCount: 3, // 横轴三个子widget
      childAspectRatio: 1.0 // 宽高比为1时，子widget
  ),
  children:<Widget>[
    Icon(Icons.ac_unit, size: 64,),
    Icon(Icons.airport_shuttle, size: 64),
    Icon(Icons.all_inclusive, size: 64),
    Icon(Icons.beach_access, size: 64),
    Icon(Icons.cake, size: 64),
    Icon(Icons.free_breakfast, size: 64),
  ]
)
```

效果：<br />![010.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608105347379-6679c552-ced2-41c4-9a09-cc772ae7f597.png#align=left&display=inline&height=338&originHeight=338&originWidth=417&size=32263&status=done&style=none&width=417)

<a name="GridView.count"></a>
## GridView.count

GridView.count 构造函数内部使用了 SliverGridDelegateWithFixedCrossAxisCount，我们通过它可以快速的创建横轴固定数量子元素的 GridView，上面的示例代码等价于：

```dart
GridView.count(
  crossAxisCount: 3,
  childAspectRatio: 1.0,
  children: <Widget>[
    Icon(Icons.ac_unit, size: 64,),
    Icon(Icons.airport_shuttle, size: 64),
    Icon(Icons.all_inclusive, size: 64),
    Icon(Icons.beach_access, size: 64),
    Icon(Icons.cake, size: 64),
    Icon(Icons.free_breakfast, size: 64),
  ],
)
```

<a name="SliverGridDelegateWithMaxCrossAxisExtent"></a>
## SliverGridDelegateWithMaxCrossAxisExtent

该子类实现了一个横轴子元素为固定最大长度的 layout 算法，其构造函数为：

```dart
SliverGridDelegateWithMaxCrossAxisExtent({
  double maxCrossAxisExtent,
  double mainAxisSpacing = 0.0,
  double crossAxisSpacing = 0.0,
  double childAspectRatio = 1.0,
})
```

maxCrossAxisExtent 为子元素在横轴上的最大长度，之所以是“最大”长度，是因为横轴方向每个子元素的长度仍然是等分的，举个例子，如果 ViewPort 的横轴长度是 450，那么当 maxCrossAxisExtent 的值在区间[450/4，450/3)内的话，子元素最终实际长度都为 112.5，而 childAspectRatio 所指的子元素横轴和主轴的长度比为最终的长度比。其它参数和 SliverGridDelegateWithFixedCrossAxisCount 相同。

```dart
GridView(
  padding: EdgeInsets.zero,
  gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
      maxCrossAxisExtent: 200.0,
      childAspectRatio: 2.0 // 宽高比为2
  ),
  children: <Widget>[
    Icon(Icons.ac_unit),
    Icon(Icons.airport_shuttle),
    Icon(Icons.all_inclusive),
    Icon(Icons.beach_access),
    Icon(Icons.cake),
    Icon(Icons.free_breakfast),
  ],
)
```

<a name="GridView.extent"></a>
## GridView.extent

GridView.extent 构造函数内部使用了 SliverGridDelegateWithMaxCrossAxisExtent，我们通过它可以快速的创建纵轴子元素为固定最大长度的的 GridView，上面的示例代码等价于：

```dart
GridView.extent(
  maxCrossAxisExtent: 120.0,
  childAspectRatio: 2.0,
  children: <Widget>[
    Icon(Icons.ac_unit),
    Icon(Icons.airport_shuttle),
    Icon(Icons.all_inclusive),
    Icon(Icons.beach_access),
    Icon(Icons.cake),
    Icon(Icons.free_breakfast),
  ],
);
```

<a name="GridView.builder"></a>
## GridView.builder

上面我们介绍的 GridView 都需要一个 widget 数组作为其子元素，这些方式都会提前将所有子 widget 都构建好，所以只适用于子 widget 数量比较少时，当子 widget 比较多时，我们可以通过 GridView.builder 来动态创建子 widget。GridView.builder 必须指定的参数有两个：

```dart
GridView.builder(
  ...
  @required SliverGridDelegate gridDelegate,
  @required IndexedWidgetBuilder itemBuilder,
)
```

其中 itemBuilder 为子 widget 构建器。

<a name="b44419b7"></a>
## 从数据源获取菜单

假设我们需要从一个异步数据源（如网络）分批获取一些 Icon，然后用 GridView 来展示：

```dart
class InfiniteGridView extends StatefulWidget {
  @override
  _InfiniteGridViewState createState() => new _InfiniteGridViewState();
}

class _InfiniteGridViewState extends State<InfiniteGridView> {

  List<IconData> _icons = []; //保存Icon数据

  @override
  void initState() {
    // 初始化数据
    _retrieveIcons();
  }

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 3,
            childAspectRatio: 1.0
        ),
        itemCount: _icons.length,
        itemBuilder: (context, index) {
          if (index == _icons.length - 1 && _icons.length < 200) {
            _retrieveIcons();
          }
          return Icon(_icons[index], size: 64,);
        }
    );
  }

  void _retrieveIcons() {
    Future.delayed(Duration(milliseconds: 200)).then((e) {
      setState(() {
        _icons.addAll([
          Icons.ac_unit,
          Icons.airport_shuttle,
          Icons.all_inclusive,
          Icons.beach_access, Icons.cake,
          Icons.free_breakfast
        ]);
      });
    });
  }
}
```

`_retrieveIcons()`：在此方法中我们通过 Future.delayed 来模拟从异步数据源获取数据，每次获取数据需要 200 毫秒，获取成功后将新数据添加到_icons，然后调用 setState 重新构建。

在 itemBuilder 中，如果显示到最后一个时，判断是否需要继续获取数据，然后返回一个 Icon。

<a name="flutter_staggered_grid_view"></a>
## flutter_staggered_grid_view

Flutter 的 GridView 默认子元素显示空间是相等的，但在实际开发中，你可能会遇到子元素大小不等的情况，<br />Pub 上有一个包 [flutter_staggered_grid_view](https://pub.dev/packages/flutter_staggered_grid_view)，它实现了一个交错 GridView 的布局模型，可以很轻松的实现这种布局

示例：
```dart
StaggeredGridView.countBuilder(
  crossAxisCount: 4,
  itemCount: 12,
  itemBuilder: (BuildContext context, int index) => new Container(
      color: Colors.green,
      child: new Center(
        child: new CircleAvatar(
          backgroundColor: Colors.white,
          child: new Text('$index'),
        ),
      )),
  staggeredTileBuilder: (int index) =>
    StaggeredTile.count(2, index.isEven ? 2 : 1),
  mainAxisSpacing: 8.0,
  crossAxisSpacing: 4.0,
)
```

效果：<br />![011.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608105384349-c577869d-0c41-4795-90cb-c692b8dd3916.png#align=left&display=inline&height=726&originHeight=726&originWidth=479&size=12811&status=done&style=none&width=479)

更多例子参考: [flutter_staggered_grid_view examples](https://github.com/letsar/flutter_staggered_grid_view/tree/master/example/lib)

貌似此插件滚动有问题，GitHub 上有很多人提相关 scroll 的 issue，过段时间再看看有没有解决！

