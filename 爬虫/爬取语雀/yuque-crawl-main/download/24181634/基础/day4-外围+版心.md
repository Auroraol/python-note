<a name="accMd"></a>
# 目的
1. 用户的分辨率是不一样的，不能确定（`1920/1600/1440/1360/1280px`），为了让各个屏幕分辨率可以友好的展现我们的页面，这个目的
2. 那么怎么做呢？我们要写版心+外围
- 注意！一般情况下，我们设置的版心，宽度不要超过`1280px`
3. 为什么？因为有些页面的背景色是延展到浏览器整屏的
<a name="szNKC"></a>
# 外围版心用`id`，其他用`class`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/demo.css">
</head>

<body>
    <!-- 头部 -->
    <div id="headWrapper"><!-- 外围 背景色延伸到整个浏览器 -->
        <div id="header" class="same"><!-- 版心 -->
            头部内容
        </div>
    </div>
    <!-- logo区域 -->
    <div id="logo" class="same"></div>
    <!-- 导航栏区域 外围有颜色 所以需要写版心+外围 -->
    <div id="navWrapper">
        <div id="nav" class="same"><!-- 版心 -->
            导航栏内容
        </div>
    </div>
</body>

</html>
```
```css
* { /* 去除页面缝隙 */
    margin: 0;
    padding: 0;
}

/* 因为前三大块的版心 宽度一致 都需要水平居中的浏览器 */
.same {
    width: 1200px;
    margin: 0 auto;
}

#headWrapper {
    /* 记住了！！外围只需要设置背景颜色 */
    background: #6f6f6f;
    /* 
        * width: 100%;块状元素默认独占一行 可以省略不写 
        * 高度直接由版心撑开 
        * 因为这个色块下边框延展到外围 所以需要给外围设置边框 
    */
    border-bottom: 2px solid #f2f2f2;
}

#header {
    width: 1200px;
    height: 36px;
    background: cyan;
}

/* 外围是白色 那就不用写 直接写版心 */
#logo {
    height: 90px;
    background: #424b52;
}

/* 导航栏部分 */
#navWrapper {
    /* 外围只需要设置背景颜色即可 */
    background: #008dd5;
}

#nav {
    /* 版心 */
    height: 50px;
    background: pink;
}
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649068091129-1514119f-b8c5-4bc9-8059-56e5665bad53.png#clientId=u6c3525aa-8209-4&from=paste&height=178&id=u39e8084a&originHeight=223&originWidth=1901&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5221&status=done&style=stroke&taskId=u5a0c5474-0c5f-41bf-9aa3-6578f615e51&title=&width=1520.8)
<a name="yRJT9"></a>
# 企业站示例

- 注意：[弹性盒是**父级**作用于**子元素**，子元素作用于孙子级元素，**父元素不作用于孙子级元素**](https://blog.csdn.net/tjy1214/article/details/81330818)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style>
    * {
        margin: 0;
        padding: 0;
    }

    .main {
        display: flex;
        flex-direction: column;
        /* justify-content: center; 在高度没有给定的情况下 浏览器页面向下（y轴）无限延伸 因此使用没有意义 */
        align-items: center;
    }

    .width100 {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    /* 统筹 */
    .same {
        width: 962px;
    }

    /* 顶部 */
    .top {
        height: 101px;
        background: #b0b0b8;
    }

    /* 导航栏 */
    .navigationWrapper {
        background: #2f2f2f;
    }

    .navigation {
        height: 57px;
    }

    /* 轮播图 */

    .bannerWrapper {
        background: #7b7b79;
    }

    .banner {
        height: 465px;
        /* text-align: center; */
    }

    /* 公司新闻 */
    .news {
        height: 269px;
        background: #f1f1f1;
    }

    /* 市场项目 */
    .project {
        height: 276px;
        background: #88a4cc;
    }

    /* 产品中心 */
    .productWrapper {
        background: #e5e5e5;
    }

    .product {
        height: 251px;
    }

    /* 底部 */
    .bottom {
        height: 81px;
        background: #989898;
    }
</style>

<body>
    <div class="main">
        <!-- 顶部 -->
        <div class="top same"></div>
        <!-- 导航栏 -->
        <div class="navigationWrapper width100">
            <div class="navigation same"></div>
        </div>
        <!-- 轮播图 -->
        <div class="bannerWrapper width100">
            <div class="banner same">11111 1111111 1 1 1 1 1 11111111111111111111 11111111111111111111 111111111111111111111111 1111111111111111 1111111 1 1 1 1 1 11111111111111111111 11111111111111111111 111111111111111111111111 1111111111111111 1111111 1 1 1 1 1 11111111111111111111 11111111111111111111 111111111111111111111111 1111111111111111 1111111 1 1 1 1 1 11111111111111111111 11111111111111111111 111111111111111111111111 1111111111111111 1111111 1 1 1 1 1 11111111111111111111 11111111111111111111 111111111111111111111111 11111111111</div>
        </div>
        <!-- 公司新闻 -->
        <div class="news same">11111</div>
        <!-- 市场项目 -->
        <div class="project same">11111</div>
        <!-- 产品中心 -->
        <div class="productWrapper width100">
            <div class="product same">1111</div>
        </div>
        <!-- 底部 -->
        <div class="bottom same">111</div>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648740935505-22b7e31f-fdbb-45ab-be0d-f0c433ea347a.png#clientId=u0c096bc8-1262-4&from=paste&height=512&id=uc8f32ea2&originHeight=640&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7297&status=done&style=stroke&taskId=u5fcd0459-57d8-4962-885a-dfbb0a9ddb4&title=&width=767.2)
