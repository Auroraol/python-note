<a name="yRWui"></a>
## Web Components简介
Web Components由以下三项技术组成：

- **Custom elements（自定义元素）：**一组JavaScript API，允许您定义custom elements及其行为，然后可以在您的用户界面中按照需要使用它们。
- **Shadow DOM（影子DOM）**：一组JavaScript API，用于将封装的“影子”DOM树附加到元素（与主文档DOM分开呈现）并控制其关联的功能。通过这种方式，您可以保持元素的功能私有，这样它们就可以被脚本化和样式化，而不用担心与文档的其他部分发生冲突。
- **HTML templates（HTML模板）：** [<template>](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/template) 和 [<slot>](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/slot) 元素使您可以编写不在呈现页面中显示的标记模板。然后它们可以作为自定义元素结构的基础被多次重用。


Web Components - MDN：<br />[Web Components | MDN](https://developer.mozilla.org/zh-CN/docs/Web/Web_Components)

可以到这个站点找到一些好用的Web Component：<br />[webcomponents.org - Discuss & share web components](https://www.webcomponents.org/)


<a name="Zd3OO"></a>
## 创建

1. 定义一个类继承HTMLElement
2. 在constructor中创建元素
3. 使用`window.customElements.define`定义Web Component
4. 在HTML中使用此Web Component

示例：
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
  <user-card></user-card>

  <script>
    class UserCard extends HTMLElement {
      constructor() {
        super();

        let image = document.createElement('img');
        image.src = 'https://semantic-ui.com/images/avatar2/large/kristy.png';
        image.width = '100'
        image.height = '100'
        image.classList.add('image');

        let container = document.createElement('div');
        container.classList.add('container');

        let name = document.createElement('p');
        name.classList.add('name');
        name.innerText = 'User Name';

        let email = document.createElement('p');
        email.classList.add('email');
        email.innerText = 'yourmail@some-email.com';

        let button = document.createElement('button');
        button.classList.add('button');
        button.innerText = 'Follow';

        container.append(name, email, button);
        this.append(image, container);
      }
    }

    window.customElements.define('user-card', UserCard);
  </script>
</body>
</html>
```
效果：<br />![Snipaste_2022-02-17_14-16-39.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1645078663121-7071557c-1929-4ed5-ace0-81fa5a766253.webp#clientId=ufc667b87-606b-4&from=drop&id=u86525012&originHeight=241&originWidth=310&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4226&status=done&style=none&taskId=u91b27eb4-fa05-4949-b903-82af362f190&title=)

<a name="mJBrn"></a>
## 模板
通过上面的方式可以穿件Web Component，但过程比较繁琐，可以通过模板的方式创建。

示例：
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
  <user-card></user-card>

  <template id="userCardTemplate">
    <img src="https://semantic-ui.com/images/avatar2/large/kristy.png" class="image" width="100" height="100">
    <div class="container">
      <p class="name">User Name</p>
      <p class="email">yourmail@some-email.com</p>
      <button class="button">Follow</button>
    </div>
  </template>

  <script>
    class UserCard extends HTMLElement {
      constructor() {
        super();

        let templateElem = document.getElementById('userCardTemplate');
        let content = templateElem.content.cloneNode(true);
        this.appendChild(content);
      }
    }
    window.customElements.define('user-card', UserCard);
  </script>
</body>
</html>
```

<a name="agmt7"></a>
## 样式
上面创建的Web Component并没有样式，可以直接在template中嵌入style书写样式。
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
  <user-card></user-card>

  <template id="userCardTemplate">
    <style>
      :host {
        display: flex;
        align-items: center;
        width: 450px;
        height: 180px;
        background-color: #d4d4d4;
        border: 1px solid #d5d5d5;
        box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
        border-radius: 3px;
        overflow: hidden;
        padding: 10px;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
      }
      .image {
        flex: 0 0 auto;
        width: 160px;
        height: 160px;
        vertical-align: middle;
        border-radius: 5px;
      }
      .container {
        box-sizing: border-box;
        padding: 20px;
        height: 160px;
      }
      .container > .name {
        font-size: 20px;
        font-weight: 600;
        line-height: 1;
        margin: 0;
        margin-bottom: 5px;
      }
      .container > .email {
        font-size: 12px;
        opacity: 0.75;
        line-height: 1;
        margin: 0;
        margin-bottom: 15px;
      }
      .container > .button {
        padding: 10px 25px;
        font-size: 12px;
        border-radius: 5px;
        text-transform: uppercase;
      }
    </style>
    <img src="https://semantic-ui.com/images/avatar2/large/kristy.png" class="image" width="100" height="100">
    <div class="container">
      <p class="name">User Name</p>
      <p class="email">yourmail@some-email.com</p>
      <button class="button">Follow</button>
    </div>
  </template>

  <script>
    class UserCard extends HTMLElement {
      constructor() {
        super();

        let templateElem = document.getElementById('userCardTemplate');
        let content = templateElem.content.cloneNode(true);
        this.appendChild(content);
      }
    }
    window.customElements.define('user-card', UserCard);
  </script>
</body>
</html>
```

效果：<br />![Snipaste_2022-02-17_14-22-04.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1645078944307-aa7873fb-6787-4d8f-a22a-7244747e12b4.webp#clientId=ufc667b87-606b-4&from=drop&id=ud9d4a77a&originHeight=295&originWidth=205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4202&status=done&style=none&taskId=u15b0d4e2-e793-4211-b888-28044a79d1c&title=)

<a name="XxwYC"></a>
## 插槽
跟Vue差不多，可以通过slot插槽传入元素：
```html
<user-card>
  <img width="200" height="200"
       slot="img" src="https://semantic-ui.com/images/avatar2/large/kristy.png">
</user-card>

<template id="userCardTemplate">
  <style>
    ...
  </style>

  <slot name="img"></slot>
  <div class="container">
    <p class="name"></p>
    <p class="email"></p>
    <button class="button">Follow John</button>
  </div>
</template>
```

<a name="RiKT4"></a>
## 参数
通过往Web Component中传递参数，可以在创建的时候通过以下方式获取参数并设置值：
```javascript
let templateElem = document.getElementById('userCardTemplate');
let content = templateElem.content.cloneNode(true);
content.querySelector('img').setAttribute('src', this.getAttribute('image'));
content.querySelector('.container>.name').innerText = this.getAttribute('name');
content.querySelector('.container>.email').innerText = this.getAttribute('email');
this.appendChild(content);
```
示例：
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
  <user-card
    image="https://semantic-ui.com/images/avatar2/large/kristy.png"
    name="User Name"
    email="yourmail@some-email.com"
  ></user-card>

  <template id="userCardTemplate">
    <style>
      :host {
        display: flex;
        align-items: center;
        width: 450px;
        height: 180px;
        background-color: #d4d4d4;
        border: 1px solid #d5d5d5;
        box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
        border-radius: 3px;
        overflow: hidden;
        padding: 10px;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
      }
      .image {
        flex: 0 0 auto;
        width: 160px;
        height: 160px;
        vertical-align: middle;
        border-radius: 5px;
      }
      .container {
        box-sizing: border-box;
        padding: 20px;
        height: 160px;
      }
      .container > .name {
        font-size: 20px;
        font-weight: 600;
        line-height: 1;
        margin: 0;
        margin-bottom: 5px;
      }
      .container > .email {
        font-size: 12px;
        opacity: 0.75;
        line-height: 1;
        margin: 0;
        margin-bottom: 15px;
      }
      .container > .button {
        padding: 10px 25px;
        font-size: 12px;
        border-radius: 5px;
        text-transform: uppercase;
      }
    </style>
    <img class="image">
    <div class="container">
      <p class="name"></p>
      <p class="email"></p>
      <button class="button">Follow John</button>
    </div>
  </template>

  <script>
    class UserCard extends HTMLElement {
      constructor() {
        super();

        let templateElem = document.getElementById('userCardTemplate');
        let content = templateElem.content.cloneNode(true);
        content.querySelector('img').setAttribute('src', this.getAttribute('image'));
        content.querySelector('.container>.name').innerText = this.getAttribute('name');
        content.querySelector('.container>.email').innerText = this.getAttribute('email');
        this.appendChild(content);
      }
    }
    window.customElements.define('user-card', UserCard);
  </script>
</body>
</html>
```

<a name="AMrHN"></a>
## Shadow DOM
Shadow DOM 允许将隐藏的 DOM 树附加到常规的 DOM 树中——它以 shadow root 节点为起始根节点，在这个根节点的下方，可以是任意元素，和普通的 DOM 元素一样。<br />![shadow-dom.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645085334336-a72c98f3-6bb5-48f2-b2eb-f5cbfffc5d80.png#clientId=u1b84a7ec-af5c-4&from=drop&id=u64a25292&originHeight=543&originWidth=1138&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22182&status=done&style=none&taskId=uc632e685-edd3-413b-86c3-939ae18940f&title=)<br />这里，有一些 Shadow DOM 特有的术语需要我们了解：

- `Shadow host`：一个常规 DOM节点，Shadow DOM 会被附加到这个节点上。
- `Shadow tree`：Shadow DOM内部的DOM树。
- `Shadow boundary`：Shadow DOM结束的地方，也是常规 DOM开始的地方。
- `Shadow root`: Shadow tree的根节点。

Shadow DOM 并不是一个新事物——在过去的很长一段时间里，浏览器用它来封装一些元素的内部结构。以一个有着默认播放控制按钮的 [<video>](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/video) 元素为例。你所能看到的只是一个 <video> 标签，实际上，在它的 Shadow DOM 中，包含了一系列的按钮和其他控制器。Shadow DOM 标准允许你为你自己的元素（custom element）维护一组 Shadow DOM。

自定义元素的`this.attachShadow()`方法开启 Shadow DOM，详见下面的代码。
```javascript
class UserCard extends HTMLElement {
  constructor() {
    super();
    let shadow = this.attachShadow( { mode: 'closed' } );

    let templateElem = document.getElementById('userCardTemplate');
    let content = templateElem.content.cloneNode(true);
    content.querySelector('img').setAttribute('src', this.getAttribute('image'));
    content.querySelector('.container>.name').innerText = this.getAttribute('name');
    content.querySelector('.container>.email').innerText = this.getAttribute('email');

    shadow.appendChild(content);
  }
}
window.customElements.define('user-card', UserCard);
```
上面代码中，`this.attachShadow()`方法的参数`{ mode: 'closed' }`，表示 Shadow DOM 是封闭的，不允许外部访问。

通过Shadow DOM技术可以使 `:host`的样式生效：<br />![Snipaste_2022-02-17_14-37-38.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1645079881146-a3bc1495-7488-4abb-8a02-8ccf76eaf323.webp#clientId=ufc667b87-606b-4&from=drop&id=uca9dce55&originHeight=200&originWidth=478&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4164&status=done&style=none&taskId=u13c481c4-37f2-4bde-be9b-f6861585f52&title=)

打开控制台，可以看到没有Shadow DOM和有Shadow DOM的区别。<br />没有Shadow DOM：<br />![Snipaste_2022-02-17_15-06-15.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645081644920-e186265b-238b-46f5-92f0-41930d905518.png#clientId=ufc667b87-606b-4&from=drop&id=u96a71517&originHeight=291&originWidth=970&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13432&status=done&style=none&taskId=u908029b0-31fc-4348-97ee-bd1ac049347&title=)<br />有Shadow DOM：<br />![Snipaste_2022-02-17_15-06-53.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645081644913-35a593fc-a0e1-4e77-81d6-79c90886030f.png#clientId=ufc667b87-606b-4&from=drop&id=u3c59f98b&originHeight=317&originWidth=1010&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14004&status=done&style=none&taskId=ub8c3dd53-1d60-4782-a4f4-ae7555121ec&title=)

**Shadow DOM 的一大优点是能将 DOM 结构、样式、行为与 Document DOM 隔离开，非常适合做组件的封装，因此它能成为 Web Component 的重要组成部分之一。**


<a name="huhi4"></a>
## 交互
跟普通的DOM事件绑定一样，获取到元素后通过`addEventListener`绑定事件即可。
```javascript
class UserCard extends HTMLElement {
  constructor() {
    super();
    let shadow = this.attachShadow( { mode: 'closed' } );

    let templateElem = document.getElementById('userCardTemplate');
    let content = templateElem.content.cloneNode(true);
    content.querySelector('img').setAttribute('src', this.getAttribute('image'));
    content.querySelector('.container>.name').innerText = this.getAttribute('name');
    content.querySelector('.container>.email').innerText = this.getAttribute('email');

    shadow.appendChild(content);

    this.$button = shadow.querySelector('button');
    this.$button.addEventListener('click', () => {
      alert('click')
    });
  }
}
window.customElements.define('user-card', UserCard);
```

<a name="Vnhjd"></a>
## 封装
封装的目的在昱可复用，思路很多。

**第一种方式**<br />将模板换为字符串，通过 `window.document.body.innerHTML`追加到body中，然后在html中引入此js。

`components/user-card.js`
```javascript
let templateStr = `
  <template id="userCardTemplate">
    <style>
      :host {
        display: flex;
        align-items: center;
        width: 450px;
        height: 180px;
        background-color: #d4d4d4;
        border: 1px solid #d5d5d5;
        box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
        border-radius: 3px;
        overflow: hidden;
        padding: 10px;
        box-sizing: border-box;
        font-family: 'Poppins', sans-serif;
      }
      .image {
        flex: 0 0 auto;
        width: 160px;
        height: 160px;
        vertical-align: middle;
        border-radius: 5px;
      }
      .container {
        box-sizing: border-box;
        padding: 20px;
        height: 160px;
      }
      .container > .name {
        font-size: 20px;
        font-weight: 600;
        line-height: 1;
        margin: 0;
        margin-bottom: 5px;
      }
      .container > .email {
        font-size: 12px;
        opacity: 0.75;
        line-height: 1;
        margin: 0;
        margin-bottom: 15px;
      }
      .container > .button {
        padding: 10px 25px;
        font-size: 12px;
        border-radius: 5px;
        text-transform: uppercase;
      }
    </style>
    <slot name="img"></slot>
    <div class="container">
      <p class="name"></p>
      <p class="email"></p>
      <button class="button">Follow John</button>
    </div>
  </template>
`

window.document.body.innerHTML += templateStr

class UserCard extends HTMLElement {
  constructor() {
    super();

    let shadow = this.attachShadow( { mode: 'closed' } );

    let templateElem = document.getElementById('userCardTemplate');
    let content = templateElem.content.cloneNode(true);
    content.querySelector('.container>.name').innerText = this.getAttribute('name');
    content.querySelector('.container>.email').innerText = this.getAttribute('email');

    shadow.appendChild(content);

    this.$button = shadow.querySelector('button');
    this.$button.addEventListener('click', () => {
      alert('click')
    });
  }
}

window.customElements.define('user-card', UserCard);
```
`index.html`
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
  <user-card
    image="https://semantic-ui.com/images/avatar2/large/kristy.png"
    name="User Name"
    email="yourmail@some-email.com"
  >
    <img slot="img" src="https://semantic-ui.com/images/avatar2/large/kristy.png" width="200" height="200">
  </user-card>

  <script src="./components/user-card.js"></script>
</body>
</html>
```
需要注意的是，这种方式只能将script引入放于body之中或之后，否则找不到body。

在上面的基础上，我们还可以把样式单独提出来，
```javascript
let templateStr = `
  <template id="userCardTemplate">
    <slot name="img"></slot>
    <div class="container">
      <p class="name"></p>
      <p class="email"></p>
      <button class="button">Follow John</button>
    </div>
  </template>
`

let styleStr = `
  :host {
    display: flex;
    align-items: center;
    width: 450px;
    height: 180px;
    background-color: #d4d4d4;
    border: 1px solid #d5d5d5;
    box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
    border-radius: 3px;
    overflow: hidden;
    padding: 10px;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }
  .image {
    flex: 0 0 auto;
    width: 160px;
    height: 160px;
    vertical-align: middle;
    border-radius: 5px;
  }
  .container {
    box-sizing: border-box;
    padding: 20px;
    height: 160px;
  }
  .container > .name {
    font-size: 20px;
    font-weight: 600;
    line-height: 1;
    margin: 0;
    margin-bottom: 5px;
  }
  .container > .email {
    font-size: 12px;
    opacity: 0.75;
    line-height: 1;
    margin: 0;
    margin-bottom: 15px;
  }
  .container > .button {
    padding: 10px 25px;
    font-size: 12px;
    border-radius: 5px;
    text-transform: uppercase;
  }
`

window.document.body.innerHTML += templateStr

class UserCard extends HTMLElement {
  constructor() {
    super();

    let shadow = this.attachShadow( { mode: 'closed' } );

    // 创建样式并为shadow Dom添加样式
    const style = document.createElement('style');
    style.textContent = styleStr
    shadow.appendChild(style);

    let templateElem = document.getElementById('userCardTemplate');
    let content = templateElem.content.cloneNode(true);
    content.querySelector('.container>.name').innerText = this.getAttribute('name');
    content.querySelector('.container>.email').innerText = this.getAttribute('email');

    shadow.appendChild(content);

    this.$button = shadow.querySelector('button');
    this.$button.addEventListener('click', () => {
      alert('click')
    });
  }
}

window.customElements.define('user-card', UserCard);
```




<a name="UpISI"></a>
## 参考资料

- [秒懂 Web Component](https://mp.weixin.qq.com/s/rtixnKwej6C2-V6WCalQUw)
- [阮一峰的网络日志：Web Components 入门实例教程](https://www.ruanyifeng.com/blog/2019/08/web_components.html)
- [Web Components Tutorial for Beginners [2019]](https://www.robinwieruch.de/web-components-tutorial/)
- [Custom Elements v1: Reusable Web Components](https://developers.google.com/web/fundamentals/web-components/customelements)
- [基于原生webComponent封装组件](https://juejin.cn/post/6890856593333616653)
- [脱离框架的组件化解决方案 - Web Component](https://juejin.cn/post/7045194698226401310)
- [你真的了解Web Component吗？](https://juejin.cn/post/7010580819895844878)

- [掘金：原生javascript组件开发之Web Component实战](https://juejin.cn/post/6844904197654052877)
- [掘金：从0到1教你搭建前端团队的组件系统（高级进阶必备）](https://juejin.cn/post/6844904068431740936)


