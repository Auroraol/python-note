- [Pinia官网](https://pinia.vuejs.org/)

<a name="aI6ez"></a>
## Pinia简介






<a name="VGVHI"></a>
## Pinia集成
<a name="qqr3b"></a>
### 安装Pinia
```javascript
yarn add pinia
```

<a name="rNpyX"></a>
### 在Vue2项目中集成


<a name="kK36G"></a>
### 在Vue3项目中集成
`main.js`
```javascript
import { createApp } from 'vue'
import App from './App.vue'

import { createPinia } from 'pinia'

let app = createApp(App)

app.use(createPinia())
app.mount('#app')
```
创建一个状态管理（选项式）：
```javascript
import { defineStore } from 'pinia'

export const useStore = defineStore('main', {
  state: () => ({ count: 0 }),
  getters: {
    double: (state) => state.count * 2,
  },
  actions: {
    increment() {
      this.count++
    },
  },
})
```
在Vue3组件中引入：
```vue
<template>
<div>{{store.count}}</div>
</template>

<script>
import { useStore } from '/src/store/index'

export default {
  setup() {
    const store = useStore()

    // 通过以下三种方式都可以修改状态
    store.count++
    store.$patch({ count: store.count + 1 })
    store.increment()

    return {
      store,
    }
  },
}
</script>
```
要变更状态管理，可以直接对其值进行操作，比如上面的 `store.count++`；也可以使用 `$patch`进行操作，相当于Vuex中的Mutation，只是处理起来更简单；或者使用`actions`进行操作。

<a name="DCY1t"></a>
## Pinia使用指南
一个完整的Pinia状态管理包括：

- `state` 状态
- `getters` 相当于状态的计算属性
- `actions` 相当于操作状态的方法

示例：
```javascript
import { defineStore } from 'pinia'

export const todos = defineStore('todos', {
  state: () => ({
    /** @type {{ text: string, id: number, isFinished: boolean }[]} */
    todos: [],
    /** @type {'all' | 'finished' | 'unfinished'} */
    filter: 'all',
    // type will be automatically inferred to number
    nextId: 0,
  }),
  getters: {
    finishedTodos(state) {
      // autocompletion! ✨
      return state.todos.filter((todo) => todo.isFinished)
    },
    unfinishedTodos(state) {
      return state.todos.filter((todo) => !todo.isFinished)
    },
    /**
     * @returns {{ text: string, id: number, isFinished: boolean }[]}
     */
    filteredTodos(state) {
      if (this.filter === 'finished') {
        // call other getters with autocompletion ✨
        return this.finishedTodos
      } else if (this.filter === 'unfinished') {
        return this.unfinishedTodos
      }
      return this.todos
    },
    // getters可以返回一个方法
    getTodoById(state) {
      return (todoId) => state.todos.find((todo) => todo.id === todoId)
    },
  },
  actions: {
    // any amount of arguments, return a promise or not
    addTodo(text) {
      // you can directly mutate the state
      this.todos.push({ text, id: this.nextId++, isFinished: false })
    },
  },
})
```
使用示例：
```javascript
export default {
  setup() {
    const todoStore = useTodoStore()

    todoStore.addTodo('Vue2')
    todoStore.addTodo('Vue3')
    console.log(todoStore.todos)

    let todo = todoStore.getTodoById(1)
    console.log(todo)

    todo.isFinished = true
    console.log(todoStore.finishedTodos)

    todoStore.filter = 'unfinished'
    console.log(todoStore.filteredTodos)
  },
}
```

<a name="NgqQ7"></a>
### 函数式状态管理
上面创建的状态管理，是以选项的方式创建的；我们也可以使用函数的形式创建：
```javascript
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  function increment() {
    count.value++
  }

  return { count, increment }
})
```
如果是Vue2项目，需要引入 `@vue/composition-api`以在创建状态管理时使用ref。

引用的时候跟选项式创建的状态管理一致：
```vue
<template>
<div>{{store.count}}</div>
</template>

<script>
import { useCounterStore } from '/src/store/count'

export default {
  setup() {
    const store = useCounterStore()

    store.count++
    store.$patch({ count: store.count + 1 })
    store.increment()

    return {
      store,
    }
  },
}
</script>
```

<a name="GJgwc"></a>
### 使用mapXXX在Vue选项中引用
<a name="DALBu"></a>
#### mapStores
引入整个Store，使用`mapStores`：
```javascript
import { mapStores } from 'pinia'
import { useCounterStore } from '/src/store/count'
import { useTodoStore } from '/src/store/todo'

export default {
  computed: {
    ...mapStores(useCounterStore, useTodoStore),
  },
  created() {
    this.counterStore.count++
    console.log(this.counterStore.count) // 1
  }
}
```
通过`mapStores`引入的store，通过去除`use`读取其内部状态，比如引入的是`useCounterStore`，读取的时候使用`this.counterStore`。<br />`mapStores`是可读写的，可以直接修改其内部状态。

<a name="UimmZ"></a>
#### mapState和mapWritableState
通过`mapState`和`mapWritableState`引入的状态，可以通过第二个参数释放要使用的状态。

这两个的区别为：

- 通过`mapState`引入的状态，只能读取
- 通过`mapWritableState`引入的状态，可以读取也可以写入

通过`mapState`和`mapWritableState`既可以引入`state`，也可引入`getters`。

示例：
```javascript
import { mapStores, mapState } from 'pinia'
import { useCounterStore } from '/src/store/count'

export default {
  computed: {
    ...mapStores(useCounterStore),
    // this.count和this.double为只读状态
    ...mapState(useCounterStore, ['count', 'double']),
  },
  created() {
    this.count++
    console.log(this.counterStore.count) // 0
    console.log(this.count) // 0
    this.counterStore.count++
    console.log(this.counterStore.count) // 1
    console.log(this.count) // 1
  }
}
```
从上面的例子可以看出，修改`this.count`，状态并未改变；修改`this.counterStore.count`，状态可以更新。

通过`mapWritableState`引入的状态可读写：
```javascript
import { mapStores, mapWritableState } from 'pinia'
import { useCounterStore } from '/src/store/count'

export default {
  computed: {
    ...mapStores(useCounterStore),
    // this.count和this.double为可读写状态
    ...mapWritableState(useCounterStore, ['count', 'double']),
  },
  created() {
    this.count++
    console.log(this.counterStore.count) // 1
    console.log(this.count) // 1
    this.counterStore.count++
    console.log(this.counterStore.count) // 2
    console.log(this.count) // 2
  }
}
```

<a name="KXi76"></a>
#### 通过对象的形式引入
`mapState`和`mapWritableState`也可通过对象的形式引入：
```javascript
import { mapStores, mapState, mapWritableState } from 'pinia'
import { useCounterStore } from '/src/store/count'

export default {
  computed: {
    ...mapStores(useCounterStore),
    ...mapWritableState(useCounterStore, {
      count: 'count',
      doubleCount: 'double', // 这是一个getters
    }),
  },
  created() {
    this.count = 5
    console.log(this.count) // 5
    console.log(this.counterStore.count) // 5
    console.log(this.doubleCount) // 10
  }
}
```

`mapState`的状态也可以是一个方法，接收一个参数`store`：
```javascript
import { mapStores, mapState, mapWritableState } from 'pinia'
import { useCounterStore } from '/src/store/count'

export default {
  computed: {
    ...mapStores(useCounterStore),
    ...mapState(useCounterStore, {
      doubleCount: store => store.double,
    }),
    ...mapWritableState(useCounterStore, {
      count: 'count',
    }),
  },
  created() {
    this.count = 5
    console.log(this.counterStore.count) // 5
    console.log(this.count) // 5
    console.log(this.doubleCount) // 10
  }
}
```
通常可以将state放到`mapWritableState`中，将getters放到`mapState`中。

<a name="S9urZ"></a>
#### mapActions
`mapActions`同样可以使用数组语法或对象语法引入actions：
```javascript
import { mapActions } from 'pinia'

export default {
  methods: {
    // gives access to this.increment() inside the component
    // same as calling from store.increment()
    ...mapActions(useStore, ['increment'])
    // same as above but registers it as this.doubleInc()
    ...mapActions(useStore, { doubleInc: 'doubleIncrement' }),
  },
}
```

<a name="SdUZQ"></a>
### 监听状态改变
<a name="DXnER"></a>
#### 监听state
```javascript
counterStore.$subscribe((mutation, state) => {
  console.log(mutation.storeId); // 当前store名，此处为counter
  console.log(mutation.type); // 'direct' | 'patch object' | 'patch function'
  console.log(mutation.events);
  console.log(state);
})
```
其中`mutation.events`如下：<br />![Snipaste_2022-01-02_10-45-40.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1641091588080-39faa85f-cbb7-4741-91a9-2a6232112ff8.png#clientId=ud46c068c-4322-4&from=drop&id=u77c5e106&originHeight=167&originWidth=755&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6467&status=done&style=none&taskId=u222ea989-2863-4ce5-9d13-adf218f5e3e&title=)

<a name="LAIbu"></a>
#### 监听actions
```javascript
// 定义一个action监听器，返回值用于取消监听
const unsubscribe = todoStore.$onAction(
  ({
    name, // name of the action
    store, // store instance, same as `someStore`
    args, // array of parameters passed to the action
    after, // hook after the action returns or resolves
    onError, // hook if the action throws or rejects
  }) => {
    // a shared variable for this specific action call
    const startTime = Date.now();
    // this will trigger before an action on `store` is executed
    console.log(`Start "${name}" with params [${args.join(", ")}].`);

    // this will trigger if the action succeeds and after it has fully run.
    // it waits for any returned promised
    after((result) => {
      console.log(
        `Finished "${name}" after ${
        Date.now() - startTime
        }ms.\nResult: ${result}.`
      );
    });

    // this will trigger if the action throws or returns a promise that rejects
    onError((error) => {
      console.warn(
        `Failed "${name}" after ${
        Date.now() - startTime
        }ms.\nError: ${error}.`
      );
    });
  }
);

// 取消监听
unsubscribe()
```

<a name="PppTZ"></a>
#### 使用watch监听
可以使用watch监听整个store：
```javascript
import { watch } from "vue";

export default {
  setup() {
    const counterStore = useCounterStore();

    watch(
      counterStore,
      (state) => {
        console.log(state)
      },
      { deep: true }
    )
  }
}
```
state为整个store：<br />![Snipaste_2022-01-02_10-55-36.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1641092148514-e1a2d99c-8f01-4797-8f29-de5a5ec101dd.png#clientId=ud46c068c-4322-4&from=drop&id=u0ecb15ba&originHeight=413&originWidth=1141&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21111&status=done&style=none&taskId=u3fffb882-2f3a-4210-85c4-eb4b33a9ed9&title=)








