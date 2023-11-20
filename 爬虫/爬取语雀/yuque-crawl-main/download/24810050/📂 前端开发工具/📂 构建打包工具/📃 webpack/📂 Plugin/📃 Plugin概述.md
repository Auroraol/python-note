<a name="html-webpack-plugin"></a>
## 常用的插件
<a name="xUv04"></a>
### html-webpack-plugin
[html-webpack-plugin](https://github.com/jaketrent/html-webpack-template) 用于帮助我们自动生成 `index.html`，以自动关联入口文件。

安装：
```bash
yarn add -D html-webpack-plugin
```

使用：
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Output Management'
    })
  ],
};
```

指定模板：
```javascript
new HtmlWebpackPlugin({ template: './src/index.html' })
```

<a name="dcEbN"></a>
### clean-webpack-plugin
[clean-webpack-plugin](https://github.com/johnagan/clean-webpack-plugin) 用于在每次构建前清理 /dist 文件夹。

安装：
```bash
yarn add -D clean-webpack-plugin
```

使用：
```javascript
const path = require('path');
const {
  CleanWebpackPlugin
} = require('clean-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new CleanWebpackPlugin()
  ],
};
```

<a name="Nfrdv"></a>
### webpack-manifest-plugin
通过 [webpack-manifest-plugin](https://github.com/danethurber/webpack-manifest-plugin) 可以生成一个 `manifest.json` 文件以追踪生成的文件。

安装：
```bash
yarn add -D webpack-manifest-plugin
```

使用：
```javascript
const path = require('path');
const ManifestPlugin = require('webpack-manifest-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new ManifestPlugin(),
  ],
};
```

生成的 `manifest.json` 类似：
```json
{
  "main.js": "main.bundle.js",
  "index.html": "index.html"
}
```

<a name="u2clz"></a>
### workbox-webpack-plugin
使用 [workbox-webpack-plugin](https://github.com/byara/workbox-webpack-plugin) 可以方便地创建一个 PWA 应用。

安装：
```bash
yarn add -D workbox-webpack-plugin
```

使用：
```javascript
const WorkboxPlugin = require('workbox-webpack-plugin');

module.exports = {
  plugins: [
    new WorkboxPlugin.GenerateSW({
      // 这些选项帮助 ServiceWorkers 快速启用
      // 不允许遗留任何“旧的” ServiceWorkers
      clientsClaim: true,
      skipWaiting: true
    })
  ],
};
```

注册 `Service Worker`：<br />`index.js`
```javascript
import _ from 'lodash';
import printMe from './print.js';

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js').then(registration => {
      console.log('SW registered: ', registration);
    }).catch(registrationError => {
      console.log('SW registration failed: ', registrationError);
    });
  });
}
```

生成后, 可以看到 dist 中添加了 `service-worker.js` 和 `precache-manifest.xxx.js`

:::warning
PWA 只有在 HTTPS 或 `http://localhost` 下才能正常运行
:::

参考: [添加 Workbox](https://www.webpackjs.com/guides/progressive-web-application/#%E6%B7%BB%E5%8A%A0-workbox)

<a name="p0OXj"></a>
### DefinePlugin
DefinePlugin 用于定义环境变量
```javascript
import webpack from 'webpack';

export default {
  ...
  plugins: [
    // 该插件帮助我们安心地使用环境变量
    new webpack.DefinePlugin({
      'process.env.ASSET_PATH': JSON.stringify('/')
    })
  ]
};
```

<a name="35808e79"></a>
## 参考资料

- [Webpack Plugins](https://www.webpackjs.com/plugins/)
- [Awesome Webpack](https://github.com/webpack-contrib/awesome-webpack#webpack-plugins)

