通常调用 uni-app，以 `uni` 开头，大部分微信小程序的接口都可以将 `wx` 前缀换为 `uni`。

比如 `wx.getLocation()` 使用 `uni.getLocation()` 代替。

<a name="ae707aac"></a>
## 接口回调
大部分接口都有以下回调：

- success：成功的回调
- fail：失败的回调
- complete：无论成功失败均回调

比如：
```javascript
uni.showToast({
  title: 'Hello uni-app',
  icon: 'none',
  success () {
    console.log('ok');
  },
  fail () {
    console.log('fail');
  }
})
```

<a name="Promise"></a>
## Promise
uni-app 对部分 API 进行了 Promise 封装 (比如 `uni.request`)，返回数据的**第一个参数是错误对象，第二个参数是返回数据**。

详细策略如下：

- 异步的方法，如果不传入 success、fail、complete 等 callback 参数，将以 Promise 返回数据。例如：uni.getImageInfo()
- 异步的方法且有返回对象，如果希望获取返回对象，必须至少传入一项 success、fail、complete 等 callback 参数。例如：uni.connectSocket()
- 同步的方法（即以 sync 结束），不封装 Promise。例如：uni.getSystemInfoSync()
- 以 create 开头的方法，不封装 Promise。例如：uni.createMapContext()
- 以 manager 结束的方法，不封装 Promise。例如：uni.getBackgroundAudioManager()

示例：
```javascript
// Promise
uni.request({
  url: 'https://www.example.com/request'
}).then(data => {
  let [error, res]  = data;
  console.log(res.data);
})

// Await
function async request () {
  let [error, res] = await uni.request({
    url: 'https://www.example.com/request'
  });
  console.log(res.data);
}
```

<a name="ce9a3c5e"></a>
## 弹出层接口
<a name="Toast"></a>
### Toast
用于对用户的操作做出反馈，显示消息提示框。<br />![002.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616395784347-eaabd680-40db-43d4-8979-e37950f7bc75.png#align=left&display=inline&height=87&originHeight=87&originWidth=229&size=1224&status=done&style=none&width=229)

参考：[http://uniapp.dcloud.io/api/ui/prompt?id=showtoast](http://uniapp.dcloud.io/api/ui/prompt?id=showtoast)

使用方式：
```javascript
uni.showToast({
  title: 'Hello uni-app',
  icon: 'none',
  duration: 10000,
  image: 'http://localhost:4000/logo.png'
})
```
![003.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616395808108-89f34712-51a9-49c2-b917-378975d21990.png#align=left&display=inline&height=134&originHeight=134&originWidth=117&size=5530&status=done&style=none&width=117)

参数中只有 `title` 是必填的，其余参数均为选填。

- **icon** 可选择 "success", "loading", "none"，默认为 "success"
- **duration** 默认为 1500
- 填写image后，icon被覆盖

或想在某个时机触发关闭toast，可以手动调用 `uni.hideToast();`。

<a name="Loading"></a>
### Loading
显示 loading 提示框, 需主动调用 uni.hideLoading 才能关闭提示框。
```javascript
uni.showLoading({
  title: '加载中',
  success () {
    setTimeout(() => {
      uni.hideLoading()
    }, 5000)
  }
});
```
![004.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616395851321-858c7cf3-44b6-4f71-bbd5-dbf0271317fa.png#align=left&display=inline&height=183&originHeight=183&originWidth=155&size=2555&status=done&style=none&width=155)

<a name="ActionSheet"></a>
### ActionSheet
显示 ActionSheet。
```javascript
uni.showActionSheet({
  itemColor: '#f00',
  itemList: ['item1', 'item2', 'item3', 'item4'],
  success: (e) => {
    console.log(e.tapIndex);
  }
})
```
![001.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616395877601-d7ed30b4-b820-4b7f-936a-f04762240ecb.png#align=left&display=inline&height=520&originHeight=602&originWidth=347&size=11495&status=done&style=none&width=300)

<a name="Modal"></a>
### Modal
显示模态框。
```javascript
uni.showModal({
  title: '提示',
  content: '这是一个模态弹窗',
  success: function (res) {
    if (res.confirm) {
      console.log('用户点击确定');
    } else if (res.cancel) {
      console.log('用户点击取消');
    }
  }
});
```

- **title**  String  必填，提示的标题
- **content**  String  必填，提示的内容
- **showCancel**  Boolean  可选，是否显示取消按钮，默认为 true
- **cancelText**  String  可选，取消按钮的文字，默认为"取消"，最多 4 个字符
- **cancelColor**  HexColor  可选，取消按钮的文字颜色，默认为"#000000"
- **confirmText**  String  可选，确定按钮的文字，默认为"确定"，最多 4 个字符
- **confirmColor**  HexColor  可选，确定按钮的文字颜色，默认为"#3CC51F"

![002.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616395987268-7a833087-bcac-48af-9957-5b6f9c1cc268.png#align=left&display=inline&height=162&originHeight=162&originWidth=284&size=4310&status=done&style=none&width=284)

<a name="Q7ohK"></a>
## 导航栏与状态栏
<a name="mU4Vf"></a>
### 设置页面标题
```javascript
uni.setNavigationBarTitle({
  title: '新的标题'
});
```

<a name="mKXUC"></a>
### 设置页面颜色
```javascript
uni.setNavigationBarColor({
  frontColor: '#ffffff',
  backgroundColor: '#ff0000',
  animation: {
    duration: 400,
    timingFunc: 'easeIn'
  }
})
```

- **frontColor**  HexColor  必填，前景颜色值，包括按钮、标题、状态栏的颜色，仅支持 #ffffff 和 #000000
- **backgroundColor**  HexColor  必填，背景颜色值，有效值为十六进制颜色
- **animation**  Object  可选，动画效果，仅支持 微信小程序

其中 animation 节点下包括：

- **duration**  Number  动画变化时间，默认0，单位：毫秒	微信小程序
- **timingFunc**  String  动画变化方式，默认 linear，可选 linear、easeIn、easeOut、easeInOut

![003.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1616396055070-bcb88f9d-9253-401a-aecc-3f8ad242357b.png#align=left&display=inline&height=80&originHeight=80&originWidth=331&size=4317&status=done&style=none&width=331)

<a name="ncaZa"></a>
## 查询接口的可用性
判断应用的 API，回调，参数，组件等是否在当前版本可用。
```javascript
uni.canIUse(String)
```

**String 参数说明**<br />使用 `${API}.${method}.${param}.${options}` 或者 `${component}.${attribute}.${option}` 方式来调用，例如：

- `${API}` 代表 API 名字
- `${method}` 代表调用方式，有效值为return, success, object, callback
- `${param}` 代表参数或者返回值
- `${options}` 代表参数的可选值
- `${component}` 代表组件名字
- `${attribute}` 代表组件属性
- `${option}` 代表组件属性的可选值

**示例**
```javascript
uni.canIUse('getSystemInfoSync.return.screenWidth');
uni.canIUse('getSystemInfo.success.screenWidth');
uni.canIUse('showToast.object.image');
uni.canIUse('request.object.method.GET');

uni.canIUse('live-player');
uni.canIUse('text.selectable');
uni.canIUse('button.open-type.contact');
```


