本文搜集了一些非常不错的RFC，有可能实现了，也有可能没有实现，大部分在本文编写时还未实现，以官方RFC为主：[Vue RFCs](https://github.com/vuejs/rfcs)。
<a name="JknjD"></a>

## style-variables

可以在css中使用js变量，方便通过js动态修改样式。

[第一阶段的提案](https://github.com/vuejs/rfcs/blob/style-vars/active-rfcs/0000-sfc-style-variables.md)：
```vue
<template>
  <div class="text">hello</div>
</template>

<script>
export default {
  data() {
    return {
      color: 'red'
    }
  }
}
</script>

<style vars="{ color }">
.text {
  color: var(--color);
}
</style>
```
[第二阶段的提案](https://github.com/vuejs/rfcs/blob/style-vars-2/active-rfcs/0000-sfc-style-variables.md)：State-driven CSS Variable Injection in `<style>`
```vue
<template>
  <div class="text">hello</div>
</template>

<script>
  export default {
    data() {
      return {
        color: 'red',
        font: {
          size: '2em',
        },
      }
    },
  }
</script>

<style>
  .text {
    color: v-bind(color);

    /* expressions (wrap in quotes) */
    font-size: v-bind('font.size');
  }
</style>
```

<a name="FHZfz"></a>
## script setup & ref sugar
将setup暴露到script级别，直接暴露顶级变量，不需要写 `export default` ，减少代码量。
```vue
<script setup>
// imported components are also directly usable in template
import Foo from './Foo.vue'
import { ref } from 'vue'

// write Composition API code just like in a normal setup()
// but no need to manually return everything
const count = ref(0)
const inc = () => { count.value++ }
</script>

<template>
  <Foo :count="count" @click="inc" />
</template>
```
ref语法糖示例：
```vue
<script setup>
// declaring a variable that compiles to a ref
ref: count = 1

function inc() {
  // the variable can be used like a plain value
  count++
}

// access the raw ref object by prefixing with $
console.log($count.value)
</script>

<template>
  <button @click="inc">{{ count }}</button>
</template>
```

详见：

- [script-setup](https://github.com/vuejs/rfcs/blob/script-setup/active-rfcs/0000-script-setup.md)
- [sfc-script-setup](https://github.com/vuejs/rfcs/blob/sfc-improvements/active-rfcs/0000-sfc-script-setup.md)
- [New script setup and ref sugar](https://github.com/vuejs/rfcs/pull/222)
- [SFC Improvements](https://github.com/vuejs/rfcs/pull/182)
- [New `<script setup>` and ref sugar implementation](https://github.com/vuejs/vue-next/pull/2532)
- [Reactivity Transform · Discussion #369 · vuejs/rfcs](https://github.com/vuejs/rfcs/discussions/369)

<a name="UeCDN"></a>
## deep selectors in style scoped
以前在Vue中使用 `/deep/` 也可做穿透选择器，在Vue3中增强了这一特性，包括如下选择器：
```vue
<style scoped>
/* deep selectors */
::v-deep(.foo) {}
/* shorthand */
:deep(.foo) {}

/* targeting slot content */
::v-slotted(.foo) {}
/* shorthand */
:slotted(.foo) {}

/* one-off global rule */
::v-global(.foo) {}
/* shorthand */
:global(.foo) {}
</style>
```

详见：

- [scoped-styles-changes](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0023-scoped-styles-changes.md)

<a name="R1Ggz"></a>
## props sugar
参考：

- [prop sugar](https://github.com/vuejs/rfcs/issues/229)

<a name="sqYel"></a>
## vite：Pug support
参考：

- [Pug support](https://github.com/vitejs/vite/issues/17)

