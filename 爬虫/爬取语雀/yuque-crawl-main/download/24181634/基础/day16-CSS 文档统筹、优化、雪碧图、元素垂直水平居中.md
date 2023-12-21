<a name="Dybev"></a>
# CSS文档统筹
我们平常写页面时，都会先去写一个`* {margin: 0; padding: 0;}`，天天写挺累的。<br />既然每个页面都需要写，为什么不能写一个`.CSS`文件，把统筹的内容直接写在文件内，在每次使用的时候，直接引入就好。<br />注意！我们写页面时，一般都是外部样式文件，所以引入顺序如下：

1.  先引入公共样式表`reset.css`    
2.  再引入`iconfont.css`  
3.  最后引入自己写的页面的`.css`文件 
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS文档统筹</title>
    <link rel="stylesheet" href="./css/reset.css">
</head>
```
```css
/* 去除页面缝隙 */
html,
body,
div,
p,
h1,
h3,
h2,
h4,
h5,
h6,
input,
button,
img,
ul,
li,
ol,
dl,
dt,
dd,
form,
table,
thead,
tfoot,
tbody,
fieldset,
legend,
select,
textarea,
marquee,
iframe,
header,
nav,
main,
footer,
section,
article,
aside,
hgroup,
figure,
figcaption,
dialog,
video,
audio {
    margin: 0;
    padding: 0;
}

/* 去除页面所有超链接下划线 */
a {
    text-decoration: none;
    color: #000;
}

/* 去除页面所有列表样式 */
ul,
li,
ol {
    list-style: none;
}

/* 取消标签的加粗和倾斜 */
h1,
h2,
h3,
h4,
h5,
h6,
b,
strong,
i,
em,
var {
    font-weight: normal;
    font-style: normal;
}

/* 去除input框聚焦线 */
input,
button {
    outline: 0;
}

/* 解决图片3px问题 */
img {
    vertical-align: top;
    border: 0;
}

/* 页面文字大小常用12px 文字大小有继承性  */
body {
    font-size: 12px;/* 注意 移动端把这行话去掉 */
    font-family: "微软雅黑";
}

/* 高度塌陷的元素 以后给设置一个class名字叫clearFix即可 */
.clearFix::after {
    content: "";
    display: block;
    clear: both;
    overflow: hidden;
    visibility: hidden;
    height: 0;
}

/* 以后 去除边框的元素  直接加一个class名字叫noborder  */
.noborder {
    border: 0 !important;
}
```
<a name="sB09z"></a>
# CSS优化 

1. 代码优化
- 精简
2. 命名优化    
- 结构命名 `.headLeft``.headRight`       
- 语义化命名 `.font12``.colorRed``.header``.nav``.footer`  
3. 图片优化
- `<img src="" alt="">``alt`即便里面什么都不写，你也加上它，便于搜索引擎爬
4. 超链接优化
- `<a href="">文字</a>`使用**文字**当超链接，**不**要使用**图片**/**视频**/**Flash**去做超链接
5. 页面主题优化
```css
<meta name="description" content="描述 感冒了想要退烧 止咳应该怎么办">
<meta name="keywords" content="关键字 感冒药 退烧 止咳 鼻塞 流鼻涕 头晕">
```

6. `PR`值，友情链接
- `PR`值越高，代表这个网站越受欢迎
<a name="YU6Na"></a>
# 雪碧图  

1. 也称为图片整合技术；也叫图片精灵；也叫精灵图；也叫`CSS sprite`
2. 图片整合的意义：
- 核心：是通过更改背景图位置来变化
- **减少**`**HTTP**`**请求次数，加快页面加载速度！**
- 减少UI小姐姐命名困扰
- 在更改最少的图片位置或路径时，可以获得漂亮的样式

[23f3ddf914b1b527d0429a3d713cfe3a.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642650912090-7003cdba-a08a-4626-a362-720f7b2111d1.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642650912090-7003cdba-a08a-4626-a362-720f7b2111d1.png%22%2C%22name%22%3A%2223f3ddf914b1b527d0429a3d713cfe3a.png%22%2C%22size%22%3A67160%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u76008eb5-8ea7-4a47-a27c-61977d4448d%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u5aa8b1cb%22%2C%22card%22%3A%22file%22%7D)[nav.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642650912185-b9d0be0f-1391-47c1-92c7-a69954a3a515.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642650912185-b9d0be0f-1391-47c1-92c7-a69954a3a515.png%22%2C%22name%22%3A%22nav.png%22%2C%22size%22%3A11404%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22uf17e98b8-8cb0-4073-ba04-1e81a57266c%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22udf2b4a93%22%2C%22card%22%3A%22file%22%7D)[nav-on.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642650912186-807de453-775e-40ff-af2b-e49f3fb58ed6.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642650912186-807de453-775e-40ff-af2b-e49f3fb58ed6.png%22%2C%22name%22%3A%22nav-on.png%22%2C%22size%22%3A15884%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u3198138a-009e-41ed-9ee6-6d42cedf046%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22udd92ea9e%22%2C%22card%22%3A%22file%22%7D)[二维码.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642650912209-97992d99-bb9a-4b9c-a931-24f0286e46e1.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642650912209-97992d99-bb9a-4b9c-a931-24f0286e46e1.png%22%2C%22name%22%3A%22%E4%BA%8C%E7%BB%B4%E7%A0%81.png%22%2C%22size%22%3A50048%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u4a38c5d0-3acd-43ab-a783-e103b2ff827%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u6fbe070b%22%2C%22card%22%3A%22file%22%7D)
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
            width: 30px;
            height: 30px;
            /* transition: .3s; */
            background: pink url(../images/二维码.png) no-repeat 0 -35px;
        }

        /* 鼠标滑过  变另一张图 */
        div:hover {
            /* 变得是什么  是背景位置！！！ */
            background-position: 0 -86px;
        }

        section {
            width: 30px;
            height: 30px;
            background: url(../images/二维码.png) -102px -35px;
        }

        section:hover {
            background-position: -102px -86px;
        }

        header {
            height: 78px;
            width: 118px;
            background: url(../images/nav.png) -370px 0;
        }

        header:hover {
            background-image: url(../images/nav-on.png);
        }
    </style>
</head>

<body>
    <div></div>
    <section></section>
    <!-- 练习 -->
    <header></header>
</body>

</html>
```

![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642651098112-4cc01442-f928-439c-a56f-757b6d22bd36.gif#clientId=u9eef4ffd-9ce1-4&from=drop&id=u7db00c42&originHeight=185&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40069&status=done&style=stroke&taskId=ua377ffc6-7636-4b41-874a-c664c7101f5&title=)<br />![QQ图片20220120105200.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642648742365-666ffc76-bb09-41bd-ad9d-b60bf5548f09.png#clientId=u9eef4ffd-9ce1-4&from=paste&height=458&id=x0lln&originHeight=572&originWidth=917&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49638&status=done&style=stroke&taskId=ue137b00a-192c-479b-973e-adc61b229f0&title=&width=733.6)
<a name="L1rL5"></a>
# 回流与重绘
![QQ图片20220120105147.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642648680321-e1e363f8-96b5-47a7-9943-2ba6d294255f.png#clientId=u9eef4ffd-9ce1-4&from=drop&id=u8e9d5438&originHeight=496&originWidth=958&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66090&status=done&style=stroke&taskId=u4690025b-0041-4e4f-a1a9-15b6e82c139&title=)
<a name="Vl2y1"></a>
# 浏览器内核

1. `Trident`    代表作：`IE`
2. `Gecko`        代表作：`Mozilla`
3. `WebKit`      代表作：苹果、谷歌旧版本
4. `Blink`        代表作：谷歌、欧朋
5.  `Presto`   （`Opera`前内核  已经废弃）

![QQ图片20220120105554.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642648689943-2c2696cb-ef48-4a46-9579-289bbf2b18f9.png#clientId=u9eef4ffd-9ce1-4&from=drop&id=ued2346db&originHeight=784&originWidth=948&originalType=binary&ratio=1&rotation=0&showTitle=false&size=94659&status=done&style=stroke&taskId=u1d56cc18-5482-4717-98d2-3e3e8057464&title=)
<a name="vD9lm"></a>
# 指针bug
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
            width: 400px;
            height: 400px;
            background: cyan;
            /* 指针样式设置 cursor  */
            /* cursor: pointer;小手 */
            /* cursor: move;移动 */
            /* cursor: text;文本 */
            /* cursor: progress;小箭头+转圈 */
            /* cursor: wait;转圈 */
            /* cursor: help;箭头+问号 */
            cursor: ne-resize;
            cursor: s-resize;
        }
    </style>
</head>

<body>
    <div>可以变化莫测</div>
</body>

</html>
```
<a name="ERKg2"></a>
# 复习
<a name="SnQyT"></a>
## 兼容
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

        input {
            /* 表单对齐不一致  解决方式  浮动 */
            float: left;
            /* 表单高度不一样  去除他们的边框 如果需要边框 使用p标签设置 */
            height: 50px;
            border: 0;
            background: cyan;
        }

        div {
            width: 30px;
            height: 300px;
            background: cyan;
            /* opacity: 0.5;取值是0~1 */
            /* filter: alpha(opacity="50");  取值范围值0~100 */
        }

        div:hover {
            filter: blur(4px);
        }
    </style>
</head>

<body>
    <p>
        <input type="text">
        <input type="submit">
    </p>
    <div>透明度</div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650899713473-f61fef2a-86a8-4286-9764-a545b92e9160.gif#clientId=ua0d22df6-2bf9-4&from=paste&height=289&id=ud948115c&originHeight=566&originWidth=367&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55965&status=done&style=stroke&taskId=u14afd7ba-0c3f-4a99-b335-8c7e38a8b85&title=&width=187.60000610351562)<br />[day12-万表网、考拉](https://www.yuque.com/naiyoumitaocha/psyhak/dmup6l?view=doc_embed&inner=ZXupU)
<a name="tTiAq"></a>
## 父元素半透明，子元素不透明
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big{
            width: 200px;
            height: 400px;
            background: rgba(66, 66, 66, 0.3);
        }
        .small{
            width: 100px;
            height: 100px;
            background: #000;
        }
    </style>
</head>
<body>
    <div class="big">
        <div class="small"></div>
    </div>
</body>
</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650900006667-f5766253-4a62-4271-a3f2-97db386eb957.png#clientId=ua0d22df6-2bf9-4&from=paste&height=418&id=uac03a596&originHeight=522&originWidth=274&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2439&status=done&style=stroke&taskId=uc8feb923-e6ad-4e52-8a02-12564d70111&title=&width=219.2)
<a name="Tzu20"></a>
## [元素垂直水平居中](https://zhuanlan.zhihu.com/p/411331013)

<a name="OgJTG"></a>
### 1、位移变换![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650900063129-d9318719-f305-47d6-82a8-9c5e1eb5ae40.png#clientId=ua0d22df6-2bf9-4&from=paste&height=100&id=ud8278b1a&originHeight=889&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8570&status=done&style=stroke&taskId=u05655b88-13d1-4b2d-b3e1-b68d1b5b890&title=&width=108)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        section {
            width: 400px;
            height: 400px;
            background: red;
            position: absolute;
            left: 50%;
            top: 50%;
            /* margin-left: 负宽度一半; */
            /* margin-top: 负高度一半; */
            /* 你还可以写成 transform: translate(-50%，-50%); */
            transform: translate(-50%, -50%);/* 基于section自己本身的一半 */
        }
    </style>
</head>

<body>
    <section></section>
</body>

</html>
```
<a name="QziHe"></a>
### 2、定位![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650900097381-2e8c0f01-84c3-4608-ba4c-ad9137d38bfa.png#clientId=ua0d22df6-2bf9-4&from=paste&height=100&id=u0c7c9243&originHeight=890&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8579&status=done&style=stroke&taskId=ua8667ffc-f680-4245-8cd8-1e5dfab370c&title=&width=108)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        section {
            width: 300px;
            height: 300px;
            background: springgreen;
            /* 元素垂直水平居中 */
            position: absolute;
            left: 0;
            top: 0;
            right: 0;
            bottom: 0;
            margin: auto;
        }
    </style>
</head>

<body>
    <section></section>
</body>

</html>
```
<a name="yPLew"></a>
### 3、弹性盒![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650900154254-479c4354-08f9-4e05-8d74-53a70cd60d19.png#clientId=ua0d22df6-2bf9-4&from=paste&height=100&id=ubcbad2c1&originHeight=450&originWidth=387&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2304&status=done&style=stroke&taskId=u734622d5-b7d9-4e45-acbf-17d85e5d1c2&title=&width=86)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big{
            width: 600px;
            height: 700px;
            background: pink;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .small{
            width: 200px;
            height: 200px;
            background: yellow;
        }
    </style>
</head>
<body>
    <div class="big">
        <div class="small"></div>
    </div>
</body>
</html>
```
<a name="IzQS9"></a>
### 4、弹性盒2.0+外边距
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
            height: 700px;
            background: pink;
            display: flex;
        }

        .small {
            width: 200px;
            height: 200px;
            background: yellow;
            margin: auto;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="small"></div>
    </div>
</body>

</html>
```
<a name="KHCrY"></a>
### 5、弹性盒3.0
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
            height: 700px;
            background: pink;
            display: flex;
            justify-content: center;
        }

        .small {
            width: 200px;
            height: 200px;
            background: yellow;
            align-self: center;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="small"></div>
    </div>
</body>

</html>
```
