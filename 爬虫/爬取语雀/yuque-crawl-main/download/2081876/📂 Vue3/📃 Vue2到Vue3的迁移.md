<a name="VcLAr"></a>
## 一、兼容性迁移：使用`@vue/compat`
<a name="UcpkP"></a>
### 添加`@vue/compat`依赖包
如果想在Vue3项目中兼容Vue2的某些特性，可以使用`@vue/compat`这个包。

首先找到`package.json`中找到vue的版本号，比如：
```html
"vue": "^3.2.16"
```
然后安装相同版本的`@vue/compat`：
```html
yarn add @vue/compat@3.2.16
```

如果是从vue2升级到vue3的，还需要将`vue-template-compiler`替换为`@vue/compiler-sfc`：
```javascript
"dependencies": {
-  "vue": "^2.6.12",
+  "vue": "^3.1.0",
+  "@vue/compat": "^3.1.0"
   ...
},
"devDependencies": {
-  "vue-template-compiler": "^2.6.12"
+  "@vue/compiler-sfc": "^3.1.0"
}
```


<a name="nX12S"></a>
### 通过构建工具配置文件修改兼容性配置
在构建设置中，为vue设置别名为`@vue/compat`，且通过 Vue 编译器选项开启兼容模式。

Vite项目中，`vite.config.js`：
```javascript
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default {
  resolve: {
    alias: {
      vue: '@vue/compat'
    }
  },
  plugins: [
    vue({
      template: {
        compilerOptions: {
          compatConfig: {
            MODE: 2
          }
        }
      }
    })
  ]
}
```

vue-cli项目中，修改`vue.config.js`：
```javascript
// https://cli.vuejs.org/zh/
module.exports = {
  chainWebpack: config => {
    config.resolve.alias.set('vue', '@vue/compat')

    config.module
      .rule('vue')
      .use('vue-loader')
      .tap(options => {
        return {
          ...options,
          compilerOptions: {
            compatConfig: {
              MODE: 2
            }
          }
        }
      })
  }
}
```

webpack项目中，修改`webpack.config.js`
```javascript
module.exports = {
  resolve: {
    alias: {
      vue: '@vue/compat'
    }
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          compilerOptions: {
            compatConfig: {
              MODE: 2
            }
          }
        }
      }
    ]
  }
}
```

<a name="Hfbwv"></a>
### 在项目中修改兼容性配置
也可以在Vue项目中设置，而不是在构建工具配置文件修改配置。

在 `main.js`中：
```javascript
import { configureCompat } from 'vue'

// 所有 Vue 3 的默认行为，并开启某些兼容性特性
configureCompat({
  MODE: 3,
  COMPILER_FILTERS: true,
  FILTERS: true
})
```
在组件中：
```vue

<template>
	<div>{{ num | price }}</div>
</template>

<script>
export default {
  setup() {
    return {
      num: 123
    }
  },
  compatConfig: {
    MODE: 3,
    COMPILER_FILTERS: true,
    FILTERS: true
  },
  filters: {
    price(value) {
      return '$' + value
    }
  },
}
</script>
```

以 `COMPILER_` 开头的特性是针对编译器的。<br />如果报以下警告，说明当前配置无效，必须在构建工具配置文件中配置，或使用完整构建版本 (含浏览器内编译器)
```javascript
Deprecation config "COMPILER_FILTERS" is compiler-specific and you are running a runtime-only build of Vue. This deprecation should be configured via compiler options in your build setup instead.
```

<a name="b5kHm"></a>
## 二、Vue3已移除或非兼容的特性
<a name="gLGHE"></a>
### 过滤器
在 3.x 中，过滤器已移除，且不再支持。官方建议用方法调用或计算属性来替换它们。

相关迁移构建开关：

- `FILTERS`
- `COMPILER_FILTERS`

Vue2的使用：
```vue
<template>
  <p>{{ accountBalance | currencyUSD }}</p>
</template>

<script>
  export default {
    data() {
      return {
        accountBalance: 100
      }
    },
    filters: {
      currencyUSD(value) {
        return '$' + value
      }
    }
  }
</script>
```

Vue3中，使用计算属性：
```vue
<template>
  <p>{{ accountInUSD }}</p>
</template>

<script>
  export default {
    data() {
      return {
        accountBalance: 100
      }
    },
    computed: {
      accountInUSD() {
        return '$' + this.accountBalance
      }
    }
  }
</script>
```

如果是全局过滤器，可以定义全局过滤器方法，挂载到vue的全局属性中：
```javascript
// main.js
const app = createApp(App)

app.config.globalProperties.$filters = {
  currencyUSD(value) {
    return '$' + value
  }
}
```
模板中使用：
```vue
<template>
  <h1>Bank Account Balance</h1>
  <p>{{ $filters.currencyUSD(accountBalance) }}</p>
</template>
```
这种方式只适用于方法，而不适用于计算属性，因为后者只有在单个组件的上下文中定义时才有意义。

参考：

- [过滤器](https://v3.cn.vuejs.org/guide/migration/filters.html)

<a name="xLKq3"></a>
### 事件总线
`$on`，`$off` 和 `$once` 实例方法已被移除，组件实例不再实现事件触发接口。`$emit` 仍然包含于现有的 API 中，因为它用于触发由父组件声明式添加的事件处理函数。

相关迁移构建开关：`INSTANCE_EVENT_EMITTER`

[📃 事件总线](https://www.yuque.com/xiaoyulive/vue/vh4z56?view=doc_embed)

参考：

- [事件 API](https://v3.cn.vuejs.org/guide/migration/events-api.html)
- [GitHub：mitt](https://github.com/developit/mitt)
- [GitHub：tiny-emitter](https://github.com/scottcorgan/tiny-emitter)

<a name="ECJZa"></a>
### 插槽
相关迁移构建开关：

- `INSTANCE_SCOPED_SLOTS`

[📃 Vue3组件相关新特性及变动](https://www.yuque.com/xiaoyulive/vue/dbehxt?view=doc_embed&inner=48305)<br />参考：

- [插槽统一](https://v3.cn.vuejs.org/guide/migration/slots-unification.html)

<a name="njbP1"></a>
### 自定义指令

参考：

- [自定义指令](https://v3.cn.vuejs.org/guide/migration/custom-directives.html)

<a name="kPOep"></a>
### 循环中的ref
相关迁移构建开关：

- `V_FOR_REF`
- `COMPILER_V_FOR_REF`

[📃 Vue3组件相关新特性及变动](https://www.yuque.com/xiaoyulive/vue/dbehxt?view=doc_embed&inner=fFwQd)<br />参考：

- [v-for 中的 Ref 数组](https://v3.cn.vuejs.org/guide/migration/array-refs.html)

<a name="xjOc0"></a>
### $attr中包含class和style


<a name="VZTQD"></a>
### 组件数据双向绑定
Vue2语法：使用`.sync`修饰符
```vue
<ChildComponent :title.sync="pageTitle" />
```
Vue3语法：使用`v-model`
```vue
<ChildComponent v-model:title="pageTitle" />
```







<a name="rTZec"></a>
## 参考资料

- [GitHub：vue-compat](https://github.com/vuejs/vue-next/tree/master/packages/vue-compat)
- [用于迁移的构建版本](https://v3.cn.vuejs.org/guide/migration/migration-build.html)



