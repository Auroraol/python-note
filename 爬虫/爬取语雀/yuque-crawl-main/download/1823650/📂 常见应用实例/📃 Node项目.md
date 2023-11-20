首先创建一个简单的 Koa 应用:

`app.js`

```javascript
const Koa = require('koa');
const app = new Koa();
const path = require('path');
const route = require('koa-route');
const staticFiles = require('koa-static');

const main = staticFiles(path.join(__dirname, 'public'));
console.log(path.join(__dirname, 'public'));

app.use(route.get('/public', main));
app.use(route.get('/', ctx => {
  ctx.response.body = 'Welcome'
}));
app.listen(3000);
```

创建 Dockerfile:

```bash
FROM node:lts-alpine
MAINTAINER quanzaiyu

ADD . /app/
WORKDIR /app

RUN npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/
RUN npm config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs/
RUN npm config set electron_mirror https://npm.taobao.org/mirrors/electron/
RUN npm config set chromedriver_cdnurl https://cdn.npm.taobao.org/dist/chromedriver
RUN npm install
RUN npm rebuild node-sass --force

ENV HOST 0.0.0.0
ENV PORT 3000

EXPOSE 3000

CMD ["node", "app"]
```

打包构建为 Docker 镜像:

```bash
$ docker build -t "731734107/test-koa" .
```

运行测试:

```bash
$ docker run -p 8080:3000 731734107/test-koa
```

将容器中的3000端口映射到宿主机的8080端口, 在宿主机中使用 [http://localhost:8080](http://localhost:8080) 即可访问

推送到 Docker Hub

```bash
$ docker push 731734107/test-koa
```
