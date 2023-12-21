<a name="wxjn6"></a>
# 1.HTML5发展史
- HTML5草案的前身名为 Web Applications 1.0，于2004年被WHATWG提出，于2007年被W3C接纳，并成立了新的 HTML 工作团队。
- HTML 5 的第一份正式草案已于2008年1月22日公布。HTML5 仍处于完善之中。然而，大部分现代浏览器已经具备了某些 HTML5 支持。
- 2012年12月17日，万维网联盟（W3C）正式宣布凝结了大量网络工作者心血的HTML5规范已经正式定稿。根据W3C的发言稿称：“HTML5是开放的Web网络平台的奠基石。”
- 2013年5月6日， HTML 5.1正式草案公布。该规范定义了第五次重大版本，第一次要修订万维网的核心语言：超文本标记语言（HTML）。在这个版本中，新功能不断推出，以帮助Web应用程序的作者，努力提高新元素互操作性。
- 本次草案的发布，从2012年12月27日至今，进行了多达近百项的修改，包括HTML和XHTML的标签，相关的API、Canvas等，同时HTML5的图像img标签及svg也进行了改进，性能得到进一步提升。
   - 拓展知识 ：XHTML 可扩展超文本标记语言，并非主流使用，与HTML区别如下
      - XHTML 元素必须被正确地嵌套。
      - XHTML 元素必须被关闭。`<img src=""/>`
      - 标签名必须用小写字母。
      - XHTML 文档必须拥有根元素。
<a name="LqPme"></a>
# 2.兼容

- 支持Html5的浏览器包括Firefox（火狐浏览器），IE9及其更高版本，Chrome（谷歌浏览器），Safari，Opera等；国内的 遨游浏览器（Maxthon），以及基于IE或Chromium（Chrome的工程版或称实验版）所推出的360浏览器、搜狗浏览器、QQ浏览器、猎豹浏览器等国产浏览器同样具备支持HTML5的能力。
<a name="OwV1Z"></a>
# 3.语法

- 内容类型（ContentType）
   - HTML5的文件扩展符与内容类型保持不变，仍然为".html"或".htm"
- DOCTYPE声明
   - 不区分大小写
- 指定字符集编码
   - `<meta charset="UTF-8">`
- 可省略标记的元素
   - 不允许写结束标记的元素：br、col、embed、hr、img、input、、link、meta	
- 可以省略结束标记的元素：
   - li、dt、dd、p、option、colgroup、thead、tbody、tfoot、tr、td、th
- 可以省略全部标记的元素：html、head、body、colgroup、tbody
- 属性值可以使用双引号，也可以使用单引号。
<a name="tdsXC"></a>
# 4.语义化标签

- 在HTML5出来之前，我们用div来表示页面章节，但是这些div都没有实际意义。（即使我们用css样式的id和class形容这块内容的意义）。这些标签只是我们提供给浏览器的指令，只是定义一个网页的某些部分。
<a name="Z65pJ"></a>
## 4.1 语义化标签的优点

   - 即使在没有CSS的支持下，浏览器依然能呈现出良好的内容结构。
   - 有利于SEO，语义化的标签更有利于爬虫去解析更多有效信息。
   - 跨设备体验，不同设备都支持语义化标签，那么即使在不同设备下依然可以有无缝体验。
   - 便于代码开发和维护，语义化可以增加代码的可读性，让团队成员可以更好理解彼此的代码意图。
<a name="nWioz"></a>
## 4.2 HTML5 提供的语义化标签

- section元素 表示页面中的一个区块
   - section标签和div标签不一样，不是用来定义局域样式的，而是用来定义一个明确的主题，通常含有一个标题 h1~h6
- article元素 定义外部的内容
   - 一般是独立的、完整的、摘自外部的内容。它可以是博客文章、新闻文章、论坛帖子、网友评论等独立的内容。
- aside元素 定义主内容之外的相关内容
   - 通常是用来辅助 <article> 标签区域的内容，因此很多人把它定义的区域称为辅助区域。经常被使用来作为侧边栏
- header元素 表示页面的头部，定义文档的页眉（介绍信息）
- footer元素 表示页面的底部，定义文档或节的页脚
- nav元素 表示页面中导航链接部分
   - nav里面可以直接写li
- figure元素 表示一段独立的内容，使用figcaption元素为其添加标题(第一个或最后一个子元素的位置)
- main元素 表示页面中的主要的内容
   - main元素中的内容对于文档来说应当是唯一的。它不应包含在文档中重复出现的内容，比如侧栏、导航栏、版权信息、站点标志或搜索表单。
- hgroup 标题的一个分组
   - 用于对网页或区段（section）的标题进行组合

![1.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1636715562376-55ea6d0f-ce95-4b24-b7c3-d1402f67fcfe.png#averageHue=%23c7a894&clientId=ub385bdef-9825-4&from=ui&id=cuypE&originHeight=592&originWidth=1049&originalType=binary&ratio=1&rotation=0&showTitle=false&size=61321&status=done&style=none&taskId=uec5e9a09-9e96-47c4-a340-e4886cfcfbb&title=)<br />![语义标签.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1636715586759-14614669-bc5d-452d-81b1-8269a48f566f.jpeg#averageHue=%23d4d3d3&clientId=ub385bdef-9825-4&from=ui&id=G1omj&originHeight=598&originWidth=627&originalType=binary&ratio=1&rotation=0&showTitle=false&size=71276&status=done&style=none&taskId=u7d100f83-968c-4522-a2d2-1b2a3d7226f&title=)

<br />
<a name="BKhlg"></a>
# 5.以下 HTML5 标签了解一下吧，几乎不用

- mark 定义高亮显示的文本，定义带有记号的文本
- time 定义时间和日期
- dialog 标记定义一个对话框(会话框) 
- embed 标记定义嵌入的内容或插件，比如flash
- small 呈现小号字体效果，指定细则，输入免责声明、注解、署名、版权
- bdi 允许您设置一段文本，使其脱离其父元素的文本方向设置。在发布用户评论或其他您无法完全控制的内容时，该标签很有用
- big 呈现大号字体效果
- command 表示用户能够调用的命令，只有当 command 元素位于 menu 元素内时，该元素才是可见的。否则不会显示这个元素，但是可以用它规定键盘快捷键
- details 用于描述文档或文档某个部分的细节，和<summary></summary>配合使用
- menuitem 用户可以从弹出菜单调用的命令/菜单项目
- meter 定义已知范围或分数值内的标量测量。也被称为 gauge（尺度）。例如磁盘用量、查询结果的相关性，等等。
- progress 定义运行中的进度（进程）。可以来显示 JavaScript 中耗费时间的函数的进度
- track 为诸如 video 元素之类的媒介规定外部文本轨道。用于规定字幕文件或其他包含文本的文件，当媒介播放时，这些文件是可见的。
- wbr 规定在文本中的何处适合添加换行符
- canvas和svg画图标签重点，需要配合js，后面再学习

<a name="wptHc"></a>
# 6. HTML5 废弃的标签

- basefont 规定页面上的默认字体颜色和字号
- center 将 HTML 网页中的文本进行水平居中处理
- font 规定文本的字体、字体尺寸、字体颜色
- s 不赞成使用，用del代替
- strike 不被赞成使用，用del代替
- tt 呈现类似打字机或者等宽的文本效果
- u 不被推荐使用
- frame 定义 frameset 中的一个特定的窗口（框架）
- frameset 可定义一个框架集。它被用来组织多个窗口（框架）。每个框架存有独立的文档
- noframes 可为那些不支持框架的浏览器显示文本。noframes 元素位于 frameset 元素内部
   - 注：html5中仍然支持**iframe**，iframe标签仍然被广泛应用
   - `<iframe src=""></iframe>` 当面页面嵌套另一个页面
- abbr 取代acronym，用于表示缩写
- object 取代了applet，定义一个嵌入的对象
- ul 取代了dir，定义目录列表
<a name="Bi9rG"></a>
# 7.多媒体标签

- `<video src=""></video> `
- `<audio src=""></audio>`
- 属性
   - controls属性：如果出现该属性，则向用户显示控件，比如播放按钮。
   - autoplay属性：如果出现该属性，则视频在就绪后马上播放。
   - loop属性：重复播放属性。
   - muted属性：静音属性。
   - poster属性：规定**视频**正在加载时显示的图像，直到用户点击播放按钮。
      - 注：属性名和属性值完全相同时，可以简写成一个属性名
- <source> 标签为媒介元素（比如 <video> 和 <audio>）定义媒介资源。<source> 标签允许您规定可替换的视频/音频文件供浏览器根据它对媒体类型或者编解码器的支持进行选择。	
- Type属性值：
   - 用于视频：video/ogg video/mp4 video/webm
   - 用于音频：audio/ogg audio/mpeg
- video支持的视频格式：ogg、mpeg4、webm
- audio支持的音频格式：ogg、mpeg3、wav
```html
<video controls>
	<source src="myvideo.mp4" type="video/mp4"></source>
	<source src="myvideo.ogg" type="video/ogg"></source>
	<source src="myvideo.webm" type="video/webm"></source>
	您的浏览器不支持Video标签
</video>

<audio controls>
    <source src="horse.ogg" type="audio/ogg">
    <source src="horse.mp3" type="audio/mpeg">
    您的浏览器不支持 audio 元素。
</audio>
```
<a name="fvh4O"></a>
# 8.HTML5表单元素

- input 新增 type 类型
   - Type=“email” 限制用户必须输入email类型
   - Type=“url” 限制用户必须输入url类型
   - Type=“range” 产生一个滑动条表单
   - Type=“number”数字类型
   - Type=“search” 搜索意义的表单
   - Type=“color” 颜色选择的表单
   - Type=“time” 时间类型
   - Type=“month” 月类型
   - Type=“week” 周类型
   - Type=“datetime-local” 选取本地时间
   - type=”date”日期
- 新增 input 表单属性
   - required 监测是否为空，默认不填写内容也可以提交
   - min 最小，max 最大，step 步幅
   - list 必须结合datalist标签，绑定datalist 的 id名称。
      - datalist也是 HTML5 新增标签
```html
<input type="url" list="url-lists"/>
<datalist id="url-lists">
  <option value="http://www.baidu.com" label="百度"/>
  <option value="http://www.google.com" label="谷歌" />
  <option value="http://www.jd.com" label="京东" />
</datalist>
```

   - placeholder 文本框、密码框的提示信息
   - autofocus 自动获取焦点，一个页面只能有一个。
   - pattern 属性值是一个正则表达式，用 js 更多
   - novalidate 取消验证，form中的控件哪怕写了required也会取消验证
   - multiple （文件上传）选择多个
   - autocomplete 是否自动提示信息 属性值 on开启、 off关闭
```html
<form action="demo_form.asp" method="get" autocomplete="on">
  First name:<input type="text" name="fname" /><br />
  Last name: <input type="text" name="lname" /><br />
  E-mail: <input type="email" name="email" autocomplete="off" /><br />
  <input type="submit" />
</form>
```

- 新增其他表单标签
   - output 接收计算后的结果
```html
<form action="" oninput="x.value=parseInt(a.value)+parseInt(b.value)">
    <input id="a" type="range" min="0" max="100">100+
    <input id="b" type="text" value="50">=
    <output name="x" for="a b"></output>
</form>
```


   - <br />
   - <br />
