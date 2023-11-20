uni-ui是DCloud提供的一个跨端ui库，它是基于vue组件的、flex布局的、无dom的跨全端ui框架。

安装:
```bash
yarn add @dcloudio/uni-ui
yarn add -D node-sass sass-loader
```

:::warning
uni-ui 不支持使用 Vue.use() 的方式安装
:::

<a name="8ef2635b"></a>
## 组件列表
| 组件名 | 引用路径 | 说明 |
| --- | --- | --- |
| uniBadge | '@dcloudio/uni-ui/lib/uni-badge/uni-badge.vue' | [数字角标](https://ext.dcloud.net.cn/plugin?id=21) |
| uniCalendar | '@dcloudio/uni-ui/lib/uni-calendar/uni-calendar.vue' | [日历](https://ext.dcloud.net.cn/plugin?id=56) |
| uniCard | '@dcloudio/uni-ui/lib/uni-card/uni-card.vue' | [卡片](https://ext.dcloud.net.cn/plugin?id=22) |
| uniCollapse | '@dcloudio/uni-ui/lib/uni-collapse/uni-collapse.vue' | [折叠面板](http://ext.dcloud.net.cn/plugin?id=23) |
| uniCollapseItem | '@dcloudio/uni-ui/lib/uni-collapse-item/uni-collapse-item.vue' | [折叠面板子组件](https://ext.dcloud.net.cn/plugin?id=23)) |
| uniCountdown | '@dcloudio/uni-ui/lib/uni-countdown/uni-countdown.vue' | [倒计时](https://ext.dcloud.net.cn/plugin?id=25) |
| uniDrawer | '@dcloudio/uni-ui/lib/uni-drawer/uni-drawer.vue' | [抽屉](https://ext.dcloud.net.cn/plugin?id=26) |
| uniGrid | '@dcloudio/uni-ui/lib/uni-grid/uni-grid.vue' | [宫格](https://ext.dcloud.net.cn/plugin?id=27) |
| uniIcons | '@dcloudio/uni-ui/lib/uni-icons/uni-icons.vue' | [图标](https://ext.dcloud.net.cn/plugin?id=28) |
| uniList | '@dcloudio/uni-ui/lib/uni-list/uni-list.vue' | [列表](https://ext.dcloud.net.cn/plugin?id=24) |
| uniListItem | '@dcloudio/uni-ui/lib/uni-list-item/uni-list-item.vue' | [列表子组件](https://ext.dcloud.net.cn/plugin?id=24) |
| uniLoadMore | '@dcloudio/uni-ui/lib/uni-load-more/uni-load-more.vue' | [加载更多](https://ext.dcloud.net.cn/plugin?id=29) |
| uniNoticeBar | '@dcloudio/uni-ui/lib/uni-notice-bar/uni-notice-bar.vue' | [通告栏](https://ext.dcloud.net.cn/plugin?id=30) |
| uniNumberBox | '@dcloudio/uni-ui/lib/uni-number-box/uni-number-box.vue' | [数字输入框](https://ext.dcloud.net.cn/plugin?id=31) |
| uniPagination | '@dcloudio/uni-ui/lib/uni-pagination/uni-pagination.vue' | [分页器](https://ext.dcloud.net.cn/plugin?id=32) |
| uniPopup | '@dcloudio/uni-ui/lib/uni-popup/uni-popup.vue' | [弹出层](https://ext.dcloud.net.cn/plugin?id=329) |
| uniRate | '@dcloudio/uni-ui/lib/uni-rate/uni-rate.vue' | [评分](https://ext.dcloud.net.cn/plugin?id=33) |
| uniSegmentedControl | '@dcloudio/uni-ui/lib/uni-segmented-control/uni-segmented-control.vue' | [分段器](https://ext.dcloud.net.cn/plugin?id=54) |
| uniSteps | '@dcloudio/uni-ui/lib/uni-steps/uni-steps.vue' | [步骤条](https://ext.dcloud.net.cn/plugin?id=34) |
| uniSwipeAction | '@dcloudio/uni-ui/lib/uni-swipe-action/uni-swipe-action.vue' | [滑动操作](http://ext.dcloud.net.cn/plugin?id=181) |
| uniSwipeDot | '@dcloudio/uni-ui/lib/uni-swipe-dot/uni-swipe-dot.vue' | [滑动操作](http://ext.dcloud.net.cn/plugin?id=284) |
| uniTag | '@dcloudio/uni-ui/lib/uni-tag/uni-tag.vue' | [标签](https://ext.dcloud.net.cn/plugin?id=35) |


<a name="a653042e"></a>
## 使用方式
以 uni-icons 举例:
```vue
<template lang="pug">
.main: uniIcon(type="contact")
</template>

<script>
  import uniIcon from '@dcloudio/uni-ui/lib/uni-icons/uni-icons.vue'
	export default {
    components: {
      uniIcon
    },
	}
</script>
```

<a name="d17a0f0b"></a>
## 参考资料

- [uni-ui 介绍](https://uniapp.dcloud.io/component/README?id=uniui)

