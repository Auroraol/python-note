<a name="H3r1m"></a>
# 移动端布局单位
<a name="Kvh2N"></a>
## 媒体查询（适用于640px）
<a name="SG3NO"></a>
## rem+vw   

1. 步骤1：需要写理想视口 `<meta.....>`
```html
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no" />
```

2. 步骤2：需要查看设计图大小，750的设计图还是640的设计图，或者是其他尺寸
- `Ctrl`+`Alt`+`C`在`PS`中查看画布大小
3. 步骤3：设置 `html {font-size}`   
- `750`的设计图 `html {font-size: 26.67vw;}`      
- `640`的设计图 `html {font-size: 31.25vw;}`
4. 步骤4：测量的设计图，需要除以`dpr`
- 例如`dpr2`，需要除以2，再除以100，变成`rem`
- 你是几倍图，`dpr`就是几
5. 步骤5：一定要在`body`中重置文字大小 `body{font-size: 0.12rem;}` 
- 为什么重置文字大小？
- 因为`rem`这个单位和`html`的`font-size`相关，但是和`body`无关，那你就在`body`里面重置文字大小，到你合适的文字达大小就可以
6. 步骤6：设置移动端一整屏页面 `html,body {height: 100%;}` 

上述两种方法有点累呢，今天学习一个新的！
<a name="KsaII"></a>
## flexble.js 布局（适用于750px）     
注意！**建议使用在750**的设计图中，**640**的设计图建议**使用**`**rem+vw**`布局

- 步骤0：引入JS文件 `<script src="路径.js"></script>`[flexble.js](https://www.yuque.com/attachments/yuque/0/2022/js/25380982/1650810921491-99e7168f-6684-4061-95d4-2e2e3f0b5293.js?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjs%2F25380982%2F1650810921491-99e7168f-6684-4061-95d4-2e2e3f0b5293.js%22%2C%22name%22%3A%22flexble.js%22%2C%22size%22%3A4073%2C%22type%22%3A%22text%2Fjavascript%22%2C%22ext%22%3A%22js%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u9c952fda-3bf9-42ed-bb98-e757bd0f7a2%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uf564f008%22%2C%22card%22%3A%22file%22%7D)
- 步骤1：不需要设置`meta`，直接将页面自带的那个`**meta**`**视口删掉**！必须删掉！！！
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- 1、删掉meta  -->
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>flexble.js布局</title>
</head>
```

- 步骤2：**不**需要给`**html**`**设置**`**font-size**`，不要设置！！！
- 步骤3：测量的大小，**直接除以100**，即可转换成**rem**，不需要除以dpr！
- 步骤4：建议依旧在`body`中重置文字大小，`font-size: 0.24rem;` 
- 步骤5：设置移动端一整屏页面 `html,body {height: 100%;} `

听起来这个方法很好用！！！试试呗
<a name="BRVob"></a>
# 用之前弹性盒的方式来写布局

- 效果：除了首栏和尾栏外，页面主体部分滚动
- 之前笔记有详细步骤，此方法在本页略看
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- 1、删掉meta  -->
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
    <title>flexble.js布局</title>
    <link rel="stylesheet" href="./css/index.css">
</head>

<body>
    <header></header>
    <main>
        <nav></nav>
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
    </main>
    <footer></footer>
</body>
<!--0 引入js文件 -->
<script src="./js/flexble.js"></script>

</html>
```
```css
* {
    margin: 0;
    padding: 0;
}

/* 设置一整屏页面 */
html,
body {
    height: 100%;
}

body {
    font-size: 0.24rem;
    /* 我们曾经如何书写的  设置弹性盒 */
    display: flex;
    /* 更改主轴的方向  纵向排列 */
    flex-direction: column;
}

/* -------页面四个部分----- */
header {
    width: 100%;
    height: 0.72rem;
    background: rgba(255, 255, 255, 0.5);
}

nav {
    width: 100%;
    height: 2.3rem;
    background: pink;
}

main {
    flex: 1;
    overflow: auto;
    width: 100%;
    /* 高度不要写具体值！！剩余空间都是它的 flex: 1; */
    background: yellow;
}

footer {
    width: 100%;
    height: 0.96rem;
    background: #000;
}
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642564870194-62d5aa61-0c59-4b5c-bbd7-552d4f0ce175.gif#clientId=u9d1a1cf8-ee52-4&from=drop&id=uac5c9369&originHeight=518&originWidth=485&originalType=binary&ratio=1&rotation=0&showTitle=false&size=191673&status=done&style=stroke&taskId=u83657ac0-1dff-4224-8e46-cbaa2cac5c3&title=)
<a name="sJbcB"></a>
# 移动端外围结构布局1（弹性盒flex:1;）

- 效果：用弹性盒纵向排列分栏
- 之前笔记有详细步骤，此方法在本页略看
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>第一种弹性盒</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        body {
            /* 设置弹性盒 */
            display: flex;
            flex-direction: column;
        }

        header {
            width: 100%;
            height: 1rem;
            background: red;
        }

        main {
            flex: 1;
            overflow: auto;
            width: 100%;
            /* height: 不知道 占满整个空间; */
            background: yellow;
        }

        footer {
            width: 100%;
            height: 0.88rem;
            background: blue;
        }
    </style>
</head>

<body>
    <header></header>
    <main></main>
    <footer></footer>

    <script src="../js/flexble.js"></script>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642564962436-135d0b6b-1637-494a-9bf4-2da0ee584a14.png#clientId=u9d1a1cf8-ee52-4&from=paste&height=209&id=u92ad0f93&originHeight=417&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1335&status=done&style=stroke&taskId=ub32a415d-1bee-4b13-bd41-dc9c59c8c3f&title=&width=118)
<a name="L8tp6"></a>
# 定位方式的预热

- 存在弊端：文字的滚动条通到文字上面
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        header {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
        }

        main {
            /* 溢出滚动 */
            overflow: auto;
            width: 100%;
            /* 注意  高度也是占满全屏 */
            height: 100%;
            /* padding-top: 头部高度; */
            /* padding-bottom: 尾部高度; */
            /* 设置怪异盒模型  让盒子宽度不会超出 */
            box-sizing: border-box;
            /* 调整文字和边界之间的距离 */
            padding-top: 1rem;
            /* 同样调整文字和底部之间的距离 */
            padding-bottom: 0.88rem;
            background: pink;
        }

        footer {
            position: absolute;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 0.88rem;
            background: rgba(0, 0, 0, 0.5);
        }
    </style>
</head>

<body>
    <header></header>
    <main>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
        <h2>我是main里面的文字</h2>
    </main>
    <footer></footer>
</body>
<script src="../js/flexble.js"></script>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642565089252-b67f411c-7dd6-4e77-a8e4-ab689bc3b7ad.gif#clientId=u9d1a1cf8-ee52-4&from=drop&id=uda0fe695&originHeight=422&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=617526&status=done&style=stroke&taskId=u33714931-6488-43c1-885f-2757ed37b68&title=)
<a name="vNT5U"></a>
# 移动端外围结构布局2（版心）

1. 借由上述案例可推导，移动端外围大布局，除了给 `body`设置弹性盒之外，我们还可以利用定位来写 
2. 第一步：`header``footer`设置宽高、设置绝对定位  
3. 第二步：给`main`设置
- 高度100%`width: 100%;``height: 100%;`
- `padding-top: 头部的高度;`
- `padding-bottom: 尾部的高度;`
- `box-sizing: border-box;`
4. 第三步：给`main`里面设置一个版心`#mainCon`
- 版心宽高都设置100% `width: 100%;``height: 100%;`
- 给版心设置 `overflow:auto;` 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        header {
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
            position: absolute;
            left: 0;
            top: 0;
        }

        main {
            width: 100%;
            /* 注意  高度也是占满全屏 */
            height: 100%;
            background: pink;
            /* padding-top: 头部高度; */
            /* padding-bottom: 尾部高度; */
            /* 设置怪异盒模型 */
            box-sizing: border-box;
            padding-top: 1rem;
            padding-bottom: 0.88rem;
        }

        #mainCon {
            width: 100%;
            height: 100%;
            background: yellow;
            overflow: auto; /* overflow: auto;设置在版心的好处是 文字不会通顶滚动 只局限于main区域内 */
        }

        footer {
            width: 100%;
            height: 0.88rem;
            background: rgba(0, 0, 0, 0.5);
            position: absolute;
            left: 0;
            bottom: 0;
        }
    </style>
</head>

<body>
    <header></header>
    <main>
        <!-- 需要设置一个版心  来包裹内容 -->
        <div id="mainCon">
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
            <h2>我是main里面的文字</h2>
        </div>
    </main>
    <footer></footer>
</body>
<script src="../js/flexble.js"></script>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642565325873-cae453cd-17bc-40d0-ba41-0af15f37673f.gif#clientId=u9d1a1cf8-ee52-4&from=drop&id=u0d64b40c&originHeight=422&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=463040&status=done&style=stroke&taskId=ud58ab023-1fdd-449f-bdf8-b9c82611a83&title=)
<a name="jTKQ2"></a>
# 移动端外围结构布局3（粘性定位position: sticky;）

- 注意！**粘性定位**的外面一定**不能**有**父元素**来**包裹**它
- 此方法常用于只有**头部固定**，比如小说网站
- 注意！设置绝对定位的话，一开始就不占位置了，而**设置粘性定位仍占位置**
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>只有头部固定</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        header {
            /* 设置粘性定位 默认占位置 鼠标滑过不占位置 */
            position: sticky;
            left: 0;
            top: 0;
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.7);
        }

        main {
            background: cyan;
        }
    </style>
</head>

<body>
    <header></header>
    <main>
        <h2>好多内容</h2>
        <h2>好多内容</h2>
        <h2>好多内容</h2>
        <h2>好多内容</h2>
        <h2>好多内容</h2>
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
    </main>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642565459751-2ef62378-459c-410a-bf3e-8dbd539c5fe5.gif#clientId=u9d1a1cf8-ee52-4&from=drop&id=ubd3bcebd&originHeight=424&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=159011&status=done&style=stroke&taskId=ud89ece7f-747f-4ce6-8a3f-b60a099f314&title=)
<a name="ryVke"></a>
# 移动端外围结构布局4（固定定位position: fixed;）
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        header {
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
            position: fixed;
            /* 固定定位 */
            left: 0;
            top: 0;
        }

        nav {
            width: 100%;
            height: 1.5rem;
            background: red;
            margin-top: 1rem;
        }

        main {
            /* main多大呢??? */
            width: 100%;
            /* 如果nav不放在main里  那么高度就不能设置100% */
            /* height: calc(100% - nav的高度？？？); */
            min-height: calc(100% - 2.5rem - 1rem);
            background: cyan;
        }

        footer {
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
            position: fixed;
            /* 固定定位  永远在 */
            left: 0;
            bottom: 0;
        }
    </style>
</head>

<body>
    <header></header>
    <nav>导航栏</nav>
    <main>
    </main>
    <footer></footer>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        header {
            /* 固定定位 */
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
        }

        nav {
            width: 100%;
            height: 1.5rem;
            margin-top: 1rem;
            background: red;
        }

        main {
            /* main多大呢??? */
            width: 100%;
            /* 如果nav不放在main里  那么高度就不能设置100% */
            /* height: calc(100% - nav的高度？？？); */
            min-height: calc(100% - 2.5rem - 1rem);
            background: cyan;
        }

        footer {
            /* 固定定位  永远在 */
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 1rem;
            background: rgba(0, 0, 0, 0.5);
        }
    </style>
</head>

<body>
    <header></header>
    <nav>导航栏</nav>
    <main>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
        <h1>nr</h1>
    </main>
    <footer></footer>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642565642270-689f1cc7-b815-49a1-a6b3-e64cd8421a95.gif#clientId=u9d1a1cf8-ee52-4&from=drop&height=400&id=u643c44e9&originHeight=422&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52401&status=done&style=stroke&taskId=ucab1f730-c6a8-4440-9112-7ff2de2d1d9&title=&width=223)![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650867634024-e26025e7-bdab-44d1-b14b-af47ccbd43c0.gif#clientId=u84cf2544-4626-4&from=drop&height=400&id=u8e83260c&originHeight=622&originWidth=350&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129509&status=done&style=stroke&taskId=uef2911d1-9324-4b5a-a515-f37f3197218&title=&width=225)
<a name="varPl"></a>
# 问题汇总
<a name="BUQqG"></a>
## 问题1一行多个
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642582063275-bf73a0cd-5425-4013-99a4-8e35f8cb5757.png#clientId=u291fdd08-8733-4&from=paste&height=155&id=zLUi9&originHeight=310&originWidth=684&originalType=binary&ratio=1&rotation=0&showTitle=false&size=118951&status=done&style=stroke&taskId=uf28ccb78-883c-4c7f-9203-247257acc00&title=&width=342)
<a name="sE2jq"></a>
### 涉及到的知识点汇总

1. `box-sizing: border-box;`怪异盒模型
2. `display: flex;`
- `main`里面的弹性盒，横向一排展示

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642582926096-c710cf6b-f7a8-47d4-84d0-ca2561464e62.png#clientId=u291fdd08-8733-4&from=paste&height=139&id=ZqRAn&originHeight=177&originWidth=383&originalType=binary&ratio=1&rotation=0&showTitle=false&size=47537&status=done&style=stroke&taskId=u46512d37-d0dc-475f-9858-a167943c032&title=&width=300)

3. `flex-wrap: wrap;`折行

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642582958862-6c79d249-a77f-4c49-9300-5a2bcb4c2df9.png#clientId=u291fdd08-8733-4&from=paste&height=140&id=tgigK&originHeight=174&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69120&status=done&style=stroke&taskId=u6bb2d185-7e41-43b1-959f-b7b8a8d56f7&title=&width=300)

4. `display: flex;`
- `section`里面的弹性盒，让每一个小模块中图片和文字呈横向展现

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642582985750-69abe55d-a54f-4dbd-a2d7-d58b6bf82432.png#clientId=u291fdd08-8733-4&from=paste&height=145&id=hTeBg&originHeight=181&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=92875&status=done&style=stroke&taskId=u8436bd21-3760-4382-90dd-fde242ded59&title=&width=300)

5. `flex-direction: column;`
- 更改主轴方向，让图片与文字两个小模块呈纵向分布

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642583065333-2e9bac4d-c776-446b-bef7-08deac2c4082.png#clientId=u291fdd08-8733-4&from=paste&height=143&id=HUQGF&originHeight=179&originWidth=375&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88325&status=done&style=stroke&taskId=u350ed973-7578-4f37-9b3e-4a963df3b80&title=&width=300)

6. 在主轴垂直居中`justify-content: center;`
7. 在交叉轴垂直居中`align-items: center;`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642583084357-3acbfddd-146a-40e1-8820-7f412722dcc2.png#clientId=u291fdd08-8733-4&from=paste&height=140&id=POPEK&originHeight=174&originWidth=374&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69852&status=done&style=stroke&taskId=u993118c9-e26f-41f2-beb7-335b50a4677&title=&width=300)
<a name="E0uS4"></a>
### 代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        body {
            font-size: 0.24rem;
        }

        main {
            /* 做弹性盒  让所有图片在一行展示 */
            display: flex;
            /* 折行 */
            flex-wrap: wrap;
            width: 100%;
            height: 3.5rem;
            background: #f90;
        }

        section {
            /* 让每一个小模块中图片和文字呈横向展现 */
            display: flex;
            /* 更改主轴方向 让图片与文字两个小模块呈纵向分布 */
            flex-direction: column;
            /* 在主轴垂直居中 */
            justify-content: center;
            /* 在交叉轴垂直居中 */
            align-items: center;
            width: 20%;
            /* border: 1px solid #000; 这两步是用来 在一开始确定模块大小位置 */
            /* box-sizing: border-box; 这两步是用来 在一开始确定模块大小位置 */
            background: pink;
        }
    </style>
</head>

<body>
    <main>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
        <section>
            <img src="../images/1.png" alt="">
            <span>坐公交</span>
        </section>
    </main>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642574877057-61f7df35-d9f2-49b3-91ad-4059a54e1fe6.png#clientId=uca37f6ec-4acc-4&from=paste&height=339&id=x2cQU&originHeight=417&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8179&status=done&style=stroke&taskId=u057ef0e2-f64a-4bff-9799-bcf1e23dc19&title=&width=192)
<a name="gzNmQ"></a>
### 问题1练习（弹性盒）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642583323321-fe768ecd-bce8-4b95-ae6b-9ab3d733344f.png#clientId=ueb00148a-87ba-4&from=paste&height=431&id=u7b5bf567&originHeight=760&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=129334&status=done&style=stroke&taskId=ua693bb28-e1a3-44c5-8d60-2dcac520bf6&title=&width=228)

- 让文字和图片之间有点距离`margin-bottom: 0.1rem;`

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642583625540-aa0e3494-7c2b-4877-80dc-d4aefa24c9e5.png#clientId=ueb00148a-87ba-4&from=paste&height=81&id=tlkC5&originHeight=97&originWidth=241&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15160&status=done&style=stroke&taskId=u388daba9-d69b-457f-bf41-4644f7a15aa&title=&width=201)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        main {
            width: 100%;
            background: pink;
            display: flex;
            /* 折行 */
            flex-wrap: wrap;
        }

        section {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 33.33%;
            height: 2rem;
            background: chartreuse;
            border: 1px solid #f00;
            box-sizing: border-box;
        }

        section img {
            width: 0.84rem;
            margin-bottom: 0.1rem;
            /* 让每一个小模块内文字和图片之间有点距离 */
        }
    </style>
</head>

<body>
    <main>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选触发
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选啊
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
        <section>
            <img src="../images/1.png" alt="">
            精选
        </section>
    </main>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642574939377-143ddfae-6971-435c-80ea-ed45e2e29f68.png#clientId=uca37f6ec-4acc-4&from=paste&height=359&id=uf1c70da5&originHeight=417&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18585&status=done&style=stroke&taskId=uaaf2e460-9c2b-4e33-b750-81d10efc0ee&title=&width=203)
<a name="fEtCx"></a>
### 问题1练习2（多列）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642575002721-f99641cc-1a69-4f50-9269-857da416e326.png#clientId=uca37f6ec-4acc-4&from=paste&height=383&id=u12260496&originHeight=417&originWidth=236&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15228&status=done&style=stroke&taskId=u4b50c8fc-7b97-486a-818e-5e66de1734a&title=&width=217)![元素是从上至下，从左至右排序的（辅助理解图）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650895781636-87697c1c-6ade-4aee-b869-d78856565835.png#clientId=u84cf2544-4626-4&from=paste&height=231&id=u30080939&originHeight=427&originWidth=401&originalType=binary&ratio=1&rotation=0&showTitle=true&size=49815&status=done&style=stroke&taskId=ua24332ed-cc27-4846-a33d-a80aaeca4ee&title=%E5%85%83%E7%B4%A0%E6%98%AF%E4%BB%8E%E4%B8%8A%E8%87%B3%E4%B8%8B%EF%BC%8C%E4%BB%8E%E5%B7%A6%E8%87%B3%E5%8F%B3%E6%8E%92%E5%BA%8F%E7%9A%84%EF%BC%88%E8%BE%85%E5%8A%A9%E7%90%86%E8%A7%A3%E5%9B%BE%EF%BC%89&width=217 "元素是从上至下，从左至右排序的（辅助理解图）")
<a name="VDqxs"></a>
#### 涉及到的知识点汇总

1. 多列`column-count: 列数;`
- 一定要搭配`break-inside: avoid;`
<a name="Sgac0"></a>
## 问题2横向滚动（版心）

1. 第一步：设置版心  
2. 第二步：给版心设置宽度
- 比如 `width: 200%;`
3. 第三步：设置滚动条（横动纵不动）
- 横向滚动 `overflow-x: auto;`
- 纵向不动 `overflow-y: hidden;`
4. 第四步：给版心设置弹性盒；两端环绕`justify-content: space-around;`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        nav {
            overflow-y: hidden;
            overflow-x: auto;
            width: 100%;
            height: 1rem;
            background: pink;
        }

        #navCon {
            display: flex;
            justify-content: space-around;
            align-items: center;
            width: 200%;
            height: 1rem;
            background: springgreen;
        }

        main {
            width: 100%;
            height: 3rem;
            background: cyan;
        }
    </style>
</head>

<body>
    <nav>
        <div id="navCon">
            <section>首页</section>
            <section>很多文字</section>
            <section>VIP</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
            <section>其他的哈</section>
        </div>
    </nav>
    <main></main>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![58eebb14-9a1f-4921-a37e-1b5126ea18f5.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642575148641-a67b2246-3bb4-4335-9ef2-ae68a454fdac.gif#clientId=uca37f6ec-4acc-4&from=drop&id=u1dd78170&originHeight=422&originWidth=588&originalType=binary&ratio=1&rotation=0&showTitle=false&size=163152&status=done&style=stroke&taskId=u0a8f9a7e-c1a7-4959-9838-1630215fb27&title=)
<a name="bn0WT"></a>
## 问题3行高line-height和align-items: center;的适用场景
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642585755733-377c0d11-3519-45b9-9c07-10179c217687.png#clientId=ueb00148a-87ba-4&from=paste&height=39&id=WzQvf&originHeight=59&originWidth=79&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7327&status=done&style=stroke&taskId=u16aec078-79cb-463e-b90f-6fac1c9320c&title=&width=52)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642585647128-b2e9ef9d-c2c6-4856-a3cf-249c4f4db3fe.png#clientId=ueb00148a-87ba-4&from=paste&height=38&id=u1dfb8881&originHeight=76&originWidth=559&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18649&status=done&style=stroke&taskId=u537946c1-605f-4499-9e34-c143b149b63&title=&width=280)

1. `line-height: 行高;` 会撑满整个行

![line-height: 行高;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650897110096-d3edb71f-646b-4ae8-beb5-9dbf52d3fd0f.png#clientId=u84cf2544-4626-4&from=paste&height=38&id=u23745124&originHeight=77&originWidth=565&originalType=binary&ratio=1&rotation=0&showTitle=true&size=24454&status=done&style=stroke&taskId=u4aaf3446-5665-4933-b236-1377c648241&title=line-height%3A%20%E8%A1%8C%E9%AB%98%3B&width=280 "line-height: 行高;")![添加伪类后的效果](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642585892318-2ee02893-af94-46d1-b778-1e6e2840ff76.png#clientId=ueb00148a-87ba-4&from=paste&height=100&id=vqRzh&originHeight=216&originWidth=151&originalType=binary&ratio=1&rotation=0&showTitle=true&size=18107&status=done&style=stroke&taskId=u64e7af56-d47e-4451-a0cc-d38d28027e4&title=%E6%B7%BB%E5%8A%A0%E4%BC%AA%E7%B1%BB%E5%90%8E%E7%9A%84%E6%95%88%E6%9E%9C&width=70 "添加伪类后的效果")

2. `align-items: center;` 是文字自己高度

![align-items: center;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642585605720-44854f71-c32f-4a74-a0bc-03305e7c9ac6.png#clientId=ueb00148a-87ba-4&from=paste&height=38&id=u7a4234aa&originHeight=77&originWidth=562&originalType=binary&ratio=1&rotation=0&showTitle=true&size=21202&status=done&style=stroke&taskId=u2cefc936-d3fa-41bd-9848-90a8fd80916&title=align-items%3A%20center%3B&width=280 "align-items: center;")![添加伪类后的效果](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642585881905-94bc0908-bceb-496e-a1d6-871a3d026147.png#clientId=ueb00148a-87ba-4&from=paste&height=38&id=u91a8dad9&originHeight=82&originWidth=184&originalType=binary&ratio=1&rotation=0&showTitle=true&size=11436&status=done&style=stroke&taskId=u6220c231-5006-4192-a21a-7cbf1d11590&title=%E6%B7%BB%E5%8A%A0%E4%BC%AA%E7%B1%BB%E5%90%8E%E7%9A%84%E6%95%88%E6%9E%9C&width=85 "添加伪类后的效果")
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        nav {
            display: flex;
            justify-content: space-around;
            align-items: center;
            width: 100%;
            height: 1rem;
            /* line-height: 1rem;  那么  子元素section  高度就是父元素高度 */
            background: pink;
        }

        section {
            position: relative;
        }

        section:first-of-type::after {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            bottom: -0.2rem;
            content: "";
            width: 50%;
            height: 0.05rem;
            background: #f90;
            border-radius: 0.02rem;
        }
    </style>
</head>

<body>
    <nav>
        <section>哈哈哈</section>
        <section>哈哈哈</section>
        <section>哈哈哈</section>
        <section>哈哈哈</section>
        <section>哈哈哈</section>
    </nav>
    <script src="../js/flexble.js"></script>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642575243087-81508cd5-d560-41a0-8d49-b4427c078d98.png#clientId=uca37f6ec-4acc-4&from=paste&height=239&id=ucdb8a16c&originHeight=477&originWidth=587&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3788&status=done&style=stroke&taskId=ubf2ee9fe-d22c-47ef-9517-47c433af4f5&title=&width=293.5)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650898146214-63110ab9-28ce-43d8-8dfb-34b92505a943.png#clientId=u84cf2544-4626-4&from=paste&height=105&id=u4d863c18&originHeight=131&originWidth=119&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3431&status=done&style=stroke&taskId=u1d93d0df-ec70-4b35-8534-9f9e7a40230&title=&width=95.2)
<a name="mfUnu"></a>
## 问题4左右两栏分别滑动
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642575361919-9e734d11-5844-479c-b14e-7fae78398a8d.gif#clientId=uca37f6ec-4acc-4&from=drop&id=k8gLq&originHeight=422&originWidth=242&originalType=binary&ratio=1&rotation=0&showTitle=false&size=234686&status=done&style=stroke&taskId=ua957a3ec-5a40-4ae2-acd4-ef5bd92e262&title=)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642586435756-dc9e6646-a2cd-4dd5-85d9-9244c7b205fb.png#clientId=ueb00148a-87ba-4&from=paste&height=422&id=u7a2af651&originHeight=669&originWidth=377&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43462&status=done&style=stroke&taskId=u5e438721-2f39-4c0e-ac02-92049716e38&title=&width=238)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        html,
        body {
            height: 100%;
        }

        body {
            display: flex;
            flex-direction: column;
        }

        header {
            width: 100%;
            height: 1rem;
            background: red;
        }

        main {
            display: flex;
            overflow: auto;
            width: 100%;
            flex: 1;
            background: yellow;
        }

        .left {
            overflow: auto;
            background: #000;
            width: 1.5rem;
            /* 高度先不写 */
            color: #FFF;
        }

        .right {
            /* 除了left  剩余的都是right */
            flex: 1;
            overflow: auto;
            background: darkred;
        }

        footer {
            width: 100%;
            height: 1rem;
            background: greenyellow;
        }
    </style>
</head>

<body>
    <header></header>
    <main>
        <div class="left">
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
            <h3>左侧</h3>
        </div>
        <div class="right">
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
        </div>
    </main>
    <footer></footer>
</body>
<script src="../js/flexble.js"></script>

</html>
```
