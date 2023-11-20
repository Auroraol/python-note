<a name="zQV9K"></a>
## 创建VSCode扩展

首先安装Yeoman和 [vscode-generator-code](https://github.com/Microsoft/vscode-generator-code)：
```bash
npm install -g yo generator-code
```

使用Yeoman创建一个VSCode Extension：
```bash
yo code
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602231801345-80a80bc8-e49f-4e89-8dbe-66ccdc51b603.png#align=left&display=inline&height=644&originHeight=644&originWidth=983&size=969342&status=done&style=none&width=983)<br />接下来回答一系列问题，最后创建好的项目结构如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602231855129-f5878413-763e-489c-a52a-348398783570.png#align=left&display=inline&height=573&originHeight=573&originWidth=313&size=21800&status=done&style=none&width=313)

<a name="j7gEp"></a>
## 扩展清单
VSCode Extension 扩展清单文件使用 `package.json` 。`package.json` 包括了  Node.js 相关的字段以及 VSCode 扩展清单相关的字段。

比较重要的VSCode扩展清单字段包括：

- **`name` 和 **`**publisher**` VSCode 使用 <publisher>.<name> 作为插件的唯一标识
- `main` 入口文件
- `activationEvents` 激活的事件
- `contributes` 功能贡献
- `engines.vscode` 引擎版本
- `categories` 分类

<a name="CqZm6"></a>
## 入口文件
使用 `main` 指定入口文件，在入口文件中引入：
```javascript
const vscode = require('vscode');
```
所有的vscode相关的API均可使用其调用。

