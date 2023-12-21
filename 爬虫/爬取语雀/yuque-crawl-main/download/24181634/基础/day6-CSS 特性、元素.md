<a name="qPnmM"></a>
# CSS的三大特性
<a name="oEFyw"></a>
## 层叠性

1. 在同等权重下，代码自上而下解析：
- 遇到相同的属性值，下面的属性值会把上面的替换掉；
- 遇到不同的属性，就会叠加这个样式
2. 在不同的权重下，
- 遇到相同的属性修饰，听从权重较大的一方
- 遇到不同的属性，就会叠加这个样式
<a name="Jlxcs"></a>
## 继承性

1. 有一些属性是可以继承的：
- 父元素设置了之后，里面的子元素/孙子元素，都会具有这个形式
2. 那么，哪些属性可以继承呢？ 
- `font-开头` 
- `text-开头` 
- `li-开头` 列表 
- `color` 文字颜色
- `line-height` 行高
- `letter-spacing` 字间距
- `word-spacing` 词间距
3. 注意！
- 继承而来的权重为**0**，也就是说继承而来的样式，永远比不过设置在元素自己身上的权重。
<a name="hErZY"></a>
## 特殊性

1. 元素本身具有样式是大于继承而来的
2. 比如说超链接自带颜色，那么你给父元素设置颜色，超链接是不继承的，我本身的样式大于继承而来的
3. 如果你想更改超链接的文字颜色，或者去除超链接下划线，一定要设置在超链接元素身上，给超链接的父元素设置则无效!!!
```html
<head>
    <meta charset="UTF-8">
    <title>CSS三大特性</title>
    <style>
        #cc {
            color: yellow;
        }

        span {
            color: red;
            background: pink;
            color: palegreen;
        }

        span {
            color: blue;
        }

        /* ---------------------继承性---- */
        #box {
            width: 400px;
            height: 200px;
            background: cyan;
            font-size: 20px;
            color: red !important;
        }

        b {
            color: yellow;
        }

        #demo {
            color: red;
        }
    </style>
</head>

<body>
    <span id="cc">我是文字</span>
    <div id="box">
        我是div里面的文字
        <b>我是b里面的文字</b>
    </div>
    <div id="demo">
        <a href="javascript:;">我是特殊性</a>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648697335527-987c2a7c-3143-469b-a2f6-1a58be01191b.png#clientId=u95d2d27b-52f2-4&from=paste&height=252&id=ua328813e&originHeight=542&originWidth=896&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25236&status=done&style=stroke&taskId=uc8eabae6-9692-4f9c-b81a-c22dc04d799&title=&width=416.3999938964844)
<a name="arL1z"></a>
# 元素类型
<a name="Cjxfn"></a>
## 块状元素

1. 独占一行
2. 可以设置宽高
3. 可以设置上下左右`padding`、`border`、`margin`
4. 可以包裹嵌套任何元素
- `<p>`标签只能嵌套行内元素，`h1~h6`之间不能互相嵌套
5. 有宽高的块状元素，水平居中父元素 `margin:0 auto;`
- 块状元素如果设置浮动，那么`margin:0 auto;`失效
6. 块状元素有：
- `h1~h6``div``p``ol``ul``li``dl``dt``dd`
- `hr``br``form``marquee``iframe`
<a name="vdh4v"></a>
## 行内元素

1. 在一行显示
2. 大小由内容撑开
3. 不可以设置宽高，只能设置左右`padding`、`border`、`margin`
4. 可以嵌套行内元素，但是不能嵌套块状元素
5. 行内元素有
- `span``a``i``em``var``b``strong`
- `s``del``u``sup``sub``font（禁用）`
<a name="CrGDo"></a>
## 行内块元素

1. 在一行内显示
2. 可以设置宽高
3. 可以设置上下左右`padding`、`border`、`margin`
4. 行内块元素有`img``input``button`
5. 只有行内块元素才可以设置`vertical-align`（图片中心和其他元素对齐）这个属性，其余元素都无法设置
- 注意！`img``input`如果设置了浮动那么`vertical-align`属性失效
<a name="I4wmL"></a>
### vertical-align: middle; 示例
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            width: 600px;
            height: 400px;
            background: pink;
        }

        img {
            /* 让图片中心和其他元素对齐 */
            vertical-align: middle;
        }
    </style>
</head>

<body>
    <div>
        <img src="../images/1.jpg" alt="">
        <span>你好</span>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641550816816-41ef66c2-4cc7-4811-97e5-6d606954df50.png#clientId=u24b8c274-ec7f-4&from=paste&height=202&id=Yp0xl&originHeight=512&originWidth=760&originalType=binary&ratio=1&rotation=0&showTitle=false&size=62703&status=done&style=stroke&taskId=uf8e764ec-d9f3-4504-b814-445d02eeabd&title=&width=300)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641550188429-c4089bd2-487a-4ee3-8f0e-51b9892f95e7.png#clientId=u24b8c274-ec7f-4&from=paste&height=145&id=MrCqH&originHeight=249&originWidth=602&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45569&status=done&style=stroke&taskId=ufc831dac-9105-42f1-8505-3968e672360&title=&width=350)
<a name="TvGUO"></a>
## 可变元素 

1. 根据上下文来确实自己的元素类型
2. 可变元素有`button`
<a name="uMNAj"></a>
## 注意

1. 任何元素都可以设置浮动，元素设置浮动后，可以设置宽高
2. `margin:0 auto;`失效
3. 图片的`vertical-align`失效
<a name="lqyzE"></a>
# 元素类型的转换
<a name="UlOZ8"></a>
## 变块状/行内/行内块 display: block/inline/inline-block;

1. 变列表元素（li的默认值）`display: list-item;`
2. 变表格 `display: table;`
<a name="Q5DT3"></a>
## 变弹性盒 display: flex;

- 假设现在需要取消弹性盒，如何处理？
- `display: block;`直接将属性值换成其他的就好了
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        span {
            width: 200px;
            height: 300px;
            background: tomato;
            /* 将元素转换为块状元素 */
            display: block;
        }

        p {
            width: 300px;
            height: 200px;
            background: pink;
            /* 将元素转换为行内元素 */
            display: inline;
        }

        h2 {
            width: 100px;
            height: 100px;
            background: powderblue;
            /* 将元素转为行内块 */
            display: inline-block;
        }
    </style>
</head>

<body>
    <div>块状元素display:block</div>
    <span>变成块状元素</span>

    <b>行内元素display:inline</b>
    <b>行内元素display:inline</b>
    <b>行内元素display:inline</b>
    <p>变成行内元素</p>
    <p>变成行内元素</p>
    <p>变成行内元素</p>

    <h2>变成行内块</h2>
    <h2>变成行内块</h2>
    <h2>变成行内块</h2>
    <input type="text" value="行内块元素display:inline-block">
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648710050597-fa44df71-b4e4-4c87-b650-6346d5da47a3.png#clientId=u95d2d27b-52f2-4&from=paste&height=514&id=u0cfd72db&originHeight=642&originWidth=932&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43368&status=done&style=stroke&taskId=u833fe419-a6e2-4280-a910-efc9f45ba26&title=&width=745.6)
<a name="zEPFR"></a>
## 元素消失 display: none;

- [注意！区分开元素消失的几种展现方式](https://www.yuque.com/naiyoumitaocha/psyhak/to3zk9#aV4i2)
- 元素消失，在文档流不占位置（骨灰都扬了）
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1 {
            width: 200px;
            height: 200px;
            background: green;
        }

        .box2 {
            width: 200px;
            height: 200px;
            background: skyblue;
        }

        /* 鼠标滑过box1 元素消失 在文档流不占位置 */
        .box1:hover {
            display: none;
        }
    </style>
</head>

<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648710424606-b6daf4eb-f476-40fe-99d2-b8e2cc79a358.gif#clientId=u95d2d27b-52f2-4&from=drop&height=223&id=u7857c8f0&originHeight=566&originWidth=284&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14589&status=done&style=stroke&taskId=ub8b0688e-228e-43d3-834e-deece02d96a&title=&width=112)
<a name="EdtM3"></a>
## [置换/非置换元素](http://blog.doyoe.com/2015/03/15/css/%E7%BD%AE%E6%8D%A2%E5%92%8C%E9%9D%9E%E7%BD%AE%E6%8D%A2%E5%85%83%E7%B4%A0/)

- 置换元素：`img``input``textarea``select``object`
```html
    <input type="text"><!-- 元素本身有大小 -->
    <img src="" alt="。。"><!-- 元素本身有大小 -->
    <!-- 注意！行内块不是置换元素 -->
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641549796526-d2e3852b-fc12-417a-9137-4ba45a8f7bac.png#clientId=u24b8c274-ec7f-4&from=paste&height=55&id=u651df916&originHeight=44&originWidth=283&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1442&status=done&style=stroke&taskId=ue2a06906-4366-40fd-a7f5-91ea8224255&title=&width=352.5)
<a name="bSE8d"></a>
# 小结[元素类型 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956748996-eabf04f0-533d-427d-8c39-c31d1ec6724e.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956748996-eabf04f0-533d-427d-8c39-c31d1ec6724e.png%22%2C%22name%22%3A%22%E5%85%83%E7%B4%A0%E7%B1%BB%E5%9E%8B%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A569411%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u30c109aa-f366-492a-a0b5-1af12b0ac05%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u7971b7e8%22%2C%22card%22%3A%22file%22%7D)
