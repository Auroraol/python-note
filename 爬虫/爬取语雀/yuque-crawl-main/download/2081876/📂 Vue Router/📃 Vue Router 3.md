- [vue-router 官网](https://router.vuejs.org/)
- [vue-router 中文文档](https://router.vuejs.org/zh/)

vue-router 主要用于创建单页应用，再结合 vue.js 的时候显得得心应手。

<a name="e655a410"></a>
## 一、安装与使用
安装：
```bash
$ yarn add vue-router
```

基本组件:

- **router-view** 路由入口
- **router-link** 路由链接

使用方式：

1. 导入 Vue 和 VueRouter，调用 Vue.use(VueRouter)
2. 引入路由组件
3. 定义路由
4. 创建 router 实例，然后传 `routes` 配置
5. 创建和挂载根实例

在vue-cli创建的项目中， `main.js` 配置如下：
```javascript
import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'

const routes = [
  { path: '/home', name: 'home', component: { template: '<div>Home</div>' } },
  { path: '/page', name: 'page', component: { template: '<div>Page</div>' } }
]

const router = new Router({
  hashbang: true,
  mode: 'history',
  routes
})

Vue.use(Router)

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
```

在 `App.vue` 中：
```vue
<template lang="pug">
div
  p
    router-link(to="/home") Home
    span(style="margin: 0 10px") |
    router-link(to="/page") Page
  router-view
</template>
```
效果：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607933542163-77c74955-70d0-4385-9332-26c01310ccf6.gif#align=left&display=inline&height=77&originHeight=77&originWidth=229&size=2988&status=done&style=none&width=229)

以上示例只为演示最简的基础用法，通常我们会将 `router` 拆分为单独的 `js` 模块，然后引入到 `main.js` 。

<a name="UWvd7"></a>
## 二、$route与$router

使用模块注册 vue-router，将会在 `Vue.prototype` 中注入一个 `$route` 和 `$router` 的只读属性。

其中，`$route` 用于监测当前路由，`$router` 用于进行路由操作，事实上，`$route` 与 `$router.currentRoute` 相同。

**$route**<br />**![025.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607933616987-5fa42f67-be8a-4149-8f02-76ce522e75b3.png#align=left&display=inline&height=162&originHeight=162&originWidth=240&size=2790&status=done&style=none&width=240)**

**$router**<br />**![026.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607933624065-ef297bfc-e8c4-4a25-8d44-13fdac55c358.png#align=left&display=inline&height=639&originHeight=639&originWidth=705&size=21557&status=done&style=none&width=705)**

- **$router**为VueRouter实例，比如想要导航到不同URL，则使用`$router.push`方法
- **$route**为当前router跳转对象，里面可以获取name、path、query、params等

<a name="vuex-router-sync"></a>
## 三、路由状态管理
[vuex-router-sync](https://www.npmjs.com/package/vuex-router-sync) 是一款将 vue-router 的 `$route` 属性同步到 vuex 中 state 的插件, 可以通过操作路由改变状态管理, 方便监视路由变化。

使用方式：<br />
```javascript
import { sync } from 'vuex-router-sync'
import store from './vuex/store' // vuex store instance
import router from './router' // vue-router instance

const unsync = sync(store, router)
```

使用：
```javascript
store.state.route.path   // current path (string)
store.state.route.params // current params (object)
store.state.route.query  // current query (object)
```

<a name="10jSs"></a>
## 四、**路由历史栈**
在使用路由的单页应用中，每访问一个页面，便将其加入**路由历史栈**当中，vue-router 提供各种控制路由的方法，操作方法同 `window.history`。

<a name="V5Jyt"></a>
### 编程式路由

- `router.push(location, onComplete?, onAbort?)` 跳转
- `router.back()` 后退
- `router.forward()` 前进
- `router.go(n)` 直接抵达指定的路由历史栈中的某个页面，指定n值，当前页面为 0，正数为此页之后的页面，负数为此页之前的页面
- `router.replace(location, onComplete?, onAbort?)` 替换

直接书写路径：
```javascript
router.push('/home')
router.push('/home?from=index')
```

通过对象的方式：
```javascript
router.push({ name: 'home' })
router.push({ path: 'foo/bar/index' })
```

动态路由参数的传递, 有以下两种写法：
```javascript
const userId = 123
router.push({ name: 'user', params: { userId }}) // -> /user/123
router.push({ path: `/user/${userId}` }) // -> /user/123
```

查询字符串的写法，有以下两种写法：
```javascript
router.push(`register?plan=${private}`)
router.push({ path: 'register', query: { plan: 'private' }})
```

<a name="CwBBg"></a>
### 声明式路由

- `<router-link :to='...'></router-link>`
- `<router-link :to="..." replace></router-link>`

直接书写路径：
```html
<router-link to='/'></router-link>
```

通过对象的方式：
```html
<router-link :to="{ name: 'home' }"></router-link>
<router-link :to="{ path: 'foo/bar/index' }"></router-link>
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>
<router-link :to="{ path: 'register', query: { plan: 'private' } }"></router-link>
```

<a name="as5lj"></a>
## 五、路由模式
`vue-router` 默认 **hash 模式**: 使用 URL 的 hash 来模拟一个完整的 URL，于是当 URL 改变时，页面不会重新加载。

如果不想要很丑的 hash，我们可以用路由的 **history 模式**，这种模式充分利用 `history.pushState` API 来完成 URL 跳转而无须重新加载页面。
```javascript
const router = new VueRouter({
  mode: 'history',
  routes: [...]
})
```

当你使用 history 模式时，URL 就像正常的 url，例如 `http://yoursite.com/user/id`。

不过这种模式要玩好，还需要后台配置支持。因为我们的应用是个单页客户端应用，如果后台没有正确的配置，当用户在浏览器直接访问 `http://oursite.com/user/id` 就会返回 404，这就不好看了。

所以呢，你要在服务端增加一个覆盖所有情况的候选资源：如果 URL 匹配不到任何静态资源，则应该返回同一个 `index.html` 页面，这个页面就是你 app 依赖的页面。

<a name="LMsyK"></a>
### 服务器配置以支持History模式
**nginx**
```bash
location / {
  try_files $uri $uri/ /index.html;
}
```

**Apache**
```xml
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
</IfModule>
```

**Node.js**
```javascript
const http = require('http')
const fs = require('fs')
const httpPort = 80

http.createServer((req, res) => {
  fs.readFile('index.htm', 'utf-8', (err, content) => {
    if (err) {
      console.log('We cannot open "index.htm" file.')
    }

    res.writeHead(200, {
      'Content-Type': 'text/html; charset=utf-8'
    })

    res.end(content)
  })
}).listen(httpPort, () => {
  console.log('Server listening on: http://localhost:%s', httpPort)
})
```

<a name="b3690595"></a>
## 六、路由传参
路由传参有两种方式：`query `和 `params`

通过 query 传参：
```javascript
// 注意: 使用 path 方式的路由才能使用 query
this.$router.push({
  path:'/xxx',
  query:{
    id: id
  }
})

// 接收参数:
this.$route.query.id
```

通过 params 传参：
```javascript
// 注意: 使用 name 方式的路由才能使用 params
this.$router.push({
  name:'xxx',
  params:{
    id: id
  }
})

// 接收参数:
this.$route.params.id
```

<a name="dad2860d"></a>
## 七、404 的处理
按照下面的方法，服务器将不再返回 404 错误页面，因为对于所有路径都会返回 `index.html` 文件。为了避免这种情况，应该在 Vue 应用里面覆盖所有的路由情况，然后在给出一个 404 页面。

```javascript
const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '*', component: NotFoundComponent }
  ]
})
```

或者，如果使用 Node.js 服务器，也可以用服务端路由匹配到来的 URL，并在没有匹配到路由的时候返回 404，以实现回退。

此配置一定要放于所有路由配置之后, 否则有些路由将无法匹配

<a name="3920986a"></a>
## 八、动态路由
我们经常需要把某种模式匹配到的所有路由，全都映射到同个组件。例如，我们有一个 `User` 组件，对于所有 ID 各不相同的用户，都要使用这个组件来渲染。那么，我们可以在 `vue-router` 的路由路径中使用『动态路径参数』（dynamic segment）来达到这个效果：
```javascript
const User = {
  template: '<div>User {{ $route.params.id }}</div>'
}

const router = new VueRouter({
  routes: [
    // 动态路径参数 以冒号开头
    {
      path: '/user/:id',
      component: {
        template: '<div>User {{ $route.params.id }}</div>'
      }
    }
  ]
})
```

现在呢，像 `/user/foo` 和 `/user/bar` 都将映射到相同的路由。

一个『路径参数』使用冒号 `:` 标记。当匹配到一个路由时，参数值会被设置到 `this.$route.params`，可以在每个组件内使用。

甚至可以在一个路由中设置多段『路径参数』，对应的值都会设置到 `$route.params` 中。例如：

| 模式 | 匹配路径 | $route.params |
| --- | --- | --- |
| /user/:username | /user/evan | `{ username: 'evan' }` |
| /user/:username/post/:post_id | /user/evan/post/123 | `{ username: 'evan', post_id: 123 }` |


除了 `$route.params` 外，`$route` 对象还提供了其它有用的信息，例如，`$route.query`（如果 URL 中有查询参数）、`$route.hash` 等等。

<a name="631b3d85"></a>
## 九、响应路由的变化
当使用路由参数时，例如从 `/user/foo` 导航到 `/user/bar`，**原来的组件实例会被复用**。因为两个路由都渲染同个组件，比起销毁再创建，复用则显得更加高效。**不过，这也意味着组件的生命周期钩子不会再被调用**。

复用组件时，如果想对路由参数的变化作出响应的话，可以简单地 watch（监测变化） `$route` 对象：

```javascript
const User = {
  template: '...',
  watch: {
    '$route' (to, from) {
      // 对路由变化作出响应...
    }
  }
}
```

或者使用 2.2 中引入的 `beforeRouteUpdate` 守卫：

```javascript
const User = {
  template: '...',
  beforeRouteUpdate (to, from, next) {
    // react to route changes...
    // don't forget to call next()
  }
}
```


<a name="bd526d70"></a>
## 十、嵌套路由

通常， `<router-view>` 是最顶层的出口，渲染最高级路由匹配到的组件。

同样地，一个被渲染组件同样可以包含自己的嵌套 `<router-view>`。

例如，在 `User` 组件的模板添加一个 `<router-view>` :

```html
<script src="//unpkg.com/vue/dist/vue.js"></script>
<script src="//unpkg.com/vue-router/dist/vue-router.js"></script>

<div id="app">
  <p>
    <router-link to="/">&le;root&gt;</router-link>
    <router-link to="/user">/user/foo</router-link>
    <router-link to="/user/profile">/user/foo/profile</router-link>
    <router-link to="/user/posts">/user/foo/posts</router-link>
  </p>
  <p>Hello Vue-Router</p>
  <router-view></router-view>
</div>
```

要在嵌套的出口中渲染组件，需要在 VueRouter 的参数中使用 children 配置：

```javascript
const User = {
  template: `
    <div class="user">
      <h2>User {{ $route.params.id }}</h2>
      <router-view></router-view>
    </div>
  `
}

const UserHome = { template: '<div>Home</div>' }
const UserProfile = { template: '<div>Profile</div>' }
const UserPosts = { template: '<div>Posts</div>' }

const router = new VueRouter({
  routes: [
    { path: '/user', component: User,
      children: [
        // 空子路由，用于默认渲染
        { path: '', component: UserHome },

        // 当 /user/profile 匹配成功
        // UserProfile 会被渲染在 User 的 <router-view> 中
        { path: 'profile', component: UserProfile },

         // 当 /user/posts 匹配成功
         // UserPosts 会被渲染在 User 的 <router-view> 中
        { path: 'posts', component: UserPosts }
      ]
    }
  ]
})

const app = new Vue({ router }).$mount('#app')
```

:::info
以 / 开头的嵌套路径会被当作根路径。 这能充分的使用嵌套组件而无须设置嵌套的路径。
:::

基于上面的配置，当访问 /user 时，User 的出口是不会渲染任何东西，这是因为没有匹配到合适的子路由。如果你想要渲染点什么，可以如上提供一个空的子路由。

<a name="bded8606"></a>
## 十一、命名视图
有时候想同时（同级）展示多个视图，而不是嵌套展示，例如创建一个布局，有 `sidebar`（侧导航） 和 `main`（主内容） 两个视图，这个时候命名视图就派上用场了。你可以在界面中拥有多个单独命名的视图，而不是只有一个单独的出口。如果 `router-view` 没有设置名字，那么默认为 `default`。
```html
<router-view class="view one"></router-view>
<router-view class="view two" name="a"></router-view>
<router-view class="view three" name="b"></router-view>
```

一个视图使用一个组件渲染，因此对于同个路由，多个视图就需要多个组件。确保正确使用 `components` 配置（带上 s）：
```javascript
const router = new VueRouter({
  routes: [
    {
      path: '/',
      components: {
        default: Foo,
        a: Bar,
        b: Baz
      }
    }
  ]
})
```

<a name="69c967fe"></a>
### 嵌套命名视图
我们也有可能使用命名视图创建嵌套视图的复杂布局，这时也可以用到嵌套 `router-view` 组件。

<a name="39db45cb"></a>
## 十二、路由重定向
重定向也是通过 `routes` 配置来完成，下面例子是从 `/a` 重定向到 `/b`：
```javascript
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: '/b' }
  ]
})
```

重定向的目标也可以是一个命名的路由：
```javascript
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: { name: 'foo' }}
  ]
})
```

甚至是一个方法，动态返回重定向目标：
```javascript
const router = new VueRouter({
  routes: [
    { path: '/a', redirect: to => {
      // 方法接收 目标路由 作为参数
      // return 重定向的 字符串路径/路径对象
    }}
  ]
})
```

<a name="d4e8f398"></a>
## 十三、路由别名
『重定向』的意思是，当用户访问 `/a`时，URL 将会被替换成 `/b`，然后匹配路由为 `/b`，而『别名』是什么？ 举个栗子： **/a 的别名是 /b，意味着，当用户访问 /b 时，URL 会保持为 /b，但是路由匹配则为 /a，就像用户访问 /a 一样。**

上面对应的路由配置为：
```javascript
const router = new VueRouter({
  routes: [
    { path: '/a', component: A, alias: '/b' }
  ]
})
```

『别名』的功能可以自由地将 UI 结构映射到任意的 URL，而不是受限于配置的嵌套路由结构。

<a name="89f7ebf2"></a>
## 十四、路由元信息
定义路由的时候可以配置 `meta` 字段：
```javascript
const router = new VueRouter({
  routes: [
    {
      path: '/foo',
      component: Foo,
      children: [
        {
          path: 'bar',
          component: Bar,
          // a meta field
          meta: { requiresAuth: true }
        }
      ]
    }
  ]
})
```

那么如何访问这个 `meta` 字段呢？

首先，我们称呼 `routes` 配置中的每个路由对象为 **路由记录**。路由记录可以是嵌套的，因此，当一个路由匹配成功后，他可能匹配多个路由记录

例如，根据上面的路由配置，`/foo/bar` 这个 URL 将会匹配父路由记录以及子路由记录。

一个路由匹配到的所有路由记录会暴露为 `$route` 对象（还有在导航守卫中的路由对象）的 `$route.matched` 数组。因此，我们需要遍历 `$route.matched` 来检查路由记录中的 `meta` 字段。

下面例子展示在全局导航守卫中检查元字段：
```javascript
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!auth.loggedIn()) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // 确保一定要调用 next()
  }
})
```

<a name="78b836e0"></a>
## 十五、路由动画
可以在路由入口外围套上一层 transition 以实现路由切换过程中的动画效果：
```html
<script src="//unpkg.com/vue/dist/vue.js"></script>
<script src="//unpkg.com/vue-router/dist/vue-router.js"></script>

<div id="app">
  <router-view></router-view>
</div>
```

```javascript
const Home = {
  template: `
    <div class="home">
      <h2>Home</h2>
      <p>hello</p>
    </div>
  `
}

const Parent = {
  data () {
    return {
      transitionName: 'slide-left'
    }
  },
  // dynamically set transition based on route change
  watch: {
    '$route' (to, from) {
      const toDepth = to.path.split('/').length
      const fromDepth = from.path.split('/').length
      this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
    }
  },
  template: `
    <div class="parent">
      <h2>Parent</h2>
      <transition :name="transitionName">
        <router-view class="child-view"></router-view>
      </transition>
    </div>
  `
}

const Default = { template: '<div class="default">default</div>' }
const Foo = { template: '<div class="foo">foo</div>' }
const Bar = { template: '<div class="bar">bar</div>' }

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: Home },
    { path: '/parent', component: Parent,
      children: [
        { path: '', component: Default },
        { path: 'foo', component: Foo },
        { path: 'bar', component: Bar }
      ]
    }
  ]
})

new Vue({
  router,
  template: `
    <div id="app">
      <h1>Transitions</h1>
      <ul>
        <li><router-link to="/">/</router-link></li>
        <li><router-link to="/parent">/parent</router-link></li>
        <li><router-link to="/parent/foo">/parent/foo</router-link></li>
        <li><router-link to="/parent/bar">/parent/bar</router-link></li>
      </ul>
      <transition name="fade" mode="out-in">
        <router-view class="view"></router-view>
      </transition>
    </div>
  `
}).$mount('#app')
```

```css
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s ease;
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
.child-view {
  position: absolute;
  transition: all .5s cubic-bezier(.55,0,.1,1);
}
.slide-left-enter, .slide-right-leave-active {
  opacity: 0;
  -webkit-transform: translate(30px, 0);
  transform: translate(30px, 0);
}
.slide-left-leave-active, .slide-right-enter {
  opacity: 0;
  -webkit-transform: translate(-30px, 0);
  transform: translate(-30px, 0);
}
```

<a name="0cfe063b"></a>
## 十六、数据获取
有时候，进入某个路由后，需要从服务器获取数据。例如，在渲染用户信息时，你需要从服务器获取用户的数据。我们可以通过两种方式来实现：

- **导航完成之后获取**：先完成导航，然后在接下来的组件生命周期钩子中获取数据。在数据获取期间显示『加载中』之类的指示。
- **导航完成之前获取**：导航完成前，在路由进入的守卫中获取数据，在数据获取成功后执行导航。

从技术角度讲，两种方式都不错 —— 就看你想要的用户体验是哪种。

<a name="7db78a95"></a>
### 导航完成后获取数据
当你使用这种方式时，我们会马上导航和渲染组件，然后在组件的 `created` 钩子中获取数据。这让我们有机会在数据获取期间展示一个 loading 状态，还可以在不同视图间展示不同的 loading 状态。

假设我们有一个 `Post` 组件，需要基于 `$route.params.id` 获取文章数据：
```html
<template>
  <div class="post">
    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="post" class="content">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>
```

```javascript
export default {
  data () {
    return {
      loading: false,
      post: null,
      error: null
    }
  },
  created () {
    // 组件创建完后获取数据，
    // 此时 data 已经被 observed 了
    this.fetchData()
  },
  watch: {
    // 如果路由有变化，会再次执行该方法
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.error = this.post = null
      this.loading = true
      // replace getPost with your data fetching util / API wrapper
      getPost(this.$route.params.id, (err, post) => {
        this.loading = false
        if (err) {
          this.error = err.toString()
        } else {
          this.post = post
        }
      })
    }
  }
}
```

<a name="a40b6e45"></a>
### 在导航完成前获取数据
通过这种方式，我们在导航转入新的路由前获取数据。我们可以在接下来的组件的 `beforeRouteEnter` 守卫中获取数据，当数据获取成功后只调用 `next` 方法。
```javascript
export default {
  data () {
    return {
      post: null,
      error: null
    }
  },
  beforeRouteEnter (to, from, next) {
    getPost(to.params.id, (err, post) => {
      next(vm => vm.setData(err, post))
    })
  },
  // 路由改变前，组件就已经渲染完了
  // 逻辑稍稍不同
  beforeRouteUpdate (to, from, next) {
    this.post = null
    getPost(to.params.id, (err, post) => {
      this.setData(err, post)
      next()
    })
  },
  methods: {
    setData (err, post) {
      if (err) {
        this.error = err.toString()
      } else {
        this.post = post
      }
    }
  }
}
```

在为后面的视图获取数据时，用户会停留在当前的界面，因此建议在数据获取期间，显示一些进度条或者别的指示。如果数据获取失败，同样有必要展示一些全局的错误提醒。

<a name="eae4f618"></a>
## 十七、滚动行为
使用前端路由，当切换到新路由时，想要页面滚到顶部，或者是保持原先的滚动位置，就像重新加载页面那样。 `vue-router` 能做到，而且更好，它让你可以自定义路由切换时页面如何滚动。

这个功能只在支持 history.pushState 的浏览器中可用

当创建一个 Router 实例，你可以提供一个 `scrollBehavior` 方法：
```javascript
const router = new VueRouter({
  routes: [...],
  scrollBehavior (to, from, savedPosition) {
    // return 期望滚动到哪个的位置
  }
})
```

`scrollBehavior` 方法接收 `to` 和 `from` 路由对象。第三个参数 `savedPosition` 当且仅当 `popstate` 导航 (通过浏览器的 前进/后退 按钮触发) 时才可用。

这个方法返回滚动位置的对象信息，长这样：

- `{ x: number, y: number }`
- `{ selector: string, offset? : { x: number, y: number }}` (offset 只在 2.6.0+ 支持)

如果返回一个 falsy (译者注：falsy 不是 `false`，[参考这里](https://developer.mozilla.org/zh-CN/docs/Glossary/Falsy))的值，或者是一个空对象，那么不会发生滚动。

举例：
```javascript
scrollBehavior (to, from, savedPosition) {
  return { x: 0, y: 0 }
}
```

对于所有路由导航，简单地让页面滚动到顶部。

返回 `savedPosition`，在按下 后退/前进 按钮时，就会像浏览器的原生表现那样：
```javascript
scrollBehavior (to, from, savedPosition) {
  if (savedPosition) {
    return savedPosition
  } else {
    return { x: 0, y: 0 }
  }
}
```

如果你要模拟『滚动到锚点』的行为：
```javascript
scrollBehavior (to, from, savedPosition) {
  if (to.hash) {
    return {
      selector: to.hash
    }
  }
}
```

我们还可以利用[路由元信息](https://router.vuejs.org/zh-cn/advanced/meta.html)更细颗粒度地控制滚动。查看完整例子请[移步这里](https://github.com/vuejs/vue-router/blob/next/examples/scroll-behavior/app.js)。

<a name="r5PIe"></a>
### 异步滚动
2.8.0+ , 也可以返回一个 Promise 来得出预期的位置描述：
```javascript
scrollBehavior (to, from, savedPosition) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ x: 0, y: 0 })
    }, 500)
  })
}
```

将其挂载到从页面级别的过渡组件的事件上，令其滚动行为和页面过渡一起良好运行是可能的。但是考虑到用例的多样性和复杂性，我们仅提供这个原始的接口，以支持不同用户场景的具体实现。

<a name="d14e3942"></a>
## 十八、路由懒加载
当打包构建应用时，Javascript 包会变得非常大，影响页面加载。如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就更加高效了。

结合 Vue 的[异步组件](https://cn.vuejs.org/guide/components.html#%E5%BC%82%E6%AD%A5%E7%BB%84%E4%BB%B6)和 Webpack 的[代码分割功能](https://doc.webpack-china.org/guides/code-splitting-async/#require-ensure-/)，轻松实现路由组件的懒加载。

首先，可以将异步组件定义为返回一个 Promise 的工厂函数 (该函数返回的 Promise 应该 resolve 组件本身)：
```javascript
const Foo = () => Promise.resolve({ /* 组件定义对象 */ })
```

第二，在 Webpack 2 中，我们可以使用[动态 import](https://github.com/tc39/proposal-dynamic-import)语法来定义代码分块点 (split point)：
```javascript
import('./Foo.vue') // 返回 Promise
```

如果您使用的是 Babel，你将需要添加 [`syntax-dynamic-import`](https://babeljs.io/docs/plugins/syntax-dynamic-import/) 插件，才能使 Babel 可以正确地解析语法。

结合这两者，这就是如何定义一个能够被 Webpack 自动代码分割的异步组件。
```javascript
const Foo = () => import('./Foo.vue')
```

在路由配置中什么都不需要改变，只需要像往常一样使用 `Foo`：
```javascript
const router = new VueRouter({
  routes: [
    { path: '/foo', component: Foo }
  ]
})
```

<a name="z4jlq"></a>
### 把组件按组分块
有时候我们想把某个路由下的所有组件都打包在同个异步块 (chunk) 中。只需要使用 [命名 chunk](https://webpack.js.org/guides/code-splitting-require/#chunkname)，一个特殊的注释语法来提供 chunk name (需要 Webpack > 2.4)。
```javascript
const Foo = () => import(/* webpackChunkName: "group-foo" */ './Foo.vue')
const Bar = () => import(/* webpackChunkName: "group-foo" */ './Bar.vue')
const Baz = () => import(/* webpackChunkName: "group-foo" */ './Baz.vue')
```

Webpack 会将任何一个异步模块与相同的块名称组合到相同的异步块中。

