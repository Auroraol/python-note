<a name="Yh4oe"></a>
# 水平居中浏览器
- 有宽高的`div` 水平居中浏览器 设置`margin:0 auto;`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="../css/index.css">
</head>

<body>
    <!-- 页面外围大色块 一般使用id -->
    <!-- 第一部分 头部 -->
    <div id="header" class="same"></div>
    <!-- 第二部分 导航栏 -->
    <div id="nav" class="same"></div>
    <!-- 第三部分 大图 banner -->
    <div id="banner" class="same"></div>
    <!-- 第四部分 内容区域 -->
    <div id="content" class="same"></div>
    <!-- 第五部分 市场项目 -->
    <div id="market" class="same"></div>
    <!-- 第六部分 灰色区域 产品 -->
    <div id="proudct" class="same"></div>
    <!-- 第七部分 尾部 -->
    <div id="footer" class="same"></div>
</body>

</html>
```
```css
/* 去除页面缝隙 */
* { /* 通配符 权重小于等于1 */
    margin: 0;
    padding: 0;
}

/* 
  * 由于这七大块 具有相同的宽度 都需要水平居中的浏览器
  * 所以我给他们起一个相同的class名字same 
  */
.same { /* 代表选中了class名字为same的元素们 */
    width: 961px;
    margin: 0 auto;
    /* 有宽高的div 水平居中 设置margin:0 auto; */
}

#header { /* 代表选中了id名字为header的元素 */
    height: 100px;
    background-color: #f1f1f1;
    /* 有宽高的div 水平居中浏览器 设置margin:0 auto; */
}

#nav {
    height: 58px;
    background: #313131;
}

#banner {
    height: 465px;
    background: #235363;
}

#content {
    height: 270px;
    background: rgb(230, 210, 175);
}

#market {
    height: 275px;
    background: rgb(120, 150, 175);
}

#proudct {
    height: 250px;
    background: rgb(229, 229, 229);
}

#footer {
    height: 82px;
    background: rgb(175, 175, 175);
}
```
![色块布局](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649067755218-b341de54-c458-4003-bdfc-1dc0a8c815fc.png#clientId=u14547d95-3f87-4&from=paste&height=401&id=u6ec0e8e2&originHeight=634&originWidth=424&originalType=binary&ratio=1&rotation=0&showTitle=true&size=2578&status=done&style=stroke&taskId=uaa708c2f-39d3-4a2f-b2f7-d9fdc877180&title=%E8%89%B2%E5%9D%97%E5%B8%83%E5%B1%80&width=268 "色块布局")![原图](https://cdn.nlark.com/yuque/0/2022/jpeg/25380982/1641364821225-db55fb37-ecb7-408b-94c6-a83f7e7a2cf2.jpeg#clientId=u9d404f0b-8035-4&from=paste&height=400&id=u1ff9876b&originHeight=1500&originWidth=1346&originalType=binary&ratio=1&rotation=0&showTitle=true&size=503494&status=done&style=stroke&taskId=u790792d7-fad4-434a-968e-3cc528f0eb2&title=%E5%8E%9F%E5%9B%BE&width=359 "原图")


