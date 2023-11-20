首先创建一个 Vue 应用, 然后打包:

```bash
$ npm run build
```

打包后, 会生成 /dist 目录, 这是构建产物

创建 `default.conf`:

```bash
server {
    listen       80;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
```

创建 Dockerfile:

```dockerfile
FROM hub.c.163.com/library/nginx

MAINTAINER quanzaiyu

RUN rm /etc/nginx/conf.d/default.conf

ADD default.conf /etc/nginx/conf.d/

COPY dist/ /usr/share/nginx/html/
```

注意, 因为引用的基础容器为nginx, 因此这里不需要暴露任何端口

打包构建为 Docker 镜像:

```bash
$ docker build -t "731734107/vue-test" .
```

以上步骤, 结合 Jenkins 会更加容易, 注意, 打包vue是在docker外部完成的, 需要的只是其构建产物

运行测试:

```bash
$ docker run -p 8088:80 731734107/vue-test
```

将容器中的80端口映射到宿主机的8088端口, 在宿主机中使用 [http://localhost:8088](http://localhost:8088) 即可访问

推送到 Docker Hub

```bash
$ docker push 731734107/vue-test
```

