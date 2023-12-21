<a name="ako6z"></a>
# 宽高自适应 width/height: 100%;

<a name="oSx2s"></a>
## 宽度自适应 width: 100%;

1. 所谓的宽高自适应，是针对于**块状元素**，或者说是针对于**外围+版心**的
2. 宽度自适应，也就是宽度占满整屏，也就是我们常见的外围+版心
3. 版心的宽最好不要超过**1280px**
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>宽高自适应</title>
    <style>
        * {
            margin: 0;
            padding: 0; 
        }

        #navWrapper {
            width: 100%;
            /* 宽度自适应 高度不写 由版心区域撑开 */
            background: cyan;
        }

        #nav {
            width: 1280px;
            height: 100px;
            background: pink;
            margin: 0 auto;
        }
    </style>
</head>

<body>
    <div id="navWrapper">
        <div id="nav"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641873459613-6e72fad4-0a4a-420e-b72e-2987e6e49686.png#clientId=u9b33d297-f812-4&from=paste&height=23&id=u0ae01b7c&originHeight=46&originWidth=939&originalType=binary&ratio=1&rotation=0&showTitle=false&size=382&status=done&style=stroke&taskId=u97a9dcd9-b2b8-4a4b-9f7b-2e557e7410e&title=&width=469.5)
<a name="YMRo2"></a>
## 高度自适应 height: auto;
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        div {
            width: 200px;
            /* 高度自适应 也就是高度由内容撑开 */
            height: auto;/* 可以省略 */
            background: cyan;
        }
    </style>
</head>

<body>
    <div>
        北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.北冥有鱼，其名为鲲.
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641873425674-562325ef-028d-4597-9838-4a089280524e.png#clientId=u9b33d297-f812-4&from=paste&height=274&id=ua0c74829&originHeight=547&originWidth=250&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19760&status=done&style=stroke&taskId=uf9c5f7d5-da90-499f-b898-c22fd3e0ab9&title=&width=125)
<a name="VpAhs"></a>
# 最小/大宽高 min/max-height/width
<a name="zEPQY"></a>
## 最小高/宽度 min-height/width（做兼容）
注意！如果你想要将代码写的很完善，最小高度是需要兼容的，它有两种兼容方式：

1. 方式一
- `min-height: 100px;` 针对于高版本浏览器说“最小高度是100px”
- `_height: 100px;` 针对低版本浏览器说，“最小高度为100px”
- (在低版本中，height就是最小高度；下划线“_”过滤器，是针对低版本浏览器使用的)
2. 方式二
- `min-height: 100px;`针对于高版本浏览器说“最小高度是100px”
- `height: 100px;`针对低版本浏览器说“最小高度为100px”
- 注意！高版本浏览器会解析成高度为100px，如何解决呢？
- 解决方式是`height: auto!important;`  高度自适应，`height: auto;` 这个值直接替换掉`100px` （`!important` 在低版本不解析）

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>即使你不写字，仍占据一定宽高</title>
    <style>
        div {
            width: 200px;
            /* 高度自适应 */
            height: auto;
            /* 最小高度 */
            min-height: 100px;
            background: pink;
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![即使你不写字，仍占据一定宽高](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641882300327-ad825870-636b-43dc-816c-86e7893605c4.png#clientId=u90587075-6b03-4&from=paste&height=100&id=DfUQz&originHeight=133&originWidth=263&originalType=binary&ratio=1&rotation=0&showTitle=true&size=496&status=done&style=stroke&taskId=u6be415b0-dfd3-4f31-a856-2cbc79e6fd3&title=%E5%8D%B3%E4%BD%BF%E4%BD%A0%E4%B8%8D%E5%86%99%E5%AD%97%EF%BC%8C%E4%BB%8D%E5%8D%A0%E6%8D%AE%E4%B8%80%E5%AE%9A%E5%AE%BD%E9%AB%98&width=198.5 "即使你不写字，仍占据一定宽高")
<a name="ouYJz"></a>
## 最大高/宽度 max-height/width
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>超过最大高度文字将会被挤出</title>
    <style>
        div {
            width: 200px;
            max-height: 200px;
            background: green;
        }
    </style>
</head>

<body>
    <div>
        北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼
    </div>
</body>

</html>
```
![超过最大高度文字将会被挤出](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649217410710-e9dbe082-6929-418d-8b48-d485d1f094b7.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=247&id=JY8eZ&originHeight=309&originWidth=272&originalType=binary&ratio=1&rotation=0&showTitle=true&size=5048&status=done&style=stroke&taskId=u0af5c12f-1883-46b4-9105-935c8dd1565&title=%E8%B6%85%E8%BF%87%E6%9C%80%E5%A4%A7%E9%AB%98%E5%BA%A6%E6%96%87%E5%AD%97%E5%B0%86%E4%BC%9A%E8%A2%AB%E6%8C%A4%E5%87%BA&width=217.6 "超过最大高度文字将会被挤出")
<a name="Wk0Zo"></a>
# 一整屏页面 html,body{height: 100%;}

- `background-size: 水平大小 垂直大小;` 设置背景图大小 
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

        /* 一整屏页面必备条件 */
        html,
        body {
            overflow: hidden;
            height: 100%;
        }

        body {
            background: url(./1.jpeg) no-repeat;
            /* 设置背景图大小 */
            /* background-size: 水平大小  垂直大小; */
            background-size: 100% 100%;
        }

        div {
            /* 垂直水平居中 */
            position: absolute;
            left: 50%;
            top: 50%;
            width: 400px;
            height: 500px;
            margin-left: -200px;
            margin-top: -250px;
            background: cyan;
            
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![放大页面后背景图固定不动](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649218412924-770dcd3f-58be-4f23-ad68-82a56dbbbed2.gif#clientId=uc3fd3a6e-d3b1-4&from=drop&id=Tc3ug&originHeight=794&originWidth=941&originalType=binary&ratio=1&rotation=0&showTitle=true&size=238192&status=done&style=stroke&taskId=uaa19c0c8-8a85-484c-96ec-90b851c8d94&title=%E6%94%BE%E5%A4%A7%E9%A1%B5%E9%9D%A2%E5%90%8E%E8%83%8C%E6%99%AF%E5%9B%BE%E5%9B%BA%E5%AE%9A%E4%B8%8D%E5%8A%A8 "放大页面后背景图固定不动")![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641911952335-5dc6bb90-61ee-4913-ae5f-522c7aa6487a.png#clientId=u620d3163-50ed-4&from=paste&height=150&id=ipQA6&originHeight=902&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1202700&status=done&style=stroke&taskId=ucb1c2d15-b250-4148-b302-3c3e124e120&title=&width=319)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641911990239-5d15d3d0-395e-468f-87ab-45b53e966005.png#clientId=u620d3163-50ed-4&from=paste&height=150&id=zFmcu&originHeight=902&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=875793&status=done&style=stroke&taskId=u5a3fafc0-451c-487f-8260-693cf51bed8&title=&width=319)<br />[login-lzy.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641911347285-626dea22-489c-4702-83a3-a525b3d7393b.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641911347285-626dea22-489c-4702-83a3-a525b3d7393b.jpeg%22%2C%22name%22%3A%22login-lzy.jpg%22%2C%22size%22%3A1870978%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u50868224-d04a-4d80-8beb-0f1efeee83f%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22xh2xy%22%2C%22card%22%3A%22file%22%7D)
<a name="P9Sj5"></a>
## 练习-健康比金钱更重要
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/jk.css">
</head>

<body>
    <!-- 第一大部分   测量高度是606   整个设计图高度是721   606/721=84% -->
    <div id="banner">
        <img src="../images/banner.jpg" alt="">
    </div>
    <!-- 导航栏 -->
    <div id="nav">
        <p>
            <a href="javascript:;">首页</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">关于我们</a>
            <a href="javascript:;">CN/EN</a>
        </p>
    </div>
    <!-- 尾部 -->
    <div id="footer">
        <p>
            版权所有：浙江王力门业有限公司
            <span>技术支持：派桑网络</span>
        </p>
    </div>
</body>

</html>
```
```css
/* 去除页面缝隙 */
* {
    margin: 0;
    padding: 0;
}

/* 一整屏页面必备条件 */
html,
body {
    height: 100%;
    overflow: hidden;
}

/* 第一大部分   测量高度是606   整个设计图高度是721   606/721=84% */
#banner {
    width: 100%;
    height: 84%; /* 606/721=0.84 */
    background: green;
}

/* 我希望我的图片 和父元素一致 */
#banner img {
    width: 100%;
    height: 100%;
}

/* ------导航栏 */
#nav {
    width: 100%;
    height: 10.7%;	/* 77/721=10.7 */
    /* background: pink; */
    /* 2）父相子绝 */
    position: relative;
}

#nav p {
    /* background: skyblue; */
    /* 1）设置定位 */
    position: absolute;
    left: 0;
    top: 50%;						/* 3）此步骤为垂直，但是只有文字上边框垂直居中 */
    /* 5）块状元素 设置完浮动或者绝对定位或者固定定位之后  宽度由内容撑开   你可以自定义宽度 */
    width: 100%;				/* 6）让文字边框占满全屏幕 */
    /* 垂直居中 */
    margin-top: -10px;	/* 4）f12检查后发现padding为20px，之所以不是12px，是因为自带一定行高 */
    text-align: center;	/* 7）文本水平居中浏览器或者说水平居中于蓝色区域 */
}

#nav a {
    padding: 0 20px;
    font-size: 12px;
    color: #323232;
    text-decoration: none;
}

/* 尾部 */
#footer {
    position: relative;
    width: 100%;
    height: 5.3%;	/* 100-84-10.7 */
    background: #f0f0f0;
    font-size: 12px;
    color: #9d9d9d;
}

#footer p {
    position: absolute;
    left: 0;
    top: 50%;
    margin-top: -10px;
    width: 100%;
    text-align: center;
}

#footer span {
    margin-left: 18px;
}
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649225188470-642754cf-4e4a-4bc5-ab6f-dedb371e92b9.gif#clientId=uc3fd3a6e-d3b1-4&from=drop&id=Kpu8U&originHeight=862&originWidth=1902&originalType=binary&ratio=1&rotation=0&showTitle=false&size=773231&status=done&style=stroke&taskId=u1c9a5d1c-41a1-44a6-a289-38f08cc813a&title=)<br />[banner.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641912339626-77195a08-6e9b-4e30-8081-f76ae30ff8d4.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641912339626-77195a08-6e9b-4e30-8081-f76ae30ff8d4.jpeg%22%2C%22name%22%3A%22banner.jpg%22%2C%22size%22%3A264145%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22ue81731e4-c34a-49a9-b81d-b9e5c6f4f68%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22w4nZa%22%2C%22card%22%3A%22file%22%7D)[案例2.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641912372537-7f12eaf1-acc9-4137-a771-0808ec7dc48f.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641912372537-7f12eaf1-acc9-4137-a771-0808ec7dc48f.jpeg%22%2C%22name%22%3A%22%E6%A1%88%E4%BE%8B2.jpg%22%2C%22size%22%3A631649%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22uffd01b4d-7166-480c-85bb-dba583d2df6%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22aj2aQ%22%2C%22card%22%3A%22file%22%7D)
<a name="eYpiI"></a>
# 高度塌陷

- 子元素设置浮动，父元素没有写高度，父元素出现了高度塌陷
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        * {
            margin: 0;
            padding: 0;
        }

        .main {
            width: 80%;
            /* 高度自适应 */
            height: auto;
            background: pink;
            margin: 0 auto;
        }

        /* 子元素设置浮动 父元素没有写高度 父元素出现了高度塌陷 */
        .son {
            width: 200px;
            height: 200px;
            background: cyan;
            margin: 10px; /* 上下左右距离10px */
            float: left;
        }
    </style>
</head>

<body>
    <div class="main">
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641873533016-e0698fb2-4cd6-4aa0-8bf5-ddad1c8abee8.png#clientId=u9b33d297-f812-4&from=paste&height=95&id=u3d88cc8a&originHeight=189&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3413&status=done&style=stroke&taskId=uaaa69825-a401-464a-beda-5ec46ba85d5&title=&width=384)
<a name="rZeJC"></a>
# 清除浮动 [clear](https://developer.mozilla.org/zh-CN/docs/Web/CSS/clear): left/right/both/none;

1. `clear: both;` 表示该元素两边都不存浮动元素
2. `clear: none;` 表示两边允许有浮动元素。
3. 将这个元素左侧/右侧的浮动元素清除后，清除效果是怎样的？折行 
4. 注意！左浮动清左，右浮动清右
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>clear</title>
    <style>
        div {
            width: 150px;
            height: 150px;
            float: left;
        }
    </style>
</head>

<body>
    <div style="background: #0ac;"></div>
    <div style="background: #fac;"></div>
    <div style="background: pink;"></div>
    <div style="background: red; clear: left;"></div>
    <div style="background: #0ffc;"></div>
    <div style="background: #f90;"></div>
    <div style="background: #fac; clear: both;"></div>
    <div style="background: black"></div>
    <div style="background: cyan"></div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641874155510-a54f2139-1599-42a5-8d9c-e91b93c25ea0.png#clientId=u9b33d297-f812-4&from=paste&height=315&id=u4f946e31&originHeight=629&originWidth=631&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3082&status=done&style=stroke&taskId=u75d3d993-455e-4616-9807-9748561b0de&title=&width=315.5)![辅助理解图](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649237305943-f6dbe1de-bcba-4a6b-8e57-689aa1de4ff3.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=315&id=u3d14885d&originHeight=433&originWidth=433&originalType=binary&ratio=1&rotation=0&showTitle=true&size=8213&status=done&style=stroke&taskId=u4be542ca-95aa-4f52-8e39-7d9a45c9b02&title=%E8%BE%85%E5%8A%A9%E7%90%86%E8%A7%A3%E5%9B%BE&width=315 "辅助理解图")
<a name="WmY1Y"></a>
## clear 注意事项

1. 如果下面模块设置了`clear`清除，可以控制上面模块的`margin-bottom`，来让这两个模块产生距离
2. 模块如果设置了`clear`清除浮动，之后`margin-top`的使用就会受到限制（失效）
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .floatDiv {
            width: 200px;
            height: 200px;
            background: cyan;
            float: left;
            /* margin-bottom: 20px; */
            /* 如果下面.clearDiv模块设置clear清除，可以控制margin-bottom来让这两个模块产生距离 */
        }

        .clearDiv {
            width: 300px;
            height: 300px;
            background: red;
            /* 我不希望和浮动在一行 */
            clear: both;
            margin-left: 30px;
            margin-top: 10000px;
            /* 文档中的div设置了clear清除浮动之后 margin-top的使用就会受到限制 */
        }
    </style>
</head>

<body>
    <div class="floatDiv">我是浮动元素</div>
    <div class="clearDiv">我是清除 clear</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641874178808-2d285fa7-64f9-40aa-bef2-abaf2860c111.png#clientId=u9b33d297-f812-4&from=paste&height=391&id=ue0be3055&originHeight=635&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5385&status=done&style=stroke&taskId=uad65ffe6-1df2-4a22-bb92-a8cc907a53c&title=&width=260)
<a name="jTRdI"></a>
## clear 案例

- `clear` 只能设置给块状元素 -> `display: block;` 把它变成块状元素
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            width: 1300px;
            margin: 0 auto;
            height: 600px;
            background: pink;
        }

        .son {
            width: 300px;
            height: 400px;
            margin: 50px;
            background: yellow;
            float: left;
        }

        button {
            clear: both; /* clear只能设置给块状元素 */
            display: block; /* 把它变成块状元素 */
            margin: 0 auto; /* 水平居中 */
            width: 180px;
            height: 80px;
            border: 0;
            background: skyblue;
            font-size: 25px;
            color: #fff;
            border-radius: 20px;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <button>更多</button>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649168280142-37605191-605f-47f9-b341-570ff1b1b65f.png#clientId=u6fde67f2-1da6-4&from=paste&height=308&id=ud5427a80&originHeight=385&originWidth=953&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3630&status=done&style=stroke&taskId=u54e553f5-5abe-4baa-8681-3e719d576f6&title=&width=762.4)
<a name="qL63D"></a>
# 解决高度塌陷1-浮动元素下面添加空div

1. 在浮动元素的后面，添加一个兄弟节点`空div`
2. 然后给这个`空div`设置3步骤
- `clear: both;` 
- `height: 0;` 在低版本浏览器中，即使你什么都不加，块状元素默认有高度，默认高度在10px左右
- `overflow: hidden;`怕加字，将字体切掉
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            width: 100%;
            height: auto;/* 高度自适应 */
            background: pink;
        }

        .son {
            width: 200px;
            height: 200px;
            background: greenyellow;
            border: 1px solid #000;
            float: left;
        }

        .clear {
            /* 
            width: 700px;
            background: purple;
            */
            clear: both;
            height: 0;
            overflow: hidden;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
        <div class="son"></div>
        <div class="son"></div>
        <div class="clear"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641874668742-1cc7fce5-f568-46fc-8511-e2b7126abb40.png#clientId=u9b33d297-f812-4&from=paste&height=63&id=u37a7cf8e&originHeight=179&originWidth=954&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1222&status=done&style=stroke&taskId=u42171428-e15c-4745-bd43-ddadb83e049&title=&width=338)
<a name="BSAUH"></a>
# 解决高度塌陷2-给父元素设置 overflow:hidden; 

- 弊端：二级导航栏不能用

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641905313512-18dfc20f-c0ea-4d47-9174-da3964d1ef61.png#clientId=u81a5ba16-3a5a-4&from=paste&height=208&id=u4358569a&originHeight=260&originWidth=379&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55850&status=done&style=stroke&taskId=u9adc3f52-e73e-47d8-8935-0ddec9df998&title=&width=302.5)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            overflow: hidden;
            width: 700px;
            height: auto;/* 高度自适应 */
            background: green;
        }

        .son {
            float: left;/* 注意！BFC后 浮动元素高度等于父元素高度 */
            width: 300px;
            height: 300px;
            background: pink;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649169816350-9a54a009-79f7-4420-ba57-d4ed592e4467.png#clientId=u6fde67f2-1da6-4&from=paste&height=120&id=ua0347f66&originHeight=289&originWidth=663&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1493&status=done&style=stroke&taskId=u9a8a2121-b43a-49da-ae00-da744299b8b&title=&width=274.4000244140625)
<a name="PEbQa"></a>
# 解决高度塌陷3-万能清浮动 ::after
<a name="Uz21w"></a>
## 伪元素 ::before ::after

1. `::before``::after` 在元素内容**最前**/**后**面添加东西
- 必须结合`content`使用
2. `::first-line` 选中块元素第一行文字
3. `::first-letter` 选中第一个字/字母
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        p {
            background: skyblue;
        }

        p::first-line { /* 代表选中块元素第一行文字 */
            font-size: 30px;
            color: #fff;
        }

        p::first-letter { /* 选中第一个字/字母 */
            font-size: 60px;
            color: blue;
        }

        div {            
            position: relative; /* 用作div::after定位父相子绝 */
            background: green;
        }

        /* 在元素内容最前面 添加东西 */
        div::before {
            /* 必须结合content使用 */
            content: "其名";
            color: yellow;
        }

        /* 在元素内容最后面添加东西 注意！！必须结合content使用 */
        div::after {
            position: absolute; /* 如果不设置此条则作用于整个页面 */
            right: 0;
            bottom: 0;
            content: "鲲之大";
            background: pink;
            color: red;
        }
    </style>
</head>

<body>
    <p>Today北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼北冥有鱼
    </p>
    <div>为鲲</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649207824515-8d84af10-4577-4aba-9dcd-a776ab44f204.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=169&id=SpgFn&originHeight=403&originWidth=955&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29013&status=done&style=stroke&taskId=u49eb908e-2641-43a3-9ba9-fa8a9b495e7&title=&width=401.3999938964844)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649210043248-8a35613f-8878-48e4-8d7a-35d984ec837d.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=239&id=yKTBE&originHeight=888&originWidth=956&originalType=binary&ratio=1&rotation=0&showTitle=false&size=64530&status=done&style=stroke&taskId=u6939b8a1-60a4-4bf7-bffc-a774a850d57&title=&width=257.40000915527344)
<a name="Hv4RP"></a>
## 万能清浮动
```css
.父元素::after {
  content:"";
  display: block;
  clear: both;
  height: 0px;
  overflow: hidden;
  visibility: hidden;
}
```
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            width: 100%;/* 宽度自适应 */
            height: auto;/* 高度自适应 */
            background: green;
        }

        .son {
            width: 200px;
            height: 200px;
            border: 1px solid #000;
            background: skyblue;
            float: left;
        }

        .big::after {
            content: "";
            display: block;/* 将元素转换为块状 */
            clear: both;
            height: 0px;
            overflow: hidden;
            visibility: hidden;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
        <div class="son"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649216434837-58ae7c8b-e716-4294-be39-9161845c742c.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=217&id=uce0b448c&originHeight=271&originWidth=960&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2290&status=done&style=stroke&taskId=u0207b542-1c36-43c6-bd2b-7e3f46e2253&title=&width=768)
<a name="aV4i2"></a>
# 元素消失的几种展现方式

1. `display: none;` 元素消失，在文档流**不占**位置
2. `visibility: hidden;` 元素消失，但是在文档流**占**据位置
3. `background: transparent` 文字内容和边框都在
4. `opacity: 0;` 透明度
- `filter: alpha(opacity=0);` 兼容
5. `background: rgba(0,0,0,0);` 透明度，文字内容和边框都是存在的（IE8以上才识别）
6. 过渡时间 :hover
- `transition: 2s;`
- `height: 0;`
- `overflow: hidden;` 让文字一起消失（一刀切）
7. 过渡时间 :hover
- `transition: 2s;` 
- `transform: scale(0);` 缩小为0
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            background: pink;
            border: 2px solid #000;
        }

        .box1 {
            display: none;
            /* 元素消失 在文档流不占位置 */
        }

        .box2 {
            visibility: hidden;
            /* 元素消失 但是在文档流占据位置 */
        }

        .box3 {
            background: transparent;
            /* 文字内容和边框都在 */
        }

        .box4 {
            /* 透明度 */
            opacity: 0;
            /* 必须配套使用兼容 */
            filter: alpha(opacity=0);
        }

        .box5 {
            /* 透明度 IE8以上才识别 */
            background: rgba(0, 0, 0, 0);/* 文字内容和边框都是存在的 */
        }

        .box6:hover {
            /* 过渡时间 */
            transition: 2s;
            height: 0;
            overflow: hidden;
            /* 让文字一起消失 */
        }

        .box7:hover {
            /* 过渡时间 */
            transition: 2s;
            /* 缩小为0 */
            transform: scale(0);
        }
    </style>
</head>

<body>
    <!-- .box$*6按tab按键 -->
    <div class="box1">元素消失1</div>
    <div class="box2">元素消失2</div>
    <div class="box3">元素消失3</div>
    <div class="box4">元素消失4</div>
    <div class="box5">元素消失5</div>
    <div class="box6">元素消失6元素消失6元素消失6元素消失6元素消失6</div>
    <div class="box7">元素消失7</div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649216487059-968d7aac-635b-48ad-b5a2-e4b429c0208a.gif#clientId=uc3fd3a6e-d3b1-4&from=drop&height=386&id=u6c28943d&originHeight=261&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81181&status=done&style=stroke&taskId=u6489ddf5-9550-4af7-939f-b7129f0480c&title=&width=303)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641909677556-6161c892-1075-48ee-945d-6a40891a3ed8.png#clientId=u81a5ba16-3a5a-4&from=paste&height=386&id=u207f18d3&originHeight=772&originWidth=502&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19548&status=done&style=stroke&taskId=uee8e0f98-ef3e-4db8-8575-f4c2b5bd306&title=&width=251)
<a name="hINJK"></a>
# 标签扩充
<a name="sX69V"></a>
## [<iframe>](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/iframe) 复用标签

1. `<iframe src="引入对应的html文件" frameborder="0">``</iframe>`
```html
<iframe src="规定在 iframe 中显示的文档的 URL(默认的显示页面)" width="宽值" height="高值" frameborder="1/0" name="iframe名称" scrolling="yes/no/auto"> </iframe>
```

- `frameborder="1/0"` “1”代表有框架边框；“0”代表无框架边框
- `scrolling="yes/no/auto"` 滚动条： yes 有 / no 无 / auto 自动
2. 作用：
- `<iframe>` 是用来在网页中插入第三方页面，早期的页面使用`<iframe>` 主要是用于导航栏这种很多页面都相同的部分，这样在切换页面的时候避免重复下载。
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>复用标签</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        #header {
            width: 1200px;
            height: 200px;
            background: cyan;
            margin: 0 auto;
        }
    </style>
</head>

<body>
    <div id="header">
        相同的头部 想要随时被复用
    </div>
</body>

</html>
```
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

        iframe {
            width: 100%;
            /* 高度和引用的部分  高度一致  这样更精准一些  */
            height: 200px;
        }
    </style>
</head>

<body>
    <iframe src="./iframe.html" frameborder="0" scrolling="no"></iframe>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641916122255-624f27e1-68ed-4817-998c-aaa9985655dd.png#clientId=u620d3163-50ed-4&from=paste&height=127&id=u3b3fc1d1&originHeight=150&originWidth=788&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2637&status=done&style=stroke&taskId=u8fe84150-0755-4445-b1d9-46bcd4d5305&title=&width=669)
<a name="ffbKD"></a>
## calc 函数

1. `calc()`函数用于动态计算长度值
2. 需要注意的是，**运算符前后**都需要保留一个**空格**
- 例如：`width: calc(100% - 10px)；`
3. 任何长度值都可以使用`calc()`函数进行计算
4. `calc()`函数支持 "`+`", "`-`", "`*`", "`/`" 运算
5. `calc()`函数使用标准的数学运算优先级规则
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>calc表示大小的</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        div {
            height: calc(389px - 23px - 66px);
            /* 
                * width = 100% - 396px
                * 可以利用calc(数学表达式)来实现   
                * 注意！运算符前后需要有空格 
            */
            width: calc(100% - 396px);
            background: green;
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649235345883-0310f611-6577-4280-bf5b-caf9380d8008.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=232&id=uc76f548b&originHeight=890&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6956&status=done&style=stroke&taskId=u426b4136-dec3-4ac2-961c-e87699ff5a7&title=&width=250.39999389648438)
<a name="mNacv"></a>
## <marquee> 走马灯 

1. `behavior="alternate"` 来回 
2. `direction` 方向 
- 值 `left`/ `right`/`up`/`down`
3. `scrollamount="300"` 滚动速度，值越大，越快
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

        marquee {
            height: 200px;
            background-color: green;
        }
    </style>
</head>

<body>
    <marquee behavior="" direction="down" scrollamount="10">
        2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 2022年1月11日 23:55:26 
    </marquee>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649235896895-45474486-9ac9-4a95-95a1-8b362e653fdd.gif#clientId=uc3fd3a6e-d3b1-4&from=drop&id=u78eac0e9&originHeight=224&originWidth=952&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2004909&status=done&style=stroke&taskId=u652a8e6a-a25d-4da9-9da8-1d9f2d013e7&title=)
<a name="aSYyJ"></a>
# [BFC](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Block_formatting_context) 块级格式化上下文

1. 全称 `Block Formatting Context`
2. 一个盒子如果变成了`BFC`，那么里面的子元素 ，无论怎样兴风作浪，都是不会影响到身为`BFC`的父元素（或页面其他元素）的布局
<a name="b9C2s"></a>
##  常见情况（将父元素变成 BFC）

- 子元素设置 `margin-top;` 父元素跟随子元素下移了(影响人家父元素了)
- 子元素设置浮动，父元素不写高度，父元素高度塌陷了(影响人家父元素了)
<a name="tV8sf"></a>
## BFC 的触发条件（怎样才能变成 BFC呢）

1. 根节点`html`是`BFC`（了解即可，页面设置任何模块元素都不会让整个页面下移）
2. `float`值不为`none`
- `float: left;`
- `float: right;`
3. `overflow`不为默认值`visible`  
- `overflow: auto;`
- `overflow: hidden;`
- `overflow: scroll;`
4. `position`值为`absolute`或者`fixed`
5. `display: inline-block;``display: flex;``display: grid;`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BFC块级格式化上下文</title>
    <style>
        .big {
            float: left;/* 写法1：父元素变成bfc  */
            position: absolute;/* 写法2：父元素变成bfc  */
            overflow: hidden;/* 写法3：父元素变成bfc  */
            width: 600px;
            height: 700px;
            background: pink;
        }

        .son {
            width: 300px;
            height: 300px;
            margin-top: 200px;/* 子元素设置margin-top，父元素跟其下移   */
            background: green;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649170015775-421c2a57-44bd-4965-8a01-8276f403b8a7.png#clientId=u6fde67f2-1da6-4&from=paste&height=166&id=cZkSd&originHeight=451&originWidth=387&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1498&status=done&style=stroke&taskId=u548df3e5-9a77-4ed0-ab5f-704c4358475&title=&width=142.60000610351562)
<a name="IparB"></a>
## BFC 应用
<a name="Ak8CP"></a>
### 两栏布局

- **BFC 区域与浮动区域不重叠**
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>两栏布局</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .left {
            float: left;
            width: 300px;
            height: 600px;
            background: skyblue;
        }

        .right {
            /* bfc区域  与  浮动区域不重叠 */
            overflow: hidden;
            /* 注意！不设置宽度width */
            height: 800px;
            background: green;
        }
    </style>
</head>

<body>
    <div class="left"></div>
    <div class="right"></div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649238686156-d1704e1a-30be-409c-84bd-f7902424bd77.gif#clientId=uc3fd3a6e-d3b1-4&from=drop&height=200&id=uded02847&originHeight=876&originWidth=1541&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2054200&status=done&style=stroke&taskId=u9ccf1725-1e50-4272-aa7e-8f07a84d249&title=&width=352)
<a name="LNP6Q"></a>
### 三栏布局

- 三栏的结构必须是**左-->右-->中**
```html
<div class="left"></div>
<div class="right"></div>
<div class="center"></div>
```
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

        .left {
            float: left;
            width: 300px;
            height: 500px;
            background: pink;
        }

        .center {
            /* 设置成BFC */
            overflow: hidden;
            height: 800px;
            background: green;
        }

        .right {
            /* 设置右浮 */
            float: right;
            width: 200px;
            height: 500px;
            background: skyblue;
        }
    </style>
</head>

<body>
    <!-- 注意！！！三栏的结构 必须是 左右中 -->
    <div class="left"></div>
    <div class="right"></div>
    <div class="center"></div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649251086954-148e6c98-ec1b-4845-b1c8-536ed9c1a373.png#clientId=uc3fd3a6e-d3b1-4&from=paste&height=722&id=u9cc5106c&originHeight=902&originWidth=1900&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8855&status=done&style=stroke&taskId=u619feb91-4e51-404e-9702-efbda4ea784&title=&width=1520)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641917769489-2760aee3-c4cb-4839-8f8d-cea87f3ae631.png#clientId=u620d3163-50ed-4&from=paste&height=200&id=u2aa6a8d1&originHeight=399&originWidth=947&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15747&status=done&style=stroke&taskId=u1ced036e-7645-4d95-8b99-175106479a0&title=&width=473.5)
<a name="LENUx"></a>

# 小结[宽高自适应 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956594390-155ec2f1-bf00-44c0-ab13-89526eebefaa.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956594390-155ec2f1-bf00-44c0-ab13-89526eebefaa.png%22%2C%22name%22%3A%22%E5%AE%BD%E9%AB%98%E8%87%AA%E9%80%82%E5%BA%94%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A313826%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22uc859d267-becc-4375-a67b-52e809c75d1%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u43e2d01a%22%2C%22card%22%3A%22file%22%7D)
