<a name="48305"></a>
## 一、插槽
<a name="bkW2a"></a>
### 具名插槽
这是一项非常不错的特性， 支持传递多个 `slot` ，并可以对其命名。

具名插槽其实在Vue 2中已被引入，但用法跟这大相径庭。<br />官网文档中给了警告：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607331543104-6d02b60d-38de-45c4-9a89-8de6a53e0c7e.png#height=150&id=Sv3bS&originHeight=184&originWidth=767&originalType=binary&ratio=1&size=25804&status=done&style=none&width=624)

示例：<br />子组件 `Container.vue`
```vue
<template>
<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>
</template>
```
父组件：
```vue
<template>
<Container>
  <template v-slot:header>Header</template>
  <template v-slot:default>
    <p>Content</p>
  </template>
  <template v-slot:footer>Footer</template>
</Container>
</template>

<script>
import Container from '../components/Container.vue'

export default {
  components: {
    Container,
  }
}
</script>
```
当然，默认插槽（ `v-slot:default`）也可以不写名字，其渲染后的元素顺序不会改变：
```vue
<template>
<Container>
  <template v-slot:header>Header</template>
  <template v-slot:footer>Footer</template>
  <p>Content</p>
</Container>
</template>
```

渲染结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607330708698-fbc48b11-99a2-4888-8588-b89b2167a8c6.png#height=143&id=LUVEB&originHeight=143&originWidth=187&originalType=binary&ratio=1&size=3214&status=done&style=none&width=187)

<a name="xX4rW"></a>
### 作用域插槽
有的时候，我们需要将slot放置于循环之中，在父组件中觉得如何展示这些slot。

举例：一个名为`TodoList.vue`的组件，循环出slot：
```vue
<template>
<ul>
  <li v-for="( item, index ) in items">
    <slot :item="item" :index="index"></slot>
  </li>
</ul>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      required: true
    },
  }
}
</script>

```
父组件中引入：
```vue
<template>
<TodoList :items="list">
  <template v-slot:default="slotProps">
    <span>{{ slotProps?.item?.name }}</span>
  </template>
</TodoList>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
  components: {
    TodoList
  },
  data() {
    return {
      list: [
        {
          id: 1,
          name: 'vue',
          age: 18
        },
        {
          id: 2,
          name: 'react',
          age: 20
        },
        {
          id: 3,
          name: 'angular',
          age: 22
        }
      ]
    }
  },
}
</script>
```

<a name="Z1WJk"></a>
### 插槽缩写
`v-slot:` 可以缩写为 `#` ：
```vue
<template>
<Container>
  <template #header>Header</template>
  <template #footer>Footer</template>
  <p>Content</p>
</Container>
</template>
```
[

](https://v3.vuejs.org/guide/component-slots.html#named-slots)<br />如果是需要带出参数，可以直接使用`#slotName=`
```vue
<TodoList :items="list" #="{item}">
  <span>{{ item.name }}</span>
</TodoList>
```
这是下面写法的缩写，省略了`default`，同样的，其他具名插槽也可通过这种方式带出参数。
```vue
<TodoList :items="list" #default="{item}">
  <span>{{ item.name }}</span>
</TodoList>
```

<a name="d44IK"></a>
### 解构插槽
也可以通过解构的方式带出参数，`template`和`default`亦可省略：
```vue
<TodoList :items="list" v-slot="{index, item}">
  <span>{{index}}: {{ item?.name }}</span>
</TodoList>
```
注意默认插槽的缩写语法不能和具名插槽混用，因为它会导致作用域不明确。

通过解构插槽重命名：
```vue
<TodoList :items="list" v-slot="{item: language, index}">
  <span>{{index}}: {{ language?.name }}</span>
</TodoList>
```

通过解构插槽指定默认值，以避免出现undefined的情况：
```vue
<TodoList :items="list" v-slot="{item: language, flag = '*'}">
  <span>{{flag}} {{ language?.name }}</span>
</TodoList>
```


<a name="cu5bE"></a>
## 二、命名Model（多v-model绑定）
这也是一项非常不错的特性， 支持传递多个 `v-model` ，并可以对其命名。

示例：<br />子组件 `CustomInput.vue` 
```vue
<template>
  <div>title: </div>
  <input
    type="text"
    :value="title"
    @input="$emit('update:title', $event.target.value)">
  <span>{{title}}</span>
  <div></div>
  <div>description: </div>
  <input
    type="text"
    :value="description"
    @input="$emit('update:description', $event.target.value)">
  <span>{{description}}</span>
</template>

<script>
export default {
  props: {
    title: String,
    description: String
  },
  emits: ['update:title', 'update:description'],
}
</script>
```
父组件：
```vue
<template>
<CustomInput v-model:title="title"  v-model:description="description"></CustomInput>
</template>

<script>
import CustomInput from '../components/CustomInput.vue'

export default {
  components: { CustomInput },
  data() {
    return {
      title: '',
      description: '',
    }
  }
}
</script>
```

效果：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607329606722-fef8e396-763a-40d9-99a0-9b00c5a6c1d9.gif#height=121&id=igq4u&originHeight=121&originWidth=335&originalType=binary&ratio=1&size=49240&status=done&style=none&width=335)

参考：[https://v3.vuejs.org/guide/component-custom-events.html#multiple-v-model-bindings](https://v3.vuejs.org/guide/component-custom-events.html#multiple-v-model-bindings)

<a name="Dn9c0"></a>
## 三、多根节点的非Prop属性继承
如果组件中根节点只有一个，那么父组件中的属性值将直接应用于子组件。以class属性为例：<br />子组件：
```vue
<template>
<div>Hello world</div>
</template>
```
父组件：
```vue
<template>
<HelloWorld class="hello"></HelloWorld>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue'

export default {
  components: {
    HelloWorld
  },
}
</script>

<style lang="stylus">
.hello {
  color: #f00;
}
</style>
```

但是如果子组件中包含多个根节点：
```vue
<template>
<div>Hello</div>
<div>world</div>
</template>
```
这样的话编译器就不知道传递过来的样式该应用到谁身上，并且控制台会报一个警告：
```vue
Extraneous non-props attributes (class) were passed to component but could not be automatically inherited because component renders fragment or text root nodes.
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607330064177-3c7337a5-8f0c-4b8d-8354-51f5b02ae413.png#height=75&id=euxIE&originHeight=75&originWidth=1194&originalType=binary&ratio=1&size=11598&status=done&style=none&width=1194)

解决方案：在子组件中添加 `v-bind="$attrs"` 标识，以便区分将属性应用到哪个根节点上。
```vue
<template>
<div v-bind="$attrs">Hello</div>
<div>world</div>
</template>
```

参考：

- [https://v3.vuejs.org/guide/component-attrs.html#attribute-inheritance-on-multiple-root-nodes](https://v3.vuejs.org/guide/component-attrs.html#attribute-inheritance-on-multiple-root-nodes)
- [https://v3.vuejs.org/guide/migration/fragments.html#overview](https://v3.vuejs.org/guide/migration/fragments.html#overview)

<a name="fFwQd"></a>
## 四、循环中的ref
这一点其实是一个比较让人头疼的点，刚开始我写的时候都习惯性地像Vue2那种写法：
```vue
<template>
<ul>
  <li v-for="(item, key) in 10" :key="key" ref="li">{{item}}</li>
</ul>
</template>

<script>
export default {
  mounted() {
    console.log(this.$refs.li)
  },
}
</script>
```
但是这里打印出来的并不是一个数组，而是得到了循环中最后一个元素。<br />![Snipaste_2021-10-29_11-44-32.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1635479127562-702c7ab5-c94a-430a-932d-93a18ac0de3f.webp#clientId=u49480015-449d-4&from=drop&id=udf0a1508&originHeight=71&originWidth=205&originalType=binary&ratio=1&size=1156&status=done&style=none&taskId=ube7c4899-3346-48a3-aab4-21972c051d8)<br />如果使用了 `@vue/compat`，并将MODE设置为2，则仍然可以获得一个数组，但会报以下警告：
```vue
[Vue warn]: (deprecation V_FOR_REF) Ref usage on v-for no longer creates array ref values in Vue 3. Consider using function refs or refactor to avoid ref usage altogether.
```

后面转念一想，Vue3中的_reactive refs_ 和 _template refs_ 的概念已经统一了，这样搞肯定不成。一看文档，的确变了。

下面是在循环中使用ref的示例：
```vue
<template lang="pug">
ul
  li(v-for="(item, key) in 10" :ref="setItemRef") {{item}}
</template>

<script>
export default {
  data() {
    return {
      itemRefs: []
    }
  },
  mounted() {
    console.log(this.itemRefs)
  },
  methods: {
    setItemRef(el) {
      this.itemRefs.push(el)
    },
  }
}
</script>
```
这样就能获取到一个数组形式的ref了：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607498503686-58f506ec-1ea4-49ea-b9f3-88ee88bfac98.png#height=260&id=aa8IV&originHeight=260&originWidth=583&originalType=binary&ratio=1&size=12566&status=done&style=none&width=583)

使用Composition API的形式：
```vue
<template lang="pug">
ul
  li(v-for="(item, key) in 10" :ref="setItemRef") {{item}}
</template>

<script setup>
import { onMounted } from 'vue'

let itemRefs = []
const setItemRef = el => {
  itemRefs.push(el)
}
onMounted(() => {
  console.log(itemRefs)
})
</script>
```

这样写起来非常不爽，但没办法，人家规范就是这样的。

参考：

- [📃 Composition API（组合式API）：模板Refs](https://www.yuque.com/xiaoyulive/vue/iikl69#tQczQ)
- [v-for 中的 Ref 数组](https://v3.cn.vuejs.org/guide/migration/array-refs.html)

<a name="2V17D"></a>
## 五、异步组件
在Vue3中的异步组件需要使用 `defineAsyncComponent` 来定义：
```javascript
import { defineAsyncComponent } from 'vue'
import ErrorComponent from './components/ErrorComponent.vue'
import LoadingComponent from './components/LoadingComponent.vue'

// Async component without options
const asyncPage = defineAsyncComponent(() => import('./NextPage.vue'))

// Async component with options
const asyncPageWithOptions = defineAsyncComponent({
  loader: () => import('./NextPage.vue'),
  delay: 200,
  timeout: 3000,
  errorComponent: ErrorComponent,
  loadingComponent: LoadingComponent
})
```

跟Vue2的异步组件相比，最显著的变化为：Vue3将选项中的 `component` 换为了 `loader` ，在 `error` 和 `loading` 后面都加上了 `Component` 。

下面是一个在vue-router 4 中使用的示例：
```javascript
import {createRouter, createWebHashHistory} from 'vue-router'
import { defineAsyncComponent } from 'vue'
import AsyncComponentLoading from "../components/AsyncComponentLoading.vue";
import AsyncComponentError from "../components/AsyncComponentError.vue";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/async', name: 'async',
      component: defineAsyncComponent({
        loader: () => import('../components-test/AsyncComponent.vue'),
        delay: 200,
        timeout: 3000,
        errorComponent: AsyncComponentError,
        loadingComponent: AsyncComponentLoading
      })
    },
  ]
})

export default router
```

当然，如果只考虑加载成功的情况，想要缩写也是完全没问题的：
```javascript
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/async', name: 'async', component: component: () => import('../components-test/AsyncComponent.vue')},
  ]
})
```

如果结合webpack（不要考虑在vite项目中使用这种写法），也可以使用`require`：
```javascript
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/async', name: 'async', component: defineAsyncComponent(
      () =>
        new Promise((resolve, reject) => {
          require(['./components/AsyncComponent.vue'], resolve)
        })
      )
    },
  ]
})
```

参考：

- [https://v3.vuejs.org/guide/migration/async-components.html](https://v3.vuejs.org/guide/migration/async-components.html#overview)

