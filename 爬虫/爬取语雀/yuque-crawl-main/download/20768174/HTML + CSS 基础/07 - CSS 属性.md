<a name="azxzo"></a>
# 1.列表属性
- 列表标识符
   - list-style-type:none无 / disc实心圆 / circle空心圆 / square实心矩形 / decimal数字;
- 列表图片
   - list-style-image:url();
- 标识符位置
   - list-style-position:inside;
- *** 去掉列表标识符
```css
li {
  list-style-type:none;
  /*或者*/
  list-style:none;
}
```
<a name="iRAhY"></a>

# 2.边框属性

- 四个方向边框的设置
   - border:粗细 线型 颜色;
   - 线型:solid直线 / dashed虚线 / dotted点状线 / double双线;
- 单方向边框的设置
   - 上边框
      - border-top:粗细 线型 颜色;
   - 下边框 `border-bottom`
   - 左边框 `border-left`
   - 右边框 `border-right`
- 面试题：利用边框制作一个三角形
   - transparent 代表透明
   -  width: 0px;代码不能删除
      - 块级元素如果不设置宽度,默认的宽度和父元素保持一致
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box {
            width: 0;
            border-top: 10px solid transparent;
            border-right: 10px solid transparent;
            border-bottom: 10px solid pink;
            border-left: 10px solid transparent;
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```
<a name="ICtCS"></a>

# 3.CSS 属性的继承性

- 不可继承的：display、margin、border、padding、background、height、min-height、max- height、、min-width、max-width、overflow、position、left、right、top、 bottom、z-index、float、clear、table-layout、vertical-align
- 所有元素可继承：visibility和cursor。
- 内联元素可继承：letter-spacing、word-spacing、line-height、color、font、 font-family、font-size、font-style、font-variant、font-weight、text- decoration、text-transform。
- 块状元素可继承：text-indent和text-align
- 列表元素可继承：list-style、list-style-type、list-style-position、list-style-image。
- 表格元素可继承：border-collapse。
1.  ***一般来说：font-,line-,text-,color,opacity有继承性
2. 注意：a标签继承不了color
3. 拓展知识：
   1. border: inherit; border的值继承与父元素的border值
   <a name="nF1V6"></a>
# 4.背景相关属性

- 背景图起装饰作用，img标签一般是页面内容
- 网页上常用的图片格式（压缩图片）
   - jpg :有损压缩格式，靠损失图片本身的质量来减小图片的体积，适用于颜色丰富的图像;(像素点组成的，像素点越多会越清晰 )
   - gif：有损压缩格式，靠损失图片的色彩数量来减小图片的体积，支持透明，支持动画，适用于颜色数量较少的图像
   - png:无损压缩格式，损失图片的色彩数量来减小图片的体积，支持透明，不支持动画，是fireworks的 源文件格式，适用于颜色数量较少的图像;
- 1、背景颜色 `background-color`
- 2、背景图 `background-image:url();`
   - 容器尺寸等于图片尺寸，背景图片正好显示在容器中
   - 容器尺寸大于图片尺寸，背景图片将默认平铺，直至铺满元素
   - 容器尺寸小于图片尺寸，只显示元素范围以内的背景图
- 3、背景重复
   - background-repeat:repeat默认值,重复 / no-repeat不重复,只出现一次 / repeat-x水平重复 / repeat-y垂直重复;
- 4、背景定位 `background-position:0px 0px;`
   - 第一个值代表水平位移,正方向移动给正值
      - right右、left左、center居中
   - 第二个值代表垂直位移,正方向移动给正值
      - top上、bottom下、center居中
- 5、背景简写形式
   - background:背景颜色 背景图路径 是否重复 背景定位;
- 6、背景固定 `background-attachment:fixed;`
   - 不随内容一块滚动
   <a name="xTfbN"></a>
# 5.CSS Sprites / 精灵图 / 雪碧图

- 将多个小图标拼合在一张大图上，通过背景属性引入进来，背景定位来调整具体想引入的背景图位置
- 优势
   - 减少加载网页图片时对服务器的请求次数
   - 图片体积较少，提高页面的加载速度
   <a name="g8P3m"></a>
# 6.透明度

- `background:rgba(255,255,255,0.4);`
   - 0.4代表40%的透明度,数值越小越透明。1代表不透明,0代表完全透明
- opacity:0-1之间的小数
   -  有继承性
- IE浏览器透明度的兼容方法
   - `filter:alpha(opacity=40);`
   - 0-100之间的整数
- 兼容写法：
```css
.box {
  background: #000;
  opacity: 0.4;
  filter:alpha(opacity=40);
}
```

<a name="cMsvy"></a>
# 7.溢出属性

- overflow:visible默认值,溢出可见 / hidden溢出隐藏 / scroll滚动条 / auto自动;
<a name="kX9Uc"></a>

# 8.单行文本省略号效果(面试题)

```css
.para {
  /* 设置宽度 */
  width:300px;
	/* 文本不换行 */
  white-space: nowrap;
  /* 溢出隐藏 */
  overflow: hidden;
  /* 添加省略号 */
  text-overflow: ellipsis;
}
```
<a name="FVFKp"></a>

# 9.拓展 - 多行文本省略号效果

```css
.box {
  width: 600px;
  border: 1px solid red;
  display: -webkit-box;
  overflow: hidden;  
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
```
