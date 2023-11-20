webpack 编译器(compiler)能够识别遵循 ES2015 模块语法、CommonJS 或 AMD 规范编写的模块。然而，一些第三方的库(library)可能会引用一些全局依赖（例如 jQuery 中的 $）。这些库也可能创建一些需要被导出的全局变量。这些“不符合规范的模块”就是 shimming 发挥作用的地方。

shimming 另外一个使用场景就是，当你希望 polyfill 浏览器功能以支持更多用户时。在这种情况下，你可能只想要将这些 polyfills 提供给到需要修补(patch)的浏览器（也就是实现按需加载）。

<a name="9b8acba1"></a>
## 引入全局变量
通过 [ProvidePlugin](https://www.webpackjs.com/plugins/provide-plugin) 插件可以引入全局变量:

`webpack.config.js`
```javascript
const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new webpack.ProvidePlugin({
      _: 'lodash'
    })
  ]
};
```

这样的话，在源码中就可以直接使用 `_` 而不必引入 lodash 了：
```javascript
// import _ from 'lodash';
_.join(['hello', 'webpack'], ' ');
```

我们还可以使用 ProvidePlugin 暴露某个模块中单个导出值，只需通过一个“数组路径”进行配置（例如 [module, child, ...children?]）。所以，让我们做如下设想，无论 join 方法在何处调用，我们都只会得到的是 lodash 中提供的 join 方法。

```javascript
new webpack.ProvidePlugin({
  join: ['lodash', 'join']
})
```

这样就能很好的与 tree shaking 配合，将 lodash 库中的其他没用到的部分去除。

<a name="b3e98514"></a>
## 全局 exports
假设有那么一个文件, 没有任何 export 语句：

`global.js`
```javascript
var file = 'blah.txt';
var helpers = {
  test: function() { console.log('test something'); },
  parse: function() { console.log('parse something'); }
}
```

我们想要引入这个文件里的某些变量或方法：
```javascript
import { file, parse } from './globals.js';
```

显然这是不可行的，但是我们可以通过 [exports-loader](https://www.webpackjs.com/loaders/exports-loader/) 实现这一需求：
```javascript
rules: [
  {
    test: require.resolve('globals.js'),
    use: 'exports-loader?file,parse=helpers.parse'
  }
]
```

<a name="5575f4cc"></a>
## 细粒度 shimming
一些传统的模块依赖的 this 指向的是 window 对象：

`index.js`
```javascript
function test() {
  // Assume we are in the context of `window`
  this.alert('Hmmm, this probably isn\'t a great idea...')
}
```

但是当此模块运行于 CommonJS 环境下将不可行, 因为此时 this 将指向 `module.exports`

我们可以通过 [imports-loader](https://www.webpackjs.com/loaders/imports-loader/) 改变这一指向：
```javascript
rules: [
  {
    test: require.resolve('index.js'), // 只在 index.js 中起效
    use: 'imports-loader?this=>window'
  },
]
```

