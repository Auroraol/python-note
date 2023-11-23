官方文档：[单文件组件 <script setup>](https://v3.cn.vuejs.org/api/sfc-script-setup.html)

<a name="MMVQA"></a>

## script setup语法糖

> 要使用这个语法，需要将 setup attribute 添加到 `<script> `代码块上：

```html
<script setup>
console.log('hello script setup')
</script>
```

以暴露所有脚本中定义的**顶级变量和方法**：
```vue
<template>
<div>{{count}}</div>
<button @click="inc">增加</button>
<button @click="dec">减少</button>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)
const inc = () => { count.value++ }
const dec = () => { count.value-- }
</script>
```

同样地，如果想要使用组件，直接引入即可：
```html
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <MyComponent />
</template>
```

参考：

- [sfc-script-setup](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-script-setup.md)
- [New script setup and ref sugar](https://github.com/vuejs/rfcs/pull/222)
- [New `script setup` (without ref sugar)](https://github.com/vuejs/rfcs/pull/227)

## $ref语法糖
为了避免在使用ref的时候，需要通过`.value`调用，vue3提供了`$ref`语法糖。

要开启`$ref`语法糖，需要先在`vite.config.js`中配置：
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    vue({
      reactivityTransform: true,
      refSugar:true
    })
  ]
})
```
然后在vue中直接使用即可：
```html
<script setup>
import { watchEffect } from 'vue'

let count = $ref(1)

watchEffect(() => console.log(count))

function inc() {
  count++
}
</script>

<template>
<div>{{count}}</div>
<button @click="inc">increase</button>
</template>
```
参考：[Reactivity Transform](https://github.com/vuejs/rfcs/discussions/369)

---


在较早的版本中（**目前已弃用**），可以使用 `ref:`创建。<br />ref语法糖是一个引起热议的试验性特性，因为其违反了JavaScript语法规则，必须借助编译器实现解析。
```vue
<template>
<div>{{count}}</div>
<button @click="inc">增加</button>
<button @click="dec">减少</button>
</template>

<script setup>
ref: count = 0
const inc = () => { count++ }
const dec = () => { count-- }
</script>
```

参考：

- [New script setup and ref sugar](https://github.com/vuejs/rfcs/pull/222)
- [Ref sugar](https://github.com/vuejs/rfcs/pull/228)

<a name="qpxTU"></a>
## 顶层await
可以直接在script setup中使用await，相当于创建了一个 `async setup()`。<br />示例：
```html
<script setup>
let res = await fetch('http://localhost:3000/')
console.log(await res.text())
</script>

```

<a name="Z09Uh"></a>
## 组件传值
<a name="EPBiI"></a>
### `defineProps`和`defineEmits`
要接收值，需要使用`defineProps`；需要传递值，需要使用`defineEmits`

示例：<br />子组件`CompA.vue`
```html
<script setup>
defineProps({
  msg: String
})

const emit = defineEmits(['func'])

function func() {
  emit('func', 'func called')
}
</script>

<template>
  <div>{{msg}}</div>
  <button @click="func">func</button>
</template>
```
父组件`App.vue`
```html
<script setup>
import CompA from './components/Comp-A.vue'

function fun(text) {
  console.log(text)
}
</script>

<template>
<CompA msg="hello" @func='fun'></CompA>
</template>
```
上面的示例：从父组件传递一个msg的参数到子组件，子组件通过`defineProps`接收，相当于optional API的`props`选项；子组件通过 `defineEmits` 定义emit，组件中有一个按钮，点击的时候，通过`emit`定义自定义事件并传出数据，父组件同样使用`@`或`v-on:`接收。

<a name="YO4cb"></a>
### 组件ref
通过引入组件的方式获取组件ref，默认是不会暴露任何声明的数据的，需要使用`defineExpose`暴露属性或方法。

示例：<br />子组件`CompA.vue`
```html
<script setup>
function func() {
  console.log('func called')
}

const a = 1
const b = ref(2)

defineExpose({
  a,
  b,
  func
})
</script>
```
父组件`App.vue`
```html
<script setup>
import CompA from './components/Comp-A.vue'
import { onMounted } from 'vue'

const compA = $ref(null)
onMounted(() => {
  // 在渲染完成后，才能获取到此组件对象
  console.log(compA)
})
</script>

<template>
	<CompA ref='compA'></CompA>
</template>
```
除了使用组件ref外，通过`$parent`获取也是同样的操作。

<a name="KZps0"></a>
## 自定义指令
自定义指令，必须按`vNameOfDirective`的格式创建。

示例：
```html
<script setup>
let count = $ref(0)

function inc() {
  count++
}

const vClickDirective = {
  mounted: (el) => {
    el.click()
  }
}
</script>

<template>
  <div>{{count}}</div>
  <button @click="inc" v-click-directive>increase</button>
</template>
```

