官网：<br />[Emmet Documentation](https://docs.emmet.io/)

Cheat Sheet：<br />[Cheat Sheet](https://docs.emmet.io/cheat-sheet/)

<a name="f2b0b493"></a>
## 语法
<a name="068430a3"></a>
### 子节点 `>`

-  `nav>ul>li` 
```html
<nav>
	<ul>
        <li></li>
	</ul>
</nav>
```

<a name="e62f4380"></a>
### 兄弟节点 `+`

-  `div+p+bq` 
```html
<div></div>
<p></p>
<blockquote></blockquote>
```

<a name="64b4da52"></a>
### 父级节点 `^`

-  `div+div>p>span+em^bq` 
```html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```

-  `div+div>p>span+em^^bq` 
```html
<div></div>
<div>
	<p><span></span><em></em></p>
</div>
<blockquote></blockquote>
```

<a name="2eea6bb5"></a>
### 分组 `()`

-  `div>(header>ul>li*2>a)+footer>p` 
```html
<div>
  <header>
    <ul>
      <li><a href=""></a></li>
      <li><a href=""></a></li>
    </ul>
  </header>
  <footer>
    <p></p>
  </footer>
</div>
```

-  `(div>dl>(dt+dd)*3)+footer>p` 
```html
<div>
  <dl>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
    <dt></dt>
    <dd></dd>
  </dl>
</div>
<footer>
  <p></p>
</footer>
```

<a name="9debd3ce"></a>
### 乘法 `*`

-  `ul>li*5` 
```html
<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>
```

<a name="2121510f"></a>
### 序号 `$`

-  `ul>li.item$*5` 
```html
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
</ul>
```
<br />`$` 序号默认是递增的 

-  `h$[title=item$]{Header $}*3` 
```html
<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
```
<br />序号可以在多个位置使用 

-  `ul>li.item$$$*5` 
```html
<ul>
  <li class="item001"></li>
  <li class="item002"></li>
  <li class="item003"></li>
  <li class="item004"></li>
  <li class="item005"></li>
</ul>
```
<br />`$$` 表示两位数<br />`$$$` 表示三位数 

-  `ul>li.item$@3*5` 
```html
<ul>
  <li class="item3"></li>
  <li class="item4"></li>
  <li class="item5"></li>
  <li class="item6"></li>
  <li class="item7"></li>
</ul>
```
<br />`$@n` 表示从序号几开始 

-  `ul>li.item$@-*5` 
```html
<ul>
  <li class="item5"></li>
  <li class="item4"></li>
  <li class="item3"></li>
  <li class="item2"></li>
  <li class="item1"></li>
</ul>
```
<br />`$@-` 表示递减 

<a name="1dcb12ae"></a>
### ID `#` 和 CLASS `.`

-  `#header` 
```html
<div id="header"></div>
```

-  `.title` 
```html
<div class="title"></div>
```

-  `form#search.wide` 
```html
<form id="search" class="wide"></form>
```

-  `p.class1.class2.class3` 
```html
<p class="class1 class2 class3"></p>
```

<a name="9a7ca835"></a>
### 属性 `[]`

-  `p[title="Hello world"]` 
```html
<p title="Hello world"></p>
```

-  `td[rowspan=2 colspan=3 title]` 
```html
<td rowspan="2" colspan="3" title=""></td>
```

-  `[a='value1' b="value2"]` 
```html
<div a="value1" b="value2"></div>
```

<a name="efc4b1e1"></a>
### 内容 `{}`

-  `a{Click me}` 
```html
<a href="">Click me</a>
```

-  `p>{Click }+a{here}+{ to continue}` 
```html
<p>Click <a href="">here</a> to continue</p>
```

<a name="31fbbf75"></a>
### 隐含标签
在一些特定情况下使用类名，可以生成隐含标签

-  `.class`
```html
<div class="class"></div>
```

-  `em>.class` 
```html
<em><span class="class"></span></em>
```

-  `ul>.class` 
```html
<ul>
	<li class="class"></li>
</ul>
```

-  `table>.row>.col` 
```html
<table>
  <tr class="row">
    <td class="col"></td>
  </tr>
</table>
```

完整的语法请查看：<br />[cheatsheet-a5.pdf](https://www.yuque.com/attachments/yuque/0/2022/pdf/2213540/1670986325726-7ddce2a4-9fd5-48e6-aae9-0ab00f42d62e.pdf)



