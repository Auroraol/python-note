使用Vite创建的Vue3项目，支持直接创建 `jsx` 和 `tsx` 文件，并编写jsx/tsx代码。

<a name="NnAok"></a>
## 一、创建并引入JSX组件
创建一个 `Counter.jsx` ，目录结构如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607071362294-2dca899b-3fa3-407d-aac2-0b71dad71f3b.png#align=left&display=inline&height=174&originHeight=174&originWidth=220&size=10149&status=done&style=none&width=220)

`Counter.jsx` 内容如下：
```javascript
import { ref, withModifiers, defineComponent } from 'vue';

export default defineComponent({
  setup() {
    const count = ref(0)

    const inc = () => {
      count.value++
    }

    const dec = () => {
      count.value--
    }

    return () => (
      <div>
        <button onClick={withModifiers(inc, ['self'])}>+1</button>
        <button onClick={withModifiers(dec, ['self'])}>-1</button>
        <div>{count.value}</div>
      </div>
    )
  }
})

```
以上，通过 `defineComponent` 创建组件，通过 `withModifiers` 绑定到setup中的方法。

在 `Home.vue` 中引入：
```vue
<template>
<Counter />
</template>

<script>
import Counter from '../components/Counter'

export default {
  components: { Counter }
}
</script>
```
效果如下：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607071478175-b5be18d0-0f07-4635-b8aa-ccea11d9ff5f.gif#align=left&display=inline&height=93&originHeight=93&originWidth=141&size=6183&status=done&style=none&width=141)<br />其中， `Counter.jsx` 可以完全使用jsx原生写法，而不使用vue中的`defineComponent` 和 `withModifiers`：
```javascript
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(0)

    return () => (
      <>
        <button onClick={() => { count.value++ }}>+1</button>
        <button onClick={() => { count.value-- }}>-1</button>
        <div>{count.value}</div>
      </>
    )
  }
}
```

当然，以下写法也是完全没问题的：
```javascript
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(0)

    const inc = () => {
      count.value++
    }

    const dec = () => {
      count.value--
    }

    return () => (
      <div>
        <button onClick={inc}>+1</button>
        <button onClick={dec}>-1</button>
        <div>{count.value}</div>
      </div>
    )
  }
}
```

甚至可以直接使用Vue的Options API中的 `render` 进行渲染：
```javascript
export default {
  data() {
    return {
      count: 0
    }
  },
  render() {
    return (
      <>
        <button onClick={() => { this.count++ }}>+1</button>
        <button onClick={() => { this.count-- }}>-1</button>
        <div>{this.count}</div>
      </>
    )
  }
}
```

<a name="GI276"></a>
## 二、使用JSX的一些弊端

从目前使用jsx来看，还存在以下一些问题，这些将丢失Vue3比较好的一些特性：

1. 模板不支持多入口，比如：
```javascript
return () => (
  <div></div>
  <div></div>
)
```

2. 不支持使用 `@` 绑定事件，比如：
```javascript
return () => (
  <div @click="xxx"></div>
)
```

3. 在模板中必须添加 `.value` 属性才能访问到 `ref` 的值，比如：
```javascript
  setup() {
    const count = ref(0)
    return () => (
      <div>{count.value}</div>
    )
  }
```

<a name="4DqtS"></a>
## 参考资料

- [vite：jsx](https://github.com/vitejs/vite#jsx)
- [jsx-next](https://github.com/vuejs/jsx-next)
- [Babel Preset JSX](https://github.com/vuejs/jsx)
