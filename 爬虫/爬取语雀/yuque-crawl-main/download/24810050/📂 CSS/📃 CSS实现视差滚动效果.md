<a name="Z0U3R"></a>
## 视差滚动简介
**视差滚动（Parallax Scrolling）**是指让多层背景以不同的速度移动，形成立体的运动效果，带来非常出色的视觉体验。

我们可以把网页解刨成：背景层、内容层、悬浮层<br />![](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649828558365-48d8d51f-bb8f-4b4b-ab73-87386532d9e1.png#clientId=ua6c8a9eb-db7c-4&from=paste&id=u65bef683&originHeight=661&originWidth=845&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u24b8f24d-bafc-4874-adf3-af4bdea672f&title=)<br />当滚动鼠标滑轮的时候，各个图层以不同的速度移动，形成视觉差的效果。


<a name="yp2cN"></a>
## 使用background-attachment: fixed实现背景固定滚动视差效果
**background-attachment** 算是一个比较生僻的属性，基本上平时写业务样式都用不到这个属性。但是它本身很有意思。<br />background-attachment：如果指定了 background-image ，那么 background-attachment 决定背景是在视口中固定的还是随着包含它的区块滚动的。

**background-attachment的具体取值如下：**

- `**scroll**`: 默认值。此关键字表示背景相对于元素本身固定， 而不是随着它的内容滚动。
- `**local**`: 此关键字表示背景相对于元素的内容固定。如果一个元素拥有滚动机制，背景将会随着元素的内容滚动， 并且背景的绘制区域和定位区域是相对于可滚动的区域而不是包含他们的边框。
- `**fixed**`: 此关键字表示背景相对于视口固定。即使一个元素拥有滚动机制，背景也不会随着元素的内容滚动。
- `**inherit**`: 继承父元素background-attachment属性的值。

:::tips
注意一下 scroll 与 fixed，一个是相对元素本身固定，一个是相对视口固定，有点类似 position 定位的 absolute 和 fixed。
:::

通过设置样式 `background-attachment: fixed;`可以让背景固定，从而实现视差效果。

示例代码：
```less
<section class="g-word">Header</section>
<section class="g-img g-img1">IMG1</section>
<section class="g-word">Content1</section>
<section class="g-img g-img2">IMG2</section>
<section class="g-word">Content2</section>
<section class="g-img g-img3">IMG3</section>
<section class="g-word">Footer</section>
```
```less
@img1: 'https://dogefs.s3.ladydaily.com/~/source/unsplash/photo-1607212053115-d85fa8fddde4';
@img2: 'https://dogefs.s3.ladydaily.com/~/source/unsplash/photo-1559373098-7c09a893f57a';
@img3: 'https://dogefs.s3.ladydaily.com/~/source/unsplash/photo-1608551283138-5f08980b3fd4';

section {
  height: 100vh;
  background: rgba(0, 0, 0, .7);
  color: #fff;
  line-height: 100vh;
  text-align: center;
  font-size: 10vh;
}

.g-img {
  background-image: url(@img1);
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
  &.g-img2 {
    background-image: url(@img2);
  }
  &.g-img3 {
    background-image: url(@img3);
  }
}
```
效果如下：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/PoEBxYM)

<a name="vJIHX"></a>
## 使用 transform: translate3d 实现滚动视差
让我们先来看一下两个概念transform和perspective：

- `**transform**`: css3 属性，可以对元素进行变换(2d/3d)，包括平移 translate,旋转 rotate,缩放 scale,等等
- `**perspective**`: css3 属性，当元素涉及 3d 变换时，perspective 可以定义我们眼睛看到的 3d 立体效果，即空间感

3D视角示意图如下所示：<br />![640.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1649828987134-f37aa81f-39cc-4d40-8479-12ce8c291cb2.webp#clientId=ua6c8a9eb-db7c-4&from=drop&id=u8918e4de&originHeight=466&originWidth=893&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15072&status=done&style=none&taskId=uc714b7a5-85cb-434e-91cd-4c65f33271c&title=)




<a name="R3f9E"></a>
## 参考资料

- [Amazing！巧用 CSS 视差实现酷炫交互动效](https://mp.weixin.qq.com/s/5bNWeGewu67qQ2ICM7O0Sw)
- [CSS实现视差效果 - GitHub](https://github.com/chokcoco/iCSS/issues/37)
- [CSS Water Wave (水波效果)](https://www.oxxostudio.tw/articles/201407/css-water-wave.html)
- [面试官：如何使用CSS完成视差滚动效果?](https://mp.weixin.qq.com/s/zidEa2l1cG7wgTCdxXgFvw)



