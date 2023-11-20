<a name="22c79904"></a>
## 容器
<a name="53aded1f"></a>
### 视图（view）
`view` 组件是所有其他组件的父容器。详见：[view](http://uniapp.dcloud.io/component/view)

**属性说明**

| 属性名 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| hover-class | String | none | 指定按下去的样式类。当 hover-class="none" 时，没有点击态效果 |
| hover-stop-propagation | Boolean | false | 指定是否阻止本节点的祖先节点出现点击态 |
| hover-start-time | Number | 50 | 按住后多久出现点击态，单位毫秒 |
| hover-stay-time | Number | 400 | 手指松开后点击态保留时间，单位毫秒 |


注意：

- 使用 div 组件编译时会被转换为 view

<a name="3062dc73"></a>
### 滚动视图（scroll-view）
可滚动视图区域。用于区域滚动。

**属性说明**

| 属性名 | 类型 | 默认值 | 说明 | 平台差异说明 |
| :--- | :--- | :--- | :--- | :--- |
| scroll-x | Boolean | false | 允许横向滚动 |  |
| scroll-y | Boolean | false | 允许纵向滚动 |  |
| upper-threshold | Number | 50 | 距顶部/左边多远时（单位px），触发 scrolltoupper 事件 |  |
| lower-threshold | Number | 50 | 距底部/右边多远时（单位px），触发 scrolltolower 事件 |  |
| scroll-top | Number |  | 设置竖向滚动条位置 |  |
| scroll-left | Number |  | 设置横向滚动条位置 |  |
| scroll-into-view | String |  | 值应为某子元素id（id不能以数字开头）。设置哪个方向可滚动，则在哪个方向滚动到该元素 |  |
| scroll-with-animation | Boolean | false | 在设置滚动条位置时使用动画过渡 |  |
| enable-back-to-top | Boolean | false | iOS点击顶部状态栏、安卓双击标题栏时，滚动条返回顶部，只支持竖向 | 微信小程序 |
| show-scrollbar | Boolean | false | 控制是否出现滚动条 | App-nvue 2.1.5+ |
| refresher-enabled | Boolean | false | 开启自定义下拉刷新 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| refresher-threshold | number | 45 | 设置自定义下拉刷新阈值 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| refresher-default-style | string | "black" | 设置自定义下拉刷新默认样式，支持设置 black，white，none，none 表示不使用默认样式 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| refresher-background | string | "#FFF" | 设置自定义下拉刷新区域背景颜色 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| refresher-triggered | boolean | false | 设置当前下拉刷新状态，true 表示下拉刷新已经被触发，false 表示下拉刷新未被触发 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| enable-flex | boolean | false | 启用 flexbox 布局。开启后，当前节点声明了 display: flex 就会成为 flex container，并作用于其孩子节点。 | 微信小程序 2.7.3 |
| scroll-anchoring | boolean | false | 开启 scroll anchoring 特性，即控制滚动位置不随内容变化而抖动，仅在 iOS 下生效，安卓下可参考 CSS overflow-anchor 属性。 | 微信小程序 2.8.2 |
| @scrolltoupper | EventHandle |  | 滚动到顶部/左边，会触发 scrolltoupper 事件 |  |
| @scrolltolower | EventHandle |  | 滚动到底部/右边，会触发 scrolltolower 事件 |  |
| @scroll | EventHandle |  | 滚动时触发，event.detail = {scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY} |   |
| @refresherpulling | EventHandle |  | 自定义下拉刷新控件被下拉 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| @refresherrefresh | EventHandle |  | 自定义下拉刷新被触发 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| @refresherrestore | EventHandle |  | 自定义下拉刷新被复位 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |
| @refresherabort | EventHandle |  | 自定义下拉刷新被中止 | app-vue 2.5.12+,微信小程序基础库2.10.1+ |


配合 `scroll-view` 的加载更多示例：[Load_More](./Load_More.html)，详见：[scroll-view](http://uniapp.dcloud.io/component/scroll-view)

<a name="2411008a"></a>
### 滑动视图（swiper）
```html
<swiper
  indicator-dots="true"
  autoplay="true"
  circular="true"
  interval="2000"
  duration="1000"
>
  <swiper-item v-for="item in ['item1', 'item2', 'item3']" :key="item">
    <text>{{item}}</text>
  </swiper-item>
</swiper>
```

参数包括：

- **indicator-dots **** **Boolean  是否显示面板指示点，默认false
- **indicator-color** ** **Color 指示点颜色，默认rgba(0, 0, 0, .3)
- **indicator-active-color** ** **Color 当前选中的指示点颜色，默认#000000
- **autoplay** ** **Boolean  是否自动切换，默认false
- **current** ** **Number 当前所在滑块的 index，默认0
- **current-item-id** ** **String 当前所在滑块的 item-id ，不能与 current 被同时指定
- **interval** ** **Number 自动切换时间间隔，默认500
- **duration** ** **Number 滑动动画时长
- **circular** ** **Boolean  是否采用衔接滑动
- **vertical** ** **Boolean  滑动方向是否为纵向

<a name="9578633a"></a>
### 覆盖视图

- `cover-view` 为覆盖在原生组件上的文本视图。
- `cover-image` 为覆盖在原生组件上的图片视图。

tip：

- 可覆盖的原生组件有：video、map。
- 支持的事件：click。
- 暂不支持 cover-view、cover-image 组件之间的嵌套。
- 微信小程序平台下，可以使用条件编译，完全按照其规范开发。

完整的例子：
```vue
<template>
<view class="page">
  <video class="video" id="demoVideo" :controls="disable" :show-fullscreen-btn="disable" :show-play-btn="disable"
    :show-center-play-btn="disable" :enable-progress-gesture="disable" @fullscreenchange="fullscreenchange" src="https://www.dcloud.io/uniapp/wap2appvsnative.mp4">
      <cover-view class="controls-title">简单的自定义 controls</cover-view>
      <cover-image class="controls-play img" @click="play" src="/static/imgs/play.png"></cover-image>
      <cover-image class="controls-pause img" @click="pause" src="/static/imgs/pause.png"></cover-image>
  </video>
</view>
</template>

<script>
export default {
  data() {
    return {
      videoCtx: null,
      disable: false
    }
  },
  mounted() {
    this.videoCtx = uni.createVideoContext('demoVideo')
  },
  methods: {
    play(event) {
      this.videoCtx.play();
      uni.showToast({
        title: '开始播放',
        icon: 'none'
      });
    },
    pause(event) {
      this.videoCtx.pause();
      uni.showToast({
        title: '暂停播放',
        icon: 'none'
      });
    }
  }
}
</script>

<style>
.page {
  display: flex;
  justify-content: center;
}

.video {
  position: relative;
}

cover-view,
cover-image {
  display: inline-block;
}

.img {
  position: absolute;
  width: 100upx;
  height: 100upx;
  top: 50%;
  margin-top: -50upx;
}

.controls-play {
  left: 50upx;
}

.controls-pause {
  right: 50upx;
}

.controls-title {
  width: 100%;
  text-align: center;
  color: #FFFFFF;
}
</style>
```
![003.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1616385052028-f6cb7f02-7555-4752-a084-2fbb41ffb328.webp#align=left&display=inline&height=244&originHeight=244&originWidth=331&size=5958&status=done&style=none&width=331)

<a name="2d711b09"></a>
## 内容
<a name="9bd10595"></a>
### 文本（text）
`text` 组件由如下属性：

- **selectable** ** **Boolean  默认值 false，文本是否可选
- **space** ** **String 显示连续空格，可选 ensp、emsp、nbsp
- **decode**  Boolean   默认值 false，是否解码

注意：

- 使用 span 组件编译时会被转换为 text
- decode 可以解析的有 &nbsp; &lt; &gt; &amp; &apos; &ensp; &emsp;
- text 组件内只支持 text 嵌套
- 支持 \n 方式换行

<a name="5666c52c"></a>
### 富文本（rich-text）
`rich-text` 用法如下：
```html
<rich-text :nodes="nodes" @tap="tap"></rich-text>
```

其中 nodes 是富文本内容，可以是 String 或 Array。详见：[rich-text](http://uniapp.dcloud.io/component/rich-text)

<a name="5fb0af42"></a>
### 进度条（progress）
`progress` 用法如下：
```html
<progress percent="20" stroke-width="12" activeColor="pink" backgroundColor="black" active show-info />
```

属性如下：

- **percent**  Float  百分比0~100
- **stroke-width**  Number  进度条线的宽度，单位px
- **activeColor**  Color  已选择的进度条的颜色
- **backgroundColor**  Color  未选择的进度条的颜色
- **active**  Boolean  进度条从左往右的动画
- **show-info**  Boolean  在进度条右侧显示百分比
- **active-mode**  String  默认 backwards，可选 backwards: 动画从头播；forwards：动画从上次结束点接着播

<a name="eee1e225"></a>
## 表单
<a name="67f8bf8a"></a>
### 按钮（button）
```html
<button @tap="setPlain">button</button>
```

属性包括：

- **size**  String  默认default，按钮的大小，可选 default、mini
- **type**  String  默认default，按钮的样式类型，可选 primary、default、warn
- **plain**  Boolean  默认false，按钮是否镂空，背景色透明
- **disabled**  Boolean  默认false，是否禁用
- **loading**  Boolean  默认false，名称前是否带 loading 图标
- **form-type**  String  用于 <form> 组件，点击分别会触发 <form> 组件的 submit/reset 事件，可选 submit、reset
- **open-type**  String  微信开放能力，可选 share、getUserInfo
- **hover-class**  String  默认button-hover，指定按钮按下去的样式类。当 hover-class="none" 时，没有点击态效果
- **hover-start-time**  Number  默认20，按住后多久出现点击态，单位毫秒
- **hover-stay-time**  Number  默认70，手指松开后点击态保留时间，单位毫秒

除了通用事件外，button 还包括以下事件

- **getuserinfo** 用户点击该按钮时，会返回获取到的用户信息，从返回参数的detail中获取到的值同 `uni.getUserInfo` （`open-type="getUserInfo"`）

<a name="b3b2626c"></a>
### 标签（label）
用来改进表单组件的可用性，使用for属性找到对应的id，或者将控件放在该标签下，当点击时，就会触发对应的控件。

<a name="847770cd"></a>
### 表单（form）
将组件内的用户输入的 switch、input、checkbox、slider、radio、picker 提交。

当点击 form 表单中 formType 为 submit 的 button 组件时，会将表单组件中的 value 值进行提交，需要在表单组件中加上 name 来作为 key。

- **submit** 携带 form 中的数据触发 submit 事件，`event.detail = {value : {'name': 'value'} , formId: ''}`
- **reset** 表单重置时会触发 reset 事件

示例：
```vue
<template>
<view>
  <form @submit="formSubmit" @reset="formReset">
    <view class="section section_gap">
      <view class="section__title">switch</view>
      <switch name="switch" />
    </view>
    <view class="section section_gap">
      <view class="section__title">slider</view>
      <slider name="slider" show-value></slider>
    </view>

    <view class="section">
      <view class="section__title">input</view>
      <input name="input" placeholder="please input here" />
    </view>
    <view class="section section_gap">
      <view class="section__title">radio</view>
      <radio-group name="radio-group">
        <label><radio value="radio1" />radio1</label>
        <label><radio value="radio2" />radio2</label>
      </radio-group>
    </view>
    <view class="section section_gap">
      <view class="section__title">checkbox</view>
      <checkbox-group name="checkbox">
        <label><checkbox value="checkbox1" />checkbox1</label>
        <label><checkbox value="checkbox2" />checkbox2</label>
      </checkbox-group>
    </view>
    <view class="btn-area">
      <button formType="submit">Submit</button>
      <button formType="reset">Reset</button>
    </view>
  </form>
</view>
</template>

<script>
export default {
  methods: {
    formSubmit: function (e) {
      console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
    },
    formReset: function () {
      console.log('form发生了reset事件')
    }
  }
}
</script>
```

<a name="2f11144b"></a>
### 复选框（checkbox）

- **checkbox-group** 多项选择器，内部由多个 checkbox 组成。选中项发生改变是触发 change 事件，`detail = {value:[选中的checkbox的value的数组]}`
- **checkbox** 多选项目。

checkbox 的属性有：

- **value**  String  checkbox 标识，选中时触发 checkbox-group 的 change 事件，并携带 checkbox 的 value。
- **disabled**  Boolean  默认false，是否禁用
- **checked**  Boolean  默认false，当前是否选中，可用来设置默认选中
- **color**  Color  checkbox 的颜色，同css的color

```html
<checkbox-group @change="checkboxChange">
  <label class="checkbox" v-for="item in items" :key="item.value">
    <checkbox :value="item.name" :checked="item.checked" />{{item.value}}
  </label>
</checkbox-group>
```

<a name="c82e843e"></a>
### 单选框（radio）

- **radio-group** 单项选择器，内部由多个 radio 组成。选中项发生改变是触发 change 事件，`detail = {value:选中项radio的value}`
- **radio** 单选项目。

radio 的属性有：

- **value**  String  radio 标识，选中时触发 radio-group 的 change 事件，并携带 radio 的 value。
- **disabled**  Boolean  默认false，是否禁用
- **checked**  Boolean  默认false，当前是否选中，可用来设置默认选中
- **color**  Color  radio 的颜色，同css的color

```html
<radio-group class="radio-group" @change="radioChange">
  <label class="radio" v-for="item in items" :key="item">
    <radio :value="item.name" :checked="item.checked" />{{item.value}}
  </label>
</radio-group>
```

<a name="ffbddac1"></a>
### 开关（switch）
switch 的属性有：

- **checked**  Boolean  默认false，是否选中
- **disabled**  Boolean  默认false，是否禁用
- **type**  String  switch 样式，有效值：switch, checkbox
- **color**  Color  switch 的颜色，同 css 的 color

事件包括：

- **change**	EventHandle		checked 改变时触发 change 事件，event.detail={ value:checked}

```html
<switch checked @change="switch1Change" />
<switch @change="switch2Change" />
```

<a name="f81665b7"></a>
### 滑块（slider）
slider 的属性有：

- **min**  Number  默认0，最小值
- **max**  Number  默认100，最大值
- **step**  Number  默认1，步长，取值必须大于 0，并且可被(max - min)整除
- **disabled**  Boolean  默认false，是否禁用
- **value**  Number  默认0，当前取值
- **activeColor**  Color  默认#1aad19，已选择的颜色
- **backgroundColor**  Color  默认#e9e9e9，背景条的颜色
- **block-size**  Number  默认28，滑块的大小，取值范围为 12 - 28
- **block-color**  Color  默认#ffffff，滑块的颜色
- **show-value**  Boolean  默认false，是否显示当前 value

事件包括：

- **change** 完成一次拖动后触发的事件，`event.detail = {value: value}`
- **changing** 拖动过程中触发的事件，`event.detail = {value: value}`

```html
<slider @change="sliderChange" min="50" max="200" show-value/>
```

<a name="c65ac7f0"></a>
### 输入框（input）
input 的属性有：

- **value**  String  输入框的初始内容
- **type**  String  input 的类型，text（文本输入键盘）、number（数字输入键盘）、idcard（身份证输入键盘）、digit（带小数点的数字键盘）
- **password**  Boolean  默认false，是否是密码类型
- **placeholder**  String  输入框为空时占位符
- **placeholder-style**  String  指定 placeholder 的样式
- **placeholder-class**  String  指定 placeholder 的样式类
- **disabled**  Boolean  默认false，是否禁用
- **maxlength**  Number  默认140，最大输入长度，设置为 -1 的时候不限制最大长度
- **cursor-spacing**  Number  默认0，指定光标与键盘的距离，单位 px 。取 input 距离底部的距离和 cursor-spacing 指定的距离的最小值作为光标与键盘的距离
- **focus**  Boolean  默认false，获取焦点
- **confirm-type**  String  默认done，设置键盘右下角按钮的文字。可选 send（发送）、search（搜索）、next（下一个）、go（前往）、done（完成）
- **confirm-hold ** Boolean   微信小程序  默认false，点击键盘右下角按钮时是否保持键盘不收起 
- **cursor**  Number   微信小程序   指定focus时的光标位置 
- **selection-start**  Number   微信小程序   默认-1，光标起始位置，自动聚集时有效，需与selection-end搭配使用 
- **selection-end**  Number   微信小程序   默认-1，光标结束位置，自动聚集时有效，需与selection-start搭配使用 
- **adjust-position**  Number   微信小程序  默认true，键盘弹起时，是否自动上推页面 

事件包括：

- **input** 当键盘输入时，触发input事件，`event.detail = {value, cursor}`。input 事件处理函数可以直接 return 一个字符串，将替换输入框的内容。仅微信小程序支持。
- **focus** 输入框聚焦时触发，`event.detail = { value, height }`，height 为键盘高度。
- **blur** 输入框失去焦点时触发，`event.detail = {value: value}`
- **confirm** 点击完成按钮时触发，`event.detail = {value: value}`

```html
<input @input="KeyInput" placeholder="placeholder" />
```


