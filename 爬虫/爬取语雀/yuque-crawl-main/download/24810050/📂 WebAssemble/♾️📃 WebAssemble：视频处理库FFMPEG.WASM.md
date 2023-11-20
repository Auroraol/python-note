FFmpeg 是视频处理最常用的开源软件，它功能强大，用途广泛，大量用于视频网站和商业软件（比如 Youtube 和 iTunes），也是许多音频和视频格式的标准编码/解码实现。

借助  WebAssembly 的能力，它现在有了一个 Web 版本：FFMPEG.WASM，让你可以在浏览器里处理视频

官网：<br />[FFMPEG.WASM](https://ffmpegwasm.netlify.app/)

GitHub：<br />[GitHub - ffmpegwasm/ffmpeg.wasm: FFmpeg for browser and node, powered by WebAssembly](https://github.com/ffmpegwasm/ffmpeg.wasm)


<a name="uzXbP"></a>
## 获取FFMPEG.WASM
获取FFMPEG.WASM有多种方法。

我们最终需要的`ffmpeg.wasm`核心文件如下：<br />![Snipaste_2022-02-23_17-22-50.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645608193237-85a66a22-2510-427f-8214-ad471ac96703.png#clientId=u907afeb6-acbe-4&from=drop&id=ud073cbc0&originHeight=333&originWidth=201&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4878&status=done&style=none&taskId=u9183f312-05f2-4567-ba39-e8bb7065d19&title=)

第一种方式：通过源码编译获取<br />首先到[GitHub](https://github.com/ffmpegwasm/ffmpeg.wasm)克隆源码，然后编译出FFMPEG.WASM，步骤如下：
```html
git clone https://github.com/ffmpegwasm/ffmpeg.wasm.git
cd ffmpeg.wasm
yarn
yarn build
```
编译好后，可以在`dist`中找到  `ffmpeg.dev.js` 和 `ffmpeg.min.js`

然后到[GitHub Release](https://github.com/ffmpegwasm/ffmpeg.wasm/releases)下载最新的`ffmpeg-core.wasm`和 `ffmpeg-core.js`。


第二种方式：通过npm安装依赖，从node_modules中提取<br />安装：
```html
yarn add @ffmpeg/ffmpeg @ffmpeg/core
```
然后可以从node_modules中找到我们需要的文件：<br />![Snipaste_2022-02-23_17-18-12.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645607940685-b5689091-7f2a-4708-bf94-5e74f2742260.png#clientId=u907afeb6-acbe-4&from=drop&id=u7d7ef975&originHeight=313&originWidth=296&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4335&status=done&style=none&taskId=u637cd607-39b1-4e76-b615-62996c9e208&title=)

<a name="b7VfE"></a>
## 在浏览器中使用
创建示例文件：
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Title</title>
	<script src="./js/ffmpeg.min.js"></script>
</head>
<body>
	<video id="player" controls></video>
  <script>
    const { createFFmpeg, fetchFile } = FFmpeg;
    const ffmpeg = createFFmpeg({
        corePath: "./js/ffmpeg-core.js",
        log: true,
    });
    (async () => {
      await ffmpeg.load();

      const dataInputVideo = await fetchFile('data/input.mp4');
      ffmpeg.FS('writeFile', 'input.mp4', dataInputVideo);
      await ffmpeg.run('-i', 'input.mp4', 'output.mp4');

      const data = ffmpeg.FS('readFile', 'output.mp4');
      const video = document.getElementById('player');
      video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
    })();
  </script>
</body>
</html>
```
需要本地测试的话，可以创建一个express服务`server.js`，运行命令`node server`（详见：[关于SharedArrayBuffer报错的处理](#C3ToD)）

运行到浏览器，可以看到控制台疯狂输出，说明在对视频做处理：<br />![Snipaste_2022-02-23_17-28-31.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645608533304-2986d57e-8c09-44f4-afd0-cb31e957df43.png#clientId=u907afeb6-acbe-4&from=drop&id=u5fddb95d&originHeight=892&originWidth=1071&originalType=binary&ratio=1&rotation=0&showTitle=false&size=29022&status=done&style=none&taskId=ue5e23692-31d1-46e2-82a1-3454cb34e81&title=)<br />这个处理是本地执行的，浏览器将`wasm`下载到本地，浏览器再执行相关操作。<br />![Snipaste_2022-02-23_17-31-58.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645608739699-2650b26a-db50-4cc4-8935-8a46b9d7fb4b.png#clientId=u907afeb6-acbe-4&from=drop&id=uf5dc914c&originHeight=278&originWidth=1006&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10325&status=done&style=none&taskId=uf1dc3c64-56cf-423a-8d2d-e74a53cbf4b&title=)<br />以上示例，是直接读取了项目下的 `data/input.mp4`文件，输出到 `output.mp4`，没有实际意义，只是一个演示。

通常我们会通过input框读取用户选择的文件：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./js/ffmpeg.min.js"></script>
</head>
<body>
  <video id="player" controls></video>
  <input type="file" id="uploader" placeholder="choose file">
  <script>
    const { createFFmpeg, fetchFile } = FFmpeg;
    const ffmpeg = createFFmpeg({
      corePath: "./js/ffmpeg-core.js",
      log: true
    });
    const transcode = async ({ target: { files } }) => {
      const { name } = files[0];
      await ffmpeg.load();
      ffmpeg.FS('writeFile', name, await fetchFile(files[0]));
      await ffmpeg.run('-i', name, 'output.mp4');
      const data = ffmpeg.FS('readFile', 'output.mp4');
      const video = document.getElementById('player');
      video.src = URL.createObjectURL(new Blob([data.buffer], { type: 'video/mp4' }));
    }
    document.getElementById('uploader').addEventListener('change', transcode);
  </script>
</body>
</html>
```

<a name="xqcsS"></a>
## 在Node.js中使用
```javascript
const fs = require('fs');
const { createFFmpeg, fetchFile } = require('@ffmpeg/ffmpeg');
const ffmpeg = createFFmpeg({ log: true });
(async () => {
  await ffmpeg.load();
  ffmpeg.FS('writeFile', 'input.mp4', await fetchFile('./data/input.mp4'));
  await ffmpeg.run('-i', 'input.mp4', 'output.mp4');
  await fs.promises.writeFile('./output.mp4', ffmpeg.FS('readFile', 'output.mp4'));
  process.exit(0);
})();
```

<a name="YCYb4"></a>
## FFMPEG.WASM使用方式
ffmpeg常用的参数都可以使用，参考：<br />[📃 使用FFMPEG实现音视频处理](https://www.yuque.com/xiaoyulive/services/sqxr9f?view=doc_embed&inner=aJl23)

通过`ffmpeg.run`调用即可，每个参数分开传递。<br />示例：
```javascript
// 命令行： ffmpeg -i input.mp4 -s 720x480 output.mp4
await ffmpeg.run('-i', name, '-s', '400x600', 'output.mp4');
```

不过现在支持的格式有限，并不是所有音视频格式都是支持的，支持列表参考：[Proposed Encoders / Decoders Libraries](https://github.com/ffmpegwasm/ffmpeg.wasm/issues/61)

<a name="PUIvO"></a>
## 常见错误
<a name="g5MHZ"></a>
### 关于SharedArrayBuffer报错的处理
如果直接打开引入FFMPEG.WASM的html页面，浏览器会报以下错误：
```javascript
Uncaught (in promise) ReferenceError: SharedArrayBuffer is not defined
```
![Snipaste_2022-02-23_15-54-40.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645602912239-0cf91a0f-b325-43e7-8ef6-e5aff51505aa.png#clientId=u907afeb6-acbe-4&from=drop&id=u8531fe98&originHeight=142&originWidth=612&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5191&status=done&style=none&taskId=u18349a8e-4f08-4be2-8599-6eb605d6b74&title=)

这是官方的解决方案：
```javascript
SharedArrayBuffer is only available to pages that are cross-origin isolated. So you need to host your own server with Cross-Origin-Embedder-Policy: require-corp and Cross-Origin-Opener-Policy: same-origin headers to use ffmpeg.wasm.
```

意思是，需要在服务端配置两个响应头：
```javascript
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

比如我们可以使用express开启一个静态服务：`server.js`
```javascript
const express = require('express');
const app = express();

app.use((_, res, next) => {
  res.header('Cross-Origin-Opener-Policy', 'same-origin');
  res.header('Cross-Origin-Embedder-Policy', 'require-corp');
  next();
});

app.use(express.static('./'));

const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}...`);
});
```

将需要加载的html文件放于`server.js`同级目录，运行 `node server.js`，默认运行到8080端口下。

效果如下：<br />![Snipaste_2022-02-23_15-53-05.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1645602804629-fd5c21ee-8ef3-47d2-98df-b4709df5f8ab.png#clientId=u907afeb6-acbe-4&from=drop&id=u3919fff1&originHeight=478&originWidth=439&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11327&status=done&style=none&taskId=ub421f6e5-a5fe-46b4-b1d6-6d7bd80f078&title=)

<a name="zFft7"></a>
### error:0308010C:digital envelope routines::unsupported
在运行[官方vue示例](https://github.com/ffmpegwasm/vue-app)的时候，可能会报以下错误
```javascript
error:0308010C:digital envelope routines::unsupported
```
解决方案为降低Node.js到17以下。

如果想要在Node.js 17以上临时解决，可以临时设置环境变量：
```bash
set NODE_OPTIONS=--openssl-legacy-provider # windows
export NODE_OPTIONS=--openssl-legacy-provider # linux
```

<a name="sWJEO"></a>
## 参考资料

- [借助ffmpeg.wasm纯前端实现多音频和视频的合成](https://www.zhangxinxu.com/wordpress/2021/03/ffmpeg-wasm-audio-video-merge/)
- [wasm + ffmpeg实现前端截取视频帧功能](https://zhuanlan.zhihu.com/p/40786748)



