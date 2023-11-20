- [官网：Pug模板引擎中文文档](https://www.pugjs.cn/api/getting-started.html)

<a name="mUU2A"></a>
## Pug常规语法
常见规则：

- 标签直接以标签名命名
- 属性放于括号中
- 标签内容打空格放于其后
- ID以`#`开始
- 类名以`.`开始
- 注释以 `//` （会编译到HTML）或 `//-` （不会编译到HTML）开始
- 多行文本以 `|` 开始
- 文本块在标签后以 `.` 结尾，其后缩进的所有行均为文本块
- 事件名称使用 `()` 包裹

示例：
```vue
<template lang="pug">
div
	//- 这是一个按钮
	input.button#btn(type='button' (click)='play()') click me
</template>
```

<a name="cWpJU"></a>
### &attributes
&attributes 语法可以将一个对象转化为一个元素的属性列表。

示例：
```vue
div(data-bar="foo")&attributes({'data-foo': 'bar'})
```
编译结果：
```vue
<div data-bar="foo" data-foo="bar"></div>
```






<a name="Emvjn"></a>
## Pug在Vue中使用的思考与总结
<a name="PiTbz"></a>
### Pug Mixin只能是模板传值
如果在Pug中使用到了Mixin，是只能在模板之间共享数据的，而不能在Vue中使用。

举例：
```vue
<template lang="pug">
view
  mixin text(name)
    view= name
  view(v-for='(item, index) in 10', :key='index'): +text('hello')
</template>
```
这里，mixin接收一个name的变量，可以通过 `=` 渲染出此数据。

然而，如果想将此name暴露到Vue中（比如通过方法传值）：
```vue
<template lang="pug">
view
  mixin text(name)
    view(@click='test(name)')= name
  view(v-for='(item, index) in 10', :key='index'): +text('hello')
</template>

<script>
export default {
  methods: {
    test(item) {
      console.log(item)
    }
  }
}
</script>
```
点击后，控制台中报警告：
```vue
[Vue warn]: Property or method "name" is not defined on the instance but referenced during render. Make sure that this property is reactive, either in the data option, or for class-based components, by initializing the property. See: https://vuejs.org/v2/guide/reactivity.html#Declaring-Reactive-Properties.
```



