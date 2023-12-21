<a name="b3eR8"></a>
# 相对定位  position: relative;
1. 一般用于一层上面，叠加另一层
2. 与定位一起配套使用的，有坐标
- 水平坐标（`left`/`right`）垂直坐标（`top`/`bottom`）
3. 在浏览器这个平面中，两点确定一个位置，类似地球经纬度
4. 相对定位在**文档流占据位置**，它是**根据自己初始位置来定位**的（来当做参照物）
5. 注意！几乎从来不单独使用相对定位，都是**配合绝对定位**使用
```html
<head>
    <meta charset="UTF-8">
    <title>定位position</title>
    <style>
        div {
            width: 300px;
            height: 300px;
            background: green;
        }

        .box1 {
            background: skyblue;
            position: relative; /* 相对定位 */
            /* left: 110px; */
            /* top: 200px; */ /* 只改变自己的位置 不会影响box2的位置 */
            right: 100px; /* 是与原有位置相比较的 */
            bottom: 200px; /* 是与原有位置相比较的 */
        }
    </style>
</head>

<body>
    <div class="box1">定位position</div>
    <div class="box2">定位position</div>
</body>
```
![原图](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648714757255-a8e505cd-68d9-4f9c-ad38-0f984b7e5155.png#clientId=u493f3331-8b45-4&from=paste&height=501&id=u1033fb3b&originHeight=838&originWidth=425&originalType=binary&ratio=1&rotation=0&showTitle=true&size=8656&status=done&style=stroke&taskId=u862db2f6-b704-4998-a208-6c07f935f93&title=%E5%8E%9F%E5%9B%BE&width=254 "原图")![移动后的位置变化](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648803833195-6671fb0a-c76b-4bf1-8b92-135e3ccaf769.png#clientId=ubaa09af9-da9b-4&from=paste&height=501&id=u5364abf8&originHeight=844&originWidth=428&originalType=binary&ratio=1&rotation=0&showTitle=true&size=20199&status=done&style=stroke&taskId=ubdb1eae0-f584-432c-879b-2f877b125d7&title=%E7%A7%BB%E5%8A%A8%E5%90%8E%E7%9A%84%E4%BD%8D%E7%BD%AE%E5%8F%98%E5%8C%96&width=254 "移动后的位置变化")
<a name="M8rUh"></a>
# 绝对定位 position: absolute;

1. 绝对定位 一定要结合定位坐标使用
- **水平坐标 **`**left**`**/**`**right**`** 垂直坐标 **`**top**`**/**`**bottom**`
2. 定位在当下可视窗口
3. 绝对定位在**文档流不占据位置**，它是根据有定位属性的**父元素**来进行定位的
- 那么如果向上查找， 祖元素一直没有定位，才根据当下可视区域来定位
4. 使用场景：蒙层、二级、banner大图、轮播图
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .big {
            width: 600px;
            height: 600px;
            background: skyblue;
            /* 相对定位 */
            position: relative;
        }

        .son1 {
            width: 100px;
            height: 100px;
            background: green;
            /* 设置绝对定位 */
            position: absolute;
            /* left: 0;
            top: 0; */
            right: 0;
            bottom: 0;
        }

        .son2 {
            width: 150px;
            height: 120px;
            background: yellowgreen;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="son1"></div>
        <div class="son2"></div>
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648715722787-548e3ab7-bc73-4365-9a38-5f4b913af46c.png#clientId=u493f3331-8b45-4&from=paste&height=301&id=u3d7429dc&originHeight=512&originWidth=511&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9303&status=done&style=stroke&taskId=u44139cfc-0534-4901-9939-ad21f016369&title=&width=300)
<a name="EauDa"></a>
## 绝对定位案例-蒙层（父相子绝）

1. `position: relative;` 注意！设置相对定位，不用写坐标
2. `position: absolute;` 注意！设置绝对定位，写坐标
3. `width: 100%;``height: 100%;` 代表图片大小和父元素一致
4. `rgba(颜色值,颜色值,颜色值,透明度);`
- 颜色值取值范围`0~255` 
- 透明度取值`0~1`
5. `transition: 3s;` 过渡时间
```html
<head>
    <meta charset="UTF-8">
    <title>蒙层</title>
    <style>
        .big {
            width: 400px;
            height: 400px;
            background: pink;
            border: 5px dotted deeppink;
            /* 有宽高的div 水平居中 */
            margin: 100px auto;
            /* 父相子绝 */
            position: relative;/* 注意 设置相对定位 不用写坐标 */
        }

        img {
            width: 100%;/* 代表图片大小和父元素一致 */
            height: 100%;
        }

        .mark {/* 这个div 是一个蒙层 设置成和图片一样大 */
            width: 400px;
            height: 400px;
            /* rgba(颜色值,颜色值,颜色值,透明度) 颜色值取值范围0~255 透明度取值0~1 */
            background: rgba(0, 0, 0, 0.6);
            /* 我想要蒙层 盖住图片 一层上面 叠加另一层 想到绝对定位 */
            position: absolute;/* 设置绝对定位  必须写坐标 */
            left: 0;
            top: 0;
            /* 过渡时间 */
            transition: 3s;
        }

        /* 鼠标滑过big 蒙层透明度为0 也是消失的一种 之前的消失有display:none; */
        .big:hover .mark {
            background: rgba(0, 0, 0, 0);
        }
    </style>
</head>

<body>
    <div class="big">
        <img src="../day3/images/1641788125607-2e474cc9-ce1d-4766-8241-773f0bf46ef4.gif" alt="">
        <div class="mark"></div><!-- 蒙层 -->
    </div>
</body>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648716123313-51207184-aaaa-4245-bf1e-a119bd5a4de9.gif#clientId=u493f3331-8b45-4&from=drop&height=237&id=u4087ae14&originHeight=382&originWidth=375&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2754283&status=done&style=stroke&taskId=u675e4477-2782-48e9-8905-6ef2d96733d&title=&width=233)[1.gif](https://www.yuque.com/attachments/yuque/0/2022/gif/25380982/1641788125607-2e474cc9-ce1d-4766-8241-773f0bf46ef4.gif?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fgif%2F25380982%2F1641788125607-2e474cc9-ce1d-4766-8241-773f0bf46ef4.gif%22%2C%22name%22%3A%221.gif%22%2C%22size%22%3A60724%2C%22type%22%3A%22image%2Fgif%22%2C%22ext%22%3A%22gif%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u02d7beb0-da71-45f6-b99d-b73b2e63a52%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ue1f7c2c7%22%2C%22card%22%3A%22file%22%7D)
<a name="z2ejh"></a>
## 子元素垂直水平居中父元素（重要）
```css
父元素 {
       position: relative;
}

子元素 {
       position: absolute;
       left: 50%;	/* 图片的左边框水平居中在图上 */
       margin-left:负宽度一半px;
       top: 50%;	/* 图片的上边框水平居中在图上 */
       margin-top:负高度一半px;
      }
```
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>demo</title>
    <style>
        .big {
            width: 700px;
            height: 600px;
            background: salmon;
            /* 父相子绝 */
            position: relative;
        }

        .son {
            width: 200px;
            height: 300px;
            background: seagreen;
            /* 想要水平居中 可以使用绝对定位 */
            position: absolute;
            left: 50%;/* 图片的左边框水平居中在图上 */
            top: 50%;
            /* margin-left: 负宽度的一半; */
            /* margin-top:负高度一半 */
            margin-left: -100px;
            margin-top: -150px;
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641788331607-3b11cbde-8fca-437e-beb4-530685fa1481.png#clientId=u8ae744f7-3baf-4&from=paste&height=287&id=u432e8f2b&originHeight=574&originWidth=672&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2878&status=done&style=stroke&taskId=u296988dc-e92e-42de-a500-039248531cd&title=&width=336)
<a name="m8cBx"></a>
### banner 大图
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

        #banner {
            /* width: 100%;这一步可不写 */
            /* 设置高度就是图片的高度 */
            height: 460px;
            background: skyblue;
            /* 父相子绝 */
            position: relative;
            /* 溢出隐藏 */
            overflow: hidden;
        }

        #banner img {
            /* 想要水平居中  利用绝对定位做  注意！！只有banner大图这样子写 */
            position: absolute;
            left: 50%;/* 图片的左边框水平居中在图上 */
            top: 0;
            /* margin-left: 负宽度的一半; */
            margin-left: -960px;
            /* 屏幕1920px */
        }
    </style>
</head>

<body>
    <div id="banner">
        <img src="../1.jpg" alt="">
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648716846715-6a2a7387-98f6-4a44-a808-0089fd4137d8.png#clientId=u493f3331-8b45-4&from=paste&height=99&id=ucc5569d4&originHeight=190&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=223804&status=done&style=stroke&taskId=uc3ccfab5-3d23-4880-a1f3-ceb231482da&title=&width=500)[2.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641788529139-0eba220d-4271-492d-be8e-4141723eb7dc.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641788529139-0eba220d-4271-492d-be8e-4141723eb7dc.jpeg%22%2C%22name%22%3A%222.jpg%22%2C%22size%22%3A454052%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8faf7841-28cd-41bc-9294-9e31be2004d%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u2d279eb0%22%2C%22card%22%3A%22file%22%7D)
<a name="MkJoZ"></a>
## 绝对定位案例-透视状态
![OOJQTC624E`RJHW8X90USCH.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641788797570-0cd3f892-5bb3-4c89-b102-5e8395c9cd48.png#clientId=u8ae744f7-3baf-4&from=paste&height=185&id=u84d8cc01&originHeight=369&originWidth=511&originalType=binary&ratio=1&rotation=0&showTitle=false&size=207754&status=done&style=stroke&taskId=ufb179d76-fa05-42df-97dc-e3cbf95c08d&title=&width=255.5)

- 复刻这张图的透视状态
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        body {
            margin: 0;
        }

        .big {
            width: 400px;
            height: 400px;
            /* 父相子绝 */
            position: relative;
        }

        img {
            /* 设置和big一样大 */
            width: 400px;
            height: 400px;
            /* 解决图片3px问题 */
            vertical-align: top;
            border: 0;
        }

        p {
            background: rgba(255, 0, 106, 0.5);
            /* 在一层上面 叠加另一层  绝对定位 */
            position: absolute;
            left: 0;
            bottom: 0;
            /* 设置单行文本省略号 */
            width: 100%;
            white-space: nowrap;/* 让文本在一行显示 */
            overflow: hidden;/* 溢出隐藏 */
            text-overflow: ellipsis;/* 单行文本省略号 */
        }

        span {
            background: #f90;
        }
    </style>
</head>

<body>
    <div class="big">
        <img src="../1.jpg" alt="">
        <p><span>10号</span>今天是腊八，过了腊八就是年，炮竹声中一岁除，噼里啪啦稀里哗啦</p>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649135019212-9b9af742-9f1e-4720-8355-ba76720f9faf.png#clientId=u4047092a-d044-4&from=paste&height=306&id=u4e91f1ef&originHeight=500&originWidth=501&originalType=binary&ratio=1&rotation=0&showTitle=false&size=252629&status=done&style=stroke&taskId=u92a92169-f70e-4344-8343-1245898f852&title=&width=306.8000183105469)
<a name="F0P7o"></a>
## 定位层叠性 z-index: 1;

1. 值越大，越在上方
- 仅作用在定位元素上
2. 默认值`z-index: auto;`
3. z-index可以设置负值，但相当于被放在div盒子后面里，不建议使用
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .box1 {
            width: 300px;
            height: 300px;
            background: palegreen;
            /* 同时设置绝对定位 */
            position: absolute;
            left: 0;
            top: 0;
            z-index: 1;
        }

        .box2 {
            width: 250px;
            height: 350px;
            background: pink;
            /* 同时设置绝对定位 */
            position: absolute;
            left: 0;
            top: 0;
        }
    </style>
</head>

<body>
    <div class="box1"></div>
    <div class="box2"></div>
</body>

</html>
```
![原图](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649136392501-79da470e-1965-4e8d-a096-d86155b9d1da.png#clientId=u4047092a-d044-4&from=paste&height=352&id=ubf56d8ca&originHeight=457&originWidth=390&originalType=binary&ratio=1&rotation=0&showTitle=true&size=1746&status=done&style=stroke&taskId=ub05158d9-329b-4100-98c7-9f89af75e64&title=%E5%8E%9F%E5%9B%BE&width=300 "原图")![z-index: 1; 后box1放在了最上层](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649136426102-7f2914dd-98e1-4b94-8061-f00157d301cc.png#clientId=u4047092a-d044-4&from=paste&height=352&id=uf01c1d8d&originHeight=457&originWidth=454&originalType=binary&ratio=1&rotation=0&showTitle=true&size=4007&status=done&style=stroke&taskId=u42e19895-2f1b-4587-9485-a10a33219a8&title=z-index%3A%201%3B%20%E5%90%8Ebox1%E6%94%BE%E5%9C%A8%E4%BA%86%E6%9C%80%E4%B8%8A%E5%B1%82&width=350 "z-index: 1; 后box1放在了最上层")
<a name="YCzIv"></a>
## 导航栏/二级菜单

- 二级永远设置绝对定位
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>二级菜单</title>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/nav.css">
</head>

<body>
    <!-- 头部外围有颜色 写外围+版心 -->
    <div id="headerWrapper">
        <div id="header">
            <a href="javascript:;">首页</a>
            <a href="javascript:;">四个文字</a>
            <a href="javascript:;">
                它有二级菜单
                <ul class="erji">
                    <li>恭喜发财</li>
                    <li>大吉大利</li>
                    <li>恭喜发财</li>
                    <li>大吉大利</li>
                    <li>恭喜发财</li>
                    <li>大吉大利</li>
                </ul>
            </a><!-- 二级菜单必须设置定位 -->
            <a href="javascript:;">四个文字</a>
            <a href="javascript:;">四个文字</a>
            <a href="javascript:;">四个文字</a>
            <a href="javascript:;">四个文字</a>
            <a href="javascript:;">四个文字</a>
        </div>
    </div>
    <!-- 大图部分 -->
    <div id="banner">
        <img src="../images/2.jpg" alt="">
    </div>
</body>

</html>
```
```css
* {
    /* 去除页面缝隙 */
    margin: 0;
    padding: 0;
}

#headerWrapper {
    background: #f90;/* 外围只设置背景色 */
}

#header {
    width: 1200px;
    height: 100px;
    margin: 0 auto;
    line-height: 100px;/* 单行文本垂直居中 */
}

#header a {
    color: #fff;
    text-decoration: none;
    padding: 0 30px;
    /* background: pink; */
    /* 超链接设置浮动   高度就是行高啦 */
    float: left;
    /* 父相子绝 目的是二级根据我来定位 */
    position: relative;
}

#header a:hover {
    background: #333;
}

ul {
    /* 注意！二级永远设置绝对定位 */
    background: skyblue;
    list-style: none;/* 去掉无序列表的小点 */
    position: absolute;/* 绝对定位 */
    left: 0;/* 距离它父元素垂直对齐 */
    top: 100px;/* 不要挤到文字 */
    /* 设置定位层叠性 */
    z-index: 2;/* 大于0的数字就可以 */
    line-height: 60px;/* 随意设置的 */
    width: 100%;
    text-align: center;
    /* 默认消失 */
    display: none;
}

#header a:hover .erji {
    /* 出现 */
    display: block;
}

/* banner部分 */
#banner {
    height: 460px;
    position: relative;/* 父相子绝 */
    overflow: hidden;
}

#banner img {
    position: absolute;
    top: 0;
    left: 50%;
    margin-left: -960px;
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641808435872-a1be3ffd-42e8-4b59-95ba-4957e31b9d82.png#clientId=u8b24eaf2-6875-4&from=paste&height=227&id=u54405c27&originHeight=349&originWidth=957&originalType=binary&ratio=1&rotation=0&showTitle=false&size=352239&status=done&style=stroke&taskId=u913a797c-21ab-4386-aff5-e846f6027f8&title=&width=622.5)
<a name="MWmWJ"></a>
## 绝对定位为什么要写坐标

- 如果不设置坐标，它默认是根据**父元素内容content区**域来进行定位的
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>绝对定位为什么要写坐标</title>
    <style>
        .big {
            width: 300px;
            height: 100px;
            background: palegreen;
            padding: 100px;
            /* 父相子绝 */
            position: relative;
        }

        .son {
            width: 100px;
            height: 60px;
            background: purple;
            position: absolute;/* 如果不设置坐标 它默认是根据父元素内容content区域来进行定位的 */
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648791238751-54438bd6-44e9-4263-9e3c-d33a6deb49fd.png#clientId=ubaa09af9-da9b-4&from=paste&height=233&id=u240e134a&originHeight=395&originWidth=630&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17308&status=done&style=stroke&taskId=u1269a616-5451-4700-bf75-5f93cc51699&title=&width=371)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .big {
            width: 200px;
            height: 200px;
            background: cyan;
            padding: 50px;
            position: relative;
        }

        span {
            background: red;
            position: absolute;
            /* 默认情况下  绝对定位 是根据参照物的内容区域content定位的    */
        }
    </style>
</head>

<body>
    <div class="big">
        <span>子元素</span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641808980545-a8a82eaa-eec5-4fd3-9653-f1a66eb6defe.png#clientId=u8b24eaf2-6875-4&from=paste&height=193&id=ua3cafa52&originHeight=386&originWidth=779&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9471&status=done&style=stroke&taskId=u640f943a-a5f2-4c90-9246-a8657e45ff7&title=&width=389.5)
<a name="X0TYG"></a>
### 绝对定位根据参照物哪里来定位的

1. 参照物指的是？
- 有定位属性的父元素
- 如果向上查找父元素/祖元素没有定位，则根据浏览器可视窗口来定位
2. 几种情况（见示例）
- 当没有写横纵坐标，是根据参照物的`content`区域来定位的
- 当写了横纵坐标，是根据参照物`padding`（`border`）区域来进行定位的
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .big {
            width: 500px;
            height: 300px;
            padding: 50px;
            border: 10px solid #000;
            background: cyan;
            /* 父相子绝 */
            position: relative;
        }

        .son {
            width: 200px;
            height: 100px;
            background: red;
            position: absolute;/* 当你没有写横纵坐标  那么是根据参照物的content区域来定位的 */
            left: 0;
            top: 0;/* 当你写了横纵坐标 你会发现 绝对定位是根据参照物padding区域来进行定位的 */
            /* ---------------------------- */
            left: -10px;
            top: -10px;/* 此时的绝对定位是根据参照物border区域来进行定位的 */
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642318225842-bc4689bc-5b8c-4b53-8e40-ba351f22009e.png#clientId=u07b68dfc-f7a4-4&from=paste&height=339&id=u7daffe77&originHeight=628&originWidth=927&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21175&status=done&style=stroke&taskId=ucf6cbc87-4db1-4eac-9c86-3af3d312069&title=&width=500)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642318348582-b1f8de5c-d1f8-40f8-8cd2-447b5e56dd2f.png#clientId=u07b68dfc-f7a4-4&from=paste&height=310&id=u4733531c&originHeight=771&originWidth=1242&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37245&status=done&style=stroke&taskId=u1d6c6af9-a210-44df-9bae-817133baca7&title=&width=500)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642318545958-35b44ae8-f078-4cf7-a3c6-6d1e55db2cfa.png#clientId=u07b68dfc-f7a4-4&from=paste&height=339&id=u7306d897&originHeight=530&originWidth=782&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28297&status=done&style=stroke&taskId=u77365696-8c46-425a-ab5e-fcc93a460b4&title=&width=500)

<a name="fR9Pr"></a>
# 固定定位 position: fixed;
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>固定定位</title>
    <style>
        div{
            width: 200px;
            height: 100px;
            background: red;
            /* 固定定位 */
            position: fixed;
            /* 建议 写坐标 */
            right: 30px;
            top: 40%;
        }
    </style>
</head>
<body>
    <div>固定定位</div>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
    <h2>岁岁平安</h2>
</body>
</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648800393999-de43004d-3056-43c4-a024-731f14ddba01.gif#clientId=ubaa09af9-da9b-4&from=drop&height=372&id=ub65d5347&originHeight=842&originWidth=936&originalType=binary&ratio=1&rotation=0&showTitle=false&size=344411&status=done&style=stroke&taskId=u749c67de-0058-4a3e-81ca-4f641d1b171&title=&width=413.4000244140625)
<a name="GgEA1"></a>
## 锚点 <a href="#对应id名字"></a>
```html
<body>
    <!-- <a href="#对应id名字"></a> -->
    <a href="#demo">锚点</a>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2 id="demo" style="color: green;">好好学习</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
</body>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648801184231-7d061b05-df8c-4989-8108-0fe581bf8447.gif#clientId=ubaa09af9-da9b-4&from=drop&height=316&id=u6bec52e4&originHeight=842&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33919&status=done&style=stroke&taskId=uc11979b7-4684-4590-8452-f4cfc360880&title=&width=77)
<a name="D6j3B"></a>
## 固定定位与锚点的案例
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
            width: 100%;
            height: 600px;
            font-size: 60px;
            line-height: 600px;
            text-align: center;
            font-weight: bold;
            color: #fff;
        }

        h1 {
            position: fixed;
            right: 0;
            top: 0;
            width: 100px;
        }

        a {
            text-decoration: none;
            color: #fff;
        }
    </style>
</head>

<body>
    <h1>
        <a href="#d1">一楼</a>
        <a href="#d2">二楼</a>
        <a href="#d3">三楼</a>
        <a href="#d4">四楼</a>
        <a href="#d5">五楼</a>
        <a href="#d6">六楼</a>
    </h1>
    <div class="floor1" id="d1" style="background: orange;">火锅</div>
    <div class="floor2" id="d2" style="background: cyan;">烧烤</div>
    <div class="floor3" id="d3" style="background: blue;">烤肉</div>
    <div class="floor4" id="d4" style="background: pink;">日料</div>
    <div class="floor5" id="d5" style="background: skyblue;">韩料</div>
    <div class="floor6" id="d6" style="background: tomato;">西餐</div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648802337379-9bf6a2f9-9872-45f6-a233-6f769582c800.gif#clientId=ubaa09af9-da9b-4&from=drop&height=268&id=u47b9713a&originHeight=842&originWidth=941&originalType=binary&ratio=1&rotation=0&showTitle=false&size=132286&status=done&style=stroke&taskId=uf649dd49-4de0-4479-a662-8a0e1839dfc&title=&width=300)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641809633446-8363bc5b-a2c1-4ee4-b5e0-9ba210428d96.png#clientId=u8b24eaf2-6875-4&from=paste&height=268&id=uadb515fe&originHeight=884&originWidth=935&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13184&status=done&style=stroke&taskId=u61839a4b-561e-428c-81b3-9328424e824&title=&width=283)
<a name="Rvcz5"></a>
# 粘性定位 position: sticky;

1. 在文档流占位置，滑过并超出这个区域时则变成固定定位
2. 一般应用于移动端，不可以有其他元素来包裹
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            width: 1200px;
            height: 300px;
            background: rgba(22, 33, 99, .5);
            /* 粘性定位 注意 必须写坐标 */
            position: sticky;
            left: 0;
            top: 0;
        }
    </style>
</head>

<body>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <div>粘性定位 一般应用于移动端，不可以有其他元素来包裹</div>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
    <h2>内容</h2>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648813040965-f4d8c928-021e-4071-b8fc-1b4a167cd919.gif#clientId=ubaa09af9-da9b-4&from=paste&height=351&id=ucf6165a4&originHeight=842&originWidth=940&originalType=binary&ratio=1&rotation=0&showTitle=false&size=592041&status=done&style=stroke&taskId=u4dcd493e-ee07-4c8a-80c6-6357e125981&title=&width=392.4000244140625)
<a name="nGF01"></a>
# 透明度 rgba、opacity

1. `rgba` 透明，IE8以下不支持，但是好用
2. `opacity: value;` 透明，value取值0~1，高版本支持

     `filter: alpha(opacity="value");`兼容，value取值0~100，低版本支持（IE浏览器）

- `opacity` 需要做兼容来支持各个版本
- `opacity` 具有继承性，子元素会继承父元素的透明，一起变浅，因此建议使用`rgba`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>下午第四节 溜号了 一会听听课</title>
    <style>
        div{
            width: 200px;
            height: 200px;
            /* rgba透明  IE8以下不支持 但是好用 */
            background: rgba(0, 0, 0, 0.5);
            color: #f90;
        }
        p{
            width: 300px;
            height: 399px;
            /* opacity透明  需要做兼容 来支持各个版本 */
            opacity: 0.5; /* 取值0~1 高版本支持 */
            filter: alpha(opacity="50"); /* 兼容 取值0~100 低版本支持 */
            background: #000;
            color: #f90;

        }
    </style>
</head>
<body>
    <div>火狐微软谷歌浏览器</div>
    <p>ie很多正式场合还需要他，不可以丢弃</p>
</body>
</html>
```
<a name="jpKmb"></a>
# [小结](https://www.jianshu.com/p/234c14df8c52)[定位position 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956378920-25820240-fea2-4b88-87b4-0ee8fa92719c.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956378920-25820240-fea2-4b88-87b4-0ee8fa92719c.png%22%2C%22name%22%3A%22%E5%AE%9A%E4%BD%8Dposition%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A491708%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ue981fe2f-58ac-476a-b071-6b4b96d1934%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uc85b6b90%22%2C%22card%22%3A%22file%22%7D)
> 1. 文档流
> 
指盒子按照`html`标签编写的顺序依次从上到下，从左到右排列。块元素占一行，行内元素在一行之内从左到右排列，先写的先排列，后写的排在后面，每个盒子都占据自己的位置。
> 2. 关于定位
> 
我们可以使用`css`的`position`属性来设置元素的定位类型，`postion`的设置项如下：
> - `relative` 生成**相对**定位元素，元素所占据的**文档流**的位置**保留**，元素本身相对**自身原位置进行偏移**。
> - `absolute` 生成**绝对**定位元素，元素**脱离文档流**，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于上一个设置了**定位的父级元素**来进行定位，如果找不到，则相对于`**body**`**元素**进行定位。
> - `fixed` 生成**固定**定位元素，元素**脱离文档流**，不占据文档流的位置，可以理解为漂浮在文档流的上方，相对于**浏览器窗**口进行定位。
> - `static` 默认值，没有定位，元素出现在正常的文档流中，相当于取消定位属性或者不设置定位属性。
> - `inherit` 从父元素继承 position 属性的值。
> 3. 定位元素的偏移
> 
定位的元素还需要用`left`、`right`、`top`或者`bottom`来设置相对于参照元素的偏移值。


