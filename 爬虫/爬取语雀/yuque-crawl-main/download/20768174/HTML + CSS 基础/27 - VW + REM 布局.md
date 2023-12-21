<a name="t7mM8"></a>
# 1.什么是vw和vh
- vw：1vw等于视口宽度的1%，100vw等于视口宽度的100%
- vh：1vh等于视口高度的1%，100vh等于视口高度的100%
- vmin：选取vw和vh中最小的那个。
- vmax：选取vw和vh中最大的那个。

![1210235-20170918162831821-1344168854.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637309214367-4061556a-da1e-476f-8e41-e8d7388659ac.jpeg#averageHue=%23f0f0f0&clientId=u2bde4a1a-72d6-4&from=ui&height=281&id=u9dd66d0e&originHeight=586&originWidth=1250&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42396&status=done&style=none&taskId=uf162c151-fc76-490f-8ca4-38f453a89eb&title=&width=600)
<a name="RNubc"></a>
# 2.用vw单位动态改变html的字体大小
```css
/*
	最常见设计稿iphone6/7/8
	100vw = 375px
	html {font-size:100px;}的时候 1rem = 100px,这样方便进行计算
	所以将 100px 根据公式100vw = 375px，转换成 26.67vw
	根元素字体大小就实现了跟随分辨率而变化
*/
html {
	font-size:26.67vw;
}
/*
	但上面的公式等同于在iphone8标准下，字体大小为100px，字体太大了
	设计稿中大部分字体量取的尺寸为24px,量取的尺寸除以2后小数点往前进两位
*/
body {
	font-size:0.12rem;
}
/*
	在这里就不再使用媒体查询动态改变根元素字体大小了，页面中所有元素的尺寸都通过
	量取后，除以2，小数点往前进两位，单位设置为rem即可
*/
.box {
	width:50rem;
  height:50rem;
  font-size:0.14rem;
}
/*等比缩放布局就搞定了~~~*/
```
