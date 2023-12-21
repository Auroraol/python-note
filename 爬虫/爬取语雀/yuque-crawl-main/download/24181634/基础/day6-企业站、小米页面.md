<a name="qoFrD"></a>
# 企业站
<a name="rsNY8"></a>
## 运用到哪些知识点了呢？

1. `margin: 0 auto;`页面水平居中浏览器
2. `outline: 0;`去除聚焦线
3. `text-decoration: none;`去除超链接下划线
4. `background: 颜色 图片url() 是否平铺no-repeat 位置; `背景属性
5. `border:1px solid #e5e5e5;`边框大小 边框线型 边框颜色（[参考day4-CSS背景属性](https://www.yuque.com/naiyoumitaocha/psyhak/lkhrdm)）
6. 外围版心用`id`，其余用`class`
7. 让图片垂直水平居中在`div`内（[参考day6-CSS特性、元素](https://www.yuque.com/naiyoumitaocha/psyhak/baflw1)）
- 给`div`设置`text-align:center;`目的是让img在div中**水平居中**
- 给`div`设置`line-height:高度值; `目的是让img在div中**垂直居中**，以默认基线来对齐
- 给`img`设置`vertical-align:middle;`目的是让图片**中线 **在div**垂直居中**
8. `padding`知识点（[参考day5-盒模型](https://www.yuque.com/naiyoumitaocha/psyhak/bw5mu5)）
9. 什么情况下超链接也可以设置高度？浮动时（[参考day4-浮动](https://www.yuque.com/naiyoumitaocha/psyhak/gg5dr1)）
10. `vertical-align: top;`图片下方像素自带3px，解决图片基线缝隙，让图片与上方对齐（[参考day3-CSS核心属性](https://www.yuque.com/naiyoumitaocha/psyhak/rqu9m3)）
11. 浏览器默认文字大小为偶数（[参考day3-CSS核心属性](https://www.yuque.com/naiyoumitaocha/psyhak/rqu9m3)）
12. `font-weight: normal;`取消加粗
13. `font-variant: small-caps;`小写英文变缩小版大写英文
14. `border-radius: 5px;`设置圆角
15. `overflow：hidden;`一刀切（[参考day6-溢出隐藏](https://www.yuque.com/naiyoumitaocha/psyhak/cu7op2)和[参考day5-盒模型](https://www.yuque.com/naiyoumitaocha/psyhak/bw5mu5)）
<a name="zjr01"></a>
## html部分代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/qiyezhan.css">
</head>

<body>
    <!-- 第一部分 头部  因为外围是白色 不用写  直接写版心即可 -->
    <div id="header" class="same">
        <img src="../images/logo.png" alt="">
        <input type="text" placeholder="SEARCH...">
    </div>
    <!-- --------第二部分  导航栏   因为外围有颜色  所以写外围+版心 -->
    <div id="navWrapper"><!-- 外围 -->
        <div id="nav" class="same"><!-- 版心 -->
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;">投资者关系</a>
            <a href="javascript:;">产品中心</a>
            <a href="javascript:;" class="noborder">产品中心</a>
        </div>
    </div>
    <!-- 第三部分 ----大图部分---- -->
    <div id="banner" class="same">
        <img src="../images/4.jpg" alt="">
    </div>
    <!-- --------第四部分--因为外围是白色  直接写版心--- -->
    <div id="content" class="same">
        <div class="xinwen">
            <h2>公司新闻</h2>
            <ul>
                <li>陈建成董事长上课从来不睡觉...<span>2022-01-07</span></li>
                <li>陈建成董事长上课从来不睡觉<span>2022-01-07</span></li>
                <li>陈建成董事长上课从来不睡觉，加油<span>2022-01-07</span></li>
                <li>陈建成董事长不会的及时问<span>2022-01-07</span></li>
                <li>陈建成董事长页面得做啊<span>2022-01-07</span></li>
                <li>陈建成董事长多做多错，多 练多会<span>2022-01-07</span></li>
            </ul>
        </div>
        <div class="jieshao">
            <h2>公司介绍</h2>
            <p class="word p1">公司成立于1984年,</p>
            <p class="word p2">经过近30年的发展</p>
            <p class="p3">已成为电器制造、房地产开发和金融投资三业并举的综合性跨国...</p>
        </div>
        <div class="zhaopin">
            <h2>人才招聘</h2>
            <p>培养一流的人才，铸造一流的工程实现员工与企业的共同发展</p>
            <div class="more">more--></div>
        </div>
    </div>
    <!-- 第五部分   因为外围是白色  直接写版心-->
    <div id="market" class="same">
        <h2>市场项目</h2>
        <div class="marketList">
            <img src="../images/企业站1_07.png" alt="">
            <p>交通轨道：由于主要采用电气牵引，而且轮轨摩擦阻力较小，与公共...</p>
        </div>
        <div class="marketList">
            <img src="../images/企业站1_09.png" alt="">
            <p>节能环保：由于不断上涨的能源消耗和我们专业知识，维护可持续...</p>
        </div>
        <div class="marketList">
            <img src="../images/企业站1_11.png" alt="">
            <p>航空与船舰：如果你是在公海行驶，你需要确保你的船只的电力系统...</p>
        </div>
        <div class="marketList marketList4">
            <img src="../images/企业站1_13.png" alt="">
            <p>石油、天然气及采矿：在市场的安全性，可靠性，效率和最短的停机...
            </p>
        </div>
    </div>
    <!-- -------------------第六部分-------外围有颜色  写外围+版心 -->
    <div id="productWrapper"><!-- 外围 -->
        <div id="product" class="same"><!-- 版心 -->
            <div class="chanpin">
                <h3>产品中心</h3>
                <ul>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>大功率电机</li>
                    <li><span>></span>汽车电机</li>
                </ul>
                <ul class="ul2">
                    <li><span>></span>工业驱动和自动化</li>
                    <li><span>></span>高压变频和系统集成</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>大功率电机</li>
                </ul>
                <ul>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>输变电设备</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>大功电机</li>
                </ul>
            </div>
            <div class="jishu">
                <h3>技术研发</h3>
                <ul>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>汽车电机</li>
                    <li><span>></span>汽车电机</li>
                </ul>
            </div>
            <div class="wangluo">
                <h3>营销网络</h3>
                <img src="../images/企业站1_14.png" alt="">
            </div>
        </div>
    </div>
    <!-- ----------------尾部  外围是白色  直接写版心---- -->
    <div id="footer" class="same">
        <a href="javascript:;" class="nopaddingLeft">网站地图</a>
        <a href="javascript:;">联系我们</a>
        <a href="javascript:;">关注我们</a>
        <a href="javascript:;" class="noborder">采购系统入口</a>
        <p>
            COPYRIGHR&copy;2013卧龙控股集团 版权所有 浙ICP备31682155号 技术支持： 博彩互动 分享到：
            <img src="../images/企业站1_03.jpg" alt="">
            <img src="../images/企业站1_05.jpg" alt="">
            <img src="../images/企业站1_07.jpg" alt="">
            <img src="../images/企业站1_12.jpg" alt="">
            <img src="../images/企业站1_10.jpg" alt="">

        </p>
    </div>
</body>

</html>
```
<a name="rB3Wn"></a>
## CSS部分代码
```css
/* 去除页面缝隙 */
* {
    margin: 0;
    padding: 0;
}

/* 因为页面版心大块的宽度都是一样的 都需要水平居中浏览器；所以我给页面这几个大的版心  设置了一个相同的class名字  */
.same {
    width: 962px;
    margin: 0 auto;
}

/* 头部  设置高度 */
#header {
    height: 100px;
}

/* 头部的图片 距离上方有间距 */
#header img {
    margin-top: 35px;
}

/* 搜索框 需要设置宽高 需要设置边框 靠右--联想到右浮 */
input {
    width: 223px;
    height: 26px;
    border: 1px solid #e5e5e5;
    /* 去除聚焦线 */
    outline: 0;
    background: #f1f1f1 url(../images/企业站1_03.png) no-repeat 203px center;
    float: right;
    margin-top: 39px;
    /* 首行缩进 */
    text-indent: 14px;
}

/* --------------第二部分  导航栏--- */
/* 外围只需要设置背景颜色 */
#navWrapper {
    background: #2f2f2f;
}

#nav {
    height: 58px;
    /* 超链接就一行文字  需要垂直居中 单行文本垂直居中 */
    line-height: 58px;
}

#nav a {
    /* 去除超链接下划线 */
    text-decoration: none;
    /* 文字大小 */
    font-size: 12px;
    /* 文字颜色 */
    color: #fff;
    /* 设置右边框 */
    border-right: 1px solid #494949;
    /* 设置内填充 padding是文字和边框之间的距离 */
    padding: 0 32px;
    /* 人家的边框  和父元素高度一致  什么情况下  超链接也可以设置高度呢-----浮动时 */
    float: left;
    /* 超链接设置浮动 但是没写高度  那么超链接的高度  就是行高   行高你设置的58 */
}

.noborder {
    /* 去除边框 */
    border: 0 !important;
}

#nav a:hover {
    background-color: skyblue;
}

/* -------大图部分---- */
/* #banner的高度直接由子元素图片撑开 */
/* 图片下边自带3px  我们需要解决图片3px问题 */
#banner img {
    vertical-align: top;
}

/* -------------第四部分----- */
#content {
    height: 240px;
}

#content h2 {
    /* 注意！！这样子代表选中了第四部分的3个h2  */
    color: #40444f;/* 文字颜色 */
    font-size: 18px;/* 文字大小 */
    font-weight: normal;/* 取消加粗 */
    /* 距离上方35px */
    margin-top: 35px;
    /* 距离下方22 */
    margin-bottom: 22px;
}

/* 公司新闻 */
.xinwen {
    width: 480px;
    height: 240px;
    /* 我需要这三块横向展现 浮动 */
    float: left;
}

.xinwen ul {
    /* 小圆圈在li内侧 */
    list-style-position: inside;
    color: #515151;/* 文字颜色 */
    font-size: 12px;/* 文字大小 */
    /* 行高 */
    line-height: 24px;
}

.xinwen li span {
    /* 靠右----右浮 */
    float: right;
    color: #949494;
    margin-right: 28px;
}

/* 公司介绍 */
.jieshao {
    width: 240px;
    height: 240px;
    background: #f1f1f1;
    /* 我需要这三块横向展现 浮动 */
    float: left;
    /* 设置内填充   会将文字内容往里面挤一挤 */
    padding-left: 20px;
    padding-right: 22px;
    /* 因为会撑大盒子  你如果还希望盒子宽度240  做减法 */
    width: 198px;
}

.word {
    color: #555555;
    font-size: 12px;
    line-height: 25px;
    margin-left: 5px;
    /* 距离左边有间距 */
}

.p1 {
    padding-top: 11px;
}

.p3 {
    color: #919191;/* 文字颜色 */
    font-size: 12px;/* 文字大小 */
    line-height: 24px;/* 行高 */
    margin-left: 5px;
    margin-top: 15px;
}

/* 人才招聘 */
.zhaopin {
    width: 242px;
    height: 240px;
    background: #fbfbfb url(../images/2.png) no-repeat right bottom;
    /* 我需要这三块横向展现 浮动 */
    float: left;
    /* 设置内填充   会将文字内容往里面挤一挤 */
    padding-left: 25px;
    padding-right: 37px;
    /* 因为会撑大盒子  你如果还希望盒子宽度240  做减法 */
    width: 180px;
}

.zhaopin p {
    font-size: 12px;
    color: #5a5a5a;
    line-height: 24px;
}

.more {
    width: 66px;
    height: 19px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12px;
    color: #FFF;
    background: #adadad;
    /* 文本水平居中 */
    text-align: center;
    /* 单行文本垂直居中 */
    line-height: 19px;
    /* 小写英文变缩小版大写英文 */
    font-variant: small-caps;
    /* 设置圆角 */
    border-radius: 5px;
    /* 距离上方间距 */
    margin-top: 22px;
}

/* ------------市场项目-------- */
#market {
    height: 305px;
    /* 因为ni子元素h2设置margin-top 导致我父元素跟随下移了  解决一下 */
    overflow: hidden;
}

#market h2 {
    /* 注意！！这样子代表选中了第四部分的3个h2  */
    color: #3f4650;/* 文字颜色 */
    font-size: 18px;/* 文字大小 */
    font-weight: normal;/* 取消加粗 */
    /* 距离上方29px */
    margin-top: 29px;
    /* 距离下方18 */
    margin-bottom: 18px;
}

/* 设置宽度   */
.marketList {
    width: 210px;
    /* 四个marketList 横向展现  浮动 */
    float: left;
    /* 距离右侧有40px */
    margin-right: 40px;
}

/* 第四个距离右侧没有间距 */
.marketList4 {
    margin-right: 0;
}

.marketList p {
    font-size: 12px;
    color: #454545;
    line-height: 24px;
    margin-top: 13px;
}

/* --------------第六部分----------- */
#productWrapper {
    /* 外围只需要设置背景颜色 */
    background: #e5e5e5;
}

#product {
    height: 250px;
}

#product h3 {
    /* 代表选中了第六部分这三个h3   */
    color: #5e5e5e;/* 文字颜色 */
    font-size: 16px;/* 文字大小 */
    font-weight: normal;/* 取消加粗 */
    margin-top: 31px;/* 距离上方31 */
    /* 设置下边框 */
    border-bottom: 1px solid #c1c1c1;
    /* 文字和边框之间的距离  padding  */
    padding-bottom: 11px;
    /* 首行缩进 */
    text-indent: 12px;
    /* 距离下方的其他元素 有15px的间距  使用margin */
    margin-bottom: 15px;
}

/* 产品中心 */
.chanpin {
    width: 452px;
    height: 250px;
    /* 我希望这三块横向展现 --左浮动 */
    float: left;
}

#product ul {
    /* 去除列表样式 */
    list-style: none;
    /* 这几个ul我想横向展现----浮动 */
    float: left;
    font-size: 12px;
    color: #646464;
    line-height: 24px;
}

#product ul span {
    margin-left: 5px;
    margin-right: 9px;
}

.ul2 {
    margin-left: 73px;
    margin-right: 66px;
}

/* 技术研发 */
.jishu {
    width: 154px;
    height: 250px;
    /* 我希望这三块横向展现 --左浮动 */
    float: left;
    /* 中间这个块  距离左右有间距 */
    margin-left: 48px;
    margin-right: 50px;
}

/* 营销网络 */
.wangluo {
    width: 256px;
    height: 250px;
    /* 我希望这三块横向展现 --左浮动 */
    float: left;
}

.wangluo img {
    margin-left: 33px;
}

/* ---------------尾部---- */
#footer {
    height: 58px;
    padding-top: 24px;
    font-size: 12px;
    color: #848484;
}

#footer p {
    float: right;
}

#footer a {
    text-decoration: none;
    color: #848484;/* 参考day6-CSS特性、元素   超链接不继承颜色属性 */
    padding: 0 7px;
    border-right: 1px solid #808080;
}

#footer .nopaddingLeft {
    padding-left: 0;
}

#footer img {
    /* 图片中心和其他元素对齐 */
    vertical-align: middle;
}
```
[1.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056307-39a43601-8da4-4875-8d2b-0e2df6b48763.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056307-39a43601-8da4-4875-8d2b-0e2df6b48763.png%22%2C%22name%22%3A%221.png%22%2C%22size%22%3A10198%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u5a9fec10-568a-4f8d-82b5-91475688ca9%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u8718a4ed%22%2C%22card%22%3A%22file%22%7D)[2.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056319-af51bdaa-8e61-440b-9a61-dee1fdc58b6b.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056319-af51bdaa-8e61-440b-9a61-dee1fdc58b6b.png%22%2C%22name%22%3A%222.png%22%2C%22size%22%3A1525%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22uc056c0be-cbd1-4ac7-a1ae-18efbae6564%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ue19c3997%22%2C%22card%22%3A%22file%22%7D)[3.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749056502-a50a8890-8607-4568-9a44-87825656925d.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749056502-a50a8890-8607-4568-9a44-87825656925d.jpeg%22%2C%22name%22%3A%223.jpg%22%2C%22size%22%3A154988%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8a79f0d7-3d64-45a9-8997-a59a19dc16e%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u9a55b31e%22%2C%22card%22%3A%22file%22%7D)[4.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056319-f18ca13c-1fae-433b-95c8-37697bcca164.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056319-f18ca13c-1fae-433b-95c8-37697bcca164.png%22%2C%22name%22%3A%224.png%22%2C%22size%22%3A27103%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u1e729140-5a6a-47f7-bc85-1bbd8033a16%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u9ce5ec75%22%2C%22card%22%3A%22file%22%7D)[5.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056319-c66c7eae-7323-4c50-a7c9-53e7563810a9.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056319-c66c7eae-7323-4c50-a7c9-53e7563810a9.png%22%2C%22name%22%3A%225.png%22%2C%22size%22%3A17614%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ubd34cb7b-4793-470d-b535-254cc36f284%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u7f42bd10%22%2C%22card%22%3A%22file%22%7D)[6.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056575-3d69ef35-ba86-4494-a13c-c22833387d46.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056575-3d69ef35-ba86-4494-a13c-c22833387d46.png%22%2C%22name%22%3A%226.png%22%2C%22size%22%3A24943%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u710d9ab5-86e6-4632-8028-548ae755a48%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u677c177e%22%2C%22card%22%3A%22file%22%7D)[7.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056642-1e1039b6-1493-425f-9fa7-17d12ca5245a.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056642-1e1039b6-1493-425f-9fa7-17d12ca5245a.png%22%2C%22name%22%3A%227.png%22%2C%22size%22%3A22040%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u23800a68-3b52-4f06-a879-0a1dadaa20e%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u340bed95%22%2C%22card%22%3A%22file%22%7D)[8.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056641-7528b5fe-485c-4b51-b96b-ee0eae5826cb.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056641-7528b5fe-485c-4b51-b96b-ee0eae5826cb.png%22%2C%22name%22%3A%228.png%22%2C%22size%22%3A19860%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u33ecfc4e-b753-4853-acb4-9087879f587%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uf3343374%22%2C%22card%22%3A%22file%22%7D)[9.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749056654-cc48534a-72a4-44fb-a3d7-4b35012d32e7.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749056654-cc48534a-72a4-44fb-a3d7-4b35012d32e7.png%22%2C%22name%22%3A%229.png%22%2C%22size%22%3A16884%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u930744f5-e0d4-4a2f-8048-17d995272ef%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ua783b45e%22%2C%22card%22%3A%22file%22%7D)[11.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749056994-728bbe55-08b9-41a9-95ff-ee4e25b84647.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749056994-728bbe55-08b9-41a9-95ff-ee4e25b84647.jpeg%22%2C%22name%22%3A%2211.jpg%22%2C%22size%22%3A1490%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22uf4cb57fd-76f6-4a50-8b05-37a289510ec%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u2a1aac89%22%2C%22card%22%3A%22file%22%7D)[22.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749057021-2c0a9fec-df4b-41e5-8afe-844ced0cb6f5.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749057021-2c0a9fec-df4b-41e5-8afe-844ced0cb6f5.jpeg%22%2C%22name%22%3A%2222.jpg%22%2C%22size%22%3A1385%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u32a681bd-7413-4481-823f-f631f4cdac0%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u92d8e083%22%2C%22card%22%3A%22file%22%7D)[33.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749057056-ec14a195-61ee-4c97-afa3-a39842d715a5.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749057056-ec14a195-61ee-4c97-afa3-a39842d715a5.jpeg%22%2C%22name%22%3A%2233.jpg%22%2C%22size%22%3A1414%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8a3d4ea5-e63a-42b1-b349-aa37b2b1361%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u5d8672f9%22%2C%22card%22%3A%22file%22%7D)[44.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749057132-844981c1-5c86-47b3-bc23-4557f7a0944b.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749057132-844981c1-5c86-47b3-bc23-4557f7a0944b.jpeg%22%2C%22name%22%3A%2244.jpg%22%2C%22size%22%3A1421%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u42413f67-27f6-4ac1-8858-845705893d2%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u133477b9%22%2C%22card%22%3A%22file%22%7D)[55.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749057375-922a1f96-d39a-42ca-81e2-47aa43f3af10.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749057375-922a1f96-d39a-42ca-81e2-47aa43f3af10.jpeg%22%2C%22name%22%3A%2255.jpg%22%2C%22size%22%3A1423%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u97a9c09c-e213-4051-aa61-472ed3832b5%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u0b6ccff1%22%2C%22card%22%3A%22file%22%7D)[企业站.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749057991-1de787bb-b428-4f2e-bc7b-5f5fd0f865aa.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749057991-1de787bb-b428-4f2e-bc7b-5f5fd0f865aa.jpeg%22%2C%22name%22%3A%22%E4%BC%81%E4%B8%9A%E7%AB%99.jpg%22%2C%22size%22%3A519142%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u27d7b04a-9197-4142-81cb-21b8f21b007%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u8ba8175b%22%2C%22card%22%3A%22file%22%7D)
<a name="QgYxM"></a>
# 小米页面
<a name="sxZto"></a>
## html部分代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>小米</title>
    <link rel="stylesheet" href="../作业/css/xioami.css">
</head>

<body>
    <div id="mainWrapper"><!-- 外围 -->
        <div id="main"><!-- 版心 -->
            <!-- 第一部分 -->
            <div class="son son1">
                <img src="../作业/images/1.jpg" alt="">
            </div>
            <!-- 第二部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/2.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第三部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/3.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第四部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/4.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第五部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/5.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第六部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/6.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第七部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/7.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第八部分 -->
            <div class="son son2">
                <div class="photo"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/8.jpg" alt="">
                </div>
                <dl>
                    <dt>小米电视6 65” OLED</dt>
                    <dd>小米电视6 65″OLED</dd>
                    <span>6999元</span>
                </dl>
            </div>
            <!-- 第九部分 -->
            <div class="son son3">
                <div class="photos"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/9.jpg" alt="">
                </div>
                <p class="xiaomi">小米电烤箱</p>
                <span class="aa">329元</span>
            </div>
            <!-- 第十部分 -->
            <div class="son son3 son4">
                <div class="photoss"><!-- 它的存在 就是让图片在这个div里面 垂直水平居中 -->
                    <img src="../作业/images/10.jpg" alt="">
                </div>
                <p class="gengduo">更多浏览</p>
                <span class="bb">热门</span>
            </div>
        </div>
    </div>
</body>

</html>
```
<a name="vi2Mg"></a>
## CSS部分代码
```css
* {
    margin: 0;
    padding: 0;
}

/* 外围 */
#mainWrapper {
    background: #f5f5f5;
}

/* 版心 */
#main {
    width: 1240px;/* 我的高度宽度或者margin-left肯定是有点什么问题 */
    height: 634px;
    /* background: tomato; */
    margin: 0 auto;
}

/* 每一块左浮动 */
.son {
    width: 236px;
    float: left;
    /* border: 1px solid #f40; */
}

/* 第一部分统一 */
.son1 {
    height: 614px;
    /* background: pink; */
}

/* 第二部分统一 */
.son2 {
    height: 300px;
    background: #ffffff;
    margin-bottom: 14px;
    margin-left: 13px;
    text-align: center;
}

/* 第二部分细节 */
.photo {
    text-align: center;
    line-height: 200px;
    /* background: chartreuse; */
}

.son2 img {
    vertical-align: middle;/* 让图片中线在div垂直居中，参考day6-CSS特性、元素 */
}

dl {
    font-size: 12px;
    color: #333333;
}

dd {
    color: #b0b0b0;
    margin-top: 10px;
    margin-bottom: 18px;
}

span {
    color: #ff7e00;
}

/* 第三部分 */
/* 最后两小块 */
.son3 {
    height: 143px;
    background: #ffffff;
    margin-left: 13px;
    margin-bottom: 14px;
}

/* .son4{
    margin-top: 14px;
} */
/* 第九、十块图片设置 */
.photos {
    float: right;
    margin-top: 52px;
    margin-right: 27px;
}

.photoss {
    float: right;
    margin-top: 48px;
    margin-right: 35px;
}

.xiaomi {
    font-size: 12px;
    color: #333333;
    margin-top: 45px;
    margin-left: 30px;
}

.aa {
    font-size: 12px;
    margin-top: 16px;
    margin-left: 31px;
    color: #ff6700;
}

.gengduo {
    font-size: 17px;
    color: #333333;
    margin-top: 55px;
    margin-left: 31px;
}

.bb {
    font-size: 12px;
    margin-top: 10px;
    margin-left: 31px;
    color: #757575;
}
```
[1.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148595-2dfa93a7-77b0-4053-ba62-ab19695c8059.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148595-2dfa93a7-77b0-4053-ba62-ab19695c8059.jpeg%22%2C%22name%22%3A%221.jpg%22%2C%22size%22%3A44429%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ue5f17f62-46e7-4b4b-9fdb-0574b9a7d4e%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u6f976d32%22%2C%22card%22%3A%22file%22%7D)[2.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148602-1b021fd8-2c73-42c9-8a4a-195985641102.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148602-1b021fd8-2c73-42c9-8a4a-195985641102.jpeg%22%2C%22name%22%3A%222.jpg%22%2C%22size%22%3A5542%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ueea22419-30eb-4231-a625-199d630bd1f%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uc6d80769%22%2C%22card%22%3A%22file%22%7D)[3.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148606-84dbb6a9-f5db-421b-889a-e3cd3dfd35e5.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148606-84dbb6a9-f5db-421b-889a-e3cd3dfd35e5.jpeg%22%2C%22name%22%3A%223.jpg%22%2C%22size%22%3A4276%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u1e643ba4-6dc8-4c18-b1ca-8d433def8af%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ubc1b5787%22%2C%22card%22%3A%22file%22%7D)[4.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148606-3791275c-376b-45ab-b1c3-f59d365aa92e.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148606-3791275c-376b-45ab-b1c3-f59d365aa92e.jpeg%22%2C%22name%22%3A%224.jpg%22%2C%22size%22%3A7010%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u10fe887c-7993-4b80-800d-1b561c43997%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u3708deb8%22%2C%22card%22%3A%22file%22%7D)[5.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148606-a3c0da00-4ccb-4bf2-9f8b-55b801026c9f.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148606-a3c0da00-4ccb-4bf2-9f8b-55b801026c9f.jpeg%22%2C%22name%22%3A%225.jpg%22%2C%22size%22%3A2255%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u26cd91a2-4a9d-48c2-ac65-b5e847a066c%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ue28e49ec%22%2C%22card%22%3A%22file%22%7D)[6.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148850-bb0f37ec-316d-4c05-aa48-01e0ce739316.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148850-bb0f37ec-316d-4c05-aa48-01e0ce739316.jpeg%22%2C%22name%22%3A%226.jpg%22%2C%22size%22%3A2865%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u1b4c9125-ddf0-4858-8ad7-b4fe7e4af93%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u9db398f0%22%2C%22card%22%3A%22file%22%7D)[7.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148894-8931f467-2e60-4b84-a133-6f87934f9b85.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148894-8931f467-2e60-4b84-a133-6f87934f9b85.jpeg%22%2C%22name%22%3A%227.jpg%22%2C%22size%22%3A3120%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22ue931425d-3fd3-416c-9aed-efbc41614fa%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22uf5da3ed9%22%2C%22card%22%3A%22file%22%7D)[8.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148895-e0774f7f-ba71-4e6d-9eb4-d0343a4beacd.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148895-e0774f7f-ba71-4e6d-9eb4-d0343a4beacd.jpeg%22%2C%22name%22%3A%228.jpg%22%2C%22size%22%3A2414%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u0d65cfbe-310f-47da-8d61-d9bac160b48%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u0eff15fa%22%2C%22card%22%3A%22file%22%7D)[9.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148903-4fbcb5ca-0d49-44f5-905e-887ce23b8fc6.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148903-4fbcb5ca-0d49-44f5-905e-887ce23b8fc6.jpeg%22%2C%22name%22%3A%229.jpg%22%2C%22size%22%3A1901%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8779eb25-e76b-4657-864e-b50eeee0e56%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u41c8c58a%22%2C%22card%22%3A%22file%22%7D)[10.jpg](https://www.yuque.com/attachments/yuque/0/2022/jpeg/25380982/1641749148943-0c9b58c3-26f8-42c6-abeb-50309458f58d.jpeg?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fjpeg%2F25380982%2F1641749148943-0c9b58c3-26f8-42c6-abeb-50309458f58d.jpeg%22%2C%22name%22%3A%2210.jpg%22%2C%22size%22%3A3205%2C%22type%22%3A%22image%2Fjpeg%22%2C%22ext%22%3A%22jpeg%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u54fe28c0-789c-4a6d-9514-22397231402%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u2bea4af1%22%2C%22card%22%3A%22file%22%7D)[小米作业.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641749149442-fdadeb4e-f49c-4c39-acaf-937454b3fa56.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641749149442-fdadeb4e-f49c-4c39-acaf-937454b3fa56.png%22%2C%22name%22%3A%22%E5%B0%8F%E7%B1%B3%E4%BD%9C%E4%B8%9A.png%22%2C%22size%22%3A285353%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8a109784-09d3-4550-8923-60782c0e6b6%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u1b826162%22%2C%22card%22%3A%22file%22%7D)
