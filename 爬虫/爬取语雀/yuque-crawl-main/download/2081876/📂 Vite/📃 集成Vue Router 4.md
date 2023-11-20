官网：[https://next.router.vuejs.org/](https://next.router.vuejs.org/)

Vue3的一对好基友，Vue Router 4，集成起来也相当容易。
<a name="4VawO"></a>
## 一、安装
由于还没发布正式版，需要使用 `@next` 标识：
```bash
yarn add vue-router@next
```
安装完成后，可以在依赖中看到：
```bash
{
	...
  "dependencies": {
    "vue": "^3.0.2",
    "vue-router": "^4.0.0-rc.6"
  },
  ...
}
```

<a name="eUzh5"></a>
## 二、集成
首先确保创建以下目录结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1606878840573-05709fd9-f26e-463b-93b8-b450a5d7706f.png#align=left&display=inline&height=350&originHeight=350&originWidth=260&size=17457&status=done&style=none&width=260)

编写 `routes/index.js` ：
```javascript
import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "../pages/Home.vue";
import Page from "../pages/Page.vue";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/home', name: 'home', component: Home },
    { path: '/page', name: 'page', component: Page },
  ]
})

export default router
```

在 `main.js` 中引入：
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './routes'

createApp(App)
  .use(router)
  .mount('#app')
```

Vue3 支持链式写法，也可以拆分成：
```javascript
const app = createApp(App)

app.use(router)
app.mount('#app')
```
但是注意 `mount` 一定得最后写。

在 `App.vue` 中写入：
```vue
<template>
  <div id='nav'>
    <router-link to='/home'>Home</router-link>
    <router-link to='/page'>Page</router-link>
  </div>
  <router-view />
</template>

<script>
export default {
  name: 'App'
}
</script>

```
Vue3 已经支持template多root写法，所以这样写没什么问题。

至于 `Home.vue` 和 `Page.vue` 就随便写点吧：
```vue
<template>
  <div>Home</div>
</template>

<script>
export default {}
</script>

<style></style>
```
```vue
<template>
  <div>Page</div>
</template>

<script>
export default {}
</script>

<style></style>
```

<a name="qeEuV"></a>
## 三、测试
执行命令 `vite` ，浏览器访问 [http://localhost:3000/](http://localhost:3000/)，效果如下：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1606879147387-a9006f1d-f9f7-48fe-9f2e-02c7813339f5.gif#align=left&display=inline&height=73&originHeight=73&originWidth=248&size=3116&status=done&style=none&width=248)


