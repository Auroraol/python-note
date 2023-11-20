以前要配置VSCode在多环境使用很麻烦，需要用到[Profile Switcher](https://marketplace.visualstudio.com/items?itemName=aaronpowell.vscode-profile-switcher)插件，而且是通过插件的卸载/安装实现的，同步起来有问题。

现在，VSCOde已经内置了多环境切换功能，参考[Visual Studio Code June 2022 - Settings Profiles](https://code.visualstudio.com/updates/v1_69#_settings-profiles)。

设置：
```javascript
workbench.experimental.settingsProfiles.enabled
```

将其启用：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1670903269461-3617d65b-c5bc-41e5-993e-31532399e31b.png#averageHue=%23544e42&clientId=u0250d1a5-35bc-4&from=paste&height=197&id=u67b0231f&originHeight=197&originWidth=1155&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52418&status=done&style=none&taskId=udb32b49c-1c14-4254-9010-e1bda283bce&title=&width=1155)

在左下角多出一个环境切换的图标：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1670903444017-4a8254ed-b6c0-4d24-baf1-7a255c4e27bf.png#averageHue=%231b82c7&clientId=u0250d1a5-35bc-4&from=paste&height=317&id=u25f8fc76&originHeight=317&originWidth=226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15868&status=done&style=none&taskId=u3f581e32-bb98-40bb-b30a-7313bdcfe25&title=&width=226)

可以对环境配置进行创建、导入导出、同步。

创建配置文件：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1670903500751-75bbfb01-59b9-4745-9260-76ce930d9117.png#averageHue=%232b3842&clientId=u0250d1a5-35bc-4&from=paste&height=106&id=ua90d42de&originHeight=106&originWidth=605&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14597&status=done&style=none&taskId=ua4743dc7-8078-4d49-baff-f7aea5cc8f4&title=&width=605)



