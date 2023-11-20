<a name="YpaAD"></a>
## 拖拽基础知识
<a name="Y7bLG"></a>
### 什么是拖拽
拖拽：Drag<br />释放：Drop<br />拖拽指的是鼠标点击源对象后一直移动对象不松手，一但松手即释放了。

<a name="D5OTU"></a>
### 可拖拽属性
将想要拖拽的元素的 [draggable](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes#attr-draggable) 属性设置成：
```javascript
 draggable="true"
```

举例：
```html
<div draggable="true" ondragstart="dragstart" ondrag="drag" ondragend="dragend">
  Drag me
</div>
```

<a name="lNxHp"></a>
### 源对象和目标对象
**源对象**：指的是我们鼠标点击的一个事物，这里可以是一张图片，一个DIV，一段文本等等。

**目标对象**：指的是我们拖动源对象后移动到一块区域，源对象可以进入这个区域，可以在这个区域上方悬停(未松手)，可以释松手释放将源对象放置此处(已松手)，也可以悬停后离开该区域。

<a name="B9zc5"></a>
### 拖拽事件
被拖动的源对象可以触发的事件：<br />(1)**ondragstart**：源对象开始被拖动<br />(2)**ondrag**：源对象被拖动过程中(鼠标可能在移动也可能未移动)<br />(3)**ondragend**：源对象被拖动结束

拖动源对象可以进入到上方的目标对象可以触发的事件：<br />(1)**ondragenter**：目标对象被源对象拖动着进入<br />(2)**ondragover**：目标对象被源对象拖动着悬停在上方<br />(3)**ondragleave**：源对象拖动着离开了目标对象<br />(4)**ondrop**：源对象拖动着在目标对象上方释放/松手


<a name="TzwN8"></a>
### 阻止默认事件
如果你想要允许放置，你必须取消 dragenter 、 dragover 、`ondrop` 事件来阻止默认的处理。你可以在属性定义的事件监听程序返回 false，或者调用事件的 `preventDefault()` 方法来实现这一点。
```html
<div ondragover="return false">
<div ondragover="event.preventDefault()">
```

如果是在页面中拖动，则设置document阻止默认事件
```javascript
document.ondragover = function(e){e.preventDefault()}
document.ondrop = function(e){e.preventDefault()}
```

<a name="Wv5Mq"></a>
### 获取拖拽对象
在事件绑定中通过`this`或`event.target`获取拖拽对象（看事件绑定到源对象还是目标对象，对应获取的就是源对象或目标对象）。

在源对象中获取的就是当前拖拽的源对象：
```javascript
let source = document.querySelector('.source'),
source.addEventListener('dragstart',function(event){
  console.log(this === event.target) // true
},false);
```
在目标对象中获取的就是当前拖拽的目标对象：
```javascript
let target = document.querySelector('.target'),
target.addEventListener('drop',function(event){
  console.log(this === event.target) // true
},false);
```

> 注意：在Vue中不能使用this获取拖拽对象，this会获取到当前Vue组件实例



<a name="QTgIz"></a>
### 拖拽数据传递
HTML5为所有的拖动相关事件提供了一个新的属性：
```javascript
e.dataTransfer // 数据传递对象
```
功能：用于在源对象和目标对象的事件间传递数据<br />  

源对象上的事件处理中保存数据：
```javascript
e.dataTransfer.setData(k, v); // k-v必须都是string类型
```

目标对象上的事件处理中读取数据：
```javascript
let v = e.dataTransfer.getData(k);
```


<a name="dHorN"></a>
## 单元素拖动
将单一元素在页面中拖动，只需要监听源对象的三个事件，在drag事件中实时更新元素的位置即可。

示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/GRmQzWj)<br />源码：
```html
<template>
<div class="source-box">
  <div draggable="true" @dragstart="dragstart" @drag="drag" @dragend="dragend" class="source" data-index="1"></div>
</div>
</template>

<script>
document.ondragover = function(e){e.preventDefault()}
document.ondrop = function(e){e.preventDefault()}
export default {
  data() {
    return {
      offsetX: 0,
      offsetY: 0
    }
  },
  methods: {
    dragstart(e) {
      this.offsetX= e.offsetX;
      this.offsetY= e.offsetY;
    },
    drag(e) {
      let x = e.pageX
      let y = e.pageY
      // drag事件最后一刻，无法读取鼠标的坐标，pageX和pageY都变为0
      if(x === 0 && y === 0) {
        return // 不处理拖动最后一刻X和Y都为0的情形
      }
      x -= this.offsetX
      y -= this.offsetY

      let element = e.target
      element.style.left= x + 'px'
      element.style.top= y + 'px'
    },
    dragend(e) {
      console.log('dragend')
      console.log(e)
    },
  }
}
</script>

<style>
.source-box {
  position: relative;
  width: 100%;
  height: 100%;
}

.source {
  position: absolute;
  width: 200px;
  height: 200px;
  background-color: red;
  top: 0;
  left: 0;
}
</style>
```


<a name="ykI0q"></a>
## 拖拽到目标元素
在页面中存在源对象与目标对象，源对象传递数据，目标对象接收数据，并对数据进行处理。

> 只有在drop事件中可以获取到传递的数据


<a name="rHUjw"></a>
### 拖拽移动、复制、删除
思路：<br />**移动**：获取到源对象和目标对象，使用appendChild将源对象添加到目标对象中<br />**复制**：获取到源对象和目标对象，使用cloneNode克隆出一个与源对象相同的对象，再使用appendChild将源对象添加到目标对象中<br />**删除**：获取到源对象及其父节点，通过父节点的removeChild方法删除此DOM

示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/MWmQKOO)<br />源码：
```vue
<template>
<div>
  <div class="source-box">
    <div draggable="true" @dragstart="dragstart" @drag="drag" @dragend="dragend" class="source" data-index="1">源1</div>
    <div draggable="true" @dragstart="dragstart" @drag="drag" @dragend="dragend" class="source" data-index="2">源2</div>
    <div draggable="true" @dragstart="dragstart" @drag="drag" @dragend="dragend" class="source" data-index="3">源3</div>
    <div draggable="true" @dragstart="dragstart" @drag="drag" @dragend="dragend" class="source" data-index="4">源4</div>
  </div>
  <div class="target-box">
    <div @dragenter="dragenter" @dragleave="dragleave" @dragover="dragover" @drop="drop1" class="target">目标1: 移动</div>
    <div @dragenter="dragenter" @dragleave="dragleave" @dragover="dragover" @drop="drop2" class="target">目标2: 复制</div>
    <div @dragenter="dragenter" @dragleave="dragleave" @dragover="dragover" @drop="drop3" class="target">目标3: 删除</div>
  </div>
</div>
</template>

<script>
/* eslint-disable */
export default {
  methods: {
    dragstart(e) {
      console.log('dragstart')
      console.log(e)
      e.dataTransfer.dropEffect = "copy";
      e.dataTransfer.setData('index', e.target.dataset.index)
    },
    drag(e) {
      // console.log('drag')
      // console.log(e)
    },
    dragend(e) {
      console.log('dragend')
      console.log(e)
    },
    dragenter(e) {
      console.log('dragenter')
      console.log(e)
    },
    dragleave(e) {
      console.log('dragleave')
      console.log(e)
    },
    dragover(e) {
      // console.log('dragover')
      // console.log(e)
      event.preventDefault()
      return false
    },
    drop1(e) {
      console.log('drop')
      console.log(e)
      // 只有drop事件的时候可以获取到传递的数据
      let index = e.dataTransfer.getData('index')
      let element = document.querySelector(`.source-box > .source:nth-child(${index})`)
      e.target.appendChild(element)
    },
    drop2(e) {
      let index = e.dataTransfer.getData('index')
      let element = document.querySelector(`.source-box > .source:nth-child(${index})`)
      let elementClone = element.cloneNode(true)
      e.target.appendChild(elementClone)
    },
    drop3(e) {
      let index = e.dataTransfer.getData('index')
      let element = document.querySelector(`.source-box > .source:nth-child(${index})`)
      element.parentNode.removeChild(element)
    },
  }
}
</script>

<style>
.source-box, .target-box {
  display: flex;
}

.source {
  width: 200px;
  height: 200px;
  background-color: red;
  margin-top: 20px;
  margin-right: 20px;
}

.target {
  width: 300px;
  height: 300px;
  background-color: #ccc;
  margin-top: 20px;
  margin-right: 20px;
}
</style>
```

<a name="Zp0j0"></a>
### 拖拽排序
思路：

- 在一个列表中，每个元素都可以被拖放，那首先要给每个元素设置 draggable 属性为 true。
- 监听每个元素的 dragstart 事件，对源对象做样式处理来区分。
- 监听每个元素的 dragenter 事件，当源对象进入到当前元素里，就把源对象添加到该元素之前。这样后面的元素就会被源对象挤下去了，实现了排序的效果。
- 但是会发现，源对象无法排到最后一个去，只能在倒数第二。这时就要监听 dragleave 事件，当过程对象是最后一个元素时，源对象离开了过程对象，这时就把源对象添加到最后去。

示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/zYwWPMK)

源码：
```vue
<template>
<ul class="list">
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目1</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目2</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目3</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目4</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目5</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目6</li>
  <li class="item" draggable="true" @dragstart="dragstart" @dragend="dragend" @dragenter="dragenter" @dragleave="dragleave">项目7</li>
</ul>
</template>

<script>
document.ondragover = function(e){e.preventDefault()}
document.ondrop = function(e){e.preventDefault()}
export default {
  data() {
    return {
      dragElement: null,
      lock: true
    }
  },
  methods: {
    // 源对象
    dragstart(e) {
      // 记录当前拖动的元素
      this.dragElement = e.target
      e.target.style.backgroundColor = '#f8f8f8'
    },
    dragend(e) {
      e.preventDefault()
      e.target.style.backgroundColor = '#fff' // 拖放结束还原拖动元素的背景
    },
    // 目标对象
    dragenter(e) {
      if(this.dragElement !== e.target){
        e.target.parentNode.insertBefore(this.dragElement, e.target) // 把拖动元素添加到当前元素的前面
      }
    },
    dragleave(e) {
      if(this.dragElement !== e.target){
        // 当前元素时最后一个元素
        if(this.lock && (e.target === e.target.parentNode.lastElementChild || e.target === e.target.parentNode.lastChild)) {
          e.target.parentNode.appendChild(this.dragElement) // 把拖动元素添加最后面
          this.lock = false
        } else {
          this.lock = true
        }
      }
    },
  }
}
</script>
```

在移动端完全不兼容上面的实现，可以使用移动端拖拽兼容库达到目的：[mobile-drag-drop](https://github.com/timruffles/mobile-drag-drop)<br />只需要在原有的代码中引入该插件，即可在移动端上实现拖动了。
```vue
<script src="./mobile-drag-drop/index.min.js"></script>
<script src="./mobile-drag-drop/scroll-behaviour.min.js"></script>
<script>
  MobileDragDrop.polyfill({
    // use this to make use of the scroll behaviour
    dragImageTranslateOverride: MobileDragDrop.scrollBehaviourDragImageTranslateOverride
  });
</script>
```

如果使用了包管理，安装：
```bash
npm install mobile-drag-drop --save
# or
yarn add mobile-drag-drop
```
引入：
```bash
import {polyfill} from "mobile-drag-drop";

// optional import of scroll behaviour
import {scrollBehaviourDragImageTranslateOverride} from "mobile-drag-drop/scroll-behaviour";

// options are optional ;)
polyfill({
    // use this to make use of the scroll behaviour
    dragImageTranslateOverride: scrollBehaviourDragImageTranslateOverride
});
```


<a name="LixuK"></a>
## 拖拽时的文件操作
在`dataTransfer`中可以获取到拖拽时包含的文件对象，通过`e.dataTransfer.files`获取。

<a name="xz4vw"></a>
### HTML5新增的文件操作对象
**File： 代表一个文件对象**<br />**FileList： 代表一个文件列表对象，类数组**<br />**FileReader：用于从文件中读取数据**<br />**FileWriter：用于向文件中写出数据**

<a name="oiiao"></a>
### 拖拽显示图片
示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/eYWVXod)

源码：
```html
<template>
<div class="target-box">
  <div @drop="drop" class="target">拖拽到此处显示图片</div>
</div>
</template>

<script>
document.ondragover = function(e){
  e.preventDefault(); //使得drop事件可以触发
}
document.ondrop = function(e){
  e.preventDefault(); //阻止在新窗口中打开图片，否则仍然会执行下载操作！！！
}

export default {
  methods: {
    drop(e) {
      e.preventDefault()
      let f0 = e.dataTransfer.files[0];
      console.log(f0); //文件对象 File

      //从文件对象中读取数据
      let fr = new FileReader()
      //fr.readAsText(f0) //从文件中读取文本字符串
      fr.readAsDataURL(f0) //从文件中读取URL数据
      fr.onload = function() {
        console.log(fr.result) // base64 URI
        let img = new Image()
        img.src = fr.result
        e.target.appendChild(img)
      }
      return false
    }
  }
}
</script>

<style>
.source-box, .target-box {
  display: flex;
}

.source {
  width: 200px;
  height: 200px;
  background-color: red;
  margin-top: 20px;
  margin-right: 20px;
}

.target {
  width: 300px;
  height: 300px;
  background-color: #ccc;
  margin-top: 20px;
  margin-right: 20px;
}

.target > img {
  width: 100%;
  height: 100%;
}
</style>
```

<a name="tICaO"></a>
### 拖拽上传文件



<a name="M10EH"></a>
## 参考资料

- [知乎：HTML5 进阶系列：拖放 API 实现拖放排序](https://zhuanlan.zhihu.com/p/26666141)
- [CSDN：HTML5--拖拽API(含超经典例子)](https://blog.csdn.net/baidu_25343343/article/details/53215193)
- [MDN：拖拽操作](https://developer.mozilla.org/zh-CN/docs/Web/API/HTML_Drag_and_Drop_API/Drag_operations)


