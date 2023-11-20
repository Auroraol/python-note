经验证发现，**在最新的vue-cli脚手架项目中，是可以直接使用装饰器的**。

<a name="JZSz4"></a>
## 在较老的vue-cli脚手架项目中
如果是比较老的vue项目，可以通过以下方式添加装饰器支持。

1. 安装babel插件：`@babel/plugin-proposal-decorators`
```javascript
yarn add -D @babel/plugin-proposal-decorators
```
参考：[@babel/plugin-proposal-decorators](https://babel.docschina.org/docs/en/babel-plugin-proposal-decorators/)

2. 编辑器配置

如果是VSCode编辑器，需要开启`experimentalDecorators`选项：<br />![Snipaste_2021-11-17_11-47-52.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1637120917715-17177101-c606-4f60-996e-0aa96dbde210.webp#clientId=u44e3fde9-295e-4&from=drop&id=H2rSI&originHeight=172&originWidth=987&originalType=binary&ratio=1&size=11860&status=done&style=none&taskId=ud8778b03-6360-4daf-b6b5-0ded2084bf0)

3. 在`babel.config.js`中配置
```javascript
module.exports = {
  ...
  plugins: [
    ['@babel/plugin-proposal-decorators', { legacy: true }]
  ]
}
```
或者在`packages.json`中添加：
```javascript
{
  ...
  babel: {
    "plugins": [
      ["@babel/plugin-proposal-decorators", { "legacy": true }],
    ]
  }
}
```

注意，一定要加`{ legacy: true }`，否则编译时会报错：
```javascript
Error: The 'decorators' plugin requires a 'decoratorsBeforeExport' option, whose value must be a boolean. If you are migrating from Babylon/Babel 6 or want to use the old decorators proposal, you should use the 'decorators-legacy' plugin instead of 'decorators'
```
```javascript
Parsing error: Decorators cannot be used to decorate object literal properties
```

4. 在eslint中配置

在`.eslintrc.js`中添加此节点
```javascript
module.exports = {
  ...
  parserOptions: {
    ecmaFeatures: {
      // 支持装饰器
      legacyDecorators: true
    }
  },
}
```

5. 在项目中使用

随后，就能在vue中使用了
```vue
<template>
  <div id="app">
  </div>
</template>

<script>
function log(target) {
  console.log('log: ', target)
}

export default {
  @log
  created() {
    console.log('created')
  },
}
</script>

<style>
</style>
```
控制台打印：<br />![Snipaste_2021-11-17_11-51-12.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1637121527723-9c7db4bf-9aaf-4da2-9337-50827b91a32c.png#clientId=u44e3fde9-295e-4&from=drop&id=ubeb9129b&originHeight=66&originWidth=356&originalType=binary&ratio=1&size=3866&status=done&style=none&taskId=u1b47481b-ee8d-4e1f-a7b6-d1f779c718d)


<a name="mrlip"></a>
## 在vite项目中











