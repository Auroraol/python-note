<a name="ckVlb"></a>
## Azure账号注册
首先通过链接 [https://login.live.com/](https://login.live.com/) 登录自己的Microsoft账号：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603768836895-28a3ea4f-2356-40b7-840b-a3040935c35a.png#align=left&display=inline&height=224&originHeight=224&originWidth=748&size=33800&status=done&style=none&width=748)

然后访问  [https://aka.ms/SignupAzureDevOps](https://aka.ms/SignupAzureDevOps) 注册一个 Azure 组织：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603768677712-df4f5d50-f691-4e8f-9b09-d3444c057d81.png#align=left&display=inline&height=431&originHeight=431&originWidth=472&size=16766&status=done&style=none&width=472)

注册好后，可以在侧边看到：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603768871926-3d69c7ea-0c1f-4393-85b2-9157d778e68e.png#align=left&display=inline&height=281&originHeight=281&originWidth=520&size=13329&status=done&style=none&width=520)


<a name="1xEC9"></a>
## 创建token

在右上角点开：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603768934954-994d918a-662e-41a0-8fc7-6d66cff4a1cc.png#align=left&display=inline&height=412&originHeight=412&originWidth=240&size=13415&status=done&style=none&width=240)<br />填写以下内容：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603769057288-6158ba02-2f6c-411b-8921-6d9b1c352e5c.png#align=left&display=inline&height=942&originHeight=942&originWidth=642&size=52371&status=done&style=none&width=642)<br />创建成功后，保存token：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603769076506-f5efeb90-fb33-464b-b4a1-3af000322786.png#align=left&display=inline&height=316&originHeight=316&originWidth=488&size=15250&status=done&style=none&width=488)

<a name="WVTqo"></a>
## 创建publisher
首先安装vsce：
```bash
npm i vsce -g
```
使用以下命令创建发布者：
```bash
vsce create-publisher your-name
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603769248673-dada98c2-2bd4-44f2-ae78-71cbe18724c1.png#align=left&display=inline&height=130&originHeight=130&originWidth=1416&size=24690&status=done&style=none&width=1416)

创建publisher的时候，默认就登录了，如果需要在其他电脑登录，需要使用命令：
```bash
vsce login quanzaiyu
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603769436875-8ad024a8-3935-4405-a684-5ca379b1d10b.png#align=left&display=inline&height=86&originHeight=86&originWidth=816&size=13560&status=done&style=none&width=816)

<a name="fc7Gj"></a>
## 发布扩展
使用以下命令即可发布扩展：
```bash
D:\Workplace\temp\vscode-extension-test>vsce publish
 INFO  Detected presense of yarn.lock. Using 'yarn' instead of 'npm' (to override this pass '--no-yarn' on the command line).
Publishing quanzaiyu.vscode-extension-test@0.0.1...
 DONE  Published quanzaiyu.vscode-extension-test@0.0.1
Your extension will live at https://marketplace.visualstudio.com/items?itemName=quanzaiyu.vscode-extension-test (might take a few minutes for it to show up).
```
过几分钟，会有邮件通知发布扩展成功，访问 [https://marketplace.visualstudio.com/items?itemName=quanzaiyu.vscode-extension-test](https://marketplace.visualstudio.com/items?itemName=quanzaiyu.vscode-extension-test) 就可以看到刚刚发布的扩展。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1603770250330-77a18914-da1d-48b2-958d-579d0f1362fc.png#align=left&display=inline&height=293&originHeight=293&originWidth=1041&size=40000&status=done&style=none&width=1041)

如果想要取消发布，可以使用以下命令：
```bash
vsce unpublish (publisher name).(extension name)
```

<a name="Bv6nS"></a>
## .vscodeignore
如果项目中有不需要发布到应用市场的文件（夹），可以将其添加到`.vscodeignore`中，类似于 `gitignore` <br />举例：
```
**/*.ts
**/tsconfig.json
!file.ts
```

<a name="HfWzi"></a>
## 常见错误
<a name="Tze4s"></a>
### Missing publisher name
错误详情：
```bash
D:\Workplace\temp\vscode-extension-test>vsce publish
 ERROR  Missing publisher name. Learn more: https://code.visualstudio.com/api/working-with-extensions/publishing-extension#publishing-extensions
```
解决方案：<br />在 `package.json` 中添加：
```bash
{
	"publisher": "yourName",
}
```

<a name="0ClYK"></a>
### Make sure to edit the README.md
错误详情：
```bash
D:\Workplace\temp\vscode-extension-test>vsce publish
 INFO  Detected presense of yarn.lock. Using 'yarn' instead of 'npm' (to override this pass '--no-yarn' on the command line).
 ERROR  Make sure to edit the README.md file before you package or publish your extension.
```
解决方案：<br />修改默认的 `README.md`  文件。

<a name="QPrht"></a>
### The Personal Access Token used has expired.
错误详情：
```javascript
ERROR  ﻿{"$id":"1","customProperties":{"Descriptor":null,"IdentityDisplayName":null,"Token":null,"RequestedPermissions":0,"NamespaceId":"00000000-0000-0000-0000-000000000000"},"innerException":null,"message":"Access Denied: The Personal Access Token used has expired.","typeName":"Microsoft.VisualStudio.Services.Security.AccessCheckException, Microsoft.VisualStudio.Services.WebApi","typeKey":"AccessCheckException","errorCode":0,"eventId":3000}
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1606379832929-4294b626-60f1-4871-becb-b2f9087924ac.png#align=left&display=inline&height=154&originHeight=154&originWidth=1456&size=373471&status=done&style=none&width=1456)<br />错误原因：Access token过期<br />解决方案：重新到Azure申请token，并重新使用 `vsce login` 命令登录

<a name="dOcAR"></a>
## 参考资料

- [publishing-extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension#publishing-extensions)
