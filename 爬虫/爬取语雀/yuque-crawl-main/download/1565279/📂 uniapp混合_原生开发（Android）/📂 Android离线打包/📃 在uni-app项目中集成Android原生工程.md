按照官方的方案，我们如果进行本地打包的话，需要重新创建一个Android原生工程，于是就会导致我们管理多个项目，切来切去的也麻烦。

经过一番折腾，觉得完全可以像React Native一样，在同一个项目中集成uni-app和Android两个项目。

具体操作如下。

1. 在uniapp项目下创建一个platforms目录，再在此目录下创建一个android目录
2. 将Android原生工程拷到`platforms/android`下，目录结构如下

![image.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1669259825754-902e5664-eb0d-4657-85e4-01c92f6853ea.png#averageHue=%2325292d&clientId=ucb6a501d-2725-4&from=paste&height=604&id=u7fdb8a60&originHeight=604&originWidth=322&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28962&status=done&style=none&taskId=u7ca195fd-f6a6-4b69-81d5-728d37672ff&title=&width=322)

3. 在`.gitignore`中添加：

```
# Android
*.apk
*.iml
.gradle
platforms/android/local.properties

# package
platforms/android/app/build
platforms/android/app/release
platforms/android/app/src/main/assets/apps
```

4. 修改`package.json`：

```json
{
  "scripts": {
    //...
    "build:app-plus": "cross-env NODE_ENV=production UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=platforms/android/app/src/main/assets/apps/__UNI__84417FE/www vue-cli-service uni-build",
    "dev:app-plus": "cross-env NODE_ENV=development UNI_PLATFORM=app-plus UNI_OUTPUT_DIR=platforms/android/app/src/main/assets/apps/__UNI__84417FE/www vue-cli-service uni-build --watch",
  },
  // ...
}
```

在 `build:app-plus` 和 `dev:app-plus` 中添加 `UNI_PLATFORM` 选项，指定输入目录为Android项目下的资源路径，其中`__UNI__84417FE` 是uniapp的appid，需要换为自己项目的appid。

ok，完成，这样就可以了。
