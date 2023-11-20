<a name="b9f1abde"></a>
## 上下文模块 API
这是我最喜欢的功能之一, 通过 `require.context` 我们可以批量引入某些文件(比如一个目录下的所有js)
```javascript
var cache = {};

function importAll (r) {
  r.keys().forEach(key => cache[key] = r(key));
}

importAll(require.context('../components/', true, /\.js$/));
// 在构建时，所有被 require 的模块都会被存到（上面代码中的）cache 里面。
```

require.context 的参数

- 第一个参数为基础目录位置
- 第二个参数, 为 false 的话不包含子目录, 为 true 的话包含子目录
- 第三个参数为要解析的文件

我曾通过这个API, 引入 Vue 项目下整个目录的库、组件、插件等, 参见我的另一篇文章 [Vue组件及库的自动注入](/books/vue/injection.html)


