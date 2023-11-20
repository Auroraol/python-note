![vue-cli.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589084610-5d874731-eaf7-423a-a65d-dd5aefd8bb37.png#align=left&display=inline&height=581&originHeight=1500&originWidth=1000&size=848398&status=done&style=none&width=387)

vue-cli 官网: [https://cli.vuejs.org/zh/](https://cli.vuejs.org/zh/)

<a name="ishRq"></a>
## 安装vue-cli 2.0
```bash
$ yarn global add vue-cli
$ vue init <template-name> <project-name>
```

<a name="WBnjY"></a>
## 官方 Templates
官方还提供其他一些常用的模板，webpack 只是其中一种：

- **webpack** - A full-featured Webpack + vue-loader setup with hot reload, linting, testing & css extraction.
- **webpack-simple** - A simple Webpack + vue-loader setup for quick prototyping.
- **browserify** - A full-featured Browserify + vueify setup with hot-reload, linting & unit testing.
- **browserify-simple** - A simple Browserify + vueify setup for quick prototyping.
- **pwa** - PWA template for vue-cli based on the webpack template
- **simple** - The simplest possible Vue setup in a single HTML file

<a name="bBB6L"></a>
## 非官方 Template
```bash
vue init username/repo#<branch-name> my-project
```

其中 username/repo 分别代表 GitHub 用户名和其放置脚手架的仓库，branch-name 代表分支名称，可以省略默认为master。

<a name="EruGC"></a>
## 本地 Template
```bash
vue init ~/fs/path/to-custom-template my-project
```

用户自己存放于本地的脚手架仍然可以通过本地路径的方式获取并创建项目。

目录结构如图：<br />![022.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589055044-eb331447-88a4-4c06-adda-6b1b57ed9e31.png#align=left&display=inline&height=464&originHeight=464&originWidth=323&size=8091&status=done&style=none&width=323)<br />开发只需要关注 `src` 目录即可，如果需要一些定制化的配置，可以修改 `build` 目录下的 `webpack` 配置。

其中比较重要的文件为 `src/main.js` ，是整个项目的入口文件，渲染模板为 `index.html`，其中 `scr/App.vue` 是可更改甚至删除的，只是脚手架提供的默认渲染组件。

<a name="PS36p"></a>
## 运行项目
```bash
$ yarn dev
```
默认监听端口 8080，只需在浏览器输入 `http://localhost:8080` 即可访问。

