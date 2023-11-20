uni-app 内置了 vuex ，在 main.js 中的引用即可。

<a name="QNjSW"></a>
## 创建状态管理文件
项目根下新建一个 store 文件夹，创建一个 index.js

`store/index.js`
```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
      appName: 'test app',
      version: '0.0.1',
      globalCount: 0
    },
    mutations: {
      increment (state) {
        state.globalCount ++
      },
      setCount (state, num) {
        state.globalCount = num
      },
      ['SET_APPNAME'] (state, arg) {
        state.appName = arg
      }
    },
    actions: {
      setCount ({commit}, args) {
        commit('setCount', args.count)
      }
    },
    getters: {
      version: state => {
        return state.version
      }
    }
})
```

以上代码创建了一个简单的状态管理文件，使用不同写法定义了 state、mutations、actions、getters

<a name="70W5U"></a>
## 在 main.js 中引入
然后在 main.js 中引入，跟平常写 Vue 程序一样：

`main.js`
```javascript
import Vue from 'vue'
import App from './App'

import store from './store'
Vue.prototype.$store = store

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
    ...App,
    store
}).$mount()
```

<a name="ezaZH"></a>
## 在组件中使用
在组件中使用就很容易了，跟平常一样用即可：
```javascript
import {mapState, mapMutations, mapActions, mapGetters} from 'vuex'
export default {
  computed: {
    ...mapState({
      appName: state => state.appName,
      globalCount: state => state.globalCount
    }),
    ...mapGetters({
      version: 'version'
    })
  },
  created () {
    // State
    console.log(this.appName); // test app

    // Mutation
    this.setAppName('Hello uni-app')
    console.log(this.appName); // Hello uni-app

    this.increment()
    console.log(this.$store.state.globalCount); // 1

    // Action
    this.setCount({count: 10})
    console.log(this.globalCount); // 10

    // Getter
    console.log(`version: ${this.version}`); // version: 0.0.1
  },
  methods: {
    ...mapMutations({
      setAppName: 'SET_APPNAME',
      increment: 'increment'
    }),
    ...mapActions({
      setCount: 'setCount'
    })
  }
}
```

当然，也可使用 commit 和 dispatch 方法进行提交：
```javascript
// Mutation
this.$store.commit('SET_APPNAME', 'Hello uni-app')
console.log(this.appName); // Hello uni-app

this.$store.commit('increment')
console.log(this.$store.state.globalCount); // 1

// Action
this.$store.dispatch('setCount', {count: 10})
console.log(this.globalCount); // 10
```

<a name="bWoGC"></a>
## 参考资料

- [uni-app 全局变量的几种实现方式](https://ask.dcloud.net.cn/article/35021)
