ESLint：[中文网](https://eslint.cn/)

<a name="kvQ4s"></a>
## 安装与使用
安装ESLint：
```bash
yarn add -D eslint
```
如果是vue-cli3脚手架安装的可以使用以下命令安装：
```bash
vue add @vue/eslint
```

初始化ESLint：
```bash
$ npx eslint --init
√ How would you like to use ESLint? · style
√ What type of modules does your project use? · esm
√ Which framework does your project use? · vue
√ Does your project use TypeScript? · No / Yes
√ Where does your code run? · browser
√ How would you like to define a style for your project? · auto
√ Which file(s), path(s), or glob(s) should be examined? · src
√ What format do you want your config file to be in? · JavaScript
Determining Config: 100% [==============================] 2.2s elapsed, eta 0.0s

Enabled 181 out of 255 rules based on 14 files.
```
初始化ESLint的时候，工具会询问一系列问题，根据自己的项目选择即可。

<a name="PI6Ui"></a>
## 配置文件
ESLint 支持几种格式的配置文件：

- **JavaScript** - 使用 `.eslintrc.js` 然后输出一个配置对象。
- **YAML** - 使用 `.eslintrc.yaml` 或 `.eslintrc.yml` 去定义配置的结构。
- **JSON** - 使用 `.eslintrc.json` 去定义配置的结构，ESLint 的 JSON 文件允许 JavaScript 风格的注释。
- **(弃用)** - 使用 `.eslintrc`，可以使 JSON 也可以是 YAML。
- **package.json** - 在 `package.json` 里创建一个 `eslintConfig`属性，在那里定义你的配置。

<a name="A5Q1A"></a>
### 错误粒度
配置文件示例：
```bash
{
    "rules": {
        "semi": ["error", "always"],
        "quotes": ["error", "double"]
    }
}
```
"semi" 和 "quotes" 是 ESLint 中 规则 的名称。第一个值是错误级别，可以使下面的值之一：

- **"off"** or **0** - 关闭规则
- **"warn"** or **1** - 将规则视为一个警告（不会影响退出码）
- **"error"** or **2** - 将规则视为一个错误 (退出码为1)

一个json格式的示例（ `.eslintrc` 或 `.eslintrc.json` ）：
```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": "airbnb-base",
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "double"]
  },
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  }
}
```

一个yaml格式的示例（ `.eslintrc.yml`）：
```yaml
env:
  browser: true
  es2021: true
extends:
  - airbnb-base
parserOptions:
  ecmaVersion: 12
  sourceType: module
rules: {}
```

一个js格式的示例（`.eslintrc.js`）：
```javascript
module.exports = {
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:vue/essential"
  ],
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "double"]
  },
}
```

<a name="T5L42"></a>
### 默认规则
在 `.eslintrc` 配置文件中可以包含下面的一行：
```json
{
	"extends": "eslint:recommended"
}
```


由于这行，所有在 [规则页面](http://eslint.cn/docs/rules) 被标记为 “**√**” 的规则将会默认开启。另外，可以在 [npmjs.com](https://www.npmjs.com/search?q=eslint-config) 搜索 “eslint-config” 使用别人创建好的配置。只有在你的配置文件中扩展了一个可分享的配置或者明确开启一个规则，ESLint 才会去校验你的代码。

<a name="8zg2V"></a>
### 环境配置
环境配置示例：
```bash
{
  "env": {
    "browser": true,
    "node": true,
    "es2021": true
  },
}
```

可用的环境包括：

- `browser` - 浏览器环境中的全局变量。
- `node` - Node.js 全局变量和 Node.js 作用域。
- `commonjs` - CommonJS 全局变量和 CommonJS 作用域 (用于 Browserify/WebPack 打包的只在浏览器中运行的代码)。
- `shared-node-browser` - Node.js 和 Browser 通用全局变量。
- `es6` - 启用除了 modules 以外的所有 ECMAScript 6 特性（该选项会自动设置 `ecmaVersion` 解析器选项为 6）。
- `worker` - Web Workers 全局变量。
- `amd` - 将 `require()` 和 `define()` 定义为像 [amd](https://github.com/amdjs/amdjs-api/wiki/AMD) 一样的全局变量。
- `mocha` - 添加所有的 Mocha 测试全局变量。
- `jasmine` - 添加所有的 Jasmine 版本 1.3 和 2.0 的测试全局变量。
- `jest` - Jest 全局变量。
- `phantomjs` - PhantomJS 全局变量。
- `protractor` - Protractor 全局变量。
- `qunit` - QUnit 全局变量。
- `jquery` - jQuery 全局变量。
- `prototypejs` - Prototype.js 全局变量。
- `shelljs` - ShellJS 全局变量。
- `meteor` - Meteor 全局变量。
- `mongo` - MongoDB 全局变量。
- `applescript` - AppleScript 全局变量。
- `nashorn` - Java 8 Nashorn 全局变量。
- `serviceworker` - Service Worker 全局变量。
- `atomtest` - Atom 测试全局变量。
- `embertest` - Ember 测试全局变量。
- `webextensions` - WebExtensions 全局变量。
- `greasemonkey` - GreaseMonkey 全局变量。

这些环境并不是互斥的，所以可以同时定义多个。

要在某个 JavaScript 文件中使用注释来指定环境，格式如下：
```
/* eslint-env node, mocha */
```


详细配置参考：[specifying-environments](http://eslint.cn/docs/user-guide/configuring#specifying-environments)

<a name="nmNK9"></a>
### 常用规则
详细的规则参考：[http://eslint.cn/docs/rules/](http://eslint.cn/docs/rules/)<br />Vue的配置规则参考：[https://eslint.vuejs.org/rules/](https://eslint.vuejs.org/rules/)

常用规则项有：

| 规则 | 说明 | 参数 | 可修复性（eslint --fix） |
| :---: | :---: | :---: | :---: |
| [quotes](http://eslint.cn/docs/rules/quotes) | 强制使用一致的反勾号、双引号或单引号 | <br />- `"double"` (默认) 要求尽可能地使用双引号<br />- `"single"` 要求尽可能地使用单引号<br />- `"backtick"` 要求尽可能地使用反勾号<br /> | √ |
| [semi](http://eslint.cn/docs/rules/semi) | 强制使用一致的分号。 | <br />- `"always"` (默认) 要求在语句末尾使用分号<br />- `"never"` 禁止在语句末尾使用分号 (除了消除以 `[`、`(`、`/`、`+` 或 `-` 开始的语句的歧义)<br /> | √ |
| [<br />indent](http://eslint.cn/docs/rules/indent) | 强制使用一致的缩进 | 参数为缩进的空格数或 `"tab"`  | √ |
| [eqeqeq](http://eslint.cn/docs/rules/eqeqeq) | 强制使用 === 和 !== | <br />- `"always"` <br />- `"smart"` <br /> | √ |
| [curly](http://eslint.cn/docs/rules/curly) | 强制所有控制语句使用一致的括号风格 | <br />- `"all"`<br />- `"multi"`<br />- `"multi-line"`<br />- `"multi-or-nest"`<br />- `"consistent"<br />`<br /> | √ |
| [key-spacing](http://eslint.cn/docs/rules/key-spacing) | 强制在对象字面量的属性中键和值之间使用一致的间距 |  | √ |
| [keyword-spacing](http://eslint.cn/docs/rules/keyword-spacing) | 强制在关键字前后使用一致的空格 | <br />- `"before": true` (默认) 要求在关键字之前至少有一个空格<br />- `"before": false` 禁止在关键字之前有空格<br />- `"after": true` (默认) 要求在关键字之后至少有一个空格<br />- `"after": false` 禁止在关键字之后有空格<br />- `"overrides"` 允许覆盖指定的关键字的空格风格<br /> | √ |
| [<br />space-before-blocks](http://eslint.cn/docs/rules/space-before-blocks) | 强制在块之前使用一致的空格 | <br />- `"always"`<br />- `"never"`<br /> | √ |
| [space-before-function-paren](http://eslint.cn/docs/rules/space-before-function-paren) | 强制在 `function`的左括号之前使用一致的空格 | <br />- `always` (默认) 要求在参数的 `(` 前面有一个空格。<br />- `never` 禁止在参数的 `(` 前面有空格。<br /> | √ |
| [space-in-parens](http://eslint.cn/docs/rules/space-in-parens) | 强制在圆括号内使用一致的空格 | <br />- `"never"` (默认) 强制圆括号内没有空格<br />- `"always"` 强制圆括号内有一个空格<br /> | √ |
| [space-infix-ops](http://eslint.cn/docs/rules/space-infix-ops) | 要求操作符周围有空格 |  | √ |
| [space-unary-ops](http://eslint.cn/docs/rules/space-unary-ops) | 强制在一元操作符前后使用一致的空格 |  | √ |
| [spaced-comment](http://eslint.cn/docs/rules/spaced-comment) | 强制在注释中 `//` 或 `/*` 使用一致的空格 |  | √ |
| [template-tag-spacing](http://eslint.cn/docs/rules/template-tag-spacing) | 要求或禁止在模板标记和它们的字面量之间有空格 | <br />- `"never"` <br />- `"always"`<br /> | √ |
| [switch-colon-spacing](http://eslint.cn/docs/rules/switch-colon-spacing) | 强制在 switch 的冒号左右有空格 | <br />- `"after": true` (默认) 要求冒号之后又一个或多个空格。<br />- `"after": false` 禁止冒号之后又空格。<br />- `"before": true` 要求冒号之前又一个或多个空格。<br />- `"before": false` (默认) 禁止冒号之前又空格。<br /> | √ |
| [dot-location](http://eslint.cn/docs/rules/dot-location) | 强制在点号之前和之后一致的换行 | <br />- `"object"` (默认)：表达式中的点号操作符应该和对象部分在同一行。

- `"property"`：表达式中的点号操作符应该和属性在同一行。

 | √ |
| [padded-blocks](http://eslint.cn/docs/rules/padded-blocks) | 要求或禁止块内填充 | <br />- `"always"` (默认) 要求块语句和类的开始或末尾有空行<br />- `"never"` 禁止块语句和类的开始或末尾有空行<br /> | √ |
| [eol-last](http://eslint.cn/docs/rules/eol-last) | 要求或禁止文件末尾存在空行 | <br />- `"always"` (默认) 强制使用换行 (LF)<br />- `"never"` 强制文件末尾不要有换行符<br /> | √ |
| [dot-notation](http://eslint.cn/docs/rules/dot-notation) | 强制尽可能地使用点号 |  | √ |
| [func-style](http://eslint.cn/docs/rules/func-style) | 强制一致地使用 `function` 声明或表达式 | <br />- `"expression"` (默认) 要求使用函数表达式而不是函数声明<br />- `"declaration"` 要求使用函数声明而不是函数表达式<br /> |  |
| [func-call-spacing](http://eslint.cn/docs/rules/func-call-spacing) | 要求或禁止在函数标识符和其调用之间有空格 | <br />- `"never"` (默认) 禁止在函数名和开括号之间有空格<br />- `"always"` 要求在函数名和开括号之间有空格<br /> | √ |
| [func-name-matching](http://eslint.cn/docs/rules/func-name-matching) | 要求函数名与赋值给它们的变量名或属性名相匹配 | <br />- `"always"`<br />- `"never"` <br /> |  |
| [func-names](http://eslint.cn/docs/rules/func-names) | 要求或禁止使用命名的 `function` 表达式 | <br />- `"always"` 要求命名的生成器函数 。<br />- `"as-needed"` 如果无法在ES6环境中自动分配名称，则需要命名的生成器函数。<br />- `"never"` 尽肯能地禁止命名的生成器函数。<br /> |  |
| [function-paren-newline](http://eslint.cn/docs/rules/function-paren-newline) | 强制在函数括号内使用一致的换行 | <br />- `"always"` 要求在所有的函数括号内换行。<br />- `"never"` 禁止在所有的函数括号内换行。<br />- `"multiline"` (默认) 如果函数的任一参数有换行，则要求在函数括号内换行。否则禁止换行。<br />- `"multiline-arguments"` 类似于 `multiline`，但如果只有一个参数/参数，则允许在函数括号内使用换行符。<br />- `"consistent"` 要求每个括号使用一致的换行。如果一个括号有换行，另一个括号没有换行，则报错。<br />- `{ "minItems": value }` 只要参数的个数大于等于指定的 `value`，则要求在函数括号内换行。否则，禁止换行。<br /> | √ |
| [implicit-arrow-linebreak](http://eslint.cn/docs/rules/implicit-arrow-linebreak) | 强制隐式返回的箭头函数体的位置 | <br />- `"beside"` (默认) 禁止在箭头函数体之前出现换行。<br />- `"below"` 要求在箭头函数体之前出现换行。<br /> | √ |
| [no-var](http://eslint.cn/docs/rules/no-var) | 要求使用 `let` 或 `const` 而不是 `var` |  | √ |
| [no-void](http://eslint.cn/docs/rules/no-void) | 禁用 `void` 操作符 |  |  |
| [no-tabs](http://eslint.cn/docs/rules/no-tabs) | 禁用 tab |  |  |
| [no-eval](http://eslint.cn/docs/rules/no-eval) | 禁用 `eval()` |  |  |
| [no-unused-vars](https://eslint.org/docs/rules/no-unused-vars) | 禁止未使用过的变量 | <br />- vars （Object）<br />   - `all` 检测所有变量，包括全局环境中的变量。这是默认值。<br />   - `local` 仅仅检测本作用域中声明的变量是否使用，允许不使用全局环境中的变量。<br />- args（Object）<br />   - `after-used` - 不检查最后一个使用的参数之前出现的未使用的位置参数，但是检查最后一个使用的参数之后的所有命名参数和所有位置参数。<br />   - `all` - 所有命名参数必须使用。<br />   - `none` - 不检查参数。<br /> |  |
| [no-empty](http://eslint.cn/docs/rules/no-empty) | 禁止空块语句 | 支持的选项：<br />- `{ "allowEmptyCatch": true }`<br /> |  |
| [no-multi-spaces](http://eslint.cn/docs/rules/no-multi-spaces) | 禁止使用多个空格 |  |  |
| [no-trailing-spaces](http://eslint.cn/docs/rules/no-trailing-spaces) | 禁用行尾空格 |  | √ |
| [no-empty-function](no-empty-function) | 禁止出现空函数 | 使用 `allow` 选项选择性地开启某些内心的函数：<br />- `{ "allow": ["functions", "arrowFunctions"] }`<br /> |  |
| [no-empty-pattern](http://eslint.cn/docs/rules/no-empty-pattern) | 禁止使用空解构模式 |  |  |
| [no-multiple-empty-lines](http://eslint.cn/docs/rules/no-multiple-empty-lines) | 禁止出现多行空行 | <br />- `"max"` (默认为 `2`) 强制最大连续空行数。<br />- `"maxEOF"` 强制文件末尾的最大连续空行数。<br />- `"maxBOF"` 强制文件开始的最大连续空行数。<br /> | √ |
| [no-mixed-spaces-and-tabs](http://eslint.cn/docs/rules/no-mixed-spaces-and-tabs) | 禁止空格和 tab 的混合缩进 |  |  |
| [no-constant-condition](http://eslint.cn/docs/rules/no-constant-condition) | 禁止在条件中使用常量表达式 |  |  |
| [no-case-declarations](http://eslint.cn/docs/rules/no-case-declarations) | 不允许在 case 子句中使用词法声明 |  |  |
| [no-console](http://eslint.cn/docs/rules/no-console) | 禁用 `console` | 使用以下属性可以开启某些方法：<br />- `{ "allow": ["warn", "error"] }` <br /> |  |
| [no-debugger](http://eslint.cn/docs/rules/no-debugger) | 禁用 `debugger` |  |  |
| [no-alert](http://eslint.cn/docs/rules/no-alert) | 禁用 `alert`、`confirm` 和 `prompt` |  |  |
| [no-div-regex](http://eslint.cn/docs/rules/no-div-regex) | 禁止除法操作符显式的出现在正则表达式开始的位置 |  | √ |
| [no-unneeded-ternary](http://eslint.cn/docs/rules/no-unneeded-ternary) | 禁止可以在有更简单的可替代的表达式时使用三元操作符 |  | √ |
| [no-whitespace-before-property](http://eslint.cn/docs/rules/no-whitespace-before-property) | 禁止属性前有空白 |  | √ |
| [no-useless-computed-key](http://eslint.cn/docs/rules/no-useless-computed-key) | 禁止在对象中使用不必要的计算属性 |  | √ |
| [no-useless-constructor](http://eslint.cn/docs/rules/no-useless-constructor) | 禁用不必要的构造函数 |  |  |
| [nonblock-statement-body-position](http://eslint.cn/docs/rules/nonblock-statement-body-position) | 强制单个语句的位置 | <br />- `"beside"` (默认) 禁止单行语句之前有换行。<br />- `"below"` 要求单行语句之前有换行。<br />- `"any"` 不强制单行语句的位置。<br /> | √ |
| [object-curly-newline](http://eslint.cn/docs/rules/object-curly-newline) | 强制大括号内换行符的一致性 | <br />- `"always"` 要求花括号内有换行符<br />- `"never"` 禁止花括号内有换行符<br />
对象选项：<br />- `"multiline": true` 如果在属性内部或属性之间有换行符，就要求有换行符<br />- `"minProperties"` 如果属性的数量至少为给定的数值，要求有换行符。默认情况下，如果一个对象包含换行符并且属性的数量少于给定的数量，该规则也会报错误。然而，如果设置 `consistent` 选项为 `true`，则该选项将不起作用。<br />- `"consistent": true` (默认)要求使用花括号，或者不使用或括号直接使用换行。注意启用该选项将改变 `minProperties` 选项的行为。<br /> | √ |
| [<br />object-curly-spacing](http://eslint.cn/docs/rules/object-curly-spacing) | 强制在大括号中使用一致的空格 | <br />- `"never"` (默认) 不允许花括号中有空格<br />- `"always"` 要求花括号内有空格 (除了 `{}`)<br />
对象选项：<br />- `"arraysInObjects": true` 要求以数组元素开始或结尾的对象的花括号中有空格 (当第一个选项为 `never` 时生效)<br />- `"arraysInObjects": false` 禁止以数组元素开始或结尾的对象的花括号中有空格 (当第一个选项为 `always` 时生效)<br />- `"objectsInObjects": true` 要求以对象元素开始或结尾的对象的花括号中有空格 (当第一个选项为 `never` 时生效)<br />- `"objectsInObjects": false` 禁止以对象元素开始或结尾的对象的花括号中有空格 (当第一个选项为 `always` 时生效)<br /> | √ |
| [object-shorthand](http://eslint.cn/docs/rules/object-shorthand) | 要求或禁止对象字面量中方法和属性使用简写语法 | <br />- `"always"` (默认) 只要有可能，简写就应该被使用。<br />- `"methods"` 保证方法简写被使用（同样适用于 generators ）。<br />- `"properties"` 保证属性简写被使用 (键和变量名称相匹配的情况).<br />- `"never"` 保证对象字面量中的任何属性和方法都不使用简写。<br />- `"consistent"` 保证对象字面量的简写或非简写一致性。<br />- `"consistent-as-needed"` 保证对象字面量的简写或非简写一致性，但尽可能的全部使用简写。<br /> | √ |
| [prefer-arrow-callback](http://eslint.cn/docs/rules/prefer-arrow-callback) | 要求回调函数使用箭头函数 | <br />- `{ allowNamedFunctions: false, allowUnboundThis: true }`<br /> | √ |
| [array-bracket-spacing](http://eslint.cn/docs/rules/array-bracket-spacing) | 强制数组方括号中使用一致的空格 | <br />- `"never"` (默认) 禁止在数组括号内出现空格<br />- `"always"` 要求在数组括号内使用一个或多个空格、或折行<br />
对于`"never"`选项，可以有例外情况，用一个对象表示：<br />- `"singleValue": true` 要求在只包含一个元素的数组的括号内使用一个或多个空格、或折行<br />- `"objectsInArrays": true` 要求在数组的方括号和数组内的对象元素的大括号之间，即`[ {` 或 `} ]`，使用一个或多个空格、或折行<br />- `"arraysInArrays": true` 要求在数组的方括号和数组内的数组元素的方括号之间，即`[ [` 或 `] ]`，使用一个或多个空格、或折行<br />
对于`"always"`选项，可以有例外情况，用一个对象表示：<br />- `"singleValue": false` 禁止在只包含一个元素的数组的括号内使用空格<br />- `"objectsInArrays": false` 禁止在数组的方括号和数组内的对象元素的大括号之间，即 `[{` 或 `}]`出现空格<br />- `"arraysInArrays": false` 禁止在数组的方括号和数组内的数组元素的方括号之间，即 `[[` 或 `]]`出现空格<br />
该规则有两个内置的例外情况：<br />- `"never"` (和 `"always"` 选项的例外情况) 允许在数组内出现折行，因为这是一种常见的模式<br />- `"always"` 在空数组中`[]`不要求出现空格或折行<br /> | √ |
| [comma-dangle](http://eslint.cn/docs/rules/comma-dangle) | 要求或禁止末尾逗号 | <br />- `"never"` (默认) 禁用拖尾逗号<br />- `"always"` 要求使用拖尾逗号<br />- `"always-multiline"` 当最后一个元素或属性与闭括号 `]` 或 `}` 在 _不同的行_时，要求使用拖尾逗号；当在 _同一行_时，禁止使用拖尾逗号。<br />- `"only-multiline"` 当最后一个元素或属性与闭括号 `]` 或 `}` 在 _不同的行_时，允许（但不要求）使用拖尾逗号；当在 _同一行_时，禁止使用拖尾逗号。<br /> | √ |
| [comma-style](http://eslint.cn/docs/rules/comma-style) | 强制使用一致的逗号风格 |  | √ |
| [<br />consistent-return](http://eslint.cn/docs/rules/consistent-return) | 要求 `return` 语句要么总是指定返回的值，要么不指定 |  |  |
| [<br />prefer-object-spread](http://eslint.cn/docs/rules/prefer-object-spread) | 禁止使用以对象字面量作为第一个参数的 Object.assign，优先使用对象扩展。 |  | √ |
| [quote-props](http://eslint.cn/docs/rules/quote-props) | 要求对象字面量属性名称用引号括起来 | <br />- `"always"` (默认) 要求对象字面量属性名称都使用引号<br />- `"as-needed"` 当没有严格要求时，禁止对象字面量属性名称使用引号<br />- `"consistent"` 要求对象字面量属性名称使用一致的引号，要么全部用引号，要么都不用<br />- `"consistent-as-needed"` 如果有属性名称要求使用引号，则所有的属性名称都要使用引号；否则，禁止所有的属性名称使用引号<br /> | √ |
| <br /><br />[for-direction](http://eslint.cn/docs/rules/for-direction)<br /> | 强制 “for” 循环中更新子句的计数器朝着正确的方向移动 |  |  |
| [linebreak-style](http://eslint.cn/docs/rules/linebreak-style) | 强制使用一致的换行风格 | <br />- `"unix"` (LF)<br />- `"windows"` (CRLF)<br /> |  |
| [array-callback-return](http://eslint.cn/docs/rules/array-callback-return) | 强制数组方法的回调函数中有 `return` 语句 |  |  |
| [block-scoped-var](http://eslint.cn/docs/rules/block-scoped-var) | 强制把变量的使用限制在其定义的作用域范围内 |  |  |
| [default-case](http://eslint.cn/docs/rules/default-case) | 要求 `switch` 语句中有 `default` 分支 |  |  |
| [line-comment-position](http://eslint.cn/docs/rules/line-comment-position) | 强制行注释的位置 | <br />- `above` (默认) 强制行注释只在代码上方，单独成行。<br />- `beside` 强制行注释只在代码行后面。<br /> |  |
| [lines-around-comment](http://eslint.cn/docs/rules/lines-around-comment) | 要求在注释周围有空行 | <br />- `"beforeBlockComment": true` (默认) 要求在块级注释之前有一空行<br />- `"beforeBlockComment": false` 禁止在块级注释之前有一空行<br />- `"afterBlockComment": true` 要求在块级注释之后有一空行<br />- `"beforeLineComment": true` 要求在行级注释之前有一空行<br />- `"afterLineComment": true` 要求在行级注释之后有一空行<br />- `"allowBlockStart": true` 允许注释出现在块语句的开始位置<br />- `"allowBlockEnd": true` 允许注释出现在块语句的结束位置<br />- `"allowObjectStart": true` 允许注释出现在对象字面量的开始位置<br />- `"allowObjectEnd": true` 允许注释出现在对象字面量的结束位置<br />- `"allowArrayStart": true` 允许注释出现在数组字面量的开始位置<br />- `"allowArrayEnd": true` 允许注释出现在数组字面量的结束位置<br />- `"allowClassStart": true` 允许注释出现在类的开始位置<br />- `"allowClassEnd": true` 允许注释出现在类的结束位置<br />- `"applyDefaultIgnorePatterns"` 启用或禁用该规则忽略的默认注释模式<br />- `"ignorePattern"` 被该规则忽略的自定义模式<br /> | √ |
| [multiline-comment-style](http://eslint.cn/docs/rules/multiline-comment-style) | 强制对多行注释使用特定风格 | <br />- `"starred-block"` (默认): 禁止使用连续的行注释来表示块注释。另外，要求块注释的每行之前有一个 `*`。<br />- `"bare-block"`: 禁止使用连续的行注释来表示块注释，并且禁止块注释每行前有一个`"*"`。<br />- `"separate-lines"`: 禁用块注释，使用连续的行注释。<br /> |  |
| [lines-between-class-members](http://eslint.cn/docs/rules/lines-between-class-members) | 要求或禁止类成员之间出现空行 | <br />- `"always"`(默认) 要求在类成员之后有一行空行<br />- `"never"` 禁止在类成员之后有一行空行<br /> | √ |
| [one-var-declaration-per-line](http://eslint.cn/docs/rules/one-var-declaration-per-line) | 要求或禁止在变量声明周围换行 | <br />- `"initializations"` (默认) 强制每个变量初始化语句换行<br />- `"always"` 强制每个变量声明都换行<br /> | √ |
| [one-var](http://eslint.cn/docs/rules/one-var) | 强制函数中的变量要么一起声明要么分开声明 | <br />- `"always"` (默认) 要求每个作用域有一个变量声明<br />- `"never"` 要求每个作用域有多个变量声明<br />- `"consecutive"` 每个作用域允许出现多个变量声明，但对连续的变量声明要求合并为单个声明<br /> | √ |


<a name="WymER"></a>
### 全局变量
可以使用 `globals` 字段配置全局变量以避免报错，比如在uniapp和小程序中：
```javascript
{
  "globals": {
		"wx": "readonly",
		"uni": "readonly"
  }
}
```

全局变量的配置参数包括 `readonly` `writable` `off` ：
```bash
{
    "globals": {
        "var1": "writable",
        "var2": "readonly",
        "var3": "off"
    }
}
```

其中：

- `false` 与 `readonly` 和 `readable` 等价
- `true` 与 `writable` 和 `writeable` 等价

详细文档参考：[specifying-globals](http://eslint.cn/docs/user-guide/configuring#specifying-globals)

<a name="hx0OV"></a>
## 自动修复
使用以下命令可以自动修复eslint错误：
```bash
npx eslint --fix src
```

<a name="E71ML"></a>
## 文件忽略
将不需要检测的文件（夹）放于 `.eslintignore` 内容中即可。


<a name="nUrr2"></a>
## 注释
<a name="qN6rj"></a>
### 添加/重写规则
为了在文件注释里配置规则，使用以下格式的注释添加或重写规则：
```javascript
/* eslint eqeqeq: "off", curly: "error" */
/* eslint eqeqeq: 0, curly: 2 */
/* eslint quotes: ["error", "double"], curly: 2 */
```
在这个例子里，`eqeqeq` 规则被关闭，`curly` 规则被打开。 `quotes` 规则被打开，并指定需要使用双引号。

<a name="j00CZ"></a>
### 禁用/开启规则
使用 `eslint-disable` 注释禁用所有eslint规则，使用 `eslint-enable` 开启eslint规则。
```javascript
/* eslint-disable */

alert('foo');

/* eslint-enable */
```

如果只想要关闭/开启某一条/多条规则，只需要将规则名添加到后面即可：
```javascript
/* eslint-disable no-alert, no-console */

alert('foo');
console.log('bar');

/* eslint-enable no-alert, no-console */
```

当前行或下一行禁用规则：
```javascript
alert('foo'); // eslint-disable-line

// eslint-disable-next-line
alert('foo');

alert('foo'); /* eslint-disable-line no-alert */

/* eslint-disable-next-line no-alert */
alert('foo');
```


详细文档参考：[using-configuration-comments](http://eslint.cn/docs/user-guide/configuring#using-configuration-comments)

<a name="FVpaC"></a>
## 插件
在配置文件里配置插件时，可以使用 `plugins` 关键字来存放插件名字的列表。插件名称可以省略 `eslint-plugin-` 前缀。
```json
{
    "plugins": [
        "plugin1",
        "eslint-plugin-plugin2"
    ]
}
```

详细文档参考：[configuring-plugins](http://eslint.cn/docs/user-guide/configuring#configuring-plugins)

<a name="vPrCp"></a>
### 示例：使用 [eslint-plugin-vue](https://eslint.vuejs.org/) 插件
通过vue-cli3安装：
```bash
vue add @vue/cli-plugin-eslint
```
手动安装：
```bash
yarn add -D eslint eslint-plugin-vue
```

配置：
```javascript
module.exports = {
  extends: [
    // add more generic rulesets here, such as:
    // 'eslint:recommended',
    'plugin:vue/vue3-recommended',
    // 'plugin:vue/recommended' // Use this if you are using Vue.js 2.x.
  ],
  rules: {
    // override/add rules settings here, such as:
    // 'vue/no-unused-vars': 'error'
  }
}
```

<a name="QRCbR"></a>
## 错误解决
<a name="xZHRv"></a>
### ESLint couldn't find the plugin "eslint-plugin-vue"
报错详情：
```bash
Oops! Something went wrong! :(

ESLint: 7.22.0

ESLint couldn't find the plugin "eslint-plugin-vue".

(The package "eslint-plugin-vue" was not found when loaded as a Node module from the directory "D:\quanzaiyu\projects\health_array_applet_uniapp".)

It's likely that the plugin isn't installed correctly. Try reinstalling by running the following:

    npm install eslint-plugin-vue@latest --save-dev

The plugin "eslint-plugin-vue" was referenced from the config file in "BaseConfig".

If you still can't figure out the problem, please stop by https://eslint.org/chat/help to chat with the team.
```
解决方案：<br />需要在项目中添加依赖：
```bash
yarn add -D eslint-plugin-vue@latest
```

