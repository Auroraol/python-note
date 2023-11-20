webview类似于网页中的iframe，开发过Android、iOS的童鞋肯定知道。简单理解就是，在VSCode中，在宿主扩展中嵌入一个网页。

<a name="YdMtK"></a>
## 创建Webview
在package.json中注册命令和在main中引入就不赘述了。直接上一个创建webview的代码：
```javascript
const vscode = require('vscode');

module.exports = function(context) {
  context.subscriptions.push(vscode.commands.registerCommand('vscode-extension-test.openWebview', function (uri) {
    const panel = vscode.window.createWebviewPanel(
        'testWebview', "WebView Test", vscode.ViewColumn.One, {
            enableScripts: true,
            retainContextWhenHidden: true,
        }
    );
    panel.webview.html = `<html><body>Hello Webview</body></html>`
  }))
}
```
说明如下：

- 通过 `vscode.window.createWebviewPanel` 创建一个webview
- `createWebviewPanel` 的第一个参数表示“视图类型”，第二个参数表示“视图标题”，第三个参数表示“显示在编辑器的哪个位置”，第四个参数为其他的一些配置选项
- 配置选项中：
   - `enableScripts: true` 启用JS，默认为false。默认情况下，在Web视图中禁用`JavaScript`，但可以通过传入`enableScripts: true` 选项启用；
   - `retainContextWhenHidden: true` webview被隐藏时保持状态，避免被重置，默认为false。默认情况下，当webview被隐藏时资源会被销毁，通过`retainContextWhenHidden: true`会一直保存，但会占用较大内存开销，仅在需要时开启。
- 通过 `panel.webview.html` 填充webview的HTML内容

效果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603701787014-ed2ab150-df60-45c8-bef0-914c86483f9c.png#align=left&display=inline&height=69&originHeight=69&originWidth=185&size=3199&status=done&style=none&width=185)

<a name="TnZLw"></a>
## 从文件中读取内容
比如有如下HTML文件，路径为 `src/views/index.html` ：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <b>Hello, webview</b>
</body>
</html>
```
vscode没有提供直接从文件渲染webview的方法，所以只能先读取文件内容，然后渲染到webview了：
```javascript
const path = require('path');
const fs = require('fs');
const vscode = require('vscode');

module.exports = function(context) {
  context.subscriptions.push(vscode.commands.registerCommand('vscode-extension-test.openWebview', function (uri) {
    const panel = vscode.window.createWebviewPanel(
        'testWebview', "WebView Test", vscode.ViewColumn.One, {}
    );
    panel.webview.html = getWebViewContent(context, 'src/views/index.html')
  }))
}

function getWebViewContent(context, templatePath) {
  const resourcePath = path.join(context.extensionPath, templatePath);
  return fs.readFileSync(resourcePath, 'utf-8');
}
```

<a name="rzGg4"></a>
## 加载本地资源
出于安全考虑，Webview默认无法直接访问本地资源，它在一个孤立的上下文中运行，想要加载本地图片、js、css等必须通过特殊的`vscode-resource:`协议，网页里面**所有的静态资源都要转换成这种格式，否则无法被正常加载**。

`vscode-resource:`协议类似于`file:`协议，但它只允许访问特定的本地文件。和`file:`一样，`vscode-resource:`从磁盘加载绝对路径的资源。

默认情况下，`vscode-resource:`只能访问以下位置中的资源：

- 扩展程序安装目录中的文件。
- 用户当前活动的工作区内。
- 可以使用`dataURI`直接在Webview中嵌入资源，这种方式没有限制；

`vscode-resource:` 协议路径示例：
```bash
# Windows
vscode-resource:/d:/Workplace/temp/vscode-extension-test/src/views/styles/index.css

# MacOS
vscode-resource:/Users/Workplace/temp/vscode-extension-test/src/views/styles/index.css
```

对于类似如下相对路径：
```html
<link rel="stylesheet" href="./styles/index.css" />
```
应该将其转化为：
```html
<link rel="stylesheet" href="vscode-resource:/d:/Workplace/temp/vscode-extension-test/src/views/styles/index.css" />
```
注意 `rel="stylesheet"` 不可省略，否则样式不会生效。

`script` 和 `img` 的`src`也应做类似转换。可以将转换封装为一个方法：
```javascript
function getWebViewContent(context, templatePath) {
  const resourcePath = path.join(context.extensionPath, templatePath);
  const dirPath = path.dirname(resourcePath);
  let html = fs.readFileSync(resourcePath, 'utf-8');
  html = html.replace(/(<link.+?href="|<script.+?src="|<img.+?src=")(.+?)"/g, (m, $1, $2) => {
      return $1 + vscode.Uri.file(path.resolve(dirPath, $2)).with({ scheme: 'vscode-resource' }).toString() + '"';
  });
  return html;
}
```
调用：
```javascript
panel.webview.html = getWebViewContent(context, 'src/views/index.html')
```

<a name="BX50e"></a>
## 与宿主容器通讯
<a name="7Hy80"></a>
### 宿主 -> webview
宿主：
```javascript
panel.webview.postMessage({text: 'Hello, I\'m xiaoyu.'});
```
webview：
```javascript
window.addEventListener('message', event => {
  const message = event.data;
  console.log(message.text);
})
```
效果，注意观察右侧的console：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603764326503-68b110fd-adc9-4e6f-8fbd-16edad22025d.png#align=left&display=inline&height=164&originHeight=164&originWidth=955&size=23367&status=done&style=none&width=955)

<a name="GMTQ0"></a>
### webview -> 宿主
webview：
```html
  <button id="btn">发送消息到宿主容器</button>

  <script>
    const vscode = acquireVsCodeApi();

    document.getElementById('btn').addEventListener('click', () => {
      vscode.postMessage({text: 'Hello, I\'m Webview.'});
    })
  </script>
```
webview中可以通过 `acquireVsCodeApi()` 方法获取vscode对象，此vscode对象暴露一个 `postMessage` 方法，用于向宿主容器发送消息。

宿主：
```javascript
panel.webview.onDidReceiveMessage(message => {
  console.log(message.text)
  vscode.window.showInformationMessage(message.text)
}, undefined, context.subscriptions);
```
效果，在右下角弹出信息：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603765472197-d663ff6c-6ada-4cde-af46-36d3a845d4b9.png#align=left&display=inline&height=45&originHeight=45&originWidth=1047&size=9167&status=done&style=none&width=1047)

<a name="qeODm"></a>
## 关闭webview

通过 `panel.dispose()` 方法主动关闭webview。


<a name="7Yo3A"></a>
## 参考资料

- [webview](https://code.visualstudio.com/api/extension-guides/webview)
- [createWebviewPanel](https://code.visualstudio.com/api/references/vscode-api#window.createWebviewPanel)
