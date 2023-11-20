![flutter.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605061935727-c1dc2604-0fe1-4f12-8b1e-f4a7793f1908.png#align=left&display=inline&height=470&originHeight=1500&originWidth=1000&size=393291&status=done&style=none&width=313)<br />Flutter 是 Google推出并开源的移动应用开发框架，主打跨平台、高保真、高性能。开发者可以通过 Dart语言开发 App，一套代码同时运行在 iOS 和 Android平台。 Flutter提供了丰富的组件、接口，开发者可以很快地为 Flutter添加 native扩展。同时 Flutter还使用 Native引擎渲染视图，这无疑能为用户提供良好的体验。

Flutter内置美丽的 Material Design 和 Cupertino（iOS风格）widget、丰富的 motion API、平滑而自然的滑动效果和平台感知，为用户带来全新体验。

<a name="92999674"></a>
## 采用Dart语言开发
这是一个很有意思，但也很有争议的问题，在了解Flutter为什么选择了 Dart而不是 JavaScript之前我们先来介绍两个概念：JIT和AOT。

目前，程序主要有两种运行方式：静态编译与动态解释。静态编译的程序在执行前全部被翻译为机器码，通常将这种类型称为AOT （Ahead of time）即 “提前编译”；而解释执行的则是一句一句边翻译边运行，通常将这种类型称为JIT（Just-in-time）即“即时编译”。AOT程序的典型代表是用C/C++开发的应用，它们必须在执行前编译成机器码，而JIT的代表则非常多，如JavaScript、python等，事实上，所有脚本语言都支持JIT模式。但需要注意的是JIT和AOT指的是程序运行方式，和编程语言并非强关联的，有些语言既可以以JIT方式运行也可以以AOT方式运行，如Java、Python，它们可以在第一次执行时编译成中间字节码、然后在之后执行时可以直接执行字节码，也许有人会说，中间字节码并非机器码，在程序执行时仍然需要动态将字节码转为机器码，是的，这没有错，不过通常我们区分是否为AOT的标准就是看代码在执行之前是否需要编译，只要需要编译，无论其编译产物是字节码还是机器码，都属于AOT。在此，读者不必纠结于概念，概念就是为了传达精神而发明的，只要读者能够理解其原理即可，得其神忘其形。

<a name="ee0bf17d"></a>
### 开发效率高
Dart运行时和编译器支持Flutter的两个关键特性的组合：

基于JIT的快速开发周期：Flutter在开发阶段采用，采用JIT模式，这样就避免了每次改动都要进行编译，极大的节省了开发时间；

基于AOT的发布包: Flutter在发布时可以通过AOT生成高效的ARM代码以保证应用性能。而JavaScript则不具有这个能力。

<a name="122889f8"></a>
## Flutter框架结构
![framework.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1605061920686-179033fa-72ce-49a5-b9a9-5f3743dddaed.png#align=left&display=inline&height=449&originHeight=449&originWidth=815&size=38960&status=done&style=none&width=815)
<a name="467c415e"></a>
### Flutter Framework
这是一个纯 Dart实现的 SDK，它实现了一套基础库，自底向上，我们来简单介绍一下：

底下两层（Foundation和Animation、Painting、Gestures）在Google的一些视频中被合并为一个dart UI层，对应的是Flutter中的dart:ui包，它是Flutter引擎暴露的底层UI库，提供动画、手势及绘制能力。

Rendering层，这一层是一个抽象的布局层，它依赖于dart UI层，Rendering层会构建一个UI树，当UI树有变化时，会计算出有变化的部分，然后更新UI树，最终将UI树绘制到屏幕上，这个过程类似于React中的虚拟DOM。Rendering层可以说是Flutter UI框架最核心的部分，它除了确定每个UI元素的位置、大小之外还要进行坐标变换、绘制(调用底层dart:ui)。

Widgets层是Flutter提供的的一套基础组件库，在基础组件库之上，Flutter还提供了 Material 和Cupertino两种视觉风格的组件库。而我们Flutter开发的大多数场景，只是和这两层打交道。

<a name="d6437846"></a>
### Flutter Engine
这是一个纯 C++实现的 SDK，其中包括了 Skia引擎、Dart运行时、文字排版引擎等。在代码调用 dart:ui库时，调用最终会走到Engine层，然后实现真正的绘制逻辑。

<a name="35808e79"></a>
## 参考资料

- [Flutter 官网](https://flutter.dev/)
- [Flutter 中文网](https://flutterchina.club/)
- [Flutter 实战](https://book.flutterchina.club/)、[GitHub](https://github.com/flutterchina/flutter-in-action)、[《Flutter实战》随书源码](https://github.com/wendux/flutter_in_action_source_code)
- [Flutter API](https://api.flutter.dev/)
- [Flutter Plugins](https://github.com/flutter/plugins)
- [Meterial 官网](https://material.io/design/)
- [Dart Pub](https://pub.dartlang.org/)
- [初识Flutter：Flutter简介](https://book.flutterchina.club/chapter1/flutter_intro.html)

