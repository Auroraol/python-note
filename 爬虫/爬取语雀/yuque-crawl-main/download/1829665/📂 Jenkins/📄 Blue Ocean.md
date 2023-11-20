官方文档：

- [https://www.jenkins.io/zh/doc/book/blueocean/getting-started/](https://www.jenkins.io/zh/doc/book/blueocean/getting-started/)

如果你刚接触 Jenkins 流水线，Blue Ocean UI 可以帮助你设置流水线项目，并通过图形化流水线编辑器为你自动创建和编写流水线（即 Jenkinsfile）。<br />作为在 Blue Ocean 中设置流水线项目的一部分，Jenkins 给你项目的源代码管理仓库配置了一个安全的、经过身份验证的适当的连接。因此，你通过 Blue Ocean 的流水线编辑器在 Jenkinsfile 中做的任何更改都会自动的保存并提交到源代码管理系统。

<a name="O3XXp"></a>
## 创建流水线
在流水线列表可以看到所有流水线任务，点击“创建流水线”，进入可视化创建流水线任务界面：<br />![Snipaste_2022-11-14_21-43-29.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440990612-d0e2e99c-6cda-41ec-bdb3-5ba473379f3e.png#averageHue=%23efd28d&clientId=ufe834b5e-e476-4&from=drop&id=x00Hc&originHeight=428&originWidth=1252&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10158&status=done&style=none&taskId=ueba16c77-f84a-4c0a-9e37-11df04d57f9&title=)

创建流水线，先选择代码仓库，再为流水线取个名字：<br />![Snipaste_2022-11-14_21-32-38.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440990607-cfb5dee2-56d8-471d-aec7-4239e42015b4.png#averageHue=%23fdfdfd&clientId=ufe834b5e-e476-4&from=drop&id=u26db8b9d&originHeight=1223&originWidth=1239&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26181&status=done&style=none&taskId=u1b238550-50e0-4a9f-a98a-2e8ad1b3cf3&title=)<br />如果git项目拥有Jenkinsfile，则自动使用此文件进行流水线作业。

如果连接的是GitHub，需要先创建[GitHub Access Token](https://github.com/settings/tokens)<br />![Snipaste_2022-11-15_23-17-05.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668526955521-d722c955-1af9-42ee-af9b-7c1ee060316e.png#averageHue=%23fcfcfc&clientId=u31672b38-5d77-4&from=drop&id=oQvKu&originHeight=1199&originWidth=927&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24282&status=done&style=none&taskId=ud0e41bb3-f1da-439b-bf61-1db9994cc0c&title=)

<a name="wuK8l"></a>
## 可视化创建流水线
参考：[流水线编辑器](https://www.jenkins.io/zh/doc/book/blueocean/pipeline-editor/)

如果项目中没有Jenkinsfile，流水线可以为项目创建可视化创建流水线<br />![Snipaste_2022-11-14_23-55-17.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668441412058-eabeb2b1-50f2-4c8f-9e57-e3210815615c.png#averageHue=%23ecd7ab&clientId=ufe834b5e-e476-4&from=drop&id=dzn2A&originHeight=570&originWidth=1195&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12448&status=done&style=none&taskId=u899268df-7f84-4301-9f4a-602dd4f5077&title=)

可视化创建流水线：<br />![Snipaste_2022-11-15_23-23-09.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668526955530-9104ee57-6837-4643-973d-42fe47bc75ea.png#averageHue=%23fdfdfd&clientId=u31672b38-5d77-4&from=drop&id=oAJW5&originHeight=652&originWidth=1555&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11368&status=done&style=none&taskId=u92cb9d44-2226-48a8-8d41-d5cec4a5d05&title=)<br />注意：凭证必须有写权限才可创建Jenkinsfile，否则会报权限错误。

<a name="KBGNG"></a>
## 运行流水线
创建完成后，流水线自动开始运行：<br />![Snipaste_2022-11-14_21-33-32.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440990606-eef5a48b-857e-4ad8-ba7f-cb60a70d6e09.png#averageHue=%23f9f7dd&clientId=ufe834b5e-e476-4&from=drop&id=u30482211&originHeight=266&originWidth=1214&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7617&status=done&style=none&taskId=ufa50c707-1fc7-46f7-a7d0-95578ca9a75&title=)

<a name="pMxpf"></a>
## 查看运行结果
流水线运行结果：<br />![Snipaste_2022-11-14_21-42-16.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668440990609-6f4aee69-d28d-43bc-814e-5ee2ea2f9b06.png#averageHue=%23a2a2a1&clientId=ufe834b5e-e476-4&from=drop&id=ufabdf47e&originHeight=775&originWidth=1841&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25125&status=done&style=none&taskId=u64be0467-0fc4-4838-9df4-c9ee6646db4&title=)

<a name="VHAeM"></a>
## 

