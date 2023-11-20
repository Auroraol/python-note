<a name="7XY4X"></a>
## 一、从一个示例入手
先看一个官方的示例：
```vue
<template>
  <button @click="increment">
    Count is: {{ state.count }}, double is: {{ state.double }}
  </button>
</template>

<script>
import { reactive, computed } from 'vue'

export default {
  setup() {
    const state = reactive({
      count: 0,
      double: computed(() => state.count * 2)
    })

    function increment() {
      state.count++
    }

    return {
      state,
      increment
    }
  }
}
</script>
```

从上面的程序可以看到，在Vue3中，新增了一个setup函数。这是一个新的组件选项。作为在组件内使用Composition API的入口点。

<a name="W2a9V"></a>
## 二、为什么使用Composition API

在Vue2中，使用的是Options API。为了向 Vue 组件添加逻辑，我们填充（可选）属性，例如 data、methods、computed等。这种方法的最大缺点是其本身并不是有效的 JavaScript 代码。你需要确切地知道模板中可以访问哪些属性以及 this 关键字的行为。在后台，Vue 编译器需要将此属性转换为工作代码。因此我们无法从自动建议或类型检查中受益。

Composition API 旨在通过将组件属性中当前可用的机制公开为 JavaScript 函数来解决这个问题。 Vue 核心团队将组件 API 描述为 “一组基于函数的附加 API，可以灵活地组合组件逻辑。” 用Composition  API 编写的代码更具有可读性，并且其背后没有任何魔力，因此更易于阅读和学习。

Vue官方文档中提到一个 **逻辑关注点** 的概念。简而言之，就是不按Vue2那种按选项组织代码，而是按功能逻辑来组织代码。详见：[逻辑关注点 vs. 选项类型](https://composition-api.vuejs.org/zh/#%E4%BB%A3%E7%A0%81%E7%BB%84%E7%BB%87)

<a name="tXrjY"></a>
### setup函数的调用时机
创建组件实例,然后初始化`props`，紧接着就调用`setup`函数。从生命周期钩子的视角来看，他会在 `beforeCreate` 钩子之前被调用。

<a name="zbbae"></a>
### 与现有的 API 配合
组合式 API 完全可以和现有的基于选项的 API 配合使用。

- 组合式 API 会在 2.x 的选项 (`data`、`computed` 和 `methods`) 之前解析，并且不能提前访问这些选项中定义的 property。
- `setup()` 函数返回的 property 将会被暴露给 `this`。它们在 2.x 的选项中可以访问到。

<a name="Ls7dM"></a>
## 三、Composition API解析
再看一个例子，这是上面例子的修改版：
```vue
<template>
 <div>count: {{count}}</div>
 <div>double: {{double}}</div>
 <button @click="add">+1</button>
 <button @click="subtract">-1</button>
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue'

export default {
  setup() {
    let count = ref(0)
    let double = computed(() => count.value * 2)

    function add() {
      count.value += 1
    }
    function subtract() {
      count.value -= 1
    }

    onMounted(() => { console.log('onMounted') })

    return {
      add,
      subtract,
      count,
      double,
    }
  },
}
</script>
```

在Composition API中，通过setup函数暴露一些属性和方法，达到数据响应、生命周期Hook、计算属性的目的。简而言之，它只是一个将属性和函数返回到模板的函数，我们在这里声明所有响应性属性、计算属性、观察者、方法、和生命周期 hook，然后将它们返回，以便可以在模板中使用它们。我们不从 setup 函数返回的内容在模板中将会变得不可用。

**核心Composition API**<br />核心的Composition API有下面这些：

- **ref：**接收一个参数值并返回一个响应式且可改变的 ref 对象。ref 对象拥有一个指向内部值的单一属性 `.value`。
- **reactive：**接收一个普通对象/ref对象然后返回该普通对象/ref对象的响应式代理。
- **computed**：传入一个 getter 函数，返回一个默认不可手动修改的 ref 对象。
- **readonly**：传入一个对象（响应式或普通）或 ref，返回一个原始对象的只读代理。一个只读的代理是“深层的”，对象内部任何嵌套的属性也都是只读的。
- **watchEffect**：立即执行传入的一个函数，并响应式追踪其依赖，并在其依赖变更时重新运行该函数。可显式的调用返回值以停止侦听。
- **watch**：全等效于 2.x `this.$watch`（以及 watch 中相应的选项）。

<a name="rGgtG"></a>
### ref
接收一个参数值并返回一个响应式且可改变的 ref 对象。ref 对象拥有一个指向内部值的单一属性 `.value`。
```typescript
const count = ref(0)
console.log(count.value) // 0

count.value++
console.log(count.value) // 1
```
如果传入 ref 的是一个对象，将调用 `reactive` 方法进行深层响应转换。

`setup` 返回的 ref 在模板中会自动解开，不需要写 `.value`。
```vue
<script setup>
import { ref } from 'vue'

const count = ref(1)
count.value++
</script>

<template>
<div>{{count}}</div>
</template>
```

**类型定义**
```typescript
interface Ref<T> {
  value: T
}
function ref<T>(value: T): Ref<T>
```

有时我们可能需要为 ref 做一个较为复杂的类型标注。我们可以通过在调用 `ref` 时传递泛型参数来覆盖默认推导：
```typescript
const foo = ref<string | number>('foo') // foo 的类型: Ref<string | number>
foo.value = 123 // 能够通过！
```

<a name="AUf6l"></a>
### reactive
接收一个普通对象然后返回该普通对象的响应式代理。等同于 2.x 的 `Vue.observable()`
```javascript
const obj = reactive({ count: 0 })
```
响应式转换是“深层的”：会影响对象内部所有嵌套的属性。基于 ES2015 的 Proxy 实现，返回的代理对象**不等于**原始对象。建议仅使用代理对象而避免依赖原始对象。

**类型定义**
```javascript
function reactive<T extends object>(target: T): UnwrapNestedRefs<T>
```

**将一个ref作为reactive的属性**<br />reactive 将解包所有深层的 refs，同时维持 ref 的响应性。
```javascript
const count = ref(1)
const obj = reactive({ count })

// ref 会被解包
console.log(obj.count === count.value) // true

// 它会更新 `obj.count`
count.value++
console.log(count.value) // 2
console.log(obj.count) // 2

// 它也会更新 `count` ref
obj.count++
console.log(obj.count) // 3
console.log(count.value) // 3
```
也可以创建一个空对象的reactive，在后续将其属性赋值为ref，将同样具有响应性。
```javascript
const count = ref(1)
const obj = reactive({})
obj.count = count // 后续将ref赋值给reactive

// ref 会被解包
console.log(obj.count === count.value) // true

// 它会更新 `obj.count`
count.value++
console.log(count.value) // 2
console.log(obj.count) // 2

// 它也会更新 `count` ref
obj.count++
console.log(obj.count) // 3
console.log(count.value) // 3
```
但如果是通过`$ref`语法糖创建的ref，他们之间的响应性将丢失。
```javascript
const count = $ref(1)
const obj = reactive({})
obj.count = count

// ref 会被解包
console.log(obj.count === count) // true

// 不会更新 `obj.count`
count = 2
console.log(count) // 2
console.log(obj.count) // 1

// 不会更新 `count` ref
obj.count = 3
console.log(obj.count) // 3
console.log(count) // 2
```
注意当嵌套在 reactive `Object` 中时，ref 才会解套。从 `Array` 或者 `Map` 等原生集合类中访问 ref 时，不会自动解套：
```javascript
const arr = reactive([ref(0)])
// 这里需要 .value
console.log(arr[0].value)
const map = reactive(new Map([['foo', ref(0)]]))
// 这里需要 .value
console.log(map.get('foo').value)
```


<a name="computed"></a>
### computed
传入一个 getter 函数，返回一个默认不可手动修改的 ref 对象。
```javascript
const count = ref(1)
const plusOne = computed(() => count.value + 1)
console.log(plusOne.value) // 2
plusOne.value++ // 错误！
```

<a name="IMNCZ"></a>
#### getter和setter
传入一个拥有 `get` 和 `set` 函数的对象，创建一个可手动修改的计算状态。
```javascript
const count = ref(1)
const plusOne = computed({
  get: () => count.value + 1,
  set: (val) => {
    count.value = val - 1
  },
})
plusOne.value = 1
console.log(count.value) // 0
```

<a name="888JD"></a>
#### 类型定义
```typescript
// 只读的
function computed<T>(getter: () => T): Readonly<Ref<Readonly<T>>>
// 可更改的
function computed<T>(options: {
  get: () => T
  set: (value: T) => void
}): Ref<T>
```

<a name="readonly"></a>
### readonly
传入一个对象（响应式或普通）或 ref，返回一个原始对象的**只读**代理。一个只读的代理是“深层的”，对象内部任何嵌套的属性也都是只读的。
```javascript
const original = reactive({ count: 0 })
const copy = readonly(original)
watchEffect(() => {
  // 依赖追踪
  console.log(copy.count)
})

// original 上的修改会触发 copy 上的侦听
original.count++

// 无法修改 copy 并会被警告
copy.count++ // warning!
```

<a name="watcheffect"></a>
### watchEffect
立即执行传入的一个函数，并响应式追踪其依赖，并在其依赖变更时重新运行该函数。
```javascript
const count = ref(0)
watchEffect(() => console.log(count.value))
// -> 打印出 0
setTimeout(() => {
  count.value++
  // -> 打印出 1
}, 100)
```

<a name="I5jjd"></a>
#### 停止侦听
当 `watchEffect` 在组件的 `setup()` 函数或生命周期钩子被调用时， 侦听器会被链接到该组件的生命周期，并在组件卸载时自动停止。<br />在一些情况下，也可以显式调用返回值以停止侦听：
```javascript
const stop = watchEffect(() => {
  /* ... */
})
// 之后
stop()
```

<a name="OtBOu"></a>
#### flush 属性
如果副作用需要同步或在组件更新之前重新运行，我们可以传递一个拥有 `flush` 属性的对象作为选项（默认为 `'post'`）：
```javascript
// 同步运行
watchEffect(
  () => {
    /* ... */
  },
  {
    flush: 'sync',
  }
)
// 组件更新前执行
watchEffect(
  () => {
    /* ... */
  },
  {
    flush: 'pre',
  }
)
```

<a name="OcQDQ"></a>
#### 在指定的时机执行
`watchEffect` 可以结合生命周期，在特定的时机执行：
```javascript
const data = ref(null)

onMounted(() => {
  watchEffect(async () => {
    data.value = await fetchData(props.id)
  })
})
```

<a name="LOrud"></a>
#### 侦听器调试
`onTrack` 和 `onTrigger` 选项可用于调试一个侦听器的行为。

- 当一个 reactive 对象属性或一个 ref 作为依赖被追踪时，将调用 `onTrack`
- 依赖项变更导致副作用被触发时，将调用 `onTrigger`

这两个回调都将接收到一个包含有关所依赖项信息的调试器事件。建议在以下回调中编写 `debugger` 语句来检查依赖关系：
```javascript
watchEffect(
  () => {
    /* 副作用的内容 */
  },
  {
    onTrigger(e) {
      debugger
    },
  }
)
```


`**onTrack**`** 和 **`**onTrigger**`** 仅在开发模式下生效。**

<a name="UBxxj"></a>
#### 类型定义
```typescript
function watchEffect(
  effect: (onInvalidate: InvalidateCbRegistrator) => void,
  options?: WatchEffectOptions
): StopHandle
interface WatchEffectOptions {
  flush?: 'pre' | 'post' | 'sync'
  onTrack?: (event: DebuggerEvent) => void
  onTrigger?: (event: DebuggerEvent) => void
}
interface DebuggerEvent {
  effect: ReactiveEffect
  target: any
  type: OperationTypes
  key: string | symbol | undefined
}
type InvalidateCbRegistrator = (invalidate: () => void) => void
type StopHandle = () => void
```
<a name="watch"></a>
### watch
`watch` API 完全等效于 2.x `this.$watch` （以及 `watch` 中相应的选项）。`watch` 需要侦听特定的数据源，并在回调函数中执行副作用。默认情况是懒执行的，也就是说仅在侦听的源变更时才执行回调。

对比`watchEffect`，`watch`允许我们：

   - 懒执行副作用；
   - 更明确哪些状态的改变会触发侦听器重新运行副作用；
   - 访问侦听状态变化前后的值。

<a name="4MGFp"></a>
#### 侦听单个数据源
侦听器的数据源可以是一个拥有返回值的 getter 函数，也可以是 ref：
```javascript
// 侦听一个 getter
const state = reactive({ count: 0 })
watch(
  () => state.count,
  (count, prevCount) => {
    /* ... */
  }
)
// 直接侦听一个 ref
const count = ref(0)
watch(count, (count, prevCount) => {
  /* ... */
})
```
<br />
<a name="iV1Ds"></a>
#### 侦听多个数据源
`watcher` 也可以使用数组来同时侦听多个源：
```javascript
watch([fooRef, barRef], ([foo, bar], [prevFoo, prevBar]) => {
  /* ... */
})
```

监听路由变化：
```javascript
const route = useRoute()

watch(
  () => [route.name, route.query],
  () => {...}
)
```

<a name="HR1wL"></a>
#### 类型定义
```typescript
// 侦听单数据源
function watch<T>(
  source: WatcherSource<T>,
  callback: (
    value: T,
    oldValue: T,
    onInvalidate: InvalidateCbRegistrator
  ) => void,
  options?: WatchOptions
): StopHandle
// 侦听多数据源
function watch<T extends WatcherSource<unknown>[]>(
  sources: T
  callback: (
    values: MapSources<T>,
    oldValues: MapSources<T>,
    onInvalidate: InvalidateCbRegistrator
  ) => void,
  options? : WatchOptions
): StopHandle
type WatcherSource<T> = Ref<T> | (() => T)
type MapSources<T> = {
  [K in keyof T]: T[K] extends WatcherSource<infer V> ? V : never
}
// 共有的属性 请查看 `watchEffect` 的类型定义
interface WatchOptions extends WatchEffectOptions {
  immediate?: boolean // default: false
  deep?: boolean
}
```

可以看出，`WatchOptions`继承自 `WatchEffectOptions`，因此， `watchEffect` 中的选项 `watch` 也能够使用。

<a name="tEcYw"></a>
### 生命周期
可以直接导入 `onXXX` 一族的函数来注册生命周期钩子：
```javascript
import { onMounted, onUpdated, onUnmounted } from 'vue'
const MyComponent = {
  setup() {
    onMounted(() => {
      console.log('mounted!')
    })
    onUpdated(() => {
      console.log('updated!')
    })
    onUnmounted(() => {
      console.log('unmounted!')
    })
  },
}
```

这些生命周期钩子注册函数只能在 `setup()` 期间同步使用， 因为它们依赖于内部的全局状态来定位当前组件实例（正在调用 `setup()` 的组件实例）, 不在当前组件下调用这些函数会抛出一个错误。

组件实例上下文也是在生命周期钩子同步执行期间设置的，因此，在卸载组件时，在生命周期钩子内部同步创建的侦听器和计算状态也将自动删除。

<a name="CGVem"></a>
#### 与 2.x 版本生命周期相对应的组合式 API

- `~~beforeCreate~~` -> 使用 `setup()`
- `~~created~~` -> 使用 `setup()`
- `beforeMount` -> `onBeforeMount`
- `mounted` -> `onMounted`
- `beforeUpdate` -> `onBeforeUpdate`
- `updated` -> `onUpdated`
- `beforeDestroy` -> `onBeforeUnmount`
- `destroyed` -> `onUnmounted`
- `errorCaptured` -> `onErrorCaptured`

<a name="9pGq8"></a>
#### 新增的钩子函数
除了和 2.x 生命周期等效项之外，组合式 API 还提供了以下调试钩子函数：

- `onRenderTracked`
- `onRenderTriggered`

两个钩子函数都接收一个 `DebuggerEvent`，与 `watchEffect` 参数选项中的 `onTrack` 和 `onTrigger` 类似：
```javascript
export default {
  onRenderTriggered(e) {
    debugger
    // 检查哪个依赖性导致组件重新渲染
  },
}
```

<a name="zvAv7"></a>
### 其他相关API

- `isProxy` 检查对象是否是由 [reactive](https://v3.cn.vuejs.org/api/basic-reactivity.html#reactive) 或 [readonly](https://v3.cn.vuejs.org/api/basic-reactivity.html#readonly) 创建的 proxy。
- `isReactive` 检查对象是否是由 [reactive](https://v3.cn.vuejs.org/api/basic-reactivity.html#reactive) 创建的响应式代理。如果该代理是 [readonly](https://v3.cn.vuejs.org/api/basic-reactivity.html#readonly) 创建的，但包裹了由 [reactive](https://v3.cn.vuejs.org/api/basic-reactivity.html#reactive) 创建的另一个代理，它也会返回 true。
- `isReadonly` 检查对象是否是由 [readonly](https://v3.cn.vuejs.org/api/basic-reactivity.html#readonly) 创建的只读代理。


<a name="laWDD"></a>
### setup的返回值
数据和方法都需要通过在setup中返回，模板才能够使用。

<a name="3zSmR"></a>
## 四、Vuex状态管理
在Composition API中，Vuex状态管理暴露了一个 `useStore` 方法，可以直接获取到 `this.$store` 的引用：
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

以后就再也不用 `this.$store.commit` 、 `this.$store.dispatch` 地用了，很爽是不是。

<a name="RTI1g"></a>
## 五、setup的参数
<a name="m2pzK"></a>
### props
setup支持接收参数，第一个参数是props，接收来自父组件的传值。

比如有如下一个组件 `HelloWorld` ：
```vue
<template>
  <h1>{{ msg }}</h1>
</template>

<script>
import { watchEffect } from 'vue'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  setup(props) {
    watchEffect(() => {
      console.log(props.msg)
    })
  }
}
</script>
```

`props` 是响应式的，作为参数传递到setup，watchEffect可以监听到props的变化。

在父组件中：
```vue
<template>
<HelloWorld :msg="msg"></HelloWorld>
<button @click="setData">设置数据</button>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue'

export default {
  components: { HelloWorld },
  setup() {
    let msg = ref('Hello xiaoyu')
    function setData() {
      msg.value = 'Hello world'
    }

    return {
      msg,
      setData
    }
  },
}
</script>
```

点击按钮，修改父组件中的msg，对应子组件中的数据也会得到修改，并触发watchEffect。

![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1606984738401-81add756-aee8-4ed9-9ca0-be00d4c53016.gif#height=113&id=i5yTg&originHeight=113&originWidth=250&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7964&status=done&style=none&title=&width=250)

值得注意的是，子组件中的**props不能直接解构**，否则会使watchEffect失效，使其失去响应性：
```javascript
  setup({msg}) {
    watchEffect(() => {
      console.log(msg)
    })
  }
```

<a name="iqwWh"></a>
### context
第二个参数提供了一个上下文对象，从原来 2.x 中 `this` 选择性地暴露了一些 property。
```javascript
const MyComponent = {
  setup(props, context) {
    context.attrs
    context.slots
    context.emit
  },
}
```

`attrs` 和 `slots` 都是内部组件实例上对应项的代理，可以确保在更新后仍然是最新值。所以可以解构，无需担心后面访问到过期的值：
```javascript
const MyComponent = {
  setup(props, { attrs }) {
    // 一个可能之后回调用的签名
    function onClick() {
      console.log(attrs.foo) // 一定是最新的引用，没有丢失响应性
    }
  },
}
```

出于一些原因将 `props` 作为第一个参数，而不是包含在上下文中：

- 组件使用 `props` 的场景更多，有时候甚至只使用 `props`
- 将 `props` 独立出来作为第一个参数，可以让 TypeScript 对 `props` 单独做类型推导，不会和上下文中的其他属性相混淆。这也使得 `setup` 、 `render` 和其他使用了 TSX 的函数式组件的签名保持一致。

<a name="LX8QZ"></a>
## 六、逻辑提取与复用
再看一个官方的例子：
```javascript
import { ref, onMounted, onUnmounted } from 'vue'

export function useMousePosition() {
  const x = ref(0)
  const y = ref(0)

  function update(e) {
    x.value = e.pageX
    y.value = e.pageY
  }

  onMounted(() => {
    window.addEventListener('mousemove', update)
  })

  onUnmounted(() => {
    window.removeEventListener('mousemove', update)
  })

  return { x, y }
}
```
这是一个监听鼠标移动的代码封装，以下是一个组件如何利用该函数的展示：
```javascript
import { useMousePosition } from './mouse'
export default {
  setup() {
    const { x, y } = useMousePosition()
    // 其他逻辑...
    return { x, y }
  },
}
```

这样，就达到了逻辑解耦以及代码复用的目的。

<a name="tPPDd"></a>
## 七、解构丢失响应性
在前面props的例子中我们已经知道。解构props会使其丢失响应性。真实情况是，在尝试对响应式对象（reactive）进行解构的时候，响应性都会丢失。看一个官方的例子：
```javascript
// 组合函数：
function useMousePosition() {
  const pos = reactive({
    x: 0,
    y: 0,
  })

  // ...
  return pos
}

// 消费者组件
export default {
  setup() {
    // 这里会丢失响应性!
    const { x, y } = useMousePosition()
    return {
      x,
      y,
    }

    // 这里会丢失响应性!
    return {
      ...useMousePosition(),
    }

    // 这是保持响应性的唯一办法！
    // 你必须返回 `pos` 本身，并按 `pos.x` 和 `pos.y` 的方式在模板中引用 x 和 y。
    return {
      pos: useMousePosition(),
    }
  },
}
```

这也是为什么框架需要将基本数据类型的ref包装成一个对象的原因，详细的内容请看：

- [Ref vs. Reactive](https://composition-api.vuejs.org/zh/#ref-vs-reactive)
- [计算状态 与 Ref](https://composition-api.vuejs.org/zh/#%E8%AE%A1%E7%AE%97%E7%8A%B6%E6%80%81-%E4%B8%8E-ref)

贴上一张官方的示意图，以便能够更形象地理解：<br />![pass-by-reference-vs-pass-by-value-animation.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607046725674-655f8a7b-f3da-46f3-899f-5be0ba781715.gif#height=270&id=uxTtw&originHeight=270&originWidth=500&originalType=binary&ratio=1&rotation=0&showTitle=false&size=119091&status=done&style=none&title=&width=500)

<a name="tQczQ"></a>
## 八、模板 Refs
在Vue2中，ref用于获取模板中的元素，而在使用组合式 API 时，_reactive refs_ 和 _template refs_ 的概念已经是统一的。为了获得对模板内元素或组件实例的引用，我们可以像往常一样在 `setup()` 中声明一个 ref 并返回它：
```vue
<template>
  <div ref="root"></div>
</template>
<script>
  import { ref, onMounted } from 'vue'
  export default {
    setup() {
      const root = ref(null)
      onMounted(() => {
        // 在渲染完成后, 这个 div DOM 会被赋值给 root ref 对象
        console.log(root.value) // <div/>
      })
      return {
        root,
      }
    },
  }
</script>
```

这里我们将 `root` 暴露在渲染上下文中，并通过 `ref="root"` 绑定到 `div` 作为其 `ref`。 在 Virtual DOM patch 算法中，如果一个 VNode 的 `ref` 对应一个渲染上下文中的 ref，则该 VNode 对应的元素或组件实例将被分配给该 ref。 这是在 Virtual DOM 的 mount / patch 过程中执行的，因此模板 ref 仅在渲染初始化后才能访问。

ref 被用在模板中时和其他 ref 一样：都是响应式的，并可以传递进组合函数（或从其中返回）。

<a name="70cXm"></a>
#### **函数型的 ref**
在Vue3中另一个比较有趣的变化是template ref可以是函数类型，例如在一个循环中，需要将循环出来的每一个元素都绑定一个ref的情景：
```vue
<template>
  <div v-for="(item, i) in list" :ref="el => { divs[i] = el }">
    {{ item }}
  </div>
</template>

<script>
  import { ref, reactive, onBeforeUpdate } from 'vue'

  export default {
    setup() {
      const list = reactive([1, 2, 3])
      const divs = ref([])

      // 确保在每次变更之前重置引用
      onBeforeUpdate(() => {
        divs.value = []
      })

      return {
        list,
        divs,
      }
    },
  }
</script>
```

<a name="0t59p"></a>
### 配合 render 函数 / JSX 的用法
```javascript
import { ref, h } from 'vue'

export default {
  setup() {
    const root = ref(null)
    return () =>
      h('div', {
        ref: root,
      })
    
    // 等效于使用 JSX
    return () => <div ref={root} />
  },
}
```

<a name="OTZ3d"></a>
## 九、获取当前组件实例
在setup中，并不能直接使用this获取当前组件实例，而需要使用 `getCurrentInstance` 方法来获取当前组件实例：
```typescript
import { getCurrentInstance } from 'vue'

export default {
  setup () {
    const instance = getCurrentInstance()
    console.log(instance)
    const vm = instance.ctx
    console.log(vm)
  }
}
```

其中 `instance` 长这样：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607309926252-f9220c70-b5c7-4348-a079-2c0157c08da2.png#height=853&id=Quk9z&originHeight=853&originWidth=989&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68849&status=done&style=none&title=&width=989)

我们在Vue2中习以为常的`this`挂载到了`ctx`中：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607309999990-dd2dfd41-eae2-4c1b-92ea-9e22943f24c7.png#height=855&id=fvMA4&originHeight=855&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&size=48860&status=done&style=none&title=&width=430)

<a name="HtQhs"></a>
## 参考资料

- [组合式 API 征求意见稿](https://composition-api.vuejs.org/zh/) / [[英文版：Composition API RFC]](https://vue-composition-api-rfc.netlify.app/)
- [Vue 组合式 API](https://composition-api.vuejs.org/zh/api.html#setup) / [[英文版：API Reference]](https://composition-api.vuejs.org/api.html)
- [GitHub：RFC：function-api](https://github.com/vuejs/rfcs/blob/function-apis/active-rfcs/0000-function-api.md) / [@vue/composition-api](https://github.com/vuejs/composition-api)
- [Vue 3.x 响应式原理——reactive源码分析](https://zhuanlan.zhihu.com/p/89940326)
- [Vue Composition API 响应式包装对象原理](https://github.com/xingbofeng/xingbofeng.github.io/issues/46)
- [Vue 3 Composition API-原汁原味,全新全异](https://zhuanlan.zhihu.com/p/134758988)
- [Vue 3 中令人兴奋的新功能](https://segmentfault.com/a/1190000020933028)

<a name="I7QYM"></a>
## 项目示例

- [Demo App for the Composition API](https://github.com/LinusBorg/composition-api-demos)


