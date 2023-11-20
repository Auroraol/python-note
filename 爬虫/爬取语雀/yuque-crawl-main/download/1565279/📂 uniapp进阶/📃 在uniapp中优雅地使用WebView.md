<a name="2a6e7e45"></a>
## 从webview页面传值到uniapp中

官方文档已经很详细了，首先在webview页面中引入相关依赖：

```html
<!-- uniapp各平台依赖 -->
<script type="text/javascript">
  var userAgent = navigator.userAgent;
  if (userAgent.indexOf('AlipayClient') > -1) {
    // 支付宝小程序的 JS-SDK 防止 404 需要动态加载，如果不需要兼容支付宝小程序，则无需引用此 JS 文件。
    document.writeln('<script src="https://appx/web-view.min.js"' + '>' + '<' + '/' + 'script>');
  } else if (/QQ/i.test(userAgent) && /miniProgram/i.test(userAgent)) {
    // QQ 小程序
    document.write('<script type="text/javascript" src="https://qqq.gtimg.cn/miniprogram/webview_jssdk/qqjssdk-1.0.0.js"><\/script>');
  } else if (/miniProgram/i.test(userAgent)) {
    // 微信小程序 JS-SDK 如果不需要兼容微信小程序，则无需引用此 JS 文件。
    document.write('<script type="text/javascript" src="https://res.wx.qq.com/open/js/jweixin-1.4.0.js"><\/script>');
  } else if (/toutiaomicroapp/i.test(userAgent)) {
    // 字节跳动小程序 JS-SDK 如果不需要兼容字节跳动小程序，则无需引用此 JS 文件。
    document.write('<script type="text/javascript" src="https://s3.pstatp.com/toutiao/tmajssdk/jssdk-1.0.1.js"><\/script>');
  } else if (/swan/i.test(userAgent)) {
    // 百度小程序 JS-SDK 如果不需要兼容百度小程序，则无需引用此 JS 文件。
    document.write('<script type="text/javascript" src="https://b.bdstatic.com/searchbox/icms/searchbox/js/swan-2.0.18.js"><\/script>');
  }
</script>
<!-- uni 的 SDK -->
<script type="text/javascript" src="https://js.cdn.aliyun.dcloud.net.cn/dev/uni-app/uni.webview.1.5.2.js"></script>
```

然后通过`uni.postMessage`向uniapp传值：

```javascript
  document.addEventListener('UniAppJSBridgeReady', function() {
    uni.postMessage({
      data: {
        action: 'message'
      }
    });

    uni.getEnv(function(res) {
        console.log('当前环境：' + JSON.stringify(res));
    });
  });
```

在uniapp中监听message：

```vue
<template lang="pug">
  view
    web-view.webview(:src="url" @message="getMessage")
</template>

<script>
  export default {
    data() {
      return {
        url: "https://zys201811.boringkiller.cn/shianonline/webview/vod.html?data=123",
      }
    },
    methods: {
      getMessage(event) {
        let data = event.detail.data
        console.log(data);
      }
    }
  }
</script>

<style lang="stylus" scoped>
$webviewHeight = 420rpx
.webview
  width 750rpx
  height $webviewHeight
</style>
```

<a name="2165d829"></a>
## 从uniapp中动态传值到webview页面

按照官方文档，从uniapp传值到webview中，只能通过query：

```vue
<template lang="pug">
  view
    <!-- #ifdef APP-PLUS -->
    web-view.webview(:src="url")
    <!-- #endif -->
</template>

<script>
  export default {
    data() {
      return {
        url: "https://zys201811.boringkiller.cn/shianonline/webview/vod.html?data=123",
      }
    }
  }
</script>

<style lang="stylus" scoped>
$webviewHeight = 420rpx
.webview
  width 750rpx
  height $webviewHeight
</style>
```

在webview中解析query：

```javascript
let data = getQuery('data')
console.log(data);  // 获取 uni-app 传来的值

// 取url中的参数值
function getQuery(name) {
    // 正则：[找寻'&' + 'url参数名字' = '值' + '&']（'&'可以不存在）
    let reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    let r = window.location.search.substr(1).match(reg);
    console.log(r);
    if(r != null) {
        // 对参数值进行解码
        return decodeURIComponent(r[2]);
    }
    return null;
}
```

但是，我们发现，通过向web-view的src中传值，只能传一次，如果参数改变了，没法动态传到webview。

对于这种需要动态传递参数的需求，我们可以使用动态创建webview达到目的，而不是通过webview组件。

实现如下：

```vue
<template lang="pug">
  view
</template>

<script>
  export default {
    data() {
      return {
        url: "https://zys201811.boringkiller.cn/shianonline/webview/vod.html",
      }
    },
    mounted() {
      // #ifdef APP-PLUS
      var w = plus.webview.create(this.url + '?data=good');
      w.show();

      setTimeout(() => {
        plus.webview.close(w);
        setTimeout(() => {
          w = plus.webview.create(this.url + '?data=123');
          w.show();
        }, 1000)
      }, 1000)
      // #endif
    }
  }
</script>
```

以上，通过`plus.webview.create`创建一个webview，然后显示。如果数据更新了，可以先关闭之前的一个webview，然后重新创建一个，再显示。

也可以直接使用open刷新页面：

```javascript
// #ifdef APP-PLUS
var w = plus.webview.open(this.url + '?data=good');
setTimeout(() => {
    w = plus.webview.open(this.url + '?data=123');
}, 1000)
// #endif
```

相关API：

```javascript
// 创建窗口
WebviewObject plus.webview.create( url, id, styles, extras );

// 创建并打开窗口
WebviewObject plus.webview.open( url, id, styles, aniShow, duration, showedCB );

// 显示窗口
void plus.webview.show( id_wvobj, aniShow, duration, showedCB, extras );

// 隐藏窗口
void plus.webview.hide( id_wvobj, aniHide, duration, extras );

// 关闭窗口
void plus.webview.close( id_wvobj, aniClose, duration, extras );
```

<a name="1588064d"></a>
## 调用webview中的evalJs方法

动态传值还有一种解决方案，就是通过`evalJs`方法直接调用webview中方法。

具体实现如下：

在模板中，通过ref暴露web-view元素：

```vue
<template lang="pug">
  web-view(:src="url" ref="wb")
</template>
```

在mounted生命周期的时候获取此元素：

```javascript
// #ifdef APP-PLUS
this.wb = this.$refs.wb
// #endif
```

在需要调用webview中方法的时候使用`evalJs`：

```javascript
// #ifdef APP-PLUS
this.wb.evalJs(`showAlert(${this.num})`)
// #endif
```

在webview页面定义对应的方法即可：

```javascript
function showAlert(num) {
  alert(num)
}
```

从uniapp动态传值，可以使用这种方式。

注意：

1. 在nvue中，只有通过ref暴露webview节点才能拿到webview本身
2. 注意`evalJs`的拼写方式，官方文档是`evalJS`，但通过ref获取时，`S`应该为小写

<a name="35808e79"></a>
## 参考资料

- [uniapp web-view](https://uniapp.dcloud.io/component/web-view)
- [h5+ webview](https://www.html5plus.org/doc/zh_cn/webview.html)
- [uniapp 窗体](https://uniapp.dcloud.io/api/window/window)
- [uni-app中如何使用5+的原生界面控件（包括map、video、livepusher、barcode、nview）](https://ask.dcloud.net.cn/article/35036)
- [在web-view加载的本地及远程HTML中调用uni的API及网页和vue页面通讯](https://ask.dcloud.net.cn/article/35083)
- [封装一个简单实用的 plusready 方法](https://ask.dcloud.net.cn/article/34922)
- [plus.webview.create()创建的webview 怎么接受网页发送的postMessage数据？](https://ask.dcloud.net.cn/question/93615)
