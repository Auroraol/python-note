<a name="QhRb9"></a>
# 2D 转换
<a name="pQlN8"></a>
## 过渡 transition

- 注意！`display`是没有`transition`过渡时间的，不用给它加，无效
<a name="cSbR8"></a>
### 过渡速度的展现 transition-timing-function

1. 越来越慢 
- `transition-timing-function: ease;`
2. 匀速 
- `transition-timing-function: linear;`
3.  加速
- `transition-timing-function: ease-in;`
4. 减速 
- `transition-timing-function: ease-out;`
5. 先加速后减速 
- `transition-timing-function: ease-in-out;`
6. 逐帧（跳跃性/跨越性过渡）
- `transition-timing-function: steps(5);`
7. 贝塞尔曲线 
- `transition-timing-function: cubic-bezier(.5, -0.85, .22, .9);`

[cubic-bezier.com](https://cubic-bezier.com/#.17,.67,.98,.91)
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
            width: 700px;
            background: green;
        }

        p {
            width: 100px;
            height: 100px;
            background: skyblue;
            /* 设置过渡时间 */
            transition-duration: 5s;
        }

        /* 鼠标滑过div时，里面的p标签变由以下样式 */
        div:hover p {
            width: 700px;
        }

        /* 过渡运动函数 */
        p:nth-of-type(1) {
            transition-timing-function: ease;/* 越来越慢 */
        }

        p:nth-of-type(2) {
            transition-timing-function: linear;/* 匀速 */
        }

        p:nth-of-type(3) {
            transition-timing-function: ease-in;/* 加速 */
        }

        p:nth-of-type(4) {
            transition-timing-function: ease-out;/* 减速 */
        }

        p:nth-of-type(5) {
            transition-timing-function: ease-in-out;/* 先加速后减速 */
        }

        p:nth-of-type(6) {
            transition-timing-function: steps(5);/* 跳跃性/跨越性过渡 */
        }

        p:nth-of-type(7) {
            transition-timing-function: cubic-bezier(.5, -0.85, .22, .9);/* 贝塞尔曲线 */
        }
    </style>
</head>

<body>
    <div>
        <p>ease越来越慢</p>
        <p>linear匀速</p>
        <p>ease-in加速</p>
        <p>ease-out减速</p>
        <p>ease-in-out先加速后减速</p>
        <p>steps(5)跨越性过渡</p>
        <p>cubic-bezier(.5,-0.85,.22,.9)</p>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649641959712-da17c0cb-a2e5-41db-9d74-12538d3c2f6b.gif#clientId=u028ddfdf-79a6-4&from=drop&id=u72f6cca1&originHeight=798&originWidth=861&originalType=binary&ratio=1&rotation=0&showTitle=false&size=404490&status=done&style=stroke&taskId=uc66d4e1f-e237-4fba-97ce-28362c5bd7d&title=)
<a name="DYmb8"></a>
### 过渡时间/延迟/属性/速度 /复合值

1. 过渡时间 `transition-duration: 12s;`
- 注意！谁需要变换，就需要给谁设置过渡时间（比如`img`旋转就给`img`设置过渡时间）

![示例](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649987233762-274569d1-2778-49fd-acf8-101c42093909.png#clientId=u1950fba5-b7d0-4&from=paste&height=174&id=uff03abbf&originHeight=218&originWidth=562&originalType=binary&ratio=1&rotation=0&showTitle=true&size=15686&status=done&style=stroke&taskId=uf020c3ca-91e6-4434-8315-4cbac8da810&title=%E7%A4%BA%E4%BE%8B&width=449.6 "示例")

2. 过渡延迟 `transition-delay: 2s;`
- 鼠标滑过2秒后再发生变化
3. 过渡属性 `transition-property: height, width，backgropund;` 
- 宽、高、背景均缓慢变化
- 当你想要多个属性拥有过渡效果时“,”逗号隔开
- 默认情况下是所有属性都变换 `transition-property: all;`
- 注意！`display`没有过渡属性
4. 过渡速度（过渡运动函数）
- `transition-timing-function: ease;` 默认值，越来越慢
- `transition-timing-function: linear;` 匀速
- 请参考上面“过渡速度的展现”部分的代码
5. 复合属性
- `transition: all/具体属性值 运动时间s/ms 延迟时间s/ms 动画类型;`
- 常见写法：`transition: 3s linear;`（过渡时间 过渡速率）
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>过渡transition</title>
    <style>
        div {
            /* 代表div各个状态下 也就是代表所有状态 */
            width: 200px;
            height: 200px;
            background: cyan;
            /* 1、过渡时间 */
            transition-duration: 12s;
            /* 2、过渡延迟 */
            transition-delay: 2s;/* 鼠标滑过2秒后再发生变化 */
            /* 3、过渡属性  默认情况下  是所有属性变换时  都有过渡  默认值是all  (display没有过渡) */
            transition-property: all;/* 默认所有属性值都可以 */
            transition-property: background;/* 背景缓慢变化 */
            transition-property: height;/* 高度缓慢变化 */
            transition-property: height, width;/* 宽高均缓慢变化  当你想要多个属性拥有过渡效果 逗号隔开 */
            /* 4、过渡速度  过渡运动函数  我们常用匀速 linear  */
            transition-timing-function: ease;/* 默认值 越来越慢 */
            /* ↑请参考上面“过渡速度的展现”的代码 */
            /* 5、复合属性  transition:all/具体属性值 运动时间s/ms 延迟时间s/ms 动画类型 */
            transition: 3s linear;
        }

        /* 鼠标滑过div  div变高 背景颜色变 */
        div:hover {/* 代表鼠标滑过div的状态 也就是只代表一个状态 */
            height: 500px;
            width: 300px;
            background: maroon;
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
<a name="SeDEh"></a>
## 变换 transform: 缩放/旋转/拉伸/位移;

1. 变换 缩放
- 元素放大 `transform: scale(2);`（取值大于0 ）
- 元素消失 `transform: scale(0);`
- 元素倒置 `transform: scale(-1);`（取值小于0）
2. 变换 旋转（有单位`deg`）
- 300度 `transform: rotate(300deg);`
3. 拉伸（有单位`deg`）
- `transform: skew(30deg);`
4. 位移 （单位可以是像素，也可以是百分比）
- `transform: translate(100px);`
- `transform: translate(-100px);`
5. **注意！以上的变化都可以分 X轴 和 Y轴**
- `transform: translateY(100px);`
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
            overflow: hidden;
            width: 500px;
            height: 600px;
            border: 1px solid #000;
        }

        img {
            /* 注意！图片是有自己的宽高的 当你设置了图片的宽 图片会进行等比例缩放至对应的高度 */
            width: 500px;
            /* 谁变化  给谁添加过渡时间 */
            transition: 2s;
        }

        /* 鼠标滑过div  想让img发生变化 */
        div:hover img {
            /* 1、变换  缩放 */
            transform: scale(2);/* 元素放大 */
            transform: scale(0);/* 元素消失 */
            transform: scale(-1);/* 元素倒过来 */
            /* 2、变换  旋转  有单位  deg  */
            transform: rotate(300deg);/* 300度 */
            /* 3、拉伸  有单位  deg */
            transform: skew(30deg);
            /* 4、位移 单位可以是像素 也可以是百分比 */
            transform: translate(100px);
            /* 注意！以上的变化  都可以分 X轴 和 Y轴  */
            transform: translateY(100px)
        }
    </style>
</head>

<body>
    <div>
        <img src="https://th.bing.com/th/id/OIP.K0bK7OGYkF9YXIc608wZ0gHaE8?pid=ImgDet&rs=1" alt="">
    </div>
</body>

</html>
```
<a name="LiCdP"></a>
### 变换原点/动画原点 transform-origin: 水平位置 垂直位置;

- 水平：`left` / `center` / `right` / 像素值
- 垂直：`top` / `center` / `bottom` / 像素值
- 元素默认原点是中点
- 示例
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>扇子开扇</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .big {
            position: relative;
            width: 800px;
            height: 800px;
            margin: 100px auto;
            background: #000;
        }

        .big div {
            /* 设置绝对定位 使10个扇面都定在同一位置 */
            position: absolute;
            left: 310px;
            top: 100px;
            width: 150px;
            height: 500px;
            /* 过渡时间 */
            transition: 1s linear;
            /* 设置动画变换原点 模拟扇子展开形态 */
            transform-origin: center bottom;
        }

        .big:hover .s10 {
            transform: rotate(40deg);
        }

        .big:hover .s9 {
            transform: rotate(32deg);
        }

        .big:hover .s8 {
            transform: rotate(24deg);
        }

        .big:hover .s7 {
            transform: rotate(16deg);
        }

        .big:hover .s6 {
            transform: rotate(8deg);
        }

        .big:hover .s5 {
            transform: rotate(-8deg);
        }

        .big:hover .s4 {
            transform: rotate(-16deg);
        }

        .big:hover .s3 {
            transform: rotate(-24deg);
        }

        .big:hover .s2 {
            transform: rotate(-32deg);
        }

        .big:hover .s1 {
            transform: rotate(-40deg);
        }

        .s1 {
            background-color: red;
        }

        .s2 {
            background-color: #f90;
        }

        .s3 {
            background-color: yellow;
        }

        .s4 {
            background-color: green;
        }

        .s5 {
            background-color: blue;
        }

        .s6 {
            background-color: skyblue;
        }

        .s7 {
            background-color: purple;
        }

        .s8 {
            background-color: rgb(129, 19, 253);
        }

        .s9 {
            background-color: hotpink;
        }

        .s10 {
            background-color: rgb(237, 40, 109);
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="s1"></div>
        <div class="s2"></div>
        <div class="s3"></div>
        <div class="s4"></div>
        <div class="s5"></div>
        <div class="s6"></div>
        <div class="s7"></div>
        <div class="s8"></div>
        <div class="s9"></div>
        <div class="s10"></div>
    </div>
</body>

</html>
```
![实际效果图](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649840990970-b984b36d-16e9-4a68-9cf0-0d4fc5766d01.gif#clientId=uea23c106-4370-4&from=paste&height=223&id=J1udU&originHeight=382&originWidth=463&originalType=binary&ratio=1&rotation=0&showTitle=true&size=216392&status=done&style=stroke&taskId=u40e8e868-88da-416a-8e1e-c93320c0ca7&title=%E5%AE%9E%E9%99%85%E6%95%88%E6%9E%9C%E5%9B%BE&width=270.3999938964844 "实际效果图")![辅助理解图](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649912113587-eda6ef7e-f6c6-45e3-a1c7-c2211328d31e.png#clientId=u392374c9-ce8b-4&from=paste&height=223&id=u1521e237&originHeight=472&originWidth=638&originalType=binary&ratio=1&rotation=0&showTitle=true&size=35339&status=done&style=stroke&taskId=u48dcba34-67d5-40cc-9ade-6b71ef3d1a9&title=%E8%BE%85%E5%8A%A9%E7%90%86%E8%A7%A3%E5%9B%BE&width=301 "辅助理解图")
<a name="Y2hWC"></a>
### "先旋转后位移"和"先位移后旋转"一样吗

1. 等比于“先向右转，再往前走两步 ”和“ 先往前走两步 ，再向右转 ”
2. 不一样的点是什么呢？它们的变换原点不一样，变换原点变了
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>不一样</title>
    <style>
        div {
            width: 100px;
            height: 50px;
            margin: 300px;
            background: pink;
            /* 过渡时间 */
            transition: 1s linear;/* 1秒匀速 */
            /* 变换原点/动画原点   元素默认原点是中点 */
            /* transform-origin: 水平(left/center/right/像素值)  垂直(top/center/bottom/像素值); */
            transform-origin: left center;/* 以左边为原点 */
        }

        div:hover {
            transform: scaleX(2);/* 横向整体放大两倍  文字和面积沿横向同时被拉长 */
        }
    </style>
</head>

<body>
    <div>
        动画原点
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649652477147-2e455498-958c-40cf-aac9-6c242982995b.gif#clientId=u028ddfdf-79a6-4&from=paste&height=66&id=ub366feb9&originHeight=82&originWidth=210&originalType=binary&ratio=1&rotation=0&showTitle=false&size=65691&status=done&style=stroke&taskId=u2627e8ea-81e8-411f-ac76-7530c623ad5&title=&width=168)
<a name="o2uQQ"></a>
### 既想放大又想旋转呢
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
            width: 300px;
            height: 300px;
            background: linear-gradient(#f90, #f00, #00f);/* 渐变 */
            margin: 100px auto;
            /* 添加过渡时间 */
            transition: 2s;
            /* 兼容 */
            -webkit-transition: 2s;
            -moz-transition: 2s;
            -ms-transition: 2s;
            -o-transition: 2s;
        }

        div:hover {
            /* 变换 */
            transform: scale(1.5) rotate(360deg);
            /* scale缩放  rotate旋转 */
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649653477290-40a4e651-49c9-456a-b8fe-4dfd68eebe52.gif#clientId=u028ddfdf-79a6-4&from=drop&height=204&id=ue7514e88&originHeight=568&originWidth=614&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2330726&status=done&style=stroke&taskId=u734c03bc-cee0-4ef6-a506-351cae4d12e&title=&width=220)
<a name="zLwVw"></a>
### 移入出现且横向放大，移出消失
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
            width: 600px;
            height: 80px;
            margin: 0 auto;
            background: pink;
        }

        p {
            width: 10px;
            height: 5px;
            margin: 0 auto;
            background: #000;
            transition: 0.5s linear;
            transform: scaleX(0);
        }

        /* 鼠标滑过big时 里面的p横向放大  */
        .big:hover p {
            transform: scaleX(10);
        }
    </style>
</head>

<body>
    <div class="big">
        <p></p>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649660137372-133a1f87-6f60-4c35-a708-8045af0e19a3.gif#clientId=u028ddfdf-79a6-4&from=drop&id=ud8219965&originHeight=142&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20102&status=done&style=stroke&taskId=u448fc166-f0f9-47a5-9480-45db26e4c0e&title=)
<a name="oHz0e"></a>
# CSS3 3D
<a name="n3kQp"></a>
## X Y Z轴形象助记

- x轴 公园老大爷单杠动图
- y轴 钢管舞动图
- z轴 墙上拧螺丝
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
            height: 300px;
            background: #000;
            margin: 60px auto;
            transition: 1s linear;
        }

        .box1:hover {
            transform: rotateX(60deg);
        }

        .box2:hover {
            transform: rotateY(60deg);
        }

        .box3:hover {
            transform: rotateZ(60deg);
        }
    </style>
</head>

<body>
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
</body>

</html>
```
![依次为X、Y、Z轴](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649837073652-42c82487-5ab1-47ae-add2-48c4b88832cd.gif#clientId=uea23c106-4370-4&from=paste&height=536&id=u8b7a0cdb&originHeight=670&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=true&size=160525&status=done&style=stroke&taskId=u0813a48c-a911-49f3-9f3d-45a6c80a676&title=%E4%BE%9D%E6%AC%A1%E4%B8%BAX%E3%80%81Y%E3%80%81Z%E8%BD%B4&width=164 "依次为X、Y、Z轴")
<a name="AtujG"></a>
## 景深 perspective
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>景深</title>
    <style>
        html,
        body {
            height: 100%;
        }

        body {
            /* 景深 */
            perspective: 82200px;/* 模拟我们眼睛到屏幕直接的距离 */
        }

        #big {
            position: absolute;/* 根据浏览器定位 */
            left: 50%;/* 左上角水平居中与浏览器 */
            top: 50%;/* 左上角水平居中与浏览器 */
            width: 300px;
            height: 400px;
            border: 2px solid #f00;
            margin: -200px 0 0 -150px; 
            /* 
                * 现在这六个面都在big这个平面里面   因为浏览器默认是平面
                * 想变成3D  需要设置3D界面  
                * 给谁设置  一般都是给需要3D显示的父元素设置 
            */
            transform-style: preserve-3d;/* 设置3D界面 */
            transform: rotateX(-30deg) rotateY(20deg);/* 倾斜/旋转 */
        }

        #big>div {/* big里面的div */
            position: absolute;
            left: 0;
            top: 0;
            width: 300px;
            height: 400px;
            background: pink;
        }
    </style>
</head>

<body>
    <div id="big">
        <!-- rotateY沿着y轴旋转度数  -->
        <div style="background:red;transform: rotateY(60deg) translateZ(300px);"></div>
        <div style="background: yellow;transform: rotateY(120deg) translateZ(300px);"></div>
        <div style="background: blue;transform: rotateY(180deg) translateZ(300px);"></div>
        <div style="background:green ;transform: rotateY(240deg) translateZ(300px);"></div>
        <div style="background: purple;transform: rotateY(300deg) translateZ(300px);"></div>
        <div style="background:#000 ;transform: rotateY(360deg) translateZ(300px);"></div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649653661189-48085955-6dac-44d8-af9d-7576a384d863.png#clientId=u028ddfdf-79a6-4&from=paste&height=297&id=u8e653c26&originHeight=890&originWidth=933&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28460&status=done&style=stroke&taskId=ua0015c87-29c4-4d06-b67b-ca39a7d6196&title=&width=311.4000244140625)
<a name="LSHr8"></a>
## 背面不可见
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
            height: 300px;
            line-height: 300px;
            margin: 100px auto;
            background: green;
            font-size: 40px;
            text-align: center;
            transition: 1s;
            /* 1、背面不可见 */
            backface-visibility: hidden;
        }

        div:hover {
            transform: rotateY(180deg);/* 微博上吃瓜，文字翻转180度 */
            /* 2、位移  可以简写  translate3d(tx,ty,tz) */
            transform: translateX(10px) translateY(20px) translateZ(20px);
            transform: translate3d(10px, 20px, 20px);
            /* 3、旋转  可以简写  rotate3d(x,y,z,a) */
            transform: rotateX(10deg) rotateY(17deg);/* 这种10、17不成等比例的没办法简写 */
            transform: rotate3d(10, 17, 0, 1deg);/* 这样勉强也行 但复杂 */
            transform: rotate3d(1, 2, 0, 30deg);/* x是1 y是2 z是0 他们每个之间是30度 */
            /* X是1*30 Y是2*30 Z是0*30 */
        }
    </style>
</head>

<body>
    <div>背面不可见</div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649655277462-2614ea90-3f47-4392-81a2-914f194f0c74.gif#clientId=u028ddfdf-79a6-4&from=drop&height=198&id=uf58c5d9b&originHeight=406&originWidth=275&originalType=binary&ratio=1&rotation=0&showTitle=false&size=226225&status=done&style=stroke&taskId=ued477a7a-c50a-472d-af14-df204077f60&title=&width=134)
<a name="BvHGM"></a>
## 示例
<a name="LOnIC"></a>
### 旋转
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            position: relative;
            width: 600px;
            height: 300px;
            margin: 900px auto;
            background: #f90;
            transform: rotateX(40deg) rotateY(20deg);
            transform-style: preserve-3d;
            animation: gouzi 100s linear infinite;
        }
        @keyframes gouzi {
            0%{transform: rotateX(40deg) rotateY(20deg);}
            100%{transform: rotateX(40deg) rotateY(2000deg);}
        }
        img{
            position: absolute;
            left: 0;
            top: 0;
            width: 600px;
            height: 300px;
        }
        .img1{
            /* 变换 沿Y轴旋转 沿Z轴位移*/
            transform: rotateY(30deg) translateZ(1100px);
        }
        .img2{
            transform: rotateY(60deg) translateZ(1100px);
        }
        .img3{
            transform: rotateY(90deg) translateZ(1100px);
        }
        .img4{
            transform: rotateY(120deg) translateZ(1100px);
        }
        .img5{
            transform: rotateY(150deg) translateZ(1100px);
        }
        .img6{
            transform: rotateY(180deg) translateZ(1100px);
        }
        .img7{
            transform: rotateY(210deg) translateZ(1100px);
        }
        .img8{
            transform: rotateY(240deg) translateZ(1100px);
        }
        .img9{
            transform: rotateY(270deg) translateZ(1100px);
        }
        .img10{
            transform: rotateY(300deg) translateZ(1100px);
        }
        .img11{
            transform: rotateY(330deg) translateZ(1100px);
        }
        .img12{
            transform: rotateY(360deg) translateZ(1100px);
        }

    </style>
</head>
<body>
    <div>
        <img src="./12张素材图/1.jpg" alt="" class="img1">
        <img src="./12张素材图/2.jpg" alt="" class="img2">
        <img src="./12张素材图/3.jpg" alt="" class="img3">
        <img src="./12张素材图/4.jpg" alt="" class="img4">
        <img src="./12张素材图/5.jpg" alt="" class="img5">
        <img src="./12张素材图/6.png" alt="" class="img6">
        <img src="./12张素材图/7.jpg" alt="" class="img7">
        <img src="./12张素材图/8.jpg" alt="" class="img8">
        <img src="./12张素材图/9.jpg" alt="" class="img9">
        <img src="./12张素材图/10.jpg" alt="" class="img10">
        <img src="./12张素材图/11.jpg" alt="" class="img11">
        <img src="./12张素材图/12.jpg" alt="" class="img12">
    </div>
</body>
</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649905078518-9f7c89d0-6348-4598-b421-14ebe0fb717f.gif#clientId=u6ff4bdef-3428-4&from=drop&height=212&id=u1ab22178&originHeight=656&originWidth=923&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10885145&status=done&style=stroke&taskId=u65d5c6b8-18e6-423f-a670-d6c74183dd8&title=&width=298.4000244140625)
<a name="hkmG1"></a>
### 正方体
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
            position: relative;
            width: 300px;
            height: 300px;
            margin: 400PX auto;
            font-size: 100px;
            /* background: rgba(0, 0, 0, 0.5); */
            /* 设置3D属性 */
            transform-style: preserve-3d;
            /* 给父元素倾斜  便于清晰观看 */
            transform: rotateY(10deg) rotateX(20deg);
        }

        .big div {
            width: 300px;
            height: 300px;
            position: absolute;
            left: 0;
            top: 0;
        }

        .s1 {
            background: rgba(248, 7, 7, 0.5);
            /* 前面 */
            transform: translateZ(150PX);
        }

        .s2 {
            background: rgba(243, 231, 12, 0.5);
            /* 后面 */
            transform: translateZ(-150PX);
        }

        .s3 {
            background: rgba(7, 250, 3, 0.5);
            /* 左面 */
            transform: rotateY(90deg) translateZ(150PX);
        }

        .s4 {
            background: rgb(7, 160, 248, 0.5);
            /* 右面 */
            transform: rotateY(90deg) translateZ(-150PX);
        }

        .s5 {
            background: rgba(71, 11, 250, 0.5);
            /* 上面 */
            transform: rotateX(90deg) translateZ(150PX);
        }

        .s6 {
            background: rgba(249, 4, 163, 0.5);
            /* 下面 */
            transform: rotateX(90deg) translateZ(-150PX);
        }
    </style>
</head>

<body>
    <div class="big">
        <!-- 正方体有六个面 -->
        <div class="s1">1</div>
        <div class="s2">2</div>
        <div class="s3">3</div>
        <div class="s4">4</div>
        <div class="s5">5</div>
        <div class="s6">6</div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649910830849-7deca7d8-12b0-4171-b71a-5a6d6b340f4c.png#clientId=u6ff4bdef-3428-4&from=paste&height=282&id=ue06e68ab&originHeight=352&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11508&status=done&style=stroke&taskId=u35be2963-1fb3-446d-b5c3-01757e36be2&title=&width=279.2)
<a name="V1AR6"></a>
# 动画 animation

1. 问题：`transition`过渡+`transform`变换，可以解决页面所有效果，为什么还要学动画? 
2. 先来看看`transition`过渡+`transform`变换的弊端：
- 需要事件触发，你需要鼠标滑过才能看见效果，不能自己动
- 只能从红色变成绿色，不能从红-蓝-白-紫-粉-黄-绿，也就是只能从开始到结束，过程中不能有其他变换
- 生命周期只有一次，想无限次实现，需要你手动无限次触发
- 不能复用，谁需要有变换，就需要给谁设置
3. 综上所述，`animation`（动画）以上问题都可以解决
4. **动画有三要素：动画名字 动画时长 关键帧@keyframes**
- 关键帧（创建动画，画小人书的过程）
- 动画名字（起名）
- 调用动画（翻动书让火柴人动起来）

![[@CR6W(W{E%%6YOHW4XU$9V.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649664666249-edfee5b4-e0d7-4f4a-b52f-6150552e1fd5.gif#clientId=u028ddfdf-79a6-4&from=paste&height=175&id=u441be567&originHeight=219&originWidth=148&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1505245&status=done&style=stroke&taskId=uc8b7019e-38c5-4f5b-bc22-f2ad683ee7b&title=&width=118.4)

5. 常用复合值写法：`**animation: 动画名字 时长（单位 s）速度（linear匀速）次数（infinite无限次）;**`
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
            width: 100px;
            height: 100px;
            background: hotpink;
            /* 绑定动画 */
            /* 1、动画名字 */
            animation-name: gouzi;/* 刚才起的名字叫gouzi */
            /* 2、动画时长 */
            animation-duration: 2s;
            /* 3、动画延迟 */
            animation-delay: .5s;/* 0.5秒 */
            /* 4、动画次数 */
            animation-iteration-count: infinite;/* 默认值 无限次 常用 */
            animation-iteration-count: 2;
            /* 5、动画方向 */
            animation-direction: normal;/* 默认值 从头到尾第一次 再从头到尾第二次 */
            animation-direction: reverse;/* 从尾到头一次 再从尾到头第二次 */
            animation-direction: alternate;/* 从头到尾第一次 再从尾到头第二次 */
            animation-direction: alternate-reverse;/* 从尾到头一次 再从头到尾第二次 */
            /* 6、动画运动函数 */
            animation-timing-function: ease;/* 默认值 越来越慢 */
            animation-timing-function: linear;/* 匀速 */
            animation-timing-function: ease-in;/* 加速 */
            animation-timing-function: ease-out;/* 减速 */
            animation-timing-function: ease-in-out;/* 先加速后加速 */
            animation-timing-function: steps(4);/* 逐帧动画 跨越性 */
            /* 7、扩展 动画结束时的状态 */
            animation-fill-mode: backwards;/* 默认状态 你的初始状态 没有动画时你是什么状态 */
            animation-fill-mode: forwards;/* 将动画最后的状态作为结束状态 */
            animation-fill-mode: both;/* 将动画最后的状态作为结束状态 */
            /* 8、动画的复合属性 */
            animation: name duration timing-function delay iteration-count direction fill-mode;
            animation: 动画名字 动画时长（单位 s） 动画速度（linear匀速） 动画延迟 动画次数（infinite无限次） 动画方向 动画结束状态;
        }

        /* 9、鼠标滑过div  动画暂停 */
        div:hover {
            animation-play-state: paused;
        }

        @keyframes gouzi {/* @k按Tab按键即可 */
            /* 
                * gouzi为动画名字 可以自己随意命名
                * 这里面的百分比 代表的是时间节点  
                * 假设这个动画100s 那么66%代表的是第66s的状态 
            */
            0% {width: 900px; background: red;}
            32% {width: 600px; background: orange;}
            55% {width: 300px; background: yellow;}
            66% {width: 700px; background: green;}
            84% {width: 900px; background: blue;}
            100% {width: 300px; background: purple;}
        }
    </style>
</head>

<body>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
</body>

</html>
```
