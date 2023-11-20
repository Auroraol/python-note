- [taro官网](https://taro-docs.jd.com/taro/docs/README)

<a name="Wmc3P"></a>
## 一、安装taro并创建项目
全局安装taro：
```css
yarn global add @tarojs/cli
```

查看taro信息及帮助：
```css
npm info @tarojs/cli # 查看信息
taro info # 查看信息

taro # 查看版本号

taro -h # 查看帮助
  
taro doctor # 问题诊断
```

<a name="VVpYu"></a>
### 创建项目
使用taro创建项目：
```css
❯ taro init taroApp
👽 Taro v3.4.0

Taro 即将创建一个新项目!
Need help? Go and open issue: https://tls.jd.com/taro-issue-helper

? 请输入项目介绍！ taro_vue3_app
? 请选择框架
  React
  PReact
  Nerv
  Vue
> Vue3
```
所有的选项：
```bash
❯ taro init taroApp
👽 Taro v3.4.0

Taro 即将创建一个新项目!
Need help? Go and open issue: https://tls.jd.com/taro-issue-helper

? 请输入项目介绍！ taro_vue3_app
? 请选择框架 Vue3
? 是否需要使用 TypeScript ？ No
? 请选择 CSS 预处理器（Sass/Less/Stylus） Stylus
? 请选择模板源 Gitee（最快）
√ 拉取远程模板仓库成功！
? 请选择模板 默认模板
```

按照提示创建项目，可选Vue、Vue3、React等框架创建taro项目。使用不同框架搭建出来的项目结构将不一样。

如果未全局安装taro，可以使用以下命令创建项目：
```css
npx @tarojs/cli init myApp
```

<a name="AkyYs"></a>
### 运行项目
```bash
# dev模式
yarn dev:h5 # 网页
yarn dev:weapp # 微信小程序
yarn dev:alipay # 支付宝小程序
yarn dev:qq # QQ小程序
yarn dev:tt # 头条小程序
yarn dev:jd # 京东小程序
yarn dev:rn # React Native

# build模式
yarn build:h5 # 网页
yarn build:weapp # 微信小程序
yarn build:alipay # 支付宝小程序
yarn build:qq # QQ小程序
yarn build:tt # 头条小程序
yarn build:jd # 京东小程序
yarn build:rn # React Native

# watch 同时开启压缩
set NODE_ENV=production && taro build --type weapp --watch # Windows
NODE_ENV=production taro build --type weapp --watch # Mac
```

<a name="Jn6ih"></a>
### CLI配置
Taro 会在用户根目录下创建 .taro 文件夹，其中 .taro/index.json 用于存放 CLI 相关配置。
```bash
# 查看用法
$ taro config --help
# 设置配置项<key>的值为<value>
$ taro config set <key> <value>
# 读取配置项<key>
$ taro config get <key>
# 删除配置项<key>
$ taro config delete <key>
# 打印所有配置项
$ taro config list [--json]
```

<a name="f6ffc"></a>
### 创建页面
使用以下命令可以在`src/pages`下创建页面：
```bash
taro create --name [页面名称]
```

<a name="xKd9m"></a>
### 尺寸适配
在 Taro 中尺寸单位建议使用 `px`、 百分比 `%`，Taro 默认会对所有单位进行转换。在 Taro 中书写尺寸按照 1:1 的关系来进行书写，即从设计稿上量的长度 100px，那么尺寸书写就是 100px，当转成微信小程序的时候，尺寸将默认转换为 100rpx，当转成 H5 时将默认转换为以 rem 为单位的值。<br />**如果你希望部分 px 单位不被转换成 rpx 或者 rem ，最简单的做法就是在 px 单位中增加一个大写字母，例如 Px 或者 PX 这样，则会被转换插件忽略。**<br />结合过往的开发经验，Taro 默认以 750px 作为换算尺寸标准，如果设计稿不是以 750px 为标准，则需要在项目配置 config/index.js 中进行设置，例如设计稿尺寸是 640px，则需要修改项目配置 config/index.js 中的 designWidth 配置为 640。

在编译时，Taro 会帮你对样式做尺寸转换操作，但是如果是在 JS 中书写了行内样式，那么编译时就无法做替换了，针对这种情况，Taro 提供了 API Taro.pxTransform 来做运行时的尺寸转换。
```bash
Taro.pxTransform(10) // 小程序：rpx，H5：rem
```
参考：[设计稿及尺寸单位](https://taro-docs.jd.com/taro/docs/size/)

<a name="tcPpp"></a>
## 二、各框架项目结构概述
虽然使用各框架搭建的项目结构、内容都有差异，但也是有一个公共的基础结构，如下：
```css
├── dist                        编译结果目录
├── config                      项目编译配置目录
|   ├── index.js                默认配置
|   ├── dev.js                  开发环境配置
|   └── prod.js                 生产环境配置
├── src                         源码目录
|   ├── pages                   页面文件目录
|   |   └── index               index 页面目录
|   |       ├── index.js        index 页面逻辑
|   |       ├── index.css       index 页面样式
|   |       └── index.config.js index 页面配置
|   ├── app.js                  项目入口文件
|   ├── app.css                 项目总通用样式
|   ├── app.config.js           项目入口配置
|   └── index.html              网页入口文件
├── project.config.json         微信小程序项目配置 project.config.json
├── project.tt.json             字节跳动小程序项目配置 project.config.json
├── project.swan.json           百度小程序项目配置 project.swan.json
├── project.qq.json             QQ 小程序项目配置 project.config.json
├── babel.config.js             Babel 配置
├── tsconfig.json               TypeScript 配置
├── .eslintrc                   ESLint 配置
└── package.json
```
其中 `src/app.css`跟你选择的预编译器有关，如果选择了预编译器，则为对应的预编译器后缀：

- less：`app.less`
- sass：`app.scss`
- stylus：`app.styl`

源码目录结构如下：
```bash
└── src                         源码目录
    └── pages                   页面文件目录
        └── index               index 页面目录
            ├── index.js        index 页面逻辑
            ├── index.css       index 页面样式
            └── index.config.js index 页面配置
```
源码目录也跟框架、预编译器有关。页面逻辑后缀可以是 `js`、`jsx`、`vue`；页面样式后缀可以是 `css`、`less`、`scss`、`styl`。


<a name="TFujG"></a>
## 三、taro配置
编译配置存放于项目根目录下的 config 目录中，包含三个文件：

- `index.js` 是通用配置
- `dev.js` 是项目预览时的配置
- `prod.js` 是项目打包时的配置

常用配置：
```bash
sourceRoot // 源码存放目录。默认src
outputRoot // 代码编译后的生产目录。默认dist
designWidth // 设计稿尺寸。默认750

defineConstants // 用于配置一些全局变量供代码中进行使用。
alias // 用于配置目录别名，从而方便书写代码引用路径。
env // 设置环境变量。

plugins // 配置 Taro 插件。
presets // 一个 preset 是一系列 Taro 插件的集合
copy // 用于把文件从源码目录直接拷贝到编译后的生产目录。

### 编译器配置
terser # 压缩 JS 代码
csso # 压缩 CSS 代码
sass # 用于控制对 scss 代码的编译行为

### 平台配置
mini # 小程序配置
h5 # h5配置
rn # 让你配置
```
参考：[编译配置详情](https://taro-docs.jd.com/taro/docs/config-detail)

<a name="j6Sbb"></a>
## 四、taro开发(Vue)
<a name="gU1s0"></a>
### 路由
在使用路由前，需将页面添加到`app.config.js`的pages中：
```javascript
export default {
  pages: [
    'pages/index/index',
    'pages/test/test'
  ]
}
```
路由方法包括：

- [navigateTo](https://taro-docs.jd.com/taro/docs/apis/route/navigateTo)
- [redirectTo](https://taro-docs.jd.com/taro/docs/apis/route/redirectTo)
- [navigateBack](https://taro-docs.jd.com/taro/docs/apis/route/navigateBack)
- [switchTab](https://taro-docs.jd.com/taro/docs/apis/route/switchTab)
- [reLaunch](https://taro-docs.jd.com/taro/docs/apis/route/reLaunch)

示例：
```vue
<template>
	<view @click="go">go</view>
</template>

<script>
import Taro from '@tarojs/taro'

export default {
  methods: {
    go() {
      Taro.navigateTo({
        url: '/pages/index/index?a=1&b=2'
      })
    }
  }
}
</script>
```

<a name="NZLar"></a>
#### 获取路由参数
比如访问如下地址：[/pages/index/index?a=1&b=2](/pages/index/index?a=1&b=2) ，要获取路由参数，通过以下方式：
```javascript
import Taro from '@tarojs/taro'

export default {
  created() {
    let instance = Taro.getCurrentInstance()
    console.log(instance.router.params)
  }
}
```
打印：
```css
{a: '1', b: '2'}
```

参考：

- [路由功能](https://taro-docs.jd.com/taro/docs/router)
- [navigateTo](https://taro-docs.jd.com/taro/docs/apis/route/navigateTo)

<a name="CRwQ9"></a>
#### EventChannel
[📃 跨页面数据传递](https://www.yuque.com/xiaoyulive/weixinminiapp/nwhywh?view=doc_embed&inner=CN6Ox)

<a name="kvFSD"></a>
### 全局变量
[📃 跨页面数据传递](https://www.yuque.com/xiaoyulive/weixinminiapp/nwhywh?view=doc_embed&inner=sJbmm)

<a name="iNdRs"></a>
### 使用taro（Vue版本）的注意事项

1. 点击事件必须使用 `@tap`。
2. 在Vue中使用jsx时，事件名称的首字母需要大写，例如`onGetphonenumber`。
3. 小程序中不支持 <style scoped>，建议使用 cssModules 代替。
4. 所有组件的 id 必须在整个应用中保持唯一（即使他们在不同的页面），否则可能导致事件不触发的问题。

参考：

- [Taro Vue版本规范](https://taro-docs.jd.com/taro/docs/vue-overall#taro-%E8%A7%84%E8%8C%83-1)
- [Taro Vue版本注意事项](https://taro-docs.jd.com/taro/docs/vue-overall#%E5%85%B6%E5%AE%83%E9%99%90%E5%88%B6)

<a name="j3UXr"></a>
## 五、taro开发(React)





<a name="Tbva6"></a>
## 六、开发技巧及注意事项
<a name="HZaXs"></a>
### CSS 编译时忽略（过滤）
<a name="J53zP"></a>
#### 忽略单个属性
当前忽略单个属性的最简单的方法，就是 px 单位使用大写字母。
```css
/* `px` is converted to `rem` */
.convert {
  font-size: 16px; // converted to 1rem
}

 /* `Px` or `PX` is ignored by `postcss-pxtorem` but still accepted by browsers */
.ignore {
  border: 1Px solid; // ignored
  border-width: 2PX; // ignored
}
```

<a name="Ov6cM"></a>
#### 忽略样式文件
对于头部包含注释 `/*postcss-pxtransform disable*/`的文件，插件不予处理。

<a name="obYRY"></a>
#### 忽略样式举例
样式文件里多行文本省略时我们一般如下面的代码：
```css
.textHide {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp:2;
  text-overflow: ellipsis;
  overflow: hidden;
}
```
但 Taro 编译后少了 `-webkit-box-orient: vertical;`这条样式属性，此时我们需要忽略掉这条样式。

**忽略样式方法 1：加入 CSS 注释强制声明忽略下一行**
```css
/* autoprefixer: ignore next */
-webkit-box-orient: vertical;
```

**忽略样式方法 2：加入 CSS 注释强制声明注释中间多行**
```css
/* autoprefixer: off */
-webkit-box-orient: vertical;
/* autoprefixer: on */
```

**忽略样式方法 3：写成行内样式**
```css
<View 
  style={{
    display: '-webkit-box',
    '-webkit-box-orient': 'vertical',
    '-webkit-line-clamp': 2,
    'text-overflow': 'ellipsis',
    overflow: 'hidden',
    'line-height': 2
  }}
>
  这是要省略的内容这是要省略的内容这是要省略的内容
</View>
```
参考：

- [CSS 编译时忽略（过滤）](https://taro-docs.jd.com/taro/docs/size/#css-%E7%BC%96%E8%AF%91%E6%97%B6%E5%BF%BD%E7%95%A5%E8%BF%87%E6%BB%A4)
- [Taro多行文本省略不生效](https://taro-club.jd.com/topic/2270/taro%E5%A4%9A%E8%A1%8C%E6%96%87%E6%9C%AC%E7%9C%81%E7%95%A5%E4%B8%8D%E7%94%9F%E6%95%88)


<a name="dfY66"></a>
### CLI与项目版本问题
有的时候，编译的时候会失败，很有可能是因为CLI版本与项目版本不一致。

使用以下命令确保CLI与项目taro版本一致：
```javascript
# 使用Taro 升级命令更新CLI版本到最新版本
$ taro update self
# 使用Taro 升级命令将项目依赖升级到与@tarojs/cli一致的版本
$ taro update project 

# 使用Taro 升级命令更新CLI版本到指定版本
$ taro update self [版本号]
# 使用Taro 升级命令将项目依赖升级到指定版本
$ taro update project [版本号]
```

参考：[保持 CLI 的版本与各端依赖版本一致](https://taro-docs.jd.com/taro/docs/GETTING-STARTED#%E4%BF%9D%E6%8C%81-cli-%E7%9A%84%E7%89%88%E6%9C%AC%E4%B8%8E%E5%90%84%E7%AB%AF%E4%BE%9D%E8%B5%96%E7%89%88%E6%9C%AC%E4%B8%80%E8%87%B4)

