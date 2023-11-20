我们的目的是：使用自己创建的 Loader 解析 test.txt, 将其内容首字母转化为大写并倒序输出

<a name="9d93e275"></a>
## 创建目录结构
```bash
/
├─config
│  ├─loaders
│  │  ├─uppercase-first-loader.js
│  │  └─reverse-text-loader.js
│  └─webpack.config.js
├─src
│  ├─index.js
│  └─test.txt
└─package.json
```

<a name="a2357c8c"></a>
## Loader 的基本结构
```javascript
module.exports = function(src){
  // 可以通过 this 访问Loader API
  // this是由webpack提供的，可以直接使用
}
```

`src` 为输入的内容, 这里就是 test.txt 的内容

<a name="40714252"></a>
## 修改必要文件
`package.json`
```json
{
  "scripts": {
    "build": "webpack --config config/webpack.config.js",
  },
}
```

`src/index.js`
```javascript
import text from './test.txt'
console.log(text);
```

`src/test.txt`
```
hello world
```

<a name="6399698d"></a>
## 创建Loader

- `uppercase-first-loader.js` 用于将第一个字母转换为大写。
- `reverse-text-loader.js` 用于将文件内容倒序输出。

`config/loaders/uppercase-first-loader.js`
```javascript
module.exports = function (src) {
  // 因为是第一个loader，所以src是原文件内容（abcde），下面对内容进行处理，这里首字符大写
  if (!src) {
    return '';
  }
  // 返回结果给下一个loader
  return src.charAt(0).toUpperCase() + src.slice(1);
}
```

`config/loaders/reverse-text-loader.js`
```javascript
module.exports = function (src) {
  // src是原文件内容，下面对内容进行处理，这里是反转
  var result = src.trim().split('').reverse().join('');

  // 返回JavaScript源码，必须是String或者Buffer
  // this.callback(null, `module.exports = \`${result}\``);
  // return;

  return `module.exports = \`${result}\``
}
```

这里的返回值有两种写法, 直接 return 一个字符串, 或者通过 `this.callback` 输出

<a name="b2c95264"></a>
## 引入Loader
`config/webpack.config.js`
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const resolveLoader = (loaderPath) => {
  return path.resolve(__dirname, "loaders", loaderPath);
}

module.exports = {
  entry: {
    app: './src/index.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, '..', 'dist')
  },
  mode: 'production',
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Index'
    }),
  ],
  module: {
    rules: [
      {
        test: /\.txt$/,
        use: [
          resolveLoader('reverse-text-loader'),
          resolveLoader('uppercase-first-loader'),
        ]
      },
    ]
  }
};
```

注意两个Loader的顺序，由于是从下往上加载的，所以 uppercase-first-loader 的输出值为 reverse-text-loader 的输入值，也就是为什么通过 uppercase-first-loader 转化后的输出值是一个普通字符串, 而通过 reverse-text-loader 转化的后的值是一个套了 `module.exports = ...` 的字符串，在 index.js 中引入的其实是转化为 js 后的字符串。

浏览器打开 `dist/index.html`, 可以看到控制台输出 `dlrow olleH`

至此，一个简单的Loader就完成了。这里只是示例。实际情况肯定比这复杂得多。

<a name="35808e79"></a>
## 参考资料

- [编写一个 loader](https://www.webpackjs.com/contribute/writing-a-loader/)
- [loader API](https://www.webpackjs.com/api/loaders/)

