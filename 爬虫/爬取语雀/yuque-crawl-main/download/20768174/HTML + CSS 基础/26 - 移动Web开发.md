<a name="TZbXQ"></a>
# 1.手机浏览器现状
- 国内的UC和QQ，百度等手机浏览器都是根据Webkit修改过来的内核，国内尚无自助研发的内核，兼容移动端主流浏览器，处理webkit内核浏览器即可。
<a name="rPtUK"></a>
# 2.手机屏幕

- 移动端设备屏幕尺寸非常多，你会见识过很多种分辨率：480x800, 480x854, 540x960, 720x1280, 1080x1920……
- ppi：Pixels Per Inch也叫像素密度单位，所表示的是每英寸所拥有的像素数量。因此PPI数值越高，即代表显示屏能够以越高的密度显示图像。当然，显示的密度越高，拟真度就越高。

![2021-11-18_223141.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637245974678-8cfdcaf0-68fc-4684-afaa-b646e03518a9.jpeg#averageHue=%23d9e6cf&clientId=u26b143ab-680b-4&from=ui&height=206&id=u9a0670c8&originHeight=549&originWidth=1862&originalType=binary&ratio=1&rotation=0&showTitle=false&size=282226&status=done&style=none&taskId=u3c067031-f8ed-4c65-82e9-4474bd5c686&title=&width=700)

- Retina屏：所谓“Retina”是一种显示标准，是把更多的像素点压缩至一块屏幕里，从而达到更高的分辨率并提高屏幕显示的细腻程度，也称为视网膜显示屏。移动电话显示器的像素密度达到或高于300ppi就不会再出现颗粒感。
- dpr = 物理像素 / 逻辑像素(CSS和JS设置的代码)
- 在早先的移动设备中，并没有DPR的概念。随着技术的发展，移动设备的屏幕像素密度越来越高。从iphone4开始，苹果公司推出了所谓的retina视网膜屏幕。之所以叫做视网膜屏幕，是因为屏幕的PPI太高，人无法分辨出屏幕上的像素点。iphone4的分辨率提高了一倍，但屏幕尺寸却没有变化，这意味着同样大小的屏幕上，像素多了一倍，于是DPR = 2
| **手机型号** | **尺寸（对角线）** | **逻辑像素(px)** | **物理像素** | **倍数dpr** |
| --- | --- | --- | --- | --- |
| iPhone 4/4S | 3.5英寸 | 320x480 | 640x960 | @2x |
| iPhone 5/5S/5C | 4英寸 | 320x568 | 640x1136 | @2x |
| iPhone SE | 4英寸 | 320x568 | 640x1136 | @2x |
| iPhone 6 | 4.7英寸 | 375x667 | 750x1334 | @2x |
| iPhone 6 Plus | 5.5英寸 | 414x736 | 1242x2208 | @3x |
| iPhone 6S | 4.7英寸 | 375x667 | 750x1334 | @2x |
| iPhone 6S Plus | 5.5英寸 | 414x736 | 1242x2208 | @3x |
| iPhone 7 | 4.7英寸 | 375x667 | 750x1334 | @2x |
| iPhone 7 Plus | 5.5英寸 | 414x736 | 1242x2208 | @3x |
| iPhone 8 | 4.7英寸 | 375x667 | 750x1334 | @2x |
| iPhone 8 Plus | 5.5英寸 | 414x736 | 1242x2208 | @3x |
| iPhone X | 5.8英寸 | 375x812 | 1125x2436 | @3x |
| iPhone XS | 5.8英寸 | 375x812 | 1125x2436 | @3x |
| iPhone XS Max | 6.5英寸 | 414x896 | 1242x2688 | @3x |
| iPhone XR | 6.1英寸 | 414x896 | 828x1792 | @2x |
| iPhone 11 | 6.1英寸 | 414x896 | 828x1792 | @2x |
| iPhone 11 Pro | 5.8英寸 | 375x812 | 1125x2436 | @3x |
| iPhone 11 Pro Max | 6.5英寸 | 414x896 | 1242x2688 | @3x |

![2021-11-18_230147.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637247721212-a857939a-ccbf-4a42-ac1d-4af1a2708e89.jpeg#averageHue=%23f7f1f0&clientId=u26b143ab-680b-4&from=ui&height=200&id=u6a4230a5&originHeight=354&originWidth=1060&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32343&status=done&style=none&taskId=u931e545b-c1a7-404c-812f-bea129d2dbc&title=&width=600)<br />![图片1.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1637305450573-fcf0ae76-a8bc-42d6-a5e5-3675d219c8f3.png#averageHue=%23f2f4f2&clientId=ued7210db-342a-4&from=ui&height=394&id=u046529cb&originHeight=348&originWidth=530&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82591&status=done&style=none&taskId=ub22e6036-c5c9-4bc5-9a9b-54d01257251&title=&width=600)
<a name="q81ZP"></a>
# 3.二倍图与三倍图

- 对于一张 50 x 50px 的一张图片，在Retina屏中打开，按照物理像素比，图片会被放大到二倍，会造成图片模糊，所以我们开发中会使用二倍图
- 相当于UI设计师给你一张iphone6的设计稿，尺寸是 750x1334，这上面的图片我们给切出来，尺寸是100 x 100px，然后我们在代码中给这个二倍图img{width:50px;height:50px;}，就可以解决图片模糊问题了。
- 我们一般都会处理img和背景图尺寸的

![2021-11-18_233142.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637249516671-452d42d5-076b-4f19-8fde-6ae1d8302505.jpeg#averageHue=%23a5e6a9&clientId=u26b143ab-680b-4&from=ui&height=152&id=k4eOg&originHeight=326&originWidth=645&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29190&status=done&style=none&taskId=u893bb000-f76e-474d-acce-44c229f0677&title=&width=300)

- 扩展：cutterman切图神器
<a name="xAYK2"></a>
## 3.1扩展：如何根据分辨率切换不同图片

- 1.关于移动端浏览器像素缩放比：window.devicePixelRatio
```javascript
var img = document.querySelector("img")
if (window.devicePixelRatio == 2) {
	img.src = "二倍图.jpg"
}
if (window.devicePixelRatio == 3) {
	img.src = "三倍图.jpg"
}
```

- 2.给img设置 `<img src="图片1.jpg" srcset="图片2.jpg 2x, 图片3.jpg 3x"`
<a name="JkDVX"></a>
# 4.视口

- 为了使网站在移动端有最理想的浏览宽度而设定的

`<meta name="viewport" content="width=device-width,initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0 ,user-scalable=no">`

| 属性 | 解释 |
| --- | --- |
| width | 宽度设置的是viewport宽度，可以设置device-width特殊值 |
| initial-scale | 初始缩放比，大于0的数字 |
| maximum-scale | 最大缩放比，大于0的数字 |
| minimum-scale | 最小缩放比，大于0的数字 |
| user-scalable | 用户是否可以缩放，yes或no（1或0） |

<a name="i8WKd"></a>
## 标准视口 

- 页面的宽度和设备样宽
- 默认的缩放比例是1.0
- 不允许用户去缩放页面
<a name="ZzWw3"></a>
# 5.移动开发选择

- 通过判断设备，如果是移动设备打开，则跳转到移动端页面
   - 京东，移动设备，刷新
- 响应式页面
<a name="KAqwT"></a>
# 6.移动端css初始化

- 地址：[https://necolas.github.io/normalize.css/](https://necolas.github.io/normalize.css/)
- Normalize.css 只是一个很小的CSS文件，但它在默认的HTML元素样式上提供了跨浏览器的高度一致性。相比于传统的CSS reset，Normalize.css是一种现代的、为HTML5准备的优质替代方案。Normalize.css现在已经被用于许许多多其他框架、工具和网站上。
<a name="rJaAO"></a>
# 7.移动端特殊样式的解决办法

- 避免宽度溢出 造成横向滚动条
   - `box-sizing: border-box;`
   - `-webkit-box-sizing: border-box;`
- 点击清除背景高亮效果
   - `-webkit-tap-highlight-color: transparent;`
- IOS环境下的按钮都是通过美化的，加它能给按钮和输入框去掉默认样式
   - `-webkit-appearance: none;`
- 禁用长按页面时的弹出菜单
   - `img,a {-webkit-touch-callout:none;}`
<a name="PTJkO"></a>
# 8.移动端常见页面布局

- 流式布局 / 百分比布局
   - 外层盒子要设置 min-width 和 max-width
   - 京东
```css
body {
  margin: 0 auto;
  min-width: 320px;
  max-width: 640px;
  background: #fff;
  font-size: 14px;
  font-family: -apple-system,Helvetica,sans-serif;
  line-height: 1.5;
  color: #666;
}
```

- flex 弹性布局 （推荐）
- calc 浮动布局

![图片3.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1637305385177-eb95ffc3-5075-49ab-ada0-6ca6498430b2.png#averageHue=%23c0bfbf&clientId=ued7210db-342a-4&from=ui&id=uf9bc6953&originHeight=559&originWidth=287&originalType=binary&ratio=1&rotation=0&showTitle=false&size=91367&status=done&style=none&taskId=uaedd81f6-a364-4e14-8b2a-5940b3d2e6e&title=)![图片4.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1637305385170-e0389c2e-1052-4033-a8d8-daab23c829df.png#averageHue=%23cfcece&clientId=ued7210db-342a-4&from=ui&id=ud59e1925&originHeight=436&originWidth=498&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67140&status=done&style=none&taskId=u8344530b-fe14-4aaf-bacc-b35b2079220&title=)

- 媒体查询 + rem 布局
- flexible.js
   - flexible.js是手淘开发出的一个用来适配移动端的js框架。框架的核心原理就是根据不同的width给网页中html根节点设置不同的font-size，然后所有的px都用rem来代替，这样就实现了不同大小的屏幕都适应相同的样式了。
- vw + rem 布局

![图片6.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1637305412387-06fcf593-6d60-453a-bb56-fab31e60abd5.png#averageHue=%238d7e6d&clientId=ued7210db-342a-4&from=ui&id=u83f98dbb&originHeight=548&originWidth=285&originalType=binary&ratio=1&rotation=0&showTitle=false&size=210848&status=done&style=none&taskId=udde2db25-2bad-4914-9a9c-3e73d32a6f9&title=)![图片7.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1637305412602-17954bbd-c46a-43c5-a70f-558648b8e0d7.png#averageHue=%23868073&clientId=ued7210db-342a-4&from=ui&id=ud5d1abf0&originHeight=591&originWidth=319&originalType=binary&ratio=1&rotation=0&showTitle=false&size=255857&status=done&style=none&taskId=u9e546263-6c65-47e3-94f6-26fc6bcee08&title=)

- 混合布局
- 响应式
- Bootstrap框架
