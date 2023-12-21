<a name="qF9Vp"></a>
# 代码的优化
1. 代码的嵌套不要超过三层
2. `.cc` 权重 > 图下面组群权重（可以理解为：一车土 > 10捧土）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649062107702-c65130f4-8cbc-41c7-917c-ffc73db1fdeb.png#clientId=ub12156d6-4ede-4&from=paste&height=94&id=u071fa95f&originHeight=118&originWidth=610&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23986&status=done&style=stroke&taskId=ubcc3bb1e-77e4-4d95-97ba-83ee0f54de5&title=&width=488)
<a name="rVCLm"></a>
# 背景属性 background
<a name="S1LBN"></a>
## 背景颜色 background-color
```css
background-color: blueviolet;
```
<a name="vnHhl"></a>
## 背景图片 background-image

1. `./`在**当前**目录
2.  `../`是返回**上一级**，跳出当前文件夹
```css
background-image: url(images/2.png);
```
<a name="xM508"></a>
## 背景图是否平铺 background-repeat
```css
background-repeat: repeat;	  /* 默认值 平铺 */
background-repeat: no-repeat; /* 常用 不平铺 */
background-repeat: repeat-x;  /* 横向平铺 */
background-repeat: repeat-y;  /* 纵向平铺 */
```
<a name="rRARV"></a>
## 背景图位置 background-position

- `background-position:` 水平位置 垂直位置;
```css
background-position-x: left/center/right/数值/百分比;  /* 水平位置 */
background-position-y: top/center/bottom/数值/百分比;  /* 垂直位置 */
/* 注意！背景图位置是可以简写的（也称为复合属性） */
/* background-position: 水平位置 垂直位置; */
```
```css
background-position: right bottom;
background-position: 200px center;
background-position: center center; 
/* 等价于 background-position: center; */
```
<a name="ePKPS"></a>
## 整体简写

- `background: 颜色 图片 平铺 位置; `
- （顺序可以更换 颜色 平铺 图片 位置）
```css
background: pink url(images/2.png) no-repeat center;
```
<a name="EZqus"></a>
## 背景图大小 background-size: 水平大小  垂直大小; 
<a name="sXNxY"></a>
## 代码汇总
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>css背景属性</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        div {/* 代表选中了页面中所有div 元素选择器 权重是1 */
            width: 1340px;
            height: 1300px;
            /* 1.背景颜色 */
            background-color: blueviolet;
            /* 2.背景图片 */
            background-image: url(images/2.png);
            /* ./在当前目录 ../是返回上一级 跳出当前文件夹 */
            /* 3.背景图是否平铺 */
            background-repeat: repeat;/* 默认值 平铺 */
            background-repeat: no-repeat;/* 常用 不平铺 */
            background-repeat: repeat-x;/* 横向平铺 */
            background-repeat: repeat-y;/* 纵向平铺 */
            background-repeat: no-repeat;/* 默认值 平铺 */
            /* 4.背景图位置 */
            background-position-x: left/center/right/数值/百分比;/* 水平位置 */
            background-position-y: top/center/bottom/数值/百分比;/* 垂直位置 */
            /* 注意！背景图位置是可以简写的（也称为复合属性） */
            /* background-position: 水平位置 垂直位置; */
            background-position: right bottom;
            background-position: 200px center;
            /* background-position: center center; 等价于 background-position: center; */
            /* 5.整体的简写 background: 颜色 图片 平铺 位置; （顺序可以更换 颜色 平铺 图片 位置） */
            background: pink url(images/2.png) no-repeat center;
        }
    </style>
</head>

<body>
    <div>知其然知其所以然,知其然知其所以然,知其然知其所以然,知其然知其所以然,知其然知其所以然,知其然知其所以然,知其然知其所以然,知其然知其所以然</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1648687926174-e58bee85-4634-4104-b3c4-d19b65ac6ae9.png#clientId=u75cc1aaa-1c4e-4&from=paste&height=658&id=u91b6cf6f&originHeight=823&originWidth=847&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8527&status=done&style=stroke&taskId=uf814c3f1-e833-4a2c-bda2-ddc4f10d991&title=&width=677.6)
<a name="cnvgT"></a>
## 背景图固定 background-attachment: fixed;

- 注意！元素设置背景图固定之后，背景图的位置是根据浏览器来设定的
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        div {
            width: 1000px;
            height: 500px;
            /* 背景：颜色 图片 平铺 位置 */
            background: pink url(../images/2.png) no-repeat center top;
            /* 背景图固定 注意！元素设置背景图固定之后 背景图的位置是根据浏览器来设定的 */
            background-attachment: fixed;
        }
    </style>
</head>

<body>
    <div>背景图最后一个属性啦！！！</div>
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
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641704044076-1c112461-90ce-49be-b59b-953b1bccc136.png#clientId=u367b93a3-d42f-4&from=paste&height=254&id=ud157da87&originHeight=568&originWidth=896&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28868&status=done&style=stroke&taskId=u9e417526-b51a-4b6a-b485-9fd1f4653e3&title=&width=400)![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1648688275921-da55175f-9288-4311-9f47-c82b189b8cfb.gif#clientId=u75cc1aaa-1c4e-4&from=drop&height=169&id=u74c8dd2d&originHeight=769&originWidth=952&originalType=binary&ratio=1&rotation=0&showTitle=false&size=440608&status=done&style=stroke&taskId=ude8160e2-4360-427d-9ba5-63b617662ab&title=&width=209)
<a name="KBKxM"></a>
# 边框属性 border
<a name="Nm3oa"></a>
## 边框 border: 大小 线型 颜色;

1. 会撑大盒子
2. 去除边框 `border: 0;`
3. 线型 
- `solid`   实线 
- `dotted` 点状线 
- `dashed` 虚线 
- `double` 双实线
```css
border: 1px solid #000;
border: 10px double #0f0f0f;
```

4. 边框可以单独设置某一边
```css
左边框：border-left: 2px solid #000;
右边框：border-right: 1px solid #999;
上边框：border-top: 3px solid #333;
下边框：border-bottom: 5px solid #222;
```

5. 复合属性
```css
border-right: 8px solid #000;
/*
    * 上述写的 是简写（复合属性）
    * 8px 边框大小 border-width
    * solid 边框线型 border-style
    * #000 边框颜色 border-color
*/
```
<a name="boKX1"></a>
### 设置边框大小 border-width

1. `border-width: 5px;`
2. 单独设置边框大小，不设置线型，则不显示边框
<a name="oruZU"></a>
### 设置边框线型 border-style

- `border-style: solid;`
- 也就是说，边框设置了大小和线型，如果没有设置颜色，默认是黑色
<a name="N0gja"></a>
#### 单独设置线型

1. 注意！边框 我们一般简写为：
- `border: 大小 线型 颜色 ;`
- `border-left: 大小 线型 颜色 ;`
2. 但是，如果你单独设置了线型，它也是会出来边框的，出来一个3px的黑色边框
<a name="o6lcp"></a>
### 设置边框颜色 border-color

- `border-color: chartreuse;`
- 上面这三个属性 等同于 ：
```css
border: 5px solid chartreuse;
```
<a name="FBVac"></a>
## 代码汇总
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>边框的属性</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        div {
            width: 200px;
            height: 200px;
            background: #d8b;
            /* 1.边框 border: 大小 线型 颜色; */
            /* 线型 solid实线 dotted点状线 dashed虚线 double双实线 */
            border: 10px double #0f0;
            /* 边框可以单独设置某一边 */
            /* 左边框：border-left: 2px solid #000;
            右边框：border-right: 1px solid #999;
            上边框：border-top: 3px solid #333;
            下边框：border-bottom: 5px solid #222; */
            /* border-right: 8px solid #000; */
            /* 其实我们刚才写的 是简写（复合属性） */
            /* 8px 边框大小 border-width
            solid 边框线型 border-style
            #000 边框颜色 border-color */
            /* 设置边框大小 */
            border-width: 5px;
            /* 设置边框线型 */
            border-style: solid;
            /* 也就是说 边框设置了大小和线型 如果没有设置颜色 默认是黑色
            设置边框颜色 */
            border-color: chartreuse;
            /* 上面这三行代码 等同于 border: 5px solid chartreuse; */
        }

        p {
            width: 200px;
            height: 200px;
            background: #099090;
            /* 我们单独设置大小 线型 颜色的时候 也是可以单独设置某一边的 */
            border-left-style: solid;
            border-left-width: 10px;
            border-left-color: chartreuse;
        }
    </style>
</head>

<body>
    <div></div>
    <p></p>
</body>

</html>
<!-- 
    * 注意！ 边框我们一般简写 border：大小 线型 颜色
    *                        border-left:大小 线型 颜色
    * 但是 如果你单独设置了线型 它也是会出来边框的 出来一个3px的黑色边框 
-->
```
<a name="xbxqQ"></a>
## 边框的注意事项

1. 块状元素可以设置上下左右边框
2. 行内元素在一行显示 ，不可以设置宽高，大小由内容撑开
- 行内元素可以设置左右边框
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {/* 块状元素 可以设置上下左右边框 */
            width: 200px;
            height: 200px;
            background: cyan;
            border-top: 5px solid darkblue;
            border-bottom: 10px solid darkmagenta;
            border-left: 10px solid darksalmon;
            border-right: 14px solid darkgoldenrod;
        }

        span {/* 行内元素 在一行显示 不可以设置宽高 大小由内容撑开 */
            /* width: 200px;无效
            height: 200px;无效 */
            background: pink;
            border-left: 10px solid tomato;
            border-right: 5px solid blue;
        }
    </style>
</head>

<body>
    <div>块状元素</div>
    <span>行内元素</span>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641359848645-16807151-ea35-4254-a253-061570003cda.png#clientId=u6eb43f89-00ca-4&from=paste&height=221&id=u719402e3&originHeight=315&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3904&status=done&style=stroke&taskId=ubae5e53b-7abd-47c9-9cdf-9e75b6249dc&title=&width=209)
<a name="KMNos"></a>
## 使用边框书写三角形

- `transparent` 表示边框值为透明

![]_T5661~)3JL$YXL8LY9S]2.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641351233068-d8751347-7296-4b3c-bdb4-91a41cc5c56d.png#clientId=u053f328d-079d-4&from=paste&height=151&id=ua421863f&originHeight=302&originWidth=1600&originalType=binary&ratio=1&rotation=0&showTitle=false&size=58399&status=done&style=stroke&taskId=u29a7392e-a361-443e-96b1-5dd53a65ba4&title=&width=800)<br />![6~_DA4%OS@XM~G$[Z($0{YW.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641351260676-426c103b-1629-4468-9fe7-eb33158fa24e.png#clientId=u8b7d13e5-2c21-4&from=paste&height=197&id=u9bd380c5&originHeight=393&originWidth=420&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26640&status=done&style=stroke&taskId=u40c5b3d1-2b1c-40d3-a899-6698d296adf&title=&width=210)<br />![XU43X$@GGZOZO%`XHMMLQ3I.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641351267770-d068c8c8-7305-4749-a90e-86cb6816928a.png#clientId=u8b7d13e5-2c21-4&from=paste&height=202&id=u72288f1a&originHeight=404&originWidth=1600&originalType=binary&ratio=1&rotation=0&showTitle=false&size=85085&status=done&style=stroke&taskId=u5ebf406d-2502-42d9-a1bb-5ff9e97c368&title=&width=800)<br />![HLJH)26V(86[E1(RE5T`Z7A.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641351279289-fd4c9d98-3ed6-4374-b37f-50bbc82e7629.png#clientId=u8b7d13e5-2c21-4&from=paste&height=105&id=ucf24cd0c&originHeight=209&originWidth=1026&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32692&status=done&style=stroke&taskId=u40632fc8-79f2-4ae2-8496-7b54c9ba8a2&title=&width=513)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            width: 0px;
            height: 0px;
            background: pink;
            /* 设置边框 */
            border: 100px solid #000;
            border-left-color: transparent;/* 单独更改左边框的颜色 */
            border-right-color: transparent;/* 单独更改右边框的颜色 */
            border-top-color: transparent;/* 单独更改上边框的颜色 */
        }

        p {/* 三角形的书写 设置宽高都为0 设置一个透明的边框 然后你想要朝下三角形 就设置上边框的颜色  */
            width: 0px;
            height: 0px;
            border: 100px solid transparent;
            border-top-color: pink;/* 单独更改上边框的颜色 */
        }
    </style>
</head>

<body>
    <div></div>
    <p></p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641352605478-eb1732ae-4568-47c4-b5c0-315d31402853.png#clientId=u8b7d13e5-2c21-4&from=paste&height=208&id=ube4f5643&originHeight=415&originWidth=262&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3047&status=done&style=stroke&taskId=uf8047f1b-09f4-4b40-ba57-fe18c033e9d&title=&width=131)
