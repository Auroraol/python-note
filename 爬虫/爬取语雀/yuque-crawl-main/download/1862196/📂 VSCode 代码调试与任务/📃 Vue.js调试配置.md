<a name="QTJHN"></a>
## Vue2的调试配置
以下示例以Vue2+Webpack为例，项目使用Vue Cli脚手架创建。<br />相关项目创建的命令如下：
```bash
npm install -g @vue/cli
vue create vue2-app
cd vue2-app
code .
npm run serve
```
添加断点：举个例子，在编辑器中为.vue文件添加几个断点，直接运行是不会进入到断点的。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604971229664-e377faa7-252c-4106-bc95-5bbaac402001.png#align=left&display=inline&height=602&originHeight=602&originWidth=653&size=76059&status=done&style=none&width=653)<br />为了方便调试，我们需要创建一个 `vue.config.js`：
```javascript
module.exports = {
  configureWebpack: {
    devtool: "source-map"
  }
};
```
指定`devtool`为`source-map`，以开启SourceMap。<br />

<a name="3FQCb"></a>
## 通过Chrome调试
需要先安装 [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604972469675-9ede4de1-a215-4c95-baf6-28a542540478.png#align=left&display=inline&height=155&originHeight=155&originWidth=901&size=43162&status=done&style=none&width=901)

在 `launch.json` 中加入以下配置：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "vuejs: chrome",
      "url": "http://localhost:8080",
      "webRoot": "${workspaceFolder}/src",
      "breakOnLoad": true,
      "sourceMapPathOverrides": {
        "webpack:///src/*": "${webRoot}/*"
      }
    }
  ]
}

```
注意几个地方：

- `webRoot` 指定了项目源文件路径
- `sourceMapPathOverrides` 指定了编译前后的文件映射
- `breakOnLoad` 启动调试时马上断住

按下F5进行调试，自动弹出Chrome并打开指定的url，发现已经在created中断住：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604971485877-4482403a-7219-4e95-b9dc-d4f0e2bb016b.png#align=left&display=inline&height=754&originHeight=754&originWidth=1343&size=156264&status=done&style=none&width=1343)

<a name="xQF53"></a>
## 通过Edge调试
需要先安装 [Debugger for Microsoft Edge](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-edge)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604972620422-d3c065b7-9e8a-4627-b0b1-e21063a465d1.png#align=left&display=inline&height=160&originHeight=160&originWidth=741&size=49201&status=done&style=none&width=741)<br />基本上跟Chrome的配置一样：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "pwa-msedge",
      "request": "launch",
      "name": "vuejs: edge",
      "url": "http://localhost:8080",
      "webRoot": "${workspaceFolder}/src",
      "sourceMapPathOverrides": {
        "webpack:///src/*": "${webRoot}/*"
      }
    }
  ]
}
```

<a name="Uz37X"></a>
## 通过Firefox调试
需要先安装 [Debugger for Firefox](https://marketplace.visualstudio.com/items?itemName=firefox-devtools.vscode-firefox-debug)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604972527230-7398e78c-d417-48e4-b850-208eb278f26f.png#align=left&display=inline&height=157&originHeight=157&originWidth=744&size=48565&status=done&style=none&width=744)<br />也不多说了，稍微有一点点改动，就是将 `sourceMapPathOverrides` 变为 `pathMappings` ：
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "firefox",
      "request": "launch",
      "name": "vuejs: firefox",
      "url": "http://localhost:8080",
      "webRoot": "${workspaceFolder}/src",
      "pathMappings": [{ "url": "webpack:///src/", "path": "${webRoot}/" }]
    }
  ]
}
```

<a name="kngTY"></a>
## FAQ
<a name="Awk1V"></a>
### 为什么是 `webpack:///src/*` 
这个疑问，可以打开浏览器的调试台，按下 `F12` 即可看到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604971766811-4a347338-c25b-4c4a-9a4a-7d6b923d1d33.png#align=left&display=inline&height=824&originHeight=824&originWidth=1447&size=131503&status=done&style=none&width=1447)<br />这个就跟源文件中的位置对应了：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1604971818147-2bc26606-05e8-4736-89c9-0bfa15dfd2ea.png#align=left&display=inline&height=515&originHeight=515&originWidth=404&size=39509&status=done&style=none&width=404)

<a name="WdmAL"></a>
## 参考资料

- [Using Vue in Visual Studio Code：Debugging](https://code.visualstudio.com/docs/nodejs/vuejs-tutorial#_debugging)
- [Vue.js：在 VS Code 中调试](https://cn.vuejs.org/v2/cookbook/debugging-in-vscode.html)
