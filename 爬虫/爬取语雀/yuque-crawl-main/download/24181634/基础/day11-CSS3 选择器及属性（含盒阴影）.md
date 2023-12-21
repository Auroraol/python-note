<a name="HQl7o"></a>
# 层级选择器
<a name="f7pqk"></a>
## 毗邻/加号选择器 A+B{}

- `A+B{}` 代表选中了A下面的第一个兄弟元素B
<a name="exvRX"></a>
## 波浪号选择器 A~B{}

- `A~B{}` 代表选中了A下面所有兄弟B
<a name="lkeaW"></a>
## 最常用的子选择器 A>B{}

- `A>B{}` 代表选中了A里面所有子元素B
<a name="iyTKc"></a>
## 注意区分 A>B{} 与 A B{}
<a name="bKnx1"></a>
### .big>span{} 

- 代表选中了`big`里面的儿子级，孙子级是选不上的
<a name="D7AMs"></a>
### .big span{}

- 代表选中了`big`里面所有的`span`，包括儿子级、孙子级...
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>层级选择器</title>
    <style>
        /* 1、毗邻选择器  也叫加号选择器  A+B{}代表选中了A下面的第一个兄弟元素B */
        div+p {
            background: pink;
        }

        /* 2、波浪号选择器  A~B{}代表选中了A下面所有兄弟B */
        div~p {
            background: green;
        }

        /* 3、最常用的子选择器  A>B{}代表选中了A里面所有子元素B */
        .big {
            width: 1000px;
            height: 100px;
            background: skyblue;
            margin: 0 auto;
            line-height: 100px;
        }

        .right {
            float: right;
        }

        .big span { /* 代表选中了big里面所有的span 包括儿子级 孙子级... */
            background: black;
        }

        .big>span { /* 代表选中了big里面的儿子级  孙子级是选不上的 */
            background: #f90;
        }
    </style>
</head>

<body>
    <div class="big">
        <span>我是big的子元素</span>
        <div class="right">
            <span>我是big的孙子级</span>
        </div>
    </div>

    <p>我是第一个孩子 姐姐p</p>
    <div>我是大儿子</div>
    <span>出现了一个私生子</span>
    <p>我是妹妹3</p>
    <p>我是妹妹4</p>
    <p>我是妹妹5</p>
    <p>我是妹妹6</p>
    <p>我是妹妹7</p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649923809587-3d00b6e5-9630-42e8-90cc-9f839e6cb40e.png#clientId=u8af4bacd-0c2f-4&from=paste&height=389&id=u3a6f38d9&originHeight=486&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18400&status=done&style=stroke&taskId=u7b7abc6a-d856-4f9b-ae58-a94049383a5&title=&width=1536)
<a name="gPyLX"></a>
# CSS3属性选择器
<a name="deI17"></a>
## 属性选择器 div[data]{}
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984556040-48fa5a5e-a308-40f9-9921-1e5a246be581.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=ud96f4784&originHeight=471&originWidth=411&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43960&status=done&style=stroke&taskId=uc7cff17e-1abe-4bc4-8a1b-e36d4203743&title=&width=150)
<a name="H6N5i"></a>
## 属性值选择器 div[data="value"]{}
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984625226-719940d9-ad90-4bee-9135-334ec8c2490d.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=u7bda458a&originHeight=467&originWidth=422&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66962&status=done&style=stroke&taskId=u628d6763-d461-416d-b6c3-eeaf52cfcf5&title=&width=155.60000610351562)
<a name="bFlos"></a>
## 属性值开头选择器 div[data^="value"]{}
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984728145-e4bdcff9-4d73-4554-a69d-53b668f6143a.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=u9b0cb675&originHeight=461&originWidth=423&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63192&status=done&style=stroke&taskId=u7569993c-27cc-4d02-804a-c99dff4e11b&title=&width=158)
<a name="DqMZj"></a>
## 属性值结尾选择器 div[data$="value"]{｝
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984768443-def75402-4dfb-453d-9e8d-857ae9a38359.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=uf0a3f70d&originHeight=449&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&size=59903&status=done&style=stroke&taskId=uf3aeb7dd-bfe8-43ff-a1a1-4fc81ea38e8&title=&width=165)
<a name="dYHv1"></a>
## 但凡有abc就行 div[data*="abc"]{｝
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984804790-169165d7-b4ba-418b-89e0-27720143f304.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=u29bfe056&originHeight=466&originWidth=447&originalType=binary&ratio=1&rotation=0&showTitle=false&size=79463&status=done&style=stroke&taskId=u21f8d5b1-81d5-4327-b9a6-77c0b535714&title=&width=165)
<a name="Eivzs"></a>
## div[data~="abc"]{}

- 代表选中了`data`属性值有`abc`这个**单词**，1**空格**隔开的

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984838583-478aa1b7-30d1-442d-8625-2c6b5be7d083.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=ud80b3f27&originHeight=452&originWidth=416&originalType=binary&ratio=1&rotation=0&showTitle=false&size=70802&status=done&style=stroke&taskId=u200a5da9-d836-459a-b676-7365c312c29&title=&width=158)
<a name="lFkFr"></a>
## div[data|="abc"]{}

- 代表选中了`data`属性值为“`abc-`开头的单词列表”  
- 注意！abc也算

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649984884721-06804cba-8230-444c-b233-b16c3a90103c.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=172&id=u89eb9709&originHeight=454&originWidth=432&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67135&status=done&style=stroke&taskId=u44888982-7409-41de-95f0-d30e8627fd5&title=&width=164)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 1、属性选择器 */
        div[data] {
            /* 代表选中了有data属性的div */
            background: red;
        }

        /* 2、属性值选择器 */
        div[data="abc"] {
            /* 代表选中了data属性值为abc的div */
            background: orange;
        }

        /* 3、属性值开头选择器 ^ */
        div[data^="abc"] {
            /* 代表选中了data属性值是abc开头的div */
            background: yellow;
        }

        /* 4、属性值结尾选择器 $ */
        div[data$="abc"] {
            /* 代表选中了data属性值是abc结尾的div */
            background: green;
        }

        /* 5、但凡有abc就行     * */
        div[data*="abc"] {
            /* 代表选中了data属性值里有abc的div   哪里有都算 */
            background: skyblue;
        }

        /* 6、~ */
        /* 代表选中了data属性值有abc这个单词！！单词！！1空格隔开的    */
        div[data~="abc"] {
            background: blueviolet;
        }

        /* 7、| */
        /* 代表选中了data属性值为“abc-开头的单词列表”  注意  abc也算 */
        div[data|="abc"] {
            background: #f90;
        }
    </style>
</head>

<body>
    <div>我没有data属性</div>
    <div data="abc">我会不会变化呢abc</div>
    <div data="abcqqqqqq">我会不会变化呢abcqqqqqq</div>
    <div data="hjhjhjhjhjabc">我会不会变化呢hjhjhjhjhjabc</div>
    <div data="gggabcjjj">我会不会变化呢gggabcjjj</div>
    <div data="abc hhh">我会不会变化呢abc hhh</div>
    <div data="hhh abc">我会不会变化呢hhh abc</div>
    <div data="kkk-abc">我会不会变化呢kkk-abc</div>
    <div data="abc-kkk">我会不会变化呢abc-kkk</div>
    <div data="abc_ooo">我会不会变化呢abc_ooo</div>
    <div data="ooo_abc">我会不会变化呢ooo_abc</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649924065934-cef53be5-c5c5-4b4b-abe8-cb7dd326a148.png#clientId=u8af4bacd-0c2f-4&from=paste&height=318&id=u334c1105&originHeight=397&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69435&status=done&style=stroke&taskId=u36f4526a-c56a-489b-98dd-e9e9695d161&title=&width=767.2)
<a name="qinQ6"></a>
# 超级不好用的结构性伪类
![为什么 :nth-child( )不好用](https://cdn.nlark.com/yuque/0/2022/png/25380982/1653382951463-ecb98103-3d84-456e-92f0-6352e6db12f7.png#clientId=uec117cbc-9c30-4&from=paste&height=214&id=u02e60688&originHeight=268&originWidth=693&originalType=binary&ratio=1&rotation=0&showTitle=true&size=79780&status=done&style=stroke&taskId=u191ff983-d49c-4dd4-857f-0a71952aad3&title=%E4%B8%BA%E4%BB%80%E4%B9%88%20%3Anth-child%28%20%29%E4%B8%8D%E5%A5%BD%E7%94%A8&width=554.4 "为什么 :nth-child( )不好用")
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 结构性伪类 */
        /* 1、选中第一个li */
        li:first-child {
            background: red;
        }

        /* 还可以这样子表示第一个 */
        li:nth-child(1) {
            background: #f90;
        }

        /* 2、选中最后一个li */
        li:last-child {
            background: yellow;
        }

        /* 还可以这样子表示最后一个 */
        li:nth-child(10) {
            background: green;
        }

        /* 3、选中第几个 */
        li:nth-child(5) {
            background: blue;
        }

        /* 4、选中倒数第几个 */
        li:nth-last-child(3) {
            background: skyblue;
        }

        /* 5、选中奇数行 odd*/
        li:nth-child(odd) {
            background: purple;
        }

        /* 6、还可以这样子表示 2n+1 */
        li:nth-child(2n+1) {
            background: pink;
        }

        /* 选中偶数行 */
        li:nth-child(2n) {
            background: hotpink;
        }

        /* 还可以这样子表示偶数行 even */
        li:nth-child(even) {
            background: rgb(238, 8, 123);
        }

        /* X:only-child 这个伪类一般用的比较少，比如上述代码匹配的是div下的有且仅有一个的p，也就是说，如果div内有多个p，将不匹配。 */
        span:only-child {
            background: rgb(246, 84, 181);
        }

        li:nth-child(4) {
            background: rgb(0, 187, 255);
        }
    </style>
</head>

<body>
    <ol>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <span>扰乱了</span>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
        <li>红豆生南国，吹来发几枝</li>
    </ol>
    <div>
        <span>只能有我自己</span>
        <p>尝试</p>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649985120851-638f49e8-e5c2-4ac3-9248-eab1e6316f5a.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=217&id=u08a2fa00&originHeight=633&originWidth=930&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88328&status=done&style=stroke&taskId=ud6f95876-c1c0-4072-9985-5e0a92a6fba&title=&width=319.3999938964844)
<a name="MGBUB"></a>
## demo1
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

        main {
            width: 1150px;
            height: auto;
            background: pink;
            margin: 0 auto;
            overflow: hidden; /* 解决高度塌陷 */
        }

        section {
            width: 300px;
            height: 400px;
            background: salmon;
            float: left;
            margin: 10px 50px;
        }

        section:nth-child(3n) {
            margin-left: 0;
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
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649986056023-792e3308-3fe4-4008-9758-b55a7199c26d.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=247&id=uf4606df1&originHeight=884&originWidth=434&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9627&status=done&style=stroke&taskId=uae9f3a34-16f2-40b3-84ec-5b7110e5550&title=&width=121.20000457763672)
<a name="Q5VT2"></a>
# 超级好用的结构性伪类

- 为什么好用？它会**先**把所有你要检索的元素**拎出**来，**再**去**找**第几个
<a name="cTJa6"></a>
## 选中第一个

1. `li:nth-of-type(1){}`
2. `li:first-of-type{}`
<a name="C6Zev"></a>
## 选中最后一个

1. `li:last-of-type{}`
2. `li:nth-of-type(10)`
- 还可以这样子表示，前提是你知道有多少个
<a name="bV1dU"></a>
## 选中倒数第几个

1. `li:nth-last-of-type(1){}`
2. `li:nth-last-of-type(3){}`
<a name="E2Mst"></a>
## 选中第几个

- `li:nth-of-type(5){}`
<a name="JYAl2"></a>
## 选中奇数行   

1. `odd` 或者 `2n+1`
2. `li:nth-of-type(odd){}`
<a name="FQX3g"></a>
## 选中偶数行

1. `even` 或者 `2n`
2. `li:nth-of-type(even){}`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 1、选中第一个li */
        li:nth-of-type(1) {
            background: red;
        }

        /* 还可以这样子表示第一个 */
        li:first-of-type {
            background: #f90;
        }

        /* 2、选中最后一个li */
        li:last-of-type {
            background: yellow;
        }

        /* 还可以这样子表示  前提是你知道有多少个*/
        li:nth-of-type(10) {
            background: green;
        }

        /* 3、选中倒数第几个 */
        li:nth-last-of-type(1) {
            background: blue;
        }

        /* 还可以这样子表示倒数第几个 */
        li:nth-last-of-type(3) {
            background: skyblue;
        }

        /* 4、选中第几个 */
        li:nth-of-type(5) {
            background: purple;
        }

        /* 5、选中奇数行  odd  或者 2n+1 */
        /* 6、选中偶数行  even 或者 2n */
        li:nth-of-type(odd) {
            background: pink;
        }

        li:nth-of-type(even) {
            background: hotpink;
        }

        /* 好用在哪呢 */
        li:nth-of-type(7) {
            background: greenyellow;
        }
    </style>
</head>

<body>
    <ol>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <span>扰乱</span>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <span>扰乱</span>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <span>扰乱</span>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
        <li>超级好用的 是把所有li先拎出来，再去选择li的第几个；不好用的是咋回事呢 不好用的是先去找第n个位置,然后你得看看，这个位置的元素是不是人家li!!麻烦</li>
    </ol>
</body>

</html>
```
<a name="w1VzK"></a>
## demo2
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 我想让哈哈哈5变红 */
        li:nth-of-type(5)>span {
            background: hotpink;
        }
    </style>
</head>

<body>
    <ol>
        <li>一定要注意的事情<span>哈哈哈1</span></li>
        <li>一定要注意的事情<span>哈哈哈2</span></li>
        <li>一定要注意的事情<span>哈哈哈3</span></li>
        <li>一定要注意的事情<span>哈哈哈4</span></li>
        <li>一定要注意的事情<span>哈哈哈5</span></li>
        <li>一定要注意的事情<span>哈哈哈6</span></li>
        <li>一定要注意的事情<span>哈哈哈7</span></li>
        <li>一定要注意的事情<span>哈哈哈8</span></li>
        <li>一定要注意的事情<span>哈哈哈9</span></li>
        <li>一定要注意的事情<span>哈哈哈10</span></li>
    </ol>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649987440934-b4fab779-6436-4a98-96fa-7c367b79e39d.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=237&id=ud4832758&originHeight=296&originWidth=303&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9660&status=done&style=stroke&taskId=uba018ab4-1003-4c73-83e4-48bdfad1112&title=&width=242.4)
<a name="VOzFI"></a>
# 根节点 html:root
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* :root代表选中了html根节点 */
        html:root {
            background: green;
        }
    </style>
</head>

<body>

</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649987695642-a6cf89ab-111f-4400-8e7c-3d546a2c072b.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=271&id=ueb4156a6&originHeight=889&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8560&status=done&style=stroke&taskId=u73b7b404-58d1-44e1-8a77-8fc87067bbf&title=&width=292.3999938964844)
<a name="TdYrD"></a>
# 空节点 :empty
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div:empty{
            width: 200px;
            height: 200px;
            background: red;
        }
    </style>
</head>
<body>
    <div>哈</div><!-- 将“哈”字删除则变为红色实体 -->
</body>
</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649987857489-a6f84503-2d96-4176-92fe-983346e28696.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=224&id=u523c8cc0&originHeight=322&originWidth=287&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6461&status=done&style=stroke&taskId=u07cf803e-585d-4850-a003-d3317d775dd&title=&width=199.60000610351562)
<a name="Ad76x"></a>
# 目标伪类 :target
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>锚点</title>
    <style>
        div:target {
            /* 代表的是锚点被点击后  目标div所呈现的样式 */
            background: hotpink;
        }
    </style>
</head>

<body>
    <a href="#box1">目标1</a>
    <a href="#box2">目标2</a>
    <div id="box1">111111</div>
    <div id="box2">222222</div>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649991512685-60a09f9a-2da0-4d57-b5b5-b52b5f5450bc.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=74&id=u12628b86&originHeight=92&originWidth=285&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23021&status=done&style=stroke&taskId=u25d28549-2812-4c3c-84a5-2976b41b72f&title=&width=228)
<a name="r7PGF"></a>
# UI 元素状态伪类（选中/禁止/可用/高亮）
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* input元素被点击选中的状态 */
        input:checked {
            width: 20px;
            height: 20px;
        }

        /* input元素被禁止使用的状态 */
        input:disabled {
            width: 10px;
            height: 10px;
        }

        /* input可用的状态  就是除了禁用 都是可用的 */
        input:enabled {
            width: 30px;
            height: 30px;
        }

        /* 框选中元素 自定义高亮区域 */
        p::selection {
            background: skyblue;
            color: hotpink;
        }
    </style>
</head>

<body>
    <input type="radio" name="cc" disabled>HTML5
    <input type="radio" name="cc">JAVA
    <input type="radio" name="cc">UI
    <input type="radio" name="cc">Python
    <input type="radio" name="cc">物联网
    <p>漫漫长路其修远兮</p>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649994018644-4fed2f06-3506-442b-9e5b-2618543c9d0f.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=150&id=ua2883a68&originHeight=187&originWidth=518&originalType=binary&ratio=1&rotation=0&showTitle=false&size=88366&status=done&style=stroke&taskId=u738a4b87-a677-489f-9269-2dea425e509&title=&width=414.4)
<a name="R1yTy"></a>
# 动态伪类选择器 :focus
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* input框聚焦时 */
        input:focus {
            background: skyblue;
        }
    </style>
</head>

<body>
    <!-- 
        * 捡到一个 LVHA 哈一笑  这4个都是动态伪类 
        * a:link{}  a:visited{}  任何元素:hover{}  a:active{}  
    -->
    <input type="text">
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649994227740-57216637-8eeb-4a9f-8df5-c534c1ad1911.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=38&id=u3f76ef9c&originHeight=48&originWidth=227&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7029&status=done&style=stroke&taskId=uadb68297-4557-45d5-a600-1239fe0320c&title=&width=181.6)
<a name="IrfgQ"></a>
## demo3
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        input {
            outline: 0;
        }

        input+span {
            /* 默认消失 */
            display: none;
            /* 代表选中了input下面第一个弟弟 同时这个弟弟是span */
            color: red;
            font-weight: bold;
        }

        input:focus+span {
            /* 代表input聚焦时 下面第一个弟弟(span)的样式 */
            /* 出现 */
            display: inline;
        }
    </style>
</head>

<body>
    <p>
        <input type="text">
        <span>请输入用户名</span>
    </p>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649994725215-5cff5828-24fe-402d-806a-40ad6794393e.gif#clientId=u0bc16bf0-8fd5-4&from=paste&height=36&id=ud50eb92b&originHeight=45&originWidth=349&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21562&status=done&style=stroke&taskId=u77bdf309-3d41-4165-8796-25e01bbde2d&title=&width=279.2)
<a name="ImIIA"></a>
# 否定伪类选择器 :not()
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        p:not(.all) {
            background: skyblue;
        }
    </style>
</head>

<body>
    <!-- 
    否定伪类选择器
    E:not(s) （IE6-8浏览器不支持:not()选择器）
    匹配所有不匹配简单选择符s的元素E 
    -->
    <p>拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p class="all">拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p class="all">拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
    <p>拒绝黄赌毒</p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649995112926-33a49356-ba68-4615-8dd2-b64692a3ec70.png#clientId=u0bc16bf0-8fd5-4&from=paste&height=182&id=u049fe5cb&originHeight=474&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19519&status=done&style=stroke&taskId=ue00bb41f-49e1-4ed1-8253-ddd656c3ec8&title=&width=368.3999938964844)
<a name="JQk5w"></a>
# 盒子阴影 box-shadow

1. 阴影复合值写法
- box-shadow: 水平(可负) 垂直(可负) 模糊程度 面积 颜色 位置 (默认在外侧); 
2. 我们说过，浏览器是有兼容的，CSS3是完全向后兼容的。那么，如果我希望我的CSS3属性，可以在各个浏览器正常显示，那么需要写完整代码，也就是写上兼容（其实就是加上浏览器前缀）
| 兼容示例 |  |
| --- | --- |
| box-shadow: ; | 正常解析 |
| **-webkit-**box-shadow: ; | 针对**谷歌**+**苹果**浏览器 |
| **-moz-**box-shadow: ;  | 针对**火狐** |
| **-ms-**box-shadow: ; | 针对**IE** |
| **-o-**box-shadow: ; | 针对**欧朋** |

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
            width: 100px;
            height: 100px;
            margin: 50px auto;
            background: yellowgreen;
            /* box-shadow:阴影水平位置(可负) 阴影垂直位置(可负) 阴影模糊程度 阴影面积 阴影颜色 阴影位置 (默认在外侧); */
            box-shadow: -30px 20px 20px 10px palegreen;
        }

        section {
            width: 200px;
            height: 200px;
            margin: 0 auto;
            background: #f90;
            border-radius: 50%;
            /* 设置盒子阴影  inset：阴影位置在内侧 */
            box-shadow: 0px 0px 20px 10px #ff0 inset;
        }

        nav {
            width: 200px;
            height: 100px;
            margin: 50px auto;
            background: skyblue;
            /* 设置多个盒子阴影 注意 不建议设置阴影位置 */
            box-shadow: 0px 0px 20px 2px blue, -1px -1px 20px 2px pink, 3px 3px 20px 3px yellow, -3px 4px 20px 5px blueviolet;
        }
    </style>
</head>

<body>
    <div>盒阴影</div>
    <section></section>
    <nav>盒子阴影，可以设置多个颜色，逗号隔开</nav>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649996954163-4a448563-c7fd-495e-b8ac-673ac2701a0d.png#clientId=u57b73542-4855-4&from=paste&height=492&id=u73e54d95&originHeight=734&originWidth=340&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37821&status=done&style=stroke&taskId=u920860c2-9feb-409a-b793-eceb3893540&title=&width=228)
<a name="oGmtF"></a>
# 文字阴影text-shadow
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* 文字阴影 */
        h1{
            /* text-shadow: 阴影水平位置(可负) 阴影垂直位置(可负) 阴影模糊程度 阴影颜色; */
            text-shadow: 0px 1px 2px green;
            /* 文字阴影 也可以设置多个颜色 使用逗号隔开 */
            text-shadow: 0px 0px 2px skyblue,1px 1px 2px #f90,-1px -1px 2px yellowgreen;
        }
    </style>
</head>
<body>
    <h1>文字阴影</h1>
</body>
</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649997265204-2233463c-7274-4496-ae7f-d2ccef981f81.png#clientId=u57b73542-4855-4&from=paste&height=37&id=u5d22fe5e&originHeight=252&originWidth=886&originalType=binary&ratio=1&rotation=0&showTitle=false&size=122350&status=done&style=stroke&taskId=u3d999096-be92-4a53-9faf-7857e8a16ec&title=&width=130.40000915527344)
<a name="lOPTR"></a>
# 矢量图应用

1. 引入对应的 `iconfont.css` 文件 
```html
    <link rel="stylesheet" href="../font矢量图/iconfont.css">
```

2. 设置 `<i>` 标签，两个 `class` 名字
- 一个是 `iconfont`，另一个是你需要的那个图案的`class`名字
```html
<i class="iconfont icon-iconset0330"></i>
```

3. 设置矢量图大小 `font-size`
4. 设置矢量图颜色  `color`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./h5-2202/day999-video、font、统筹css、js/font矢量图/iconfont.css">
    <style>
        li:hover {
            color: red;
            font-size: 20px;
            /* 鼠标滑过文字变大  但是矢量图没有变大 */
        }

        /* 
            * 继承性  元素继承而来的权重是0  
            * 我i本身呢 .iconfont{font-size: 16px;} 16像素   
        */
        li:hover i {
            /* 想要鼠标滑过 矢量图变大 需要设置在i本身上面 此时i权重为12 */
            font-size: 30px;
        }
    </style>
</head>

<body>
    <ul>
        <li><i class="iconfont icon-iconset0330"></i>全部商品</li>
        <li><i class="iconfont icon-taobao"></i>全部商品</li>
        <li><i class="iconfont icon-jitui"></i>全部商品</li>
        <li><i class="iconfont icon-jitui1"></i>全部商品</li>
        <li><i class="iconfont icon-nanbaobao"></i>全部商品</li>
        <li><i class="iconfont icon-nvbaobao"></i>全部商品</li>
        <li><i class="iconfont icon-ertongpiao"></i>全部商品</li>
    </ul>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649997436828-7efd8e07-b22c-47a6-8854-36ef05936daa.gif#clientId=u57b73542-4855-4&from=paste&height=166&id=u7bcd1b9a&originHeight=208&originWidth=306&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112491&status=done&style=stroke&taskId=ueab642c3-3fa4-4598-bc6e-bee633e6d17&title=&width=244.8)
