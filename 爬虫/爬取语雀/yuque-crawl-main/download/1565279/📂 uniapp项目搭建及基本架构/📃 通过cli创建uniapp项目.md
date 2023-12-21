官方文档：[https://uniapp.dcloud.io/quickstart-cli](https://uniapp.dcloud.io/quickstart-cli)

首先确保vue-cil已经安装，若未安装，使用以下命令安装：
```bash
npm i -g @vue/cli
```

通过 cli 生成项目：
```bash
# vue2 + vue-cli
vue create -p dcloudio/uni-preset-vue my-project # 正式版
vue create -p dcloudio/uni-preset-vue#alpha my-alpha-project # alpha版

# vue3 + vite 
npx degit dcloudio/uni-preset-vue#vite my-vue3-project # javascript
npx degit dcloudio/uni-preset-vue#vite-ts my-vue3-project # typescript
```

创建好的项目结构如下：
```bash
┌─components            uni-app公共组件目录
│  └─comp-a.vue         可复用的a组件
├─wxcomponents          小程序私有组件，遵循小程序的开发方式，也可使用Vue的写法
│   └──miniprogram-slide-view
│        ├─index.js
│        ├─index.vue
│        ├─index.json
│        └─index.wxss
├─pages                 业务页面文件存放目录
│  ├─index
│  │  └─index.vue       index页面
│  └─list
│     └─list.vue        list页面
├─static                存放应用引用静态资源（如图片、视频等）的地方，注意：静态资源只能存放于此
├─main.js               Vue初始化入口文件
├─App.vue               应用配置，用来配置App全局样式以及监听
├─manifest.json         配置应用名称、appid、logo、版本等打包信息
└─pages.json            配置页面路由、导航条、选项卡等页面类信息，应用的生命周期
```

![](https://kan.xiaoyulive.top/uniapp/017.png#height=439&id=qYtVf&originHeight=439&originWidth=232&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=232)

<a name="18b69eb8"></a>

## 项目结构规划
我规划的项目结构如下：<br />![](https://kan.xiaoyulive.top/uniapp/018.png#height=863&id=iREmV&originHeight=863&originWidth=332&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=332)

最重要的是src目录的规划，一些关键的目录：

- `api` 存放请求
- `components` 存放全局组件
- `directives` 存放全局指令
- `filter` 存放全局过滤器
- `hybrid` 存放混合编译页面
- `library` 自定义库
- `pages` 页面
- `static` 静态资源
- `store` Vuex状态管理

<a name="f3457ac2"></a>
## 必要的工具
工欲善其事，必先利其器，列举我常用的一些开发工具：

- pug
- pug-plain-loader
- stylus
- stylus-loader
- node-sass
- prettier
- postcss-comment

<a name="53ebff98"></a>
## 使用不同的开发工具

- [使用HBuilderX开发](https://uniapp.dcloud.io/quickstart)
- [使用WebStrom开发](https://ask.dcloud.net.cn/article/36307)
- [使用VSCode开发](https://ask.dcloud.net.cn/article/36286)

CLI 工程默认带了 uni-app 语法提示和 5+App 语法提示

可以下载 [uniapp-snippets-vscode](https://github.com/zhetengbiji/uniapp-snippets-vscode) 放于 `.vscode` 目录下已获得 uniapp 的代码块提示

## 参考资料

- [开发uni-app，HBuilderX和其他工具(如vscode)有什么区别](https://ask.dcloud.net.cn/article/35451)



