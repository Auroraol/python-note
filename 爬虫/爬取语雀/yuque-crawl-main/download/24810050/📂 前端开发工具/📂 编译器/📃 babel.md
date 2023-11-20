<a name="e05dce83"></a>
## 简介
Babel 是一个 JavaScript 编译器，主要用于将 ECMAScript 2015+ 版本的代码转换为向后兼容的 JavaScript 语法，以便能够运行在当前和旧版本的浏览器或其他环境中。下面列出的是 Babel 能为你做的事情：

- 语法转换
- 通过 Polyfill 方式在目标环境中添加缺失的特性 (通过 `@babel/polyfill` 模块)
- 源码转换 (codemods)

相关站点：

- [Babel 官网](https://babeljs.io/)
- [Babel 中文网](https://www.babeljs.cn/)
- [Babel 插件开发指南](https://github.com/brigand/babel-plugin-handbook/blob/master/translations/zh-Hans/README.md#asts)
- [@babel/parser (babylon) AST node types](https://github.com/babel/babel/blob/master/packages/babel-parser/ast/spec.md)
- [babel-types definitions](https://github.com/babel/babel/tree/master/packages/babel-types/src/definitions)

<a name="babel-cli"></a>
## babel-cli
Babel 自带了一个内置的 [CLI](https://www.babeljs.cn/docs/babel-cli) 命令行工具，可通过命令行编译文件。

安装：
```bash
yarn add @babel/core @babel/cli @babel/preset-env
```

package.json 中增加：
```json
{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "babel src -d lib",
    "dev": "babel src -w -d lib"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@babel/cli": "^7.5.5",
    "@babel/core": "^7.5.5",
    "@babel/preset-env": "^7.5.5"
  }
}
```

运行 build 命令，将把 src 中的源文件编译到 lib。运行 dev 命令，将监听文件的变化，实时编译输出。

增加 babel 配置文件 `.babelrc`
```json
{
  "presets": ["@babel/preset-env"]
}
```

测试：<br />创建 `src/test.js`
```javascript
let func = a => {
  console.log(a);
};
```

运行 `yarn build`, 可以看到新增了 `lib/test.js`
```javascript
"use strict";

var func = function func(a) {
  console.log(a);
};
```

可以看到，已经将 ES6 代码编译为 ES5 了

<a name="0dfbe902"></a>
### 常用命令
完整的babel参数列表如下：
```bash
$ npx babel --help
Usage: babel [options] <files ...>

Options:
  -f, --filename [filename]                   The filename to use when reading from stdin. This will be used in source-maps, errors etc.
  --presets [list]                            A comma-separated list of preset names.
  --plugins [list]                            A comma-separated list of plugin names.
  --config-file [path]                        Path to a .babelrc file to use.
  --env-name [name]                           The name of the 'env' to use when loading configs and plugins. Defaults to the value of BABEL_ENV, or else
                                              NODE_ENV, or else 'development'.
  --root-mode [mode]                          The project-root resolution mode. One of 'root' (the default), 'upward', or 'upward-optional'.
  --source-type [script|module]
  --no-babelrc                                Whether or not to look up .babelrc and .babelignore files.
  --ignore [list]                             List of glob paths to **not** compile.
  --only [list]                               List of glob paths to **only** compile.
  --no-highlight-code                         Enable or disable ANSI syntax highlighting of code frames. (on by default)
  --no-comments                               Write comments to generated output. (true by default)
  --retain-lines                              Retain line numbers. This will result in really ugly code.
  --compact [true|false|auto]                 Do not include superfluous whitespace characters and line terminators.
  --minified                                  Save as many bytes when printing. (false by default)
  --auxiliary-comment-before [string]         Print a comment before any injected non-user code.
  --auxiliary-comment-after [string]          Print a comment after any injected non-user code.
  -s, --source-maps [true|false|inline|both]
  --source-map-target [string]                Set `file` on returned source map.
  --source-file-name [string]                 Set `sources[0]` on returned source map.
  --source-root [filename]                    The root from which all sources are relative.
  --module-root [filename]                    Optional prefix for the AMD module formatter that will be prepended to the filename on module definitions.
  -M, --module-ids                            Insert an explicit id for modules.
  --module-id [string]                        Specify a custom name for module ids.
  -x, --extensions [extensions]               List of extensions to compile when a directory has been the input. [.es6,.js,.es,.jsx,.mjs]
  --keep-file-extension                       Preserve the file extensions of the input files.
  -w, --watch                                 Recompile files on changes.
  --skip-initial-build                        Do not compile files before watching.
  -o, --out-file [out]                        Compile all input files into a single file.
  -d, --out-dir [out]                         Compile an input directory of modules into an output directory.
  --relative                                  Compile into an output directory relative to input directory or file. Requires --out-dir [out]
  -D, --copy-files                            When compiling a directory copy over non-compilable files.
  --include-dotfiles                          Include dotfiles when compiling and copying non-compilable files.
  --no-copy-ignored                           Exclude ignored files when copying non-compilable files.
  --verbose                                   Log everything. This option conflicts with --quiet
  --quiet                                     Don't log anything. This option conflicts with --verbose
  --delete-dir-on-start                       Delete the out directory before compilation.
  --out-file-extension [string]               Use a specific extension for the output files
  -V, --version                               output the version number
  -h, --help                                  output usage information
```
常用命令示例：
```bash
# 编译文件, 输出到标准输出设备（stdout）
npx babel script.js

# 输出到文件
npx babel script.js -o script-compiled.js

# 监测文件修改
npx babel script.js -w -o script-compiled.js

# 输出源码映射表
npx babel script.js -o script-compiled.js -s

# 输出内联源码映射表
npx babel script.js -o script-compiled.js -s inline

# 编译整个目录
npx babel src -d lib

# 编译整个 src 目录下的文件并将输出合并为一个文件
npx babel src -d script-compiled.js

# 忽略某些文件
npx babel src -d lib --ignore "src/**/*.spec.js","src/**/*.test.js"

# 拷贝不需要编译的文件
npx babel src -d lib --copy-files

# 通过 stdin 和管道（pipe）将文件内容传递给 babel 命令，并将编译结果输出到 script-compiled.js 文件
npx babel -o script-compiled.js < script.js

# 使用插件
npx babel script.js -o script-compiled.js --plugins=@babel/proposal-class-properties,@babel/transform-modules-amd

# 使用预设
npx babel script.js -o script-compiled.js --presets=@babel/preset-env,@babel/flow

# 忽略项目中的 .babelrc 配置文件，并通过命令行参数执行定制化的构建流程
npx babel --no-babelrc script.js -o script-compiled.js --presets=es2015,react
```

<a name="64ed5f4e"></a>
## 在webpack中使用
安装 [babel-loader](https://github.com/babel/babel-loader)
```bash
yarn add babel-loader
```

在 `webpack.config.js` 中添加
```javascript
module.exports = {
  module: {
    rules: [
      { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }
    ]
  }
}
```

同样还是得配置 `.babelrc`
```json
{
  "presets": ["@babel/preset-env"]
}
```

<a name="224e2ccd"></a>
## 配置
参考: [config-files](https://www.babeljs.cn/docs/config-files)

<a name="af87b4c9"></a>
### 配置文件
babel支持以下名称的配置文件：

- `.babelrc` (json)
- `babel.config.js` 或 `.babelrc.js` (js)
- `package.json` 中使用 `babel` 字段 (json)

示例：<br />`.babelrc` (json)
```json
{
  "presets": [
    ["@babel/preset-env", {
      "loose": true,
      "modules": false
    }]
  ]
}
```

`babel.config.js` 或 `.babelrc.js` (js)
```javascript
module.exports = {
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "esmodules": true,
        "node": process.versions.node
      }
    }]
  ]
}
```

<a name="1524f74f"></a>
### 配置写法
配置有以下几种写法：

`.babelrc`
```json
{
  "presets": [
    "presetA",
    ["presetB"],
    ["presetC", { "option1": true, "option2": false}],
  ],
  "plugins": [
    "my-plugin1",
    ["my-plugin2"],
    ["my-plugin3", { "option1": true, "option2": false }]
  ]
}
```

数组写法，比如：
```json
{
  "presets": [
    ["@babel/preset-env", {
      "loose": true,
      "modules": false
    }]
  ]
}
```

<a name="9cdfce42"></a>
## 预设
<a name="5b18a54e"></a>
### ES6 to ES5
这个前面已经说过了，安装 [@babel/preset-env](https://babeljs.io/docs/en/babel-preset-env) 即可，不赘述

参数：
```json
{
  "presets": [
    ["@babel/preset-env", {
      "targets": {
        "esmodules": true
      }
    }]
  ]
}
```

- `targets.esmodules` 是否支持ES Modules
- `targets.node` 指定 node的版本, 可选值如 `process.versions.node`、`true`、`"current"` 或 指定版本号
- `targets.safari` 支持的safari
- `targets.browsers` 支持的浏览器, 类型为 `string | Array<string>`, 参看 [browserslist](https://github.com/browserslist/browserslist)
- `loose` 默认false
- `modules` "amd" | "umd" | "systemjs" | "commonjs" | "cjs" | "auto" (默认) | false

<a name="e3278952"></a>
### 转换 JSX
需要安装 [@babel/preset-react](https://babeljs.io/docs/en/babel-preset-react)：
```bash
yarn add @babel/preset-react
```

配置 `.babelrc`
```json
{
  "presets": ["@babel/preset-react"]
}
```

测试，创建 `src/test.jsx`：
```jsx
export default React.createClass({
  getInitialState() {
    return {
      num: this.getRandomNumber()
    };
  },

  getRandomNumber() {
    return Math.ceil(Math.random() * 6);
  },

  render() {
    return <div>Your dice roll: {this.state.num} </div>;
  }
});
```

执行 `yarn build`, 生成 `lib/test.js`：
```javascript
export default React.createClass({
  displayName: "test",

  getInitialState() {
    return {
      num: this.getRandomNumber()
    };
  },

  getRandomNumber() {
    return Math.ceil(Math.random() * 6);
  },

  render() {
    return React.createElement(
      "div",
      null,
      "Your dice roll: ",
      this.state.num,
      " "
    );
  }
});
```

还可以指定多个 presets：
```json
{
  "presets": ["@babel/preset-react", "@babel/preset-env"]
}
```

这样转换出来的文件内容为：
```javascript
"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _default = React.createClass({
  displayName: "test",
  getInitialState: function getInitialState() {
    return {
      num: this.getRandomNumber()
    };
  },
  getRandomNumber: function getRandomNumber() {
    return Math.ceil(Math.random() * 6);
  },
  render: function render() {
    return React.createElement(
      "div",
      null,
      "Your dice roll: ",
      this.state.num,
      " "
    );
  }
});

exports["default"] = _default;
```

<a name="509cd1bd"></a>
### 转换 flow
需要安装 [@babel/preset-flow](https://babeljs.io/docs/en/babel-preset-flow)：
```bash
yarn add @babel/preset-flow
```

配置 `.babelrc`
```json
{
  "presets": ["@babel/preset-flow"]
}
```

测试, 创建 `src/test.js`：
```javascript
// @flow
function square(n: number): number {
  return n * n;
}
```

转化为：
```javascript
"use strict";

function square(n) {
  return n * n;
}
```

<a name="9548f920"></a>
### 转换 TypeScript
需要安装 [@babel/preset-typescript](https://babeljs.io/docs/en/babel-preset-typescript)：
```bash
yarn add @babel/preset-typescript
```

创建测试文件`test.ts`：
```typescript
function Greeter(greeting: string) {
  this.greeting = greeting;
}
```

执行 `npx babel --presets @babel/preset-typescript test.ts`, 输出：
```javascript
function Greeter(greeting) {
  this.greeting = greeting;
}
```

<a name="minify"></a>
### minify
使用 minify 可以将输出的代码进行压缩

安装：
```bash
yarn add babel-preset-minify
```

配置, `babel.config.js`：
```javascript
module.exports = {
  "presets": [
    "minify"
  ]
}
```

<a name="ployfill"></a>
## ployfill
Babel 预设只能进行语法的转换, 对于 ES6+ 新提供的一些API却是无能无力，比如 `Array.prototype.includes`, 我们可以使用 `@babel/polyfill` 解决

安装：
```bash
yarn add @babel/polyfill
```

<a name="5af1f17a"></a>
### 在 Node 中使用

1. 在需要转换的文件头部加入 `require("@babel/polyfill");`
2. 修改 `.babelrc.js`, 添加 `useBuiltIns`：
```javascript
module.exports = {
  "presets": [
    ["@babel/preset-env", {
      "useBuiltIns": "entry"
    }],
  ],
}
```

<a name="42076543"></a>
### 在 Browserify 中使用

1. 在需要转换的文件头部加入 `import "@babel/polyfill";`
2. 修改 `.babelrc.js`, 添加 `useBuiltIns: "entry"`

<a name="0e3cba30"></a>
### 在 Webpack 中使用
在 `webpack.config.js` 中添加
```javascript
module.exports = {
  entry: ["@babel/polyfill", "./app/js"],
};
```

