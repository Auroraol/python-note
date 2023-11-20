<a name="EVgks"></a>
## 一、什么是Vite

按照作者尤雨溪的描述：

> Vite，一个基于浏览器原生 ES imports 的开发服务器。利用浏览器去解析 imports，在服务器端按需编译返回，完全跳过了打包这个概念，服务器随起随用。同时不仅有 Vue 文件支持，还搞定了热更新，而且热更新的速度不会随着模块增多而变慢。针对生产环境则可以把同一份代码用 rollup 打。虽然现在还比较粗糙，但这个方向我觉得是有潜力的，做得好可以彻底解决改一行代码等半天热更新的问题。



它具有以下特点：

1. 快速的冷启动<br />
2. 即时的模块热更新<br />
3. 真正的按需编译<br />

<br />

- [GitHub：Vite ](https://github.com/vitejs/vite)
- [GitHub：Vite App](https://github.com/vitejs/create-vite-app)

<a name="QNiKZ"></a>
## 二、创建一个Vite+Vue3项目
<a name="OGCep"></a>
### 创建Vite1.x项目
使用yarn：
```bash
$ yarn create vite-app <project-name>
$ cd <project-name>
$ yarn
$ yarn dev
```
或者使用npm：
```bash
$ npm init vite-app <project-name>
$ cd <project-name>
$ npm install
$ npm run dev
```

<a name="UusFt"></a>
### 创建Vite2.x项目
使用最新版的vite脚手架创建项目的时候会报一个警告：
```bash
warning create-vite-app@1.21.0: create-vite-app has been deprecated. run `npm init @vitejs/app` or `yarn create @vitejs/app` instead.
```
提示很明显，使用如下命令即可创建Vite2项目：
```bash
$ npm init @vitejs/app <project-name>
$ yarn create @vitejs/app <project-name>
```

创建好之后，注意到 `package.json` 中的依赖 vue 已经到3.x 了
```json
{
  "name": "maker-pc-vue3",
  "version": "0.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "vue": "^3.0.2"
  },
  "devDependencies": {
    "vite": "^1.0.0-rc.8",
    "@vue/compiler-sfc": "^3.0.2"
  }
}
```

运行效果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602208842592-16e5be01-382b-47d7-a1db-74e025507665.png#align=left&display=inline&height=711&originHeight=711&originWidth=1273&size=49327&status=done&style=none&width=1273)<br />查看控制台，可以看到编译飞快，几乎是刚敲完键盘就实时刷新：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602208880825-f6d3f068-a3e9-4c70-8899-52cc32c0bc2a.png#align=left&display=inline&height=349&originHeight=349&originWidth=493&size=28625&status=done&style=none&width=493)<br />打包使用：
```bash
yarn build
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602208927538-771d728c-490b-4e26-b8a2-3131556acc95.png#align=left&display=inline&height=218&originHeight=218&originWidth=476&size=17264&status=done&style=none&width=476)

<a name="T09A2"></a>
## 三、Vue3新特性

- [Vue3 中文文档 - GitHub](https://github.com/vuejs/docs-next-zh-cn)
- [Vue3 中文文档](https://v3.cn.vuejs.org/)
- [Vue3 英文文档 - GitHub](https://github.com/vuejs/docs-next)
- [Vue3 英文文档](https://v3.vuejs.org/)

