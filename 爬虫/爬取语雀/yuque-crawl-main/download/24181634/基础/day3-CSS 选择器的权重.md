<a name="sDab3"></a>
# 权重
<a name="lFaYy"></a>
## 元素选择器  `权重 1`
```css
li { /* 代表选中了页面中所有的li */
    color: cyan;
    color: tomato;
}
```
<a name="zG2kQ"></a>
## class 类选择器  `**权重10**`
```css
/* .你起的class名字{} */
.colorYellow { /* 代表选中了class名字为colorYellow的元素 */
    color: yellow;
}
```
<a name="pyRhn"></a>
## id 选择器  `**权重100**`

- 具有唯一性
```css
/* #你起得id名字{} */
#colorPurple { /* 代表选中了id名字为colorPurple的元素 */
    color: purple;
}
```
<a name="f8Uwz"></a>
## 包含/后代选择器  `**权重相加**`

- 要区分于子选择器
```css
/* ul li{代表选中了ul里面所有li} */
ul li { /* 权重 ul的权重+li的权重 1+1=2 */
    color: seagreen;
}
ul #colorPurple { /* 权重 ul的权重+#colorPurple的权重 1+100=101 */
    color: skyblue;
}
```
<a name="SFO9X"></a>
## 通配符选择器  `**权重小于等于1 [0,1)**`

-  `*{ } `一般只用于去除页面缝隙
```css
* {
    padding: 0;
    margin: 0;
}
```
<a name="scXsY"></a>
## 群组选择器  `**权重各自看各自的 互不干扰**`
```css
/* aa bb cc{学习css} */
p,
div,
#car {/* 权重1,1,100 */
    color: springgreen;
}
```
<a name="vgnyT"></a>
## 伪类选择器  `**权重10**`
```css
li:hover { /* 1+10=11 */
    color: tomato;
}

#colorPurple:hover{ /* 100+10=110 */
    color: violet;
}
```
<a name="WAgMv"></a>
## ！important

- （**禁用×，了解就好**）
```css
        /* 8.!important 权重1000 不可以使用 */
        li{
            color: seagreen!important;
        }
```
<a name="ZzhPh"></a>
## 代码汇总
```html
<head>
    <meta charset="UTF-8">
    <title>css选择器的权重</title>
    <!-- 内部样式表的创建 -->
    <style type="text/css">
        /* 1.元素选择器 权重 1 */
        li {
            /* 代表选中了页面中所有的li */
            color: cyan;
            color: tomato;
        }

        /* 2.class类选择器 权重 10 */
        /* .你起的class名字{} */
        .colorYellow {
            /* 代表选中了class名字为colorYellow的元素 */
            color: yellow;
        }

        /* 3.id选择器 具有唯一性 权重 100 */
        /* #你起得id名字{} */
        #colorPurple {
            /* 代表选中了id名字为colorPurple的元素 */
            color: purple;
        }

        /* 4.包含选择器 也叫后代选择器（区分于子选择器） */
        /* ul li{代表选中了ul里面所有li} */
        ul li {
            /* 权重 ul的权重+li的权重 1+1=2 */
            color: seagreen;
        }

        ul #colorPurple {
            /* 权重 ul的权重+#colorPurple的权重 1+100=101 */
            color: skyblue;
        }

        /* 5.通配符选择器 *{} 一般只用于去除页面缝隙 权重小于等于 1 [0,1) */
        * {
            padding: 0;
            margin: 0;
        }

        /* 6.群组选择器 权重 各自看各自的 互不干扰 */
        /* aa bb cc{学习css} */
        p,
        div,
        #car {
            /* 权重1,1,100 */
            color: springgreen;
        }

        /* 7.伪类选择器 权重 10 */
        li:hover {
            /* 1+10=11 */
            color: tomato;
        }

        #colorPurple:hover {
            color: violet;
        }

        /* 8.!important 权重1000 不可以使用 */
        li {
            color: seagreen !important;
        }
    </style>
</head>

<body>
    <ul>
        <li>CSS选择器权重学习</li>
        <li class="colorYellow" id="colorPurple">CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <li>CSS选择器权重学习</li>
        <p>aa</p>
        <div>bb</div>
        <p id="car">cc</p>
    </ul>
</body>
```
<a name="ySMlf"></a>
## 权重练习
```css
元素选择器       权重1 p{} div{} a{}
class类选择器    权重10 .xxx{}
id选择器         权重100 #xxx{}
包含选择器       权重做加法 父元素 子元素｛｝ ul li{}
群组选择器       权重各自看各自的 互不干扰 i,#dd,.aa{} 1,100,10
通配符选择器     权重小于等于1[0,1) *｛｝
伪类选择器       权重10 a:link{} 任何元素:hover a:active a:visited 
注意！！
a:hover{}        权重11
#cc:hover        权重110
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641264558043-eb204d35-70bb-4c4e-b7cd-931f55fda2aa.png#clientId=u17c62c63-2c72-4&from=paste&height=207&id=u5226af74&originHeight=181&originWidth=355&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42998&status=done&style=stroke&taskId=u4e13f964-8f9d-4b80-a474-26d45ff1fa1&title=&width=405.5)
