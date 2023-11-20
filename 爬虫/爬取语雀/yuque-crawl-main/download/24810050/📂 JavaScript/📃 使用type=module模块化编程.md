<a name="csFyn"></a>
## 一、在Script中引用ES6模块
<a name="taDR2"></a>
### 通过import...from引入
比如有如下index.js模块：
```javascript
export default {
  hello() {
    console.log('hello')
  }
}
```
引入：
```html
<html>
<body>
  <script type="module">
    import test from './index.js'
    test.hello()
  </script>
</body>
</html>
```

<a name="qVE8f"></a>
### 在script标签中引入
```html
<script type="module" src="./index.js"></script>
```
注意，必须开启WebServer才能正常访问。如果直接双击打开，会报CORS跨域：
```html
Access to script at 'file:///D:/test/index.js' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, chrome-extension, edge, https, chrome-untrusted.
```

<a name="BBM4i"></a>
## 二、加载远程资源
`type="module"`可以通过HTTP请求的方式直接加载远程资源：
```html
<html>
  <body>
    <script type="module">
      import { createSignal, onCleanup } from "https://cdn.skypack.dev/solid-js";
      import { render } from "https://cdn.skypack.dev/solid-js/web";
      import html from "https://cdn.skypack.dev/solid-js/html";

      const App = () => {
        const [count, setCount] = createSignal(0),
          timer = setInterval(() => setCount(count() + 1), 1000);
        onCleanup(() => clearInterval(timer));
        return html`<div>${count}</div>`;
      };
      render(App, document.body);
    </script>
  </body>
</html>
```
跟普通的script不同, module script (以及它们的 imports 行为) 受 CORS 跨域资源共享限制。也就是说，跨域的 module scripts 必须返回带有有效 `Access-Control-Allow-Origin: *` 的CORS头信息。

<a name="WgocU"></a>
## 三、有效的module路径定义
因为是在浏览器端的实现，不会像在node中，有全局module一说（全局对象都在window里了）。<br />所以说，from "XXX"这个路径的定义会与之前你所熟悉的稍微有些出入。<br /> <br />下面几种 module 路径语法是有效的：

- 绝对路径的URL。也就是说，使用 `new URL`(模块地址) 也不会报错。
- 远程服务器资源地址，`http://`、`https://` 等开头的。
- 地址开头是 `/`。
- 地址开头是 `./`。
- 地址开头是 `../`。

示例：
```javascript
// 被支持的几种路径写法
import module from "http://XXX/module.js"
import module from "/XXX/module.js"
import module from "./XXX/module.js"
import module from "../XXX/module.js"

// 不被支持的写法
import module from "XXX"
import module from "XXX/module.js"
```

在webpack打包的文件中，引用全局包是通过`import module from "XXX"`来实现的。这个实际是一个简写，webpack会根据这个路径去`node_modules`中找到对应的module并引入进来。<br />但是原生支持的module是不存在node_modules一说的。

所以，在使用原生module的时候一定要切记，from后边的路径一定要是一个有效的URL，以及一定不能省略文件后缀（是的，即使是远端文件也是可以使用的，而不像webpack需要将本地文件打包到一起）。


<a name="d4E54"></a>
## 四、一个模块只执行一次
比如`index.js` 中打印：
```html
console.log('hello')
```
在html中引入了三次此脚本
```html
  <script type="module" src="./index.js"></script>
  <script type="module" src="./index.js"></script>
  <script type="module" src="./index.js"></script>
```
实际在浏览器中控制台只会打印一次。


而普通的脚本引入会多次执行：
```html
  <script src="./index.js"></script>
  <script src="./index.js"></script>
  <script src="./index.js"></script>
```
这会在浏览器控制台打印三次。

<a name="sbBgW"></a>
## 五、脚本异步加载
在script标签上加入async属性，可以异步加载脚本，不阻碍DOM解析。
```html
<!-- 这个脚本将会在import完成后立即执行 -->
<script async type="module">
  import test from './index.js';
  test.hello()
</script>

<!-- 这个脚本将会在脚本加载和import完成后立即执行 -->
<script async type="module" src="index.js"></script>
```

<a name="KbqNl"></a>
## 六、nomodule降级处理
这里有一个类似于`noscript`标签的存在。<br />可以在script标签上添加`nomodule`属性来实现一个回退方案。
```html
<script type="module">
  import module from "./module.js"
</script>
<script nomodule>
  alert("your browsers can not supports es modules! please upgrade it.")
</script>
```
nomodule的处理方案是这样的： 支持`type="module"`的浏览器会忽略包含nomodule属性的script脚本执行。<br />而不支持type="module"的浏览器则会忽略type="module"脚本的执行。

这是因为浏览器默认只解析`type="text/javascript"`的脚本，而如果不填写type属性则默认为text/javascript。

也就是说在浏览器不支持module的情况下，nomodule对应的脚本文件就会被执行。

<a name="hV7CG"></a>
## 七、module的文件默认为defer
这是script的另一个属性，用来将文件标识为不会阻塞页面渲染的文件，并且会在页面加载完成后按照文档的顺序进行执行。
```html
<script type="module" src="./defer/module.js"></script>
<script src="./defer/simple.js"></script>
<script defer src="./defer/defer.js"></script>
```

为了测试上边的观点，在页面中引入了这样三个JS文件，三个文件都会输出一个字符串，在Console面板上看到的顺序是这样的：<br />![](https://cdn.nlark.com/yuque/0/2021/png/2213540/1635301743786-ccb73f83-3d6e-4e72-bd85-46ede553023b.png#clientId=ua63baa26-42f7-4&from=paste&id=u520dc9ae&originHeight=644&originWidth=2058&originalType=url&ratio=1&status=done&style=none&taskId=u10506665-aa9b-493e-93b6-58b0b738197)

<a name="cRIZe"></a>
### 行内script也会默认添加defer特性
因为在普通的脚本中，defer关键字是只指针对脚本文件的，如果是`inline-script`，添加属性是不生效的。<br />但是在`type="module"`的情况下，不管是文件还是行内脚本，都会具有defer的特性。

<a name="MoDlb"></a>
## 八、导出与导入重命名
在导入、导出某些模块时，也是可以使用`as`关键字来重命名你要导出的某个值。<br />导出：
```javascript
let name = "Niko"
let age = 18

export { name as firstName }
export { age }
```
导入：
```javascript
import {firstName, age as old} from "./index.js"
console.log(firstName, old)
```

<a name="qtacw"></a>
## 九、默认导出与导入
没有添加default的导出：
```javascript
let name = "Niko"
let age = 18

export {
	name as firstName,
  age
}
```
通过通配符 `*` 导入此模块中的所有（变量、函数、类等），并通过as重命名：
```javascript
import * as person from "./index.js"
console.log(person.firstName, person.age)
```

如果是通过`default`导出的：
```javascript
let name = "Niko"
let age = 18

export default {
	name,
  age
}
```
> 注意：使用default导出不支持使用as重命名。

导入的时候直接取个名即可：
```javascript
import person from "./index.js"
console.log(person.name, person.age)
```
或者：
```javascript
    import { default as person } from "./index.js"
    console.log(person.name, person.age)
```
或者：
```javascript
import p, { default as person } from "./index.js"
console.log(p.name, p.age)
console.log(person.name, person.age)
```

<a name="BAeen"></a>
## 十、导出索引文件
在某些地方可能会用到十个module，如果每次都import十个，肯定是一种浪费，视觉上也会给人一个不好的感觉。<br />所以你可能需要写一个类似`index.js`的文件，在这个文件中将其引入到一块，然后使用时`import index`即可。

将所有的module引入，并导出为一个Object，这样确实在使用时已经很方便了。<br />但是这个索引文件依然是很丑陋，所以可以用下面的语法来实现类似的功能：<br />`index.js`
```javascript
import a from './a.js'
import b from './b.js'

export default {
	a,
  b
}
export { default as a } from "./a.js"
export { default as b } from "./b.js"
```

引入：
```html
<script type="module">
  import index, { a, b } from "./index.js"
  index.a()
  index.b()
  a()
  b()
</script>
```


<a name="dutw3"></a>
## 参考资料

- [原生ES-Module <script type="module" >](https://www.yht7.com/news/92376)


