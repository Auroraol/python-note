<a name="hzTVY"></a>

# 浮动 float
<a name="xXwoM"></a>
## 左/右/不浮动 float: left/right/none;

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        img {
            float: right;
        }
    </style>
</head>

<body>
    <img src="../images/2.png" alt="">
    <p>小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子小寒吃饺子
    </p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648780961700-94fd55d4-7dbd-47c6-9d41-6052899ff4fc.png#clientId=u8db27ce7-2dcd-4&from=paste&height=361&id=u84fb7550&originHeight=451&originWidth=954&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55429&status=done&style=stroke&taskId=ub82626f6-191c-405f-8ea2-5ab91fe30a1&title=&width=763.2)
<a name="MJEMu"></a>
## 浮动示例
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1 {
            width: 200px;
            height: 200px;
            background: orangered;
            float: left;
        }

        .box2 {
            width: 210px;
            height: 210px;
            background: orange;
            float: left;
        }

        .box3 {
            width: 220px;
            height: 220px;
            background: tomato;
            float: left;
        }
    </style>
</head>

<body>
    <!-- .box*3 按tab按键 -->
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641710237879-fde87530-a104-44dc-ae0a-8e63f880db41.png#clientId=u72c3c4ac-30ae-4&from=paste&height=144&id=udd0555e0&originHeight=288&originWidth=802&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1661&status=done&style=stroke&taskId=u8fc54331-7afb-4bd2-9f4a-8176574fb7b&title=&width=401)
<a name="k13FF"></a>
## 浮动特性（重要）

1. 浮动元素**脱离文档流**了，不占据位置
2. 任何元素**都**可以设置浮动
3. 任何元素（针对行内）设置浮动之后
- **都**可以设置宽高；
- **都**可以设置上下左右`padding`、`border`、`margin`
4. 元素设置了浮动，没有写高度，那么**行高**就是它的高度
5. 元素设置了浮动，没有写宽度，那么元素内容的大小就是它的宽度
6. 版心不可以设置浮动
- 元素设置浮动后`margin: 0;``vertical-align`属性失效
7. 子元素设置浮动后，父元素不写高度，父元素则出现高度塌陷
- [高度塌陷的解决办法](https://www.yuque.com/naiyoumitaocha/psyhak/to3zk9#yj2iU)
<a name="QWRq3"></a>

## 行内元素设置浮动后可设宽高练习

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        #nav {
            width: 1200px;
            height: 80px;
            background: #333;
            /* 有宽高的块状元素水平居中浏览器 */
            margin: 0 auto;
            /* 单行文本垂直居中 设置行高=高度值 */
            line-height: 80px;
        }

        a {
            color: #fff;
            /* 去除超链接下划线 */
            text-decoration: none;
            /* background: red; */
            /* 设置有边框 */
            border-right: 2px solid #ff0;
            padding: 0 20px;
            /* 设置左浮 */
            float: left;
            /* 子元素设置浮动 父元素一定要写高度 也就是#nav{line-height: 80px;} */
        }

        a:hover {
            background: #f90;
        }
    </style>
</head>

<body>
    <div id="nav">
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
        <a href="javascript:;">产品中心</a>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648690568332-042100ff-6b34-4c41-b310-784ab4d66cf0.gif#clientId=ua9f56957-b7c3-4&from=drop&id=ucec6de87&originHeight=90&originWidth=951&originalType=binary&ratio=1&rotation=0&showTitle=false&size=84408&status=done&style=stroke&taskId=uaf5c16a3-7af7-4ca4-84fc-fed843f1250&title=)
<a name="uuZXg"></a>
## 四个色块布局练习
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        .big {
            width: 962px;
            height: 500px; /* 如果不设置高度 则高度塌陷 */
            background: pink;
        }

        .son {
            width: 210px;
            height: 400px;
            background: cyan;
            float: left; /* 横向展现 */
            margin-right: 40px;
        }

        .son4 {
            margin-right: 0;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son son4"></div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641467830243-9a7a6a85-a77a-4038-934f-ff374f622525.png#clientId=uf477036d-9f10-4&from=paste&height=213&id=u98a86f50&originHeight=426&originWidth=813&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2441&status=done&style=stroke&taskId=u0e434919-e917-4cbf-ad0a-a511af1f92a&title=&width=406.5)
<a name="dd4Mn"></a>
## 头部练习
<a name="egLAP"></a>
### 去除聚焦线 outline: 0;
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641468491905-368f51d2-9832-43f9-bc4f-9333c0994f83.png#clientId=uf477036d-9f10-4&from=paste&height=25&id=u13397af3&originHeight=50&originWidth=269&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14454&status=done&style=stroke&taskId=u58159263-1830-4731-b107-183669e3d06&title=&width=134.5)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        /* 去除页面缝隙 */
        * {
            margin: 0;
            padding: 0;
        }

        #header {
            width: 962px;
            height: 100px;
            background: pink;
            margin: 0 auto; /* 有宽高的块状元素水平居中浏览器 */
        }

        #header img {
            /* 
                * 注意  图片img和输入框input
                * 可以设置上下padding  border  margin  
                * 还可以设置宽高  
            */
            margin-top: 33px;
        }

        input {
            float: right; /* 靠右呢  就是右浮 */ 
            margin-top: 37px;
            width: 223px;
            /* 
                * 输入框input
                * 可以设置上下padding border margin 
                * 还可以设置宽高 
            */
            height: 26px;
            border: 1px solid #e5e5e5;
            background: #f1f1f1 url(../images/4.png) no-repeat 203px center;
            outline: 0; /* 去除聚焦线 */
            text-indent: 2em; /* 首行缩进 */
        }
    </style>
</head>

<body>
    <!-- 因为外围是白色  所以直接写版心 -->
    <div id="header">
        <img src="../images/3.png" alt="">
        <input type="text" placeholder="SEARCH...">
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648691655747-1440d044-5433-42c4-b346-aa702acaaf77.gif#clientId=ua9f56957-b7c3-4&from=drop&id=u01deeb56&originHeight=87&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48411&status=done&style=stroke&taskId=ub6704634-9df5-46ce-ac80-0513072a804&title=)
<a name="vJgGj"></a>

# 浮动特性->跟随前一个浮动元素

- 注意！浮动元素的**位置**，是跟随**前一个**兄弟**浮动元素**来走的
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box1 {
            width: 800px;
            height: 400px;
            background: red;
            float: left;
        }

        .box2 {
            width: 500px;
            height: 200px;
            background: blue;
            float: left;
        }

        .box3 {
            width: 200px;
            height: 100px;
            background: yellow;
            float: left;
        }

        .box4 {
            width: 70px;
            height: 80px;
            background: #000;
            float: left;
        }

        .box5 {
            width: 180px;
            height: 400px;
            background: cyan;
            float: left;
        }

        .box6 {
            width: 730px;
            height: 40px;
            background: palegreen;
            float: left;
        }
    </style>
</head>

<body>
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
    <div class="box4"></div>
    <div class="box5"></div>
    <div class="box6"></div>
    <!--  <div class="box7"></div> -->
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641553214700-cbf1f669-4e1f-4040-a1df-f487db1e6bf0.png#clientId=u04b43f44-73ff-4&from=paste&height=95&id=uc6a22c13&originHeight=422&originWidth=1592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8590&status=done&style=stroke&taskId=u3b61fda4-418e-44ba-bba5-ec4f098e779&title=&width=359.3999938964844)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641553507480-ed3c1b1a-d04c-4cdf-8025-ef36be56765d.png#clientId=u04b43f44-73ff-4&from=paste&height=125&id=u45993931&originHeight=550&originWidth=1600&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46402&status=done&style=stroke&taskId=u8e8ccd12-0a37-47fd-9021-cab94b4e8fe&title=&width=364.3999938964844)
<a name="jhmZq"></a>
# 小米色块练习
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        #mainWrapper {
            /* 外围只写背景颜色 */
            background: #f5f5f5;
        }

        #main {
            height: 705px;
            width: 1227px;
            background: black;
            /* 有宽高的块状元素 整体水平居中 */
            margin: 0 auto;
        }

        /* 因为这10个小块  宽度一致  */
        .son {
            width: 234px;
            float: left;
        }

        .son1 {
            height: 614px;
            background: pink;
        }

        .son2 {
            height: 300px;
            background: green;
            margin-bottom: 14px;
            margin-left: 14px;
        }

        .son3 {
            height: 143px;
            background: skyblue;
            margin-bottom: 14px;
            margin-left: 14px;
        }
    </style>
</head>

<body>
    <!-- 因为外围有颜色  所以写外围+版心 -->
    <div id="mainWrapper">
        <!-- 外围 -->
        <div id="main">
            <!-- 版心 -->
            <div class="son son1">1</div>
            <div class="son son2">2</div><!-- 之所以都命名为son2是因为图片大小一致 -->
            <div class="son son2">3</div>
            <div class="son son2">4</div>
            <div class="son son2">5</div>
            <div class="son son2">6</div>
            <div class="son son2">7</div>
            <div class="son son2">8</div>
            <div class="son son3">9</div><!-- 之所以都命名为son3是因为图片大小一致 -->
            <div class="son son3">10</div>
        </div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649069256649-2489df80-469d-4925-8747-fe5d052a5b5c.png#clientId=ub512f469-4ca6-4&from=paste&height=354&id=u1f1339d1&originHeight=442&originWidth=944&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3935&status=done&style=stroke&taskId=u9cf85f51-c650-4df8-b172-4713403af64&title=&width=755.2)
<a name="bWxRY"></a>
## 小米单独块练习
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .son2 {
            width: 243px;
            height: 300px;
            background: pink;
            text-align: center;
        }

        .photo {
            width: 243px;
            height: 200px;
            background: palegreen;
            /* 让图片在这个区域垂直水平居中 */
            /* text-align: center; */ /* 给son2设 */
            /* 垂直居中  先设置行高=高度值 */
            line-height: 200px;
        }

        .photo img {
            vertical-align: middle;
            /* 让图片中线在div垂直居中，参考day6-CSS特性、元素 */
        }

        /* 因为文字颜色  文字大小  text-开头的可以继承  所以直接 设置给父元素dl */
        dl {
            font-size: 12px;
            color: #333333;
            /* text-align: center; */ /* 给son2设 */
        }

        dd {
            margin-top: 11px;
            margin-bottom: 18px;
            color: #c1b0b7;
        }

        span {
            color: #ff7e00;
        }
    </style>
</head>

<body>
    <div class="son2">
        <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
            <img src="../images/1.jpg" alt="">
        </div>
        <!-- 三行字 -->
        <dl>
            <dt>小米电视6 65” OLED</dt>
            <dd>小米电视6 65″OLED</dd>
            <span>6999元</span>
        </dl>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649069380224-f48111ce-2b15-4a90-8d90-2d0093976173.png#clientId=ub512f469-4ca6-4&from=paste&height=275&id=ucd887ba2&originHeight=447&originWidth=361&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49862&status=done&style=stroke&taskId=u0bf6f6bd-a35c-4d53-990e-57ca88132c9&title=&width=221.8000030517578)
<a name="Y4Xxd"></a>

# 小结[浮动 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956433834-285f07be-5d22-463e-a75c-11af6b2b90cb.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956433834-285f07be-5d22-463e-a75c-11af6b2b90cb.png%22%2C%22name%22%3A%22%E6%B5%AE%E5%8A%A8%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A304521%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ua4defc1b-ff42-4388-9d57-adbba3411fb%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u1d846f18%22%2C%22card%22%3A%22file%22%7D)
