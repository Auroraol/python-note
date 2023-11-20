在uniapp[页面生命周期](https://uniapp.dcloud.io/api/lifecycle?id=%e9%a1%b5%e9%9d%a2%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f)中，有一个onBackPress的事件监听，可以监听APP的导航栏返回和物理按键返回。

返回的数据如下：
```javascript
event = {from: backbutton | navigateBack}
```

当用户进行以下操作时，会触发该函数：

- Android 实体返回键 (from = backbutton)
- 顶部导航栏左边的返回按钮 (from = backbutton)
- 返回 API，即 uni.navigateBack() (from = navigateBack)

注意事项：

- 只有在该函数中返回值为 true 时，才表示不执行默认的返回，自行处理此时的业务逻辑。
- 不返回或返回其它值，均会执行默认的返回行为。
- H5 平台，顶部导航栏返回按钮支持 `onBackPress()`，浏览器默认返回按键及Android手机实体返回键不支持 `onBackPress()`
- 暂不支持直接在自定义组件中配置该函数，目前只能是在页面中来处理。


举例：
```javascript
onBackPress(event) {
  if (event.from === 'navigateBack') {
    return false
  }
  if (this.mode === 2) {
    this.mode = 1
    return true
  }
}
```

<a name="35808e79"></a>
## 参考资料

- [uni-app自定义返回逻辑教程](https://ask.dcloud.net.cn/article/35120)

