<a name="lAngM"></a>
## 一、全局API
在Vue2中，要在全局挂载组件、插件、指令等，都是通过往Vue原型中添加属性完成的：
```javascript
import Vue from 'vue'
import App from './App.vue'

Vue.config.ignoredElements = [/^app-/]
Vue.use(/* ... */)
Vue.mixin(/* ... */)
Vue.component(/* ... */)
Vue.directive(/* ... */)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

在Vue3中，通过创建新的 Vue 实例，对 Vue 对象所做的任何更改都会影响每个 Vue 实例和组件。
```javascript
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

app.config.ignoredElements = [/^app-/]
app.use(/* ... */)
app.mixin(/* ... */)
app.component(/* ... */)
app.directive(/* ... */)

app.mount('#app')
```
下面一张表列举了API的变化：

| **2.x Global API** | **3.x Instance API ** |
| --- | --- |
| Vue.config | app.config |
| Vue.config.productionTip | ~~_removed_~~ |
| Vue.config.ignoredElements | app.config.isCustomElement |
| Vue.component | app.component |
| Vue.directive | app.directive |
| Vue.mixin | app.mixin |
| Vue.use | app.use |
| Vue.prototype | app.config.globalProperties |


参考：[https://v3.vuejs.org/guide/migration/global-api.html](https://v3.vuejs.org/guide/migration/global-api.html)

<a name="XvPrl"></a>
## 二、模板可存在多个根节点
这一点很棒，在Vue2的组件模板中，只能存在一个ROOT节点，这可能会导致创建的DOM臃肿，产生很多不必要的标签。

在Vue3中解决了这个问题：
```vue
<template>
<HelloWorld :msg="msg"></HelloWorld>
<button @click="setData">设置数据</button>
</template>
```

<a name="JYzNa"></a>
## 三、修饰符
<a name="nET3C"></a>
### `v-model` 组件修饰符
在Vue3的 `v-model` 在组件中支持命名，相应的修饰符也做了增强，可以在多 `v-model` 的组件上直接使用修饰符。

内置的 `v-model` 修饰符包括：

- `.lazy` 
- `.number`
- `.trim` 

在Vue3中可以这样在组件中使用修饰符：
```vue
<CustomInput v-model:title.lazy="title"  v-model:description.trim="description"></CustomInput>

<CustomInput v-model:title.lazy.trim="title"></CustomInput>
```

但是特别注意，需要在 `CustomInput` 中暴露出对应的props修改器，其命名格式为 `arg + "Modifiers"` ：
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
  props: ["title", "description", "titleModifiers", "descriptionModifiers"],
  emits: ['update:title', 'update:description'],
  created() {
    console.log(this.titleModifiers) // {lazy: true}
    console.log(this.descriptionModifiers) // {trim: true}
  }
}
</script>
```

参考：[https://v3.vuejs.org/guide/component-custom-events.html#handling-v-model-modifiers](https://v3.vuejs.org/guide/component-custom-events.html#handling-v-model-modifiers)

<a name="KdFYB"></a>
### `v-model` 自定义组件修饰符
在前面可以看到， `xxxModifiers` 接收所有的修饰符参数，因此，我们完全可以自定义一些修饰符，达到自己想要的修改效果。

比如我们想要将输入的文字改为首字母大写，就可以通过以下方式达到目的：
```vue
<template>
  <div>title: </div>
  <input
    type="text"
    :value="title"
    @input="(e) => { emitValue(e, 'title') }">
  <span>{{title}}</span>
  <div></div>
  <div>description: </div>
  <input
    type="text"
    :value="description"
    @input="(e) => { emitValue(e, 'description') }">
  <span>{{description}}</span>
</template>

<script>
export default {
  props: ["title", "description", "titleModifiers", "descriptionModifiers"],
  emits: ['update:title', 'update:description'],
  created() {
    console.log(this.titleModifiers) // {capitalize: true}
    console.log(this.descriptionModifiers) // {capitalize: true}
  },
  methods: {
    emitValue(e, propsName) {
      let value = e.target.value
      if (this[`${propsName}Modifiers`].capitalize) {
        value = value.charAt(0).toUpperCase() + value.slice(1)
      }
      this.$emit(`update:${propsName}`, value)
    }
  },
}
</script>
```

使用的时候，只需要添加 `capitalize` 修饰符即可：
```vue
<CustomInput v-model:title.capitalize="title"  v-model:description.capitalize="description"></CustomInput>
```

参考：[https://v3.vuejs.org/guide/component-custom-events.html#handling-v-model-modifiers](https://v3.vuejs.org/guide/component-custom-events.html#handling-v-model-modifiers)

<a name="jqdvB"></a>
## 四、渲染函数
在Vue3中的渲染函数为 `h` ，而Vue2中为 `createElement` 。

示例：
```html
<template lang="pug">
HelloView
</template>

<script>
import { h } from 'vue'
export default {
  components: {
    HelloView: {
      render: () => {
        return h('h1', 'Hello world")
      }
    }
  }
}
</script>
```
参考：[https://v3.vuejs.org/guide/render-function.html#the-dom-tree](https://v3.vuejs.org/guide/render-function.html#the-dom-tree)

<a name="IjTpm"></a>
## 五、多事件处理器
事件处理程序中可以有多个方法，这些方法由逗号运算符分隔：
```vue
<!-- 这两个 one() 和 two() 将执行按钮点击事件 -->
<button @click="one($event), two($event)">
  Submit
</button>
```
```javascript
// ...
methods: {
  one(event) {
    // 第一个事件处理器逻辑...
  },
  two(event) {
   // 第二个事件处理器逻辑...
  }
}
```
