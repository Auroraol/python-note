先上一个简单的 Package.json：
```json
{
  "name": "vscode-extension-test",
  "displayName": "vscode-extension-test",
  "description": "",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.50.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [
    "onCommand:vscode-extension-test.helloWorld"
  ],
  "main": "./src/main.js",
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
            "group": "navigation@1"
        }
      ]
    }
  },
  // npm 相关配置，不多讲了
  "scripts": {
    "lint": "eslint .",
    "pretest": "yarn run lint",
    "test": "node ./test/runTest.js"
  },
  "devDependencies": {
        "@types/vscode": "^1.50.0",
        "@types/glob": "^7.1.3",
        "@types/mocha": "^8.0.0",
        "@types/node": "^12.11.7",
        "eslint": "^7.9.0",
        "glob": "^7.1.6",
        "mocha": "^8.1.3",
        "typescript": "^4.0.2",
        "vscode-test": "^1.4.0"
    }
}
```
<a name="6gnOP"></a>
## activationEvents

插件在`VS Code`中默认是没有被激活的，哪什么时候才被激活呢？就是通过`activationEvents`来配置，目前支持一下8种配置：

- `onLanguage:${language}`
- `onCommand:${command}`
- `onDebug`
- `workspaceContains:${toplevelfilename}`
- `onFileSystem:${scheme}`
- `onView:${viewId}`
- `onUri`
- `*`

举个例子，如果我配置了`onLanguage:javascript`，那么只要我打开了`javascript`类型的文件，插件就会被激活了。

如果配置了`*`，只要一启动vscode，插件就会被激活，为了出色的用户体验，官方不推荐这么做。

<a name="Rk0Fv"></a>
## contributes

`contributes` 字段声明了在extension中贡献的功能列表。可选值如下：

- `configuration`：设置
- `configurationDefaults`：覆盖默认配置
- `commands`：命令
- `menus`：菜单
- `keybindings`：快捷键绑定
- `languages`：新语言支持
- `debuggers`：调试
- `breakpoints`：断点
- `grammars` 语法
- `themes`：主题
- `snippets`：代码片段
- `jsonValidation`：自定义JSON校验
- `views`：左侧侧边栏视图
- `viewsContainers`：自定义activitybar
- `problemMatchers`
- `problemPatterns`
- `taskDefinitions`
- `colors` 

<a name="UiASK"></a>
### [contributes.configuration](https://code.visualstudio.com/api/references/contribution-points#contributes.configuration)
`contributes.configuration` 可以在配置文件中添加配置时提示和显示描述：
```json
{
  "contributes": {
    "configuration": {
      "title": "vscode-extension-test",
      "properties": {
        "vscode-extension-test.language": {
          "type": "string",
          "default": "javascript",
          "description": "配置语言"
        },
      }
    }
  }
}
```
在配置文件中：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602298788071-c5011c4c-f444-485b-ac18-1d8a8b9d6ba6.png#align=left&display=inline&height=208&originHeight=208&originWidth=611&size=19627&status=done&style=none&width=611)<br />在设置的UI中也可以找到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602299511259-2f35ec1f-2303-4f7d-8822-2916eea1f37e.png#align=left&display=inline&height=310&originHeight=310&originWidth=989&size=20912&status=done&style=none&width=989)

枚举选项的配置：
```json
{
  "contributes": {
    "configuration": {
      "title": "vscode-extension-test",
      "properties": {
        "vscode-extension-test.color": {
          "type": "string",
          "default": "red",
          "enum": ["red", "black"],
          "enumDescriptions": [
            "红色",
            "黑色"
          ]
        }
      }
    }   
  }
}
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602299337555-4657938d-8b8a-4f3c-bb63-2c17635de2d5.png#align=left&display=inline&height=149&originHeight=149&originWidth=408&size=5630&status=done&style=none&width=408)

<a name="SCiJd"></a>
#### 通过API获取配置
```javascript
const result = vscode.workspace.getConfiguration().get('vscode-extension-test.language');
console.log(result)
```
如果没有此设置，则返回undefined。

<a name="QTIEG"></a>
#### 通过API更新配置
```javascript
vscode.workspace.getConfiguration().update('vscode-extension-test.language', 'typescript', true);
```
最后一个参数为true时表示写入全局配置，为false或不传时则只写入工作区配置。

<a name="brhnU"></a>
### [contributes.configurationDefaults](https://code.visualstudio.com/api/references/contribution-points#contributes.configurationDefaults)
`contributes.configurationDefaults` 可以覆盖默认配置：
```json
{
  "contributes": {
    "configurationDefaults": {
      "[markdown]": {
        "editor.wordWrap": "on",
        "editor.quickSuggestions": false
      }
    }
  }
}
```

<a name="lHQfH"></a>
### [contributes.commands](https://code.visualstudio.com/api/references/contribution-points#contributes.commands)
`contributes.commands` 可以注册一个命令：
```json
{
  "contributes": {
		"commands": [{
      "command": "vscode-extension-test.sayHello",
      "title": "xiaoxiao昱",
      "category": "Hello"
    }, {
      "command": "vscode-extension-test.helloWorld",
      "title": "World",
      "category": "Hello"
    }],
  }
}
```
使用 `Ctrl+Shift+P` 可以在命令面板中调出：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602300355742-faba3b48-02a9-40b2-9dfb-047192667a03.png#align=left&display=inline&height=97&originHeight=97&originWidth=608&size=5410&status=done&style=none&width=608)

<a name="Ci94B"></a>
### [contributes.menus](https://code.visualstudio.com/api/references/contribution-points#contributes.menus)

`contributes.menus` 可以注册右键上下文菜单：
```json
{
  "contributes": {
    "commands": [{
      "command": "vscode-extension-test.sayHello",
      "title": "xiaoxiao昱",
      "category": "Hello"
    }],
    "menus": {
      "editor/context": [
        {
            "when": "editorFocus",
            "command": "vscode-extension-test.sayHello",
            "group": "navigation@1"
        }
      ]
    },
  }
}
```
menu 的 key 指定在编辑器什么区域触发菜单的显示，比如上面的 `editor/context` 就指定在编辑区域中触发显示：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602301506188-2970f23f-10cd-4b00-8414-f9fa861d617c.png#align=left&display=inline&height=258&originHeight=258&originWidth=675&size=12124&status=done&style=none&width=675)<br />`when` 指定了何时显示此菜单<br />`command` 需要事先在 `contributes.commands` 中注册，才能调取到该命令。<br />`group` 指定菜单所在位置排序，上面的 `navigation@1` 指定在顺序为1的位置显示（下标从0开始）

目前menus支持的key值有：

- `commandPalette` 控制命令是否显示在命令选项板中
- `explorer/context` 资源管理器上下文菜单
- `editor/context` 编辑器上下文菜单
- `editor/title` 编辑标题菜单栏
- `editor/title/context` 编辑器标题上下文菜单
- `extension/context` 扩展上下文菜单
- `debug/callstack/context` 调试视图上下文菜单
- `debug/toolbar` 调试视图工具栏菜单
- `scm/title` SCM标题菜单
- `scm/resourceGroup/context` SCM资源组菜单
- `scm/resourceState/context` SCM资源菜单
- `scm/change/title` SCM更改标题菜单
- `view/title` 左侧视图标题菜单
- `view/item/context` 视图项菜单
- `touchBar`
- `comments/commentThread/title`
- `comments/commentThread/context`
- `comments/comment/title`
- `comments/comment/context`
- `timeline/title` 时间轴标题栏菜单
- `timeline/item/context` 时间轴项菜单

**editor context menu** 默认有以下可选的group：

- `navigation`
- `1_modification`
- `9_cutcopypaste`
- `z_commands`

**explorer context menu** 默认有以下可选的group：

- `navigation`
- `2_workspace`
- `3_compare`
- `4_search`
- `5_cutcopypaste`
- `6_copypath`
- `7_modification`

**editor tab context menu** 默认有以下可选的group：

- `1_close`
- `3_preview`

**editor title menu** 默认有以下可选的group：

- `navigation`
- `1_run`
- `1_diff`
- `3_open`
- `5_close`

**Timeline view item context menu** 默认有以下可选的group：

- `inline`
- `1_actions`
- `5_copy`

**Extensions view context menu** 默认有以下可选的group：

- `1_copy`
- `2_configure`

<a name="AMmE8"></a>
### [contributes.keybindings](https://code.visualstudio.com/api/references/contribution-points#contributes.keybindings)
`contributes.keybindings` 可以添加键盘按键映射：
```json
{
  "contributes": {
    "commands": [{
      "command": "vscode-extension-test.sayHello",
      "title": "xiaoxiao昱",
      "category": "Hello"
    }],
    "keybindings": [
      {
        "command": "vscode-extension-test.sayHello",
        "key": "ctrl+1",
        "mac": "cmd+1",
        "when": "editorTextFocus"
      }
    ],
  }
}
```
以上，使用 `Ctrl/Command + 1` 即可调用 `sayHello` 命令。

<a name="oZLMu"></a>
### [contributes.languages](https://code.visualstudio.com/api/references/contribution-points#contributes.languages)
通过 `contributes.languages` 可以定义一款新语言的特性，或增强一款已知语言的特性。

<a name="spSJJ"></a>
### [contributes.snippets](https://code.visualstudio.com/api/references/contribution-points#contributes.snippets)<br />
通过 `contributes.snippets` 可以添加代码片段。

示例：
```json
{
  "contributes": {
    "snippets": [
      {
        "language": "javascript",
        "path": "./snippets/javascript.json"
      }
    ]
  }
}
```
snippet 示例如下：
```json
{
  "Print to console": {
    "prefix": "testLog",
    "body": [
      "console.log('$1')",
      "$2"
    ],
    "description": "Log output to console"
  }
}
```
效果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602316287839-239ddfbc-2bb8-459e-b713-855697a47994.png#align=left&display=inline&height=169&originHeight=169&originWidth=797&size=16335&status=done&style=none&width=797)

代码片段参考： [snippet-syntax](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_snippet-syntax)

<a name="UDfgy"></a>
### [contributes.views](https://code.visualstudio.com/api/references/contribution-points#contributes.views)
`contributes.views` 可以创建视图，其key指定的是视图容器：
```json
{
  "contributes": {
    "viewsContainers": {
      "activitybar": [
        {
          "id": "languages",
          "title": "语言分类",
          "icon": "src/icons/language.svg"
        }
      ]
    },
    "views": {
      "languages": [
        {
            "id": "javascript",
            "name": "javascript"
        },
        {
            "id": "python",
            "name": "python"
        }
      ]
    }
  }
}
```
效果如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602316663579-c52a55de-c9ce-47b7-8887-b9b957290b20.png#align=left&display=inline&height=289&originHeight=289&originWidth=374&size=11011&status=done&style=none&width=374)

VSCode默认提供以下容器：

- `explorer`
- `scm`
- `debug`
- `test`

如果需要自定义，可以通过 [Custom view containers](https://code.visualstudio.com/api/references/contribution-points#contributes.viewsContainers) 创建自定义容器，上面的示例代码就是通过这种方式创建的。

......

好了，还有很多contributes内容，等遇到了再加上，先讲这些，不清楚的还是去看官网说明吧。

<a name="OOQtu"></a>
## 参考资料

- [activation-events](https://code.visualstudio.com/api/references/activation-events)
- [extension-manifest](https://code.visualstudio.com/api/references/extension-manifest)
