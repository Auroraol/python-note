<a name="df368884"></a>
## 前言
结合由 Facebook 出品的静态类型检查工具 [Flow](https://flow.org)，和最近将 Flow 引入到一个 Vue.js 项目中的实践经验，本文想聊聊 Flow 类型检查工具和它在Vue项目中实际使用的效果。

<a name="767fa455"></a>
## 目录

- 为什么需要引入类型检查？
- Flow 是什么？
- Flow 的作用
- Flow 在 Vue 项目中的使用
- Flow 的配置过程
- 在 Vue 组件中使用 Flow 的几个方法
- 类型检查工具对团队有什么好处？
- 总结

<a name="a1558b2e"></a>
## 为什么需要引入类型检查？
JS作为一个弱类型语言，一个著名的黑点是它很容易就写出非常隐蔽的隐患代码，在编译期甚至运行时看上去都不会报错，但是可能会发生各种各样奇怪的和难以解决的bug。<br />类型检查是当前动态类型语言的发展趋势，根据[stateofjs](https://github.com/flow-typed/flow-typed)的调查结果，JS的强类型超集TypeScript已经有了相当的知名度，吸引了大量开发者的学习兴趣，并且大部分开发者计划继续了解或者使用。

1. 使得大型项目可维护
2. 增加代码的可读性
3. 通常会有更好的IDE支持

<a name="0411265b"></a>
## Flow是什么？
[Flow](https://github.com/facebook/Flow)是一个由Facebook出品的JavaScript静态类型检查工具，它与Typescript不同的是，它可以部分引入，不需要完全重构整个项目，所以对于一个已有一定规模的项目来说，迁移成本更小，也更加可行。除此之外，Flow可以提供实时增量的反馈，通过运行Flow server不需要在每次更改项目的时候完全从头运行类型检查，提高运行效率。<br />Flow 和 Typescript 都是给 Javascript 增加类型检查的优秀解决方案，两者的简单对比如下：

| 工具 | Flow | Typescript |
| --- | --- | --- |
| 公司 | Facebook | 微软 |
| star | 12k+ | 23k+ |
| 文档支持程度 | 中等 | 更多 |
| 第三方库支持工具 | Flow-typed | tsd |
| IDE支持 | Webstorm自带插件支持 | Webstorm支持，Visual Studio原生支持 |
| 其他 | 自由度更高，老项目的迁移成本低 | 工程化强，社区活跃度和官方支持力度更高，适合新项目 |


两者在代码语法上有大量相似的地方，除了对于一些数据类型的支持不一样，具体请查看Flow的文档。关于 Flow 和 Typescript 的比较，可以简单总结为：对于新项目，可以考虑使用 TypeScript 或者 Flow，对于已有一定规模的项目则建议使用Flow进行较小成本的逐步迁移来引入类型检查。

<a name="2c0cb939"></a>
## Flow的作用
一个简单的demo如下。
<a name="66318be7"></a>
## Flow 在 Vue 项目中的使用
Flow 在Vue 项目中的具体使用价值有：

- 使用 Flow 可以在不需要重构整个 Vue 项目（如UI组件迁移成本）、不需要引入大量的工具链（eslint+babel）、不需要第三方库一定支持的情况下引入静态类型检查
- Vue.js 官方对 TypeScript 做了支持，但是项目所依赖的第三方库不一定支持TypeScript，从全局考虑TypeScript的迁移成本比较大

在尝试Flow+Vue.js的实践过程中，主要的步骤包括：

1. 使用[Flow-typed工具](https://github.com/flow-typed/flow-typed) packages的支持；
2. 在一个由Vue cli (webpack + babel + eslint) 生成的脚手架项目中配置 Flow（见后文）；3，Vue 的单文件组件结构如何支持 Flow，在业务项目的实践中前后使用了三种方案，也会在后文分别介绍这几种方法和其优缺点。

<a name="c63ccc3f"></a>
## Flow的配置过程
假设目前有一个从vue-cli命令行生成的项目：vue init webpack-simple Flow-vue-demo。关于Babel，Eslint（可选）和Flow，需要安装所需的 npm packages，参考列表如下：

Babel:

- babel-plugin-syntax-Flow
- babel-plugin-transform-class-properties
- babel-plugin-transform-Flow-strip-types

Eslint: (可选)

- eslint
- babel-eslint
- eslint-plugin-html
- eslint-plugin-Flowtype-errors
- eslint-plugin-vue
- eslint-config-vue

Flow:

- Flow-bin

1. Webstorm 自带了 Flow 的支持，需要开启，结合 eslint 配置 Flow 相关的 rules，在编辑时通过eslint即可自动报错。
2. 安装Flow，运行Flow init && Flow check。配置 .vue 文件为 Flow 的检查范围。
3. 使用 Flow-typed 处理第三方的 npm packages 的类型声明。
4. 必要的话增加自定义的类型声明文件，如自定义的对象等，具体可以参考Flow文档。

<a name="ffcaa46b"></a>
## 在 Vue 组件中使用 Flow 的几个方法
在前面的 demo 中已经展示了纯 JS 文件里面怎么用 Flow，那么在一个vue组件文件中应该如何配置呢？有下面几种方法。

方法一：直接在script标签中，像纯 js 文件处理一样添加 Flow 注释，发现可以正常编译运行，但是运行Flow check是无效的。

方法二：注释掉template, style 和 script 标签，由于Vue的编译器即使注释了也会识别其中的`<template>, <style> 和 <script>` 标签，而Flow检查会忽略注释，因此对于Flow来说可以当做一个 javascript 文件进行处理。demo如下图所示。<br />对于这样处理的vue文件，Flow命令能够报出关于一般的函数声明的类型检查错误，但是对于绑定到Vue实例（this）上的方法是无效的。因此Flow类型检查不是100%覆盖。这种方法的主要问题在于代码和注释混用不便于阅读，目前 Flow 社区有一个 open issue 就是关于这个问题的，即不能自动检测中文件中的script标签，请见：[Support HTML files #2218](https://github.com/facebook/Flow/issues/2218)

方法三：Vue 文件引用外部的 js 文件，将js部分单独抽离出来进行类型检查。该方法的优点在于可以用到Flow的所有功能，但是没有了vue单文件组件的结构，项目结构略显臃肿。（每个组件都会有至少两个文件）。如下图：<br />三种解决方法的优缺点对比如下表所示：

| 方法 | Pros | Cons |
| --- | --- | --- |
| 标签中直接添加Flow | 代码添加量最小 | Flow 类型检查无效. 不予考虑 |
| 注释template中的标签 | 1. 可以通过Flow check检查出部分的类型错误 2. 最接近使用直觉. 目前是一个open issue | 1. 对于和组件无关的函数以及import. 可以正常工作. 但是不是100%覆盖 2. 看上去样式比较糟糕 |
| Vue 文件引用外部的 js 文件 | 1. 通过 eslint 中通过使用 Flow 插件. 配置Flow规则. 可以在编辑时实时提示 2. 没有影响文件结构 3. 单独的 js 文件可以几乎完全使用 Flow 的所有功能 | 1. method仍然不能自动识别. 由于 Vue 中的一些函数一般没有return value. 需要手动判断类型防止bug 2. 一个组件的代码被分拆到多个文件. 不如单文件组件那么直观 |


<a name="d7b56b14"></a>
## 类型检查工具对团队有什么好处？
通过在一个 Vue 技术栈的实际业务项目中引入 Flow，我们大致获得了这些收益：

1. 几乎消灭了由函数数据类型引起的bug
2. 无需额外的关于变量、参数、返回值类型的注释，可以让读者了解必要的附加信息
3. 大量减少由于使用第三方库不当引起的类型错误
4. 可以在CI系统中集成
5. 工具链配置成本比较低，只需要很少的工作量即可达到这些效果

关于类型检查工具，读者可能需要考虑的问题，回答如下表所示。

| Question | Answer |
| --- | --- |
| 类型检查可以让我的代码bug free吗？ | 不能保证bug free，只能检查类型错误 |
| 可以提高我的生产力吗？ | 需要多写一些代码，但是相应地可以减少很多runtime debug的时间 |
| 将Flow引入我的项目，所需要的工作量大吗？ | 不大，可以逐步引入 |
| 我的项目需要长期维护？ | 请使用 Flow 或者 Typescript |
| 我的项目非常简单？ | 简单项目不一定需要类型检查，可能会有些多余 |
| 我的项目需要重构？ | 请引入类型检查 |
| 我的项目对于bug free的要求非常高？ | 请引入类型检查，减少类型错误等难以发现的bug |
| 我的项目开发人员流动很频繁？ | 请引入类型检查，增加项目可读性 |
| 我的项目有大量的算法计算？ | 请引入类型检查，减少隐蔽的类型转换错误等 |


<a name="25f9c7fa"></a>
## 总结

1. Flow 或者 TypeScript 都是静态类型检查的优秀解决方案，能够给有类型检查需求的一定规模的项目带来实际收益。
2. Flow+Vue目前看来有些使用上的不便，期待尽早解决open issue，能够自动识别Vue组件文件的标签，从而使得 Flow 在 vue 项目中的使用更加流畅。

<a name="35808e79"></a>
## 参考资料

- [Flow 静态类型检查及在 Vue 项目中的使用](https://juejin.im/post/5967038d51882568b4630faa)
