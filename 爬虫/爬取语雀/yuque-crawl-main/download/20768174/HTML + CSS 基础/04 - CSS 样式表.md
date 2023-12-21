<a name="NUpsh"></a>
# 一、CSS 概述
- CSS(cascading style sheet) 汉译为层叠样式表,是用于控制网页样式
- CSS优势
   - 弥补html语言的不足
   - 缩减页面代码，提高访问速度
   - 代码减少，页面文件就会小，占用网络带宽就少，客户端打开速度就快，用户体验就会更好
   - 结构清晰，有利于seo优化
   - 缩短改版时间
   - 对网站的重构有很好的支持
   <a name="GgGAQ"></a>
# 二、CSS 语法

- CSS语法由两部分组成：选择器、样式声明。
   - 样式声明包括：属性和属性值
   - 选择符 {属性: 属性值 ;属性:属性值}
- 基础的CSS样式
   - 宽度 width:200px;
   - 高度 height:200px;
   - 字体颜色 color:red;
   - 背景颜色 background-color:yellow;
- CSS 特点
   - 1）每个CSS样式由两部分组成，即选择符和声明，声明又分为属性和属性值；
   - 2）属性必须放在花括号中，属性与属性值用冒号连接。
   - 3）每条声明用分号结束。
   - 4）当一个属性有多个属性值的时候，属性值与属性值不分先后顺序,用空格隔开。
   - 5）在书写样式过程中，空格、换行等操作不影响属性显示。
   <a name="EdjED"></a>
# 三、CSS 样式表分类
<a name="jU6aV"></a>
## 1.内部样式表

- 语法：在`<head></head>`标签中引入一个`<style></style>`标签
```html
<style type="text/css">
  css语句 
</style>
```
注：使用style标记创建样式时，最好将该标记写在<head></head>中;
<a name="RMtNZ"></a>
## 2.外部样式表

- 语法：`<link rel="stylesheet" type="text/css" href="目标文件的路径及文件名全称" />`
- 使用 link 元素导入外部样式表时，需将该元素写在文档头部，即<head>与</head>之间。
   - rel：用于定义文档关联，表示关联样式表；
   - type：定义文档类型；
- 在外部css样式表最顶部添加 `@charset"utf-8";` 防止css中存在中文而产生的乱码问题
<a name="Va9YD"></a>
## 3.行内样式/内联样式
```html
<div style="width: 200px;height: 200px;background-color: yellow;">这是第一个div</div>
```
<a name="nVIIu"></a>
## 4.扩展：@import方法

```html
<style type="text/css">
  @import  url("目标文件的路径及文件名全称");
</style>
```
面试题：link 与 @import 方法的区别

1. 老祖宗的差别：link属于XHTML标签，而@import完全是CSS提供的一种方式。 link标签除了可以加载CSS外，还可以做很多其它的事情，比如定义RSS，定义rel连接属性等，@import就只能加载CSS。
2. 加载顺序的差别：当一个页面被加载的时候（就是被浏览者浏览的时候），link引用的CSS会同时被加载，而@import引用的CSS 会等到页面全部被下载完再被加载。所以有时候浏览@import加载CSS的页面时开始会没有样式。
3. 兼容性的差别。：@import是CSS2.1提出的，所以老的浏览器不支持，@import只在IE5以上的才能识别，而link标签无此问题。
4. 使用dom控制样式时的差别：当使用javascript控制dom去改变样式的时候，只能使用link标签，因为@import不是dom可以控制的。
<a name="je46T"></a>
# 四、CSS的层叠性

- CSS三大特性-继承性、层叠性、优先级
- CSS层叠性指多种CSS样式的叠加
   - 是浏览器处理冲突的一个能力，只有在多个选择器选中"同一个标签", 然后又设置了"相同的属性", 才会发生层叠性。层叠性由优先级决定。
- CSS层叠性原则：
   - 样式冲突，选择器权值相同遵循就近原则，选择器权值不同则应用权值大的
   - 样式不冲突，属性都会生效
