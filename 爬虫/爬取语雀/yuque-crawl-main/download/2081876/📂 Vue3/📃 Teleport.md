<a name="nbn4M"></a>
## 概述
在实际开发中，可能会遇到这样一个问题：某个组件包含在一个容器中，其宽高依赖于容器的宽高。而实际情况并不需要依赖于父容器，而是依赖于更高层级的容器。

举个例子。

先看一个容器：
```vue
<template>
<div class="box">
  <TeleportView></TeleportView>
</div>
</template>

<script setup>
import TeleportView from '../components/TeleportView.vue'
</script>

<style lang="stylus">
.box {
  width: 400px;
  height: 100px;
  position: relative;
}
</style>
```
一个名为 `.box` 的容器包裹着一个名为 `TeleportView` 的组件，并且 `.box` 设置为相对定位，含有宽高。

<a name="UusPJ"></a>
## 不使用Teleport
以下为子组件`TeleportView`的内容，这个示例下没有使用 `Teleport` ：
```vue
<template>
  <button @click="modalOpen = true">
      Open full screen modal!
  </button>

  <div v-if="modalOpen" class="modal">
    <div>
      I'm a modal!
      <button @click="modalOpen = false">
        Close
    	</button>
    </div>
  </div>
</template>

<script setup>
ref: modalOpen = false
</script>

<style>
.modal {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  background-color: rgba(0,0,0,.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.modal div {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: white;
  width: 300px;
  height: 300px;
  padding: 5px;
}
</style>
```

从效果可以看到， `.box` 的宽高限制了`TeleportView`的显示范围：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607392601573-966a1117-780b-4051-824b-8c05bdc360c6.gif#align=left&display=inline&height=207&originHeight=207&originWidth=451&size=7562&status=done&style=none&width=451)

<a name="3UWCu"></a>
## 使用Teleport
使用了Teleport的版本如下：
```vue
<template>
  <button @click="modalOpen = true">
      Open full screen modal!
  </button>

  <teleport to="body">
    <div v-if="modalOpen" class="modal">
      <div>
        I'm a modal!
        <button @click="modalOpen = false">
          Close
        </button>
      </div>
    </div>
  </teleport>
</template>

<script setup>
ref: modalOpen = false
</script>

<style>
.modal {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  background-color: rgba(0,0,0,.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.modal div {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: white;
  width: 300px;
  height: 300px;
  padding: 5px;
}
</style>
```
以上，将模态框用 `teleport` 包裹，并将其附着于 `body` 。

效果如下：<br />![GIF.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1607392715741-f27206aa-4885-4bef-b09b-101baa98659c.gif#align=left&display=inline&height=439&originHeight=439&originWidth=855&size=33435&status=done&style=none&width=855)

在CodePen中查看效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu-the-decoder/embed/MWjeOBd)

<a name="RPCxQ"></a>
## 参考资料

- [Teleport](https://v3.vuejs.org/guide/teleport.html#using-with-vue-components)
