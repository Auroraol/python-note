Vue3的另一个好基友，Vuex 4，集成起来也相当简单。

官网：[https://next.vuex.vuejs.org/](https://next.vuex.vuejs.org/)

<a name="Kvk5z"></a>
## 一、安装
同样地，也需要加上 `@next` 标识：
```bash
yarn add vuex@next
```
安装完成后，可以在依赖中看到：<br />
```json
{
  ...
  "dependencies": {
    "vue": "^3.0.2",
    "vue-router": "^4.0.0-rc.6",
    "vuex": "^4.0.0-rc.2"
  },
  ...
}
```

<a name="O4e2h"></a>
## 二、集成
首先确保创建以下目录结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1606880182462-967cf3ab-186f-4721-88e2-1ad8e593ec9b.png#align=left&display=inline&height=360&originHeight=360&originWidth=211&size=17593&status=done&style=none&width=211)

创建个简单的状态管理 `stores/index.js` ：
```javascript
import { createStore } from "vuex"

const store = createStore({
  state: {
    name: ''
  },
  mutations: {
    ['SET_DATA'](state, val) {
      state.name = val
    }
  },
  actions: {},
  modules: {},
})

export default store
```
这里只创建了一个 `mutation` 和 `state` ，用于测试Vuex是否正常运作。


在 `main.js` 中引入：
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './routes'
import store from './stores'

const app = createApp(App)

app.use(router)
app.use(store)
app.mount('#app')
```

在 `Home.vue` 中编写：
```vue
<template>
  <div>
    <button @click="setData">设置数据</button>
  </div>
</template>

<script>
export default {
  methods: {
    setData() {
      this.$store.commit('SET_DATA', 'Hello world')
      console.log(this.$store)
    }
  }
}
</script>

<style>
</style>
```

在 `Page.vue` 中编写：
```vue
<template>
  <div>{{name}}</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState({
      name: state => state.name
    })
  }
}
</script>

<style>
</style>
```

<a name="ILVeS"></a>
## 三、测试
执行命令 `vite` ，浏览器访问 [http://localhost:3000/](http://localhost:3000/)，效果如下：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1606881857806-2df7bd85-1ac1-4c69-871f-eac7dd991612.gif#align=left&display=inline&height=133&originHeight=133&originWidth=248&size=5211&status=done&style=none&width=248)<br />在控制台中可以看到，Vuex4已经使用了Proxy进行代理。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1606881961630-46552cdb-46e2-433c-9c15-7495a6014345.png#align=left&display=inline&height=425&originHeight=425&originWidth=797&size=36931&status=done&style=none&width=797)

