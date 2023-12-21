<a name="beVMf"></a>
# HTML5 新增语义化标签
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649771428934-1644cff3-2ead-45a4-8120-4085e9d9aeb2.png#clientId=u03dc686d-e455-4&from=paste&height=433&id=ua4e20a71&originHeight=541&originWidth=907&originalType=binary&ratio=1&rotation=0&showTitle=false&size=318709&status=done&style=stroke&taskId=u9d0cd47f-ceb8-4fb6-a1b2-687921d4e9c&title=&width=725.6)
<a name="C2IeT"></a>
## <section> 类似div、li

- 表示页面中的一个**内容**区块
<a name="DJZZC"></a>
## <article> 类似p标签

- 表示一块与上下文无关的**独立**的内容
<a name="k1Stu"></a>
## <aside> 侧边栏

- 在`article`之外的，与`article`内容相关的**辅助**信息
<a name="jVGaF"></a>
## <header> 头部

1. 表示页面中的一个内容区块或者整个页面的标题
2. 等同于`<div id="header"></div>`
3. 权重为`1`（因为是语义化标签，而标签的权重为1）
<a name="NPR2X"></a>
## <footer> 脚注

- 表示页面中一个内容区块或者整个页面的**脚注**
<a name="MDJ8N"></a>
## <nav> 导航栏

- 表示页面中导航链接部分
```html
<nav><!-- 导航栏 -->
    <section>类似div和li</section>
    <section>用来表示一个小块</section>
    <section>首页</section><!-- 首页就是用<section>来表示的 -->
    <section>首页</section>
    <section>块状元素</section>
    <section>首页</section>
</nav>
```
<a name="UpWvp"></a>
## <figure> 类似di>dt+dd

- 表示一段独立的流内容，使用`figcaption`元素为其添加标题（第一个或者最后一个子元素的位置）
- 注意！图片很特殊，当你设置宽度百分百，代表宽度和父元素的宽度一致，那么他的高度，会等比例进行缩放
```html
<figure>
    <img src="../images/1.jpg" alt="">
    <figcaption>类似dl>dt+dd的存在</figcaption>
</figure>
```
<a name="a3Z2P"></a>
## <main> 主体

1. 表示页面中的主要内容
2. `IE`不兼容，也就是说IE低版本不识别
3. 移动端常用
<a name="L3uR6"></a>
## 兼容版本浏览器

- `<script src="html5.js"></script>`
<a name="h0Iru"></a>
# 完整代码
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
            width: 100%;
            height: 100px;
            background: cyan;
        }

        nav {
            width: 100%;
            height: 80px;
            background: springgreen;
        }

        section {
            float: left;
            padding: 0 30px;
            line-height: 80px;
            border-right: 1px solid #FFF;
        }

        main {
            width: 100%;
            height: 900px;
            background: tomato;
        }

        figure {
            width: 300px;
            height: 400px;
            float: left;
            margin: 10px 40px;
        }

        figure img {
            width: 100%;
            /* 注意图片很特殊  当你设置宽度百分百  代表宽度和父元素的宽度一致  那么他的高度  会等比例进行缩放 */
        }

        footer {
            width: 100%;
            height: 400px;
            background: violet;
        }

        aside {
            width: 100px;
            height: 400px;
            background: pink;
            position: fixed;
            /* 固定定位 */
            right: 0;
            top: 40%;
        }
    </style>
</head>

<body>
    <!-- <div id="header"></div>等同于<header>头部</header> -->
    <!-- HTML5   语义化 标签   -->
    <header>头部</header><!-- 权重 1  因为是标签 标签的权重为1 -->
    <nav>
        <!-- 导航栏 -->
        <section>类似div和li</section>
        <section>用来表示一个小块</section>
        <section>首页</section><!-- 首页就是用<section>来表示的 -->
        <section>首页</section>
        <section>块状元素</section>
        <section>首页</section>
    </nav>
    <main>
        <!-- 主体 注意IE低版本不识别 我们移动端常用 -->
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
        <figure>
            <img src="../images/1.jpg" alt="">
            <figcaption>类似dl>dt+dd的存在</figcaption>
        </figure>
    </main>
    <footer>
        <!-- 尾部 -->
        <article>其实就是p标签的集合 它代表的是一大块文字/文章</article>
        <hgroup>是标题标签的集合 代表标题 但是人家不会加粗</hgroup>
    </footer>

    <aside>侧边栏</aside>
    <dialog>你是看不见的</dialog>
    <time>表示时间 行内元素</time>
    <mark>变红</mark><!-- 蒙层  是行内元素  默认黄色背景色 -->
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649768910095-be466683-05a2-4179-80dc-aa88addc0750.gif#clientId=u03dc686d-e455-4&from=drop&id=u50a2a65a&originHeight=854&originWidth=1909&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4203512&status=done&style=stroke&taskId=ue313f326-ad24-46cb-aabc-6e876a21719&title=)
<a name="qLn78"></a>
## 汇总
```html
<header></header>		表示页面的头部
<nav></nav>				  表示页面的导航栏区域
<main></main>		 		表示页面的主体内容区域  注意！IE低版本不识别 那你在PC端慎重使用
<footer></footer>		表示页面的尾部
<section></section>	表示区域块  类似div和li的结合体（比div小比li大） 是块状元素
<figure>						表示一个独立的区域  有点类似dl>dt+dd组合
    <figcatipon></figcatipon>注意！要么在figure里面第一位 要么在figure里面最后一位
</figure>
<article></article> 代表<p>的集合  类似表示一大块  多用于表示很多文字
<aside></aside>			侧边栏  一般用于表示页面的某一侧边  也可以作为页面左右侧固定定位区域
<hgroup></hgroup>		代表 标题标签的集合  注意！不会加粗
<dialog></dialog>		代表页面弹出的对话框  默认元素消失  并且自己是绝对定位
<time></time>				表示时间  行内元素
<mark></mark>				蒙层  是行内元素  默认黄色背景色
```
<a name="PjHaK"></a>
# 音/视频的引入 <audio/video> <source src=""  type="">

1. 我们知道，图片的形式有 `.jpg` / `.png` / `.gif` ，同样，音/视频文件的格式也是有很多种类的
2. 拿音频文件来说，它具有很多种格式
- 比如有的浏览器只能识别 `.mp3` / `.ogg` / `.webm` 中的一种格式
3. 我们不可以规定用户使用哪一个浏览器，但我们需要让用户在各个浏览器下都可以正常的听音乐，所以我们需要去**兼容**各个格式，有一个标签叫 `<source>`
```html
<audio controls autoplay loop muted>
    <source src="./video/3theA.mp4" type="audio/mpeg"><!-- 先识别第一个音乐  不能播放再往下识别  和字体规则一样（海王） -->
    <source src="./video/a.mp3" type="audio/mpeg"><!-- type属性可以省略不写 -->
    <source src="./video/movie.ogg" type="audio/ogg">
    <source src="./video/movie.webm" type="audio/webm">
</audio>
```
| 属性 | 作用 |
| --- | --- |
| `controls` | 控制条显示 |
| `autoplay` | 自动播放 |
| `loop` | 循环播放 |
| `muted` | 默认静音 |
| `poster` | 视频中用作加载时出现 |

- `loop="2"` 播放两次

![控制条](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649920856355-d7e5ed68-af43-46fe-9ac0-a56a3e51f37a.png#clientId=ud48cd5e8-61ad-4&from=paste&height=58&id=Ie4y8&originHeight=73&originWidth=320&originalType=binary&ratio=1&rotation=0&showTitle=true&size=23779&status=done&style=stroke&taskId=u9876605a-bebd-4e9e-a195-f512d4cbccd&title=%E6%8E%A7%E5%88%B6%E6%9D%A1&width=256 "控制条")<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642037451019-5f0c8efa-058f-453c-bcbf-4f914ddf6b39.png#clientId=ucf1d1a8d-91f4-4&from=paste&height=366&id=Ddqyl&originHeight=394&originWidth=716&originalType=binary&ratio=1&rotation=0&showTitle=false&size=119570&status=done&style=stroke&taskId=u6cdc9998-ab6f-4503-a619-66dd1beefef&title=&width=665.6000366210938)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>音/视频的引入</title>
</head>

<body>
    <!-- 音频的引入 -->
    <audio controls autoplay loop muted>
        <source src="./video/3theA.mp4" type="audio/mpeg"><!-- 先识别第一个音乐  不能播放再往下识别  和字体规则一样-海王 -->
        <source src="./video/a.mp3" type="audio/mpeg"><!-- type属性可以省略不写 -->
        <source src="./video/movie.ogg" type="audio/ogg">
        <source src="./video/movie.webm" type="audio/webm">
    </audio>
    
    <!-- 视频的引入 -->
    <video controls loop autoplay muted poster="../banner.png">
        <source src="./video/movie.mp4" type="video/mp4">
        <source src="./video/movie.ogg" type="video/ogg">
        <source src="./video/movie.webm" type="video/webm">
    </video>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642038359174-459c6b59-d542-4921-9f93-e5185c43e291.png#clientId=ucf1d1a8d-91f4-4&from=paste&height=209&id=u340d5fbe&originHeight=418&originWidth=800&originalType=binary&ratio=1&rotation=0&showTitle=false&size=141924&status=done&style=stroke&taskId=ube9da4c1-4913-4369-994e-bd8c5907f37&title=&width=400)
<a name="KalaD"></a>
# HTML5 表单新增
```html
<form action="后台接口（世纪佳缘数据库地址）" method="传送数据的方式" name="表单名字" id="">
    <!-- 1、数字框  仅能输入数字 -->
    <input type="number">
    <!-- min最小值  max最大值  step间隔步幅 -->
    <input type="number" min="50" max="60" step="2">
    <!-- 2、 搜索框-->
    <input type="search">
    <!-- 3、颜色框  用作取色 -->
    <input type="color">
    <!-- 4、范围框 -->
    <input type="range">
    <!-- step间隔步幅 -->
    <input type="range" step="10">
    <!-- 5、网址框 -->
    <input type="url">
    <!-- 可以输入多个网址  逗号隔开  multiple="2"代表可以写两个   multiple代表无数个 -->
    <input type="url" multiple="2">
    <!-- 6、邮件框 -->
    <input type="email">
    <!-- 也可以写多个  英文逗号隔开就可 -->
    <input type="email" multiple>
    <!-- 我们还有一个属性  叫正则表达式pattern -->
    <!-- pattern="[a-z]{6}" 代表可以输入6位小写英文字母 -->
    <input type="text" pattern="[a-z]{6}">
    <!-- 7、电话框 -->
    <input type="tel">
    <!-- 8、日期 -->
    <!-- 年月 -->
    <input type="month">
    <!-- 年周 -->
    <input type="week">
    <!-- 年月日 -->
    <input type="date">
    <!-- 时分 -->
    <input type="time">
    <!-- 年月日时分 -->
    <input type="datetime-local">
    <input type="submit">
</form>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642068021165-6708d7cc-8625-430c-8fda-5a0f0f7051ef.png#clientId=u9c2068b6-6ee5-4&from=paste&height=98&id=udd15e709&originHeight=138&originWidth=937&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6407&status=done&style=stroke&taskId=ufdfd590a-b611-4032-a3f4-9f435a3589e&title=&width=667.5)
<a name="kWzxM"></a>
# HTML5 表单新增属性
```html
<form action="" novalidate>
    <!-- 1、虚焦提示信息 -->
    <input type="text" placeholder="请输入">
    <!-- 2、最大值max    -->
    <!-- 3、最小值min -->
    <!-- 4、间隔步幅step -->
    <input type="number" max="20" min="1" step="2">
    <!-- 5、可以写多个网址/邮箱 multiple-->
    <input type="url" multiple>
    <!-- 6、正则表达式 pattern-->
    <input type="text" pattern="[a-z]{8}">
    <!-- 7、自动聚焦 -->
    <input type="text" autofocus>
    <!-- 8、只读 readonly  你只能看 不能改变 -->
    <input type="text" value="123" readonly>
    <!-- 9、必填项 -->
    <input type="text" required>
    <!-- 10、默认选中 checked    -->
    <!-- 11、禁止使用 disabled  -->
    <!-- 12、除了禁止使用的  剩下的都是可使用的  enabled -->
    <!-- 13、取消验证 novalidate 给form标签加  那么form里面的所有验证条件全部失效 -->
    <!-- 14、数据列表 list="你给<datalist>标签起的id值"-->
    <!-- 15、历史记录 自动补全 针对datalist -->
    <input type="text" list="demo" autocomplete="on">
    <datalist id="demo">
        <option value="最辣的" label="火锅"></option>
        <option value="最甜的" label="提拉米苏"></option>
        <option value="最苦的" label="苦瓜"></option>
        <option value="最臭的" label="螺蛳粉"></option>
        <option value="最咸的" label="狗宝咸菜"></option>
    </datalist>
    <input type="submit">
</form>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642068309889-d1b41b4f-4ba2-4098-bd45-a385053b33e8.png#clientId=u9c2068b6-6ee5-4&from=paste&height=319&id=ufa72bdbe&originHeight=458&originWidth=938&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15668&status=done&style=stroke&taskId=u0bb01c70-f91c-474a-8701-eecf0813f45&title=&width=653)
