<a name="Q4YFm"></a>
## 单文件配置
一个node.js单文件的调试器配置如下：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "启动程序",
      "skipFiles": [
        "<node_internals>/**"
      ],
      "program": "${file}"
    }
  ]
}
```

<a name="JSNlL"></a>
## 运行后在浏览器中打开
一个express的示例，运行并在浏览器中打开：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "在浏览器中打开",
      "program": "${workspaceFolder}/app.js",
      "serverReadyAction": {
        "pattern": "listening on port ([0-9]+)",
        "uriFormat": "http://localhost:%s",
        "action": "openExternally"
      }
    }
  ]
}
```
在 `app.js` 中：
```javascript
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.send('Hello World!');
});

app.listen(3000, function() {
  console.log('App listening on port 3000!');
});
```

<a name="AvUCb"></a>
## 修改文件后自动重启
首先安装 `nodemon`
```bash
npm i -g nodemon
```
launch配置如下：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "在浏览器中打开",
      "program": "${workspaceFolder}/app.js",
      "runtimeExecutable": "nodemon",
      "restart": true,
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    }
  ]
}

```
启动调试，与执行以下命令效果相同：
```bash
nodemon --inspect app.js
```

<a name="qwra4"></a>
## 通过NPM启动
一个使用npm启动项目的示例：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "启动",
      "request": "launch",
      "runtimeArgs": [
        "run-script",
        "start"
      ],
      "runtimeExecutable": "npm",
      "type": "pwa-node"
    }
  ]
}
```
启动以上配置，相当于执行了 `npm start` 。

<a name="l8nbw"></a>
## 附加调试器
如果程序先启动，而没有开启调试，可以使用附加调试器的方式进行调试。<br />比如有如下一个 `app.js` 的程序：
```javascript
setInterval(() => {
  console.log(new Date())
}, 1000)
```
先启动了程序：
```bash
$ node --inspect app.js
# or
$ node --inspect-brk app.js
Debugger listening on ws://127.0.0.1:9229/e9413477-b1a3-41c1-821b-f6b4f983415b
For help, see: https://nodejs.org/en/docs/inspector
```
此时打断点，是没有作用的，因为此时还没有启动调试器。<br />可以添加一个launch配置：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Process",
      "type": "node",
      "request": "attach",
      "port": 9229
    }
  ]
}

```
使用 `inspect` 启动的程序，默认使用9229端口开启调试。<br />启动调试器：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602817464945-8b7d4ead-df82-41d3-b4a6-5ada6d17c51e.png#align=left&display=inline&height=34&originHeight=34&originWidth=292&size=2527&status=done&style=none&width=292)<br />在程序中打下断点：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602817501727-e8578c82-c37f-4043-8923-31e6caca3b8f.png#align=left&display=inline&height=78&originHeight=78&originWidth=397&size=5329&status=done&style=none&width=397)<br />可以看到，调试器生效了。

<a name="EmMZn"></a>
## 自动附加调试器
在配置中设置 `debug.javascript.autoAttachFilter` 可自动附加调试器。<br />可选值有：

- `smart`
- `always`
- `onlyWithFlag` 当添加 `--inspect` 或 `--inspect-brk` 时附加调试器

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602818465627-a6333257-16ff-4b4f-a046-8efa014a8315.png#align=left&display=inline&height=228&originHeight=228&originWidth=993&size=22983&status=done&style=none&width=993)

<a name="luSEd"></a>
## 通过命令附加调试器
打开命令面板，输入 `Attach to Node Process` 可以将运行中的程序附加调试器。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602818691120-3a1655d7-74d4-4db2-9839-003ffd0dc0fa.png#align=left&display=inline&height=364&originHeight=364&originWidth=609&size=37534&status=done&style=none&width=609)

<a name="O2O8j"></a>
## 从package.json查找启动程序
如果在launch.json中没有指定启动文件，或者找不到启动文件，会自动从package.json中查找配置，寻找 `main` 字段，如果找到，则执行 `main` 指定的文件，未找到则报错。
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "从package.json中读取配置",
      "program": "${workspaceFolder}",
    }
  ]
}
```
`package.json` :
```json
{
  "name": "demos",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

<a name="0FaSr"></a>
## 从环境变量中读取配置
使用 `envFile` 指定环境变量文件：
```json
{
  // 使用 IntelliSense 了解相关属性。
  // 悬停以查看现有属性的描述。
  // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "从环境变量中读取配置",
      "program": "${workspaceFolder}",
      // "env": { "FILENAME": "test.js" },
      "envFile": "${workspaceFolder}/.env"
    },
  ]
}

```
环境变量文件 `.env` 如下：
```json
FILENAME=app.js
```
如果在 `launch.json` 中设置 `env` 字段，将覆盖 `.env` 文件中相同字段的值。

在 `app.js` 中打印环境变量：
```javascript
console.log(process.env.FILENAME)
```

<a name="35808e79"></a>
## 参考资料

- [Node.js debugging in VS Code](https://code.visualstudio.com/docs/nodejs/nodejs-debugging)
