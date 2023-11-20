<a name="clRjr"></a>
## 通过“构建一个自由风格的软件项目”构建
要构建Node.js项目，需要先安装NodeJS插件。

到“系统管理 -> 插件管理 -> 可选软件”中搜索node，安装[NodeJS插件](https://plugins.jenkins.io/nodejs/)：<br />![Snipaste_2022-11-12_18-58-08.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668251726344-d7bfb532-f45c-4f38-8c49-46714d04716a.png#averageHue=%23fbfbfb&clientId=u15140c47-0d78-4&from=drop&id=ubb9e6e34&originHeight=831&originWidth=1516&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30123&status=done&style=none&taskId=ud8aae586-feb5-4cad-8bb1-6a93cfcaa2f&title=)

安装完成后，重启Jenkins，到 “系统管理 -> 全局功能配置 -> NodeJS”中配置NodeJS环境：<br />![Snipaste_2022-11-12_19-10-51.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668251726355-63b15b04-9c3f-44f8-a29f-eb42816f330b.png#averageHue=%23fefefe&clientId=u15140c47-0d78-4&from=drop&id=u48c4c917&originHeight=1032&originWidth=1302&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20521&status=done&style=none&taskId=udfbca3f6-dcff-4556-a248-af998e1eb77&title=)

在创建NodeJS环境后，通过“构建环境”选择创建的NodeJS环境，在“构建”中选择 `Execute shell`即可使用NodeJS相关的命令。<br />![Snipaste_2022-11-12_19-57-53.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668254351098-fc6ca458-39a1-4f0c-a12a-f2f8c20cc705.png#averageHue=%23f9f9f9&clientId=u15140c47-0d78-4&from=drop&id=ueeac2f41&originHeight=806&originWidth=1248&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15202&status=done&style=none&taskId=u18d28d0f-2108-49de-a06c-2c87187b431&title=)

构建脚本示例：
```bash
npm i -g pnpm
pnpm config set registry https://registry.npmmirror.com

node -v
pnpm -v
pnpm config list

pnpm install
pnpm run build

# 这里将构建好的文件复制到目标目录，可以通过SSH连接传输，或者通过bash脚本、node.js脚本执行，也可以构建Docker镜像运行
cp -r dist/* /data/web/
```

除了使用NodeJS环境，还可以创建JS脚本，使用NodeJS执行，选择“Execute NodeJS script”即可：<br />![Snipaste_2022-11-12_20-03-26.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668256941504-aa618dbe-98e6-4d41-9efc-a4c19466cc8d.png#averageHue=%23fafafa&clientId=u15140c47-0d78-4&from=drop&id=ud583c86a&originHeight=690&originWidth=1220&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11732&status=done&style=none&taskId=u0af96065-06d5-4823-8bdd-622e07ebebd&title=)

<a name="JrTxv"></a>
### node: No such file or directory
参考：[Jenkins env: 'node': No such file or directory](https://blog.csdn.net/Ray_20160915/article/details/102782712)

报错详情：<br />![Snipaste_2022-11-12_20-46-02.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668257216104-91d7fc0c-43d7-4648-982d-ec56e08c6c12.png#averageHue=%23efefef&clientId=u15140c47-0d78-4&from=drop&id=u8d2820f7&originHeight=331&originWidth=1227&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13442&status=done&style=none&taskId=u3b42fadd-5156-404a-90d8-b0528db64b6&title=)

经验证，在Docker中使用NodeJS插件并不能正确使用node.js环境，原因未知。

解决方案：以root身份进入容器安装node.js环境。
```bash
❯ docker exec -u root -it [容器ID] /bin/bash
bash-5.1# apk add nodejs
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86_64/APKINDEX.tar.gz
(1/6) Installing c-ares (1.18.1-r0)
(2/6) Installing libgcc (11.2.1_git20220219-r2)
(3/6) Installing icu-data-en (71.1-r2)
Executing icu-data-en-71.1-r2.post-install
*
* If you need ICU with non-English locales and legacy charset support, install
* package icu-data-full.
*
(4/6) Installing libstdc++ (11.2.1_git20220219-r2)
(5/6) Installing icu-libs (71.1-r2)
(6/6) Installing nodejs (16.17.1-r0)
Executing busybox-1.35.0-r17.trigger
OK: 339 MiB in 95 packages

bash-5.1# node -v
v16.17.1

bash-5.1# apk add npm
(1/1) Installing npm (8.10.0-r0)
Executing busybox-1.35.0-r17.trigger
OK: 350 MiB in 96 packages

bash-5.1# npm -v
8.10.0
```

再次运行任务，运行成功：
```bash
Started by user admin
Running as SYSTEM
Building in workspace /var/jenkins_home/workspace/vite-vue3-free-style
[vite-vue3-free-style] $ /bin/sh -xe /tmp/jenkins7787640950710457777.sh
+ node -v
v16.17.1
+ npm -v
8.10.0
Finished: SUCCESS
```
![Snipaste_2022-11-12_20-52-07.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668257567494-7b4e7183-d544-42fe-9e68-d8ee50f9c910.png#averageHue=%23f1f1f1&clientId=u15140c47-0d78-4&from=drop&id=u267ae627&originHeight=327&originWidth=587&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6238&status=done&style=none&taskId=u0664e4b6-15f9-4928-ae75-e9a007bb13a&title=)

<a name="mMHih"></a>
## 通过流水线构建
<a name="z9iA6"></a>
### 使用Docker镜像node.js作为代理
构建脚本完整示例：
```bash
pipeline {
    agent {
      docker {
        image 'node:18-alpine'
      }
    }
    stages {
      stage ('Checkout Code') {
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

<a name="hoRhi"></a>
### 使用其他Docker镜像安装node.js作为代理
Jenkins脚本示例：
```bash
pipeline {
    agent {
        docker { 
            image 'alpine:3.12.0' 
            args '-u root:root'
        }
    }

    stages {
        stage ('Install dependencies') {
            steps {
                sh "apk add nodejs"
                sh "apk add npm"
                sh "echo $PATH"
            }
        }
        stage('Build') {
            steps {
                sh """
                    node -v
                    npm -v
                """
            }
        }
    }
}
```

这里使用`-u root:root`参数进入容器，以便可以使用apk安装相关应用。

配置示例：<br />![Snipaste_2022-11-12_20-56-22.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668257847919-2012cfe5-8ae6-46e2-98f1-4c8a738dbffb.png#averageHue=%23fbfbfb&clientId=u15140c47-0d78-4&from=drop&id=ucc96b2f6&originHeight=698&originWidth=1217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13282&status=done&style=none&taskId=ua2bf0fc4-8abf-4f19-ad07-27aafe92091&title=)

