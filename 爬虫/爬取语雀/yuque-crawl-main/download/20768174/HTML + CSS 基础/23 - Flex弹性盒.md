<a name="EFX3P"></a>
# 1.怪异盒模型
- 标准盒模型 `box-sizing:content-box`
   - 元素的宽度(不包含外边距) = width内容区域+左右内边距+左右边框
- 怪异盒模型 `box-sizing:border-box`
   - 元素的宽度(不包含外边距) = width
   - 怪异盒模型的width把内容、内边距和边框都包含在内
- 移动端 *{box-sizing:border-box}
<a name="XoMOo"></a>
# 2.弹性盒 / flex布局
![flex主轴方向.png](https://cdn.nlark.com/yuque/0/2023/png/22608300/1676953375531-7e429201-90f7-473b-b438-d385a675146b.png#averageHue=%23fcfcfc&clientId=uf449dac6-aba7-4&from=paste&height=771&id=uf16746bf&originHeight=1541&originWidth=2992&originalType=binary&ratio=2&rotation=0&showTitle=false&size=64647&status=done&style=none&taskId=u3a54f573-85ad-49f8-ad8e-bb13e37dd74&title=&width=1496)
<a name="hIaiq"></a>
## 2.1 父元素添加的属性

- 1.display:flex/inline-flex;
   - flex将对象作为弹性伸缩盒显示
   - inline-flex将对象作为内联块弹性伸缩盒显示
- 2.flex-direction (主轴排列方向)
   - row 默认，横向一行排列
   - row-reverse 反转横向排列
   - column 纵向排列
   - column-reverse 反转纵向排列
- 3.justify-content(主轴对齐方式)
   - flex-start 默认，顶端对齐
   - flex-end 末端对齐
   - center 居中对齐
   - space-between 两端对齐，中间自动分配
   - space-around 中间距离为两端二倍
   - space-evenly 等距离分配
      - 默认元素在主轴上容不下不会换行，会被压缩
- 4.align-items(侧轴对齐方式)
   - flex-start 侧轴起始边界
   - flex-end 侧轴结束边界
   - center 居中放置
   - baseline 基线对齐
   - stretch 默认值，项目被拉伸以适应容器，前提是子元素没有在侧轴方向上设置尺寸
- 5.flex-wrap设置换行
   - nowrap 容器为单行，该情况下子项可能会溢出容器
   - wrap 容器为多行，子项内部会发生断行
   - wrap-reverse 反转排列
- 6.align-content(行与行之间对齐方式)
   - flex-start 顶部对齐没有行间距
   - flex-end 底对齐没有行间距
   - center 居中没有行间距
   - space-between 两端对齐，中间自动分配
   - space-around 中间距离为两端二倍
   - space-evenly 等距离分配
   - stretch 默认值，项目被拉伸以适应容器
<a name="VuFNR"></a>
## 2.2 子元素添加的属性

- 1.align-self 灵活容器内被选中项目的对齐方式
      - 可重写灵活容器的align-items属性
   - auto 默认值，元素继承了它的父容器的align-items属性
   - stretch 元素被拉伸以适应容器
   - center 元素位于容器的中心
   - flex-start 元素位于容器的顶部
   - flex-end 元素位于容器的底部
- 2.order 排序优先级
   - 数字越大越往后排，默认为0，支持负数
- 3.flex-grow 项目的放大比例
   - flex-grow:1;
   - 同flex:1;--放大比例
- 4.flex-shrink 项目的缩小比例
   - flex-shrink:0;元素不缩小
- 5.flex-basis 项目的长度
- 6.flex为345的简写形式
   - 默认值flex:0 1 auto;
<a name="krNNs"></a>
# 3.flex布局练习
![2021-11-17_230639.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637161746062-b8fc44b0-2ca7-4816-9885-5d3984674c7b.jpeg#averageHue=%23f7f4f3&clientId=ueb2172a0-46da-4&from=ui&height=281&id=u0ed3f5fb&originHeight=565&originWidth=1004&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67080&status=done&style=none&taskId=u8d627f31-60ae-47e3-b62b-47a7a49bd98&title=&width=500)![2021-11-17_230750.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637161746090-61dee9a5-377b-47e7-a465-faed94f82a4a.jpeg#averageHue=%23e9e7e3&clientId=ueb2172a0-46da-4&from=ui&height=213&id=uacf35175&originHeight=273&originWidth=642&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30243&status=done&style=none&taskId=u55c07fb0-bb33-4cbe-8c78-39cde3ff79c&title=&width=500)<br />![2021-11-17_230733.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637161746073-633d9851-107e-408b-922a-3f23ff4fd463.jpeg#averageHue=%23f8e5e5&clientId=ueb2172a0-46da-4&from=ui&height=52&id=Tsbx4&originHeight=104&originWidth=1000&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10502&status=done&style=none&taskId=ub946bb4f-e335-4356-95d7-a6cf73a21cc&title=&width=500)<br />![2021-11-17_230701.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637161746069-799187a9-0680-4b55-9954-c83b771627a1.jpeg#averageHue=%23dcdc00&clientId=ueb2172a0-46da-4&from=ui&height=357&id=SfIq4&originHeight=867&originWidth=1456&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38314&status=done&style=none&taskId=ua483efa8-6622-40af-998e-e77a0956d41&title=&width=600)![2021-11-17_230806.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637161746087-d57b4fe0-f24a-476a-87c5-c8a4e66dcac1.jpeg#averageHue=%23717171&clientId=ueb2172a0-46da-4&from=ui&id=u6f235720&originHeight=272&originWidth=1834&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39776&status=done&style=none&taskId=ubf58a3a4-ba31-4a81-a56a-c8d3fbe54db&title=)
