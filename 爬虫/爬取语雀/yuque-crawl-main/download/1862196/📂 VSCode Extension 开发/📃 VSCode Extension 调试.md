按下 `F5` ，将打开一个新的VSCode窗口，这是**扩展容器宿主**窗口（作用类似于浏览器，开发网页需要到浏览器中查看效果，开发扩展自然到另一个VSCode中查看效果），使用 `Ctrl + Shift + P` 调出命令面板：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602232736920-8f086806-53ad-4e7e-bc71-fd75a519ddf2.png#align=left&display=inline&height=112&originHeight=112&originWidth=1022&size=17359&status=done&style=none&width=1022)<br />输入 `Hello World` 命令，可以看到通知区域出现以下提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602231999631-04f6f630-6e59-49b8-a1f7-3f9067904f5b.png#align=left&display=inline&height=90&originHeight=90&originWidth=468&size=4166&status=done&style=none&width=468)<br />打开 `extension.js` ，刚才注册的命令其实就是这一段代码执行的结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602232101727-dc79f9d9-876b-46a0-8917-14d94f675bef.png#align=left&display=inline&height=151&originHeight=151&originWidth=1062&size=25413&status=done&style=none&width=1062)

<a name="WMJCj"></a>
## 断点调试
在代码中打上断点，可以直接代码调试：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602232234553-373650e4-3f87-4cdb-b186-b6650347c8ba.png#align=left&display=inline&height=1034&originHeight=1034&originWidth=1492&size=172404&status=done&style=none&width=1492)

<a name="i5p5K"></a>
## 加载代码
修改代码后，并不能实时生效，需要在扩展容器宿主中重新加载窗口后才能生效。<br />命令： `reload window`<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602232484503-87305dc8-de9c-4b17-9de5-671a112e93e5.png#align=left&display=inline&height=135&originHeight=135&originWidth=848&size=18717&status=done&style=none&width=848)

<a name="K1GBR"></a>
## 禁用其他扩展
自己开发扩展的时候，难免会跟已安装的扩展产生功能上的冲突，为了排除错误，我们可以禁用已安装的扩展，专注于当前正在开发的扩展。<br />使用命令：
```bash
extensions disable
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603181352922-e2b494cb-1b1b-46b5-b324-afa6cc9aa735.png#align=left&display=inline&height=185&originHeight=185&originWidth=606&size=26394&status=done&style=none&width=606)<br />注意要选“此工作区”的那个啊，不然你正在开发扩展的这个窗口也没得扩展咯。

也可以选择这个选项禁用扩展：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603761846047-b80f8285-95bd-4e1d-91ba-c1d6ada6b2da.png#align=left&display=inline&height=92&originHeight=92&originWidth=608&size=10248&status=done&style=none&width=608)

<a name="Xv3CH"></a>
## 开发者控制台
在[扩展容器宿主]中，按下 `Ctrl + Shift + I` （菜单选项：`帮助` -> `切换开发人员工具`）打开开发者控制台，类似于浏览器的 `F12` ，很多错误可以在此进行最终调试。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603699958722-41b41fdd-6a38-484c-bce5-3f479f06b0a6.png#align=left&display=inline&height=1040&originHeight=1040&originWidth=1920&size=319416&status=done&style=none&width=1920)

