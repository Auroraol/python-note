> **提示**<br />字体图标：微信小程序和Android端不支持本地字体图标。


> **解决方案**<br />替代方式1：不用图标改用图片，但失去了矢量和方便高亮变色的好处<br />替代方式2：字体文件放到服务器，从网络地址引用<br />替代方式3：将字体图标转换为base64格式字符串直接放到css里


> **特别注意**<br />对于首页底部的原生tab，是在pages.json里配置，微信只支持图片不支持其他任何形式


其实, 如果只是H5端的话, 使用字体图标会跟普通的Web开发一样, 非常简单, 但是如果涉及到小程序端的话, 使用这种方式就会出问题, 总结一下

<a name="9e6157b0"></a>
## 在H5端使用字体图标
<a name="c607fed2"></a>
### 使用Font Class
就很正常地使用, 首先下载阿里巴巴图标库到静态目录文件夹，在 `main.js` 中引入：
```javascript
import("@/static/iconfont/iconfont.css")
```

或在 `App.vue` 的 style 中引入：
```css
@import "./static/iconfont/iconfont.css";
```

在组件中使用：
```pug
.main
  .iconfont.icon-xxx
```

通过这种方式，图标为纯色，可以通过css修改图标的颜色和大小：
```css
.iconfont
	font-size: 16rpx
	color: #f00
```

当然，也可以在`public/index.html`中引入线上图标：
```html
<script src="https://at.alicdn.com/t/font_1830168_xxx.css"></script>
```

<a name="91857576"></a>
## 使用Symbol
在 `main.js` 中引入：
```javascript
import("@/static/iconfont/iconfont.js")
```

或在 `App.vue` 的 style 中引入
```javascript
import("./static/iconfont/iconfont.js")
```

在组件中使用：
```pug
.main
  svg.svg-icon: use(xlink:href="#icon-xxx")
```

通过这种方式，图标为纯色，可以直接设置图标大小。如果想要修改图标颜色，可以先到阿里巴巴图标库中去色：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596618380493-af9852dd-ccb5-4918-802d-6ae1cac99892.png#height=301&id=b7yDT&originHeight=301&originWidth=1009&originalType=binary&size=0&status=done&style=none&width=1009)

然后通过css修改图标的颜色和大小：
```css
.svg-icon
  width: 1em;
  height: 1em;
  font-size 24rpx
  color #f00
  fill: #f00;
```

当然，也可以在`public/index.html`中引入线上图标：
```html
<script src="https://at.alicdn.com/t/font_1830168_xxx.js"></script>
```

<a name="bb99997c"></a>
## 封装组件使用
封装一个vue组件，使用的时候调用这个vue组件即可（参考了 uni-icons 的实现）
```vue
<template>
  <text :style="{ color: color, 'font-size': size + 'px' }" class="iconfont" @click="_onClick">{{icons[type]}}</text>
</template>

<script>
  import icons from './icons.js';
  export default {
    name: 'UniIcons',
    props: {
      type: {
        type: String,
        default: ''
      },
      color: {
        type: String,
        default: '#333333'
      },
      size: {
        type: [Number, String],
        default: 16
      }
    },
    data() {
      return {
        icons: icons
      }
    },
    methods: {
      _onClick() {
        this.$emit('click')
      }
    }
  }
</script>

<style lang="stylus" scoped>
version = 0.8
baseUrl = './'
ttf = baseUrl + 'iconfont.ttf?v=' + version
eot = baseUrl + 'iconfont.eot?v=' + version
svg = baseUrl + 'iconfont.svg?v=' + version

@font-face
  font-family: "iconfont"
  src: url(ttf) format('truetype'),
    url(svg) format('svg'),
    url(eot) format('embedded-opentype')

.iconfont
  font-family: "iconfont" !important
  font-size 16px
  font-style normal
  text-decoration: none;
  text-align: center;
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
</style>
```

在同名目录下创建一个 `icons.js`, 其key-value是对应的字体图标的Unicode值：
```javascript
export default {
  'icon-phone': '\ue68b',
}
```

在vue中使用的时候：
```vue
<template lang="pug">
.main
  .icon: iconFont(type="phone")
</template>

<script>
import iconFont from '@/library/iconfont/index.vue'
export default {
  components: {
    iconFont
  },
}
</script>
```

<a name="fd921d2c"></a>
## 使用 uni-icons 引入
当然，也可以直接通过 uni-icons 引入：
```vue
<template lang="pug">
.main
  uniIcon.iconfont.icon-phone(size="30")
</template>

<script>
import uniIcon from '@dcloudio/uni-ui/lib/uni-icons/uni-icons.vue'
export default {
  components: {
    uniIcon
  },
}
</script>
```

<a name="2f58b00d"></a>
## 使用网络字体
经测试，目前这种方式在小程序和Android端中才能够正常显示：
```javascript
version = 0.8
baseUrl = 'https://at.alicdn.com/t/'
ttf = baseUrl + 'iconfont.ttf?v=' + version
eot = baseUrl + 'iconfont.eot?v=' + version
svg = baseUrl + 'iconfont.svg?v=' + version

@font-face
  font-family: "iconfont"
  src: url(ttf) format('truetype'),
       url(svg) format('svg'),
       url(eot) format('embedded-opentype')

.iconfont
  font-family: "iconfont" !important
  font-size 16px
  font-style normal
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale

.icon-phone:before
  content: "\e60a"
```

这样可以通过 Unicode 或类名创建字体图标：
```pug
.main
  .iconfont &#xe60a
  .iconfont.icon-phone
```

> **提示**<br />在APP端，要使网络字体生效，必须加上 `https://`，如果只是网页的话，可以只写`//`。


<a name="0862dbe6"></a>
## 使用base64
可以将woff2字体文件进行base64本地化（其实阿里巴巴图标库自带了base64版），这种方式小程序也是支持的，比如：
```html
<span class="iconfont icon-phone"></span>
<span class="iconfont">&#xe748</span>
```

```css
@font-face {font-family: "iconfont";
  src: url('data:application/x-font-woff2
charset=utf-8;base64,d09GMgABAAAAAAbAAAsAAAAADOAAAAZyAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHEIGVgCEJgqLMIh+ATYCJAMsCxgABCAFhG0HfRvLCiOSUc4Dyf5ZYLdRj5CEpkmhUGAm8IR9nyVdPLW8tg+KwYd+cK/JedLoQTz5V9Xr7o/pntkZRwc4ArhQdFIKhnBGRc6FbKXo+OcYXboY/mhcATMWL2kK0XmBLCTsyg0FGGiKjfKQNYlDsC1gjXDFGXxfyWZe/2Ly8f73WART3aSSPMYnMIw+XxKxgfKdaIC1XR2jHBnWJOuC7dpDc+ITX98dHWVIPx3gU36Ddv1RufyLE3PinyYLGIqUKrBQAA') format('woff2');
}
.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.icon-phone:before {
  content: "\e748";
}
```

<a name="35808e79"></a>
## 参考资料

- [uni-app如何引入iconfont图标](https://ask.dcloud.net.cn/question/57433)

