vue-cli 官网: [https://cli.vuejs.org/zh/](https://cli.vuejs.org/zh/)

与 3.0 相比, 2.0 还是有一些令人满意的功能, 本人比较喜欢的是 2.0 可以自定义初始化模板, 而 3.0 必须引入 `@vue/cli-init` 包才行。

<a name="QgoaR"></a>
## 安装vue-cli 3.0
如果要使用 3.0, 必须卸载 2.0 才能进行安装。
```bash
$ yarn global remove vue-cli
```

安装 3.0 并创建项目
```bash
$ yarn global add @vue/cli
$ vue --version
$ vue create hello-world # 创建项目
$ vue add element # 安装模板
$ yarn serve # 运行程序
```

为了兼容 2.0, 3.0 版本提供了一个 `@vue/cli-init` 以集成自定义的初始化模板:
```bash
$ yarn global add @vue/cli-init
# `vue init` 的运行效果将会跟 `vue-cli@2.x` 相同
$ vue init webpack my-project
```

<a name="zdlgt"></a>
## 可视化操作

```bash
$ vue ui
🚀  Starting GUI...
🌠  Ready on http://localhost:8000
```

默认开启 8000 端口, 也可自定义端口访问:

```bash
$ vue ui -p 3000
```
![001.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589234841-e966836f-91c6-48c4-a13d-ca36aabfd807.png#align=left&display=inline&height=897&originHeight=897&originWidth=1259&size=30925&status=done&style=none&width=1259)<br />![002.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589259131-14da3c91-375a-4bd5-8bd8-1b157ddf93d1.png#align=left&display=inline&height=933&originHeight=933&originWidth=1900&size=104540&status=done&style=none&width=1900)<br />![003.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589270341-74712f59-2177-40da-bd0c-bff7cbc1d6af.png#align=left&display=inline&height=406&originHeight=406&originWidth=1901&size=60321&status=done&style=none&width=1901)<br />![004.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589280402-2e1a8d7e-6ab8-4118-a700-1d6c100264df.png#align=left&display=inline&height=773&originHeight=773&originWidth=1917&size=99907&status=done&style=none&width=1917)<br />![005.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589293828-e93f2b14-2f3e-4e06-b530-6f400d28e48c.png#align=left&display=inline&height=531&originHeight=531&originWidth=1899&size=41395&status=done&style=none&width=1899)<br />![006.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589302905-72004aa0-1039-45dd-b846-1d9815f5119b.png#align=left&display=inline&height=810&originHeight=810&originWidth=1915&size=87190&status=done&style=none&width=1915)<br />![007.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589312219-2451ce7f-9b92-48b3-a5d9-a336bb87837d.png#align=left&display=inline&height=735&originHeight=735&originWidth=911&size=37813&status=done&style=none&width=911)<br />![008.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589415198-7eb86ca5-1d23-4a83-b5ea-978619c49c18.png#align=left&display=inline&height=896&originHeight=896&originWidth=1325&size=107273&status=done&style=none&width=1325)<br />![009.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589419786-6fdeccfb-371b-4888-b421-f23f8977d205.png#align=left&display=inline&height=906&originHeight=906&originWidth=1379&size=88203&status=done&style=none&width=1379)

<a name="pVZHY"></a>
## vue-cli配置
在 Vue-cli3.0 脚手架搭建的项目中, webpack配置被集成到了 `vue.config.js` 中, 配置使用如下格式：
```javascript
const path = require('path')

module.exports = {
  publicPath: './', // 基本路径
  outputDir: 'dist', // 输出文件目录
  lintOnSave: false, // eslint-loader 是否在保存的时候检查
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md
  // webpack配置
  chainWebpack: (config) => {
  },
  configureWebpack: (config) => {
    if (process.env.NODE_ENV === 'production') {
      // 为生产环境修改配置...
      config.mode = 'production'
    } else {
      // 为开发环境修改配置...
      config.mode = 'development'
    }
    Object.assign(config, {
      // 开发生产共同配置
      resolve: {
        alias: {
          '@': path.resolve(__dirname, './src'),
          '@c': path.resolve(__dirname, './src/components'),
          '@p': path.resolve(__dirname, './src/pages')
        } // 别名配置
      }
    })
  },
  productionSourceMap: false, // 生产环境是否生成 sourceMap 文件
  // css相关配置
  css: {
    extract: true, // 是否使用css分离插件 ExtractTextPlugin
    sourceMap: false, // 开启 CSS source maps?
    loaderOptions: {
      css: {}, // 这里的选项会传递给 css-loader
      postcss: {} // 这里的选项会传递给 postcss-loader
    }, // css预设器配置项 详见https://cli.vuejs.org/zh/config/#css-loaderoptions
    modules: false // 启用 CSS modules for all css / pre-processor files.
  },
  parallel: require('os').cpus().length > 1, // 是否为 Babel 或 TypeScript 使用 thread-loader。该选项在系统的 CPU 有多于一个内核时自动启用，仅作用于生产构建。
  pwa: {}, // PWA 插件相关配置 see https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
  // webpack-dev-server 相关配置
  devServer: {
    open: process.platform === 'darwin',
    host: '0.0.0.0', // 允许外部ip访问
    port: 8022, // 端口
    https: false, // 启用https
    overlay: {
      warnings: true,
      errors: true
    }, // 错误、警告在页面弹出
    proxy: {
      '/api': {
        target: 'http://www.baidu.com/api',
        changeOrigin: true, // 允许websockets跨域
        // ws: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    } // 代理转发配置，用于调试环境
  },
  // 第三方插件配置
  pluginOptions: {}
}
```

