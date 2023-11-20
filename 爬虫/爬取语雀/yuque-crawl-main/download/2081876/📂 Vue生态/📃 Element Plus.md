Element Plus（Element+）是饿了么团队以Vue3为基础构建的PC端优先的模板库。官网：[Element Plus](https://element-plus.gitee.io/#/zh-CN)

<a name="g65nD"></a>
## 一、安装
<a name="thIhw"></a>
### 在Vite项目中安装
```bash
yarn add element-plus
```
在 `main.js` 中：
```javascript
import { createApp } from 'vue'
import router from './routes'
import store from './stores'
import ElementPlus from 'element-plus';

import App from './App.vue'

import './index.css'
import 'element-plus/lib/theme-chalk/index.css';

const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(store)
app.mount('#app')
```
这样将引入Element+中的所有组件。之后，就可以在Vue中愉快地使用Element+了。

<a name="OLQeD"></a>
### 使用脚手架
Element+提供了Vite的脚手架项目，clone下来就可快速使用：[element-plus-vite-starter](https://github.com/element-plus/element-plus-vite-starter)

如果是Vue Cli脚手架项目，可以使用：[element-plus-starter](https://github.com/element-plus/element-plus-starter)

<a name="SwNZV"></a>
## 二、常用API的使用

<a name="qYopo"></a>
### Loading
通过服务调用：
```typescript
import { ElLoading } from 'element-plus';

export default {
  components: { Counter },
  setup () {
    ElLoading.service({ text: "Hello" })
  }
}
```

通过应用实例调用：
```typescript
import { getCurrentInstance } from 'vue'

export default {
  components: { Counter },
  setup () {
    const { ctx: vm } = getCurrentInstance()
    vm.$loading({ text: "Hello" })
  }
}
```

`ElLoading` 支持一个选项（ILoadingOptions），定义如下：
```typescript
export declare type ILoadingOptions = {
    parent?: ILoadingParentElement;
    background?: string;
    spinner?: boolean | string;
    text?: string;
    fullscreen?: boolean;
    body?: boolean;
    lock?: boolean;
    customClass?: string;
    visible?: boolean;
    target?: string | HTMLElement;
};

```

`ElLoading` 的实例还有以下方法：
```typescript
export declare type ILoadingInstance = {
    parent?: Ref<ILoadingParentElement>;
    background?: Ref<string>;
    spinner?: Ref<boolean | string>;
    text?: Ref<string>;
    fullscreen?: Ref<boolean>;
    body?: Ref<boolean>;
    lock?: Ref<boolean>;
    customClass?: Ref<string>;
    visible?: Ref<boolean>;
    target?: Ref<string | HTMLElement>;
    originalPosition?: Ref<string>;
    originalOverflow?: Ref<string>;
    setText: (text: string) => void;
    close: () => void;
    handleAfterLeave: () => void;
    vm: VNode;
    $el: HTMLElement;
};
```
方法调用示例：
```typescript
const { ctx: vm } = getCurrentInstance()
let loading = vm.$loading({ text: "Hello" })
setTimeout(() => {
  loading.setText('world')
  setTimeout(() => {
    loading.close()
  }, 1000)
}, 1000);
```

详情参看：[https://element-plus.gitee.io/#/zh-CN/component/loading](https://element-plus.gitee.io/#/zh-CN/component/loading)

<a name="KseR4"></a>
### Message
使用示例：
```javascript
import { ElMessage } from 'element-plus';

ElMessage.success('Success')
```

通过应用实例调用：
```typescript
import { ElMessage } from 'element-plus';
import { getCurrentInstance } from 'vue'

export default {
  setup () {
    const instance = getCurrentInstance()
    instance.ctx.$message('Hello')
    instance.ctx.$message.success('Hello')
  }
}
```

IMessage的定义：
```typescript
export interface IMessage {
    (options?: MessageParams): IMessageHandle;
    success: (options?: TypedMessageParams<'success'>) => IMessageHandle;
    warning: (options?: TypedMessageParams<'warning'>) => IMessageHandle;
    info: (options?: TypedMessageParams<'info'>) => IMessageHandle;
    error: (options?: TypedMessageParams<'error'>) => IMessageHandle;
    closeAll(): void;
}
```

success、warning、info、error的参数可以是字符串，也可以是一个选项：
```typescript
export declare type TypedMessageParams<T extends MessageType> = {
    type: T;
} & Omit<IMessageOptions, 'type'> | string;
```

选项（IMessageOptions）的定义如下：
```typescript
export declare type IMessageOptions = {
    customClass?: string;
    center?: boolean;
    dangerouslyUseHTMLString?: boolean;
    duration?: number;
    iconClass?: string;
    id?: string;
    message?: string | VNode;
    offset?: number;
    onClose?: () => void;
    showClose?: boolean;
    type?: 'success' | 'warning' | 'info' | 'error' | '';
    zIndex?: number;
};
```

详情参看：[https://element-plus.gitee.io/#/zh-CN/component/message](https://element-plus.gitee.io/#/zh-CN/component/message)

<a name="2T3Ig"></a>
### MessageBox
使用示例（以alert为例）：
```typescript
import { ElMessageBox } from 'element-plus'

export default {
  setup () {
    ElMessageBox.alert("", "", {
      title: "提示",
      message: "This is a essageBox",
      type: "warning",
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      showCancelButton: true
    })
  }
}
```

通过应用实例调用（以alert为例）：
```typescript
import { getCurrentInstance } from 'vue'

export default {
  setup () {
    const { ctx: vm } = getCurrentInstance()

    vm.$alert("Hello")

    vm.$alert("", "", {
      title: "提示",
      message: "This is a essageBox",
      type: "warning",
      confirmButtonText: "确定",
      cancelButtonText: "取消",
      showCancelButton: true
    })
  }
}
```
`MessageBox` 的定义如下：
```typescript
declare const MessageBox: {
    (options: ElMessageBoxOptions | string, callback?: any): Promise<any>;
    alert(message: any, title: any, options?: ElMessageBoxOptions): Promise<any>;
    confirm(message: any, title: any, options?: ElMessageBoxOptions): Promise<any>;
    prompt(message: any, title: any, options?: ElMessageBoxOptions): Promise<any>;
    close(): void;
};
```

<a name="eYLlO"></a>
#### 属性
`MessageBox` 挂载到vue上下文的有以下属性：
```typescript
$msgbox(options)
$alert(message, title, options) 或 $alert(message, options)
$confirm(message, title, options) 或 $confirm(message, options)
$prompt(message, title, options) 或 $prompt(message, options)
```
源码如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1607311908438-9d7d4ead-aac1-44f8-8346-e961bd8f4aa7.png#align=left&display=inline&height=174&originHeight=174&originWidth=652&size=45305&status=done&style=none&width=652)

上面展示了alert的用法。接下来看看其他几种API的用法。<br />`confirm` 的示例：
```typescript
vm.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
  confirmButtonText: '确定',
  cancelButtonText: '取消',
  type: 'warning'
}).then(() => {
  vm.$message({
    type: 'success',
    message: '删除成功!'
  });
}).catch(() => {
  vm.$message({
    type: 'info',
    message: '已取消删除'
  });
});
```
`prompt` 的示例：
```typescript
vm.$prompt('请输入邮箱', '提示', {
  confirmButtonText: '确定',
  cancelButtonText: '取消',
  inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
  inputErrorMessage: '邮箱格式不正确'
}).then(({ value }) => {
  vm.$message({
    type: 'success',
    message: '你的邮箱是: ' + value
  });
}).catch(() => {
  vm.$message({
    type: 'info',
    message: '取消输入'
  });
});
```
自定义内容 `msgbox` 的用法：
```typescript
vm.$msgbox({
  title: '消息',
  message: h('p', null, [
    h('span', null, '内容可以是 '),
    h('i', { style: 'color: teal' }, 'VNode')
  ]),
  showCancelButton: true,
  confirmButtonText: '确定',
  cancelButtonText: '取消',
  beforeClose: (action, instance, done) => {
    if (action === 'confirm') {
      instance.confirmButtonLoading = true;
      instance.confirmButtonText = '执行中...';
      setTimeout(() => {
        done();
        setTimeout(() => {
          instance.confirmButtonLoading = false;
        }, 300);
      }, 3000);
    } else {
      done();
    }
  }
}).then(action => {
  vm.$message({
    type: 'info',
    message: 'action: ' + action
  });
});
```

<a name="NAH5w"></a>
#### 选项
选项（ElMessageBoxOptions）的定义如下：
```typescript
export interface ElMessageBoxOptions {
    title?: string;
    message?: string | VNode;
    type?: MessageType;
    iconClass?: string;
    customClass?: string;
    callback?: (action: MessageBoxCloseAction, instance: ElMessageBoxComponent) => void;
    beforeClose?: (action: MessageBoxCloseAction, instance: ElMessageBoxComponent, done: (() => void)) => void;
    lockScroll?: boolean;
    showCancelButton?: boolean;
    showConfirmButton?: boolean;
    showClose?: boolean;
    cancelButtonText?: string;
    confirmButtonText?: string;
    cancelButtonClass?: string;
    confirmButtonClass?: string;
    center?: boolean;
    dangerouslyUseHTMLString?: boolean;
    roundButton?: boolean;
    closeOnClickModal?: boolean;
    closeOnPressEscape?: boolean;
    closeOnHashChange?: boolean;
    showInput?: boolean;
    inputPlaceholder?: string;
    inputValue?: string;
    inputPattern?: RegExp;
    inputType?: string;
    inputValidator?: MessageBoxInputValidator;
    inputErrorMessage?: string;
    distinguishCancelAndClose?: boolean;
}
```

<a name="sDPdp"></a>
#### 返回值
返回值（Promise形式）：
```typescript
try {
  let res = await ElMessageBox.alert("", "", {
    title: "提示",
    message: "This is a essageBox",
    type: "warning",
    confirmButtonText: "确定",
    cancelButtonText: "取消",
    showCancelButton: true
  })
  console.log(res) // confirm
} catch (e) {
  console.log(e) // cancel
}
```
返回值（回调形式）：
```typescript
ElMessageBox.alert("", "", {
  title: "提示",
  message: "This is a essageBox",
  type: "warning",
  confirmButtonText: "确定",
  cancelButtonText: "取消",
  showCancelButton: true,
  callback(res) {
    console.log(res) // confirm or cancel
  }
})
```

详情参看：[https://element-plus.gitee.io/#/zh-CN/component/message-box](https://element-plus.gitee.io/#/zh-CN/component/message-box)

<a name="Ry2vF"></a>
### Notification
使用示例：
```typescript
import { ElNotification } from 'element-plus'

export default {
  setup () {
    ElNotification({
      title: '成功',
      message: '这是一条成功的提示消息',
      type: 'success'
    });
  }
}
```

通过应用实例调用：
```typescript
import { getCurrentInstance, h } from 'vue'

export default {
  setup () {
    const { ctx: vm } = getCurrentInstance()

    vm.$notify({
      title: '标题名称',
      message: h('i', { style: 'color: teal'}, '这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案这是提示文案')
    });
  }
}
```

`Notification` 的选项 `INotificationOptions` 定义如下：
```typescript
export declare type INotificationOptions = {
    customClass?: string;
    dangerouslyUseHTMLString?: boolean;
    duration?: number;
    iconClass?: string;
    id?: string;
    message?: string | VNode;
    zIndex?: number;
    onClose?: () => void;
    onClick?: () => void;
    offset?: number;
    position?: 'top-right' | 'top-left' | 'bottom-right' | 'bottom-left';
    showClose?: boolean;
    type?: 'success' | 'warning' | 'info' | 'error' | '';
    title?: string;
};
```

详情参看：[https://element-plus.gitee.io/#/zh-CN/component/notification](https://element-plus.gitee.io/#/zh-CN/component/notification)


