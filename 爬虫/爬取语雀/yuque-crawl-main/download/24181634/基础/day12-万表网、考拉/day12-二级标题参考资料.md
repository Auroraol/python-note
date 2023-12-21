<a name="DYI8i"></a>
# 二级示例
[css导航栏二级菜单写法_恬静的男子的博客-CSDN博客_导航栏二级菜单](https://blog.csdn.net/a732894380/article/details/84033428)<br />![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650636183168-b1cc617d-98c2-4ab6-b09f-32a25904160f.gif#clientId=u3c85c17a-a31a-4&from=paste&height=241&id=uf9a13260&originHeight=301&originWidth=768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61185&status=done&style=stroke&taskId=ub183ef0d-609c-416b-a67f-c2be82b3332&title=&width=614.4)
```html
<html>

<head>
    <title>二级菜单测试</title>
    <meta charset="utf-8">
    <style type="text/css">
        /*为了使菜单居中*/
        body {
            padding-top: 100px;
            text-align: center;
        }


        /* -------------菜单css代码----------begin---------- */
        .menuDiv {
            border: 2px solid #aac;
            /* overflow: hidden; */
            display: inline-block;
        }

        /* 去掉a标签的下划线 */
        .menuDiv a {
            text-decoration: none;
        }

        /* 设置ul和li的样式 */
        .menuDiv ul,
        .menuDiv li {
            list-style: none;
            margin: 0;
            padding: 0;
            float: left;
        }

        /* 设置二级菜单绝对定位，并隐藏 */
        .menuDiv>ul>li>ul {
            position: absolute;
            display: none;
        }

        /* 设置二级菜单的li的样式 */
        .menuDiv>ul>li>ul>li {
            clear: both;
        }

        /* 鼠标放在一级菜单上，显示二级菜单 */
        .menuDiv>ul>li:hover ul {
            display: block;
        }

        /* 一级菜单 */
        .menuDiv>ul>li>a {
            width: 120px;
            line-height: 40px;
            color: black;
            background-color: #cfe;
            text-align: center;
            border-left: 1px solid #bbf;
            display: block;
        }

        /* 在一级菜单中，第一个不设置左边框 */
        .menuDiv>ul>li:first-child>a {
            border-left: none;
        }

        /* 在一级菜单中，鼠标放上去的样式 */
        .menuDiv>ul>li>a:hover {
            color: #f0f;
            background-color: #bcf;
        }

        /* 二级菜单 */
        .menuDiv>ul>li>ul>li>a {
            width: 120px;
            line-height: 36px;
            color: #456;
            background-color: #eff;
            text-align: center;
            border: 1px solid #ccc;
            border-top: none;
            display: block;
        }

        /* 在二级菜单中，第一个设置顶边框 */
        .menuDiv>ul>li>ul>li:first-child>a {
            border-top: 1px solid #ccc;
        }

        /* 在二级菜单中，鼠标放上去的样式 */
        .menuDiv>ul>li>ul>li>a:hover {
            color: #a4f;
            background-color: #cdf;
        }

        /* -------------菜单css代码----------end---------- */
    </style>
</head>

<body>

    <!-- -------菜单html代码---------begin------- -->
    <div class="menuDiv">
        <ul>
            <li>
                <a href="#">菜单一</a>
                <ul>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                </ul>
            </li>
            <li>
                <a href="#">菜单二</a>
                <ul>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                </ul>
            </li>
            <li>
                <a href="#">菜单三</a>
                <ul>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                </ul>
            </li>
            <li>
                <a href="#">菜单四</a>
            </li>
            <li>
                <a href="#">菜单五</a>
                <ul>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                    <li><a href="#">二级菜单</a></li>
                </ul>
            </li>
        </ul>
    </div>
    <!-- -------菜单html代码---------end------- -->

</body>

</html>
```
<a name="SDGUw"></a>
# 京东二级内容区
```html
<!DOCTYPE html>
<html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>二级里面的内容</title>
    <style>
      /* 去除页面缝隙 */
      * {
        margin: 0;
        padding: 0;
      }
      
      .erji {
        width: 900px;
        height: 422px;
        /* 设置边框    边框：大小  线型  颜色 */
        border: 1px solid #f7f7f7;
        margin: 0 auto;
      }
      
      .right {
        width: 151px;
        height: 404px;
        /* 我想要他两横向展现  设置浮动 */
        float: left;
        /* 距离左侧20 */
        margin-left: 20px;
        /* 距离上方18px */
        margin-top: 18px;
      }
      
      /* 右边的图片  横向展现  那就设置浮动   因为图片默认有3px问题  设置浮动  上下左右的间隙也没有了 */
      .right img {
        float: left;
        /* 距离下方1px */
        margin-bottom: 1px;
      }
      
      .marginRight1 {
        /* 第一张  第三张  第五张图  距离右侧有1px间隙 */
        margin-right: 1px;
      }
      
      .marginTop10 {
        /* 这张图距离上方10px */
        margin-top: 10px;
      }
      
      /* 里面分左右两大部分  左边是各种文字  右边是图片 */
      .left {
        /* 设置宽度 */
        width: 715px;
        height: 422px;
        /* 我想要他两横向展现  设置浮动 */
        float: left;
      }
      
      a {
        /* 代表选中了页面中所有的超链接 */
        /* 我想去除页面中所有超链接下划线 */
        text-decoration: none;
        font-size: 12px;
      }
      
      /* 左边第一部分 */
      .erjiTitle {
        /* 距离上方18px */
        margin-top: 18px;
        /* 距离左侧18px */
        margin-left: 18px;
        /* 距离下方10px */
        margin-bottom: 10px;
        /* 请设置一个高度  因为子元素都设置浮动了  如果不想影响页面下方的布局  那么父元素就需要设置高度 */
        height: 22px;
      }
      
      .erjiTitle a {
        color: #FFF;
        /* 文字距离左边9  文字距离右边12 */
        background: #333333;
        padding-left: 9px;
        padding-right: 12px;
        /* 整体距离右侧9 */
        margin-right: 9px;
        /* 因为超连接是行内元素   在一行显示  大小由内容撑开  默认不能设置宽高  那咋办  我们设置个浮动吧  因为元素设置了浮动  就可以设置宽高 */
        float: left;
        height: 22px;
        /* 设置行高=高度值  目的是为了让里面的文字垂直居中 */
        line-height: 22px;
      }
      
      .erji dl {
        position: relative;
        line-height: 29px;
      }
      
      .erji dt {
        font-size: 12px;
        color: #333333;
        /* 设置绝对定位   那么 dt就不占据位置了 */
        /* 我想要根据我当前的这一组进行定位   什么意思？？我想要根据dl进行定位  所以  我们需要给dl设置相对定位  父相子绝 */
        position: absolute;
        right: 650px;
        top: 0;
      }
      
      .erji dd a {
        font-size: 12px;
        color: #666666;
        /* 左右各有3px间隙  我们微调了  其实不知这些  是6px  因为我们文字大小和设计图上的不一样  所以这个时候  我们把距离调整了一下*/
        /* padding-left: 3px; */
        padding-right: 3px;
      }
      
      .erji dd {
        /* 文字距离左边界91px  使用padding  微调了一下距离*/
        padding-left: 80px;
      }
      
      /* 请注意权重问题 */
      .erji .reline {
        line-height: 22px;
        /* 距离下方8px */
        margin-bottom: 8px;
      }
    </style>
  </head>
  
  <body>
    <div class="erji">
      <div class="left">
        <!-- 左边第一部分两个超链接 -->
        <div class="erjiTitle">
          <a href="">家电馆 > </a>
          <a href="">开店设备一站购 > </a>
        </div>
        <!-- 左边的种类分组 -->
        <dl>
          <dt>电视 > </dt>
          <dd>
            <a href="">全面屏电视</a>
            <a href="">教育电视</a>
            <a href="">OLED电视</a>
            <a href="">智慧屏</a>
            <a href="">4K超清电视</a>
            <a href="">55英寸</a>
            <a href="">65英寸</a>
            <a href="">电视配件</a>
          </dd>
        </dl>
        <!-- 二组 -->
        <dl>
          <dt>空调 > </dt>
          <dd>
            <a href="">新风空调</a>
            <a href="">以旧换新</a>
            <a href="">空调挂机</a>
            <a href="">空调柜机</a>
            <a href="">空调套装</a>
            <a href="">新一级能效</a>
            <a href="">挂机1.5匹</a>
            <a href="">柜机3匹</a>
            <a href="">变频空调</a>
            <a href="">中央空调</a>
            <a href="">移动空调</a>
          </dd>
        </dl>
        <!-- 三组 -->
        <dl>
          <dt>洗衣机 > </dt>
          <dd>
            <a href="">滚筒洗衣机</a>
            <a href="">洗烘一体机</a>
            <a href="">波轮洗衣机</a>
            <a href="">洗烘套装</a>
            <a href="">迷你洗衣机</a>
            <a href="">洗衣机配件</a>
            <a href="">烘干机</a>
          </dd>
        </dl>
        <!-- 四组 -->
        <dl>
          <dt>冰箱 > </dt>
          <dd>
            <a href="">多门</a>
            <a href="">对开门</a>
            <a href="">三门</a>
            <a href="">双门</a>
            <a href="">冰洗套装</a>
            <a href="">冷柜/冰吧</a>
            <a href="">酒柜</a>
            <a href="">冰箱配件</a>
          </dd>
        </dl>
        <!-- 五组 -->
        <dl class="reline">
          <dt>厨卫大电 > </dt>
          <dd>
            <a href="">油烟机</a>
            <a href="">燃气灶</a>
            <a href="">烟灶套装</a>
            <a href="">集成灶</a>
            <a href="">集成水槽</a>
            <a href="">消毒柜</a>
            <a href="">洗碗机</a>
            <a href="">电热水器</a>
            <a href="">燃气热水器</a>
            <a href="">壁挂炉</a>
            <a href="">空气能热水器</a>
            <a href="">嵌入式厨电</a>
            <a href="">太阳能热水器</a>
            <a href="">烟机灶具配件</a>
          </dd>
        </dl>
        <!-- 六组 -->
        <dl class="reline">
          <dt>厨房小电 > </dt>
          <dd>
            <a href=""> 破壁机</a>
            <a href=""> 咖啡机</a>
            <a href=""> 榨汁机</a>
            <a href=""> 电炖锅</a>
            <a href=""> 果蔬净化清洗机</a>
            <a href=""> 三明治机/早餐机</a>
            <a href=""> 电烤箱</a>
            <a href=""> 厨师机/和面机</a>
            <a href=""> 料理机</a>
            <a href=""> 电饼铛</a>
            <a href=""> 电水壶/热水瓶</a>
            <a href=""> 面包机</a>
            <a href=""> 电火锅</a>
            <a href=""> 空气炸锅</a>
            <a href=""> 养生壶</a>
            <a href=""> 电磁炉</a>
            <a href=""> 电饭煲</a>
            <a href=""> 电压力锅</a>
            <a href=""> 微波炉</a>
            <a href=""> 面条机</a>
            <a href=""> 电陶炉</a>
            <a href=""> 电烧烤炉</a>
            <a href=""> 煮蛋器</a>
            <a href=""> 电热饭</a>
            <a href=""> 盒豆浆机</a>
          </dd>
        </dl>
        <!-- 七组 -->
        <dl class="reline">
          <dt>生活电器 > </dt>
          <dd>
            <a href="">取暖器</a>
            <a href="">加湿器</a>
            <a href="">空气净化器</a>
            <a href="">净水器</a>
            <a href="">饮水机</a>
            <a href="">茶吧机</a>
            <a href="">吸尘器</a>
            <a href="">扫地机器人</a>
            <a href="">洗地机</a>
            <a href="">蒸汽/电动拖把</a>
            <a href="">除螨仪</a>
            <a href="">挂烫机/熨斗</a>
            <a href="">擦地/擦窗机器人</a>
            <a href="">干衣机</a>
            <a href="">除湿机</a>
            <a href="">电话机</a>
            <a href="">电风扇</a>
            <a href="">冷风扇</a>
            <a href="">毛球修剪器</a>
            <a href="">生活电器</a>
          </dd>
        </dl>
        <!-- 八组 -->
        <dl class="reline">
          <dt>配件 > </dt>
          <dd>
            <a href="">剃须刀</a>
            <a href="">电动牙刷</a>
            <a href="">冲牙器</a>
            <a href="">电吹风卷/直发器</a>
            <a href="">理发器</a>
            <a href="">美容仪</a>
            <a href="">剃/脱毛器</a>
            <a href="">洁面仪</a>
            <a href="">按摩器</a>
            <a href="">按摩椅</a>
            <a href="">足浴盆</a>
            <a href="">电动牙刷头</a>
          </dd>
        </dl>
        <!-- 九组 -->
        <dl class="reline">
          <dt>视听影音 > </dt>
          <dd>
            <a href="">家庭影院</a>
            <a href="">KTV音响</a>
            <a href="">迷你音响</a>
            <a href="">DVD</a>
            <a href="">功放</a>
            <a href="">回音壁</a>
            <a href="">麦克风</a>
          </dd>
        </dl>
      </div>
      <div class="right">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_03.jpg" alt="" class="marginRight1">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_05.jpg" alt="">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_09.jpg" alt="" class="marginRight1">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_10.jpg" alt="">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_13.jpg" alt="" class="marginRight1">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_14.jpg" alt="">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_18.jpg" alt="" class="marginTop10">
        <img src="./images/)S%I{NT143]Z_%ID)ZIDRY6_20.jpg" alt="">
      </div>
    </div>
  </body>
  
</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650451524253-fd866845-e18e-4c79-b724-ee907fd72853.png#clientId=u9dee61d1-9fba-4&from=paste&height=478&id=u6f9d4495&originHeight=597&originWidth=1335&originalType=binary&ratio=1&rotation=0&showTitle=false&size=236920&status=done&style=stroke&taskId=u892df274-1ff9-42f8-84a0-d66f024559b&title=&width=1068)
<a name="MBRJv"></a>
# 京东二级
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 去除页面缝隙 */
        * {
            margin: 0;
            padding: 0;
        }

        .menu {
            /* 去除列表样式  去除那个小圆点*/
            list-style: none;
            width: 173px;
            height: 416px;
            background: pink;
            font-size: 12px;
            line-height: 22px;
            /* 请注意  会撑大盒子  但是高度我还是希望是425  那么 需要做减法 */
            padding-top: 9px;
            /* 让二级根据我进行定位 */
            position: relative;
        }

        .menu a {
            /* 去除超链接下划线 */
            text-decoration: none;
            color: #333333;
        }

        .menu li {
            padding-left: 16px;
        }

        .menu li:hover {
            background: #d9d9d9;
        }

        .erji {
            width: 715px;
            height: 425px;
            background: cyan;
            /* 二级永远设置绝对定位 */
            /* 此时这个二级  应该跟谁谁定位呢？   是父元素li吗？？？  不是  我们是根据左侧整体进行定位   那么就是爷爷辈 .menu */
            position: absolute;
            left: 173px;
            top: 0;
            /* 默认情况下  二级不出现   也就是二级消失*/
            /* 元素消失 */
            display: none;
        }

        /* 什么情况下   二级出现？？？   鼠标滑到li上    li里面的二级出现 */
        li:hover .erji {
            /* 注意   空格代表是li里面的子元素或者孙子元素等  代表的是后代 */
            /* 二级出现 */
            display: block;
        }
    </style>
</head>

<body>
    <ul class="menu">
        <li>
            <a href="">家用电器</a>
        </li>
        <li>
            <a href="">手机</a> / <a href="">运营商</a> / <a href="">数码</a>
            <div class="erji"></div>
        </li>
        <li><a href="">电脑</a> / <a href="">办公</a></li>
        <li><a href="">家居</a> / <a href="">家具</a> / <a href="">家装</a> / <a href="">厨具</a></li>
        <li><a href="">男装</a> / <a href="">女装</a> / <a href="">童装</a> / <a href="">内衣</a></li>
        <li><a href="">美妆</a> / <a href="">个护清洁</a> / <a href="">宠物</a></li>
        <li><a href="">女鞋</a> / <a href="">箱包</a> / <a href="">钟表</a> / <a href="">珠宝</a></li>
        <li>
            <a href="">男鞋</a> / <a href="">运动</a> / <a href="">户外</a>
            <div class="erji" style="background: yellow;"></div>
        </li>
        <li><a href="">房产</a> / <a href="">汽车</a> / <a href="">汽车用品</a></li>
        <li><a href="">母婴</a> / <a href="">玩具乐器</a></li>
        <li><a href="">食品</a> / <a href="">酒类</a> / <a href="">生鲜</a> / <a href="">特产</a></li>
        <li><a href="">艺术 / 礼品鲜花</a> / <a href="">农资绿植</a></li>
        <li><a href="">医药保健</a> / <a href="">计生情趣</a></li>
        <li><a href="">图书</a> / <a href="">文娱</a> / <a href="">教育</a> / <a href="">电子书</a></li>
        <li>
            <a href="">机票</a> / <a href="">酒店</a> / <a href="">旅游</a> / <a href="">生活</a>
            <div class="erji" style="background: red;"></div>
        </li>
        <li><a href="">理财</a> / <a href="">众筹</a> / <a href="">白条</a> / <a href="">保险</a></li>
        <li><a href="">安装</a> / <a href="">维修</a> / <a href="">清洗</a> / <a href="">二手</a></li>
        <li>
            <a href="">工业品</a>
            <div class="erji" style="background: palegreen;"></div>
        </li>
    </ul>
</body>

</html>
<!-- 如果你有鼠标  按下鼠标滑轮键  按下去！！ 然后将鼠标整体向下位移   物理性  手动挪下去 -->
<!-- 没有鼠标 按住alt按键  去选择其他的  也可以   或者  alt+shift框选多个 -->
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650451659830-29ea6ce6-bca2-4439-9509-e8a13190eab4.gif#clientId=u9dee61d1-9fba-4&from=paste&height=435&id=u7b8786cd&originHeight=544&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=139118&status=done&style=stroke&taskId=u225ab24c-59d7-47e4-b538-624c4c1352a&title=&width=760)
<a name="qcJxe"></a>
# 站酷二级
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

        #header {
            width: 1200px;
            height: 60px;
            background: #333;
            margin: 0 auto;
            line-height: 60px;
        }

        .menu {
            color: #FFF;
            text-decoration: none;
            padding-left: 30px;
            padding-right: 30px;
            border-right: 1px solid #fff;
            /* 因为超链接里面想要包裹div  默认情况下 行内元素a是不可以包裹块状元素div的 */
            /* 所以我设置浮动 */
            float: left;
            background: #ccc;
            /* 父相子绝 */
            position: relative;
        }

        .erji {
            width: 100%;
            /* 这里面  百分百代表和父元素宽度一致  前提条件是你设置了绝对定位   */
            background: pink;
            /* 二级永远设置绝对定位   我想根据父元素进行定位 所以父元素menu设置相对定位*/
            position: absolute;
            left: 0;
            top: 60px;
            /* 默认的时候  我希望他的高度是0  */
            height: 0;
            /* 设置一个过渡时间 */
            transition: 1s;
            /* 因为有文字  高度为0 的时候  文字会溢出  设置溢出隐藏 */
            overflow: hidden;
        }

        /* 鼠标滑过menu  我希望二级高度变300 */
        .menu:hover .erji {
            height: 300px;
        }

        .erji span {
            padding-left: 3px;
        }
    </style>
</head>

<body>
    <div id="header">
        <a href="" class="menu">
            城市
            <div class="erji">
                <span>北京</span>
                <span>重庆</span>
                <span>大连</span>
                <span>葫芦岛</span>
                <span>抚顺</span>
                <span>锦州</span>
                <span>丹东</span>
                <span>长沙</span>
                <span>哈尔滨</span>
                <span>阜新</span>
            </div>
        </a>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650451804701-e7ac536e-d4fd-4a8e-ad4a-cf9ba85b6bc1.gif#clientId=u9dee61d1-9fba-4&from=paste&height=363&id=u508ec7a9&originHeight=454&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43555&status=done&style=stroke&taskId=u951e1471-158f-402f-b253-d563e920da1&title=&width=760)
<a name="E6Gx9"></a>
# 运动网二级
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

        .big {
            width: 500px;
            height: 500px;
            background: pink;
        }

        .small {
            background: palegreen;
            width: 200px;
            line-height: 40px;
            height: 0px;
            /* 溢出隐藏 */
            overflow: hidden;
            /* 设置过渡时间 */
            transition: 0.2s linear;
        }

        /* 鼠标滑过大盒子    里面的子元素高度改变 */
        .big:hover .small {
            height: 320px;
        }
    </style>
</head>

<body>
    <div class="big">
        <div class="small">
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
            <p>二级标题</p>
        </div>
    </div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650451874744-dee22f85-f6e6-4948-aba8-bdbb33933b02.gif#clientId=u9dee61d1-9fba-4&from=paste&height=499&id=u38573368&originHeight=624&originWidth=678&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21376&status=done&style=stroke&taskId=ua5066f4c-3f02-4b4d-964d-f0464d01b10&title=&width=542.4)
