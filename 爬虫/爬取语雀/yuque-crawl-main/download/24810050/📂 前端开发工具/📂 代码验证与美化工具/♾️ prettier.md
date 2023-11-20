Prettier：[官网](https://prettier.io/)

<a name="nnYQQ"></a>
## 安装与使用
安装Prettier：
```javascript
yarn add --dev --exact prettier
```

创建一个配置文件： `.prettierrc.json` ，示例：
```javascript
{
  "tabWidth": 2,
  "useTabs": false,
  "singleQuote": true,
  "semi": false,
  "trailingComma": "none",
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "crlf",
  "htmlWhitespaceSensitivity": "ignore"
}
```

使用Prettier（格式化src下的所有文件）：
```bash
yarn prettier --write src
```

<a name="Wc4E7"></a>
## 配置文件
Prettier支持以下格式的配置文件：

- 在 `package.json`  中添加 `"prettier"` 字段进行配置
- `.prettierrc` 文件，可以书写 JSON 或 YAML.
- `.prettierrc.json`, `.prettierrc.yml`, `.prettierrc.yaml`, `.prettierrc.json5`, `.prettierrc.toml`
- `.prettierrc.js`, `.prettierrc.cjs`, `prettier.config.js`, or `prettier.config.cjs`，通过 `module.exports` 导出配置<br />

各种格式的配置文件示例：<br />JSON:
```json
{
  "trailingComma": "es5",
  "tabWidth": 4,
  "semi": false,
  "singleQuote": true
}
```

JS:
```javascript
// prettier.config.js or .prettierrc.js
module.exports = {
  trailingComma: "es5",
  tabWidth: 4,
  semi: false,
  singleQuote: true,
};
```

YAML:
```yaml
# .prettierrc or .prettierrc.yaml
trailingComma: "es5"
tabWidth: 4
semi: false
singleQuote: true
```

TOML:
```yaml
# .prettierrc.toml
trailingComma = "es5"
tabWidth = 4
semi = false
singleQuote = true
```

<a name="HoINC"></a>
## 常用配置项
所有配置项参考：

- [https://prettier.io/docs/en/options.html](https://prettier.io/docs/en/options.html)
- [https://prettier.io/docs/en/configuration.html](https://prettier.io/docs/en/configuration.html)

<a name="UDs1r"></a>
## 格式化忽略
创建一个忽略文件： `.prettierignore` ，示例：
```javascript
src/static
src/style/font
```

在不需要使用Prettier格式化的地方添加注释以忽略其后代码的格式化：
```javascript
// prettier-ignore
```
使用以下注释忽略注释范围内的代码格式化：
```javascript
// prettier-ignore-start
...
// prettier-ignore-end
```

<a name="cETzK"></a>
## 解决方案
<a name="K4Bgc"></a>
### Delete `␍`eslint(prettier/prettier)
仿这种，在每行末尾都报错：<br />![Snipaste_2021-01-25_15-35-59.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1611560216742-9e80b3de-0036-4c49-827e-66b9181a3e0c.webp#align=left&display=inline&height=270&originHeight=327&originWidth=424&size=13898&status=done&style=none&width=350)

错误原因：换行符与设置的不匹配。

解决方案：<br />方案一：一个一个文件的选择，具体操作如下，手动把CRLF换成LF。缺点：文件太多，换不过来。<br />WebStrom：<br />![Snipaste_2021-01-25_15-33-39.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1611560036602-b64e5baf-fe42-45ed-87c2-45bdf75a8190.webp#align=left&display=inline&height=116&originHeight=116&originWidth=384&size=5044&status=done&style=none&width=384)<br />VSCode：<br />![Snipaste_2021-01-25_15-39-15.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1611560401795-0e736d44-b93c-4b19-931f-7cab0655a2cc.webp#align=left&display=inline&height=357&originHeight=357&originWidth=1278&size=50076&status=done&style=none&width=1278)

方案二：`yarn run lint --fix`<br />比上面省事，eslint错误消失，但暂存区多了n个文件改动记录，对比Working tree也没发现任何不同。<br />其中 lint 命令对应的命令为：
```bash
eslint --fix --ext .ts,.js,.vue --ignore-path .gitignore .
```

方案三、修改`.prettierrc`文件<br />在项目根目录下的`.prettierrc`文件中写入即可。其实就是不让prettier检测文件每行结束的格式。
```
"endOfLine": "auto"
```

参考：

- [Delete `␍`eslint(prettier/prettier)错误](https://blog.csdn.net/qq_27674439/article/details/111408453)
- [https://github.com/prettier/eslint-plugin-prettier/issues/114](https://github.com/prettier/eslint-plugin-prettier/issues/114)

<a name="RgD2A"></a>
## 参考资料

- [ESLint+Prettier代码规范实践](https://www.jianshu.com/p/dd07cca0a48e)
- [VS Code Prettier + ESlint 格式化Vue代码及遇到问题](https://zhuanlan.zhihu.com/p/64627216)

