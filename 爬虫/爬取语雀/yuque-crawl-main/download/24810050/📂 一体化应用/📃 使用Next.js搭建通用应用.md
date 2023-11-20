<a name="vSYIC"></a>
## Next.js简介
官方介绍：
:::tips
Next.js 为您提供生产环境所需的所有功能以及最佳的开发体验：包括静态及服务器端融合渲染、 支持 TypeScript、智能化打包、 路由预取等功能 无需任何配置。
:::

用我自己的话来说，Next.js是一个全栈框架，将服务端和客户端有效地统一起来了。

[Next.js by Vercel - The React Framework](https://nextjs.org/)<br />[Next.js - React 应用开发框架](https://www.nextjs.cn/)<br />[Next.js on Vercel – Vercel](https://vercel.com/solutions/nextjs)

官方GitHub：

- [https://github.com/vercel/next.js](https://github.com/vercel/next.js)
- [https://github.com/vercel/next-learn](https://github.com/vercel/next-learn/)

<a name="VlVqe"></a>
## 创建Next.js应用
使用命令创建Next.js应用：
```bash
npx create-next-app@latest
# or
yarn create next-app
```

项目创建好后，会自动安装依赖，但项目本身不包含目录结构，只有一个`packages.json`：
```bash
{
  "name": "nextjs_project",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "12.1.1",
    "react": "17.0.2",
    "react-dom": "17.0.2"
  }
}
```

运行项目，使用命令：
```bash
yarn dev
```
应用程序默认运行到3000端口下。

如果需要加入git版本控制，请手动在项目下添加 `.gitignore`文件：
```jsx
node_modules
.next
```

<a name="OZi4b"></a>
## 构建
使用命令 `yarn build`进行应用程序构建：
```jsx
❯ yarn build
yarn run v1.22.17
$ next build
info  - Checking validity of types
info  - Need to disable some ESLint rules? Learn more here: https://nextjs.org/docs/basic-features/eslint#disabling-rules
info  - Creating an optimized production build  
info  - Compiled successfully
info  - Collecting page data
├ λ /api/data1                             0 B            71.8 kB
├ ● /page1                                 303 B          72.1 kB
├ ● /page2                                 354 B          72.2 kB
└ ○ /posts/[id]                            323 B          72.2 kB
+ First Load JS shared by all              71.8 kB
  ├ chunks/framework-5f4595e5518b5600.js   42 kB
  ├ chunks/main-38102973b285480e.js        27.7 kB
  ├ chunks/pages/_app-9a4e0bcfd9f9bf48.js  1.36 kB
  └ chunks/webpack-fd82975a6094609f.js     727 B

λ  (Server)  server-side renders at runtime (uses getInitialProps or getServerSideProps)
○  (Static)  automatically rendered as static HTML (uses no initial props)
●  (SSG)     automatically generated as static HTML + JSON (uses getStaticProps)

Done in 11.71s.
```
构建完成后会生成 `.next`文件夹。

使用命令 `yarn start`会运行构建好的运用程序。

<a name="Y5vLv"></a>
## 页面
在项目中创建 `pages`目录，用于存放React页面代码。

创建页面`pages/index.js`
```jsx
function HomePage() {
  return <div>home</div>
}

export default HomePage
```

直接访问 [http://localhost:3000/](http://localhost:3000/) 就可在浏览器看到效果

<a name="zYzsy"></a>
## 路由
<a name="csFon"></a>
### 动态路由
创建一个动态路由页面，格式为 `[queryParam].js`

比如创建一个文件 `pages/post/[id].js`，内容如下：
```jsx
import { useRouter } from 'next/router'

const Post = () => {
  const router = useRouter()
  const { id } = router.query

  return <p>Post: {id}</p>
}

export default Post
```

在浏览器中输入 [http://localhost:3000/posts/1](http://localhost:3000/posts/1)，可以看到页面中显示：
```jsx
Post: 1
```

<a name="bxkuK"></a>
## 数据请求
在









