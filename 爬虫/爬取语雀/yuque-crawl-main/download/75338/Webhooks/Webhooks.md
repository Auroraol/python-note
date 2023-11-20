<a name="661c71f4"></a>
## 概况

通过配置知识库的 Webhooks 开发者能够获取到指定知识库下所有文档的发布状态。只要该知识库下的文档被发布或更新，会按需触发该知识库下所配置的 Webhooks。

目前仅 **知识库内文档格式 **支持配置 Webhooks。

⚠️ ： **知识库 ** 配置了 「自动发布」功能后，文档的 更新/推送 操作暂不会发送机器人通知。<br />「自动发布」功能具体可以查阅 ： [🙃 看这个按钮不爽很久了](https://www.yuque.com/yuque/blog/nyb4v9?view=doc_embed)
<a name="62382372"></a>
## 
<a name="R7CHL"></a>
## 配置方式

在 **知识库** -> **设置 -> **开发者设置** **页面，会出现 Webhooks 配置地址。

![](https://cdn.nlark.com/yuque/0/2018/png/84137/1545308898454-1dbb7056-fa30-4581-a639-d24b2c6d5256.png#averageHue=%23fbfbfb&height=354&id=HXNHu&originHeight=928&originWidth=1488&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=568)


确保 WebHook 配置的 URL 地址能够被语雀访问到，即要求它能够被互联网网络访问到。


<a name="65939ccd"></a>
## 触发条件

支持触发条件：

- **所有更新触发**：该知识库下的任何一篇文档的更新都会触发 Webhooks


<a name="ce4a77c8"></a>
## 本地开发环境调试

Webhooks 的触发请求是由语雀的服务端发起的，所以你在本地开发环境接入实现 Webhooks 的时候，你可能需要一些额外的工具，将你本地的 HTTP 服务暴露在外网。这样语雀才能请求到。

我们推荐 ngrok 这个工具，安装帮助可参考官方网站：[https://ngrok.com](https://ngrok.com/)

<a name="481feccf"></a>
### 如何使用

启动你的应用 HTTP Server:

```bash
$ rails s
Listening on http://localhost:3000
```

使用 **ngrok** 将 `localhost:3000` 暴露在外网：

```bash
$ ngrok http 3000
ngrok by @inconshreveable                                                       
                                                                                
Session Status                online                                            
Session Expires               7 hours, 59 minutes                               
Update                        update available (version 2.2.8, Ctrl-U to update)
Version                       2.2.4                                             
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    http://bcb8c93a.ngrok.io -> localhost:3000        
Forwarding                    https://bcb8c93a.ngrok.io -> localhost:3000
```

现在你有 `http://bcb8c93a.ngrok.io` 这样一个可以在外部网络访问的地址了。

你可以将它配置在语雀的 Webhooks 界面，例如：

![](https://cdn.yuque.com/yuque/2018/png/84199/1523331630432-6da8d83a-0aa3-497c-98f9-2bc74583ad82.png#averageHue=%23fbfbfb&height=213&id=qt4dQ&originHeight=614&originWidth=1462&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=508)


<a name="4da6e742"></a>
## 语雀回调 Webhooks URL 方式

语雀会使用 HTTP POST 请求 Webhooks URL，具体的 body 是一个 JSON 数据结构，里面包含的 data 数据定义是 [DocDetailSerializer](https://yuque.com/yuque/developer/DocDetailSerializer)，示例如下：

```json
POST http://someone.com/yuque/webhook

{
  "data": DocDetailSerializer
}
```

除了 DocDetailSerializer 中的数据之外，请求 body 中还扩展了三个字段：

- `path` : 文档的完整访问路径（不包括域名）
- `action_type` : 值有 `publish` - 发布、 `update` - 更新
- `publish` : 文档是否为第一次发布，第一次发布时为 `true<br />`

只有首次文档的发布 `publish = true`， `action_type = 'publish'` 之后的发布是更新 `publish = false` ， `action_type = 'update'`。


<a name="3290b598"></a>
## 钉钉机器人

语雀 Webhooks 对[钉钉自定义机器人](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)做了数据适配，如果添加的 Webhooks URL 是钉钉自定义机器人地址，那么会以 [钉钉 link 消息格式](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq#404d04c3)发送该知识库的文档 **发布 **和 **更新 **信息给机器人。由于钉钉开启了机器人的安全设置，需要在“自定义关键词”中添加“语雀”。<br />![配置截图](https://cdn.nlark.com/yuque/0/2020/png/84137/1580627939339-bc8c71eb-9fb1-47c0-b2d8-bf6e2b66d04b.png#averageHue=%23f2f2f2&height=484&id=uGiyy&originHeight=967&originWidth=1102&originalType=binary&ratio=1&rotation=0&showTitle=true&size=265950&status=done&style=none&title=%E9%85%8D%E7%BD%AE%E6%88%AA%E5%9B%BE&width=551 "配置截图")<br />![钉钉上显示效果](https://cdn.nlark.com/yuque/0/2018/png/84137/1537246359489-dfae7658-3bab-4f11-8941-d031d28e4792.png#averageHue=%2376d680&height=341&id=oA8PY&originHeight=614&originWidth=916&originalType=binary&ratio=1&rotation=0&showTitle=true&status=done&style=none&title=%E9%92%89%E9%92%89%E4%B8%8A%E6%98%BE%E7%A4%BA%E6%95%88%E6%9E%9C&width=509 "钉钉上显示效果")






