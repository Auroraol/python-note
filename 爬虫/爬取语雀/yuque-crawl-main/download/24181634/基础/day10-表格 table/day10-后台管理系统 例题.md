```html
<!DOCTYPE html>
<html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/system.css">
  </head>
  
  <body>
    <div id="header">
      <!-- 左边 -->
      <img src="../images/logo.png" alt="" class="logo">
      <ul>
        <li><a href=""><img src="../images/1.jpg">办公系统</a></li>
        <li><a href=""><img src="../images/2.jpg">教学系统</a></li>
        <li><a href=""><img src="../images/3.jpg">工单系统</a></li>
        <li><a href=""><img src="../images/4.jpg">运营系统</a></li>
      </ul>
      <!-- 右边 -->
      <a href="" class="headRight">奶盖</a>
    </div>
    <div id="left">
      <ul>
        <li><b><img src="../images/6.jpg" alt="" class="liImg1"></b>教学系统<img src="../images/7.jpg" alt=""
                                                                             class="liImg2"></li>
        <li class="li2">系统首页</li>
        <li><b><img src="../images/8.jpg" alt="" class="liImg1"></b>班级管理<img src="../images/7.jpg" alt=""
                                                                             class="liImg2"></li>
        <li><b><img src="../images/9.jpg" alt="" class="liImg1"></b>就业管理<img src="../images/7.jpg" alt=""
                                                                             class="liImg2"></li>
        <li><b><img src="../images/10.jpg" alt="" class="liImg1"></b>教学管理<img src="../images/7.jpg" alt=""
                                                                              class="liImg2"></li>
        <li><b><img src="../images/11.jpg" alt="" class="liImg1"></b>考试管理<img src="../images/7.jpg" alt=""
                                                                              class="liImg2"></li>
        <li><b><img src="../images/12.jpg" alt="" class="liImg1"></b>周报管理<img src="../images/7.jpg" alt=""
                                                                              class="liImg2"></li>
        <li><b><img src="../images/13.jpg" alt="" class="liImg1"></b>测试管理<img src="../images/7.jpg" alt=""
                                                                              class="liImg2"></li>
        <li><b><img src="../images/14.jpg" alt="" class="liImg1"></b>讲师培训管理<img src="../images/7.jpg" alt=""
                                                                                class="liImg2"> </li>
      </ul>
      <div class="photo">
        <img src="../images/15.jpg" alt="">
      </div>
    </div>
    <div id="right">
      <div class="rightTop">
        <div class="rightTopLeft">
          <a href="">系统管理</a>
          <span>></span>
          <a href="" class="color555">管理首页</a>
        </div>
        <div class="rightTopRight">
          搜索：
          <input type="text" placeholder="请输入学生或公司名字...">
        </div>
      </div>
      <div class="rightMain">
        <table>
          <tr class="tr1">
            <td>登录账户</td>
            <td>IP</td>
            <td>登陆所在地</td>
            <td>上次登陆时间</td>
          </tr>
          <tr class="bgf9">
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr>
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr class="bgf9">
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr>
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr class="bgf9">
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr>
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr class="bgf9">
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr>
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr class="bgf9">
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
          <tr>
            <td>milllllk</td>
            <td>106.38.62.154</td>
            <td>127.0.0.1</td>
            <td>2019-09-24 17:49:55 </td>
          </tr>
        </table>
        <p class="final">
          <span>
            <img src="../images/17.jpg" alt="">
            查看更多
          </span>
        </p>
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

/* 一整屏页面必备条件 */
html,
body {
  height: 100%;
}

/* 头部 */
#header {
  height: 50px;
  background: #418aca;
}

#header .logo {
  float: left;
  margin-left: 39px;
  margin-top: 8px;
  margin-right: 47px;
}

#header ul {
  float: left;
  list-style: none;
  line-height: 50px;
}

#header ul li {
  float: left;
  padding: 0 20px;
}

#header ul a {
  font-size: 16px;
  color: #ffffff;
  text-decoration: none;
}

#header a img {
  /* 图片和其他元素垂直对齐 */
  vertical-align: middle;
  margin-right: 5px;
}

.headRight {
  float: right;
  font-size: 12px;
  color: #ffffff;
  margin-right: 27px;
  text-decoration: none;
  line-height: 50px;
}

#left {
  width: 189px;
  background: #f9f9f9;
  /* 高度是 一整屏高度 减去头部高度 */
  height: calc(100% - 50px);
  float: left;
  border-right: 1px solid #cccccc;
  ;
  
}

#left li {
  line-height: 40px;
  height: 39px;
  border-bottom: 1px solid #e5e5e5;
  /* 去除列表样式 */
  list-style: none;
  font-size: 12px;
  color: #585858;
}

#left .li2 {
  height: 33px;
  line-height: 34px;
  color: #f5f5f5;
  padding-left: 37px;
  background: #6fb3e0;
}

b {
  width: 43px;
  /* 将元素转化为行内块元素 */
  display: inline-block;
  text-align: center;
  vertical-align: middle;
}

.liImg2 {
  float: right;
  margin-right: 12px;
  margin-top: 16px;
}

.photo {
  border-bottom: 1px solid #e0e0e0;
  ;
  height: 26px;
  line-height: 26px;
  text-align: center;
}

#right {
  /* 不要设置宽度  占满一行*/
  height: calc(100% - 50px);
  overflow: hidden;
}

.rightTop {
  height: 40px;
  border-bottom: 1px solid #e5e5e5;
  padding-left: 16px;
  padding-right: 52px;
  line-height: 40px;
}

.rightTopLeft {
  /* 靠左 */
  float: left;
}

.rightTop a {
  text-decoration: none;
  font-size: 12px;
  color: #4c8fbd;
}

.rightTop .color555 {
  color: #555555;
}

.rightTop span {
  font-size: 12px;
  color: #b2bcd5;
  margin-left: 6px;
  margin-right: 7px;
}

.rightTopRight {
  /* 靠右 */
  float: right;
  font-size: 12px;
  color: #393939;
}

input {
  width: 150px;
  height: 26px;
  border: 1px solid #6fb3e0;
  /* 设置圆角 */
  border-radius: 3px;
  font-size: 12px;
  /* 去除聚焦线 */
  outline: 0;
  background: url(../images/16.jpg) no-repeat right center;
}

.rightMain {
  width: 94%;
  /* 代表宽度是父元素宽度的百分之九十四 */
  /* 有宽高的块状元素水平居中 */
  margin: 0 auto;
  margin-top: 8px;
  /* 设置边框 */
  border: 1px solid #c5d0dc;
}

table {
  width: 97%;
  /* 代表表格的宽度是rightMain的百分之九十七 */
  border: 1px solid #dddddd;
  /* 表格需要水平居中父元素 */
  margin: 0 auto;
  /* 单元格之间的距离清零 */
  border-spacing: 0;
  /* 表格边框合并 */
  border-collapse: collapse;
  font-size: 12px;
  color: #707070;
  margin-bottom: 35px;
}

td {
  border: 1px solid #dddddd;
  padding-left: 8px;
  height: 35px;
  line-height: 35px;
}

.tr1 {
  background: #f3f3f3;
  /* 文字加粗 */
  font-weight: bold;
}

tr {
  background: #fff;
}

.bgf9 {
  background: #f9f9f9;
}

.final {
  border-top: 2px solid #c5d0dc;
}

.final span {
  width: 64px;
  height: 60px;
  background: #3190cf;
  float: left;
  margin-left: 14px;
  margin-top: 18px;
  color: #ffffff;
  font-size: 14px;
  text-align: center;
}

.final span img {
  display: block;
  margin-left: 19px;
  margin-top: 6px;
  margin-bottom: 5px;
}
```
[images.rar](https://www.yuque.com/attachments/yuque/0/2022/rar/25380982/1653441808978-49857dee-133a-4fee-9456-37d1422b7f00.rar)<br />![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1653441944641-4acfb8f5-4dc4-4b4b-a649-36530571fcf8.gif#clientId=ue877d41c-a73c-4&from=drop&id=ue82d9908&originHeight=896&originWidth=1908&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2662900&status=done&style=stroke&taskId=u6691dbe1-c342-4aa1-9fb3-4270a6530ac&title=)
