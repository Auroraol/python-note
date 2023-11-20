<a name="rWauO"></a>
## 插槽传值

<a name="frAjD"></a>
## 小程序：循环的插槽中不允许访问页面数据
什么意思呢，比如有一个页面A，引入了一个组件B，B中有一个循环出来的插槽，A中使用组件B，在A中定义的数据是无法直接在插槽中使用的。

举例：<br />组件`inner.vue`：
```vue
<template lang="pug">
view
  view 外面的
  view(v-for="(item, index) in list" :key="index")
    slot(v-bind:item="item")
</template>

<script>
export default {
  name: 'inner',
  props: {
    list: {
      type: Array,
      default() {
        return []
      }
    }
  }
}
</script>
```

页面中引入此组件：
```vue
<template lang="pug">
view
  view {{obj.name}}
  inner(:list="list" v-slot='{ item }')
    view {{obj.name}}
    view {{item}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      obj: {
        name: 'hello'
      },
      list: [1,2,3,4,5]
    }
  },
}
</script>
```

在H5中渲染正常：<br />![Snipaste_2021-06-01_15-53-15.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1622534024396-e714a193-59f4-4434-b9c0-c3e0ffbb71ae.png#clientId=u7621f2f6-ec23-4&from=drop&id=OUWR1&originHeight=324&originWidth=402&originalType=binary&size=2423&status=done&style=none&taskId=uf787277c-aaa9-48b4-97cc-7f01a4cee39)

在小程序中：<br />![Snipaste_2021-06-01_15-53-59.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1622534048463-1fff256f-216f-40ac-baab-33ed7006b988.png#clientId=u7621f2f6-ec23-4&from=drop&id=YIvES&originHeight=281&originWidth=411&originalType=binary&size=2787&status=done&style=none&taskId=uab126463-7908-4630-9865-df7cdaae4f4)

可以看出，在小程序中，放到循环插槽中，是不能获取到父页面中的值的。

对此，只能采取一个折中的解决方案：将需要的值传入子组件之中，再暴露给父页面。<br />具体修改如下：<br />组件`inner.vue`：
```vue
<template lang="pug">
view
  view 外面的
  view(v-for="(item, index) in list" :key="index")
    slot(v-bind:item="item" v-bind:data="extraData")
</template>

<script>
export default {
  name: 'inner',
  props: {
    list: {
      type: Array,
      default() {
        return []
      }
    },
    extraData: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>
```
用一个props（extraData）接收父页面传入的数据，再使用`v-bind`将其暴露。

页面中：
```vue
<template lang="pug">
view
  view {{obj.name}}
  inner(:list="list" :extraData="obj" v-slot='{ item, data }')
    view {{data.name}}
    view {{item}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      obj: {
        name: 'hello'
      },
      list: [1,2,3,4,5]
    }
  },
}
</script>
```
通过 `v-slot`将其解构，获取数据。

在小程序中：<br />![Snipaste_2021-06-01_16-03-52.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1622534643946-1bed7e87-e0e0-400b-a748-9447ba9b3fd6.png#clientId=u7621f2f6-ec23-4&from=drop&id=XIxbd&originHeight=376&originWidth=402&originalType=binary&size=3129&status=done&style=none&taskId=u6027d0dc-7a30-4b37-aed5-3e885d1f4c1)

写法有点挫，但没办法，只能这样搞定。

一个包含计算属性的示例：
```vue
<template lang="pug">
Layout(:type='2', title='测试', :showFooter='false')
  view {{computedName}}
  inner(:list="list" :extraData="computedName" v-slot='{ item, data }')
    view {{data}}
    view {{item}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      obj: {
        name: 'hello'
      },
      list: [1,2,3,4,5]
    }
  },
  computed: {
    computedName() {
      return this.obj.name + ' world'
    }
  }
}
</script>
```

如果计算属性是vuex的值，最好是直接放到组件中。<br />举例：<br />组件`inner.vue`：
```vue
<template lang="pug">
view
  view 外面的
  view(v-for="(item, index) in list" :key="index")
    slot(v-bind:item="item" v-bind:data="skin")
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'inner',
  props: {
    list: {
      type: Array,
      default() {
        return []
      }
    },
  },
  computed: {
    ...mapGetters({
      skin: 'skin'
    })
  },
}
</script>
```
页面中引入：
```vue
<template lang="pug">
view
  view {{obj.name}}
  inner(:list="list" v-slot='{ item, data }')
    view(:class="data.tc1") {{item}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      obj: {
        name: 'hello'
      },
      list: [1,2,3,4,5]
    }
  },
}
</script>
```

之前试过将vuex的计算属性传入，但是会得到不可预期的效果，不知道原因。


<a name="XPHOI"></a>
## 小程序：循环的插槽中不允许使用过滤器
这点比较头疼，小程序不支持在循环插槽中Vue中的过滤器语法。

比如有如下过滤器：
```javascript
Vue.filter('date', (value, len = 10) => {
  if (!value) return ''
  value = value.slice(0, len)
  return value
})
```

组件还是同上面 [小程序：循环的插槽中不允许数据穿透](#frAjD) 的一样。

在页面中调用：
```vue
<template lang="pug">
view
  view {{'2021-01-01 12:00:00' | date}}
  inner(:list="list" v-slot='{ item }')
    view {{'2021-01-01 12:00:00' | date}}
</template>
```

小程序端编译出来仍然是无效的。

浏览器：<br />![Snipaste_2021-06-01_16-51-25.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1622537493722-598b3319-ce33-4f37-9392-8a302cbb9bdf.png#clientId=u2ad8f224-13bd-4&from=drop&id=Sl3Yj&originHeight=233&originWidth=391&originalType=binary&size=1803&status=done&style=none&taskId=u89bf26df-cbf9-440b-beb8-56d95e2eb1b)

小程序：<br />![Snipaste_2021-06-01_16-51-55.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1622537529553-f88fedfe-2dde-4ce3-82bf-a6dae0aea510.png#clientId=u2ad8f224-13bd-4&from=drop&id=u67c9a9bd&originHeight=175&originWidth=403&originalType=binary&size=2538&status=done&style=none&taskId=uc06a2d1a-ef8a-4f8e-ad82-78acedec632)

<a name="lXGBL"></a>
## 小程序：循环的插槽中不允许使用页面方法
其实看懂了上面两点，这一点也是一样的。说白了，其实就是：
```vue
在小程序中，循环插槽不允许使用页面中的方法、过滤器、数据。
```

示例：
```vue
<template lang="pug">
view
  view {{parseTime('2021-01-01 12:00:00')}}
  inner(:list="list" v-slot='{ item }')
    view {{parseTime('2021-01-01 12:00:00')}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      list: [1,2,3,4,5]
    }
  },
  methods: {
    parseTime(time) {
      return time.slice(0, 10)
    }
  }
}
</script>
```

或者使用计算属性：
```vue
<template lang="pug">
view
  view {{parseTime('2021-01-01 12:00:00')}}
  inner(:list="list" v-slot='{ item }')
    view {{parseTime('2021-01-01 12:00:00')}}
</template>

<script>
import inner from './inner.vue'
export default {
  components: { inner },
  data() {
    return {
      list: [1,2,3,4,5]
    }
  },
  computed: {
    parseTime() {
      return time => time.slice(0, 10)
    }
  },
}
</script>
```

可以看到，在H5端正常，小程序端仍然是不能渲染。

解决方案：暂未找到什么好的解决方案。

针对这个问题，我向uniapp提了一个issue：[小程序：循环的插槽中不允许访问页面数据](https://ask.dcloud.net.cn/question/124279)


