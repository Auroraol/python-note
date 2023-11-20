<a name="S51kR"></a>
## Assemblyscript简介
**AssemblyScript** 是一个 **TypeScript** 到 **WebAssembly** 的编译器。

Assemblyscript官网：<br />[AssemblyScript](https://www.assemblyscript.org/)<br />WebAssemble官网：<br />[WebAssembly](https://webassembly.org/)<br />WebAssemble - MDN：<br />[WebAssembly - JavaScript | MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly)

<a name="m7p4d"></a>
## 使用脚手架创建Assemblyscript项目
首先创建一个目录用来存放AssemblyScript项目，再进入此目录执行以下命令：
```javascript
mkdir AssembleScriptDemos
cd AssembleScriptDemos
npm init
npm install --save @assemblyscript/loader
npm install --save-dev assemblyscript
```
初始化此项目：
```javascript
npx asinit .
```
编译：
```javascript
npm run asbuild
```
运行测试：
```javascript
npm test
```
不出意外，控制台输出：`ok`

**项目目录解析**

- `assembly`存放AssembleScript的源码，入口文件是`index.ts`文件
- `build`编译路径，生成`untouched.wasm`和`optimized.wasm`
- `tests`测试文件路径
- `asconfig.json`AssembleScript配置文件
- `index.js`入口文件
- `package.json`项目包配置

<a name="IGks1"></a>
## 编译AssembleScript并测试
修改`assembly/index.ts`：
```typescript
export function fib(n: i32): i32 {
  var a = 0, b = 1
  if (n > 0) {
    while (--n) {
      let t = a + b
      a = b
      b = t
    }
    return b
  }
  return a
}

export function add(a: i32, b: i32): i32 {
  return a + b;
}

export function sub(a: i32, b: i32): i32 {
  return a - b;
}
```
修改`tests/index.js`：
```typescript
const assert = require("assert");
const myModule = require("..");

let res = myModule.add(1, 2)
console.log(res)

assert.strictEqual(res, 3);
console.log("ok");

res = myModule.sub(1, 2)
console.log(res)

res = myModule.fib(10)
console.log(res)
```
其中`myModule`是入口文件`index.js`
```typescript
const fs = require("fs");
const loader = require("@assemblyscript/loader");
const imports = {};
const wasmModule = loader.instantiateSync(fs.readFileSync(__dirname + "/build/optimized.wasm"), imports);
module.exports = wasmModule.exports;
```
可以看到，引入了`optimized.wasm`，并将其导出。

编译：
```typescript
npm run asbuild
```

运行测试：
```typescript
npm test
```
不出意外，控制台输出：
```typescript
3
ok
-1
55
```

<a name="VEJFy"></a>
## 在html中加载wasm
通过运行命令`npm run asbuild`后，会在 `build`目录生成`optimized.wasm`文件，如果想要在html中引入，可以通过以下几种方式。

方式一：通过fetch引入
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    async function fetchAndInstantiate() {
      const response = await fetch("./build/optimized.wasm");
      const buffer = await response.arrayBuffer();
      const obj = await WebAssembly.instantiate(buffer);

      let exports = obj.instance.exports;

      console.log(exports.add(1, 2));
      console.log(exports.sub(1, 2));
      console.log(exports.fib(10));
    }

    fetchAndInstantiate()
  </script>
</body>
</html>
```

方式二：通过loader引入（ESM方式）
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script type="module">
    import loader from "https://cdn.jsdelivr.net/npm/@assemblyscript/loader/index.js";
    loader.instantiate(
      // Binary to instantiate
      fetch("./build/optimized.wasm"),
    ).then(({ exports }) => {
      console.log(exports.add(1, 2))
      console.log(exports.sub(1, 2))
      console.log(exports.fib(10))
    })
  </script>
</body>
</html>
```

方式三：通过loader引入（UMD方式）
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <!-- UMD -->
  <script src="https://cdn.jsdelivr.net/npm/@assemblyscript/loader/umd/index.js"></script>
</head>
<body>
  <script>
    // import loader from "@assemblyscript/loader"; // or require
    loader.instantiate(
      // Binary to instantiate
      fetch("./build/optimized.wasm"),
    ).then(({ exports }) => {
      console.log(exports.add(1, 2))
      console.log(exports.sub(1, 2))
      console.log(exports.fib(10))
    })
  </script>
</body>
</html>
```

参考：[Using the loader](https://www.assemblyscript.org/loader.html)



<a name="ptfZI"></a>
## 参考资料

- [Wasm 为 Web 开发带来无限可能](https://mp.weixin.qq.com/s/6dHxBZcZk8905nvSsjz67A)
- [awesome-wasm-zh](https://github.com/chai2010/awesome-wasm-zh)
- [awesome-wasm](https://github.com/mbasso/awesome-wasm)

