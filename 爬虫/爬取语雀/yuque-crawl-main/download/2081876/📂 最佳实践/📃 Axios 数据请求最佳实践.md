<a name="25bf391e"></a>
## 请求拆分
通常, 我们会将所有请求拆分出来, 便于维护与修改, 也更易于管理。比如我们可以在项目根下建立一个 `services` 文件夹, 用于调取服务。

<a name="85837643"></a>
## 结合 async 获取数据
`services/getData.js`
```javascript
import axios from '../library/modules/axios'
import store from '../stores'

export default {
  async homeMenus () {
    let res = await axios.get({ url: 'home/homeMenus' })
    return res.data.status === 1 ? res.data.data : []
  },
  async swipers () {
    let res = await axios.get({ url: 'home/swipers' })
    return res.data.status === 1 ? res.data.data : []
  }
}
```

在 `main.js` 中引入：
```javascript
import getData from './services/getData'
Vue.prototype.$getData = getData
```

在需要的组件中使用：
```javascript
export default {
  data () {
    return {
      menus: [],
      swipers: []
    }
  },
  async created () {
    this.menus = await this.$getData.homeMenus()
    this.swipers = await this.$getData.swipers()
  }
}
```

<a name="81a5c092"></a>
## 结合 vuex 使用
可以更进一层封装, 在 vuex 中缓存数据, 如果第二次访问数据则不进行数据更新。

`store/index.js`
```javascript
let modules = {
  home: require('./modules/home.js').default
}

export default new Vuex.Store({
  modules,
  actions: {
    setData ({ state }, args) {
      state[args.module][args.type] = args.data
    }
  }
})
```

`store/modules/home.js`
```javascript
const state = {
  homeMenus: [],
  homeSwipers: []
}

const mutations = {}
const actions = {}
const getters = {}

export default {
  state, mutations, actions, getters
}
```

`services/getData.js`
```javascript
import axios from '../library/modules/axios'
import store from '../stores'

export default async function (args) {
  let url = ''
  let data = []
  let module = args.split('.')[0]
  let type = args.split('.')[0] + args.split('.')[1]
  switch (type) {
    case 'homeMenus':
      url = 'home/homeMenus'
      break
    case 'homeSwipers':
      url = 'home/swipers'
      break
  }
  if (store.state[module][type].length > 0) {
    data = store.state[module][type]
  } else {
    try {
      let res = await axios.get({ url })
      data = res.data.status === 1 ? res.data.data : parts[2] === 'list' ? [] : {}
      store.dispatch('setData', { data, module, type })
    } catch (e) {
      alert(e)
    }
  }
  return data
}
```

在需要的组件中使用：
```javascript
export default {
  data () {
    return {
      menus: [],
      swipers: []
    }
  },
  async created () {
    this.menus = await this.$getData('home.Menus')
    this.swipers = await this.$getData('home.Swipers')
  }
}
```

通过上述代码, 就可以判断状态管理中是否存在调用过的数据, 如果存在就不进行重复请求。

<a name="65682ee5"></a>
## 缓存处理
当然, 上面的方式是有问题的, 对于首页菜单或者是轮播图这种数据, 请求后进行存储问题不大, 但是如果是一些实时性比较强的数据, 就不能直接这样存储了, 需要找一种更加委婉的方式进行处理。

