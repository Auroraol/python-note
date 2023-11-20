webpack 可以使用 [loader](https://www.webpackjs.com/concepts/loaders/) 来预处理文件, 用于对模块的源代码进行转换。这允许你打包除 JavaScript 之外的任何静态资源。你可以使用 Node.js 来很简单地编写自己的 loader。

loader 可以使你在 import 或"加载"模块时预处理文件。因此，loader 类似于其他构建工具中“任务(task)”，并提供了处理前端构建步骤的强大方法。loader 可以将文件从不同的语言（如 TypeScript）转换为 JavaScript，或将内联图像转换为 data URL。loader 甚至允许你直接在 JavaScript 模块中 import CSS文件！

loader 支持链式传递。能够对资源使用流水线(pipeline)。一组链式的 loader 将按照相反的顺序执行。loader 链中的第一个 loader 返回值给下一个 loader。在最后一个 loader，返回 webpack 所预期的 JavaScript。

官方推荐的 Loaders: [https://www.webpackjs.com/loaders/](https://www.webpackjs.com/loaders/)

<a name="28a769bc"></a>
## 规则配置
`module.rules` 允许你在 webpack 配置中指定多个 loader。 这是展示 loader 的一种简明方式，并且有助于使代码变得简洁。同时让你对各个 loader 有个全局概览, 使用 Loader 有以下几种写法：

<a name="8df3465c"></a>
### 使用字符串形式的Loader名称
```javascript
module.exports = {
  module: {
    rules: [
      { test: /\.css$/, use: 'css-loader' },
      { test: /\.ts$/, use: 'ts-loader' }
    ]
  }
};
```

如果使用多个Loader可以使用感叹号串联
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: 'style-loader!css-loader'
      },
    ]
  }
};
```

<a name="0314a8e2"></a>
### 使用数组串联多个Loader
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      }
    ]
  }
};
```

<a name="c2066bfe"></a>
### 使用对象形式指定, 可以带其他参数
```javascript
{
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          { loader: "style-loader" },
          {
            loader: "css-loader",
            options: {
              modules: true
            },
            exclude: /node_modules/,
            include: [
              path.resolve(__dirname, "vendor/styles")
            ]
          }
        ]
      }
    ]
  }
}
```

如果只使用一个Loader进行处理, options 和 loader 可以平铺：
```javascript
{
  test: /\.(eot|ttf|woff|woff2)$/,
  loader: 'url-loader',
  options: {
    limit: 10000
  }
}
```

<a name="aa81d14e"></a>
## 内联使用
可以在 `import` 语句或任何[等效于 "import" 的方式](https://www.webpackjs.com/api/module-methods)中指定 loader。使用 `!` 将资源中的 loader 分开。分开的每个部分都相对于当前目录解析。
```javascript
import Styles from 'style-loader!css-loader?modules!./styles.css';
```

通过前置所有规则及使用 `!`，可以对应覆盖到配置中的任意 loader。

选项可以传递查询参数，例如 `?key=value&foo=bar`，或者一个 JSON 对象，例如 `?{"key":"value","foo":"bar"}`。

<a name="505195ab"></a>
## module.rules 的常用选项

- **test** 规则匹配
- **exclude** 排除的文件(夹)
- **include** 包含的文件(夹)
- **loader** 使用单个Loader解析
- **use** 使用多个Loader解析
- **enforce** 可选 "pre" | "post"

<a name="57bfc2fd"></a>
## 常用文件的处理
<a name="h2sOs"></a>
### 样式
<a name="CSS"></a>
#### CSS
```bash
yarn add -D style-loader css-loader
```

其中：

- [style-loader](https://www.webpackjs.com/loaders/style-loader/) 将模块的导出作为样式添加到 DOM 中
- [css-loader](https://www.webpackjs.com/loaders/css-loader/) 解释(interpret) `@import` 和 `url()`，会 `import/require()` 后再解析(resolve)它们。

`webpack.config.js`
```javascript
const path = require('path');

module.exports = {
  entry: ["./src/index.js"],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  mode: 'production',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      }
    ]
  }
};
```

`src/index.js`
```javascript
import './index.css';
```

css-loader 带参数的配置：
```javascript
{
  loader: 'css-loader',
  options: {
    minimize: true || {/* CSSNano Options */},
    sourceMap: true
  }
}
```
参数：

- **minimize** 是否压缩, 布尔值或[CSSNano Options](http://cssnano.co/guides/)
- **sourceMap**
- **camelCase** 可选 true | 'dashes', 类名是否驼峰化

<a name="6T1EO"></a>
#### Less
```bash
yarn add -D less-loader less
```
其中：

- [less-loader](https://www.webpackjs.com/loaders/less-loader/) 加载和转译 LESS 文件

`webpack.config.js`
```javascript
module.exports = {
  ...
  module: {
    rules: [{
      test: /\.less$/,
      use: [{
        loader: "style-loader"
      }, {
        loader: "css-loader", options: {
          sourceMap: true
        }
      }, {
        loader: "less-loader", options: {
          sourceMap: true
        }
      }]
    }]
  }
};
```

<a name="Vusyx"></a>
#### Sass
```bash
yarn add -D sass-loader node-sass
```
其中：

- [sass-loader](https://www.webpackjs.com/loaders/sass-loader/) 加载和转译 SASS/SCSS 文件

`webpack.config.js`
```javascript
module.exports = {
  ...
  module: {
    rules: [{
      test: /\.scss$/,
      use: [{
          loader: "style-loader" // 将 JS 字符串生成为 style 节点
      }, {
          loader: "css-loader" // 将 CSS 转化成 CommonJS 模块
      }, {
          loader: "sass-loader" // 将 Sass 编译成 CSS
      }]
    }]
  }
};
```

<a name="8cS1P"></a>
#### Stylus
```bash
yarn add -D stylus-loader stylus
```
其中：

- [stylus-loader](https://github.com/shama/stylus-loader) 加载和转译 Stylus 文件

`webpack.config.js`
```javascript
module: {
  rules: [
    {
      test: /\.styl$/,
      use: [
        'style-loader',
        'css-loader',
        'stylus-loader'
      ],
    }
  ],
},
```

<a name="3mA9i"></a>
#### postcss-loader
```bash
yarn add -D postcss-loader
```
其中：

- [postcss-loader](https://www.webpackjs.com/loaders/postcss-loader/) 使用 PostCSS 加载和转译 CSS 文件

`webpack.config.js`
```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader',
          'postcss-loader'
        ]
      }
    ]
  }
}
```

<a name="F0RN6"></a>
### 脚本
<a name="q3SQR"></a>
#### JavaScript
使用 [babel-loader](https://github.com/babel/babel-loader), 将 ES6+ 转换为 ES5 的代码, 参考：<br />[📃 babel](https://www.yuque.com/xiaoyulive/front_end/uvdmf0?inner=64ed5f4e&view=doc_embed)

<a name="ZwioZ"></a>
#### TypeScript
```bash
yarn add -D typescript ts-loader
```
其中：

- ts-loader 将TypeScript转换为JavaScript

我们设置一个基本的配置，来支持 JSX，并将 TypeScript 编译到 ES5

[tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)
```json
{
  "compilerOptions": {
    "outDir": "./dist/",
    "noImplicitAny": true,
    "sourceMap": true,
    "module": "es6",
    "target": "es5",
    "jsx": "react",
    "allowJs": true
  }
}
```

`webpack.config.js`
```javascript
const path = require('path');

module.exports = {
  entry: './src/index.ts',
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.(ts|tsx)?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: [ '.tsx', '.ts', '.js' ]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};
```

**在 TypeScript 中导入其他资源**<br />要在 TypeScript 里使用非代码资源，我们需要告诉 TypeScript 如何兼容这些导入类型。首先，我们需要在项目里创建 `custom.d.ts` 文件，这个文件用来编写自定义的类型声明。让我们将 .svg 文件进行声明设置：

`custom.d.ts`
```typescript
declare module "*.svg" {
  const content: any;
  export default content;
}
```

这里，我们通过指定任何以 `.svg` 结尾的导入，并将模块的 content 定义为 any，将 SVG 声明一个新的模块。我们可以通过将类型定义为字符串，来更加显式地将它声明为一个 url。同样的理念适用于其他资源，包括 CSS, SCSS, JSON 等。

<a name="r1tVl"></a>
### 图片
<a name="AKCSx"></a>
#### file-loader
```bash
yarn add -D file-loader
```
其中：

- [file-loader](https://www.webpackjs.com/loaders/file-loader/) 将文件发送到输出文件夹，并返回（相对）URL

`webpack.config.js`
```javascript
module.exports = {
  ...
  module: {
      ...
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          'file-loader'
        ]
      }
    ]
  }
};
```

当使用 `import MyImage from './my-image.png'`，该图像将被处理并添加到 output 目录，并且 MyImage 变量将包含该图像在处理后的最终 url。当使用 css-loader 时，CSS 中的 `url('./my-image.png')` 会使用类似的过程去处理。loader 会识别这是一个本地文件，并将 './my-image.png' 路径替换为输出目录中图像的最终路径。html-loader 以相同的方式处理 `<img src="./my-image.png" />`。

<a name="YYUZO"></a>
#### url-loader
```bash
yarn add -D url-loader
```
其中：

- [url-loader](https://www.webpackjs.com/loaders/url-loader/) 像 file-loader 一样工作，但如果文件小于限制，可以返回 data URL

`webpack.config.js`
```javascript
module.exports = {
  ...
  module: {
      ...
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
              mimetype: 'image/png',
              fallback: 'file-loader'
            }
          }
        ]
      }
    ]
  }
};
```

参数：

- limit {Number} 大小限制(单位: 字节)
- mimetype {String} 文件类型
- fallback {String} 当文件大小超过限制调用的Loader

<a name="eFei5"></a>
#### image-webpack-loader
```bash
yarn add -D image-webpack-loader
```
其中：

- [image-webpack-loader](https://github.com/tcoopman/image-webpack-loader) 提供更多的可配置选项, 比如质量压缩等, 可以配合 `url-loader` 和 `file-loader` 使用

`webpack.config.js`
```javascript
module.exports = {
  ...
  module: {
      ...

      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
              mimetype: 'image/png',
              fallback: 'file-loader'
            }
          },
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: {
                progressive: true,
                quality: 65
              },
              // optipng.enabled: false will disable optipng
              optipng: {
                enabled: false,
              },
              pngquant: {
                quality: '65-90',
                speed: 4
              },
              gifsicle: {
                interlaced: false,
              },
              // the webp option will enable WEBP
              webp: {
                quality: 75
              }
            }
          },
        ]
      }
    ]
  }
};
```

参数：

- **mozjpeg** — Compress JPEG images
- **optipng** — Compress PNG images
- **pngquant** — Compress PNG images
- **svgo** — Compress SVG images
- **gifsicle** — Compress GIF images
- **webp** — Compress JPG & PNG images into WEBP

<a name="c9c4c301"></a>
### 静态资源
通常静态资源我们也使用 `url-loader` 进行处理, 比如字体文件：
```javascript
{
  test: /\.(eot|ttf|woff|woff2)$/,
  loader: 'url-loader',
  options: {
    limit: 10000
  }
}
```

在 CSS 中引入的字体将使用url-loader进行处理：
```css
 @font-face {
   font-family: 'MyFont';
   src:  url('./my-font.woff2') format('woff2'),
         url('./my-font.woff') format('woff');
   font-weight: 600;
   font-style: normal;
 }

.hello {
  color: red;
  font-family: 'MyFont';
  background: url('./icon.png');
}
```

<a name="8ef83f77"></a>
### 数据
JSON 数据导入是内置的，不需要Loader进行处理, CSV、TSV 和 XML等数据需要特定的 Loader 进行处理：
```bash
yarn add -D csv-loader xml-loader
```

`webpack.config.js`
```javascript
{
  test: /\.(csv|tsv)$/,
  use: [
    'csv-loader'
  ]
},
{
  test: /\.xml$/,
  use: [
    'xml-loader'
  ]
}
```

创建一个 xml：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Mary</to>
  <from>John</from>
  <heading>Reminder</heading>
  <body>Call Cindy on Tuesday</body>
</note>
```

在JS中引入：
```javascript
import Data from './data.xml';
console.log(Data);
```

<a name="1cf481e0"></a>
### 代码检查

- [eslint-loader](https://github.com/webpack-contrib/eslint-loader) PreLoader，使用 ESLint 清理代码

<a name="816da5d0"></a>
### 框架相关

- [vue-loader](https://github.com/vuejs/vue-loader) 加载和转译 Vue 组件

<a name="35808e79"></a>
## 参考资料

- [module.rules](https://www.webpackjs.com/configuration/module/#module-rules)
- [Webpack Loaders](https://www.webpackjs.com/loaders/)
- [Awesome Webpack](https://github.com/webpack-contrib/awesome-webpack#loaders)
- [webpack指南 TypeScript](https://www.webpackjs.com/guides/typescript/)

