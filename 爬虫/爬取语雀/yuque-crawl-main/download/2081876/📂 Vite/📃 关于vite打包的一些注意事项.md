<a name="ry6nw"></a>
## 路径级打包
如果打包后需要在某个路径下运行，比如 `http://localhost/demo`下访问，需要进行以下配置。

1. 修改vite配置`vite.config.js`
```javascript
import { defineConfig } from 'vite'
import path from "path";
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/demo/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets'
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  plugins: [vue()]
})

```

2. 修改路由配置

如果是history模式，在`createWebHistory`里面传入需要访问的路径：
```javascript
import { createRouter, createWebHistory } from "vue-router";

...

const router = createRouter({
  history: createWebHistory('/demo/'),
  routes,
});


```
如果是hash模式：
```javascript
import { createRouter, createWebHashHistory } from 'vue-router'

...

const router = createRouter({
  history: createWebHashHistory('/demo/'),
  routes
})
```
参考：

- [createwebhistory](https://next.router.vuejs.org/zh/api/#createwebhistory)
- [createwebhashhistory](https://next.router.vuejs.org/zh/api/#createwebhashhistory)

3. nginx配置

比如vite打包后的路径为`D:/Projects/_test/websites/demo`
```javascript
server {
    listen       8001;
    access_log  logs/dist.access.log;
    error_log  logs/dist.error.log;

    server_name   localhost;

    location / {
        root D:/Projects/_test/websites;
        index  index.html index.htm;
        autoindex on;
    }

    location ^~/demo {
        alias D:/Projects/_test/websites/demo;
        index  index.html index.htm;
        autoindex on;
    }
}
```




