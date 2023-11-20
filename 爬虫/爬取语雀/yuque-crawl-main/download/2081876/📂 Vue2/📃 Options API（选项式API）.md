<a name="0695325f"></a>
## 一、选项对象

当创建一个 Vue 实例时，可以传入一个选项对象。在Vue3中将其称之为Options API。

通常会指定以下选项:

- `el` 指定Vue挂载的DOM元素
- `template` 模板组件
- `components` 组件注册
- `router` 如果项目中用到 vue-router，需要在此加入
- `store` 如果项目中用到 vuex，需要在此加入

一个最简单的示例:
```javascript
import Vue from 'vue'

let template = `<h1>Hello Vue</h1>`

new Vue({
  el: '#app',
  template
})
```

如果是采用组件的方式创建的项目，从外部引入了组件、状态管理、路由，则：
```javascript
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

let vm = new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
```

<a name="7ca7de1b"></a>
## 二、数据和方法（data和methods）
当一个 Vue 实例被创建时，它向 Vue 的响应式系统中加入了其 data 对象中能找到的所有的属性。当这些属性的值发生改变时，视图将会产生“响应”，即匹配更新为新的值。

在模板中绑定一个属性值使用 `{{ }}`

在 Vue 中，使用方法需要将之定义到 methods 选项中，在模板中使用的时候可以用 `@` 进行事件绑定。

举例说明：
```javascript
import Vue from 'vue'

let template = `<h1 @click='func'>{{text}}</h1>`

new Vue({
  el: '#app',
  template,
  data: {
    text: 'Hello'
  },
  methods: {
    func () {
      this.text = 'welcome'
    }
  }
})
```

现象是模板首先渲染出一个 `Hello`，点击之后时候渲染出 `welcome`，这也能看出数据是响应式的。

在实例内部，使用 `data` 和 `methods` 中的属性与方法都可以直接使用 `this` 进行调用。

另外，data 除了直接返回对象外，还可以返回一个返回对象的方法：
```javascript
new Vue({
  data () {
    return {
      text: 'Hello'
    }
  }
})
```

<a name="c8ba44c9"></a>
### data 的两种写法

1. 在简单的Vue实例中，没什么区别，因为你app对象不会被复用。
```javascript
var app = new Vue({...})
```

2. 但是在组件中，因为可能在多处调用同一组件，所以为了不让多处的组件共享同一data对象，只能返回函数。
```javascript
export default{
  data () {
    return {
      ...
    }
  }
}
```

<a name="76ed858a"></a>
## 三、内置实例属性
除了数据属性，Vue 实例还暴露了一些有用的实例属性与方法。它们都有前缀 `$`，以便与用户定义的属性区分开来。

比如：
```javascript
import Vue from 'vue'

let template = `<h1>{{text}}</h1>`

let vm = new Vue({
  el: '#app',
  template,
  data: {
    text: 'Hello'
  },
  created () {
    console.log(this.$data)
  }
})

console.log(vm.$data)
console.log(vm.$el)
```

可以看出，`$data` 和 `$el` 分别获取了实例属性中的 `data` 和 `el`。

控制台先后打印出：<br />![023.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607589721453-cf3ee132-21c8-4d99-861b-c5a6daec54d9.png#align=left&display=inline&height=325&originHeight=325&originWidth=706&size=8355&status=done&style=none&width=706)

<a name="5c678822"></a>
## 四、计算属性（computed）
虽然模板中允许使用任何JS表达式，但是对于一些复杂的运算不建议直接在模板中书写，否则项目扩展后很有可能造成维护困难。

比如一个糟糕的例子：
```html
<div id="example">
  {{ message.split('').reverse().join('') }}
</div>
```

更好的解决方案是使用 Vue 的计算属性：
```html
<div id="example">
  <p>Original message: "{{ message }}"</p>
  <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>
```

```javascript
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
})
```

Vue 知道 vm.reversedMessage 依赖于 vm.message，因此当 vm.message 发生改变时，所有依赖 vm.reversedMessage 的绑定也会更新。而且最妙的是我们已经以声明的方式创建了这种依赖关系：计算属性的 getter 函数是没有副作用 (side effect) 的，这使它更易于测试和理解。

计算属性在定义的时候是一个 function，可以像绑定普通属性一样在模板中绑定计算属性。

<a name="2ee134cb"></a>
### getter 和 setter
计算属性默认只有 getter ，不过在需要时你也可以提供一个 setter。
```javascript
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
// ...
```

现在再运行 `vm.fullName = 'John Doe'` 时，setter 会被调用，`vm.firstName` 和 `vm.lastName` 也会相应地被更新。

<a name="71f5fea4"></a>
## 五、监听器（watch）
虽然计算属性在大多数情况下更合适，但有时也需要一个自定义的侦听器。这就是为什么 Vue 通过 watch 选项提供了一个更通用的方法，来响应数据的变化。当需要在数据变化时执行异步或开销较大的操作时，这个方式是最有用的。
```javascript
import Vue from 'vue'

let template = `
<div id="watch-example">
  <p>
    Ask a yes/no question:
    <input v-model="question">
  </p>
  <p>{{ answer }}</p>
</div>
`

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template,
  data: {
    question: '',
    answer: 'I cannot give you an answer until you ask a question!'
  },
  watch: {
    // 如果 `question` 发生改变，这个函数就会运行
    question: function (newQuestion, oldQuestion) {
      this.answer = 'Waiting for you to stop typing...'
      setTimeout(() => {
        this.getAnswer()
      }, 500)
    }
  },
  methods: {
    getAnswer () {
      if (this.question.indexOf('?') === -1) {
        this.answer = 'Questions usually contain a question mark (?).'
        return
      }
      this.answer = 'Question over!'
    }
  }
})
```

运行效果：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607589975702-78dda363-f28b-4860-9d08-b311ff4b621c.gif#align=left&display=inline&height=101&originHeight=101&originWidth=506&size=20235&status=done&style=none&width=506)

:::info
不能使用箭头函数定义 watcher（回调）函数，因为箭头函数绑定了父级作用域的上下文，所以里面的 this 将不会按照期望指向 Vue 实例
:::

<a name="24b6c93e"></a>
### watcher 的三种写法
<a name="9c283c96"></a>
#### 方法写法
这是最常见的一种写法, 接收两个参数: newValue, oldValue, 适用于普通变量 (简单类型的值的观测写法)
```javascript
let vm = new Vue({
  data: {
    a: 1
  },
  watch: {
    a: function (val, oldVal) {
      console.log('new: %s, old: %s', val, oldVal)
    }
  }
})

vm.a = 2 // -> new: 2, old: 1
```

如果要检测的变量层级比较深, 可以使用字符串形式:
```javascript
let vm = new Vue({
  data: {
    a: {
      b: 1
    }
  },
  watch: {
    'a.b': function (val, oldVal) {
      console.log('new: %s, old: %s', val, oldVal)
    }
  }
})
```

<a name="8b306e21"></a>
#### 对象写法
可以进行深度观测 (能观测对象c下多重属性变化), 适用于复杂类型的值的观测写法, 当c变化后会回调handler函数
```javascript
var vm = new Vue({
  data: {
    a: {
      b: 1
    }
  },
  watch: {
    a: {
      handler: function (val, oldVal) {
        console.log('new: %s, old: %s', val, oldVal)
      },
      deep: true
    }
  }
})
vm.a.b = 2 // -> new: 2, old: 1
```

<a name="febdd4d4"></a>
#### 方法名
可以在 watch 中指定一个方法名, 方法在 methods 中进行定义 (此种方式不常见)
```javascript
var vm = new Vue({
  data: {
    a: 1
  },
  methods: {
    watchA (val, oldVal) {
      console.log('new: %s, old: %s', val, oldVal)
    }
  },
  watch: {
    a: 'watchA'
  }
})

vm.a = 2 // -> new: 2, old: 1
```

<a name="4e06b456"></a>
### $watch
除了作为属性选项外，还可使用实例方法的形式创建。

:::info
观察 Vue 实例变化的一个表达式或计算属性函数。回调函数得到的参数为新值和旧值。表达式只接受监督的键路径。对于更复杂的表达式，用一个函数取代。
:::

:::warning
在变异 (不是替换) 对象或数组时，旧值将与新值相同，因为它们的引用指向同一个对象/数组。Vue 不会保留变异之前值的副本。
:::

```javascript
vm.$watch(expOrFn, callback, [options])
```

参数：

- expOrFn 
- callback 
- options 
   - deep 
   - immediate 

返回值： unwatch 

上面的例子可以改写成：
```javascript
import Vue from 'vue'

let template = `
<div id="watch-example">
  <p>
    Ask a yes/no question:
    <input v-model="question">
  </p>
  <p>{{ answer }}</p>
</div>
`

/* eslint-disable no-new */
let vm = new Vue({
  el: '#app',
  template,
  data: {
    question: '',
    answer: 'I cannot give you an answer until you ask a question!'
  },
  methods: {
    getAnswer: function () {
      if (this.question.indexOf('?') === -1) {
        this.answer = 'Questions usually contain a question mark (?).'
        return
      }
      this.answer = 'Question over!'
    }
  }
})

vm.$watch('question', (newQuestion, oldQuestion) => {
  vm.answer = 'Waiting for you to stop typing...'
  setTimeout(() => {
    vm.getAnswer()
  }, 500)
})
```

vm.$watch 返回一个取消观察函数，用来停止触发回调：

```javascript
var unwatch = vm.$watch('a', cb)
// 之后取消观察
unwatch()
```

<a name="FKMDx"></a>
#### 选项：deep
为了发现对象内部值的变化，可以在选项参数中指定 `deep: true` 。注意监听数组的变动不需要这么做。

```javascript
vm.$watch('someObject', callback, {
  deep: true
})
vm.someObject.nestedValue = 123
// callback is fired
```

<a name="dkIVT"></a>
#### 选项：immediate
在选项参数中指定 `immediate: true` 将立即以表达式的当前值触发回调：

```javascript
vm.$watch('a', callback, {
  immediate: true
})
// 立即以 `a` 的当前值触发回调
```

<a name="4C3Wu"></a>
## 六、生命周期
首先看一张官方的生命周期图：<br />![lifecycle.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607590268081-aa0d75e7-c447-4626-adef-8ad6d78d243d.png#align=left&display=inline&height=3039&originHeight=3039&originWidth=1200&size=55420&status=done&style=none&width=1200)

<a name="sSSIc"></a>
### 生命周期历程
从图中可以看到，整个 Vue 实例/组件的生命周期大致分为以下几个阶段

- **init** 初始化阶段
- **mount** 挂载阶段
- **update** 更新阶段
- **destroy** 销毁阶段

在每个阶段都会有对应的一些生命周期钩子。

<a name="1ogjA"></a>
### 生命周期钩子
生命周期钩子，又称生命周期函数，比较重要的有:

<a name="beforeCreate"></a>
#### beforeCreate
在实例初始化之后，数据观测 (data observer) 和 event/watcher 事件配置之前被调用。

<a name="SzSyc"></a>
#### created
在实例创建完成后被立即调用。在这一步，实例已完成以下的配置：数据观测 (data observer)，属性和方法的运算，watch/event 事件回调。然而，挂载阶段还没开始，$el 属性目前不可见。

<a name="Mmxpy"></a>
#### beforeMount
在挂载开始之前被调用：相关的 render 函数首次被调用。

注意: 该钩子在服务器端渲染期间不被调用。

<a name="Ds8Rf"></a>
#### mounted
el 被新创建的 vm.$el 替换，并挂载到实例上去之后调用该钩子。如果 root 实例挂载了一个文档内元素，当 mounted 被调用时 vm.$el 也在文档内。

注意: mounted 不会承诺所有的子组件也都一起被挂载。如果你希望等到整个视图都渲染完毕，可以用 `vm.$nextTick` 替换掉 mounted：
```javascript
mounted: function () {
  this.$nextTick(function () {
    // Code that will run only after the entire view has been rendered
  })
}
```

注意: 该钩子在服务器端渲染期间不被调用。

<a name="beforeUpdate"></a>
#### beforeUpdate
数据更新时调用，发生在虚拟 DOM 重新渲染和打补丁之前。

你可以在这个钩子中进一步地更改状态，这不会触发附加的重渲染过程。

注意: 该钩子在服务器端渲染期间不被调用。

<a name="Ibwsc"></a>
#### updated
由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。

当这个钩子被调用时，组件 DOM 已经更新，所以你现在可以执行依赖于 DOM 的操作。然而在大多数情况下，你应该避免在此期间更改状态。如果要相应状态改变，通常最好使用计算属性或 watcher 取而代之。

注意: updated 不会承诺所有的子组件也都一起被重绘。如果你希望等到整个视图都重绘完毕，可以用 vm.$nextTick 替换掉 updated：

```javascript
updated: function () {
  this.$nextTick(function () {
    // Code that will run only after the
    // entire view has been re-rendered
  })
}
```

注意: 该钩子在服务器端渲染期间不被调用。

<a name="WVHLr"></a>
#### beforeDestroy
实例销毁之前调用。在这一步，实例仍然完全可用。

注意: 该钩子在服务器端渲染期间不被调用。

<a name="yTBq7"></a>
#### destroyed
Vue 实例销毁后调用。调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。

注意: 该钩子在服务器端渲染期间不被调用。

