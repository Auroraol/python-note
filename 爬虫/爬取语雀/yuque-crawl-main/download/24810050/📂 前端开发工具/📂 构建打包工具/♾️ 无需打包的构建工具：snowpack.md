<a name="Be8Fs"></a>
## ✨  snowpack简介
- [s](https://www.snowpack.dev/)snowpack官网

[Snowpack](https://www.snowpack.dev/)

- GitHub

[GitHub - withastro/snowpack: ESM-powered frontend build tool. Instant, lightweight, unbundled development. ✌️](https://github.com/snowpackjs/snowpack)

`snowpack`，号称 `无需打包工具（Webpack，Parcel）便能将代码结果实时展现在浏览器中`。

Snowpack最初是Fred在Google 的 Polymer 团队工作中做出来一个用于替代 HTML imports规范的构建工具，后来引申出 「为什么npm包在浏览器运行都需要借助webpack打包，而不能单独运行在浏览器呢？」 的问题，于是Fred就针对 「npm包单独运行在浏览器」 的可行性开始不断的尝试，这就有了之后的Snowpack。

在 ESM 出现之前，JavaScript 的模块化就有各式各样的规范，主要有 CommonJS, AMD, CMD, UMD 等规范，最为广泛的就是 Node.js 的 CommonJS，使用 module.exports 和 require 来导出导入模块，它是 npm 中的模块最主要提供的格式。由于浏览器并不直接支持这些模块，因此打包工具（Webpack，Browserify，Parcel 等）出现了。

1. 在开发过程中你是否遇到 webapp 总是需要等待才能看到结果，每次保存后电脑就非常疯狂。
2. webpack 之类的打包工具功能非常强大，他们引入配置，插件，依赖成本很低，任意创建一个 react 应用便将要安装 200M 的依赖包，并且需要写很多行的webpack配置。
3. ESM在浏览器中使用了大约5年的时间，现在在所有现代浏览器中都受支持（可追溯到2018年初）。使用ESM，不再需要打包工具。您可以在没有 Webpack 的情况下构建一个现代化，高性能，可用于生产的Web应用程序！
4. 你只需安装运行一次 snowpack 替换 Webpack，Parcel等繁杂的打包工具，可以获得更快的开发环境，并减少工具复杂性。


bundle与bundleless对比图：

|  | Bundle（Webpack） | Bundleless（Snowpack） |
| --- | --- | --- |
| 启动时间 | 长，完整打包项目 | 短，只启动 dev server，按需加载 |
| 构建时间 | 随项目体积线性增长 | 构建时间复杂度O(1) |
| 加载性能 | 打包后加载对应bundle | 请求映射至本地文件 |
| 缓存能力 | 缓存利用率一般，受spit方式影响 | 缓存利用率近乎完美 |
| 文件更新 | 重新打包 | 重新请求单个文件 |
| 调试体验 | 通常需要SourceMap进行调试 | 不强依赖 SourceMap，可单文件调试 |
| 生态 | Webpack做的太好太强大了 | 不成熟，但一年时间发展迅猛 |


<a name="EWtpS"></a>
## ✨  创建snowpack项目
创建一个snowpack项目，只需要安装snowpack包即可：
```html
npm init
yarn add -D snowpack
```
在`package.json`中添加以下脚本：
```json
{
  "scripts": {
    "start": "snowpack dev",
    "build": "snowpack build"
  },
  "devDependencies": {
    "snowpack": "^3.8.8"
  }
}
```

接下来创建一个ESM的模块：
```json
export function helloWorld() {
  console.log('Hello World !');
}
```
在`index.js`中引入：
```json
import { helloWorld } from './sayHello.js';

helloWorld();
```
再创建一个`index.html`中引入：
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Starter Snowpack App" />
    <title>Starter Snowpack App</title>
    <script type="module" src="./js/index.js"></script>
  </head>
  <body>
    <div>Hello Snowpack</div>
  </body>
</html>
```

通过运行命令即可开启本地服务：
```html
yarn start
```
默认运行在 [http://localhost:8080](http://localhost:8080)，这是一个热更新服务器，修改代码可以直接看到效果。

<a name="E1yeD"></a>
### 使用NPM包
比如引入一个`canvas-confetti`包
```html
yarn add canvas-confetti
```
修改`index.js`
```javascript
import confetti from 'canvas-confetti';
confetti.create(document.getElementById('canvas'), {
  resize: true,
  useWorker: true,
})({ particleCount: 200, spread: 200 });
```
直接保存，在浏览器就可以看到效果。


<a name="V5wlL"></a>
### 使用CSS
可以跟正常使用CSS一样的，创建一个css，通过link引入
```css
body {
  color: red;
}
```
```css
<link rel="stylesheet" type="text/css" href="./css/index.css" />
```

也可以在script中直接引入css（注意：一定要添加`type="module"`）
```less
<script type="module">
  import './css/index.css'
</script>
```

<a name="zWIE9"></a>
### 运行项目
通过运行 `yarn start`运行项目，会自动打开浏览器访问，会在`node_modules`下生成`.cache/snowpack`目录：<br />![Snipaste_2022-04-11_16-23-26.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649665447536-84d4a6ac-07ce-4c67-ac4f-ea3088bfad80.png#clientId=u35641d61-d002-4&from=drop&id=ub3e738f1&originHeight=153&originWidth=261&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3787&status=done&style=none&taskId=u183b0a06-b5b3-42d6-9a25-4a1e8161393&title=)

<a name="Nkoqc"></a>
### 构建项目
通过运行 `yarn build`构建项目，会生成一个`build`目录：<br />![Snipaste_2022-04-08_14-49-52.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649400601934-ae149504-9de4-4a40-8957-b8bffb9b9c9a.png#clientId=ubf625398-1eef-4&from=drop&id=ue535fe29&originHeight=287&originWidth=187&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4526&status=done&style=none&taskId=uce2946d0-a5ed-40ba-aa1f-ce1bd972e44&title=)<br />直接开启本地服务即可运行。

<a name="DauD4"></a>
## ✨  使用snowpack脚手架创建项目
针对一些特定项目（比如Vue、React），snowpack提供对应的脚手架创建项目。

- 官方文档：[Create Snowpack App (CSA)](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/cli#create-snowpack-app-csa)
```javascript
npx create-snowpack-app new-dir --template @snowpack/app-template-NAME [--use-yarn | --use-pnpm | --no-install | --no-git]
```

官方模板：

- [@snowpack/app-template-blank](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-blank)
- [@snowpack/app-template-blank-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-blank-typescript)
- [@snowpack/app-template-11ty](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-11ty)
- [@snowpack/app-template-lit-element](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-lit-element)
- [@snowpack/app-template-lit-element-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-lit-element-typescript)
- [@snowpack/app-template-preact](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-preact)
- [@snowpack/app-template-preact-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-preact-typescript)
- [@snowpack/app-template-react](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-react)
- [@snowpack/app-template-react-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-react-typescript)
- [@snowpack/app-template-svelte](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-svelte)
- [@snowpack/app-template-svelte-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-svelte-typescript)
- [@snowpack/app-template-vue](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-vue)
- [@snowpack/app-template-vue-typescript](https://github.com/snowpackjs/snowpack/tree/main/create-snowpack-app/app-template-vue-typescript)

<a name="dm0H4"></a>
### 创建空模板项目
使用`@snowpack/app-template-minimal`创建一个空模板项目
```css
npx create-snowpack-app snowpack-test --template @snowpack/app-template-minimal --use-yarn
cd snowpack-test
npm run start
```
查看`package.json`，这样创建出的是一个最小化的snowpack应用程序，并没有用到其他依赖。
```json
{
  "scripts": {
    "start": "snowpack dev",
    "build": "snowpack build"
  },
  "devDependencies": {
    "snowpack": "^3.3.7"
  }
}
```

<a name="qDcsf"></a>
### 创建React项目
<a name="ucR9C"></a>
#### 通过模板创建React项目
```bash
npx create-snowpack-app snowpack-react-test --template @snowpack/app-template-react --use-yarn
cd snowpack-react-test
yarn start
```
![Snipaste_2022-04-11_09-56-34.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649642285769-c8b7053f-62e2-472e-9137-d8be3253ea8d.png#clientId=ud0a2eccb-9688-4&from=drop&id=u847dcdbd&originHeight=351&originWidth=404&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10129&status=done&style=none&taskId=u9559a16b-3b9f-4bb7-9627-1a82608b98a&title=)<br />查看`package.json`，可以看到使用了以下依赖：
```json
{
  "scripts": {
    "start": "snowpack dev",
    "build": "snowpack build",
    "test": "web-test-runner \"src/**/*.test.jsx\"",
    "format": "prettier --write \"src/**/*.{js,jsx}\"",
    "lint": "prettier --check \"src/**/*.{js,jsx}\""
  },
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "devDependencies": {
    "@snowpack/plugin-dotenv": "^2.1.0",
    "@snowpack/plugin-react-refresh": "^2.5.0",
    "@snowpack/web-test-runner-plugin": "^0.2.2",
    "@testing-library/react": "^11.2.6",
    "@web/test-runner": "^0.13.3",
    "chai": "^4.3.4",
    "prettier": "^2.2.1",
    "snowpack": "^3.3.7"
  }
}
```

<a name="SVsGN"></a>
#### 通过空模板创建React项目
```css
npx create-snowpack-app snowpack-react-test --template @snowpack/app-template-minimal --use-yarn
cd snowpack-react-test
npm run start
```
这样创建出的是一个最小化的snowpack应用程序，并没有用到其他依赖。

我们得手动添加依赖：
```json
yarn add react react-dom
```

然后将`index.js`重命名为`index.jsx`，内容替换为：
```json
import React from 'react';
import ReactDOM from 'react-dom';
ReactDOM.render(<div>"HELLO REACT"</div>, document.getElementById('root'));
```
在`index.html`中引入的仍然是`index.js`：
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Starter Snowpack App" />
    <title>Starter Snowpack App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/index.js"></script>
  </body>
</html>
```

重新运行 `yarn start`，即可看到效果。

<a name="xGGhz"></a>
##### 使用@snowpack/plugin-react-refresh
` @snowpack/plugin-react-refresh`用于增强snowpack对于React快速刷新。

安装：
```json
yarn add -D @snowpack/plugin-react-refresh
```

配置：
```json
module.exports = {
  plugins: ['@snowpack/plugin-react-refresh'],
  ...
};
```

修改`index.jsx`：
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
);

// Hot Module Replacement (HMR) - Remove this snippet to remove HMR.
// Learn more: https://www.snowpack.dev/concepts/hot-module-replacement
if (import.meta.hot) {
  import.meta.hot.accept();
}
```
其中`App.jsx`示例：
```jsx
import React, {useState, useEffect} from 'react';

function App() {
  // Create the count state.
  const [count, setCount] = useState(0);
  // Update the count (+1 every second).
  useEffect(() => {
    const timer = setTimeout(() => setCount(count + 1), 1000);
    return () => clearTimeout(timer);
  }, [count, setCount]);
  // Return the App component.
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Page has been open for <code>{count}</code> seconds.
        </p>
      </header>
    </div>
  );
}

export default App;
```

<a name="phnXI"></a>
### 创建Vue项目
<a name="LNLU5"></a>
#### 通过模板创建Vue项目
```bash
npx create-snowpack-app snowpack-vue-test --template @snowpack/app-template-vue --use-yarn
cd snowpack-vue-test
yarn start
```
![Snipaste_2022-04-11_09-56-48.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649642298499-0331284c-aca4-4fd2-960d-5fb193efebf3.png#clientId=ud0a2eccb-9688-4&from=drop&id=u4365d498&originHeight=319&originWidth=365&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4087&status=done&style=none&taskId=ubf013733-a64e-48b3-bc7e-b0dcb17ba31&title=)<br />查看`package.json`，可以看出其实是使用了`@snowpack/plugin-vue`插件解析Vue文件：
```json
{
  "scripts": {
    "start": "snowpack dev",
    "build": "snowpack build"
  },
  "dependencies": {
    "vue": "^3.0.11"
  },
  "devDependencies": {
    "@snowpack/plugin-dotenv": "^2.1.0",
    "@snowpack/plugin-vue": "^2.4.0",
    "snowpack": "^3.3.7"
  }
}
```

<a name="uErhy"></a>
#### 通过空模板创建Vue项目
```css
npx create-snowpack-app snowpack-vue-test --template @snowpack/app-template-minimal --use-yarn
cd snowpack-vue-test
npm run start
```
这样创建出的是一个最小化的snowpack应用程序，并没有用到其他依赖。

我们得手动添加依赖：
```json
yarn add  vue@3.0.11
yarn add -D @snowpack/plugin-vue
```
然后在`snowpack.config.mjs`中注册插件：
```json
export default {
  plugins: [
    /* ... */
    '@snowpack/plugin-vue',
  ],
  ...
};
```

修改`index.html`
```jsx
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Starter Snowpack App" />
    <title>Starter Snowpack App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/index.js"></script>
  </body>
</html>
```
修改`index.js`
```jsx
import {createApp} from 'vue';
import App from './App.vue';

const app = createApp(App);
app.mount('#app');
```
创建`App.vue`
```vue
<script>
  export default {
    setup() {
      return {};
    },
  };
</script>
<template>
<div>Welcome to my Vue app!</div>
</template>
```

重新运行 `yarn start`，即可看到效果。


<a name="WuZUb"></a>
### 创建Svelte项目
<a name="PxQBh"></a>
#### 通过模板创建Svelte项目
```diff
npx create-snowpack-app snowpack-svelte-test --template @snowpack/app-template-svelte --use-yarn
cd snowpack-svelte-test
npm run start
```
![Snipaste_2022-04-11_11-21-53.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1649647340460-33767168-1c4b-429d-bc03-e02f0b1a76c9.png#clientId=ud0a2eccb-9688-4&from=drop&id=u21804c58&originHeight=392&originWidth=426&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7976&status=done&style=none&taskId=u9b05a7e9-8f43-4b97-8d8d-6a24f5fe1b3&title=)<br />查看`package.json`，可以看出其实是使用了`@snowpack/plugin-svelte`插件解析Svelte文件：
```json
{
  "scripts": {
    "start": "snowpack dev",
    "build": "snowpack build",
    "test": "web-test-runner \"src/**/*.test.js\""
  },
  "dependencies": {
    "svelte": "^3.37.0"
  },
  "devDependencies": {
    "@snowpack/plugin-dotenv": "^2.1.0",
    "@snowpack/plugin-svelte": "^3.6.1",
    "@snowpack/web-test-runner-plugin": "^0.2.2",
    "@testing-library/svelte": "^3.0.3",
    "@web/test-runner": "^0.13.3",
    "chai": "^4.3.4",
    "snowpack": "^3.3.7"
  }
}
```

<a name="aHucc"></a>
#### 通过空模板创建Svelte项目
```css
npx create-snowpack-app snowpack-svelte-test --template @snowpack/app-template-minimal --use-yarn
cd snowpack-svelte-test
npm run start
```
这样创建出的是一个最小化的snowpack应用程序，并没有用到其他依赖。

我们得手动添加依赖：
```json
yarn add svelte
yarn add -D  @snowpack/plugin-svelte
```
然后在`snowpack.config.mjs`中注册插件：
```json
export default {
  plugins: [
    /* ... */
    '@snowpack/plugin-svelte',
  ],
  ...
};
```

配置完后，创建一个`svelte`文件：
```html
<script>
  /* component logic will go here */
</script>
<style>
  /* css will go here */
</style>
<div class="App">
  <header class="App-header">
    <a class="App-link" href="https://svelte.dev" target="_blank" rel="noopener noreferrer">
      Learn Svelte
    </a>
  </header>
</div>
```
再在`index.js`中引入：
```javascript
import App from "./App.svelte";

let app = new App({
  target: document.body,
});

export default app;
```

重新运行 `yarn start`，即可看到效果。


<a name="rqU9v"></a>
## ✨  snowpack工程化
<a name="B2hgZ"></a>
### 引入less
使用[snowpack-plugin-less](https://www.npmjs.com/package/snowpack-plugin-less)以增加对less的支持。

安装依赖：
```javascript
yarn add -D snowpack-plugin-less less
```
在`snowpack.config.json`中添加配置：
```less
{
  "plugins": [
    "snowpack-plugin-less"
  ]
}
```

比如创建一个 `index.less`文件：
```less
.a {
  .b {
    color: red;
  }
}
```

在`index.js`中引入less文件：
```less
import './index.less'
```

在`index.html`中引入js：
```less
<!DOCTYPE html>
<html lang="en">
  <head>
    <script type="module" src="./index.js"></script>
  </head>
  <body>
    <div class="a">
      <div class="b">hello</div>
    </div>
  </body>
</html>
```

也可以在html的script中直接引入`less`文件（注意：一定要添加`type="module"`）：
```less
<!DOCTYPE html>
<html lang="en">
  <head>
    <script type="module">
      import './index.less'
    </script>
  </head>
  <body>
    <div class="a">
      <div class="b">hello</div>
    </div>
  </body>
</html>

```

<a name="kNS5A"></a>
### 引入scss/sass
使用[@snowpack/plugin-sass](https://www.npmjs.com/package/@snowpack/plugin-sass)插件以增加对sass的支持。

安装依赖：
```less
yarn add -D @snowpack/plugin-sass sass
```
在`snowpack.config.json`中添加配置：
```less
{
  "plugins": [
    [
      '@snowpack/plugin-sass',
      {
        /* plugin options */
      },
    ],
  ]
}
```

比如创建一个 `index.scss`文件：
```less
.a {
  .b {
    color: red;
  }
}
```

在`index.js`中引入scss文件：
```less
import './index.scss'
```

在`index.html`中引入js：
```less
<!DOCTYPE html>
<html lang="en">
  <head>
    <script type="module" src="./index.js"></script>
  </head>
  <body>
    <div class="a">
      <div class="b">hello</div>
    </div>
  </body>
</html>
```

也可以在html的script中直接引入`scss`（注意：一定要添加`type="module"`）：
```less
<!DOCTYPE html>
<html lang="en">
  <head>
    <script type="module">
      import './index.scss'
    </script>
  </head>
  <body>
    <div class="a">
      <div class="b">hello</div>
    </div>
  </body>
</html>

```

<a name="RANQd"></a>
### 引入pug
使用[snowpack-plugin-pug](https://www.npmjs.com/package/snowpack-plugin-pug)插件以增加对sass的支持。

安装依赖：
```less
yarn add -D @marlonmarcello/snowpack-plugin-pug pug
```
在`snowpack.config.json`中添加配置：
```less
export default {
  plugins: [
    ['@marlonmarcello/snowpack-plugin-pug',
      {
        "data": {
          "meta": {
            "title": "My website"
          }
        }
      }
    ]
  ]
}
```
将 `index.html`重命名为 `index.pug`，修改内容（注意title的传值）：
```less
doctype html
html(lang="en")
  head
    meta(charset="UTF-8")
    meta(name="viewport", content="width=device-width, initial-scale=1.0")
    title!=meta.title
  body
    div Hello
```

通过地址访问 [http://localhost:8080/index.html](http://localhost:8080/index.html)，注意必须刚上文件名(index.html)，暂时不知道解决方案。

如果要在pug中引入js或其他文件，可以通过以下写法引入：
```less
doctype html
html(lang="en")
  head
    meta(charset="UTF-8")
    meta(name="viewport", content="width=device-width, initial-scale=1.0")
    title!=meta.title
    script(type='module' src="./index.js")
    script(type="module").
      import './index.scss'
```


<a name="c9I3R"></a>
## ✨  snowpack配置
snowpack配置文件位于`snowpack.config.mjs`。

<a name="A0Sol"></a>
### 配置目标路径
在 `mount`节点配置生成目录的映射，格式为：
```javascript
mount: {
  [path: string]: string | {url: string, resolve: boolean, static: boolean, dot: boolean}
}
```
其中key为源路径；value可以为字符串，也可以为对象，为目标路径。<br />当value为对象时，支持以下选项：

- mount.url | string | _required_ : The URL to mount to, matching the string in the simple form above.
- mount.static | boolean | _optional_ | **Default**: false : If true, don’t build files in this directory. Copy and serve them directly from disk to the browser.
- mount.resolve | boolean | _optional_ | **Default**: true: If false, don’t resolve JS & CSS imports in your JS, CSS, and HTML files. Instead send every import to the browser, as written.
- mount.dot | boolean | _optional_ | **Default**: false: If true, include dotfiles (ex: .htaccess) in the final build.

示例：
```javascript
export default {
  mount: {
    // directory name: 'build directory'
    public: '/',
    src: '/dist',
  },
};
```
或者：
```javascript
export default {
  mount: {
    public: {url: '/', static: true},
    src: {url: '/dist'},
  },
}
```

图解如下：<br />![folder-structure.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1649646424154-f9cbc760-2b0c-4266-a3b2-b3d0334af63b.webp#clientId=ud0a2eccb-9688-4&from=drop&id=uebd46953&originHeight=800&originWidth=2048&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30502&status=done&style=none&taskId=u1224e706-043b-48ff-ad72-6124921e95a&title=)<br />配置后，在相应引入文件的地方也得修改路径：
```diff
index.html --> public/index.html
index.css --> public/index.css
index.js --> src/index.js
```
```diff
  <body>
    <h1>Welcome to Snowpack!</h1>
-   <script type="module" src="/index.js"></script>
+   <script type="module" src="/dist/index.js"></script>
  </body>
```

<a name="MZWyK"></a>
### 别名
使用`alias`选项可以配置别名，举例：
```javascript
export default {
  alias: {
    '@components': './src/components',
    '@': './src',
  }
};

```

比如在Vue项目中使用：
```vue
<template>
<div class="App">
  <AAAVue></AAAVue>
</div>
</template>

<script>
import AAAVue from '@components/AAA.vue';
export default {
  components: { AAAVue }
}
</script>
```

除了路径别名外，`node_modules`里面的包也可通过这种方式设置别名：
```javascript
export default {
  alias: {
    lodash: 'lodash-es',
    react: 'preact/compat',
  },
};
```

<a name="m4yAB"></a>
### 插件
插件配置有两种格式，单字符串或数组形式：
```javascript
export default {
  plugins: [
    // Simple format: no options needed
    'plugin-1',
    // Expanded format: allows you to pass options to the plugin
    ['plugin-2', {'plugin-option': false}],
  ];
}
```
如果是数组形式，第0项为插件名称，第1项为插件选项

可以在这个页面查询需要的插件：<br />[The Snowpack Plugin Catalog](https://www.snowpack.dev/plugins)


<a name="X7cNQ"></a>
## ✨  snowpack原理
snowpack 的最初版核心目标就是不再打包业务代码，而是直接使用浏览器原生的 JavaScript Module 能力。

所以从它的处理流程上来看，**对业务代码的模块，基本只需要把 ESM 发布（拷贝）到发布目录，再将模块导入路径从源码路径换为发布路径即可。**<br />而对 node_modules 则通过遍历 package.json 中的依赖，按该依赖列表为粒度将 node_modules 中的依赖打包。**以 node_modules 中每个包的入口作为打包 entry，使用 rollup 生成对应的 ESM 模块文件，放到 web_modules 目录中，最后替换源码的 import 路径，是得可以通过原生 JavaScript Module 来加载 node_modules 中的包。**
```bash
node_modules/react/**/*     -> http://localhost:3000/web_modules/react.js
node_modules/react-dom/**/* -> http://localhost:3000/web_modules/react-dom.js
```
对比源码和生成后的代码对比大概长这样：
```javascript
- import { createElement, Component } from "preact";
- import htm from "htm";

+ import { createElement, Component } from "/web_modules/preact.js";
+ import htm from "/web_modules/htm.js";
```

<a name="AjFx2"></a>
## ✨ snowpack命令行
<a name="OmBJV"></a>
### 查看帮助
通过执行`npx snowpack --help`可以看到所有的snowpack命令：
```javascript
$ npx snowpack --help
[18:06:52] [snowpack] snowpack - A faster build system for the modern web.

  Snowpack is best configured via config file.
  But, most configuration can also be passed via CLI flags.
  📖 https://www.snowpack.dev/reference/configuration

Commands:
  snowpack init          Create a new project config file.
  snowpack prepare       Prepare your project for development (optional).
  snowpack dev           Develop your project locally.
  snowpack build         Build your project for production.
  snowpack add [package] Add a package to your project.
  snowpack rm [package]  Remove a package from your project.

Flags:
  --config [path]        Set the location of your project config file.
  --help                 Show this help message.
  --version              Show the current version.
  --reload               Clear the local cache (useful for troubleshooting).
  --cache-dir-path       Specify a custom cache directory.
  --verbose              Enable verbose log messages.
  --quiet                Enable minimal log messages.
```

<a name="mckOV"></a>
### 指定包管理工具
如果不想要使用npm作为包管理工具，可以添加以下参数指定其他包管理工具：

- `--use-yarn`
- `--use-pnpm`

<a name="nTQTe"></a>
## ✨  参考资料

- [snowpack，提高10倍打包速度的神奇工具](https://mp.weixin.qq.com/s/VMYw-tSsNKfoIA41nV5olQ)
- [Snowpack 的作者，不打算维护它了……](https://mp.weixin.qq.com/s?__biz=MzAxODE2MjM1MA==&mid=2651582901&idx=2&sn=c865f2a410c4ee5a7870ee56b2fa7344&chksm=80252674b752af62435bb0553ed849ae5e45d5926e96b77177f16c691ceb0222d287fa53dae0&scene=21#wechat_redirect)
- [替代 webpack？带你了解 snowpack 原理，你还学得动么](https://zhuanlan.zhihu.com/p/149351900)
- [学了Vite再来看看Snowpack吧](https://www.jianshu.com/p/005e443256b5)


