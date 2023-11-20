<a name="WmfC3"></a>
## NW.js简介
官网：<br />[NW.js](https://nwjs.io/)<br />GitHub：<br />[GitHub - nwjs/nw.js: Call all Node.js modules directly from DOM/WebWorker and enable a new way of writing applications with all Web technologies.](https://github.com/nwjs/nw.js)

nw.js 基于Node.js 和 Chromium ，可以看做是`node-webkit`的缩写，是创建桌面应用的方案之一。相比于Electron，可以直接使用HTML构建应用。

<a name="s1w7y"></a>
## 下载及使用
到 nw.js 官网 [https://nwjs.io/](https://nwjs.io/)，下载最新的应用，有normal版和SDK版，随便下载一个即可。

解压后可以看到以下目录结构：<br />![Snipaste_2022-03-08_10-03-18.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1646705026323-b43cc75f-4c3d-4744-a0ef-27a77c8196e7.png#clientId=u81cf2938-5d01-4&from=drop&id=u06b66e24&originHeight=524&originWidth=298&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7408&status=done&style=none&taskId=u805ac86e-969a-477f-8677-259d6718589&title=)<br />其中：

- `package.json`配置了应用的入口文件
- `src`是我自己创建的，永远存放html源文件
- `nw.exe`是可执行文件

修改 `package.json`配置入口文件：
```json
{
  "name": "这是一个名称",
  "main": "src/index.html",
  "nodejs": true,
  "window": {
    "title": "这是一个标题",
    "toolbar": true,
    "width": 1920,
    "height": 1080,
    "resizable":true,
    "show_in_taskbar":true,
    "frame":true,
    "kiosk":false
  },
  "webkit":{
    "plugin":true
  }
}
```
其中：

- `name`指定应用名称
- `main`指定入口文件
- `window`配置视窗参数

配置好后，创建一个入口文件 `src/index.html`即可。随便输入点内容，双加 `nw,exe`执行即可。

<a name="ia1YD"></a>
## 窗口控制
本来以为会跟浏览器一样，可以通过快捷键来控制窗口，试了才知道，根本不行。

查阅资料，发现`nw.js`可以使用node模块，可以模拟浏览器的控制方式控制窗口。

按照以下快捷键操作进行控制：

- `F5`刷新
- `F11`最大化
- `F12`调出控制台
- `ESC`退出窗口

我们结合浏览器以及node模块引入的写法，可以达到以上控制目的：
```json
let gui = require('nw.gui')
let win = gui.Window.get()
let devToolFlag = false

window.addEventListener('keyup', (e) => {
  // alert(e.keyCode)

  // 按下F11全屏
  if (e.keyCode === 122) {
    win.toggleFullscreen()
  }

  // 按下F12打开控制台
  if (e.keyCode === 123) {
    devToolFlag = !devToolFlag
    if (devToolFlag) {
      win.showDevTools()
    } else {
      win.closeDevTools()
    }
  }

  // 按下F5刷新
  if (e.keyCode === 116) {
    win.reload()
  }

  // 按下ESC关闭窗口
  if (e.keyCode === 27) {
    win.close()
  }
})
```
通过监听键盘抬起事件，判断其 `keyCode`，执行不同窗口操作即可。

:::warning
注意：打开控制台需要SDK版本才支持。
:::

<a name="NQhKa"></a>
## 调用Node.js方法
在`NW.js`中，可以直接调用Node.js的方法。

比如：
```json
	const os = require('os')
	console.log(os)
	alert(os.arch())
	alert(os.version())
```

<a name="Gvly5"></a>
## 生成安装包
通常情况下，直接将整个项目打包为压缩文件，解压后运行 `nw.exe`即可。

如果想打包为安装程序，并生成快捷方式，可以借助WinRAR的自解压程序。


具体操作如下：

1. 改选“创建自解压格式压缩文件”

![Snipaste_2022-04-06_15-30-53.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649230277356-e83b085a-fa0e-450d-8c69-048ece8636c4.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u4ff5be4d&originHeight=438&originWidth=456&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9349&status=done&style=none&taskId=u554ba5fb-2f21-473a-9c3e-5c154bfb37b&title=)

2. 切到“高级”选项卡，点击“自解压选项”

![Snipaste_2022-04-06_15-32-03.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649230353782-d9a84c95-8cd8-4aa6-9b2a-a5cecaab4103.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u56885a01&originHeight=438&originWidth=456&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9002&status=done&style=none&taskId=u83250f41-d7c8-4501-8b5b-39499523f68&title=)

3. 选择“添加快捷方式”

![Snipaste_2022-04-06_15-33-10.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649230402820-99fef681-7f22-4f53-8c33-453e0634cf26.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u3aec7ee7&originHeight=504&originWidth=395&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6145&status=done&style=none&taskId=uf41cc5f5-77d3-4654-9b54-ccf0d4ef4b8&title=)

4. 输入源文件名、快捷方式名等，可以使用相对路径

![Snipaste_2022-04-06_15-34-04.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649230457073-10391eba-ab9c-4918-bede-793ddd05d842.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u8e66fb57&originHeight=422&originWidth=343&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4290&status=done&style=none&taskId=u5078a2e9-75ce-44b1-bf3b-18f8e265591&title=)![Snipaste_2022-04-06_15-36-35.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649230608087-3e8ff914-0408-4488-8636-3d2a1ada5a78.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u8c308aab&originHeight=422&originWidth=343&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4879&status=done&style=none&taskId=ue69b185e-ff0a-41e2-a75f-16e79480db9&title=)

打包好后，生成自解压安装文件：<br />![Snipaste_2022-04-06_15-58-58.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649231956022-bfd70261-0d6c-48c0-bf5e-fefdaab2ed7b.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=ue452916e&originHeight=142&originWidth=124&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2653&status=done&style=none&taskId=u5f209eba-a62c-458c-9a48-23de16eaf65&title=)

安装完成后，会在桌面生成一个快捷方式：<br />![Snipaste_2022-04-06_16-00-42.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649232066870-f42d729a-8bb6-4336-99d1-b1a0a2ca68c5.png#clientId=u4ef5b0dd-1d31-4&from=drop&id=u042a6b4e&originHeight=100&originWidth=81&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3842&status=done&style=none&taskId=u9687e795-6cc9-4b65-b6a1-7a62a657fe8&title=)

如果要指定快捷方式的图标，需要在“快捷方式图标”栏填写图标路径，相对于压缩包项目本身的路径，图标需要为`.ico`扩展名。比如：<br />![Snipaste_2022-04-15_02-56-48.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1649962647946-d8177fc3-4e49-483f-8d55-f92dacf9df1b.webp#clientId=uc200c171-e8b1-4&from=drop&id=u636f491f&originHeight=123&originWidth=107&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2556&status=done&style=none&taskId=ufe6e9c35-3447-4b8a-9c90-38da4a49a98&title=)

解压时注意，需要在当前解压目录建一个文件夹，否则解压后文件会散落到当前目录：<br />![Snipaste_2022-04-15_03-23-08.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649964216275-77c3640d-6e9b-4911-b3bd-887931ab0665.png#clientId=ue52d80af-3d20-4&from=drop&id=ua14a1413&originHeight=391&originWidth=523&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8304&status=done&style=none&taskId=u1feb9e9c-cdca-49d9-92da-dce8f254736&title=)
