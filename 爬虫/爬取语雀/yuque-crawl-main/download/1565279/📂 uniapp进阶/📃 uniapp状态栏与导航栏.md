<a name="bc38dd85"></a>
## 状态栏遮挡页面的处理

本地打包时，遇到那么一个问题，状态栏会浮现于页面之前，出现遮挡页面的情况：

![](https://kan.xiaoyulive.top/uniapp/019.png#height=184&id=fmu7V&originHeight=184&originWidth=399&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=399)

解决方案：

在`App.vue`中设置：

```javascript
onLaunch: function() {
    // #ifdef APP-PLUS
    // 全屏显示
    plus.navigator.setFullscreen(true);
    // #endif
}
```

效果如下：

![](https://kan.xiaoyulive.top/uniapp/020.png#height=179&id=dIxmM&originHeight=179&originWidth=391&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=391)

还需要在 `manifest.json` 中配置：

```json
{
    "app-plus" : {
        "statusbar": {
            "immersed": false
        },
    }
}
```

这一段配置是用于解决带有状态栏的页面顶部留有间隔的问题。

<a name="966ed89c"></a>
## 自定义导航栏

先看看自定义导航栏的效果：

![](https://kan.xiaoyulive.top/uniapp/021.png#height=118&id=CybAq&originHeight=118&originWidth=392&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=&width=392)

实现方式：在`pages.json`中，对需要自定义导航栏的页面进行配置：

```json
{
  "pages": [
	{
      "path": "test/test",
      "style": {
        "navigationBarTitleText": "测试",
        "navigationStyle": "default",
        "app-plus": {
            "titleNView": {
                "backgroundColor": "#ff0000",
                "titleText": "测试app-plus",
                "titleColor": "#ffffff",
                "titleSize": "18px",
                "buttons": [{
                        "text": "\ue60b",
                        "fontSrc": "/static/fonts/iconfont/iconfont.ttf",
                        "fontSize": "22px",
                        "float": "left"
                    },
                    {
                        "text": "\ue60b",
                        "fontSrc": "/static/fonts/iconfont/iconfont.ttf",
                        "fontSize": "22px"
                    }
                ]
            }
        }
      }
    }
  ]
}
```

全局导航栏：如果想要每个页面都拥有自定义导航栏，在`pages.json`中的`globalStyle`节点配置即可：

```json
{
  "globalStyle": {
    "navigationStyle": "custom",
    "navigationBarTextStyle": "black",
    "navigationBarTitleText": "app",
    "navigationBarBackgroundColor": "#F8F8F8",
    "backgroundColor": "#F8F8F8",
    "app-plus": {
        "titleNView": {
            "backgroundColor": "#ff0000",
            "titleColor": "#ffffff",
            "titleSize": "18px"
        }
    }
  }
}
```

配置参数详解：

```json
{
    "titleNView": {
        "backgroundColor": "#RRGGBB, 标题栏背景颜色",
        "titleText": "标题栏标题文字内容",
        "titleColor": "#RRGGBB, 标题栏标题文字颜色",
        "titleSize": "17px，标题字体大小，默认大小为17px",
        "autoBackButton": "true|false，是否显示标题栏上返回键",
        "backButton": "JSON对象，标题栏上返回键样式",
        "buttons": [{
            "color": "按钮上的文字颜色",
            "colorPressed": "按钮按下状态的文字颜色",
            "float": "按钮在标题栏上的显示位置",
            "fontWeight": "按钮上文字的粗细",
            "fontSize": "按钮上文字的大小",
            "fontSrc": "按钮上文字使用的字体文件路径",
            "text": "按钮上显示的文字"
        }],
        "splitLine": "JSON对象，标题栏底部分割线样式"
    },
}
```

如果需要监听导航栏按键事件，在对应页面添加以下代码：

```javascript
    onNavigationBarButtonTap:function(e){
        console.log(e.index)
    },
```

通过 `e.index` 区别不同的按钮，下标从0开始

<a name="35808e79"></a>
## 参考资料

- [CSS变量 --status-bar-height](https://uniapp.dcloud.io/frame?id=css%E5%8F%98%E9%87%8F)
- [plus.navigator.setFullscreen](http://www.html5plus.org/doc/zh_cn/navigator.html#plus.navigator.setFullscreen)
- [自定义导航栏使用注意](https://uniapp.dcloud.io/collocation/pages?id=customnav)
- [uni-app导航栏开发指南](https://ask.dcloud.net.cn/article/34921)
- [uni-app导航栏和状态栏配置](https://www.jianshu.com/p/7344c4066e82)
- [manifest.json 规范](https://uniapp.dcloud.io/collocation/manifest?id=app-plus)
- [manifest.json 文档说明](https://ask.dcloud.net.cn/article/94)
- [pages.json app-plus](https://uniapp.dcloud.io/collocation/pages?id=app-plus)
- [pages.json 导航栏](https://uniapp.dcloud.io/collocation/pages?id=app-titlenview)
