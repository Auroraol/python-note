本文搭建项目使用的环境：
```javascript
❯ node -v
v16.13.1

❯ npm -v
8.1.2

❯ yarn -v
1.15.2


❯ yarn config list
yarn config v1.15.2
info yarn config
{
  'version-tag-prefix': 'v',
  'version-git-tag': true,
  'version-commit-hooks': true,
  'version-git-sign': false,
  'version-git-message': 'v%s',
  'init-version': '1.0.0',
  'init-license': 'MIT',
  'save-prefix': '^',
  'bin-links': true,
  'ignore-scripts': false,
  'ignore-optional': false,
  registry: 'https://registry.yarnpkg.com',
  'strict-ssl': true,
  'user-agent': 'yarn/1.15.2 npm/? node/v16.13.1 win32 x64',
  email: '731734107@qq.com',
  lastUpdateCheck: 1641975096604,
  username: 'quanzaiyu'
}
info npm config
{
  registry: 'http://registry.npm.taobao.org',
  disturl: 'https://npm.taobao.org/dist',
  'chromedriver-cdnurl': 'https://npm.taobao.org/mirrors/chromedriver',
  'couchbase-binary-host-mirror': 'https://npm.taobao.org/mirrors/couchbase/v{version}',
  'debug-binary-host-mirror': 'https://npm.taobao.org/mirrors/node-inspector',
  'electron-mirror': 'https://npm.taobao.org/mirrors/electron/',
  'flow-bin-binary-host-mirror': 'https://npm.taobao.org/mirrors/flow/v',
  'fse-binary-host-mirror': 'https://npm.taobao.org/mirrors/fsevents',
  'fuse-bindings-binary-host-mirror': 'https://npm.taobao.org/mirrors/fuse-bindings/v{version}',
  'git4win-mirror': 'https://npm.taobao.org/mirrors/git-for-windows',
  'gl-binary-host-mirror': 'https://npm.taobao.org/mirrors/gl/v{version}',
  'grpc-node-binary-host-mirror': 'https://npm.taobao.org/mirrors',
  'hackrf-binary-host-mirror': 'https://npm.taobao.org/mirrors/hackrf/v{version}',
  'python-mirror': 'https://npm.taobao.org/mirrors/python',
  'rabin-binary-host-mirror': 'https://npm.taobao.org/mirrors/rabin/v{version}',
  'sass-binary-site': 'https://npm.taobao.org/mirrors/node-sass',
  'sodium-prebuilt-binary-host-mirror': 'https://npm.taobao.org/mirrors/sodium-prebuilt/v{version}',
  'sqlite3-binary-site': 'https://npm.taobao.org/mirrors/sqlite3',
  'utf-8-validate-binary-host-mirror': 'https://npm.taobao.org/mirrors/utf-8-validate/v{version}',
  'utp-native-binary-host-mirror': 'https://npm.taobao.org/mirrors/utp-native/v{version}',
  'zmq-prebuilt-binary-host-mirror': 'https://npm.taobao.org/mirrors/zmq-prebuilt/v{version}'
}Done in 0.08s.

❯ npm config list
; "user" config from C:\Users\quanz\.npmrc
chromedriver-cdnurl = "https://npm.taobao.org/mirrors/chromedriver" couchbase-binary-host-mirror = "https://npm.taobao.org/mirrors/couchbase/v{version}" debug-binary-host-mirror = "https://npm.taobao.org/mirrors/node-inspector" disturl = "https://npm.taobao.org/dist" 
electron-mirror = "https://npm.taobao.org/mirrors/electron/" 
flow-bin-binary-host-mirror = "https://npm.taobao.org/mirrors/flow/v" 
fse-binary-host-mirror = "https://npm.taobao.org/mirrors/fsevents" 
fuse-bindings-binary-host-mirror = "https://npm.taobao.org/mirrors/fuse-bindings/v{version}" 
git4win-mirror = "https://npm.taobao.org/mirrors/git-for-windows" 
gl-binary-host-mirror = "https://npm.taobao.org/mirrors/gl/v{version}"
grpc-node-binary-host-mirror = "https://npm.taobao.org/mirrors"
hackrf-binary-host-mirror = "https://npm.taobao.org/mirrors/hackrf/v{version}"
leveldown-binary-host-mirror = "https://npm.taobao.org/mirrors/leveldown/v{version}"
leveldown-hyper-binary-host-mirror = "https://npm.taobao.org/mirrors/leveldown-hyper/v{version}"
mknod-binary-host-mirror = "https://npm.taobao.org/mirrors/mknod/v{version}"
node-sqlite3-binary-host-mirror = "https://npm.taobao.org/mirrors"
node-tk5-binary-host-mirror = "https://npm.taobao.org/mirrors/node-tk5/v{version}"
nodegit-binary-host-mirror = "https://npm.taobao.org/mirrors/nodegit/v{version}/"
operadriver-cdnurl = "https://npm.taobao.org/mirrors/operadriver"
phantomjs-cdnurl = "https://npm.taobao.org/mirrors/phantomjs"
profiler-binary-host-mirror = "https://npm.taobao.org/mirrors/node-inspector/"
puppeteer-download-host = "https://npm.taobao.org/mirrors"

python-mirror = "https://npm.taobao.org/mirrors/python"   
rabin-binary-host-mirror = "https://npm.taobao.org/mirrors/rabin/v{version}"
registry = "http://registry.npm.taobao.org/"
sass-binary-site = "https://npm.taobao.org/mirrors/node-sass"
sodium-prebuilt-binary-host-mirror = "https://npm.taobao.org/mirrors/sodium-prebuilt/v{version}"
sqlite3-binary-site = "https://npm.taobao.org/mirrors/sqlite3"
utf-8-validate-binary-host-mirror = "https://npm.taobao.org/mirrors/utf-8-validate/v{version}"
utp-native-binary-host-mirror = "https://npm.taobao.org/mirrors/utp-native/v{version}"
zmq-prebuilt-binary-host-mirror = "https://npm.taobao.org/mirrors/zmq-prebuilt/v{version}"

; node bin location = C:\Program Files\nodejs\node.exe    
; cwd = D:\Projects\_test\_NestjsProjects\nest-project    
; HOME = C:\Users\quanz
; Run `npm config ls -l` to show all defaults.
```

<a name="v6zf3"></a>
## 一、通过vite搭建项目

- [vite官网](https://cn.vitejs.dev/)【[Docs：GitHub](https://github.com/vitejs/docs-cn)】【[vite：GitHub](https://github.com/vitejs/vite)】

创建项目：
```javascript
$ yarn create vite
yarn create v1.15.2
[1/4] Resolving packages...
[2/4] Fetching packages...
info fsevents@1.2.13: The platform "win32" is incompatible with this module.
info "fsevents@1.2.13" is an optional dependency and failed compatibility check. Excluding it from installation.
info fsevents@2.3.2: The platform "win32" is incompatible with this module.
info "fsevents@2.3.2" is an optional dependency and failed compatibility check. Excluding it from installation.
[3/4] Linking dependencies...
[4/4] Building fresh packages...

success Installed "create-vite@2.7.2" with binaries:
      - create-vite
      - cva
√ Project name: ... vite-vue3
√ Select a framework: » vue
√ Select a variant: » vue

Scaffolding project in D:\Projects\_test\_ViteProjects\vite-vue3...

Done. Now run:

  cd vite-vue3
  npm install
  npm run dev

Done in 22.24s.
```
或者通过以下命令可直接使用vue3模板进行项目创建：
```javascript
yarn create vite vite-vue3 --template vue
```
后续步骤也很清楚了，进入项目目录安装依赖：
```javascript
cd vite-vue3
yarn
yarn dev
```
默认项目会跑到本地3000端口，浏览器通过 [http://localhost:3000](http://localhost:3000/) 访问。

<a name="PvaJl"></a>
## 二、目录结构规划及项目基本配置
以下是我的项目目录结构规划，只列举一些比较重要的目录和文件：<br />![Snipaste_2022-01-13_10-46-09.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1642042071030-7b6f6edc-8830-40ad-9432-1a76417ff1fe.png#clientId=ueee78a94-9397-4&from=drop&id=u6bff57e3&originHeight=631&originWidth=240&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10719&status=done&style=none&taskId=u4d722174-ce04-41f4-b5f5-84b37375337&title=)<br />为了方便对比，我把项目刚创建完后的目录结构也粘了出来：<br />![Snipaste_2022-01-13_10-49-02.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1642042171583-a4561d98-a669-46c8-98f8-ee7bf80b5a02.png#clientId=ueee78a94-9397-4&from=drop&id=u5da8a7fa&originHeight=318&originWidth=184&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4864&status=done&style=none&taskId=uc872dd99-32e6-4a6d-8144-87760bfc752&title=)

项目创建之初的`package.json`如下：
```json
{
  "name": "vite-vue3",
  "version": "0.0.0",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.2.25"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^2.0.0",
    "vite": "^2.7.2"
  }
}
```
可以看到依赖很少，也只有三个可执行的命令。

初始的`vite.config.js`配置如下：
```json
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()]
})
```
为了后面使用路径方便，可以添加 `@`别名解析：
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { base } from './src/config'

export default defineConfig({
  base,
  plugins: [
    vue({
      reactivityTransform: true,
      refSugar: true
    })
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    }
  },
})
```

运行dev时，默认安装新依赖需要重启，如果想要实时安装依赖并生效，可以将dev修改为：
```json
{
  "scripts": {
    "dev": "vite --force",
  }
}
```
这是官方原话：
```json
Vite 会将预构建的依赖缓存到 node_modules/.vite。它根据几个源来决定是否需要重新运行预构建步骤:

package.json 中的 dependencies 列表
- 包管理器的 lockfile，例如 package-lock.json, yarn.lock，或者 pnpm-lock.yaml
- 可能在 vite.config.js 相关字段中配置过的
- 只有在上述其中一项发生更改时，才需要重新运行预构建。

如果出于某些原因，你想要强制 Vite 重新构建依赖，你可以用 --force 命令行选项启动开发服务器，或者手动删除 node_modules/.vite 目录。
```
参考：[vite官方文档：文件系统缓存](https://cn.vitejs.dev/guide/dep-pre-bundling.html#file-system-cache)

初始的`main.js`长这样：
```javascript
import { createApp } from 'vue'
import App from './App.vue'

let app = createApp(App)

app.mount('#app')

// 挂载到全局
window.app = app
```
我在这里稍微改造了一下，将vue的实例挂载到了window下，以方便后续在浏览器中的调试。

<a name="Ua1NJ"></a>
## 三、集成pug与stylus

- [Pug官网](https://pugjs.org/)【[npm](https://www.npmjs.com/package/pug)】【[GitHub](https://github.com/pugjs/pug)】
- [Stylus官网](https://www.stylus-lang.cn/)【[GitHub](https://github.com/stylus/stylus/)】

我是比较喜欢使用pug作为模板引擎的，喜欢stylus作为样式预处理器。

这没什么好说的，vite是开箱即用的，直接安装即可使用，都不需要额外配置：
```javascript
yarn add pug stylus -D
```
重新运行项目，测试是否生效：
```vue
<template lang="pug">
div 123
</template>

<script setup>
</script>

<style scoped lang='stylus'>
div
  color red
</style>
```

如果大家喜欢使用sass或less作为预编译器，也是可以的。

- [less官网](https://less.bootcss.com/)【[less：GitHub](https://github.com/less/less.js)】
- [sass中文网](https://www.sass.hk/)

vite是开箱即用的，只需要安装sass或less即可：
```vue
yarn add less sass -D
```
测试less：
```vue
<template lang="pug">
.a
  .b 123
</template>

<script setup>
</script>

<style scoped lang='less'>
.a {
  .b {
    color: red;
  }
}
</style>
```
测试scss：
```vue
<template lang="pug">
.a
  .b 123
</template>

<script setup>
</script>

<style scoped lang='scss'>
$color: red;
.a {
  .b {
    color: $color;
  }
}
</style>
```
测试sass：
```vue
<template lang="pug">
.a
  .b 123
</template>

<script setup>
</script>

<style scoped lang='sass'>
$color: red
.a
  .b
    color: $color
</style>
```

相关工具：

- [Sass、Less在线转换工具](https://www.sass.hk/css2sass/)

<a name="Lrn2g"></a>
## 四、集成tailwindcss

- [tailwindcss官网](https://tailwindcss.com/) 【[GitHub](https://github.com/tailwindlabs/tailwindcss)】

安装依赖：
```json
yarn add -D tailwindcss@latest postcss@latest autoprefixer@latest
```
生成配置文件：
```json
$ npx tailwindcss init -p
Created Tailwind CSS config file: tailwind.config.js
Created PostCSS config file: postcss.config.js
```
可以看到生成了以下两个文件：`tailwind.config.js`和 `postcss.config.js`，一个是tailwindcss的配置文件，一个是postcss的配置文件。


可以看到在 `postcss.config.js`中引入了 `tailwindcss`和 `autoprefixer`：
```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

修改`tailwind.config.js`的配置：
```javascript
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  media: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
```
其中 content 选项表名对哪些文件应用 tailwindcss 样式规则。<br />注意：

- purge在tailwindcss3.0中改为了content
- darkMode在tailwindcss3.0中改为了 'media' or 'class'

我们创建一个 `index.css`引入tailwindcss基础样式、组件和功能：
```javascript
/* ./src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```
在`main.js`中引入此文件：
```javascript
import './index.css'
```

在模板中验证：
```vue
<template lang="pug">
.bg-red-50.text-green-300 12345
</template>
```

参考：

- [Install Tailwind CSS with Vue 3 and Vite](https://tailwindcss.com/docs/guides/vite)
- [在 Vue 3 和 Vite 安装 Tailwind CSS](https://www.tailwindcss.cn/docs/guides/vue-3-vite)

<a name="uREck"></a>
## 五、集成各种代码验证修复工具
<a name="YO74t"></a>
### eslint
eslint配置可以根据自己的喜好进行配置，以下为我的配置方式。<br />引入依赖：
```vue
yarn add -D eslint eslint-plugin-vue
```
创建eslint配置文件 `.eslintrc.js`
```javascript
module.exports = {
  root: true,
  env: { node: true },
  extends: ['plugin:vue/essential', 'eslint:recommended'],
  parserOptions: {
    ecmaFeatures: {
      // 支持装饰器
      legacyDecorators: true
    }
  },
  globals: {
    dayjs: 'readonly'
  },
  rules: {
    indent: ['error', 2, { SwitchCase: 1, flatTernaryExpressions: false }],
    semi: [2, 'never'],
    quotes: [2, 'single'],
    eqeqeq: 1,
    curly: [2, 'multi-line'],
    'no-console': [1, { allow: ['info', 'warn', 'error'] }],
    'no-debugger': 1,
    'no-alert': 1,
    'padded-blocks': [2, 'never'],
    'key-spacing': 2,
    'keyword-spacing': 2,
    'eol-last': 2,
    // 'array-element-newline': [1, 'always'],
    'linebreak-style': [2, 'windows'],
    'array-callback-return': 2,
    'block-scoped-var': 2,
    'no-empty': 2,
    'no-empty-function': 2,
    'no-empty-pattern': 2,
    'no-var': 2,
    'no-void': 2,
    'no-eval': 2,
    'no-tabs': 2,
    'no-unused-vars': 1,
    'no-case-declarations': 0,
    'no-div-regex': 2,
    'no-multi-spaces': 2,
    'no-trailing-spaces': 2,
    'no-eq-null': 2,
    'no-unneeded-ternary': 2,
    'no-mixed-spaces-and-tabs': 2,
    'no-whitespace-before-property': 2,
    'no-multiple-empty-lines': [2, { max: 1 }],
    'nonblock-statement-body-position': 2,
    'dot-location': [2, 'property'],
    'dot-notation': [2, { allowKeywords: true }],
    'func-style': 0,
    'func-call-spacing': 2,
    'func-names': [2, 'never'],
    'function-paren-newline': 2,
    'line-comment-position': 0,
    'lines-around-comment': 0,
    'lines-between-class-members': 2,
    'space-infix-ops': 2,
    'space-unary-ops': 2,
    'spaced-comment': 2,
    'space-before-blocks': 2,
    'space-in-parens': [2, 'never'],
    'space-before-function-paren': [2, 'never'],
    'one-var': [2, 'never'],
    'one-var-declaration-per-line': 2,
    'multiline-comment-style': 0,
    'consistent-return': 0,
    'object-curly-spacing': [2, 'always'],
    'object-curly-newline': [0, { multiline: true, minProperties: 1 }],
    'array-bracket-spacing': [2, 'never'],
    'prefer-promise-reject-errors': 0,
    'implicit-arrow-linebreak': 2,
    'default-case': 0,
    'switch-colon-spacing': 2,
    'template-tag-spacing': 2,
    'vue/require-valid-default-prop': 0,
    'vue/no-multiple-template-root': 0,
    'vue/multi-word-component-names': 0,
    'vue/valid-template-root': 0,
    'comma-style': 2,
    'comma-dangle': [0, 'never'],
    'prefer-object-spread': 2,
    'quote-props': [2, 'as-needed'],
    'no-useless-computed-key': 2,
    'no-useless-constructor': 2,
    'object-shorthand': 2,
    'use-isnan': 0,
    'prefer-arrow-callback': 2
  }
}
```
在 `vite.config.js`配置中引入`vite-plugin-eslint`
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import eslintPlugin from 'vite-plugin-eslint'
...

export default defineConfig({
  ...,
  plugins: [
    vue({
      reactivityTransform: true,
      refSugar: true
    }),
    eslintPlugin()
  ],
})
```
如果有什么文件不想要通过eslint验证，可以将其加入 `.eslintignore`文件中。

经过上面的配置，在编辑器和编译时都会报eslint警告或错误。

可以在 `package.json`中添加命令：
```javascript
{
  "scripts": {
    ...
    "fix:eslint": "eslint --fix src --ext .js,.vue"
  },
  ...
}

```
这样，如果想要修复eslint问题时，只需要执行以下命令即可：
```javascript
yarn fix:eslint
```

<a name="tjKu4"></a>
### stylelint
引入依赖：
```javascript
yarn add -D stylelint stylelint-config-idiomatic-order stylelint-config-recommended stylelint-plugin-stylus
```
其中：

- `stylelint-plugin-stylus`用于支持stylus的验证
- `stylelint-config-idiomatic-order`用于验证样式属性排序
- `stylelint-config-recommended `推荐的配置

创建stylelint配置文件`.stylelintrc.js`
```javascript
module.exports = {
  extends: [
    'stylelint-config-recommended',
    'stylelint-config-idiomatic-order',
    'stylelint-plugin-stylus/standard'
  ],
  plugins: ['stylelint-order'],
  rules: {
    'stylus/selector-type-no-unknown': [
      true,
    ],
    'stylus/at-rule-no-unknown': [
      true,
      {
        ignoreAtRules: [
          'tailwind',
          'layer',
          'apply',
          'variants',
          'responsive',
          'screen'
        ]
      }
    ],
    'stylus/semicolon': ['never'],
    'stylus/number-leading-zero': ['never'],
    'unit-no-unknown': [true, { ignoreUnits: ['rpx'] }],
    'no-descending-specificity': null,
    'no-empty-source': null,
    'font-family-no-missing-generic-family-keyword': null,
    'no-empty-source': null
  }
}
```
如果有什么文件不想要通过stylelint验证，可以将其加入 `.stylelintignore`文件中。

在 `package.json`中添加两条命令，用于验证和修复样式问题：
```json
{
  "scripts": {
    "lint:style": "stylelint --custom-syntax stylelint-plugin-stylus/custom-syntax src/**/*.{vue,css,styl}",
    "fix:style": "stylelint --custom-syntax stylelint-plugin-stylus/custom-syntax src/**/*.{vue,css,styl} --fix"
  }
}
```

<a name="QbTbn"></a>
### prettier
引入依赖：
```javascript
yarn add -D prettier prettier-eslint prettier-eslint-cli
```
创建prettier配置文件`.prettierrc.json`
```javascript
{
  "printWidth": 120,
  "tabWidth": 2,
  "useTabs": false,
  "singleQuote": true,
  "semi": false,
  "trailingComma": "none",
  "bracketSpacing": true,
  "arrowParens": "avoid",
  "endOfLine": "crlf",
  "htmlWhitespaceSensitivity": "ignore"
}
```
如果有什么文件不想要通过prettier格式化，可以将其加入 `.prettierignore`文件中。

在 `package.json`中添加一条命令，用于Prettier格式化代码：
```json
{
  "scripts": {
    "fix:prettier": "prettier --write src"
  }
}
```

<a name="Z0ALR"></a>
### pug-lint
引入依赖：
```javascript
yarn add pug-lint pug-lint-config-clock pug-lint-vue -D
```
创建pug-lint配置文件`.pug-lintrc.js`
```javascript
module.exports = {
  extends: "clock",
  validateIndentation: 2,
  validateLineBreaks: "CRLF",
  disallowClassAttributeWithStaticValue: true,
}
```

<a name="LmJLq"></a>
## 六、集成代码提交验证工具（husky）
参考我的另一篇文章，有详细介绍：<br />[📃 Git提交信息规范化与自动化](https://www.yuque.com/xiaoyulive/services/qc4vey?view=doc_embed)

<a name="oUIRZ"></a>
## 七、集成路由vue-router4

- [vue-router官网](https://next.router.vuejs.org/zh/)

安装：
```vue
yarn add vue-router@next
```
安装完后，在src下创建一个`routes`文件夹，在里面创建`index.js`：
```javascript
import {
  createRouter,
  createWebHistory,
  createWebHashHistory
} from 'vue-router'

import { routerMode, base } from '../config'

const routes = [
  {
    path: '/',
    name: 'index',
    component: () => import('@/pages/index/index.vue'),
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('@/pages/test/test.vue'),
  },
]

const router = createRouter({
  history: routerMode === 'hash' ? createWebHashHistory(base) : createWebHistory(base),
  routes
})

export default router
```
其中：

- `base`如果在服务器中使用了路径级路由（项目不运行在根下），需要配置base
- `routerMode`路由模式，分为hash模式和history模式，分别使用`createWebHashHistory`和 `createWebHistory`创建路由

其中 `config.js`为公共配置文件，这里需要用到以下配置：
```javascript
// 路由模式: hash / history
export const routerMode = 'history'

// 应用的基路径。例如，如果整个单页应用服务在 /app/ 下，然后 base 就应该设为 "/app/"
export const base = '/app/'
```
如果启用了路径级路由，相应地在`vite.config.js`中也应该配置：
```javascript
import { base } from './src/config'

export default defineConfig({
  base,
  ...
})
```

在`main.js`中引入路由：
```javascript
import { createApp } from 'vue'
import router from './routes/index'
import App from './App.vue'

let app = createApp(App)
app.use(router)
app.mount('#app')
```

在`App.vue`中使用路由视图 `router-view`：
```vue
<template lang='pug'>
router-view
</template>
```

创建两个页面：`pages/index/index.vue`和 `pages/test/test.vue`
```vue
// pages/index/index.vue
<template lang='pug'>
div
  button(@click='go("test")') test
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function go(name) {
  router.push({ name })
}
</script>
```
```vue
// pages/test/test.vue
<template lang='pug'>
div
  button(@click='go("index")') index
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function go(name) {
  router.push({ name })
}
</script>
```
运行项目后，就可以看到路由相互跳转了。

<a name="DLzsE"></a>
## 八、集成状态管理pinia

- [pinia官网](https://pinia.vuejs.org/)

安装：
```vue
yarn add pinia
```

安装完后，在`main.js`中引入pinia：
```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
...

let app = createApp(App)

app.use(createPinia())
...

app.mount('#app')
```

在src下创建一个`stores`文件夹，写一些示例的状态管理：
```javascript
// src/stores/main.js
import { defineStore } from 'pinia'

export const useMainStore = defineStore('main', {
  state: () => ({ count: 1 }),
  actions: {
    increment() {
      this.count++
    },
  },
})
```
在vue单页文件中使用：
```vue
<template lang='pug'>
div
  div {{ counter.count }}
  button(@click="increment") increment
</template>

<script setup>
import { useMainStore } from '@/stores/main'

const counter = useMainStore()

function increment() {
  // counter.count++
  // counter.$patch({ count: counter.count + 1 })
  counter.increment()
}
</script>
```

<a name="laKFr"></a>
## 九、封装请求类
首先我们在 `config.js`中配置公共请求地址：
```json
export const globalUrl = 'http://localhost:8001'
```

为了满足大部分请求的情况，使用Map映射表的方式处理请求地址。

创建一个请求映射文件 `src\api\urls.js`，基本配置如下：
```json
export const urls = function(type) {
  // [请求地址, 请求方式, contentType]
  // contentType === 1 : 'application/x-www-form-urlencoded;charset=UTF-8'
  // contentType === 2 : 'application/json'
  let urlObj = {
    success: ['/app/success', 'get', 1],
    fail: ['/app/fail', 'get', 1],
    500: ['/app/500', 'get', 1],
    404: ['/app/404', 'get', 1],
    get: ['/app', 'get', 1],
    post: ['/app', 'post', 1],
    put: ['/app', 'put', 1],
    delete: ['/app', 'delete', 1],
  }

  return urlObj[type] || ''
}
```
这里用了一个数组存储 `[请求地址, 请求方式, contentType] `

- 请求地址: 除去globalUrl以外的部分
- 请求方式: 可以是get、post、put、delete等
- contentType: 用枚举存储，主要是`x-www-form-urlencoded`和 `json`，其他也可以自定义添加

<a name="Ry6SS"></a>
### 基础请求类
以下我使用了fetch作为请求方法，然后就是创建一个解析上面Map映射的请求类 `src\api\index.js`：
```json
import { urls } from './urls'
import { globalUrl } from '../config'

export class API {
  constructor(baseProjectUrl) {
    this.baseProjectUrl = baseProjectUrl
  }

  async resolve(
    type,
    data = {},
    options = {
      data: {},
      noPos: false,
      showErrorToast: false,
      shouldLogin: true
    }
  ) {
    let [url, method, requestType] = urls(type, options)

    if (!url.includes('http')) {
      url = this.baseProjectUrl + url
    }

    // TODO: 从storage获取授权码
    let authentication = ''

    let contentType = ''

    if (requestType === 1) {
      contentType = 'application/x-www-form-urlencoded;charset=UTF-8'
    } else {
      contentType = 'application/json'
    }

    options.data = options.data || {}
    options.data.authentication = authentication

    data = { ...options.data, ...data }

    // 删除无用的键值
    for (const key in data) {
      if (data[key] === undefined || data[key] === null) {
        delete data[key]
      }
    }

    let res = await fetch(url, {
      method,
      headers: {
        'Content-Type': contentType,
        authentication
      },
    })

    try {
      // 错误的处理，根据实际情况进行处理
      if (res.status === 500) {
        console.error('500: 服务器错误')
        throw res.status
      } else if (res.status === 404) {
        console.error('404: 请求资源不存在')
        throw res.status
      } else if (res.status === 400) {
        console.error('400: 参数错误')
        throw res.status
      }

      // 响应正常：200
      let resData = await res.json()
      if (Number(resData.code) === 1) {
        // 成功返回的数据结构：
        // {"code": 1, "data": {}, "message":"操作成功！"}
        return resData.data
      } else {
        // 失败返回的数据结构：
        // {"code": 0, "data": {}, "message":"操作失败！"}
        throw resData.message
      }
    } catch (e) {
      // 失败的处理
      console.error(e)
    }
  }
}

export const api = new API(globalUrl)
```
这只是一个基础的请求类封装，后续可以根据业务进行扩展。只有一个基本方法：`resolve`，用来解析上面的那个请求的Map映射。

我们用nest.js创建一个基本的控制器：
```json
import { Controller, Delete, Get, HttpStatus, Post, Put, Res } from '@nestjs/common';
import { Response } from 'express';
import { AppService } from './app.service';

@Controller('app')
export class AppController {
  constructor() {}

  @Get('/success')
  success() {
    return {
      code: 1,
      data: { name: 'xiaoyu', age: 18 },
      message: "操作成功！"
    }
  }

  @Get('/fail')
  fail() {
    return {
      code: 0,
      data: {},
      message: "操作失败！"
    }
  }

  @Get('/500')
  serverError(@Res() res: Response) {
    res.status(HttpStatus.INTERNAL_SERVER_ERROR).send()
  }

  @Get('/404')
  notFoundError(@Res() res: Response) {
    res.status(HttpStatus.NOT_FOUND).send()
  }

  @Get()
  async query(): Promise<any> {
    return {
      code: 1,
      data: {},
      message: "查询成功！"
    };
  }

  @Post()
  async add(): Promise<any> {
    return {
      code: 1,
      data: {},
      message: "添加成功！"
    };
  }

  @Delete()
  async delete(): Promise<any> {
    return {
      code: 1,
      data: {},
      message: "删除成功！"
    };
  }

  @Put()
  async modify(): Promise<any> {
    return {
      code: 1,
      data: {},
      message: "修改成功！"
    };
  }
}
```

在vue单页中使用：
```vue
<script setup>
import { onMounted } from 'vue'
import { api } from '@/api'

onMounted(async() => {
  let res = await api.resolve('success')
  console.log(res)
})
</script>
```
这里调用 `api.resolve`去请求数据，参数为Map映射表里面的key，resolve相当于做了如下翻译：
```vue
以get的方式去请求接口 http://localhost:8001/app/success，请求头里面的content-type为'application/x-www-form-urlencoded;charset=UTF-8'
```
可以看到控制台打印：
```vue
{name: 'xiaoyu', age: 18}
```

<a name="I4ufD"></a>
### 请求的参数
<a name="NvEOv"></a>
#### 查询字符串参数
我们修改nest.js中的控制器，让其可以接收查询字符串参数：
```typescript
  @Get()
  async query(@Query() query: any): Promise<any> {
    return {
      code: 1,
      data: {
        id: query.id,
        name: query.name
      },
      message: "查询成功！"
    };
  }
```
我的封装类还需要修改，用于处理query：
```typescript
import qs from 'qs'

export class API {
		...
    
		// get请求方式，直接在url中拼上查询字符串
    if (method.toLowerCase().trim() === 'get') {
      if (data) {
        url += '?' + qs.stringify(data)
      }
    }

    let res = await fetch(url, {
      method,
      data,
      headers: {
        'Content-Type': contentType,
        authentication
      },
    })
    
    ...
}
```
在vue单页中调用：
```typescript
onMounted(async() => {
  let res = await api.resolve('get', {
    id: 1,
    name: 'xiaoyu'
  })
  console.log(res)
})
```
这样就可以通过第二个参数传递查询字符串了。

![Snipaste_2022-01-15_17-06-07.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1642237609939-30d54a72-94f6-4133-b222-a4a6fdd05218.png#clientId=u5bb28d21-66b1-4&from=drop&id=ua680767d&originHeight=153&originWidth=519&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4314&status=done&style=none&taskId=uf42247a9-7d83-47f3-81f9-549d9e177b8&title=)![Snipaste_2022-01-15_17-06-20.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1642237609954-9a0ce912-84f8-4da4-bd56-f430c99eee2c.png#clientId=u5bb28d21-66b1-4&from=drop&id=u98a41bdb&originHeight=108&originWidth=513&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3248&status=done&style=none&taskId=ueeac6d97-2359-451a-a35a-e383ce992a3&title=)

<a name="AVcXG"></a>
#### 请求体参数
我们修改nest.js中的控制器，让其可以接收请求体参数：
```typescript
  @Post()
  async add(@Body() data: any): Promise<any> {
    return {
      code: 1,
      data: data,
      message: "添加成功！"
    };
  }
```
我的封装类还需要修改，用于处理请求体：
```typescript
import qs from 'qs'

export class API {
		...
    
		// get请求方式，直接在url中拼上查询字符串
    let body = ''
    if (method.toLowerCase().trim() === 'get') {
      if (data) {
        url += '?' + qs.stringify(data)
      }
    } else {
      // post、put、delete请求方式，解析body
      if (requestType === 1) {
        body = qs.stringify(data)
      } else {
        body = JSON.stringify(data)
      }
    }

    let res = await fetch(url, {
      method,
      body,
      headers: {
        'Content-Type': contentType,
        authentication
      },
    })
    
    ...
}
```
其中，body需要根据Content-Type做相应的处理：

- `application/x-www-form-urlencoded;charset=UTF-8` 使用`qs.stringify`解析
- `application/json`使用 `JSON.stringify`解析

<a name="cxV8H"></a>
### 错误处理








<a name="z1ZcM"></a>
## 十、外部库



<a name="EaG6C"></a>
## 十一、公共库






