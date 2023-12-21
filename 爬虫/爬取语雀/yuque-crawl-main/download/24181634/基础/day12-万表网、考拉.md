<a name="A3LKH"></a>
# 轮播图
- 用动画来做
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

        /* 3、设置banner的高度  banner的高度与单张图片的高度一致 */
        #banner {
            /* 父相子绝 */
            position: relative;
            /* 溢出隐藏 */
            overflow: hidden;
            width: 100%;
            height: 460px;
            /* background: pink; */
        }

        /* 
            * 4、设置lunbo的大小  注意！lunbo是包裹三张图片的  
            * 那么 设置lunbo的宽度是图片的宽度  lunbo的高度是包裹三张图片的高度 
        */
        .lunbo {
            /* 轮播永远定位 */
            position: absolute;
            left: 50%; /* 图片左边水平居中 */
            top: 0;
            transform: translateX(-50%);
            /* margin≠-50%不可以实现的（语法错误）transform可以 */
            width: 1920px;
            height: 1380px; /* 也可以这么写 height: calc(460px * 3); */
            /* background: green; */
            /* 绑定动画 */
            animation: cc 4s steps(3) infinite;
            /* 
                * steps(3) 是三张图的意思  
                * 均分的是@keyframes cc里面的宽度   
                * infinite 无限次 
            */
        }

        /* 5、解决一下轮播图的图片3px问题  可以用vertical-align: top; */
        .lunbo>img {
            display: block; /* 也可以 */
            border: 0;
            /* 低版本图片有边框 高版本没有了 但是养成习惯 */
        }

        /* 
            * 动画  让他自己动   
            * 首先你要知道  让谁动？？  .lunbo   
            * 动什么？？  top值 
        */
        @keyframes cc {
            0% { top: 0;}
            100% { top: -1380px;} /* 注意  top值应该是图片高度*图片数量 */
        }
    </style>
</head>

<body>
    <div id="banner"> <!-- 1、最大的盒子  展示图片的区域 -->
        <div class="lunbo"> <!-- 2、包裹图片的盒子  此案例为3张图片 -->
            <img src="https://image8.wbiao.co/mall/e7e711e64ed545098c3e0063a99656a2.png" alt="">
            <img src="https://image8.wbiao.co/mall/2511720fb4344ce9af8e528d94991074.jpg" alt="">
            <img src="https://image8.wbiao.co/mall/988281ca043a4b14863fdf35323cee6b.jpg" alt="">
        </div>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650083755302-f271442f-11ec-4396-8f34-ec3d92642a2a.gif#clientId=ua80672a5-c12f-4&from=paste&height=166&id=u74e87b8c&originHeight=208&originWidth=927&originalType=binary&ratio=1&rotation=0&showTitle=false&size=243992&status=done&style=stroke&taskId=u552b29f2-86f3-45b6-91d1-3ffe3a14203&title=&width=741.6)
<a name="FJpLg"></a>
# 万能导航栏

1. 适用于需要长/短边框做分割线情境下
2. 给`<li>`设置左浮，给`<a>`设置`padding`
- 想要短的边框给`<a>`设置
- 想要长的边框给`<li>`设置
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>万能导航栏</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        nav {
            width: 1200px;
            height: 100px;
            line-height: 100px; /* 设置行高等于高度 */
            margin: 0 auto;
            background: cyan;
        }

        /* 1、去除列表样式  去除超链接下划线*/
        ul,
        li {
            list-style: none;
        }

        a {
            /* 3、给a设置左右padding */
            padding: 0 30px;
            border-right: 2px solid #FFF; /* 给a设置右边框 */
            /* background: red; */
            text-decoration: none;
        }

        /* 2、给li设置浮动 */
        nav li {
            float: left;
            /* border-right: 2px solid #000; 给li设置右边框 */
            /* background: springgreen; */
        }

        /* 
            * 4、你需要和高度一致的边框  那就给li设置边框   
            *    你需要和文字一样的边框  那你就a设置边框 
            * 注意！a不能设置浮动
        */
    </style>
</head>

<body>
    <nav>
        <!-- 0、万能导航栏 建议ul>li>a  -->
        <ul>
            <li><a href="javascript:;">全部商品</a></li>
            <li><a href="javascript:;">全部商品</a></li>
            <li><a href="javascript:;">全商品</a></li>
            <li><a href="javascript:;">商品</a></li>
            <li><a href="javascript:;">全部啊商品</a></li>
            <li><a href="javascript:;">全部商品</a></li>
            <li><a href="javascript:;">全部商品</a></li>
            <li><a href="javascript:;">全部商品</a></li>
        </ul>
    </nav>
</body>

</html>
```

- 给a设置右边框效果图

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642210478596-a0eb510b-f57c-4a05-9ac4-5476f8e991b7.png#clientId=u5c35298f-8dad-4&from=paste&height=56&id=u46619b0b&originHeight=127&originWidth=1508&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68698&status=done&style=stroke&taskId=u00ff7e71-85d9-443f-8b8a-0d3a2738d16&title=&width=670)

- 给li设置右边框效果图

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642210833212-dbc5bd11-21bc-45a3-b476-a18dd27b3a08.png#clientId=u5c35298f-8dad-4&from=paste&height=65&id=u83e88428&originHeight=93&originWidth=960&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3275&status=done&style=stroke&taskId=uc95e5c2a-2131-4210-80c3-758295f8291&title=&width=670)
<a name="zAmgN"></a>
# 考拉
<a name="Hdv89"></a>
## 导航栏
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

        p {
            overflow: hidden;
            width: 300px;
            height: 80px;
            border: 1px solid #f00;
            margin: 100px 0 0 100px;
            background: pink;
            border-radius: 40px;
        }

        input {
            float: left;
            outline: 0;
            width: 200px;
            height: 80px;
            border: 0;
            background: pink;
            /* 设置圆角  左上  右上  右下 左下 */
            border-radius: 40px 0 0 40px;
        }

        button {
            float: left;
            width: 100px;
            height: 80px;
            border: 0;
            background: #ff0;
            border-radius: 40px 0 0 40px;
        }
    </style>
</head>

<body>
    <p>
        <input type="text"><button></button>
    </p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642071145270-99fb643a-7cb6-49c2-a577-8c14d885649a.png#clientId=uc1f9726f-d5b6-4&from=paste&height=80&id=ue7c40e67&originHeight=159&originWidth=434&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4389&status=done&style=stroke&taskId=u965172d6-4814-4c8b-8ab5-1554fbba405&title=&width=217)
<a name="RcXKR"></a>
## 完整页面
[QQ截图20220113173840.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642230054640-f6a38478-d4e9-49b6-8f1b-eac46b0cad40.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642230054640-f6a38478-d4e9-49b6-8f1b-eac46b0cad40.png%22%2C%22name%22%3A%22QQ%E6%88%AA%E5%9B%BE20220113173840.png%22%2C%22size%22%3A171148%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22uac47596e-7dd4-4e12-8b76-b0e8ca62f2e%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u587f30fe%22%2C%22card%22%3A%22file%22%7D)[考拉海购.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1642230058320-a3a4ccde-93b2-49ef-903e-d9c6fb8efa64.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1642230058320-a3a4ccde-93b2-49ef-903e-d9c6fb8efa64.png%22%2C%22name%22%3A%22%E8%80%83%E6%8B%89%E6%B5%B7%E8%B4%AD.png%22%2C%22size%22%3A5328313%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u176b94cc-06d8-446e-8fb6-c580851030e%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uac5ae36e%22%2C%22card%22%3A%22file%22%7D)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 引入矢量图库 -->
    <link rel="stylesheet" href="../iconfont.css">
    <!-- 引入外部样式表 -->
    <link rel="stylesheet" href="../css/kaola.css">
</head>

<body>
    <!-- 头部 因为外围有颜色  所以需要写外围+版心-->
    <div id="headerWrapper">
        <header class="same">
            <!-- 头部左侧 -->
            <div class="headLeft">
                <a href="javascript:;">考拉欢迎你</a>
                <a href="javascript:;">登录</a>
                <a href="javascript:;">免费注册</a>
                <a href="javascript:;">手机考拉</a>
            </div>
            <!-- 头部右侧 -->
            <ul class="headRight">
                <li><a href="javascript:;">每日签到</a></li>
                <li><a href="javascript:;">我的订单</a></li>
                <li class="yiji"><a href="javascript:;">个人中心<img src="../images/1.png" alt=""></a></li>
                <li class="yiji"><a href="javascript:;">客户服务<img src="../images/1.png" alt=""></a></li>
                <li class="yiji"><a href="javascript:;">充值中心<img src="../images/1.png" alt=""></a></li>
                <li class="yiji">
                    <a href="javascript:;">消费者权益<img src="../images/1.png" alt=""></a>
                    <!-- 在这里写二级  和<a>兄弟同级  因为鼠标滑过通栏时出现下拉菜单  也就是滑过整块li时 -->
                    <div class="erji">
                        <a href="javascript:;">消费者告知书</a>
                    </div>
                </li>
                <li class="yiji"><a href="javascript:;">更多<img src="../images/1.png" alt=""></a></li>
                <li><a href="javascript:;">视频内容</a></li>
            </ul>
        </header>
    </div>
    <!-- 导航栏 外围没有颜色 直接写版心 -->
    <nav class="same">
        <img src="../images/3.png" alt="">
        <p>
            <input type="text">
            <button></button>
        </p>
        <input type="button" value="购物车">
    </nav>
    <!-- 一级 所有分类部分 -->
    <article class="same">
        <section>
            <i class="iconfont icon-toggle"></i>
            所有分类
            <!-- 二级写在一级里面 注意！只有学习CSS阶段这么写 -->
            <ul>
                <li>
                    <i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i>
                    <div class="sanji" style="background: olive;"></div>
                </li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li>
                    <i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i>
                    <div class="sanji" style="background: tomato;"></div><!-- 注意！三级别写在i里面 -->
                </li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li>
                    <i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i>
                    <div class="sanji" style="background: springgreen;"></div>
                </li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i></li>
                <li class="noborder"><i class="iconfont icon-kouhong"></i>美容彩妆 <i class="iconfont icon-arrow-right"></i>
                </li>
            </ul>
        </section>
        <section>首页</section>
        <section>海外直购</section>
        <section>考拉海购出品</section>
        <section>品质奶粉</section>
        <section>人气面膜</section>
        <section>充值</section>
    </article>
    <!-- 大图区域 -->
    <div id="banner">
        <img src="../images/1.jpg" alt="">
        <div class="end">
            <hgroup class="same"></hgroup>
        </div>
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

/* 去除页面所有超链接下划线  重置超链接颜色*/
a {
    text-decoration: none;
    color: #999999;
}

/* 文字大小具有继承性 所以我先给body设置文字大小 */
body {
    font-size: 12px;
}

/* 去除页面所有列表样式 */
ol,
li,
ul {
    list-style: none;
}

/* -----------统筹----- */
/* 因为页面版心都是一样的宽度1095  都需要水平居中  所以我给这几块大的版心起了一个相同的class名字same */
.same {
    width: 1095px;
    margin: 0 auto;
}

/* -----------头部------ */
#headerWrapper { /* 外围只需要设置背景色 */
    /* 因为边框是延展到外围  所以设置给外围 */
    border-bottom: 1px solid #ededee;
    background: #000;
}

header {
    height: 30px;
    line-height: 30px; /* 单行文本垂直居中 */
    /* background: pink; */

}

header a {
    padding: 0 18px;
    /* background: cyan; */
}

header a:hover {
    color: #FFF;
}

.headLeft {
    float: left;
}

.headLeft>a:first-of-type {
    padding: 0 12px 0 0;
}

.headRight {
    float: right;
}

.headRight li a>img {
    vertical-align: middle;
}

.headRight li {
    float: left;
    position: relative;
}

.yiji a:hover {
    color: #ff1e32;
}

/* -------二级---- */
/* 
    * 二级永远绝对定位
    * 二级我希望根据父元素li进行定位  li有一个class叫yiji  父相子绝即可   
    * 因为是根据“消费者权益”这一整个小板块进行定位的 
*/
.erji {
    /* 默认二级是不在的 */
    display: none;
    position: absolute;
    left: 0;
    top: 30px;
    width: 100%;
    height: 44px;
    background: #FFF;
}

.erji a {
    padding-right: 0;
}

/* 什么情况下二级在   鼠标滑过li 二级出现 */
.headRight li:hover .erji {
    display: block;
}

.yiji:hover {
    background: #fff;
}

/* 导航栏部分 */
nav {
    height: 100px;
    /* background: pink; */
}

nav>img {
    float: left;
    margin-top: 26px;
    /* logo距离上方26px */
}

nav p * { /* 代表nav里面p里面所有元素 */
    float: left;
    width: 448px;
    height: 36px;
    /* 它俩都需要去除边框 */
    border: 0;
    outline: 0;
}

nav p button {
    width: 60px;
    background: #ff2c61 url(../images/5.png) no-repeat center;
    border-radius: 18px; /* 设置圆角  高度一半36/2=18 */
}

nav p {
    float: left;
    /* 为啥  因为p是块状元素 独占一行 我想图片  p  购物车按钮在一行  所以浮动 */
    overflow: hidden;
    border: 2px solid #ff2337;
    margin: 33px 0 0 147px;
    background: #ff2c61;
    border-radius: 20px; /* 36+4=40 */
}

input[type="button"] { /* 写法参考day11-CSS3选择器及属性 */
    float: left;
    width: 110px;
    height: 40px;
    border: 2px solid #ff2337;
    margin: 33px 0 0 50px; /* button参考day7-小米搜索框 button属性委屈自己 */
    background: #FFF url(../images/4.png) no-repeat 20px center;
    color: #333333;
    text-indent: 39px; /* 调整按钮中“购物车”文字的位置 */
    border-radius: 20px;
}

/* ---------所有分类部分----- */
article {
    height: 43px;
    line-height: 40px;
}

section {
    float: left;
    padding: 0 20px;
    font-size: 14px;
    font-weight: bold;
    color: #333333;
}

section:first-of-type {
    /* 父相子绝 */
    position: relative;
    width: 164px;
    padding: 0;
    margin-right: 25px;
    color: #FFF;
    background: linear-gradient(to right, #ff0103, #ff3162);
    font-weight: normal;
}

article .iconfont { /* 儿子 孙子级别全部被选中 */
    color: #dddddd;
}

section>.iconfont { /* 儿子级别的被选中 */
    margin: 0 24px 0 15px;
}

/* 注意！！注意！！你上方  代表选中了article里面所有矢量图  不行啊 */
section li .iconfont:first-of-type { /* 选中了section里面li 里面的第一个i */
    margin: 0 27px 0 16px;
}

section li .iconfont:last-of-type {
    float: right;
    margin-right: 16px;
}

/* 这个是在轮播图的区域 */
section ul {
    /* 设置定位  设置绝对定位 */
    position: absolute;
    left: 0;
    top: 41px; /* 行高40边框1 */
    z-index: 3; /* 将导航栏置顶于banner大图上面 */
    width: 154px; /* 164-10=154 */
    height: 460px;
    line-height: 37px;
    padding: 0 7px 0 3px;
    background: linear-gradient(to right, #ff0103, #ff3162);
}

section ul li {
    border-bottom: 1px solid #ff5160;
}

.noborder {
    border: 0 !important;
}

/* 我们开始写三级啦 */
.sanji {
    /* 默认三级消失 */
    display: none;
    /* 三级也是定位 绝对定位 */
    position: absolute;
    left: 164px;
    top: 0;
    width: 928px;
    height: 460px;
}

/* 鼠标滑过二级里面的li 对应的三级出现 */
section ul li:hover .sanji { /* 写法参考day2-CSS样式表的创建及其优先级 */
    display: block;
}


/* -----------------bannner----------- */
#banner {
    position: relative;
    overflow: hidden;
    height: 506px;
}

#banner img {
    position: absolute;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
}

#banner .end {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 44px;
    background: rgba(0, 0, 0, 0.5);
}

.hgroup {
    height: 44px;
    background: cyan;
}
```
<a name="vYc6Z"></a>
# [万表网](https://www.wbiao.cn/)
<a name="S44KS"></a>
## 头部二级边框问题
![万表网实际效果图](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650117655493-a4c786c4-7353-44ff-ac19-f4930341d323.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=248&id=u66172545&originHeight=310&originWidth=353&originalType=binary&ratio=1&rotation=0&showTitle=true&size=31252&status=done&style=stroke&taskId=uc8dad12a-a088-4b3b-b952-6abfedaa1b7&title=%E4%B8%87%E8%A1%A8%E7%BD%91%E5%AE%9E%E9%99%85%E6%95%88%E6%9E%9C%E5%9B%BE&width=282.4 "万表网实际效果图")![辅助参考图（1）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650117775317-96787f9d-2613-4d4d-b244-bcbda8cf1f52.png#clientId=u4bc6d5ff-29ba-4&from=paste&height=248&id=ucfffa51f&originHeight=316&originWidth=354&originalType=binary&ratio=1&rotation=0&showTitle=true&size=24482&status=done&style=stroke&taskId=ua7516489-ca0c-4dec-876d-3b013543eec&title=%E8%BE%85%E5%8A%A9%E5%8F%82%E8%80%83%E5%9B%BE%EF%BC%881%EF%BC%89&width=278 "辅助参考图（1）")![辅助参考图（2）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650119258252-8b96e911-92ee-4e39-b66d-0efee773f3fc.png#clientId=u4bc6d5ff-29ba-4&from=paste&height=248&id=uba734287&originHeight=530&originWidth=426&originalType=binary&ratio=1&rotation=0&showTitle=true&size=43203&status=done&style=stroke&taskId=u4dd62a25-85a1-4702-b5b9-bc1cdeb1ebc&title=%E8%BE%85%E5%8A%A9%E5%8F%82%E8%80%83%E5%9B%BE%EF%BC%882%EF%BC%89&width=199 "辅助参考图（2）")![辅助参考图（3）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650119785485-b579bb06-8503-469c-bf80-6b13d7d61d48.png#clientId=u4bc6d5ff-29ba-4&from=paste&height=248&id=ue2377580&originHeight=340&originWidth=335&originalType=binary&ratio=1&rotation=0&showTitle=true&size=20837&status=done&style=stroke&taskId=ubce57e4e-adcc-4969-b703-60a287c5d4c&title=%E8%BE%85%E5%8A%A9%E5%8F%82%E8%80%83%E5%9B%BE%EF%BC%883%EF%BC%89&width=244 "辅助参考图（3）")
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

        header {
            width: 1200px;
            height: 100px;
            line-height: 100px;
            margin: 0 auto;
            background: pink;
        }

        /* 头部导航栏  居右---右浮 */
        .headRight {
            float: right;
            list-style: none;
        }

        /* 万能导航栏 给li设置左浮 给a设置左右padding  想要短的边框给a设置 想要长的边框给li设置 */
        .headRight>li {
            position: relative;
            float: left;
            height: 97px; /* 100-2border-1margin-top=97 */
            border: 1px solid transparent; /* 因为border自带边框  加入透明色边框后  鼠标滑过li不会颤抖 transparent透明边框 */
            margin-top: 1px; /* 因为原图顶部有1px间隙 对照辅助参考图1 */
            background: springgreen;
        }

        .headRight>li>a {
            border-right: 1px solid #fff;
            padding: 0 30px;
            background: pink;
            color: #333;
            text-decoration: none;
        }

        /* 
            * 注意  li在默认情况下就应该存在边框  只不过颜色看不见而已(透明色)  参考第34行代码
            * 鼠标滑过倒数第三个li  让li边框颜色改变 
        */
        .headRight li:nth-last-of-type(3):hover {
            border-color: #f00; /* 如果li不设置边框 鼠标滑过时候会抖 */
            background: #FFF;
        }

        /* -------二级----- */
        .erji {
            /* 默认消失 */
            display: none;
            /* 二级永远绝对定位   参考day8-定位position */
            position: absolute;
            /* right区域是根据padding区域 来定位的 对照辅助参考图3 */
            right: -1px;
            /* 
                * 根据父元素.headRight>li的border区域来下沉定位97+2=99  参考day8-定位position 
                * 也就是说 top值=li高度97+上下border2-往上移动1px=98 对照辅助参考图2
            */
            top: 98px;
            width: 300px;
            height: 400px;
            background: rgb(150, 144, 144);
            border: 1px solid #f00;
        }

        /* 鼠标滑过 出现 */
        li:hover .erji {
            /* 参考day11-CSS3选择器及属性 */
            display: block;
        }

        /* 注意  去除一小部分的边框  我们需要使用伪类来盖住 */
        .headRight li:nth-last-of-type(3)::after {
            position: absolute;
            /* 根据父元素.headRight>li来定位 */
            left: 0;
            bottom: -2px;
            content: "";
            width: 100%;/* 注意  100%是谁的  父元素的吗  不是  根据谁定位  就是谁的  */
            height: 2px;
            background: #f90; /* 正常情况写成白色来盖住 此处写颜色便于查找 */
        }
    </style>
</head>

<body>
    <header>
        <!-- ul>li>a和div -->
        <ul class="headRight">
            <li><a href="javascript:;">首页1</a></li>
            <li><a href="javascript:;">首页2</a></li>
            <li><a href="javascript:;">首页3</a></li>
            <li>
                <a href="javascript:;">首页4</a>
                <div class="erji">在这里加二级</div>
            </li>
            <li><a href="javascript:;">首页5</a></li>
            <li><a href="javascript:;">首页6</a></li>
        </ul>
    </header>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650107579084-f853c204-0966-40db-a8bd-3e21a9cfc491.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=254&id=u635ee05b&originHeight=318&originWidth=933&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8130&status=done&style=stroke&taskId=udbc6ba37-6996-498e-91d1-b07baeb012d&title=&width=746.4)
<a name="qVcGe"></a>
## 导航栏划过有边框
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650166418047-c8d5d5d8-7aff-4870-862d-163f479cba97.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=63&id=ud8e2f58d&originHeight=79&originWidth=1359&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76021&status=done&style=stroke&taskId=u014a67cd-30ab-4ff2-aa6a-526f6180fb5&title=&width=1087.2)
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

        nav {
            width: 1200px;
            height: 100px;
            line-height: 100px;
            margin: 0 auto;
            /* background: pink; */
        }

        section {
            position: relative;
            float: left;
            margin: 0 30px; /* 因为文字下边的边框和文字齐宽，所以不用padding */
            /* background: skyblue; */
        }

        /* 我们先加上  伪类  模拟的边框 */
        section:hover::after {
            position: absolute;
            left: 0;
            bottom: 5px;
            content: "";
            width: 100%; /* 代表宽度和包含块的宽度一样 */
            /* 什么是包含块  你根据谁定位  谁就是包含块 */
            height: 1px;
            background: tomato;
        }
    </style>
</head>

<body>
    <nav>
        <section>男表</section>
        <section>女表</section>
        <section>秒杀</section>
        <section>手表行情</section>
        <section>品牌馆</section>
        <section>体验中心</section>
        <section>名匠维修</section>
    </nav>
</body>

</html>
<!-- section::after表示section各个状态下都有这个伪类
section:hover::after表示section滑过状态下有这个伪类 -->
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650166493408-4bf55c91-cf64-497e-9960-07fa5b7b01b9.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=62&id=u6fe91a79&originHeight=78&originWidth=900&originalType=binary&ratio=1&rotation=0&showTitle=false&size=34409&status=done&style=stroke&taskId=u0dceebb1-05b4-4e15-b7ab-e321dfc807f&title=&width=720)
<a name="SUYG7"></a>
## 鼠标滑过图片放大
![1.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344820343-ccd1a227-4bc4-4b01-850b-c6b85fd60043.gif#clientId=u5c35298f-8dad-4&from=drop&id=u4a9fc513&originHeight=364&originWidth=1508&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5517234&status=done&style=stroke&taskId=uce4d6152-0ea0-45dd-9736-54e06c61d6c&title=)
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
            overflow: hidden;
            width: 400px;
            height: 400px;
        }

        .big>img {
            width: 400px;
            height: 400px;
            border: 0;
            vertical-align: top; /* 解决图片三像素问题 也可以用display: block; */
            transition: 1s; /* 谁变化给谁加1s */
        }

        /* 注意  鼠标滑过big  图变大了 */
        .big:hover img {
            transform: scale(1.5);
        }

        article {
            position: absolute;
            top: 10px;
            width: 100%; /* 让文本水平居中  如果隐藏这行代码高度则由内容撑开 */
            /* background: pink; */
            text-align: center; /* 文字水平居中 */
        }
    </style>
</head>

<body>
    <div class="big">
        <img src="https://image8.wbiao.co/mall/806af5bef42f421a84871cfb683796f8.jpg?x-oss-process=image/resize,w_291"
            alt="">
        <article>
            <b>是加粗的那一拨文字</b>
            <p>这样子就是两行，因为p是块状元素，不会和行内b 在一行显示</p>
            <!-- <p>哈哈哈</p> -->
            <!-- 段落标签<P>不可以嵌套包裹其他块状元素 -->
        </article>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650173363773-3a447d7a-5225-452a-8cf2-5313ba4bf28b.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=278&id=uabe698e9&originHeight=348&originWidth=342&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2580141&status=done&style=stroke&taskId=ua408594b-f0d7-4c6a-b0f0-1eca0fb928e&title=&width=273.6)
<a name="Gn36Y"></a>
## 鼠标滑过盒子阴影
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344744245-19096de8-4498-468a-8ec1-345f496f5cc4.gif#clientId=u5c35298f-8dad-4&from=drop&id=u19997c9c&originHeight=462&originWidth=1006&originalType=binary&ratio=1&rotation=0&showTitle=false&size=245627&status=done&style=stroke&taskId=ua8d62ddd-607e-42bc-b605-ca2c7a6cf5e&title=)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        main {
            width: 1000px;
            height: auto;
            overflow: hidden;
            background: #ddd;
            margin: 0 auto;
        }

        section {
            width: 400px;
            height: 300px;
            background: #fff;
            float: left;
            margin-right: 100px;
            margin-bottom: 30px;
            border: 3px solid #000;
            transition: 0.5s;
        }

        section:nth-of-type(2n) {
            margin-right: 0;
        }

        section:hover {
            /* 盒子阴影 */
            box-shadow: 0px 0px 20px 3px #000;
            /* 盒子向上移动  参考day12-2D、3D */
            transform: translateY(-5px);
        }
    </style>
</head>

<body>
    <main>
        <!-- 也可以用div替换section -->
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
    </main>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650173453442-e54173ec-5f04-455f-9193-52772f58ec87.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=402&id=ud7c58e49&originHeight=848&originWidth=734&originalType=binary&ratio=1&rotation=0&showTitle=false&size=272355&status=done&style=stroke&taskId=u16366f98-9574-496c-9c65-d423f93a923&title=&width=348.20001220703125)
<a name="gjgdn"></a>
## 鼠标滑过蒙层上来
![2.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344674584-c1e793ed-79fe-40f8-9d02-4a0067765211.gif#clientId=u5c35298f-8dad-4&from=drop&id=u6e4b3f1f&originHeight=356&originWidth=491&originalType=binary&ratio=1&rotation=0&showTitle=false&size=132747&status=done&style=stroke&taskId=uaabe5ff9-b71f-4e95-8e7a-16f27fb5d11&title=)
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
            overflow: hidden;
            width: 500px;
            height: 400px;
            margin: 100px auto;
        }

        .big>img {
            width: 500px;
            height: 400px;
        }

        article {
            position: absolute;
            left: 0;
            bottom: -100px;
            width: 100%;
            height: 100px;
            background: rgba(255, 255, 255, 0.5);
            text-align: center;
            transition: 1s;
        }

        /* 鼠标滑过div   让article的bottom值变为0    从-100变成0   就u看见了 */
        .big:hover article {
            bottom: 0;
        }
    </style>
</head>

<body>
    <div class="big">
        <img src="https://image8.wbiao.co/mall/806af5bef42f421a84871cfb683796f8.jpg?x-oss-process=image/resize,w_291"
            alt="">
        <article>
            <p>里面很多文字啊</p>
            <b>就是第二行 因为p独占一行</b>
        </article>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650175263582-d5cce27d-b112-4ecd-bd1b-06073420e12b.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=197&id=ue59c13b1&originHeight=246&originWidth=307&originalType=binary&ratio=1&rotation=0&showTitle=false&size=137621&status=done&style=stroke&taskId=u34e00fdc-8d57-4037-b6b7-bc8ebeca6ba&title=&width=245.6)
<a name="ZXupU"></a>
## 虚焦
<a name="nxZQN"></a>
### 鼠标滑过图片后虚焦
```css
.class名:hover>img {
    filter: blur(2px);
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
        img:hover {
            filter: blur(2px); /* 虚焦 */
        }
    </style>
</head>

<body>
    <img src="1.jpg" alt="">
</body>

</html>
```
![1.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344572884-a86cedcf-a5cb-46f7-bb10-4ba17ee86b66.gif#clientId=u5c35298f-8dad-4&from=drop&id=u4aa0db87&originHeight=311&originWidth=379&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104766&status=done&style=stroke&taskId=ude809627-b3dc-48b3-8556-878c3752707&title=)
<a name="tCczB"></a>
### 鼠标滑过虚焦并出现另一块
![2.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344387768-288415c4-6237-4a81-ae69-75321a2d4ea6.gif#clientId=u5c35298f-8dad-4&from=drop&id=ubb195c8f&originHeight=748&originWidth=1503&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5520471&status=done&style=stroke&taskId=ue1084066-4658-4618-87ea-730f85eae0c&title=)
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
            width: 600px;
            height: 400px;
        }

        .big>img {
            display: block; /* 解决图片3px问题 */
            width: 600px;
            height: 400px;
            border: 0;
        }

        /* 鼠标滑过big  里面的子元素img 虚焦 */
        .big:hover>img {
            filter: blur(2px);
        }

        .imgList {
            /* 默认不出 */
            display: none;
            position: absolute;
            left: 50%;
            top: 50%;
            /* margin-left: 负宽度一半; */
            /* margin-top: 负高度一半; */
            transform: translate(-50%, -50%);
            width: 300px;
            height: 200px;
            background: pink;
        }

        /* 鼠标滑过big  imgList出现 */
        .big:hover .imgList {
            display: block; /* display是没有transition过渡时间的  不用给它加  无效 */
        }
    </style>
</head>

<body>
    <div class="big">
        <img src="1.jpg"
            alt="">
        <div class="imgList"></div>
    </div>
</body>

</html>
```
![鼠标滑过虚焦并出现另一块.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344212825-4357caf3-cb12-46bc-aa97-2877f7b3455b.gif#clientId=u5c35298f-8dad-4&from=paste&height=136&id=u1546146d&originHeight=272&originWidth=379&originalType=binary&ratio=1&rotation=0&showTitle=false&size=89982&status=done&style=stroke&taskId=uc14c545d-84f4-4d52-90c6-fc8aa037c82&title=&width=189.5)
<a name="FU9FO"></a>
## 鼠标滑过换东西了
![1.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642344292278-ae5a77e1-d746-4079-9740-b3496e04b162.gif#clientId=u5c35298f-8dad-4&from=drop&id=u33997886&originHeight=127&originWidth=1503&originalType=binary&ratio=1&rotation=0&showTitle=false&size=116132&status=done&style=stroke&taskId=u6c11d83f-3ead-4d82-9575-986df9470d3&title=)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .small{
            width: 500px;
            height: 300px;
            position: relative;
        }
        .small img{
            width: 500px;
            height: 300px;
            position: absolute;
            left: 0;
            top: 0;
        }
        .small section{
            display: none;
            position: absolute;
            left: 0;
            top: 0;
            width: 500px;
            height: 300px;
            background: skyblue;
        }
        /* 你呢  先让section消失  鼠标滑过再出现就对了 */
        .small:hover section{
            display: block;
        }
    </style>
</head>
<body>
    <div class="small">
        <img src="https://image8.wbiao.co/mall/806af5bef42f421a84871cfb683796f8.jpg?x-oss-process=image/resize,w_291" alt="">
        <section>你想切换时是文字形式就用section标签 否则也是img标签</section>
    </div>
</body>
</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650176887491-1c2ea90b-bd68-477b-9ec7-7b2234e2dc30.gif#clientId=u4bc6d5ff-29ba-4&from=paste&height=195&id=u90ce2df8&originHeight=377&originWidth=624&originalType=binary&ratio=1&rotation=0&showTitle=false&size=269520&status=done&style=stroke&taskId=u5b4d9710-9ce9-40d9-bb3b-884dd5a9176&title=&width=322.20001220703125)
