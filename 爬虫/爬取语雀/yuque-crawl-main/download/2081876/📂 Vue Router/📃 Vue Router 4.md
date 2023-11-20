官网：[https://next.router.vuejs.org/](https://next.router.vuejs.org/)

在Vue3项目中集成Vue Router 4，参看：<br />[📃 集成Vue Router 4](https://www.yuque.com/xiaoyulive/vue/sh6pdf?view=doc_embed)

<a name="CQL0j"></a>
## 一些重要的改动
<a name="w8l2J"></a>
### 创建路由
通过 `createRouter` 创建路由：
```javascript
import {createRouter, createWebHistory} from 'vue-router'
import HomeTest from "../pages-test/Home.vue";
import PageTest from "../pages-test/Page.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/home', name: 'home', component: HomeTest },
    { path: '/page', name: 'page', component: PageTest },
  ]
})

export default router
```

<a name="7iA88"></a>
### 路由模式
在Vue Router 3 中，路由模式直接使用字符串 `hash` 或 `history` 标识，而在4中，使用以下两种方式创建：
```javascript
createWebHashHistory()
createWebHistory()
```
示例：
```javascript
import {createRouter, createWebHashHistory} from 'vue-router'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    ...
  ]
})
```

<a name="vue-router-and-the-composition-api"></a>
# Composition API
使用 `useRouter()` 和 `useRoute()` 分别获取Options API中的 `this.$router` 和 `this.$route` 

举例：
```java
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
import ls from 'local-storage'

console.log(route.query)
    
let token = ls("token")

if (token.access_token) {
  router.push("/home")
} else {
  router.push("/login")
}
```

参考：[https://next.router.vuejs.org/guide/advanced/composition-api.html](https://next.router.vuejs.org/guide/advanced/composition-api.html)



