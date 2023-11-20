官方文档：[https://vitejs.dev/config/](https://vitejs.dev/config/)

<a name="KrdRV"></a>
## 一、配置文件
vite配置文件命名为 `vite.config.js` 。

Vite1的配置文件结构如下：
```javascript
const path = require('path')

module.exports = {
  alias: {
    '/@/': path.resolve(__dirname, './src')
  },
  proxy: {
    proxy: {
      '/api': 'https://api.test.com'
    },
  },
}
```

Vite2的配置文件结构如下：
```javascript
import vue from '@vitejs/plugin-vue'

const resolve = dir => require('path').join(__dirname, dir);

/**
 * @type {import('vite').UserConfig}
 */
export default {
  plugins: [vue()],
  alias: {
    '@': resolve('src'),
    'pages': resolve('./src/pages'),
    'stores': resolve('./src/stores'),
    'routes': resolve('./src/routes'),
    'components': resolve('./src/components'),
    'library': resolve('./src/library'),
    'api': resolve('./src/api'),
  }
}
```

如果不是默认名称 `vite.config.js` ，可以使用 `--config` 指定，比如：<br />
```javascript
vite --config my-config.js
```

<a name="To7Dq"></a>
## 二、路径别名
`alias` 用于制定路径别名（Vite1）：
```javascript
const path = require('path')

module.exports = {
  alias: {
    '/@/': path.resolve(__dirname, './src')
  }
}
```
在Vue中：
```html
<script setup>
import api from '/@/api'
</script>
```

至于在Vite1中为什么要写成 `/@/` ，我也不清楚，反正如果不加 `/` 是会报错的，估计是Vite1个一个小bug。

到了Vite2就成功解决了这个问题：
```javascript
import vue from '@vitejs/plugin-vue'

const resolve = dir => require('path').join(__dirname, dir);

/**
 * @type {import('vite').UserConfig}
 */
export default {
  plugins: [vue()],
  alias: {
    '@': resolve('src'),
    'pages': resolve('./src/pages'),
    'stores': resolve('./src/stores'),
    'routes': resolve('./src/routes'),
    'components': resolve('./src/components'),
    'library': resolve('./src/library'),
    'api': resolve('./src/api'),
  }
}
```
引用：
```vue
<script setup>
import navbar from 'components/navbar.vue'
import tabbar from 'components/tabbar.vue'
</script>
```

在模板中，还是无法使用别名，建议将静态资源放于 `public` 中，引入的时候使用根路径：
```vue
<template lang='pug'>
img(src="/logo.jpg")
</template>
```
使用 `/logo.jpg` 与 `/public/logo.jpg` 效果一致，但最好使用前者，因为vite编译后会将 `public` 中的文件全部释放到根目录，即使使用后者也会被映射到前者路径。

<a name="CGZPO"></a>
## 三、代理服务器
`server.proxy` 为开发服务器配置自定义代理规则。
```javascript
module.exports = {
  server: {
    proxy: {
      '/api': 'https://api.test.com'
    },
  },
}
```

