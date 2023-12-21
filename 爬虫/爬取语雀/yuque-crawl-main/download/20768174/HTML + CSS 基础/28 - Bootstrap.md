- Bootstrap 是最受欢迎的 HTML、CSS 和 JS 框架，用于开发响应式布局、移动设备优先的 WEB 项目。
- 地址：[https://v3.bootcss.com/](https://v3.bootcss.com/)
- 优点
   - 标准化的html+css编码规范。
   - 提供了一套简洁、直观、强悍的组件。
   - 有自己的生态圈，不断的更新迭代。
   - 让开发更简单，提高了开发的效率。

---

<a name="j2MHN"></a>
# 1.安装步骤

- 下载安装包
- 引入目录文件
- 使用 <link>标签引入bootstrap.css 或者 bootstrap.min.css
```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <!-- 要求当前网页使用IE浏览器最高版本的内核来渲染 -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

    <!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
    <!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
    <!--[if lt IE 9]>
      <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>你好，世界！</h1>

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js" integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ" crossorigin="anonymous"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd" crossorigin="anonymous"></script>
  </body>
</html>
```
<a name="GEqhZ"></a>
# 2.使用方法

- 在官网 CSS样式和组件中查找，粘贴对应代码即可
- bootstrap 是通过类名来实现不同的样式，所以元素可以改变，用类名就可以了
- 如何更改定义好的组件样式？
   - 添加一个新的类名
<a name="iiFhP"></a>
# 3.布局容器

- Bootstrap 需要为页面的内容和栅格系统包裹一个 .container 容器(预定义类)，Bootstrap提前定义好了样式，我们就不需要写媒体查询了
- container
   - 响应式布局容器，固定宽度
      - 大屏(>=1200px) 宽度定为1170px
      - 中屏(>=992px) 宽度定为970px
      - 小屏(>=768px) 宽度定为750px
      - 超小屏 (100%)
   - 有默认的左右15px的内边距
- container-fluid
   - 流式布局容器 宽度百分百，占据全部视口
   - 适合于单独做移动端开发
   - 有默认的左右15px的内边距
<a name="Ox8SW"></a>
# 4.栅格系统

- 栅格系统，英文名grid systems，也叫网格系统，用于通过一系列的行（row）与列（column）的组合来创建页面布局，你的内容就可以放入这些创建好的布局中。
- Bootstrap框架提供了一套响应式、移动设备优先的流式栅格系统，就是将容器(container)平分成12列。

![2021-11-20_221037.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637417465831-b727ccdc-d11f-4c45-b3b1-06a4c5b559f9.jpeg#averageHue=%23bdcbda&clientId=u5b2ce3d4-6c54-4&from=ui&height=634&id=u8eb428fa&originHeight=976&originWidth=1540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=222070&status=done&style=none&taskId=uce4da73c-4e7e-4cb5-8ec6-452d6e58678&title=&width=1000)

- 先有行row再有列column，列column是行row的唯一子元素，我们的内容要放置在列column中。
<a name="qzme2"></a>
# 5.简单使用栅格系统
![2021-11-20_223330.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637418847563-f8854715-8274-4e8a-9d52-3064ac57f16c.jpeg#averageHue=%23accceb&clientId=u5b2ce3d4-6c54-4&from=ui&height=222&id=ufe7bb879&originHeight=484&originWidth=2178&originalType=binary&ratio=1&rotation=0&showTitle=false&size=127131&status=done&style=none&taskId=u20970e31-4dca-4d50-8e15-cb0f6d2f19c&title=&width=1000)

```html
<!--  -->
<div class="container">
  <div class="row">
    <div class="col-lg-3">1</div>
    <div class="col-lg-3">2</div>
    <div class="col-lg-3">3</div>
    <div class="col-lg-3">4</div>
  </div>
  <div class="row">
    <div class="col-lg-6">1</div>
    <div class="col-lg-1">2</div>
    <div class="col-lg-1">3</div>
    <div class="col-lg-4">4</div>
  </div>
</div>
```

- row 具体作用：去除父容器左右15px的外边距，可加可不加。如果添加必须放在 .container 内部
- 每一列都有默认的15px左右内边距padding
- 如果列数少于或者多于12份会怎么样？(如下)
```html
<div class="container">
  <!-- 少于12，则占不满 -->
  <div class="row">
    <div class="col-lg-1">1</div>
    <div class="col-lg-1">2</div>
    <div class="col-lg-1">3</div>
    <div class="col-lg-1">4</div>
  </div>
  <!-- 多于12，则换行 -->
  <div class="row">
    <div class="col-lg-5">1</div>
    <div class="col-lg-5">2</div>
    <div class="col-lg-5">3</div>
    <div class="col-lg-5">4</div>
  </div>
</div>
```

- 每一列可以设置多个类名，以便在不同分辨率下划分不同的份数(如下)
   - Bootstrap官网设置效果
```html
<!-- 大屏幕一行4列,中等屏幕一行3列,小屏幕一行2列,超小屏幕一行1列-->
<div class="container">
  <div class="row">
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">1</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">2</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">3</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">4</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">1</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">2</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">3</div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">4</div>
  </div>
</div>
```
<a name="trcfb"></a>
# 6.栅格中的列嵌套

- 在已经划分好的列当中再次进行12列的划分
```html
<div class="container">
  <div class="row">
    <div class="col-sm-6">
      <div class="row">
        <div class="col-sm-4">1</div>
        <div class="col-sm-4">1</div>
        <div class="col-sm-4">1</div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="row">
        <div class="col-sm-6">2</div>
        <div class="col-sm-6">2</div>
      </div>
    </div>
  </div>
</div>
```
<a name="VZF9E"></a>
# 7.列偏移
![2021-11-20_232250.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637421815588-23bf6d93-561e-4969-9a88-bb445b326af7.jpeg#averageHue=%23f1eadf&clientId=u5b2ce3d4-6c54-4&from=ui&height=30&id=ua663bebb&originHeight=100&originWidth=2325&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69128&status=done&style=none&taskId=u70361d04-844d-49c3-842f-c02025be4ec&title=&width=700)

- col-*-offset-* 向右偏移几等份
   - 实际就是给元素添加了左侧的外边距margin，浏览器计算得出来的
```html
<!-- 左右布局 -->
<div class="container">
  <div class="row">
    <div class="col-sm-4">1</div>
    <div class="col-sm-3 col-sm-offset-5">2</div>
  </div>
</div>
<!-- 水平居中,不能再用margin:auto;实现居中 -->
<div class="container">
  <div class="row">
    <div class="col-sm-8 col-sm-offset-2">中间</div>
  </div>
</div>
```
<a name="kLdWz"></a>
# 8.列排序
![2021-11-20_233246.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637422382425-8036ee85-2352-47a1-9a3f-564d8744afc1.jpeg#averageHue=%23c7daf0&clientId=u5b2ce3d4-6c54-4&from=ui&height=116&id=u82ace2af&originHeight=343&originWidth=2062&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35148&status=done&style=none&taskId=ubb4b2ab8-eaa1-49b1-8096-66a793c6cc4&title=&width=700)

- col-*-pull-* 向前拉几等份
- col-*-push-* 向后推几等份
   - 往右是推push，往左是拉pull
```html
<div class="container">
  <div class="row">
    <div class="col-sm-4 col-sm-push-8">左</div>
    <div class="col-sm-8 col-sm-pull-4">右</div>
  </div>
</div>
```
<a name="W7V9u"></a>
# 9.响应式工具

- 为了加快对移动设备友好的页面开发工作，利用媒体查询功能并使用这些工具类可以方便的针对不同设备展示或隐藏页面内容。
| **类名** | **超小屏** | **小屏** | **中屏** | **大屏** |
| --- | --- | --- | --- | --- |
| **.hidden-xs** | 隐藏 | 可见 | 可见 | 可见 |
| **.hidden-sm** | 可见 | 隐藏 | 可见 | 可见 |
| **.hidden-md** | 可见 | 可见 | 隐藏 | 可见 |
| **.hidden-lg** | 可见 | 可见 | 可见 | 隐藏 |

- 添加 visible-xx 可以显示某个元素
