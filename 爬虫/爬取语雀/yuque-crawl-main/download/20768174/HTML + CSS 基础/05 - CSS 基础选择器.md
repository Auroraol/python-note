<a name="Wov51"></a>

# 1.元素选择器
- 用在页面中某一类的标签统一去掉某些样式
- `div {}` 相当于给页面中所有的div添加相同的样式
- 用法：
   1. 用在a标签：去掉下划线和颜色
   2. 用在li标签：去掉列表标识符
   3. 用在img标签：去掉基线对齐
   <a name="hL16G"></a>

#  2.类选择器(重点)

- 给元素起类名 `<div class="box">1</div>`
- 添加样式方法 `.box {}`
- 类名命名规则：
   - 见名知意，可以包含小写字母、数字、_、-，小写字母开头
   - 数字不允许开头
- 元素可以拥有多个类名 `<div class="one two three"></div>`
   - 必须写在一个class内部，类名空格隔开
   - 一个类名可以被多个元素使用
- 也可以写成 `div.box`，代表类名为box的div标签
<a name="pQMOe"></a>
# 3.id选择器

- 给元素起一个id名 `<div id="content">content</div>`
-  添加样式 `#content {}`
- id选择器限制
   - 一个元素只能有一个id名,一个id名只能被使用一次
   - 因为唯一性
- 用在哪
   - 一般给大板块起id名,内部其他元素一般用类名
   <a name="JU05V"></a>

# 4.通配符选择器/通用选择器

- * 代表页面中所有的标签
- 带有默认内外边距的元素：
   - body,p,h1,h2,h3,h4,h5,h6,ul,ol,li,dl,dt,dd,input
- 一般清除页面所有元素的内外边距
```css
* {
  margin:0;
  padding:0;
}
/*
	margin代表外边距
	padding代表内边距
	css中值为0，可以不带单位
*/
```
<a name="tpOQw"></a>
# 5.群组选择器

- 多个元素应用一套样式,用逗号进行分隔 `.box , #wrap , .content {}`
<a name="FjLHT"></a>
# 6.子代选择器：

- IE6不识别
- > 前后一定是父子关系
- 利用父亲的名字统一给所有的某一类子元素添加样式,省去了给每一个子元素起类名
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
				/*方法一：不建议用元素选择器，因为并未这个页面所有li都是这个样式*/
        /* li {
            width: 100px;
            height: 100px;
            background-color: red;
        } */

				/*方法二：如果给每一个li起一个类名叫one,是极好的,但如果li太多了，起名也太多*/
        /* .one {
            width: 100px;
            height: 100px;
            background-color: red;
        } */

				/*方法三：给父元素起个名字box,他里面的所有li标签设置样式*/
        .box>li {
            width: 100px;
            height: 100px;
            background-color: red;
        }

				/*方法四：选择器写的太多了,还不如方法三*/
        .wrap>.box>li {
            width: 100px;
            height: 100px;
            background-color: red;
        }
    </style>
</head>
<body>
    <!-- 给6个li添加宽高100，背景颜色是红色 -->
    <div class="wrap">
        <ul class="box">
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
            <li>6</li>
        </ul>
    </div>
</body>
</html>
```
<a name="bXRGK"></a>
# 7.后代选择器

- 空格隔开，慎重使用
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
				/*wrap中所有的a标签都可以被选中*/
        .wrap a {
            color: red;
        }

				/*box中所有的a标签都可以被选中*/
        .box a {
            color: red;
        }
    </style>
</head>
<body>
    <div class="wrap">
        <a href="#">aaaa</a>
        <ul class="box">
            <li>
                <a href="#">1</a>
            </li>
            <li>
                <a href="#">2</a>
            </li>
            <li>
                <a href="#">3</a>
            </li>
            <li>
                <a href="#">4</a>
            </li>
        </ul>
    </div>
</body>
</html>
```
<a name="Dq8gD"></a>
# 8.伪类选择器

- 鼠标移入效果 :hover
- 拓展了解-面试题：
   - 一般用于超链接，需要按照如下顺序书写才能生效
   - :link访问前 :visited访问后 :hover鼠标移入 :active激活 的使用顺序（love-hate）
```css
a:link {color: red;}        /* 未访问的链接状态 */
a:visited {color: green;}		/* 已访问的链接状态 */
a:hover {color: blue;}      /* 鼠标滑过链接状态 */
a:active {color: yellow;}   /* 鼠标按下去时的状态 */
```

<a name="OlFFh"></a>
# 9.选择器权值计算

- 元素选择器 1
- 类选择器 10
- id选择器 100
- 行内样式 1000
- 属性后面添加!important 权值最高
- 计算权值：
   -  `.wrap > ul > li` :12
   - ` #wrap li .box` :111
   - `#wrap , .box` :权值不可累加，分开计算
- 权值实际应用
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
				/*先统一设置所有li的样式，然后单独把spe的背景色改掉*/
        .wrap li {
            width: 100px;
            height: 100px;
            background-color: pink;
        }
				/*.spe的权值为10,上面为11,无法覆盖
					想办法提高.spe的权值即可或者给他的属性添加!important
				*/
        /* .spe {
            background-color: green !important;
        }  */
    </style>
</head>
<body>
    <div class="wrap">
        <ul>
            <li>1</li>
            <li class="spe">2</li>
            <li>3</li>
            <li>4</li>
        </ul>
    </div>
</body>
</html>
```
