<a name="x77Sa"></a>

# 一、前端概述

- **什么是前端**
   - 前端开发是从网页制作演变而来，随着互联网的发展，现代网页更佳美观，交互更多，功能更强。因此现在的前端开发可以制作浏览器运行的页面，手机 app，小程序，网页游戏等等。
- **前端需要用到哪些技术？**
   - 基本的就是HTML，CSS，JavaScript
   - 前端框架JQuery，Vue，React等
   <a name="X76ar"></a>
# 二、HTML 简介

- **什么是HTML**
   - HTML 全称是 Hyper Text Markup Language （即超文本标记语言）
- **WEB标准组成**
   - 一个标准的 Web 由三部分组成，即 HTML 、CSS 、Javascript 。分别对应页面的结构、表现 还有 行为
- **W3C**
   - W3C( World Wide Web Consortium )万维网联盟，创建于1994年，是Web技术领域最具权威和影响力的国际中立性技术标准机构；是专门负责网络标准制定的非赢利组织。制定了结构标准和样式标准，保证各种 Web 技术能很好地协同工作
- **文件命名注意事项**
   - 实际开发中文件或文件夹的命名一般包含数字、字母、_ 、- 。不允许包含比如#*等特殊字符，避免空格及中文
- **HTML文件后缀名**
   - .html 或 .htm
   <a name="uBZls"></a>
# 三、HTML 文档结构
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

- `<!DOCTYPE html>`
   - HTML5 的文档声明，指示 web 浏览器关于页面使用哪个 HTML 版本进行编写的指令
- `<html></html>`
   - 根元素
- `<html lang="en"></html>`
   - lang 属性，规定元素内容的语言，中文网站一般使用 `lang = "zh-CN"`
- `<head></head>`
   - 页面的头部，一般包含编码信息、页面标题、关键字、描述等
- `<meta charset="UTF-8">`
   - 编码方式，万国码，支持大部分语言
- `<title></title>`
   - 网页的标题
- `<body></body>`
   - 页面主体，一般包含构建网页的标签
   <a name="vHlza"></a>
# 四、HTML 标签样式分类与属性

- **元素分类**	
   - 封闭类型标签	<body></body>	
   - 非封闭类型标签(空标签,单标签) 	<meta/>
- **元素属性**
   - 属性提供了有关 HTML 元素的更多的信息，元素可以有多个属性，排名不分先后，空格隔开
   - `<div class="box" id="wrap"></div>`
   - `<meta charset="UTF-8">`
   <a name="uPPS9"></a>
# 五、HTML 标签 之 块级元素

- 块级元素特点：独占一行，能设置宽高
1. `**<div></div>**`
   - 用作容器，给页面划分板块
2. **标题元素**
   - 一共 6 个标题元素，标题可以被搜索引擎搜索
   - h1 是页面中最大的标题，只能出现一次，用作网页的标题
   - h2-h6没有次数限制，h2 一般代表页面中大板块标题，h3代表大板块中的小板块标题，h4 比 h3权重还要小
   - 特点：标题默认自带加粗,垂直方向有间距,一级标题最大,六级标题最小
```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

3. **段落元素**`**<p></p>**`
   - 一般包裹一段描述性的文本，比如文章段落，商品描述等
   - 特点：有垂直方向段落间距
4. **列表**
   1. **无序列表**
   - type属性值
      - type="circle" 空心圆
      - type="disc" 默认值,实心圆
      - type="square" 实心矩形
   - 通常列表会用在导航与新闻列表处
```html
<ul type="">
  <li>无序列表1</li>
  <li>无序列表2</li>
  <li>无序列表3</li>
  <li>无序列表4</li>
</ul>
```

   2. **有序列表**
   - type属性值
      - type="1" 默认值，数字
      - type="a" 小写字母
      - type="A" 大写字母
      - type="i"  小写罗马数字
      - type="I"  大写罗马数字
   - start 可以指示从第几个数字或字母开始，值只能是数字
      - `<ol type="a" start="3">` 代表从小写字母 c 开始
```html
<ol type="" start="">
  <li>有序列表1</li>
  <li>有序列表2</li>
  <li>有序列表3</li>
  <li>有序列表4</li>
</ol>
```

   3. **自定义列表**
   - 用法：名词与解释、图文混排
```html
<dl>
  <dt>HTML</dt>
  <dd>HTML也叫超文本标记语言</dd>
</dl>
```

5. **水平分割线 **`**<hr>**`
<a name="Z4Oh8"></a>
# 六、HTML 标签 之 行内元素

- 行内元素特点：逐行排列，个别标签能设置宽高（常见img/input/textarea/select标签可以设置尺寸）
- 行内元素之间不论敲多少回车或者空格，只会被浏览器解析成一个空格
1. **加粗**
   - `<b></b>`
   - `<strong></strong>` 有强调的意思，推荐使用
2. **倾斜**
   - `<i></i>`
   - `<em></em>` 有强调的意思，推荐使用
3. **下划线**
   - `<u></u>`
   - `<ins></ins>` 推荐使用
4. **删除线**
   - `<s></s>`
   - `<del></del>` 推荐使用
   - `<strike></strike>`
5. **上标 <sup></sup>**
6. **下标 <sub></sub>**
7. **文本换行 **`**<br>**`
8. **span**
   - <span></span>用于一大段文本中某一部分字体样式的设置
   - 好处：1.span 包裹的文本前后不换行	2.span 标签本身不带有任何样式
9. **图片  <img src="" alt="" title=""/>**
   - src 属性：引图片路径
   - alt 属性：图片无法正常显示时显示的提示文本
   - title 属性：鼠标移入显示的文本，其他标签也可以使用
   - 图片格式
      - .gif 动图,支持透明
      - .jpg 有损压缩,不支持透明
      - .png 无损压缩,支持透明

![UDJK3(P[1)V20NAY[T]933S.png](https://cdn.nlark.com/yuque/0/2023/png/22608300/1685581551099-45c256cc-173c-462a-bf2f-a08313ad321f.png#averageHue=%23474b41&clientId=uef2c6ca6-4b7e-4&from=paste&height=455&id=u4ed8a8f2&originHeight=909&originWidth=1206&originalType=binary&ratio=2&rotation=0&showTitle=false&size=356389&status=done&style=none&taskId=u678f610b-8be1-4150-bfcd-459f2491e5c&title=&width=603)

10. **超链接  <a href="" target=""></a>**
   - 页面之间的跳转
   - href 属性：引入页面的路径
   - target 属性：页面打开的方式
      - target="_self" 当前页面打开，默认值	
      - target="_blank" 新的标签页打开
- **补充**
   - 元素嵌套原则：块级元素包行内元素，反之不行。块级元素中p标签不能包任何块级元素
```html
<!-- 既是标题有又是超链接 -->
<h2>
  <a href="https://www.baidu.com/">标题</a> 
</h2>
```
<a name="jtcIN"></a>
# 七、路径

1. **绝对路径**：完整的路径
   - C://images/file/girl.png
   - https://
2. **相对路径**
   - ./ 当前目录
   - ../ 返回上一级
3. **根目录**
   - /
   - 例如：`<a href="/11.html">根目录跳转</a>` 看地址栏中显示效果
   <a name="Mhuzg"></a>
# 八、转义字符

- 在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。
| 显示结果 | 描述 | 实体名称 | 实体编号 |
| --- | --- | --- | --- |
|   | 空格 | &nbsp; | &#160; |
| < | 小于号 | &lt; | &#60; |
| > | 大于号 | &gt; | &#62; |
| & | 和号 | &amp; | &#38; |
| " | 引号 | &quot; | &#34; |
| ' | 撇号  | &apos; (IE不支持) | &#39; |
| ￠ | 分（cent） | &cent; | &#162; |
| £ | 镑（pound） | &pound; | &#163; |
| ¥ | 元（yen） | &yen; | &#165; |
| € | 欧元（euro） | &euro; | &#8364; |
| § | 小节 | &sect; | &#167; |
| © | 版权（copyright） | &copy; | &#169; |
| ® | 注册商标 | &reg; | &#174; |
| ™ | 商标 | &trade; | &#8482; |
| × | 乘号 | &times; | &#215; |
| ÷ | 除号 | &divide; | &#247; |

- 更完整的可以参考 [https://www.w3school.com.cn/charsets/ref_html_8859.asp](https://www.w3school.com.cn/charsets/ref_html_8859.asp)

