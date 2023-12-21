<a name="TQ8EO"></a>

# 文字相关的属性
<a name="JhE49"></a>
## 文字大小 font-size

1. 单位`px`,`pt`
- `font-size: 16px;`浏览器默认文字大小为`16px`
- 文字大小低于`12px`之后，是不显示的
- `font-size: 9pt;`
- `9pt = 12px`
2. 数值为**偶数**（不可以设置为奇数）
```html
<head>
    <meta charset="UTF-8">
    <title>文字相关的属性</title>
    <style type="text/css">
        #box {
            width: 400px;
            height: 100px;
            background-color: pink;
            /* 文字大小 */
            /* font-size: 16px;浏览器默认文字大小为16px */
            font-size: 12px;/* 偶数 */
            font-size: 10px;/* 偶数 */
            /* 扩展 */
            font-size: medium;/* 16px */
            font-size: large;
            font-size: larger;
            font-size: x-large;
            font-size: xx-large;
            font-size: xxx-large;
            font-size: smaller;
            font-size: small;
            font-size: x-small;
        }
    </style>
</head>
<body>
    <div id="box">
        2022年1月4日
    </div>
</body>
```
<a name="Astym"></a>
## 文字颜色 color,rgb

1. `color: pink;`
2. 十六进制颜色
- 值 0 1 2 3 4 5 6 7 8 9 A B C D E F
- #12 3d fa
- `color:#aabbcc;`= `#abc`
```css
color: #05d2b3;
color: #ff0000;
color: #f00;
color: #66bb00;
color: #6b0;
color: #abc;
```

3. `rgb(颜色值,颜色值,颜色值)`
-   颜色值的取值`0~255`
```css
color: rgb(000, 000, 000);
color: rgb(255,255,255);
```

4. [透明度rgba](https://www.yuque.com/naiyoumitaocha/psyhak/eeo5te/edit#nGF01)
<a name="Pbvu1"></a>
## 文字字体 font-family
```css
font-family: "楷体";
font-family: 'Times New Roman';
font-family: '甲骨文','草书','楷体','宋体';
/* 后三个文字字体为备选，以便不显示甲骨文时候使用 */
```
<a name="ef6Fu"></a>
## 字体加粗 font-weight
<a name="U2H6K"></a>
### 文字加粗 font-weight: bold/bolder;
```css
font-weight: bold;
font-weight: bolder;
font-weight: 600; 
/* 600-900为加粗 */
```
<a name="emn9Q"></a>
### 加粗文字变常规文字 font-weight: normal;
```css
font-weight: 500;
font-weight: 400;
font-weight: normal;
```
<a name="fhfir"></a>
### 常规文字变细（字体轻量级变化）font-weight: lighter;
```css
font-weight: 300;
font-weight: 200;
font-weight: 100;
font-weight: lighter;
```
<a name="PIifG"></a>
## 文字倾斜 font-style
```css
font-style: oblique;
font-style: italic;
```
<a name="iX3KH"></a>
### 倾斜文字变常规文字 font-style: normal
```css
i,
em,
var {
    font-style: normal;
}
```
<a name="eYqQA"></a>
## 行高 line-height

1. **单行**文字，垂直居中：设置**行高=高度值**
2. 多行不行，会被挤出去
3. 适用场景：文字大小一致、颜色一致、多行之间有行间距 
```css
p{
    width: 600px;
    height: 200px;
    background-color: pink;
    line-height: 200px;/* 上下各100px */
}
```
<a name="Eh7bo"></a>
## 代码汇总
```html
<head>
    <meta charset="UTF-8">
    <title>文字相关的属性</title>
    <style type="text/css">
        #box {
            width: 400px;
            height: 100px;
            background-color: pink;
            /* 1.文字大小 */
            /* font-size: 16px;浏览器默认文字大小为16px */
            font-size: 12px;
            /* 偶数 */
            font-size: 10px;
            /* 偶数 */
            /* 扩展 */
            font-size: medium;
            /* 16px */
            font-size: large;
            font-size: larger;
            font-size: x-large;
            font-size: xx-large;
            font-size: xxx-large;
            font-size: smaller;
            font-size: small;
            font-size: x-small;
            /* 表示大小 还有另一个单位 pt 9pt=12px */
            font-size: 9pt;
            font-size: 12px;
            /* 2.文字颜色 */
            color: pink;
            /* 十六进制颜色值 0 1 2 3 4 5 6 7 8 9 A B C D E F
            R G B
            #12 3d fa  */
            color: #05d2b3;
            color: #ff0000;
            color: #66bb00;
            color: #abc;
            /* color:#aabbcc;= #abc */
            /* 颜色值还可以这样子表示rgb(颜色值,颜色值,颜色值)  颜色值的取值0~255 */
            color: rgb(000, 000, 000);
            color: rgb(255, 255, 255);
            /* 3.文字字体 */
            font-family: "楷体";
            font-family: 'Times New Roman';
            font-family: '甲骨文', '草书', '楷体', '宋体';
            /* 后三个文字字体为备胎，以便不显示甲骨文时候使用 */
            /* 4.文字加粗 */
            font-weight: bold;
            font-weight: bolder;
            font-weight: 600;
            /* 600/700/800/900为加粗 */
            /* 倾斜 */
            font-style: oblique;
            font-style: italic;
        }

        h1 {
            /* 4.1加粗文字变常规文字 */
            font-weight: 500;
            font-weight: 400;
            font-weight: normal;
            /* 4.2常规文字变细（字体轻量级变化） */
            font-weight: 300;
            font-weight: 200;
            font-weight: 100;
            font-weight: lighter;
        }

        /* 5.倾斜文字变常规文字 */
        i,
        em,
        var {
            font-style: normal;
        }

        /* 6.行高 */
        p {
            width: 600px;
            height: 200px;
            background-color: pink;
            line-height: 200px;
            /* 上下各100px */
            /* 单行文字 垂直居中 设置行高=高度值 */
            /* 多行不行，会被挤出去 */
        }
    </style>
</head>

<body>
    <p>文字文字</p>
    <i>周二</i>
    <em>周三</em>
    <var>周四</var>
    <h1>我想变成常规文字</h1>
    <div id="box">
        2022年1月4日
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648630177365-e239e270-5bb1-4672-8453-48826aab74ed.png#clientId=uf22decbc-5dcd-4&from=paste&height=347&id=u772a0b3e&originHeight=543&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14709&status=done&style=stroke&taskId=u34075b19-c053-4381-bb4a-a86f7beb03b&title=&width=490.4000244140625)
<a name="XAZAR"></a>
## 文字属性简写

- `font: 加粗 倾斜 文字大小/行高 "字体";`
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        div {
            width: 800px;
            height: 200px;
            background-color: pink;
            color: powderblue;
            /* 简写：font:加粗 倾斜 文字大小/行高 "字体" */
            font: bold italic 30px/200px "楷体";
            /* 简写：font:文字大小/行高 "字体" */
            font: 50px/200px "黑体";
            /* 简写：font:文字大小 "字体" */
            font: 60px "宋体";
            /* font语句会覆盖执行 */
        }
    </style>
</head>

<body>
    <div>文字</div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648774812307-716d10d4-3534-4535-8386-c8da5e4d90f3.png#clientId=u804e6896-fb0c-4&from=paste&height=110&id=u0a5cfa09&originHeight=262&originWidth=710&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5615&status=done&style=stroke&taskId=u26b64be8-be07-48fd-b0a6-db8ce3af2e4&title=&width=299)
<a name="hmFxO"></a>
## 小型大写字母 font-variant: small-caps;

- 把段落设置为小型大写字母字体
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        p {
            /* 将小写的英文 变成缩小版的大写英文 */
            font-variant: small-caps;
        }
    </style>
</head>

<body>
    <p>拓展 HELLO hello</p>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648774749301-2e91664c-98d2-4e9e-99fb-90db0ec111de.png#clientId=u804e6896-fb0c-4&from=paste&height=34&id=u2bbc1f62&originHeight=43&originWidth=170&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1272&status=done&style=stroke&taskId=u57c3cf61-1542-4585-af54-40d832c2c1a&title=&width=136)
<a name="rAGC9"></a>

# text 开头的属性

<a name="zABEP"></a>
## 首行缩进 text-indent: XXem

1. `em`是一个表示大小的单位
- 该值可以为**负值**
- 默认情况下`**1em= 16px**`**  **
2. `1em`表示一个文字的字体大小
3. `em`和该元素的字体大小相关
- 假设你设置`<p>`文字大小为`30px` 那么`1em=30px `
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        p {
            width: 500px;
            height: 300px;
            background-color: rgb(33, 66, 123);
            text-indent: 2em; /* 首行缩进 可以为负值 */
        }
    </style>
</head>

<body>
    <p>深入学习css深入学习css深入学习css深入学习css深入学习css深入学习css深入学习css</p>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648774863441-6186bf48-023b-4b3f-8a24-08ba04f56368.png#clientId=u804e6896-fb0c-4&from=paste&height=250&id=ud3e3da58&originHeight=396&originWidth=645&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9674&status=done&style=stroke&taskId=uef048ede-7640-430e-ba80-928b1147318&title=&width=407)
<a name="RcGzQ"></a>
## 文本水平居中/左/右/两端 text-align

- 注意：只能设置给**块状元素**（给行内元素设置无效）
```css
text-align: left;/* 居左 默认值 */
text-align: center;/* 居中 */
text-align: right;/* 居右 */
text-align: justify;/* 居两端 针对多行英文 */
```
<a name="rVRiR"></a>
## 文本修饰（下划线）text-decoration
```css
text-decoration: underline;/* 下划线 */
text-decoration: line-through;/* 中划线 */
text-decoration: overline;/* 上划线 */
/* 扩展 这个线可以 设置颜色： */
text-decoration: red underline;
```
```css
/* 去除页面所有超链接下划线 */
a {
    text-decoration: none;
}
```
<a name="KND0Z"></a>
## 检索英文字母大小写(了解）text-transform
```css
text-transform: uppercase;/* 全大写 */
text-transform: lowercase;/* 全小写 */
text-transform: capitalize;/* 首字母大写 */
```
<a name="WiEmG"></a>
## 代码汇总
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        p {
            width: 500px;
            height: 300px;
            background-color: rgb(33, 66, 123);
            /* 1.首行缩进 可以为负值 */
            text-indent: 2em;
            /* 2.文本水平居左/中/右/两端 */
            text-align: left;/* 居左 */
            text-align: center;/* 居中 */
            text-align: right;/* 居右 */
            text-align: justify;/* 居两端 针对多行英文 */
            /* 3.文本修饰（下划线） */
            text-decoration: underline;/* 下划线 */
            text-decoration: line-through;/* 中划线 */
            text-decoration: overline;/* 上划线 */
            /* 扩展 这个线可以 设置颜色： */
            text-decoration: red underline;
            /* 了解就好 4.检索英文字母大小写 */
            text-transform: uppercase;/* 全大写 */
            text-transform: lowercase;/* 全小写 */
            text-transform: capitalize;/* 首字母大写 */
        }

        /* 去除页面所有超链接下划线 */
        a {
            text-decoration: none;
        }
    </style>
</head>

<body>
    <p>DSDSFS FSFDSFRETRE SGFD GF深入学习css深入学习css深入学习css深入学习css深入学习css深入学习css深入学习css ssssssssssssss sssssssss ssssss s
        sssssssss ssss ssssss ss ssssssss ssssssss sssss sssssss ssssssssss sssssssssss sssssssss ss sssssssssss
        sssssssss ssssssss ssssssssss ssssss sss </p>
    <a href=":;">空链接</a>
</body>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648632147437-ba1e51f7-099b-4e97-a3af-1e2b21025f9f.gif#clientId=uf22decbc-5dcd-4&from=paste&height=273&id=udb06e818&originHeight=428&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29257&status=done&style=stroke&taskId=u957000eb-743b-47bf-80c5-f2f544d91b4&title=&width=451.3999938964844)
<a name="EpbyP"></a>

# 图片相关的属性 vertical-align

1. **图片默认自带3px间隙**，[如何解决图片3px问题](https://blog.csdn.net/qq_37855074/article/details/88826617)？
- img添加：`vertical-align: top;`
- img添加：`display: block;`
- **float**：浮动的意义就是为了解决缝隙
2. 注意！`vertical-align`这个属性只能给图片设置
- 给其他元素设置则无效
```css
vertical-align: baseline;	/* 默认值 图片基线（图片底部往下3px）和其他元素对齐 */
vertical-align: bottom;		/* 图片底部和其他元素对齐 */
vertical-align: middle;		/* 图片中心和其他元素对齐 */
vertical-align: top;			/* 图片上边和其他元素对齐（一般用来解决图片3px问题） */
```
![](https://cdn.nlark.com/yuque/0/2021/png/1158459/1638177918305-d6278b07-f43a-4972-9c2f-d797d885b1e0.png#from=url&id=yJZdA&originHeight=431&originWidth=1208&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=stroke&title=)
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        img {
            width: 100px;
            height: 100px;
            vertical-align: baseline; /* 默认值 图片基线（图片底部往下3px）和其他元素对齐 */
            vertical-align: bottom;		/* 图片底部和其他元素对齐 */
            vertical-align: middle;		/* 图片中心和其他元素对齐 */
            vertical-align: top;			/* 图片上边和其他元素对齐（一般用来解决图片3px问题） */
        }
    </style>
</head>

<body>
    <img src="https://aaludra.com/wp-content/uploads/2019/06/html5.gif" alt="">
    <span>你好</span>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648774930861-d6be09ab-4b4c-46a5-80c7-4dbdb12806cb.png#clientId=u804e6896-fb0c-4&from=paste&height=115&id=udf08524e&originHeight=144&originWidth=186&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5226&status=done&style=stroke&taskId=u4f29458e-8413-46a0-9863-c2fcec59721&title=&width=148.8)
<a name="a3F9f"></a>
## 图片垂直水平居中div  [vertical-align: middle;](https://www.jianshu.com/p/dea069fecb62)

1. 需要给`div`设置`text-align: center;`
- 目的是让`<img>`和`<span>`这一由两部分组合而成的整体在div布局上**水平**居中
2. 需要给`div`设置`line-height: 高度值; `
- 目的是让`<img>`在`div`上**垂直**居中，以`默认基线3px`来对齐（参考图上粉色线）
- 目的同时也是让`<span>`在`div`上**垂直**居中，
3. 需要给`img`设置`vertical-align: middle;`
- 目的是让图片**中线**在div上垂直居中
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            width: 600px;
            height: 400px;
            background: red;
            /* 文字/图片/input框  统称为文本 */
            /* 我们有一个css属性 文本水平居中 */
            text-align: center;
            /* 单行文本水平垂直居中 设置行高=高度值 */
            line-height: 400px;
        }

        img {
            vertical-align: middle;
            /* 由文字对准图片基线变成对准图片中间 */
        }
    </style>
</head>

<body>
    <div>
        <img src="../../img/logo.png" alt="">
        <span>你好</span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641709522243-bad28477-b82a-439c-a635-32ac580102a5.png#clientId=u01ffd19e-8f06-4&from=paste&height=140&id=u54ee0c1c&originHeight=832&originWidth=1210&originalType=binary&ratio=1&rotation=0&showTitle=false&size=91487&status=done&style=stroke&taskId=ucc78decb-cadc-42c5-9827-30795d6298d&title=&width=204)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641709416588-9ea23961-1460-4854-b954-d06a244129ef.png#clientId=u01ffd19e-8f06-4&from=paste&height=140&id=ud6f077d9&originHeight=942&originWidth=1404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135988&status=done&style=stroke&taskId=u26de2bb9-19e8-4335-9b57-bd8fa9e3e20&title=&width=208.40000915527344)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641552481565-2edc3b15-fe77-424d-93e1-1961e1c49eb4.png#clientId=u24b8c274-ec7f-4&from=paste&height=143&id=u8d95acc2&originHeight=435&originWidth=644&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39897&status=done&style=stroke&taskId=u0a297301-129d-4799-a594-845fee72813&title=&width=212)
<a name="jJvNw"></a>

# 扩展-字词间距

<a name="LCm3l"></a>
## 字间距 letter-spacing

- 用于**中文**
```css
div {
    letter-spacing: 20px;
}
```
<a name="WbJAe"></a>
## 词间距 word-spacing

- 用于**英文**（**空格隔开**，它是来识别空格的）
```css
p {
    word-spacing: 30px;
}
```
<a name="xBVGd"></a>
## 代码汇总
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        div {
            /* 字间距 用于中文 */
            letter-spacing: 20px;
        }

        p {
            /* 词间距 用于英文（空格隔开 它是来识别空格的） */
            word-spacing: 30px;
        }
    </style>
</head>

<body>
    <div>万事顺意，平安喜乐，nice</div>
    <p>sss sss ssssss sssss ssss ssssssss sssss</p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648632811658-fcef17d8-d226-429b-8c8a-156bed2f0471.png#clientId=uf22decbc-5dcd-4&from=paste&height=79&id=u4d855150&originHeight=99&originWidth=596&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3469&status=done&style=stroke&taskId=uba64386e-5f4d-4909-88c5-148b5c32973&title=&width=476.8)
<a name="TrQnA"></a>

# 列表的属性

<a name="vb0C7"></a>

## 去除样式 list-style: none;

```css
list-style: none;
```
<a name="oWNhh"></a>

## 更改小圆圈的样式 list-style-type

```css
list-style-type: disc;				/* 实心圆 */
list-style-type: circle;			/* 空心圆 */
list-style-type: square;			/* 正方实体 */
list-style-type: none;				/* 去除样式 */
list-style-type: decimal;			/* 阿拉伯数字 */
list-style-type: georgian;		/* 格鲁吉亚语言 */
list-style-type: lower-roman;	/* 小罗马 */
list-style-type: lower-greek;	/* 希腊 */
list-style-type: lower-latin;	/* 英文 */
```
<a name="IGMfY"></a>
## 更改列表小圆圈的位置 list-style-position

- 默认值在`li`外侧
```css
list-style-position: outside; /* 默认值 */
list-style-position: inside;  /* 在li内侧 */
```
<a name="tXEID"></a>
## 自定义图片为列表样式 list-style-image: url
```css
list-style-image: url(../images/1.jpg);
```
<a name="zgBOx"></a>
## 代码汇总
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style type="text/css">
        ul {
            background-color: skyblue;
            /* 1.注意！要背住的 是一个简写 是啥呢 去除列表样式 */
            /* list-style: none; */
            /* 2.更改小圆圈的样式 */
            list-style-type: disc;/* 实心圆 */
            list-style-type: circle;/* 空心圆 */
            list-style-type: square;/* 正方实体 */
            list-style-type: none;/* 去除样式 */
            list-style-type: decimal;/* 阿拉伯数字 */
            list-style-type: georgian;/* 格鲁吉亚语言 */
            list-style-type: lower-roman;/* 小罗马 */
            list-style-type: lower-greek;/* 希腊 */
            list-style-type: lower-latin;/* 英文 */
            /* 3.更改列表小圆圈的位置 默认值在li外侧 */
            list-style-position: outside;/* 默认值 */
            list-style-position: inside;/* 在li内侧 */
            /* 4.自定义图片为列表样式 */
            list-style-image: url(../images/1.jpg);
        }

        li {
            background-color: slateblue;
        }
    </style>
</head>

<body>
    <ul>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
        <li>阿拉丁神灯许愿：年年有余</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648632990555-bae565f1-5a13-4cb1-bef5-7b84a5d2579d.png#clientId=uf22decbc-5dcd-4&from=paste&height=196&id=ub38390ed&originHeight=245&originWidth=955&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22256&status=done&style=stroke&taskId=u34762ab0-86e8-403f-9350-54d800aaa68&title=&width=764)
