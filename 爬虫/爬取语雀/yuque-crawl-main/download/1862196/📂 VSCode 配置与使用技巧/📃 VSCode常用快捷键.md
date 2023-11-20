以下是我个人的使用习惯，列举我常用的一些快捷键。

<a name="k3lZX"></a>

## 编辑

- `Ctrl + Y` 恢复
- `Ctrl + Z` 撤销
- `F2` 重命名符号
- `Shift + Alt + 上箭头/下箭头` 将当前行的内容向上/向下复制一行
- `Alt + 上箭头/下箭头` 将当前行的内容向上/向下移动一行

新增、修改的快捷键：

- 删除行 `Ctrl + X`
```json
  {
    "key": "ctrl+d ctrl+d",
    "command": "editor.action.deleteLines",
    "when": "textInputFocus && !editorReadonly"
  },
  {
    "key": "ctrl+shift+k",
    "command": "-editor.action.deleteLines",
    "when": "textInputFocus && !editorReadonly"
  },
```

- 替换 `Ctrl + R`
```json
  {
    "key": "ctrl+r",
    "command": "editor.action.startFindReplaceAction"
  },
  {
    "key": "ctrl+h",
    "command": "-editor.action.startFindReplaceAction"
  },
```

<a name="KN5Bc"></a>
## 光标

- `Ctrl + 上箭头/下箭头` 向上/ 向下滚动一行
- `Ctrl + Alt + 上箭头/下箭头` 向上/向下添加光标
- `Alt + 左箭头/右箭头` 后退/前进（所有打开的文件中，光标上一个/下一个文件光标位置）
- `Ctrl + U` 光标撤销（当前文件）

新增、修改的快捷键：

- 光标重做（当前文件） Alt + U
```json
  {
    "key": "alt+u",
    "command": "cursorRedo",
    "when": "textInputFocus"
  },
```

<a name="cf55x"></a>
## 选区

- `Ctrl + Shift + 上箭头/下箭头` 向上/向下选择一行
- `Shit + Alt + 左箭头/右箭头` 收起/展开选择

<a name="Myby0"></a>
## 终端

- 打开终端 `Ctrl + `` 

新增、修改的快捷键：

- 面板最大化 `Ctrl + Enter`
```json
  {
    "key": "ctrl+enter",
    "command": "workbench.action.toggleMaximizedPanel",
    "when": "terminalFocus"
  },
```

<a name="QHTCS"></a>
## 代码
<a name="tb9x2"></a>
### 代码提示

新增、修改的快捷键：

- 代码提示 `Alt + /` 
```json
  {
    "key": "alt+oem_2",
    "command": "editor.action.triggerSuggest",
    "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly"
  },
  {
    "key": "ctrl+i",
    "command": "-editor.action.triggerSuggest",
    "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly"
  },
  {
    "key": "ctrl+space",
    "command": "-editor.action.triggerSuggest",
    "when": "editorHasCompletionItemProvider && textInputFocus && !editorReadonly"
  },
  {
    "key": "alt+oem_2",
    "command": "toggleSuggestionDetails",
    "when": "suggestWidgetVisible && textInputFocus"
  },
  {
    "key": "ctrl+space",
    "command": "-toggleSuggestionDetails",
    "when": "suggestWidgetVisible && textInputFocus"
  },
```

<a name="mgbWK"></a>
### 代码修复

- `Shift + Alt + .` 自动修复

新增、修改的快捷键：

- 快速修复 `Alt + Enter`
```json
  {
    "key": "alt+enter",
    "command": "editor.action.quickFix",
    "when": "editorHasCodeActionsProvider && editorTextFocus && !editorReadonly"
  },
  {
    "key": "ctrl+oem_period",
    "command": "-editor.action.quickFix",
    "when": "editorHasCodeActionsProvider && editorTextFocus && !editorReadonly"
  },
```

<a name="tnO7v"></a>
### 代码注释

- `Ctrl + /` 行注释

新增、修改的快捷键：

- 块注释 `Ctrl + Shift + /`
```json
  {
    "key": "ctrl+shift+oem_2",
    "command": "editor.action.blockComment",
    "when": "editorTextFocus && !editorReadonly"
  },
  {
    "key": "shift+alt+a",
    "command": "-editor.action.blockComment",
    "when": "editorTextFocus && !editorReadonly"
  },
```

<a name="qSi1K"></a>
## 窗口

- `Ctrl + Alt + 左箭头/右箭头` 将当前文件移动到左/右窗口
