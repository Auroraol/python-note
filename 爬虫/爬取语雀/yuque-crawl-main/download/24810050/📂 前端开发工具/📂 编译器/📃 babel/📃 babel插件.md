<a name="79aa75de"></a>
## 插件安装与配置
安装插件, 比如：
```bash
yarn add babel-plugin-root-import
yarn add @babel/plugin-proposal-optional-chaining
```

配置插件：<br />`babel.config.js`
```javascript
module.exports = {
  plugins: [
    // 数组语法 [插件名, 配置选项]
    [
      "babel-plugin-root-import",
      {
        rootPathPrefix: "~",
        rootPathSuffix: "src"
      }
    ],
    // 字符串语法
    "@babel/plugin-proposal-optional-chaining"
  ]
};
```

如果插件是以 `babel-plugin` 开头的, 可以省略, 如：
```javascript
module.exports = {
  plugins: ["root-import"]
};
```

<a name="aa755661"></a>
### 插件选项
若你希望让你的用户自定义 Babel 插件的行为，你可以接收指定的选项：
```javascript
{
  plugins: [
    [
      "my-plugin",
      {
        option1: true,
        option2: false
      }
    ]
  ];
}
```

这些选项会通过 `state` 对象传递给插件的访问者（visitors）：
```javascript
export default function({ types: t }) {
  return {
    visitor: {
      FunctionDeclaration(path, state) {
        console.log(state.opts);
        // { option1: true, option2: false }
      }
    }
  };
}
```

这些选项是插件特定的，因此你不能从其他插件里访问到这些选项。

<a name="83169f72"></a>
## 一些有用的插件
<a name="babel-plugin-proposal-optional-chaining"></a>
### babel-plugin-proposal-optional-chaining
[@babel/babel-plugin-proposal-optional-chaining](https://babeljs.io/docs/en/babel-plugin-proposal-optional-chaining) 用于处理 `?.` 运算符, 参考 [在 JavaScript 中使用可选链和双问号](/categories/javascript/optional-chaining.html)

<a name="plugin-proposal-nullish-coalescing-operator"></a>
### plugin-proposal-nullish-coalescing-operator
[@babel/plugin-proposal-nullish-coalescing-operator](https://babeljs.io/docs/en/babel-plugin-proposal-nullish-coalescing-operator) 用于处理 `??` 运算符, 参考 [在 JavaScript 中使用可选链和双问号](/categories/javascript/optional-chaining.html)

<a name="plugin-proposal-decorators"></a>
### plugin-proposal-decorators
[@babel/plugin-proposal-decorators](https://babeljs.io/docs/en/babel-plugin-proposal-decorators) 用于处理装饰器, 参考 [在 JavaScript 中使用装饰器](/categories/javascript/decorator.html)

<a name="637bb74a"></a>
## 编写 Babel 插件
必要工具：
```bash
yarn add babel-core babel-types
```

<a name="f27f353c"></a>
### 插件结构
```javascript
export default function(babel) {
  return {
    visitor: {
      // visitor contents
    }
  };
}
```

直接取出 `babel.types` 会更方便：
```javascript
export default function({ types: t }) {
  return {
    visitor: {
      // visitor contents
    }
  };
}
```

<a name="004f94e1"></a>
### 示例：基础用法
```javascript
module.exports = function({ types: t }) { // 将插件导出
  return {
    visitor: {
      BinaryExpression(path) {
        if (path.node.operator !== "===") {
          return;
        }

        path.node.left = t.identifier("left");
        path.node.right = t.identifier("right");
      }
    }
  }
};
```

配置:
```javascript
module.exports = {
  plugins: ["test"]
};
```

比如有以下源码：
```javascript
console.log(a === b);
```

其 AST 形式如下：
```javascript
{
  type: "BinaryExpression",
  operator: "===",
  left: {
    type: "Identifier",
    name: "foo"
  },
  right: {
    type: "Identifier",
    name: "bar"
  }
}
```

将会转化为：
```javascript
console.log(left === right);
```

<a name="36e29447"></a>
### 示例：包引入替换
当我们导入 lodash 中指定的工具函数时，会将整个 lodash 打包进来：
```javascript
import { flattenDeep, chunk } from "lodash";
```

换成按需引入的写法，但是这样写有些麻烦，我们想由上面写法，自动分解为下面写法：
```javascript
import flattenDeep from "lodash/flattenDeep";
import chunk from "lodash/chunk";
```

所以我们就可以编写一个 babel 插件来实现这一点：
```javascript
const babel = require("babel-core");
const types = require("babel-types");

// Babel将源码转换AST之后，通过遍历AST树（其实就是一个js对象），对树做一些修改，然后再将AST转成code，即成源码。
let visitor = {
  // import 语句解析时触发该函数
  ImportDeclaration(path, ref = { opts: {} }) {
    // path 语句抽象语法树 opts 插件参数
    let node = path.node;
    let { specifiers } = node; // 导入的包的说明符, 是个数组集合
    // 确认导入库是否是 .babelrc library属性指定库, 以及, 如果不是默认导入, 才进行按需导入加载
    if (
      ref.opts.library === node.source.value &&
      !types.isImportDefaultSpecifier(specifiers[0])
    ) {
      let newImports = specifiers.map((
        specifier // 遍历出导入的每个包的说明描述符
      ) =>
        types.importDeclaration(
          [types.importDefaultSpecifier(specifier.local)],
          // 生成import语句，如 import chunk from 'library/chunk'
          types.stringLiteral(`${node.source.value}/${specifier.local.name}`)
        )
      );

      // 将原有语句写法替换为新写法
      path.replaceWithMultiple(newImports);
    }
  }
};

module.exports = function(babel) {
  return { visitor };
};
```

配置选项：
```json
{
  "plugins": [
    [
      "extract",
      {
        "library": "lodash"
      }
    ]
  ]
}
```

测试：运行 `npm run build`, 发现此时编译后的 `bundle.js` 变小了

如果只是对 lodash 做处理, 可以使用 [babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash)

<a name="35808e79"></a>
## 参考资料

- [Babel 插件编写](https://github.com/Brolly0204/babel-plugin-extract)

