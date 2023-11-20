<a name="8a95a6d1"></a>
## 结构
一个最基础的 Plugin 的结构是这样的：
```javascript
// 一个 JavaScript 命名函数。
function BasicPlugin() {

};

// 在插件函数的 prototype 上定义一个 `apply` 方法。
BasicPlugin.prototype.apply = function(compiler) {
  // 指定一个挂载到 webpack 自身的事件钩子。
  // 设置回调来访问 compilation 对象：
  compiler.plugin("compilation", function(compilation, callback) {
    console.log("This is an example plugin!!!");

    // 现在，设置回调来访问 compilation 中的步骤：
    compilation.plugin("optimize", function() {
      console.log("Assets are being optimized.");
    });

    // 功能完成后调用 webpack 提供的回调。
    callback();
  });
};

// 导出 Plugin
module.exports = BasicPlugin;
```

或者：<br />
```javascript
class BasicPlugin{
  // 在构造函数中获取用户给该插件传入的配置
  constructor(options){
  }

  // Webpack 会调用 BasicPlugin 实例的 apply 方法给插件实例传入 compiler 对象
  apply(compiler){
    compiler.plugin('compilation',function(compilation) {
      callback();
    })
  }
}

// 导出 Plugin
module.exports = BasicPlugin;
```

<a name="e655a410"></a>
## 安装
要安装这个插件，只需要在你的 webpack 配置的 plugin 数组中添加一个实例：
```javascript
var HelloWorldPlugin = require('./hello-world-plugin');

var webpackConfig = {
  // ... 这里是其他配置 ...
  plugins: [
    new HelloWorldPlugin({options: true})
  ]
};
```

<a name="d3082e69"></a>
## Compiler 和 Compilation
在开发 Plugin 时最常用的两个对象就是 Compiler 和 Compilation，它们是 Plugin 和 Webpack 之间的桥梁。

Compiler 和 Compilation 的含义如下：

- Compiler 对象包含了 Webpack 环境所有的的配置信息，包含 options，loaders，plugins 这些信息，这个对象在 Webpack 启动时候被实例化，它是全局唯一的，可以简单地把它理解为 Webpack 实例；
- Compilation 对象包含了当前的模块资源、编译生成资源、变化的文件等。当 Webpack 以开发模式运行时，每当检测到一个文件变化，一次新的 Compilation 将被创建。Compilation 对象也提供了很多事件回调供插件做扩展。通过 Compilation 也能读取到 Compiler 对象。<br />Compiler 和 Compilation 的区别在于：Compiler 代表了整个 Webpack 从启动到关闭的生命周期，而 Compilation 只是代表了一次新的编译。

<a name="35808e79"></a>
## 参考资料

- [编写一个插件](https://www.webpackjs.com/contribute/writing-a-plugin/)
- [Webpack原理-编写Plugin](https://segmentfault.com/a/1190000012840742)
