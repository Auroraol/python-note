<a name="PTVy5"></a>

# 内容区 content

```css
div {
    width: 200px;
    height: 200px
}
```

1. 说白了就是你设置的宽高，如上面的案例，代表内容区就是200*200的
2. 如果说你没有设置宽高，那就是内容撑开的高度，宽度需要看你是什么元素类型
- 假设是<p>标签，那么高度是<p>里面内容撑开的高度，宽度独占一行(块状元素)
- 假设是<span>标签，那么宽高都是内容撑开的(行内元素)
<a name="t0bhX"></a>

# 内填充/补白区/内边距 padding

```css
padding-left: 50px;   /* 左内填充 */
padding-right: 100px; /* 右内填充 */
padding-top: 30px;		/* 上内填充 */
padding-bottom: 50px; /* 下内填充 */
```
<a name="OmCyS"></a>
## 复合属性
```html
<head>
    <meta charset="UTF-8">
    <title>盒子模型</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        div {
            width: 200px;
            height: 200px;
            background: #01acde;
            /* 边框border 会不会撑大盒子 会的 */
            border: 10px solid #000;
            /* 内填充/补白区 padding */
            padding-left: 50px; /* 左内填充 */
            padding-right: 100px; /* 右内填充 */
            padding-top: 30px; /* 上内填充 */
            padding-bottom: 50px; /* 下内填充 */

            /* 注意！有复合属性 */
            /* padding: 值; 代表上下左右都是这个值 */
            padding: 100px; /* 代表上下左右都是100px */
            /* padding:上下值 左右值;当上下值相同、左右值相同时 是可以这样子写 */
            padding: 50px 20px; /* 代表上下各50px 左右各20px */
            /* padding: 上值 左右值 下值; 当上下值不同 左右值相同时 可以这样子写 */
            padding: 100px 30px 50px; /* 代表上padding是100px 左右各30px 下padding是50px */
            /* padding: 上 右 下 左;当四个值都不相同 可以这样子写（相同值也可以这样子写） */
            padding: 10px 20px 30px 40px; /* 代表上10px 右20px 下30px 左40px */
            /* 助记：上右下左 钟表顺时针 */
        }
    </style>
</head>

<body>
    <div>
        六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀，六月春风似剪刀。
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641435932804-6b6ea4ed-e7b0-4b39-a1ad-4c9e717f93da.png#clientId=u67ee74df-69ef-4&from=paste&height=342&id=u1ca1ccea&originHeight=683&originWidth=362&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38980&status=done&style=stroke&taskId=u5ceed0c3-802d-4e40-aea3-0c273bef1e6&title=&width=181)
<a name="DiWPA"></a>

## padding 使用的注意事项

1. 块状元素，可以设置上下左右的`padding`
2. 行内元素，默认情况下只能设置左右`padding`
- 行内元素**不**可以设置**宽高**、**上下**`**padding**`、**上下**`**border**`
3. 会撑大盒子
4. 一般用于内容和边界之间的距离
5. 属性
- 上下左右相同`padding:值;`
- 上下相同，左右相同`padding:上下值 左右值;`
- 上下不同，左右相同`padding:上值 左右值 下值;`
- 上下左右想要分开时，顺时针方向`padding:上 右 下 左;`
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style>
        div { /* 块状元素可以设置上下左右的padding */
            width: 100px;
            height: 100px;
            background: #dea;
            padding-left: 50px;
            padding-right: 50px;
            padding-top: 50px;
            padding-bottom: 50px;
        }

        span { /* 行内元素 不可以设置宽高 大小由内容撑开 */
            background: red;
            padding-left: 50px;
            padding-right: 50px;
            /* 
                * 行内元素 默认情况下只能设置左右padding 
                * padding-top: 50px;错误的 
            */
        }
    </style>
</head>

<body>
    <div>块状元素</div>
    <span>行内元素</span>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641435897187-e73cda22-7e86-4511-bacc-60c1dbaba4ef.png#clientId=u67ee74df-69ef-4&from=paste&height=147&id=u85df5809&originHeight=294&originWidth=273&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3166&status=done&style=stroke&taskId=u4e597a1c-a0b3-49fb-acea-67fcfb92623&title=&width=136.5)
<a name="zbxkn"></a>
## padding 练习
```html
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

        /* 外围只设置背景颜色 */
        #navWrapper {
            background: #2e2e2e;
        }

        /* 设置版心的宽高 */
        #nav {
            width: 962px;
            height: 58px;
            background: red;
            /* 有宽高的块状元素水平居中浏览器 */
            margin: 0 auto;
            /* 
                * 注意！建议给父元素设置行高 
                * 因为超链接就一行 想要单行文字垂直居中 设置行高=高度值 
            */
            line-height: 58px;
        }

        #nav a { /* 代表选中了id名字为nav的元素 里面所有的超链接 */
            /* 文字大小 */
            font-size: 12px;
            /* 文字颜色 */
            color: #ffffff;
            /* 去除超链接下划线 */
            text-decoration: none;
            /* 我先设置了一个背景色 方便我们看 */
            background: #f90;
            /* 设置右边框 */
            border-right: 1px solid #474747;
            /* 文字内容到边界之间的距离 使用padding */
            padding-left: 31px;
            padding-right: 32px;
        }

        #nav .noborder {
            /* 去除边框 */
            border: 0;
        }
    </style>
</head>

<body>
    <div id="navWrapper"><!-- 外围 -->
        <div id="nav"><!-- 版心 -->
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;">集团介绍</a>
            <a href="iavascript:;" class="noborder">集团介绍</a>
        </div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648692865067-64cd3e9c-570b-4fd1-8953-fec1a54416e7.png#clientId=u994dd6d9-d692-4&from=paste&height=46&id=u9e1bac93&originHeight=57&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1909&status=done&style=stroke&taskId=u413e14f4-958e-4566-bb25-b48b865b72e&title=&width=767.2)
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        /* 去除页面缝隙 */
        * {
            margin: 0;
            padding: 0;
        }

        /* 外围只需要设置背景颜色 因为块状元素默认宽度独占一行 也就是width:100%；可以省略 高度由版心撑开 */
        #navWrapper {
            background: #232323;
        }

        #nav {
            width: 993px;
            height: 60px;
            margin: 0 auto;
            line-height: 60px;
        }

        #nav a {
            font-size: 14px;
            color: #ffffff;
            /* 去除超链接下划线 */
            text-decoration: none;
            background: url(../images/1.png) no-repeat right center;
            /* 距离左右各15px的补白区 */
            padding: 0 15px;
            /* 代表上下为0 左右为15px */
        }

        #nav a:hover {
            background: #f15a23;
        }
    </style>
</head>

<body>
    <!-- 因为外围有颜色 所以写外围+版心 -->
    <div id="navWrapper"><!-- 外围 -->
        <div id="nav"><!-- 版心 -->
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
            <a href="javascript:;">首页孵化</a>
        </div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648692984415-dd95c150-8406-41ab-9b1e-3fb139a0074b.png#clientId=u994dd6d9-d692-4&from=paste&height=52&id=uf63349c7&originHeight=65&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3368&status=done&style=stroke&taskId=u53b56506-5eaa-4180-a0bb-fe9fe667077&title=&width=767.2)
<a name="FBvcf"></a>

# 边框 border

1. 块状元素，可以设置上下左右`border`边框
2. 行内元素，只能设置左右`border`边框
3. 会撑大盒子
4. 去除边框 `border: 0;`
5. 块状元素水平居中 `margin: 0 auto;`
- [margin:0 auto 失效的原因](https://www.yuque.com/sumingcheng/css/gqio09)
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            height: 200px;
            width: 200px;
            background: green;
            /* 会撑大盒子 内填充 用于文字等等内容 距离 边界之间的举例 */
            padding: 50px;
            /* 边框 会撑大盒子 */
            padding: 20px solid #000;
            /* 
            * 边框的注意事项 
            * 块状元素可以设置上下左右边框 
            * 但是行内元素只能设置左右边框 
            */
        }
    </style>
</head>

<body>
    <div>块状元素块状元素块状元素块状元素块状元素块状元素</div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648693243526-be39139f-4f67-43e0-a8ca-56c9f1d47d42.png#clientId=u994dd6d9-d692-4&from=paste&height=279&id=u7a558b9b&originHeight=349&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3099&status=done&style=stroke&taskId=u2771190c-d4a2-4663-bcdf-4c7165c1278&title=&width=279.2)
<a name="ledui"></a>
# 外边界/外边距 margin

1. 块状元素，可以设置上下左右边框
2. 行内元素，只能设置左右边框 
3. 作用：
- 一般用于一个标签和另一个标签之间的距离
- 一般用于元素整体和其他地方之间的距离
4. 不会撑大盒子
5. `margin` 可以设置负值
6. 注意！
- `text-align: center;` 让这个块里面的内容，在这个块里，水平居中
- `margin: 0 auto;` 是将整个块水平居中
```html
<head>
    <meta charset="UTF-8">
    <title>外边界/外边距</title>
    <style>
        div {
            width: 100px;
            height: 200px;
            background: green;
            /* 外边界 一般用于元素整体 和其他地方之间的距离 */
            margin-left: 100px;/* 左边距/左外边界 */
            margin-right: 200px;
            margin-top: 100px;
            margin-bottom: 100px;
            /* margin的简写/复合属性; */
            /* 当上下值相同左右值相同时 margin: 值; */
            margin: 0;
            /* 当上下值相同 左右值相同时 margin: 上下值 左右值; */
            margin: 100px auto;
            /* 当上下值不同 左右值相同时 margin: 上值 左右值 下值; */
            margin: 10px auto 30px;
            /* 当上下左右值不同时 margin: 上 右 下 左; */
            margin: 10px 30px 20px 50px;
        }
    </style>
</head>

<body>
    <div>css学习</div>
</body>
```
<a name="GiOD5"></a>
## margin 使用注意事项

1. 块状元素可以设置上下左右 `margin`
2. 行内元素只能设置左右 `margin` 不能设置上下 `margin`
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            background: cyan;
            margin-left: 100px;
            margin-top: 100px;
            /* 块状元素可以设置上下左右margin */
        }

        span {
            background: red;
            margin-left: 100px;
            /* 行内元素只能设置左右margin  不能设置上下margin */
            /* margin-top: 100px;  错误 */
        }
    </style>
</head>

<body>
    <div>块状元素</div>
    <span>行内元素</span>
</body>

```
<a name="XKDUe"></a>
## margin 的特性
<a name="NnpYe"></a>
### `margin`左右边界相加，上下边界取最大值
```html
<head>
    <meta charset="UTF-8">
    <title>margin左右边界相加 上下边界取最大值</title>
    <style>
        span {
            background: cyan;
            margin-left: 50px;
            margin-right: 50px;
        }

        b {
            background: #f90;
            margin-left: 50px;
        }

        .box1 {
            width: 200px;
            height: 200px;
            background: palegreen;
            margin-bottom: 100px;
        }

        .box2 {
            width: 200px;
            height: 200px;
            background: yellow;
            margin-top: 190px;
        }
    </style>
</head>

<body>
    <span>111</span>
    <b>222</b>
    <div class="box1"></div>
    <div class="box2"></div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648693646739-98e9a594-c75d-4196-9906-142398a6c853.png#clientId=u994dd6d9-d692-4&from=paste&height=621&id=ua21b46cc&originHeight=776&originWidth=274&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3620&status=done&style=stroke&taskId=u70cb54f1-d6fc-4492-bd9a-2c7b2c9d43d&title=&width=219.2)
<a name="H7csA"></a>
### 子元素设置`margin-top;`父元素跟随子元素下移

1. 先尝试用`padding`来做
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        /* 先尝试使用padding来做 */
        .big {
            width: 350px;
            /* 500变成350 */
            height: 400px;
            /* 500变成400 */
            background: yellowgreen;
            padding-left: 150px;
            padding-top: 100px;
        }

        .son {
            height: 100px;
            width: 100px;
            background: pink;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641445138385-fcb0f776-9995-4fab-8839-182756864e6c.png#clientId=ud9a86334-6479-4&from=paste&height=150&id=uc2486700&originHeight=648&originWidth=644&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3141&status=done&style=stroke&taskId=ub455a468-2342-4e68-ae37-a7b3bc342bb&title=&width=149)

2. `margin`方法：`overflow: hidden;`溢出隐藏（[BFC原理](https://www.yuque.com/naiyoumitaocha/psyhak/to3zk9#F0Y9E)）
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        .big {
            width: 500px;
            height: 500px;
            background: yellowgreen;
            /* 问题：子元素设置margin-top;父元素跟随子元素下移了 */
            /* 解决方式1 给父元素设置overflow: hidden;原理BFC */
            overflow: hidden;
            /* 解决方式2 给父元素设置padding-top:1px;缺点 会给父元素撑大1px */
            padding-top: 1px;
            /* 解决方式3 给父元素设置border-top: 1px solid transparent; */
            border-top: 1px solid transparent;
        }

        .son {
            height: 100px;
            width: 100px;
            background: pink;
            margin-left: 150px;/* 左外边距 */
            margin-top: 100px;/* 问题之源？？？ */
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641445138385-fcb0f776-9995-4fab-8839-182756864e6c.png#clientId=ud9a86334-6479-4&from=paste&height=150&id=YXdVd&originHeight=648&originWidth=644&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3141&status=done&style=stroke&taskId=ub455a468-2342-4e68-ae37-a7b3bc342bb&title=&width=149)
> **总结：当子元素设置**`**margin-top;**`**父元素跟随子元素下移了**
> 解决方式1：给父元素设置`overflow: hidden;`原理BFC
> 解决方式2：给父元素设置`padding-top:1px;`缺点会给父元素撑大1px
> 解决方式3：给父元素设置`border-top: 1px solid transparent;`

3. `margin`属于盒模型!!!
<a name="Q4Bkx"></a>
# 盒模型组成
![Y{G2Q]52DRE%]LZADLP4%{V.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641471720623-5c584855-11ac-4f17-ae5b-b49343c2d41d.png#clientId=ub6378184-257c-4&from=paste&height=306&id=htLSL&originHeight=659&originWidth=1442&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28340&status=done&style=stroke&taskId=ub2eb9429-5ba6-4eca-8654-681030a829e&title=&width=670)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649080152031-8a5f370b-1879-48ad-93ac-758a445a456a.png#clientId=uf9f1c930-628a-4&from=paste&height=453&id=u1d56a6f1&originHeight=523&originWidth=774&originalType=binary&ratio=1&rotation=0&showTitle=false&size=260440&status=done&style=stroke&taskId=u98288bd9-5c46-4b48-8fd5-e00cf6fac10&title=&width=670)
<a name="JP1kR"></a>
## 如何区分 margin 与 padding

1. 元素和元素距离`margin`
2. 字距离边境`padding`
3. `padding`不能写负值，`margin`可以写负值
<a name="pDvK4"></a>
# 练习
<a name="hHpu5"></a>

## 公司介绍练习

```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box {
            width: 192px; /* width: 240px-padding多出来的48px */
            height: 240px;
            background: #f1f1f1;
            /* 给父元素设置内容填充 这样子就会把文字往里挤 */
            padding-left: 25px;
            padding-right: 23px;
            overflow: hidden;
        }

        h2 {
            color: #40444f;
            font-size: 18px;
            font-weight: normal; /* 取消加粗 */
            padding-top: 36px; /* 距离上方的间距 */
            margin-bottom: 33px; /* 距离下方的距离 */
        }

        .font12 {
            font-size: 12px;
            color: #4e4e4e;
            line-height: 25px;/* 设置行高 */
        }

        .p3 {
            font-size: 12px; /* 浏览器解析文字最小是12px，选取文字只能是偶数，不可以是奇数 */
            color: #909090;
            line-height: 24px; /* 设置行高 */
            margin-top: 15px; /* 距离上方的间距 */
        }
    </style>
</head>

<body>
    <div class="box">
        <h2>公司介绍</h2>
        <p class="font12">公司成立于1984年</p>
        <p class="font12">经过近30年的发展</p>
        <p class="p3">已成为电器制造、房地产开发和金融投资三业并举的综合性跨国...</p>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648694358945-3c4e8ad8-f71f-4236-b1cb-bf915d655797.png#clientId=u994dd6d9-d692-4&from=paste&height=301&id=uc55147ad&originHeight=525&originWidth=524&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34784&status=done&style=stroke&taskId=ubcb34160-7b09-41ec-a7e8-fa4bde6527d&title=&width=300)
<a name="xGeik"></a>
### 辅助计算

1. 标题距离边境36
2. 第一标题和第一行行高57  标题18
- 间隙39/2=19
3. 第一行和第二行 行高25px 第一行 字12（13）px
- 间隙 25-12=13 13/2=6（0.5不要）
4. 第二行和第三行 行高38px   第三行 12
- 间隙26/2=13
5. 第三行到第四行 行高24px   第三行12
- 间隙12/2=6
<a name="BswQ4"></a>
## 马身练习

- 圆角`border-radius:` 可以写**数值**4`px` 也可以写**百分比**`;`
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式表的创建 -->
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box {
            width: 180px;
            /* 242-62 */
            height: 240px;
            background: #fbfbfb url(../day3/images/2.png) no-repeat right bottom;
            /* 设置内填充 会将里面的内容 往里挤一挤 */
            padding-left: 25px;
            padding-right: 37px;
            overflow: hidden;
            /* 因为h2设置margin-top 会带着父元素box一起下移，设置这行代码来解决该问题 */
        }

        h2 {
            font-size: 18px;
            color: #222;
            font-weight: normal;
            /* 取消加粗 */
            /* 距离上方间距 */
            margin-top: 36px;
            /* 距离下方间距 */
            margin-bottom: 21px;
        }

        p {
            font-size: 12px;
            color: #5a5a5a;
            line-height: 24px;
        }

        .more {
            width: 66px;
            height: 19px;
            background: rgb(173, 173, 173);
            color: #fcfcfc;
            /* 英文字体 */
            font-family: Arial, Helvetica, sans-serif;
            font-size: 12px;
            /* 文字在色块里水平居中 */
            text-align: center;
            /* 单行文本垂直居中 设置 行高=高度值 */
            line-height: 19px;
            /* 距离上方22 */
            margin-top: 22px;
            /* 圆角 border-radius: 可以写数值4px 也可以写百分比; */
            border-radius: 5px;
        }
    </style>
</head>

<body>
    <div class="box">
        <h2>人才招聘</h2>
        <p>培养一流的人才，铸造一流的工程，实现员工与企业的共同发展</p>
        <div class="more">more---></div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648694888881-9b1ae80f-4d2f-47c1-8fd9-e34877ab92cb.png#clientId=u994dd6d9-d692-4&from=paste&height=287&id=u786f2915&originHeight=505&originWidth=527&originalType=binary&ratio=1&rotation=0&showTitle=false&size=115546&status=done&style=stroke&taskId=u59c7628b-cb48-4bd5-bf38-3030b5a29af&title=&width=300)
<a name="qeuYi"></a>

# 小结[盒模型 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956529065-d9b11c25-ed51-4f13-91df-ceea93a230a2.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956529065-d9b11c25-ed51-4f13-91df-ceea93a230a2.png%22%2C%22name%22%3A%22%E7%9B%92%E6%A8%A1%E5%9E%8B%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A801269%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22udb31c968-128f-4aca-9018-8fe773af14f%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ue8ea1acb%22%2C%22card%22%3A%22file%22%7D)
