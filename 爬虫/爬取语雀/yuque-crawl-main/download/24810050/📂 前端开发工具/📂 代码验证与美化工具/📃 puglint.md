- 相关站点：[GitHub](https://github.com/pugjs/pug-lint)、[Rules](https://github.com/pugjs/pug-lint/blob/HEAD/docs/rules.md)、[NPM](https://www.npmjs.com/package/pug-lint)

<a name="sYFmY"></a>
## 安装和使用
安装：
```bash
yarn add -D pug-lint
```

支持的配置文件有：

- `.pug-lintrc` 
- `.pug-lintrc.js` 
- `.pug-lintrc.json` 
- 在 `package.json` 中配置 `"pugLintConfig"` 选项



添加默认配置规则：
```bash
yarn add -D pug-lint-config-clock
```
在配置文件中指定：
```bash
module.exports = {
  extends: "clock",
}
```

开始验证文件：
```bash
npx pug-lint index.pug
```

<a name="FoXry"></a>
## 常用配置项
配置示例：
```javascript
module.exports = {
  extends: "clock",
  validateIndentation: 2,
  validateLineBreaks: "CRLF",
  disallowClassAttributeWithStaticValue: true,
}
```
常用配置项：

- `validateIndentation`: `int` | `"\t"` 缩进空格数或指定为tab缩进
- `validateLineBreaks`: `"CR"` | `"LF"` | `"CRLF"` 指定换行符
- `disallowClassAttributeWithStaticValue`: `true` 不允许在属性列表中写class
- `disallowClassLiteralsBeforeIdLiterals`: `true` ID必须书写于class之前
- `disallowDuplicateAttributes`: `true` 不允许出现相同的属性
- `disallowMultipleLineBreaks`: `true` 不允许出现多行空格

<a name="d5V4A"></a>
## 验证Vue文件中的Pug模板
如果需要在Vue文件中开启pug验证，支持如下形式的模板：
```vue
<template lang="pug">
.contaiiner
  .header.text-white Hello
</template>
```

安装 [`pug-lint-vue`](https://www.npmjs.com/package/pug-lint-vue) [[GitHub](https://github.com/sourceboat/pug-lint-vue)]：
```vue
yarn add -D pug-lint-vue
```

验证命令：
```vue
npx pug-lint-vue index.vue
```

如果想要格式化，需要安装 [prettier-plugin-pug](https://github.com/prettier/plugin-pug)：
```vue
yarn add -D @prettier/plugin-pug
```


