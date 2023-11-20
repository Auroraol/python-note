<a name="scqXx"></a>
## 消息总线
类似于[vue-bus](https://www.npmjs.com/package/vue-bus)和[vue-happy-bus](https://github.com/tangdaohai/vue-happy-bus)。

使用：<br />发送事件并传递消息：
```javascript
uni.$emit('update', { msg: '页面更新' })
```
监听事件并获取消息（通常在页面的onLoad或created中）：
```javascript
created() {
  uni.$on('update',function(data){
    console.log('监听到事件来自 update ，携带参数 msg 为：' + data.msg);
  })
},
```

移出事件监听（通常在页面的onUnload或destroyed中）：
```javascript
onUnload() {
  uni.$off('login')
},
```

如果只想要监听一次，可以使用`uni.$once`
```javascript
uni.$once('update',function(data){
  console.log('监听到事件来自 update ，携带参数 msg 为：' + data.msg);
})
```
一次性的事件，直接使用`uni.$once`监听，不需要移除。

如果页面没有打开，将不能 注册监听事件`uni.$on`和`uni.$once`。



参考：

- [如何使用uni.$emit()和uni.$on() 进行页面间通讯](https://ask.dcloud.net.cn/article/36010)
- [uniapp官网：页面通讯](https://uniapp.dcloud.io/api/window/communication)


<a name="egSr2"></a>
## 页面返回时传值
**假如从B页面返回A页面，小程序中的写法是：**
```javascript
var pages = getCurrentPages();
var prevPage = pages[pages.length - 2]; //上一个页面
prevPage.setData({
	mdata: 1
})
```
经过测试，在uniapp中使用B页面使用setData设置A页面参数无法实现（应该是被更改为常量属性了）。

<a name="qNSWb"></a>
### 方法一：调用前一个页面的生命周期
A页面的生命周期：
```javascript
onHide: ƒ ()
onLoad: ƒ ()
onReady: ƒ ()
onResize: ƒ ()
onRouteEnd: ƒ ()
onShow: ƒ ()
onUnload: ƒ ()
```
B页面传递：
```javascript
let object={
  sx1:"参数1",
  sx2:"参数2",
}
prevPage.onShow(object);
uni.navigateBack();
```
A页面接收参数：
```javascript
onShow(object){
  if(!!object){
    this.object = object
  	console.log(object)
  }
}
```

<a name="ENsPq"></a>
### 方法二：调用前一个页面的方法
B页面传递：
```javascript
let object= {
  sx1:"参数1",
  sx2:"参数2",
}

prevPage.$vm.setData(object); // 重点$vm
uni.navigateBack();
```
A页面接收参数：
```javascript
export default {
  methods: {
    setData(object){
      if(!!object){
        this.object = object
        console.log(object)
      }
    }
  }
}
```
参考资料：[uni.navigateBack()返回时传递参数，最简单的办法！](https://ask.dcloud.net.cn/article/36845)

<a name="ONDLZ"></a>
### 方法三：修改前一个页面的数据
可以直接通过`$vm`修改上一个页面的数据：
```javascript
let pages = getCurrentPages() // 获取路由栈
let prevPage = pages[pages.length - 2] // 上一页面

prevPage.$vm.from = 'index'
uni.navigateBack()
```

