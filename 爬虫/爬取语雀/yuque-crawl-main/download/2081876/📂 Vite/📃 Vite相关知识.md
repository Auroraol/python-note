<a name="T27ms"></a>
## 一、环境变量
使用 `--mode` 参数指定环境变量，比如：
```java
vite --mode development
```
这样的话，vite将查找项目下的 `.env.development` 文件，并获取其中的环境变量设置。

比如 `.env.development` 内容如下：
```java
NODE_ENV=development
```

在程序中就可以获取到此环境变量设置：
```javascript
console.log(process.env.NODE_ENV)
```

<a name="9xeFo"></a>
## 二、可选链
在Vite中不需要进行任何配置即可使用可选链：
```javascript
...

if (token?.access_token) {
  router.push("/home")
} else {
  router.push("/login")
}
```

