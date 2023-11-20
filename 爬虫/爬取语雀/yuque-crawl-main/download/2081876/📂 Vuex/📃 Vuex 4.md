官网：[https://next.vuex.vuejs.org/](https://next.vuex.vuejs.org/)

<a name="3zSmR"></a>
## Composition API
在Composition API中，Vuex状态管理暴露了一个 `useStore` 方法，可以直接获取到 `this.$store` 的引用：
```vue
<template>
 <div>{{state.name}}</div>
 <button @click="setData">设置数据</button>
</template>

<script>
import { useStore } from 'vuex'

export default {
  setup() {
    const { state, commit, dispatch } = useStore()

    function setData() {
      commit('SET_DATA', "Hello world")
    }

    return {
      state,
      setData
    }
  },
}
</script>
```

以后就再也不用 `this.$store.commit` 、 `this.$store.dispatch` 地用了，很爽是不是。
