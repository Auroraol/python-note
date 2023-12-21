<a name="NR7lW"></a>
# 1.什么是BFC
   - BFC(Block formatting context)直译为“块级格式化上下文”。它是一个独立的渲染区域，它规定了内部的块如何布局，并且与这个区域外部毫不相干。
<a name="F6qtg"></a>
# 2.BFC的布局规则

   1. 内部的Box会在垂直方向，一个接一个地放置
   2. Box垂直方向的距离由margin决定。属于同一个BFC的两个相邻Box的margin会发生重叠（按照最大margin值设置）
   3. 每个元素的margin box的左边， 与包含块(定位元素的参考物)border box的左边相接触
   4. BFC的区域不会与float box重叠
   5. BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素
   6. 计算BFC的高度时，浮动元素也参与计算
<a name="VhKdu"></a>
# 3.哪些元素或属性能触发BFC

   1. 根元素(html)
   2. float属性不为none
   3. position为absolute或fixed
   4. display为inline-block, table-cell, table-caption, flex, inline-flex
   5. overflow不为visible
<a name="PZG0J"></a>
# 4.面试题：一侧固定一侧自适应布局

- 定位方法
- 浮动+margin
- BFC
- calc() - 这是css3的属性
   - width: calc(100% - 200px); 注意符号前后一定有空格
- 弹性盒 flex布局

![2021-11-08_190622.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1636369595487-fff3c4c8-b794-4530-ac4c-12c5a6f7118d.jpeg#averageHue=%23fefe00&clientId=uf239542f-acb1-4&from=ui&height=441&id=u1c948711&originHeight=1339&originWidth=2427&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44094&status=done&style=none&taskId=u3d4f6049-60ed-446e-af88-de3542f8b1e&title=&width=800)

- 拓展：左右固定中间自适应布局

![2021-11-08_190545.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1636369556620-d0a2cc23-793a-4404-b6e4-ccee6713f2ee.jpeg#averageHue=%23feb078&clientId=uf239542f-acb1-4&from=ui&height=392&id=u5d4ecca5&originHeight=1186&originWidth=2418&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42449&status=done&style=none&taskId=ud7e36978-88c4-48d6-bf1b-566e9a59300&title=&width=800)

- 拓展：圣杯布局

![20190118092113972.png](https://cdn.nlark.com/yuque/0/2021/png/22608300/1636369381213-bd0e6060-ac41-4f09-84ec-f1069ff6832d.png#averageHue=%23aa998d&clientId=uf239542f-acb1-4&from=ui&height=317&id=u4cb87f87&originHeight=420&originWidth=1060&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17223&status=done&style=none&taskId=u93bf9f4a-4c53-4d63-b275-9cfd08f4886&title=&width=800)
