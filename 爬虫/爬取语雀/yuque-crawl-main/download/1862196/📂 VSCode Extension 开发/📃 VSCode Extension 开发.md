<a name="gXYBV"></a>
## 扩展的激活和释放

首先，修改目录结构，把 `src/main.js` 作为入口文件， `src/extensions` 存储所有扩展。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602294662142-e6efe5d7-2b24-43ac-9fde-9c32ba6125e3.png#align=left&display=inline&height=387&originHeight=387&originWidth=319&size=17562&status=done&style=none&width=319)

在 `package.json` 中修改：
```json
{  
  "main": "./src/main.js",
}
```

在 `main.js` 中：
```javascript
const vscode = require('vscode');

// 激活
exports.activate = function (context) {
  console.info('提示：vscode-extension-test以被激活！');
  console.log(vscode);
}

// 释放
exports.deactivate = function () {
  console.log('extension deactivate')
}
```
当扩展注册时，在控制台可以看到提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602296221469-9164b4c2-93d9-4578-9e57-4e936a1d15b3.png#align=left&display=inline&height=195&originHeight=195&originWidth=770&size=22137&status=done&style=none&width=770)

<a name="jOeL6"></a>
## 注册命令

在 `src/extensions` 中添加 `command.js` 
```javascript
const vscode = require('vscode');

module.exports = function(context) {
  context.subscriptions.push(vscode.commands.registerCommand('vscode-extension-test.helloWorld', () => {
      vscode.window.showInformationMessage('Hello xiaoxiao昱！');
  }));
};
```
在 `activate` 中引入：
```javascript
exports.activate = function (context) {
  require('./extensions/command')(context)
}
```
在 `package.json` 中注册：
```json
{
  "contributes": {
    "commands": [{
      "command": "vscode-extension-test.helloWorld",
      "title": "Hello xiaoxiao昱"
    }]
  },
}
```
这样就可以使用 `Ctrl + Shift + P` 调出命令面板，使用 `Hello xiaoxiao昱` 命令了：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602296042106-991bf772-04e3-48c2-8933-8ab64ce2f256.png#align=left&display=inline&height=72&originHeight=72&originWidth=614&size=3763&status=done&style=none&width=614)<br />命令执行结果，可以在右下角看到通知：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602296069505-3edcd1e3-fc90-4dd1-8887-971a79abe10f.png#align=left&display=inline&height=86&originHeight=86&originWidth=467&size=3494&status=done&style=none&width=467)

<a name="XOO7C"></a>
## 右键菜单

稍微修改下 `helloWorld` 命令：
```javascript
  context.subscriptions.push(vscode.commands.registerCommand('vscode-extension-test.helloWorld', (uri) => {
    vscode.window.showInformationMessage(`当前文件(夹)路径是：${uri ? uri.path : '空'}`);
    console.log(uri)
  }));
```
然后在 `package.json` 中注册右键菜单：
```javascript
{
  "contributes": {
    "commands": [{
      "command": "vscode-extension-test.helloWorld",
      "title": "Hello xiaoxiao昱"
    }],
    "menus": {
      "editor/context": [
        {
            "when": "editorFocus",
            "command": "vscode-extension-test.helloWorld",
            "group": "navigation@5"
        }
      ]
    }
  },
}
```
然后随便打开一个文件，右键可以看到选项：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602297413368-07ff749b-d8f8-482f-b561-95ffb57b3394.png#align=left&display=inline&height=268&originHeight=268&originWidth=621&size=23333&status=done&style=none&width=621)<br />执行结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602297463286-390b7cb2-833d-440d-b821-c51d19009628.png#align=left&display=inline&height=75&originHeight=75&originWidth=462&size=7675&status=done&style=none&width=462)<br />可以看到，将当前路径在通知区域显示了出来。
