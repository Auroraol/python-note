<a name="http-server"></a>
## http-server
如果我们想要通过http运行dist目录里面的资源而不是直接双击打开的话, 我们需要一个http服务器：
```bash
yarn add -D http-server
```

修改package.json
```json
{
  "scripts": {
    "build": "webpack",
    "start": "http-server dist"
  },
}
```

这样, 我们就可以通过 `yarn start` 直接运行编译好的 dist 下的资源了

<a name="webpack-dev-middleware"></a>
## webpack-dev-middleware
可以通过 [webpack-dev-middleware](https://github.com/webpack/webpack-dev-middleware) 结合 Express 创建服务器脚本：
```bash
yarn add -D express webpack-dev-middleware
```

但是使用以下脚本创建的服务，更新代码需要手动刷新浏览器
```javascript
const express = require('express');
const webpack = require('webpack');
const webpackDevMiddleware = require('webpack-dev-middleware');

const app = express();
const config = require('./webpack.config.js');
const compiler = webpack(config);

app.use(webpackDevMiddleware(compiler, {
  publicPath: config.output.publicPath
}));

app.listen(3000, function () {
  console.log('Example app listening on port 3000!\n');
});
```

这样创建的服务，会监听文件的变化，但是需要手动刷新浏览器。


