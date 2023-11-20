Official Jenkins Docker image官方文档：

- [https://github.com/jenkinsci/docker/blob/master/README.md](https://github.com/jenkinsci/docker/blob/master/README.md)
- [https://www.jenkins.io/zh/doc/book/installing/#docker](https://www.jenkins.io/zh/doc/book/installing/#docker)

建议使用的Docker镜像版本：

- `[jenkins/jenkins:lts-jdk11](https://hub.docker.com/r/jenkins/jenkins)`
- `[jenkinsci/blueocean](https://hub.docker.com/r/jenkinsci/blueocean/)`

拉取镜像：
```json
docker pull jenkinsci/blueocean
```

<a name="NqKYN"></a>
## 在Linux中创建
创建并运行容器（Linux）：
```bash
docker run -d --name jenkins-blueocean -p 8080:8080 -p 50000:50000 --privileged=true --restart=on-failure -v jenkins_home:/var/jenkins_home jenkinsci/blueocean
```

其中：

- 8080端口为Web管理界面端口，可以通过浏览器访问
- 50000端口可以不用暴露
- `/var/jenkins_home`为jenkins数据目录，可以暴露到宿主环境

如果创建的时候没加 `-d` 参数，可以在终端中打印初始密码：
```json
*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

5092ae7507b24b6aae198a3bfcdbd394

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
```

<a name="s6Ufq"></a>
## 在Windows中创建
如果是在Windows上，可以通过Docker Desktop可视化创建容器：<br />![Snipaste_2022-11-11_15-15-03.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668151937471-0056babb-d2f0-48f8-9a2d-581d6c2f251e.png#averageHue=%23e9eaed&clientId=u061474d2-df93-4&from=drop&id=u50ce720a&originHeight=748&originWidth=596&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10482&status=done&style=none&taskId=u06d98532-5bff-4795-a0d5-b7f74b23c2c&title=)

当然也可以通过命令行创建：
```bash
docker run -d --name jenkins-blueocean -p 30080:8080 --privileged=true --restart=on-failure -v D:\wsl\docker-desktop-data\jenkins\jenkins_home:/var/jenkins_home jenkinsci/blueocean
```

上面创建的时候，将8080映射到了宿主机的30080端口，因为很多Windows Web服务都使用了8080端口作为入口，避免冲突。

如果是通过Docker Desktop创建的，可以通过日志查看初始密码：<br />![Snipaste_2022-11-11_15-43-36.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668152645235-34f702fe-b64b-4a86-9b93-ca82508e2af2.png#averageHue=%23e1eaf3&clientId=u061474d2-df93-4&from=drop&id=u6b0e811f&originHeight=720&originWidth=1270&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35714&status=done&style=none&taskId=ue2bb69b9-57dd-476f-8f5c-91d96fa02db&title=)

<a name="CH6Hq"></a>
## 通过Docker Compose部署
也可以通过编写`docker-compose.yml`部署
```yaml
version: "3"

services:
  server:
    image: jenkinsci/blueocean
    container_name: jenkins-blueocean
    restart: on-failure
    privileged: true
    volumes:
      - D:\wsl\docker-desktop-data\jenkins\jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "30080:8080"  # web
```

其中：

- `/var/jenkins_home`为jenkins的数据卷
- `/var/run/docker.sock`需要映射到宿主机的`/var/run/docker.sock`才能与宿主机的docker通讯
- `8080`端口为jenkins暴露的web管理后台端口
- `privileged: true`可以通过root用户进入容器修改权限

部署：
```yaml
docker-compose up -d
```

<a name="X0ZYn"></a>
## 初始化Jenkins
容器运行后，通过 [http://localhost:30080](http://localhost:8080/) （具体看映射到宿主机的端口）访问。

首次访问，要求输入管理员密码，就是上面日志中获取到的密码：<br />![Snipaste_2022-11-11_15-16-58.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668152958700-0afa5ac9-9d94-4c3b-9be0-786f0c1e4d85.webp#averageHue=%23fbfaf6&clientId=u061474d2-df93-4&from=drop&id=ue0b205ed&originHeight=914&originWidth=1013&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17836&status=done&style=none&taskId=uad88a081-2ab6-490c-8719-21479056de2&title=)

选择需要安装的插件：<br />![Snipaste_2022-11-11_15-18-51.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668153620357-7a452d99-c9d7-4af8-b38d-e6622ef503f8.webp#averageHue=%23fcfcf9&clientId=u061474d2-df93-4&from=drop&id=u154368b2&originHeight=910&originWidth=1020&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19416&status=done&style=none&taskId=u28984efc-bd2e-424f-93ae-ae85e938f9a&title=)

安装插件：<br />![Snipaste_2022-11-11_15-19-52.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668153639494-646aef85-7e06-4b35-86d6-8b8a5adf6174.webp#averageHue=%23edecef&clientId=u061474d2-df93-4&from=drop&id=u6a68f230&originHeight=903&originWidth=1010&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20062&status=done&style=none&taskId=ub023c504-e1a0-4f42-9ea4-78131534385&title=)

创建管理员：<br />![Snipaste_2022-11-11_15-45-42.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668153657770-7348e1ce-3de6-4f42-adcd-5fff5d3b6d10.webp#averageHue=%23d9e2ec&clientId=u061474d2-df93-4&from=drop&id=u7bd73ff0&originHeight=909&originWidth=1010&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14300&status=done&style=none&taskId=u702fe0ab-6e33-46b1-8888-c5f56a5de5b&title=)

配置实例：<br />![Snipaste_2022-11-11_15-55-11.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668153689728-e61f93e4-bf58-4400-ab1f-ecc9fc9f2521.webp#averageHue=%23fcfcfc&clientId=u061474d2-df93-4&from=drop&id=uc902f4fb&originHeight=910&originWidth=1005&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20288&status=done&style=none&taskId=u18ed1fc3-1c46-4740-9617-a8cb0811aa1&title=)

配置完成：<br />![Snipaste_2022-11-11_15-55-46.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668153708445-15c50867-80c0-4ce5-bfd2-1a939ec36d50.webp#averageHue=%23fcfcfc&clientId=u061474d2-df93-4&from=drop&id=ud76022e0&originHeight=910&originWidth=1011&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8548&status=done&style=none&taskId=u8631641f-cf1f-481c-90bf-921fadee742&title=)

创建完成后，通过 http://localhost:30080 访问Jenkins；通过 [http://localhost:30080/blue](http://localhost:8080/blue) 访问 Blue Ocean。


