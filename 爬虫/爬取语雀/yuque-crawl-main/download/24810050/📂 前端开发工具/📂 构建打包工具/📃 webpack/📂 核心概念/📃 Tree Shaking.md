tree shaking 是一个术语，通常用于描述移除 JavaScript 上下文中的未引用代码(dead-code)。这个词是由最先从[Rollup](https://github.com/rollup/rollup#tree-shaking)社区开始流行的，不过本身的理念很早就有了。

“tree shaking”这个词来自于应用的架构以及本身的依赖关系就像一个树形结构。树的每一个节点表示应用中一个唯一的功能。在现代网页应用中，依赖关系通常使用static import statement

```javascript
// Import all the array utilities!
import arrayUtils from "array-utils";

// or
import * as utils from "../../utils/utils";
```

当你的app还很小的时候，也许只有很少的依赖文件。而且应该几乎使用了所有你自己添加的依赖。但是，当你的app开发了一段时间，越来越多的依赖添加进去。由于各种原因，旧的依赖可能根本没有使用了，但是呢依然在你的代码库里面，没有被删除。最终导致你的app夹带了很多并没有使用的JavaScript。通过分析我们如何使用import语句，tree shaking会移除无用代码。

```javascript
// Import only some of the utilities!
import { unique, implode, explode } from "array-utils";
```

这个import语句和之前的区别在于，与其引入整个array-utils，而整个array-utils可能有非常多的函数，不如只引入我们需要的部分。在开发构建的时候，这两种使用方法并没有区别。但是在生产打包的时候，我们可以配置webpack来剔除不需要的函数，使得整个代码文件变小。在这篇文章中，我们会指导你如何做。

<a name="a35f238f"></a>
## 配置 tree shaking
> 「副作用」的定义是，在导入时会执行特殊行为的代码，而不是仅仅暴露一个 export 或多个 export。举例说明，例如 polyfill，它影响全局作用域，并且通常不提供 export。


如果所有代码都不包含副作用，我们就可以简单地将该属性标记为 false，来告知 webpack，它可以安全地删除未用到的 export 导出。
```javascript
module.exports = {
  ...
  module: {
    rules: [
      {
        sideEffects: false
      }
    ]
  }
};
```

如果某些文件包含副作用，需要将 sideEffects 指定为一个数组，把有副作用的文件列举出来
```javascript
module.exports = {
  ...
  module: {
    rules: [
      {
        sideEffects: [
          "./src/some-side-effectful-file.js",
          "*.css"
        ]
      }
    ]
  }
};
```

<a name="8dfc7c16"></a>
## 依赖库
某些依赖库, 比如 lodash 并不会如期地做 tree shaking, 因为Lodash的架构就不支持, 这里分几种情况讨论

情况一：只是引入而不使用
```javascript
import { last } from 'lodash'
// or
import _ from 'lodash'
```

这样使用 webpack 打包后将剔除 lodash (配置了tree shaking且的情况, 如果没有配置tree shaking仍然会包含整个lodash包)

情况二：引入后使用, 即使只是引入部分
```javascript
import { last } from 'lodash'

last([1,2,3])
```

这样的话，webpack 打包时仍然会包含完整的 lodash 依赖包

---

有以下几种解决方案：

方式一：使用分包引入的方式
```javascript
import last from "lodash/last";
```

方式二: 自己编写 Babel 插件, 参考我的另一篇文章 [编写 Babel 插件](/books/babel/write_plugin.html#%E7%A4%BA%E4%BE%8B%EF%BC%9A%E5%8C%85%E5%BC%95%E5%85%A5%E6%9B%BF%E6%8D%A2)

方法三: 使用 Babel 插件 [babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash)
```bash
yarn add -D babel-plugin-lodash
```

配置：<br />
```json
{
  "plugins": ["lodash"],
  "presets": ["@babel/env"]
}
```

Transforms
```javascript
import _ from 'lodash'
import { add } from 'lodash/fp'

const addOne = add(1)
_.map([1, 2, 3], addOne)
```

roughly to
```javascript
import _add from 'lodash/fp/add'
import _map from 'lodash/map'

const addOne = _add(1)
_map([1, 2, 3], addOne)
```

<a name="CommonJS"></a>
## CommonJS
如果有些模块使用CommonJS格式(`module.exports`)，那么webpack无法使用tree shaking。

如果使用了 `babel-preset-env`，它会将你的ES6编译到可兼容性更好的CommonJS，这时只需要配置：
```json
{
  "presets": [
    ["env", {
      "modules": false
    }]
  ]
}
```

简单地配置 `"modules":false` 即可，webpack会分析所有文件中模块的依赖关系，然后剔除那些没有使用的代码。并且，这个处理不会有兼容问题，因为webpack最终会将代码转换到兼容的版本。

一些插件也可以帮助我们做 CommonJS 的 tree shaking, 比如 [webpack-common-shake](https://github.com/indutny/webpack-common-shake), 使用方式如下：
```bash
yarn add -D webpack-common-shake
```

```javascript
const ShakePlugin = require('webpack-common-shake').Plugin;

module.exports = [{
  ...
  plugins: [ new ShakePlugin() ]
}];
```

<a name="35808e79"></a>
## 参考资料

- [tree shaking](https://www.webpackjs.com/guides/tree-shaking/)
- [Allow app authors to force libraries into sideEffects: `false`](https://github.com/webpack/webpack/issues/065#issuecomment-351060570)
- [配置Tree Shaking来减少JavaScript的打包体积](https://www.cnblogs.com/fundebug/archive/2018/08/15/reduce_js_payload_with_tree_shaking.html)
