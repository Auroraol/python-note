html2canvas官网：<br />[html2canvas - Screenshots with JavaScript](https://html2canvas.hertzen.com/)<br />GitHub：<br />[GitHub - niklasvh/html2canvas: Screenshots with JavaScript](https://github.com/niklasvh/html2canvas)

<a name="dx8Cu"></a>
## 使用html2canvas
安装依赖：
```bash
yarn add html2canvas
```

在Vue中的使用示例：
```html
<template>
  <div class="canvas-app">
    <!-- canvas原内容 -->
    <div class="canvas-content">
      <div class="canvas-content-text">这是文本内容</div>
    </div>
    
    <!-- 按钮 -->
    <div class="canvas-btns">
      <div @click="generatorCanvas">生成海报</div>
    </div>
    
    <!-- canvas生成弹窗 -->
    <div class="canvas-wrap">
      <div class="canvas-wrap-img">
        <img :src="imgUrl" alt="">
      </div>
      <div class="canvas-wrap-content"></div>
    </div>
  </div>
</template>

<script>
  import html2canvas from 'html2canvas';
  export default {
    data() {
      return {
        imgUrl: ''
      }
    },
    methods: {
      generatorCanvas() {
        let ele = document.querySelector('.canvas-content')
        html2canvas(ele, {
          backgroundColor: "#ffffff",
          allowTaint: true,  //开启跨域
          useCORS: true,
          scrollY: 0,
          scrollX: 0,
        }).then(canvas => {
          let wrap = document.querySelector('.canvas-wrap-content')
          wrap.appendChild(canvas);
          this.imgUrl = canvas.toDataURL('image/png');
          // debugger
        });
      }
    }
  };
</script>

<style>
  .canvas-content {
    height: 50px;
    background-color: #0f0;
  }
  .canvas-content-text {
    color: red;
  }
</style>
```
生成后的DOM结构：<br />![Snipaste_2022-04-14_09-54-02.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649901282426-fd1a4e5c-ac00-43ad-94ff-2fd46606d476.png#clientId=ubebaf247-8900-4&from=drop&id=uc38da11d&originHeight=387&originWidth=984&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16886&status=done&style=none&taskId=u199bf53d-d5ec-4af1-b19a-01020a11479&title=)

<a name="sIopF"></a>
## 图片跨域问题
如果是同源的图片路径，像这种，生成海报图片是正常的：
```html
<div class="canvas-content">
  <div class="canvas-content-text">这是文本内容</div>
  <div>
    <img src="/favicon.png" width="100" height="100" alt="">
  </div>
</div>
```

如果是非同源的图片路径，生成海报将报错：
```html
<div class="canvas-content">
  <div class="canvas-content-text">这是文本内容</div>
  <div>
    <img src="https://www.baidu.com/img/flexible/logo/pc/result.png" alt="">
  </div>
</div>
```
点击“生成海报”报跨域问题：<br />![Snipaste_2022-04-14_10-12-43.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649902391232-11c0a93b-4eee-44a7-b83f-a52ab9764fae.png#clientId=ubebaf247-8900-4&from=drop&id=ue750602e&originHeight=70&originWidth=1439&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6295&status=done&style=none&taskId=u207052fb-c969-48f1-b1c0-8a661bc5520&title=)

解决方案有两种，都需要服务端支持。

方法一：服务器设置静态资源响应头 `Access-Control-Allow-Origin`为 `*`或者域名白名单，然后在img标签添加`crossorigin="anonymous"`属性。
```html
<img crossorigin=“anonymous” src="https://www.baidu.com/img/flexible/logo/pc/result.png" alt="">
```

方法二：使用代理服务器获取资源。参考：<br />[GitHub - niklasvh/html2canvas-proxy-nodejs: Express middleware proxy for html2canvas](https://github.com/niklasvh/html2canvas-proxy-nodejs)


<a name="YhIOL"></a>
## 参考资料

- [html2canvas 跨域问题的全方位解读](https://blog.csdn.net/u013140948/article/details/116145382)
- [使用html2canvas在前端生成图片](https://www.jianshu.com/p/22bd5b98e38a)


