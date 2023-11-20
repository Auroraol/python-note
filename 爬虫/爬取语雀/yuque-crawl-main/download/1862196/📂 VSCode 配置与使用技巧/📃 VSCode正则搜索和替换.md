<a name="x551O"></a>
## 开启正则搜索和替换

在VSCode中，可以开启正则模式进行搜索替换。

在文件中开启正则搜索和替换：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602312932764-79a619c8-c35d-4da7-bb49-ef8a52090268.png#align=left&display=inline&height=84&originHeight=84&originWidth=437&size=5079&status=done&style=none&width=437)<br />全局开启搜索和替换：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602312947614-0f223251-660a-441b-8f0b-9bef4ed9b6bf.png#align=left&display=inline&height=154&originHeight=154&originWidth=375&size=7032&status=done&style=none&width=375)

<a name="FnNFC"></a>
## 分组替换

举例，首先有如下一段文字：
```json
- The global Command Palette - `commandPalette`
- The Explorer context menu - `explorer/context`
- The editor context menu - `editor/context`
- The editor title menu bar - `editor/title`
- The editor title context menu - `editor/title/context`
- The debug callstack view context menu - `debug/callstack/context`
- The debug callstack view inline actions - `debug/callstack/context` group `inline`
- The debug toolbar - `debug/toolbar`
- The [SCM title menu](https://code.visualstudio.com/api/extension-guides/scm-provider#menus) - `scm/title`
- [SCM resource groups](https://code.visualstudio.com/api/extension-guides/scm-provider#menus) menus - `scm/resourceGroup/context`
- [SCM resources](https://code.visualstudio.com/api/extension-guides/scm-provider#menus) menus - `scm/resourceState/context`
- [SCM change title](https://code.visualstudio.com/api/extension-guides/scm-provider#menus) menus - `scm/change/title`
- The [View title menu](https://code.visualstudio.com/api/references/contribution-points#contributes.views) - `view/title`
- The [View item menu](https://code.visualstudio.com/api/references/contribution-points#contributes.views) - `view/item/context`
- The macOS Touch Bar - `touchBar`
- The comment thread title menu bar - `comments/commentThread/title`
- The comment thread context menu - `comments/commentThread/context`
- The comment title menu bar - `comments/comment/title`
- The comment context menu - `comments/comment/context`
- The Timeline view title menu bar - `timeline/title`
- The Timeline view item context menu - `timeline/item/context`
- The Extensions view context menu - `extension/context`
```

需求一：保留 `-` 和  ```` 中的内容，删除其余内容<br />分析：要保留 ```` 中的内容，需要选择并将其存储，然后使用 `$n` 替换第 n处括号 `(n)` <br />搜索表达式：
```json
.*`(.*)`
```
替换表达式：
```json
- $1
```
匹配的内容：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602311391772-e76abc07-e278-4a05-99ea-7e3f66519585.png#align=left&display=inline&height=596&originHeight=596&originWidth=1374&size=113533&status=done&style=none&width=1374)<br />替换后的结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602311545261-605f3784-92d9-4ac7-840e-1b9b8373c4a1.png#align=left&display=inline&height=541&originHeight=541&originWidth=356&size=30906&status=done&style=none&width=356)

<a name="A9nDc"></a>
## 懒惰模式

需要替换的内容还是上面一部分的内容。

需求二：删除 `-` 和 ``` 之间的内容<br />分析：这里需要使用到懒惰模式，而正则默认使用了贪婪模式，所以我们需要使用 `?` 开启懒惰模式<br />搜索表达式：
```json
-.*?`
```
替换表达式：
```json
- `
```
匹配的内容：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602311287783-e762fec2-08d1-4dc7-bad1-9378f906d570.png#align=left&display=inline&height=607&originHeight=607&originWidth=1386&size=118306&status=done&style=none&width=1386)<br />替换后的结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602311780741-68058da2-70c5-4b0b-b621-ffcb3b552382.png#align=left&display=inline&height=543&originHeight=543&originWidth=501&size=38555&status=done&style=none&width=501)

下图可以清楚地看出贪婪模式和懒惰模式的区别：<br />![Snipaste_2020-09-27_16-51-58.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602313288546-7cb1d4fa-f32d-4bdf-8b87-eb09902639fd.png#align=left&display=inline&height=306&originHeight=306&originWidth=1307&size=47578&status=done&style=none&width=1307)<br />贪婪模式<br />![Snipaste_2020-09-27_16-51-33.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602313282259-57a54f99-4ff8-4ce8-baf9-8e77dc3b294f.png#align=left&display=inline&height=305&originHeight=305&originWidth=1313&size=45348&status=done&style=none&width=1313)<br />懒惰模式

<a name="VO0ee"></a>
## 零宽断言

比如有如下一段css
```json
div {
  width: 100px;
  height: 50px;
  left: 30rpx;
  top: 30rpx
}
```
需求：将px转换为rpx。<br />分析：首先想到的肯定是直接将px替换为rpx，但这样做显然不对，因为里面的rpx也会受到影响，替换后变为rrpx。这里就需要使用到零宽断言了。<br />搜索表达式：
```json
(?<!r)px
```
替换表达式：
```json
rpx
```
匹配的内容：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602312857237-42ad3956-b998-4b81-a4e0-102a0cbccc80.png#align=left&display=inline&height=159&originHeight=159&originWidth=227&size=5727&status=done&style=none&width=227)<br />替换后的结果：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1602312878563-e56edf1d-a452-4cdb-a139-5ef85787674f.png#align=left&display=inline&height=154&originHeight=154&originWidth=239&size=5627&status=done&style=none&width=239)
