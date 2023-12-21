<a name="LQSFw"></a>
# CSS 样式表
1. 全称
- `cascading style sheets` 层叠样式表
2. 作用
- 让`body`里面的内容有宽度、高度、背景/文字颜色、大小...各种排版样式
- 其实`CSS`就是修饰`body`里面的标签
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        h1 {
            color: green;
        }

        p {
            width: 300px;/* 宽度 有单位 像素px */
            height: 100px;/* 高度 有单位 像素px */
            background-color: pink;/* 背景颜色 */
            color: green;/* 文字颜色 */
        }

        div {
            background-color: red;
            background-color: blue;
            background-color: green;
            color: white;
            color: blue;
            /* 以最后一个口令为主色 */
        }
    </style>
</head>

<body>
    <h1>html学习</h1>
    <p>今天学css</p>
    <p>样式</p>
    <p>基础</p>
    <div>我是什么颜色</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649049361199-f4f8e802-e011-45ea-afce-5d53af20b843.png#clientId=u4190fd32-139d-4&from=paste&height=299&id=u6e195294&originHeight=757&originWidth=578&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18437&status=done&style=stroke&taskId=u00ca5393-35c0-4922-a6ed-326689dbaab&title=&width=228.40000915527344)
<a name="HE7HB"></a>
## 内部样式表

1. 在头部`<head>`内书写
- `<style type="text/css"></style>`
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style type="text/css">
        /* 
        * 这里面是css语法
        * 你要修饰的元素｛
        * 属性:属性值;
        * 属性:属性值;
        * 属性:属性值;
        ｝ 
        */
    </style>
</head>
```

2. 作用域：当前这个页面
3. 快速创建样式表：
- `ul>li{内部样式表的创建}*9` 按`Tab`键
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>内部样式表的创建</title>
    <style type="text/css">
        li {
            color: green;
        }
    </style>
</head>

<body>
    <!-- 快速创建样式表 ul>li{内部样式表的创建}*9 -->
    <ul>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
        <li>内部样式表的创建</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649049464599-292ab26d-b782-4e8b-ab7f-15da08bd6e52.png#clientId=u4190fd32-139d-4&from=paste&height=192&id=u1257d811&originHeight=333&originWidth=283&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45865&status=done&style=stroke&taskId=ubcf2d924-a33e-490d-b743-2a52b2d8a08&title=&width=163.40000915527344)
<a name="X2qKn"></a>
## 行内/内联/内嵌/嵌入样式表

1. `<标签 style="属性:属性值;属性:属性值;">文字内容<标签>`
- **此样式表禁用×，了解就好**
2. 行内样式表是把`CSS`写在人家标签里面
3. 作用域：当下这个标签，写在哪里它就作用于谁
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>行内/内联/内嵌/嵌入样式表</title>
</head>

<body>
    <ul>
        <li>7777777</li>
        <li>7777777</li>
        <li>7777777</li>
        <li style="color:pink">7777777</li>
        <li>7777777</li>
        <li>7777777</li>
        <li>7777777</li>
        <li>7777777</li>
        <li>7777777</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640920977159-c2f2dfdf-86d0-44af-92b8-d05974ae73df.png#clientId=ufc4cb615-1239-4&from=paste&height=174&id=u6618e2eb&originHeight=253&originWidth=144&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2374&status=done&style=stroke&taskId=u4e117aab-7468-4aab-bd1c-256a64457a8&title=&width=99)
<a name="xYl20"></a>
## 外部样式表

1. 引入方法（两种）
- 在头部`<head>`内`<link rel="stylesheet" href="css文件及其路径">`
   - 隶属于`HTML`
   - `link`这种引入方式，是结构和表现同时加载
   - 是`HTML`在很早之前就提出来的，没有兼容性问题，好用
   - 因为是标签，故而，可以使用`JS`控制`CSS`样式
- （了解）`<style>@import url（css文件及其路径）</style>`
   - 隶属于`CSS`
   - `@import`是先让结构加载完毕，再加载`CSS`
   - 存在兼容问题，`IE`低版本不支持
   - 不受`JS`控制
2. 另建`CSS`样式表，命名为`happy.css`
3. 属性
- `rel="stylesheet"`的作用是关联样式表
4. 外部样式表的作用域非常广泛，谁引入，就作用于哪一个页面
- 优点：谁都可以调用，复用性强

![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640929733991-8e00edaa-290f-4375-be64-48a3668954ea.png#clientId=ub45fb59b-61b2-4&from=paste&height=83&id=VOHzG&originHeight=165&originWidth=264&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8996&status=done&style=stroke&taskId=ud75eae6b-0ac5-44cd-b2dc-b88871c831c&title=&width=132)
<a name="iifYh"></a>
### 外部样式表的引入示例
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 
        * 外部样式表的引入
        * <link rel="stylesheet" href="css文件及其路径"> 
    -->
    <link rel="stylesheet" href="../css/happy.css">
</head>

<body>
    <div>111</div>
    <h1>222</h1>
    <p>333</p>
    <p>444</p>
    <p>555</p>
</body>
```
```
你要修饰的元素｛
  属性:属性值;
  属性:属性值;
｝ 
```
```css
p {
    background-color: pink;
}

li {
    background-color: aqua;
}

h1 {
    color: yellow;
    background-color: pink;
}

div {
    width: 400px;
    height: 100px;
    background-color: purple;
}
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640929693585-518b4ba0-3ca3-4d4b-aa77-22f08956b249.png#clientId=ub45fb59b-61b2-4&from=paste&height=183&id=ue78038bc&originHeight=366&originWidth=366&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4733&status=done&style=stroke&taskId=ud0126151-c2c8-4b4d-bfef-df6390605bb&title=&width=183)

5. 拓展：另一种引入方式（写在头部`<head>`内）
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- 
        * 在头部写style
        * <style>
        * @import url(css文件及其路径);
        * </style> 
    -->
    <style>
        @import url(../css/happy.css);
    </style>
</head>

<body>
    <div>6666</div>
</body>
```
<a name="gfYH2"></a>
## 样式表的优先级

1. **行内样式表优先级最大**
2. **外部**样式表和**内部**样式表相比较，和书写顺序有关，**后来居上**，谁书写在后面谁的优先级高一点点，因为代码自**上而下**解析
<a name="CeTEY"></a>
### 验证优先级顺序
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640931534272-07473cad-5fc8-4c8e-9e61-973c46126c2f.png#clientId=ub45fb59b-61b2-4&from=paste&height=142&id=u2d76b3a5&originHeight=283&originWidth=295&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17161&status=done&style=stroke&taskId=u3d28ac7c-83cf-437d-81d0-d1ded75321f&title=&width=147.5)
```html
<head>
    <meta charset="UTF-8">
    <title>样式表的优先级</title>
    <!-- 内部样式表 -->
    <style>
        div {
            background-color: green;
            background-color: red;
        }
    </style>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/demo.css">
</head>

<body>
    <div>我到底会是什么颜色呢</div>
</body>
```
```css
div{
    background-color: pink;
    color: tomato;
}
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640931575117-0b55cbf2-bd0b-411b-80fd-90b4efd8c478.png#clientId=ub45fb59b-61b2-4&from=paste&height=42&id=u004822e3&originHeight=84&originWidth=408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7937&status=done&style=stroke&taskId=ue96a1137-c240-4212-a15a-b659963047d&title=&width=204)
```html
<head>
    <meta charset="UTF-8">    
    <title>样式表的优先级</title>
    <!-- 内部样式表 -->
    <style>
        div {
            background-color: yellow;
            background-color: red;
        }
    </style>
    <!-- 外部样式表的引入 -->
    <link rel="stylesheet" href="../css/demo.css">
</head>

<body>
    <!-- 行内样式表 -->
    <div style="background-color: green;">我到底会是什么颜色呢</div>
    <!-- 外部样式表和内部样式表相比较，和书写顺序有关，后来居上，谁书写在后面谁的优先级高一点点,因为代码自上而下解析 -->
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649052060864-da998c2a-4d9b-41d6-be06-1be27f0cd2e5.png#clientId=u4190fd32-139d-4&from=paste&height=47&id=uc00f85af&originHeight=59&originWidth=382&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6788&status=done&style=stroke&taskId=udc976a27-0743-42b6-9e85-49ac956d6b7&title=&width=305.6)<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649058818415-76e191de-da56-42d5-8716-012e7498c5bc.png#clientId=u4190fd32-139d-4&from=paste&height=497&id=u7dd16231&originHeight=621&originWidth=874&originalType=binary&ratio=1&rotation=0&showTitle=false&size=81076&status=done&style=stroke&taskId=uc73d6e97-0244-4c16-8d6e-b4170ed6720&title=&width=699.2)
<a name="MMDHa"></a>
# 选择器/符
```html
<head>
    <meta charset="UTF-8">
    <title>常见的选择器</title>
    <!-- 外部样式表的创建 -->
    <link rel="stylesheet" href="../css/index.css">
</head>

<body>
    <a href="javascript:;">空链接</a>
    <a href="javascript:;">空链接</a>
    <a href="javascript:;">空链接</a>
    <div>111</div>
    <p id="study">222</p>
    <p class="cc colorred">333</p>
    <p>444</p>
    <p class="cc">555</p>
    <h2>为什么不写h1</h2>
    <h2 class="cc colorred">有一个不成文的规定</h2>
    <h2 class="aa">一个页面只能出现一次h1</h2>
    <ol>
        <li>666</li>
        <li>777</li>
        <li>888</li>
    </ol>
    <ul>
        <li>999</li>
        <li>***</li>
        <li>###</li>
    </ul>
    <b>周一</b>
    <strong>周二</strong>
    <i>周三</i>
    <em>周四</em>
    <span>周五</span>
    <a href="#">锚链接</a>
    <a href="javascript:;">空链接</a>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649059690300-a6633ae9-ffa8-455b-bb74-36016a6abc36.png#clientId=u4190fd32-139d-4&from=paste&height=281&id=Z8XYG&originHeight=585&originWidth=716&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44606&status=done&style=stroke&taskId=u0d8d8483-200a-4a84-bfca-642cb113126&title=&width=343.79998779296875)
<a name="AVTIb"></a>
## 元素选择器

1. 定义
- 代表选中了页面中所有这个元素，一般用于重置某个标签自带的样式
- 比如去除页面所有的超链接下划线 
2. 常见元素选择器：
- `a{}` `span{}` `div{}` `p{}` `li{}`
```css
a {/* 代表选中了页面中所有的超链接 */
    text-decoration: none;/* 去除超链接下划线 */
}
```
<a name="og8qo"></a>
## id 选择器

1. `#你起的id名字{ }`
2. 特点：具有**唯一性**，`id`不可以相同
```css
#study {/* 代表你选中了id名字为study的元素 */
    background-color: purple;
}
```
<a name="ro0QD"></a>
## class 类选择器

1. `.你起的class名字{}`
2. 特点：
- 可以选择一个或者多个元素
```css
.cc {
    background-color: tomato;
}

.aa {/* 代表你选中了class名字为aa的元素 */
    color: royalblue;
}
```

- 注意！一个标签是可以拥有多个`class`的名字的，用空格隔开即可
```html
<div class="a b">
```
```css
.colorred {
    color:seashell
}
```
<a name="F1Sct"></a>
## 通配符选择器

1. 特点：
- 当下只用于去除页面缝隙
- `*`代表页面中所有的元素
```css
* {
    margin: 0;
    padding: 0;
}
```
<a name="KSX0t"></a>
## 包含选择器/后代选择器

1. `A B{}`
- 代表选中了`A`里面的后代元素，`儿子B`、`孙子B`...
```css
ol li {/* 代表选中了ol里面的li们 */
    color: red;
}
```
<a name="HUGxI"></a>
## 群组选择器 

1. 小白 小红 小明 小花{喜欢二狗}
2. 特点：同时选择多个元素，逗号隔开
```css
b,
strong,
i,
em,
span {
    background-color: yellowgreen;
}
```
<a name="OiLLd"></a>
## 伪类选择器（重点）

1. 口诀：捡到一个`l``v`，`H``A`哈一笑
2. **锚链接不可重复**使用此功能设置
- 解决办法：清空缓存
```css
/* 超链接有四个状态 */
a:link {/* 代表超链接初始状态 */
    color: yellow;
}
a:visited {/* 代表超链接被点击过后的状态 */
    color: cyan;
}
a:hover {/* 代表超链接被鼠标滑过的状态 */
    color: pink;
}
a:active {/* 代表超链接被点击时/激活时的状态 */
    color: palegreen;
}
```
<a name="iZrUk"></a>
### :hover
```css
/* 我们平常更愿意这样子写 代表超链接各个状态下文字颜色都是黑色 鼠标滑过是蓝色 */
a {
    color: black;
}

a:hover {
    color: cyan;
}
```
<a name="xbxpr"></a>
### hover 拓展
```css
/* 使用a 控制其他块的样式 */
/* 1、使用a控制a的子元素 b   中间什么都不加  控制子元素 */
.a:hover .b {}
/* 2、使用a控制a的兄弟元素 c(同级元素)   ‘+’ 控制同级元素(兄弟元素) */
.a:hover + .c {}
/* 3、使用a控制a的就近元素d   ‘～’ 控制就近元素   参考day11-CSS3选择器及属性的层级选择器 */
.a:hover ~ .d {}
```
<a name="jsYIr"></a>
### hover 状态

- 注意！**只有超链接**可以使用`a:link`  `a:activite`  `a:visited`
- 其他标签不可以
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <!-- 内部样式的创建 -->
    <style type="text/css">
        /* 
            * 只有超链接可以使用a:link  a:activite  a:visited 
            * 其他标签不可以 
            */
        li:hover {/* 代表鼠标滑过li */
            background-color: cyan;
        }
    </style>
</head>

<body>
    <ul>
        <li>超链接四个状态都有，其他元素只有一个hover可以用</li>
        <li>超链接四个状态都有，其他元素只有一个hover可以用</li>
        <li>超链接四个状态都有，其他元素只有一个hover可以用</li>
        <li>超链接四个状态都有，其他元素只有一个hover可以用</li>
    </ul>
</body>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649060196756-657a1724-2aad-44c4-9621-d37fc9a643bf.gif#clientId=u7b47c5da-be77-4&from=drop&height=90&id=u971974de&originHeight=158&originWidth=701&originalType=binary&ratio=1&rotation=0&showTitle=false&size=118317&status=done&style=stroke&taskId=u22463af7-510f-41a3-80a2-96cf9bcaa63&title=&width=398.4000244140625)
<a name="loOxk"></a>
### 示例-伪类按钮（从中间开始渐变）
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1658813389122-330927a8-22bc-45ca-87fc-8a6bb1638682.gif#clientId=ue2a4c9ac-8e12-4&from=drop&id=u5c529837&originHeight=42&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24922&status=done&style=stroke&taskId=u4c72f6c6-d2db-4d61-85dd-1d587a27fe2&title=)
```html
<button>重置选项</button>
```
```css
button {
    position: relative;
    z-index: 1;
    width: 120px;
    line-height: 35px;
    border: none;
    background: #e1e1e1;
    letter-spacing: 3px;
    font-size: 16px;
    color: #4d4d4d;
    border-radius: 1px;
}

button::after {
    content: "";
    z-index: -1;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    height: 0;
    margin: auto;
    transition: .3s linear;
}

button:hover::after {
    background: #b4282d;
    height: 100%;
}

button:hover {
    color: #fff;
    transition: .3s linear;
}
```

