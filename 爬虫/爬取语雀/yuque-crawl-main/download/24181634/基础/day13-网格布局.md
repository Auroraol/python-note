[01-课件.zip](https://www.yuque.com/attachments/yuque/0/2022/zip/25380982/1651828048949-dfabeb45-63a3-46b5-8958-4b0e3598820c.zip?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fzip%2F25380982%2F1651828048949-dfabeb45-63a3-46b5-8958-4b0e3598820c.zip%22%2C%22name%22%3A%2201-%E8%AF%BE%E4%BB%B6.zip%22%2C%22size%22%3A2605744%2C%22type%22%3A%22application%2Fx-zip-compressed%22%2C%22ext%22%3A%22zip%22%2C%22source%22%3A%22%22%2C%22status%22%3A%22done%22%2C%22mode%22%3A%22title%22%2C%22download%22%3Atrue%2C%22taskId%22%3A%22u62050100-2bac-4035-9b8d-fbc4234bebd%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22u4c988670%22%2C%22card%22%3A%22file%22%7D)
<a name="FylRC"></a>
# 网格布局

- 什么是行列？**横**为**行**，**纵**为**列**
<a name="bSnhe"></a>
# 容器属性
<a name="hKust"></a>
## 固定行/列属性 grid-template-rows/columns: 数值/百分比;
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
            display: grid;
            grid-template-rows: 25% 25% 25% 25%;
            grid-template-columns: 20% 50% 30%;
            grid-template-rows: 200px 400px 100px;
            grid-template-columns: 100px 100px 100px 100px 100px;
            width: 500px;
            height: 700px;
            background: green;
        }

        span {
            border: 1px solid #000;
            background: skyblue;
        }
    </style>
</head>

<body>
    <div>
        <span>1</span>
        <span>2</span>
        <span>3</span>
        <span>4</span>
        <span>5</span>
        <span>6</span>
        <span>7</span>
        <span>8</span>
        <span>9</span>
        <span>10</span>
        <span>11</span>
        <span>12</span>
        <span>14</span>
        <span>15</span>
        <span>16</span>
        <span>17</span>
        <span>18</span>
        <span>19</span>
        <span>20</span>
    </div>
</body>

</html>
```
![如果溢出，则由元素自身内容撑开（参考示例里17-20）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654045927104-1acd3cf2-2d72-4cef-8fd9-16dc6c1d653d.png#averageHue=%2386cdea&clientId=udfd9425b-c1c7-4&from=paste&height=279&id=cVQZ8&originHeight=831&originWidth=579&originalType=binary&ratio=1&rotation=0&showTitle=true&size=8080&status=done&style=stroke&taskId=u660c1ce8-d504-490e-b227-345a3e83f64&title=%E5%A6%82%E6%9E%9C%E6%BA%A2%E5%87%BA%EF%BC%8C%E5%88%99%E7%94%B1%E5%85%83%E7%B4%A0%E8%87%AA%E8%BA%AB%E5%86%85%E5%AE%B9%E6%92%91%E5%BC%80%EF%BC%88%E5%8F%82%E8%80%83%E7%A4%BA%E4%BE%8B%E9%87%8C17-20%EF%BC%89&width=194.20001220703125 "如果溢出，则由元素自身内容撑开（参考示例里17-20）")
<a name="xqkuK"></a>
## repeat() 功能函数 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>网格布局</title>
    <style>
        /* 父元素(容器)设置网格布局之后  里面的子元素(项目) 可以设置宽高 参考第58行代码 */
        .big {
            /* 1、设置给父元素  也就是容器  形成网格布局 */
            display: grid;
            /* 
                * 行 grid-template-rows:
                * 列 grid-template-columns: 
            */
            /* 代表分成3列  第一列宽600  第二列宽400  第三列宽200 */
            grid-template-columns: 600px 400px 200px;/* 数值 */
            grid-template-rows: 300px 300px 200px 100px;/* 数值 */
            grid-template-columns: 33.33% 33.33% 33.33%;/* 百分比 */
            grid-template-rows: 25% 25% 25% 25%;/* 百分比 */
            /* 功能函数 repeat()  上述代码可简写成以下代码  依个人喜好 */
            grid-template-columns: repeat(3, 33.33%);
            grid-template-rows: repeat(4, 100px);
            /* fr关键字(列宽片段) */
            grid-template-columns: 3fr 2fr 1fr;
            grid-template-rows: 2fr 1fr 1fr 1fr;
            width: 1200px;
            height: 900px;
            margin: 0 auto;
            background: pink;
        }

        span {
            background: green;
            border: 1px solid #000;
        }

        /* 
            * 2、grid-column ， grid-row网格线合并(单一属性)  
            * 请注意  它是设置给  子元素（项目的） 
        */
        .s5 {
            /* 代表第二条列网格线 到 第四条列网格线区域 */
            grid-column: 2 / 4;
            /* 代表第一条行网格线 到 第二条行网格线之间的区域 */
            grid-row: 1 / 2;
            /*  请注意 数字和/斜杠之间 一定要用空格隔开 */
        }
    </style>
</head>

<body>
    <!-- 容器：指的是父元素   也就是在这里  div是容器 -->
    <div class="big">
        <!-- 项目：指的是子元素   也就是在这里  10个span都是项目 -->
        <span>1</span><!-- span默认是行内元素  在一行显示  不能设置宽高 -->
        <span>2</span>
        <span>3</span>
        <span>4</span>
        <span class="s5">5</span>
        <span>6</span>
        <span>7</span>
        <span>8</span>
        <span>9</span>
        <span>10</span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651829220740-01223d12-1c34-458f-acd5-a3ba4dc6a24c.png#averageHue=%23007f00&clientId=u70348416-9246-4&from=paste&height=603&id=k5Ptr&originHeight=754&originWidth=1002&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5934&status=done&style=stroke&taskId=u9ed72839-d660-4350-a542-abdedf66e29&title=&width=801.6)
<a name="xDvOY"></a>
## auto-fill 自动填充 

1. `auto-fill`关键字（自动填充），搭配功能函数`repeat()`使用
2. 适用场景：
- **父元素**不是固定宽高，**是百分比**
- 适用于移动端 
3. 实现效果：
- 不管页面放大缩小，永远是固定的宽高（实现效果有些类似响应式布局）
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        header {
            display: grid;
            grid-template-columns: repeat(auto-fill, 300px);
            grid-template-rows: repeat(auto-fill, 200px);
            width: 60%;
            height: 800px;
            background: green;
        }

        section {
            background: skyblue;
            border: 1px solid #000;
        }
    </style>
</head>

<body>
    <header>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
        <section></section>
    </header>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654047557933-7e60b773-228f-447a-bf02-7e19ffced78d.png#averageHue=%23027f01&clientId=udfd9425b-c1c7-4&from=paste&height=200&id=u745752ec&originHeight=592&originWidth=940&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17636&status=done&style=stroke&taskId=u1251d38f-fbce-4ccf-8643-cc663c4ad8a&title=&width=318)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654046981906-f53fe843-7ccd-4de5-8e0d-c1dec12b6bcd.png#averageHue=%23abd7e9&clientId=udfd9425b-c1c7-4&from=paste&height=200&id=uf7d29151&originHeight=258&originWidth=380&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12292&status=done&style=stroke&taskId=u4261801e-0d74-4f5d-8ab5-38bc03f1aa3&title=&width=295)
<a name="tI1ka"></a>
## fr  列宽片段 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* fr 关键字（列宽片段） */
        main {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr; /* 1fr就是1等份 */
            grid-template-rows: 1fr 2fr 3fr;
            width: 80%;
            height: 600px;
            margin: 0 auto;
            background: skyblue;
        }

        section {
            background: #000;
            border: 1px solid #fff;
        }
    </style>
</head>

<body>
    <main>
        <section></section>
        <section></section>
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654047458915-08cfbe1a-b6b2-48e4-b87f-9eaa44296eec.png#averageHue=%23585858&clientId=udfd9425b-c1c7-4&from=paste&height=221&id=u97c59b4c&originHeight=884&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6975&status=done&style=stroke&taskId=u5236e572-0a37-4093-bcdc-6ca545906c0&title=&width=239.4000244140625)
<a name="QPrbH"></a>
## minmax() 功能函数、auto 关键字
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
            display: grid;
            /* 1. minmax() 功能函数  最小最大 */
            /* grid-template-columns: 100px 150px minmax(100px, 500px); */
            /* 2. auto关键字 自动填充  剩下的都是它的（占满剩余空间） */
            grid-template-columns: 100px auto 200px;
            /* 除了第一列和第三列的宽度，剩下都是第二列的宽度 */
            width: 80%;
            height: 500px;
            margin: 0 auto;
            padding: 50px;
            background: skyblue;
        }

        section {
            border: 1px solid #000;
            background: hotpink;
        }
    </style>
</head>

<body>
    <main>
        <section></section>
        <section></section>
        <section></section>
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
<a name="hkfdR"></a>
## [ ] 网格线起名、gap 网格间距 
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
            display: grid;
            /* 
            * 1. 网格线名称  网络线命名的时候[]在每一个单元格的左右 
            * 行rows，所以横向的网格线叫r；列col，所以纵向的网络线叫c；当然，叫gouzi也没问题 
            */
            /* 比如三行三列 那就是4条横线 4条纵线 */
            grid-template-columns: [c1] 100px [c2] 200px [c3] 300px [c4];
            grid-template-rows: [r1] 1fr [r2] 1fr [r3] 1fr [r4];
            /* 2. gap网格间距  gap:水平 垂直; */
            gap: 20px 30px;
            width: 1200px;
            height: 500px;
            background: green;
        }

        section {
            border: 1px solid #000;
            background: skyblue;
        }
    </style>
</head>

<body>
    <main>
        <section></section>
        <section></section>
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
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654050868919-6de39c56-4bd1-4a67-9318-1208f01b6053.png#averageHue=%230b8106&clientId=udfd9425b-c1c7-4&from=paste&height=482&id=u193cfeb0&originHeight=603&originWidth=1370&originalType=binary&ratio=1&rotation=0&showTitle=false&size=82689&status=done&style=stroke&taskId=u24d0dc77-bc91-44b7-a670-45790d05781&title=&width=1096)
<a name="u4fsu"></a>
## grid-area 指定区域
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

        ul {
            /* 设置网格布局 */
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: 1fr 1fr 1fr;
            grid-template-areas: 'a b c'
                                 'd e f'
                                 'g h i';
            /* 此时代表给网格布局区域，三行三列，每个单元格起了一个名字，分别叫a..i */
            width: 1000px;
            height: 600px;
            margin: 0 auto;
            background: pink;
            list-style: none;
        }

        li {
            border: 1px solid #000;
            background: green;
        }

        .li-1 {
            grid-area: b;
        }
    </style>
</head>

<body>
    <ul>
        <li class="li-1">1</li>
        <li class="li-2">2</li>
        <li class="li-3">3</li>
        <li class="li-4">4</li>
        <li class="li-5">5</li>
        <li class="li-6">6</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654184422829-96e74d7c-dbf4-47ec-88e7-b3a7435c813c.png#averageHue=%23dbdcdd&clientId=ub31dfd65-4233-4&from=paste&height=307&id=u0013c5b1&originHeight=503&originWidth=835&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7517&status=done&style=stroke&taskId=u24358da0-f872-4f7d-b1c0-f69c197cb26&title=&width=510.4000244140625)
<a name="O56j1"></a>
## grid-auto-flow: column/row; 项目排列顺序

1. 在**默认情况**下（也就是默认值），子元素没有设置宽高，就会和单元格宽高一致 
- 什么叫单元格？就是你划分成几行几列，我和里面的那个小网格块一样大
2. 但是！如果设置单元格内容对齐，子元素就不是单元格宽高了 ，就变成了自己本身的大小（也就是说，子元素如未设置宽高，则由内容撑开）
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
            display: grid;
            grid-template-columns: repeat(3, 400px);
            grid-template-rows: repeat(4, 100px);
            /* 项目排列顺序 */
            grid-auto-flow: column; /* 默认rows */
            width: 1200px;
            height: 400px;
            background: green;
        }
        section{
            border: 1px solid #000;
            background: skyblue;
        }
    </style>
</head>

<body>
    <main>
        <section>1</section>
        <section>2</section>
        <section>3</section>
        <section>4</section>
        <section>5</section>
        <section>6</section>
    </main>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654068906290-be1bea7a-9e34-4455-948e-d052f470558a.png#averageHue=%235fb7a6&clientId=u01c81977-2185-4&from=paste&height=374&id=sAaRt&originHeight=467&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5478&status=done&style=stroke&taskId=u443430bb-bf1a-4d02-a201-be28f7d3298&title=&width=767.2)
<a name="aR0Uu"></a>
## place-items 单元格内容对齐（重要）
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
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            /* 单元格内容对其（重点：复合属性） */
            /* 垂直 justify-items: start/center/end/stretch默认值; */
            /* 水平 align-items: stretch默认值/start;/center/end */
            /* align-items: end; */
            /* 上述这两个 简写为  place-items: 水平 垂直; */
            place-items: center center;
            width: 1200px;
            height: 600px;
            background: green;
        }

        section {
            border: 1px solid #000;
            background: skyblue;
            width: 100px;
            height: 100px;
        }
    </style>
</head>

<body>
    <main>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
    </main>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654186078087-5943bb72-3f19-4ef4-93bb-851f2ef4a65b.png#averageHue=%23008000&clientId=ub31dfd65-4233-4&from=paste&height=200&id=u82d1e39d&originHeight=771&originWidth=1522&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11794&status=done&style=stroke&taskId=u0a3db4aa-f91e-4eb1-86b3-7f096315bc8&title=&width=395)![辅助理解图（对齐的是网格）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654187481843-17e5fe71-b439-4b94-afea-8fcedc73ff24.png#averageHue=%2386aacd&clientId=ub31dfd65-4233-4&from=paste&height=200&id=u954e7fcc&originHeight=298&originWidth=308&originalType=binary&ratio=1&rotation=0&showTitle=true&size=41283&status=done&style=stroke&taskId=u6431cfca-2076-41f4-a96f-9e9e21f99b1&title=%E8%BE%85%E5%8A%A9%E7%90%86%E8%A7%A3%E5%9B%BE%EF%BC%88%E5%AF%B9%E9%BD%90%E7%9A%84%E6%98%AF%E7%BD%91%E6%A0%BC%EF%BC%89&width=207 "辅助理解图（对齐的是网格）")
<a name="itBa0"></a>
## place-content 单元格项目对齐（参考弹性盒）
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
            display: grid;
            grid-template-columns: repeat(3, 200px);
            grid-template-rows: repeat(3, 100px);
            /* 单元格项目对其（重点：复合属性） */
            /* 水平  和弹性盒的属性值一样*/
            justify-content: center;
            justify-content: space-around;
            /* 垂直  和弹性盒的属性值一样 */
            align-content: space-around;
            /* 简写 */
            /* place-content: 水平 垂直; */
            place-content: center center;
            width: 1200px;
            height: 600px;
            background: skyblue;
        }

        section {
            border: 1px solid #000;
            background: pink;
        }
    </style>
</head>

<body>
    <main>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
        <section>网格布局</section>
    </main>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654186867548-dc8120a4-9114-434c-8b60-55405d66c79c.png#averageHue=%2386cdea&clientId=ub31dfd65-4233-4&from=paste&height=200&id=u1adfbcf9&originHeight=772&originWidth=1522&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11579&status=done&style=stroke&taskId=uedb5e7f3-4af0-412c-b8c8-68bf64efadd&title=&width=394)![辅助理解图（对齐的是整个容器）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1654187586583-cfab2669-a59b-4192-9777-4bb1ac1ec895.png#averageHue=%23f9cc9d&clientId=ub31dfd65-4233-4&from=paste&height=200&id=u053d5639&originHeight=317&originWidth=337&originalType=binary&ratio=1&rotation=0&showTitle=true&size=40469&status=done&style=stroke&taskId=u1f25439e-b9bd-402d-a284-c89044684ba&title=%E8%BE%85%E5%8A%A9%E7%90%86%E8%A7%A3%E5%9B%BE%EF%BC%88%E5%AF%B9%E9%BD%90%E7%9A%84%E6%98%AF%E6%95%B4%E4%B8%AA%E5%AE%B9%E5%99%A8%EF%BC%89&width=213 "辅助理解图（对齐的是整个容器）")
<a name="dAQiV"></a>
# 项目属性
<a name="hc3nQ"></a>
## grid-column、grid-row 网格线合并
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
            /* 设置网格 */
            display: grid;
            /* 三行  三列 */
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: 1fr 1fr 1fr;
            width: 510px;
            height: 457px;
            background: pink;
            margin: 0 auto;

        }

        span {
            background: green;
            bordeR: 1px solid #000;
        }

        .s1 {
            /* 单独设置  我希望 他的列数 是从1到3  行数不变  所以可以不用设置行 */
            grid-column: 1 / 3;
        }

        /* 单独设置  我希望第四个 列数是2~4  行数不变  所以可以不用设置行 */
        .s4 {
            grid-column: 2 / 4;
        }

        .s5 {
            /* 单独设置  我希望 他的列数 是从1到3  行数不变  所以可以不用设置行 */
            grid-column: 1 / 3;
        }
    </style>
</head>

<body>
    <div class="big">
        <span class="s1">1</span>
        <span class="s2">2</span>
        <span class="s3">3</span>
        <span class="s4">4</span>
        <span class="s5">5</span>
        <span class="s6">6</span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651830175641-e320b401-df99-4f32-9448-9cf27cbb6408.png#averageHue=%23007f00&clientId=u70348416-9246-4&from=paste&height=393&id=JzoWF&originHeight=716&originWidth=800&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5720&status=done&style=stroke&taskId=u1dde2b31-c622-4e15-8d89-18cc3129850&title=&width=439)
<a name="G0erw"></a>
# demo
![QQ图片20220506141343.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651844695455-e40488a2-fd6b-4758-bd00-0d91154e01fa.png#averageHue=%234f89a8&clientId=u86a045fc-9ce0-4&from=paste&height=366&id=u9afe16ee&originHeight=457&originWidth=510&originalType=binary&ratio=1&rotation=0&showTitle=false&size=421224&status=done&style=stroke&taskId=ua54f4abd-01d2-459e-b62d-ef89494001f&title=&width=408)
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

        ul {
            /* 设置网格布局 */
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: 1fr 1fr 1fr;
            grid-template-areas: 'b b c'
                                 'd a a'
                                 'h h i';
            width: 1300px;
            height: 600px;
            margin: 0 auto;
            background: pink;
            list-style: none;
        }

        li {
            border: 1px solid #000;
            background: green;
        }

        .li-1 {
            grid-area: b;
        }

        .li-4 {
            grid-area: a;
        }

        .li-5 {
            grid-area: h;
        }
    </style>
</head>

<body>
    <ul>
        <li class="li-1">1</li>
        <li class="li-2">2</li>
        <li class="li-3">3</li>
        <li class="li-4">4</li>
        <li class="li-5">5</li>
        <li class="li-6">6</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651840484145-e40b4a7a-9f2c-4bd7-b2e7-7587e6b4c7c3.png#averageHue=%23007f00&clientId=u70348416-9246-4&from=paste&height=302&id=uec6c0491&originHeight=377&originWidth=815&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2727&status=done&style=stroke&taskId=uf039ec24-530f-4414-bfbe-783f098a293&title=&width=652)
<a name="CyCoI"></a>
# demo2
![QQ图片20220506170620.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651840562327-0c31e7bc-5d96-4769-94b1-baaf07b32ff7.png#averageHue=%2380705a&clientId=u70348416-9246-4&from=paste&height=573&id=uc4506390&originHeight=716&originWidth=1290&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1433703&status=done&style=stroke&taskId=u53d29596-8239-43a0-9419-772fa72f327&title=&width=1032)
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

        ul {
            /* 设置网格布局 */
            display: grid;
            /* 设置三行四列 */
            grid-template-columns: 2fr 1fr 1fr 2fr;
            grid-template-rows: 2fr 1fr 1fr;
            grid-template-areas: 'a b c c'
                                 'd d e f'
                                 'd d h i';
            width: 1200px;
            height: 700px;
            margin: 0 auto;
            background-color: pink;
            list-style: none;
        }

        li {
            background: green;
            border: 1px solid #000
        }

        .li3 {
            grid-area: c;
        }

        .li4 {
            grid-area: d;
        }
    </style>
</head>

<body>
    <ul>
        <li class="li1">1</li>
        <li class="li2">2</li>
        <li class="li3">3</li>
        <li class="li4">4</li>
        <li class="li5">5</li>
        <li class="li6">6</li>
        <li class="li7">7</li>
        <li class="li8">8</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1651840613926-4384c583-982d-4f6d-abb7-023c17762778.png#averageHue=%23007f00&clientId=u70348416-9246-4&from=paste&height=352&id=u556e734f&originHeight=440&originWidth=752&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3072&status=done&style=stroke&taskId=u684bf9d9-18a9-4e46-93b6-37df96681dc&title=&width=601.6)
