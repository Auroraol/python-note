<a name="RXRNs"></a>
#  1.字号
-  `font-size:20px;`
- 浏览器默认字体大小16px,浏览器允许设置的最小字体是12px
- em和rem的区别
   - em：父元素字体大小的倍数
   - rem：根元素字体大小的倍数
<a name="k0gRn"></a>
# 2.字体类型

- `font-family:"微软雅黑",Arial,"Times New Roman";`
   - 浏览器首先会寻找字体1、如存在就使用改字体来显示内容，如在字体1不存在的情况下，则会寻找字体2，如字体2也不存在，按字体3显示内容，如果字体3 也不存在；则按系统默认字体显示；
   - 当字体是中文字体时，需加双引号。当英文字体中有空格时，需加双引号如（“Times New Roman”）。当英文字体只有一个单词组成是不加双引号；如：（Arial）。
- Windows中文版本操作系统下，中文默认字体为宋体或者新宋体，英文字体默认为Arial.
<a name="FSX9e"></a>
# 3.字体颜色

- `color:#e3393c;`
   - 用十六进制(是计算机中数据的一种表示方法)表示颜色值：
      - 0 1 2 3 4 5 6 7 8 9 A B C D E F
   - 当表示三原色的三组数字同时相同时，可以缩写为三位;
      - #aabbcc 可以简写为 #abc
- `color:rgb(227,57,60);`
   - 光色模式
   - 每一位的范围是0-255
- 常用颜色值
   - 黑色：#000000 ，#000， rgb(0,0,0)
   - 白色：#ffffff ，#fff ，rgb(255,255,255)

![QQ图片20230518150944.jpg](https://cdn.nlark.com/yuque/0/2023/jpeg/22608300/1684393963052-e7a49416-6c5c-4d85-88a4-ca9d02071979.jpeg#averageHue=%238a9a8b&clientId=ueec5aef1-e7a0-4&from=paste&height=349&id=u70b8cf8c&originHeight=557&originWidth=628&originalType=binary&ratio=2&rotation=0&showTitle=false&size=77948&status=done&style=none&taskId=u443af8fe-fc32-4fca-9981-22b1b8afe87&title=&width=393)
<a name="k34lb"></a>
# 4.字体粗细

- font-weight:normal正常 / bold加粗 / 100-900之间的整数,不带单位;
- 在css规范中，把字体的粗细分为9个等级，分别为100-900，其中100对应最轻的字体变形，而900对应最重的字体变形。100-400 细 ，500常规， 600-900加粗字体。
<a name="qFX30"></a>
# 5.字体倾斜

- `font-style:italic / oblique;`
- italic和oblique都是向右倾斜的文字, 但区别在于Italic是指斜体字，而Oblique是倾斜的文字，对于没有斜体的字体应该使用Oblique属性值来实现倾斜的文字效果。
<a name="pRgUT"></a>
# 6.字体线条修饰

- text-decoration:none无线条 / underline下划线 / line-through删除线 / overline上划线;
```css
a {
   text-decoration: none;
   color: #000;
}
a:hover {
  text-decoration: underline;
  color: #f00;
}
```
<a name="wXJUb"></a>
# 7.首行缩进

- `text-indent:2em;`
   - text-indent可以取负值；
   - text-indent属性只对第一行起作用。
<a name="bfC8p"></a>
# 8.行高

- `line-height:`
   - 单行文本所占高度
- 重要用法：单行文本垂直居中
   - 字体的行高设置为容器的高度即可
<a name="lMWYc"></a>
# 9.字间距

-  `letter-spacing:10px;`
<a name="Qbqxj"></a>
# 10.词间距

- `word-spacing:10px;`
<a name="mwuWr"></a>
# 11.文本和图片的水平对齐方式

- text-align:left左对齐 / right右对齐 / center居中 / justify两端对齐;
   - *** img的水平居中属性要设置给img的容器，而不是img本身
   - justify两端对齐一般用在中英文混合情况下，右侧对不齐的情况
<a name="VHYDo"></a>
# 12.垂直对齐方式? 

- vertical-align:top顶部 / bottom底部 / middle垂直居中 / baseline默认值,基线对齐;
-  一般我们会去掉所有img的基线对齐,如果不去掉,img的下方会存在3-6px间距
```css
img {
  vertical-align: middle;
}
/*或者*/
img {
  display:block;
}
```

- 单元格 td 可以设置内容垂直对齐方式
<a name="qcidC"></a>
# 13.font的简写形式

- font:bold italic 12px/1.5em "宋体"; 
- 分别对应五个属性：
   1. font-weight:bold; 文本加粗
   2. font-style:italic; 文本倾斜
   3. font-size:12px; 字号
   4. line-height:1.5em; 行高
   5. font-family:"宋体"; 
- font简写形式至少要包含字号和字体;

