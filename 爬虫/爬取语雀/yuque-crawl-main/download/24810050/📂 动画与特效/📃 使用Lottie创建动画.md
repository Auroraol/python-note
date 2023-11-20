<a name="mEk0F"></a>
## Lottie简介
[Lottie](https://airbnb.design/lottie/)是一个用于Android，iOS，Web和Windows的库，用于解析使用[Bodymovin](https://github.com/airbnb/lottie-web)导出为json的[Adobe After Effects](http://www.adobe.com/products/aftereffects.html)动画，并在移动设备和网络上呈现它们！<br />![Snipaste_2022-04-06_11-29-46.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649215804381-9a946616-1cf5-4c05-ac06-82befc966a92.png#clientId=ucb2b63ef-5585-4&from=drop&id=ud8c53ec8&originHeight=712&originWidth=1450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14967&status=done&style=none&taskId=u414e8a9b-eeca-4ef2-bc7d-687188da433&title=)

官方文档：<br />[Lottie Docs](https://airbnb.io/lottie/#/web?id=usage)

GitHub：<br />[GitHub - airbnb/lottie-web: Render After Effects animations natively on Web, Android and iOS, and React Native. http://airbnb.io/lottie/](https://github.com/airbnb/lottie-web)

CDN：<br />[bodymovin - Libraries - cdnjs - The #1 free and open source CDN built to make life easier for developers](https://cdnjs.com/libraries/bodymovin)

CodePen示例：<br />[Attention Required! | Cloudflare](https://codepen.io/tag/lottie)

目前，[阿里巴巴图标库](https://www.iconfont.cn/home/index)已经支持Lottie了。<br />![Snipaste_2022-04-06_11-27-09.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1649215667227-0bfb2e49-2f21-4314-93f7-6a43c1906e35.webp#clientId=ucb2b63ef-5585-4&from=drop&id=ua9f05a05&originHeight=947&originWidth=1203&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43838&status=done&style=none&taskId=uc52fe59f-c3cd-4bfc-bd22-b41e11f767b&title=)

<a name="Xor7S"></a>
## 使用AE导出动画
<a name="riRL5"></a>
### 安装插件

1. 安装AE（Adobe After Effect）
2. 安装ZXP，下载地址：[https://aescripts.com/learn/zxp-installer/](https://aescripts.com/learn/zxp-installer/)
3. 安装bodymovin，下载地址：[https://github.com/airbnb/lottie-web/blob/master/build/extension/bodymovin.zxp](https://github.com/airbnb/lottie-web/blob/master/build/extension/bodymovin.zxp)

<a name="KzxWG"></a>
### 配置AE
安装好后，在AE中进行设置：<br />在“编辑 -> 首选项 -> 常规 -> 脚本与表达式”中开启“允许脚本写入文件和访问网络”<br />![Snipaste_2022-04-06_11-18-09.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649215592286-0fe95812-3d33-4ab8-800b-ef8515241f12.png#clientId=ucb2b63ef-5585-4&from=drop&id=u696c3c56&originHeight=688&originWidth=897&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19734&status=done&style=none&taskId=u6cb3804e-bde1-47c3-bdc1-530af080cfa&title=)

<a name="JpKeH"></a>
### 导出json动画文件
在“窗口 -> 扩展 -> Bodymovin”可以导出动画<br />![Snipaste_2022-04-06_11-33-57.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649216055730-a98f4d5d-47d3-4819-83a7-fa1929e0862c.png#clientId=u99f605cb-d132-4&from=drop&id=uc7186610&originHeight=107&originWidth=537&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4644&status=done&style=none&taskId=u77061ab8-bc7f-47cd-aedd-ca8c31f584c&title=)<br />勾选需要导出的动画，设置导出路径，<br />![Snipaste_2022-04-06_11-36-45.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649216215304-26377841-6c99-45d4-9330-ace6b27652c2.png#clientId=u99f605cb-d132-4&from=drop&id=ue2de64ed&originHeight=786&originWidth=1558&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18690&status=done&style=none&taskId=ub6fcf9dc-450e-48ba-aa2e-2b68f98e499&title=)<br />在设置中可以设置导出参数：<br />![Snipaste_2022-04-06_11-38-29.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649216339676-e7b49c6c-aa40-44f2-b298-4ffc6adae413.png#clientId=u99f605cb-d132-4&from=drop&id=u1afec1c4&originHeight=786&originWidth=1558&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28181&status=done&style=none&taskId=ufbeabf9f-6c03-4512-a0c4-321324ec6b7&title=)<br />点击“渲染动画”开始导出<br />![Snipaste_2022-04-06_11-39-22.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649216371771-a6e8129a-fc45-432c-becc-f09aa13304d9.png#clientId=u99f605cb-d132-4&from=drop&id=u364fc7a6&originHeight=786&originWidth=1558&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4978&status=done&style=none&taskId=uaf73de37-ce43-440e-a7c9-01fd2e00615&title=)

导出后，可以看到导出的文件 `data.json`，由于我勾选了“转成Base64”选项，只导出了一个json文件。如果未勾选此选项，会生成一个`images`文件夹，用于存放动画中的图片资源。

实际上，导出的json文件是用来描述动画位置、节点、运动信息的一个文件，可以用Lottie进行加载。

<a name="bJi1W"></a>
## 在Web中使用
<a name="WNqBI"></a>
### 引入
通过CDN引入：
```html
lottie:
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.9.1/lottie.min.js"></script>

lottie-player:
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
```

通过NPM引入：
```html
npm install lottie-web
```

<a name="R7r7D"></a>
### 创建动画
创建动画的方式有两种。

第一种：使用`lottie.min.js`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./lottie.min.js"></script>
</head>
<body>
  <div id="container" style="width: 300px; height: 300px;"></div>
  <script>
    let container = document.querySelector("#container")
    lottie.loadAnimation({
      container: container, // the dom element that will contain the animation
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: './data.json' // the path to the animation json
    });
  </script>
</body>
</html>
```
`lottie.loadAnimation`接收以下参数：

| 名称 | 描述 |
| --- | --- |
| container | 用于渲染的容器，一般使用一个 div 即可 |
| renderer | 渲染器，可以选择 'svg' / 'canvas' / 'html'，个人测试发现 svg 效果和兼容性最好 |
| name | 动画名称，用于 reference |
| loop | 循环 |
| autoplay | 自动播放 |
| path | json 路径，页面会通过一个 http 请求获取 json |
| animationData | json 动画数据，与 path 互斥，建议使用 path，因为 animationData 会将数据打包进来，会使得 js bundle 过大 |


第二种：使用`lottie-player.js`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./lottie-player.js"></script>
</head>
<body>
  <lottie-player src="./data.json" background="transparent" speed="1" style="width: 600px; height: 600px;" loop controls autoplay></lottie-player>
</body>
</html>
```

Lottie拥有加载网络资源的能力，可以直接加载一个来源于网络的json动画：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
</head>
<body>
  <lottie-player src="https://assets8.lottiefiles.com/private_files/lf30_wpyddzzi.json" background="transparent" speed="1" style="width: 600px; height: 600px;" loop controls autoplay></lottie-player>
</body>
</html>
```

<a name="H7Jad"></a>
### 常用方法
使用`lottie.loadAnimation`创建的动画返回一个实例，可以调用以下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| stop | 无 | 停止动画 |
| play | 无 | 播放动画 |
| pause | 无 | 暂停 |
| setSpeed | Number | 设置播放速度，1 表示1倍速度，0.5 表示 0.5倍速度 |
| setDirection | Number | 正反向播放，1 表示 正向，-1 表示反向 |
| goToAndStop | Number, [Boolean] | 跳到某一帧或某一秒停止，第二个参数 iFrame 为是否基于帧模式还是时间，默认为 false |
| goToAndPlay | Number, [Boolean] | 跳到某一帧或某一秒开始，第二个参数 iFrame 为是否基于帧模式还是时间，默认为 false |
| playSegments | Array, [Boolean] | 播放片段，参数1为数组，两个元素为开始帧和结束帧；参数2为，是否立即播放片段，还是等之前的动画播放完成 |
| destroy | 无 | 销毁 |

示例：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./lottie.min.js"></script>
</head>
<body>
  <div id="container" style="width: 300px; height: 300px;"></div>
  <button onclick="play()">播放</button>
  <button onclick="stop()">停止</button>
  <button onclick="pause()">暂停</button>
  <script>
    let container = document.querySelector("#container")
    let anim = lottie.loadAnimation({
      container: container,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: './data1.json'
    });

    function play() {
      anim.play()
    }
    function stop() {
      anim.stop()
    }
    function pause() {
      anim.pause()
    }
  </script>
</body>
</html>
```

<a name="d9ccD"></a>
### 事件监听
可以设置以下事件监听函数：

- `onComplete` 创建时将loop设置为false的时候，播放完后出发
- `onLoopComplete` 单次循环结束触发
- `onEnterFrame` 每进入一帧就会触发，播放时每一帧都会触发一次，stop方法也会触发
- `onSegmentStart` 播放指定片段开始时触发，playSegments、resetSegments等方法刚开始播放指定片段时会发出，如果playSegments播放多个片段，多个片段最开始都会触发。

<br />可以通过 `addEventListener`绑定以下事件：

- `complete`同`onComplete` 
- `loopComplete`同`onLoopComplete` 
- `enterFrame`同`onEnterFrame` 
- `segmentStart`同`onSegmentStart` 
- `config_ready` (when initial config is done)
- `data_ready` 动画json文件加载完毕触发
- `DOMLoaded` 动画相关的dom已经被添加到html后触发
- `destroy`将在动画删除时触发

示例：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./js/lottie.min.js"></script>
</head>
<body>
  <div id="container" style="width: 300px; height: 300px;"></div>
  <button onclick="play()">播放</button>
  <button onclick="stop()">停止</button>
  <button onclick="pause()">暂停</button>
  <div id="loop"></div>

  <script>
    let container = document.querySelector("#container")
    let anim = lottie.loadAnimation({
      container: container,
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: './data/data.json'
    })

    anim.onLoopComplete = function(e) {
      console.log(e)
      document.getElementById("loop").textContent = `播放了${e.currentLoop}次`
      if (e.currentLoop > 3) {
        anim.stop()
      }
    }

    function play() {
      anim.play()
    }
    function stop() {
      anim.stop()
    }
    function pause() {
      anim.pause()
    }
  </script>
</body>
</html>
```
Lottie事件支持事件对象，第28行的事件对象结构如下：
```html
{
  currentLoop: 1, // 当前循环次数
  direction: 1, // 方向
  totalLoops: 73, // 总时长，只在"enterFrame"中有效，
  type: "loopComplete" // 事件类型
}
```
当播放停止后，如果再次开始播放，则`currentLoop`从1重新计数。

<a name="ot539"></a>
## 其他平台相关库

- Vue：[https://github.com/chenqingspring/vue-lottie](https://github.com/chenqingspring/vue-lottie)
- React：[https://github.com/felippenardi/lottie-react-web](https://github.com/felippenardi/lottie-react-web)
- 微信小程序：[https://github.com/wechat-miniprogram/lottie-miniprogram](https://github.com/wechat-miniprogram/lottie-miniprogram)


<a name="SJAoQ"></a>
## 参考资料

- [Lottie中文文档 - 语雀](https://www.yuque.com/lottie/document/readme)
- [Lottie - 轻松实现复杂的动画效果 - 掘金](https://juejin.cn/post/6844903661760413704)



