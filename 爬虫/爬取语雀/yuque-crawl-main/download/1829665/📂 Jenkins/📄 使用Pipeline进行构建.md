<a name="cUxXf"></a>
## 流水线概述
相关文档：

- [流水线入门](https://www.jenkins.io/zh/doc/book/pipeline/getting-started/)
- [流水线语法](https://www.jenkins.io/zh/doc/book/pipeline/syntax/)

Jenkins 流水线是一套插件，它支持实现和集成持续交付流水线到 Jenkins。流水线提供了一组可扩展的工具，用于通过流水线 DSL 将简单到复杂的交付流水线建模为“代码”。

[声明式和脚本式流水线](https://www.jenkins.io/zh/doc/book/pipeline/#declarative-versus-scripted-pipeline-syntax)都是 DSL 语言，用来描述软件交付流水线的一部分。 脚本式流水线是用一种限制形式的 [Groovy 语法](http://groovy-lang.org/semantics.html)编写的。

流水线可以通过以下任一方式来创建：

- [通过 Blue Ocean](https://www.jenkins.io/zh/doc/book/pipeline/getting-started/#through-blue-ocean) - 在 Blue Ocean 中设置一个流水线项目后，Blue Ocean UI 会帮你编写流水线的 Jenkinsfile 文件并提交到源代码管理系统。
- [通过经典 UI](https://www.jenkins.io/zh/doc/book/pipeline/getting-started/#through-the-classic-ui) - 你可以通过经典 UI 在 Jenkins 中直接输入基本的流水线。
- [在源码管理系统中定义](https://www.jenkins.io/zh/doc/book/pipeline/getting-started/#defining-a-pipeline-in-scm) - 你可以手动编写一个 Jenkinsfile 文件，然后提交到项目的源代码管理仓库中。

使用两种方式定义流水线的语法是相同的。尽管 Jenkins 支持在经典 UI 中直接进入流水线，但通常认为最好的实践是在 `Jenkinsfile` 文件中定义流水线，Jenkins 之后会直接从源代码管理系统加载。

<a name="s8KhD"></a>
## 创建及配置流水线
创建任务的时候，选择“流水线”：<br />![Snipaste_2022-11-12_21-33-50.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668260085180-eeece030-5c0f-411f-98e9-0435fbfde57a.png#averageHue=%23f3f1f1&clientId=uba816b97-dada-4&from=drop&id=u02a1d774&originHeight=799&originWidth=1468&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31968&status=done&style=none&taskId=u46fe07be-e986-4915-ac1d-dc38efc07b3&title=)

进入任务配置界面，找到“流水线”选项卡，进行以下配置：<br />![95b23dd9-ab4e-4eff-8d74-8c09e9dc9ea9.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668260016444-8ff7dcbc-097d-4b4c-a21e-3d6e9edecfdc.png#averageHue=%23f9f9f9&clientId=uba816b97-dada-4&from=drop&id=ubfefa64b&originHeight=1301&originWidth=1217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16535&status=done&style=none&taskId=u1011ce72-83ac-40b4-a7e5-194aac39d24&title=)

Jenkinsfile配置示例：
```bash
pipeline {
    agent any
    stages {
      stage('Test') {
          steps {
            sh whoami
          }
      }
    }
}
```

如果是多分支流水线，可以在“构建配置”中找到Jenkinsfile配置：<br />![Snipaste_2022-11-12_18-07-12.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668247742294-a0f8ab61-23c7-4c92-9eee-4a483aca59f9.png#averageHue=%23f9f9f9&clientId=ue49eb80e-63d4-4&from=drop&id=ubf1dfb1d&originHeight=394&originWidth=1826&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7901&status=done&style=none&taskId=u9318f441-ccab-4b56-b30c-dec4bace4d8&title=)

<a name="kkV7s"></a>
## 在Jenkinsfile中使用Docker作为代理构建
以构建一个Node.js Web应用程序为例。

比如是一个Vite Vue3项目，项目结构如下：<br />![Snipaste_2022-11-12_13-48-15.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668232142768-93d97912-621a-4472-94a4-fe74d4019b2c.png#averageHue=%2326272a&clientId=uef3b5579-c90a-4&from=drop&id=ua6bf7b6d&originHeight=295&originWidth=228&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4816&status=done&style=none&taskId=u25a4c4f9-2f13-4c76-99ab-941e27b4d1d&title=)

Jenkinsfile配置示例：
```yaml
pipeline {
    agent {
      docker {
        image 'node:18-alpine'
      }
    }
    stages {
      stage ('Checkout') {
        steps {
          checkout scm
        }
      }
      stage('Build') {
          steps {
            sh """
              npm config set registry https://registry.npmmirror.com
              npm install
              npm run build
            """
          }
      }
      stage('Deploy') {
          steps {
            // 这里是部署脚本（将构建产物通过SSH上传、生成Docker镜像部署到k8s等）
            sh 'ls -l dist'
          }
      }
    }
}
```

可以看到，需要使用`node:18-alpine`的Docker镜像作为代理。

<a name="FgXuN"></a>
## 错误信息：**Invalid agent type docker specified**
构建时，Jenkins可能会输出如下错误：
```yaml
WorkflowScript: 3: Invalid agent type "docker" specified. Must be one of [any, label, none]
```

![Snipaste_2022-11-12_13-52-23.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668232385036-2a2bf98f-70ad-4e04-8376-b573a0a22271.png#averageHue=%23f2f1f1&clientId=uef3b5579-c90a-4&from=drop&id=u4f3f5d99&originHeight=672&originWidth=1226&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26600&status=done&style=none&taskId=u759fd8ab-9cbf-40cf-9ea4-80630ffd838&title=)

意思是，不能使用docker作为代理进行构建。

解决方案：安装docker相关的jenkins插件（`docker-commons`、`docker-java-api`、`docker-build-step`、`docker-workflow`、`dockerpipline`）

![Snipaste_2022-11-12_10-11-08.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668232482619-b10bf4b5-a83d-49f7-9d6e-51a4306e9306.png#averageHue=%23efeeed&clientId=uef3b5579-c90a-4&from=drop&id=u40b272e4&originHeight=928&originWidth=1854&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36244&status=done&style=none&taskId=ufdec01bb-1924-4dbe-9efb-f9822d758e7&title=)

<a name="EEarA"></a>
## 错误信息：Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
构建时，Jenkins可能会输出如下错误：
```yaml
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

![91e2bc0c-8f73-44cb-9bc7-99ed48b83c77.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668233197205-b2dd27c0-601e-44aa-99c5-b1d82f86d3d8.png#averageHue=%23f0eeee&clientId=uef3b5579-c90a-4&from=drop&id=ue3e1383b&originHeight=495&originWidth=833&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8675&status=done&style=none&taskId=uec3384b9-c4fd-4096-a401-742d5c5d50f&title=)<br />如果直接在容器中执行`docker ps`命令，也是会出现以下错误：
```yaml
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
…………………………………………………………
dial unix /var/run/docker.sock: connect: permission denied
```

:::info
出现此错误的原因是权限不够。
:::

解决方案：

1. 首先在启用Docker容器的时候，必须加上--privileged=true。例：
```bash
docker run --name [ContainerName] -d -p 8888:8888 --privileged=true [ImageName]
```

其中：

- `-d`是在后台运行；
- `-p 8888:8888`表示端口的映射，可以自行修改；
- `--privileged=true`必须加，否则后续操作不生效。

如果是使用`docker-compose.yml`创建（以Docker Desktop for Windows为例），则使用以下格式：
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

2. 在进入容器时，使用 `-u root`使用root用户进入容器：
```
docker exec -it -u root [ContainerID] /bin/bash
```

3. 此时你已经以root身份进入docker容器了 ，就算使用su也不需要输入密码。
```
❯ docker exec -it -u root ecc8247b9cc9aeb539e9b6b96d978390510f75545a8a159e8daf4abcc9416901 /bin/bash
bash-5.1# whoami
root
bash-5.1# cd /var/run
bash-5.1# ls
docker.sock
bash-5.1# chmod 777 docker.sock 
bash-5.1# docker ps
CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS                                               NAMES
ecc8247b9cc9   jenkinsci/blueocean   "/sbin/tini -- /usr/…"   About a minute ago   Up About a minute   50000/tcp, 0.0.0.0:30080->8080/tcp                  jenkins-blueocean
cba2a4a8dba6   gitea/gitea           "/usr/bin/entrypoint…"   13 hours ago         Up 4 hours          0.0.0.0:30022->22/tcp, 0.0.0.0:30081->3000/tcp      gitea       
b86e00f77f3e   mysql:8               "docker-entrypoint.s…"   13 hours ago         Up 4 hours          0.0.0.0:33060->33060/tcp, 0.0.0.0:33306->3306/tcp   gitea_db_1  
bash-5.1#
```

使用 `chmod 777 docker.sock`改变 `docker.sock`的权限，通过 `docker ps`可以查看宿主机中的docker容器，即表示权限修改成功了。

参考：

- [怎样以root权限进入Docker容器_刺客765的博客-CSDN博客_docker root权限](https://blog.csdn.net/Florine113/article/details/121790806) 
- [docker搭建jenkins环境执行宿主机的docker无权限的解决方法_alim2012的博客-CSDN博客_docker jenkins 权限](https://blog.csdn.net/u014595589/article/details/107028711)



