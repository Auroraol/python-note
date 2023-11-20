Official Gitea Docker image官方文档：

- [https://docs.gitea.io/en-us/install-with-docker/](https://docs.gitea.io/en-us/install-with-docker/)
- [https://docs.gitea.io/zh-cn/install-with-docker/](https://docs.gitea.io/zh-cn/install-with-docker/)

建议使用的Docker镜像版本：

- [gitea/gitea](https://hub.docker.com/r/gitea/gitea)

拉取镜像：
```json
docker pull gitea/gitea
```

<a name="KkZgm"></a>
## 通过Docker Compose部署
<a name="aKriw"></a>
### 最简部署方案
```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    networks:
      - gitea
    volumes:
      - D:\wsl\docker-desktop-data\gitea\data:/data
      - D:\wsl\docker-desktop-data\gitea\timezone:/etc/timezone:ro
      - D:\wsl\docker-desktop-data\gitea\localtime:/etc/localtime:ro
      - D:\wsl\docker-desktop-data\gitea\.ssh:/data/git/.ssh
    ports:
      - "30081:3000"  # web
      - "30022:22"    # SSH
```

部署：
```yaml
docker-compose up -d
```

<a name="RkWjr"></a>
### 使用 MySQL 数据库
```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=db:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea
    restart: always
    networks:
      - gitea
    volumes:
      - D:\wsl\docker-desktop-data\gitea\data:/data
      - D:\wsl\docker-desktop-data\gitea\timezone:/etc/timezone:ro
      - D:\wsl\docker-desktop-data\gitea\localtime:/etc/localtime:ro
      - D:\wsl\docker-desktop-data\gitea\.ssh:/data/git/.ssh
    ports:
      - "30081:3000"  # web
      - "30022:22"    # SSH
    depends_on:
      - db

  db:
    image: mysql:8
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=gitea
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=gitea
      - MYSQL_DATABASE=gitea
    networks:
      - gitea
    volumes:
      - ./mysql:/var/lib/mysql
    ports:
      - "33306:3306"
      - "33060:33060"
```

部署：
```yaml
docker-compose -f docker-compose-with-mysql.yml up -d
```

<a name="Vj3wG"></a>
### 使用 PostgreSQL 数据库
```yaml
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: gitea/gitea
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=postgres
      - GITEA__database__HOST=db:5432
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea
    restart: always
    networks:
      - gitea
    volumes:
      - D:\wsl\docker-desktop-data\gitea\data:/data
      - D:\wsl\docker-desktop-data\gitea\timezone:/etc/timezone:ro
      - D:\wsl\docker-desktop-data\gitea\localtime:/etc/localtime:ro
      - D:\wsl\docker-desktop-data\gitea\.ssh:/data/git/.ssh
    ports:
      - "30081:3000"  # web
      - "30022:22"    # SSH
    depends_on:
      - db

  db:
    image: postgres:14
    restart: always
    environment:
      - POSTGRES_USER=gitea
      - POSTGRES_PASSWORD=gitea
      - POSTGRES_DB=gitea
    networks:
      - gitea
    volumes:
      - ./postgres:/var/lib/postgresql/data
```

部署：
```yaml
docker-compose -f docker-compose-with-postgresql.yml up -d
```

以上演示了三种创建方式，选择适合自己的方式部署即可。

<a name="WSP5K"></a>
## 初始化Gitea
容器运行后，浏览器访问 [http://localhost:30081/](http://localhost:30081/)

第一次进请进行初始化配置：<br />![网页捕获_11-11-2022_23930_localhost_爱奇艺.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1668180263229-aff8eff6-0121-488a-bb78-f4e039c61ef6.webp#averageHue=%23e6e7e4&clientId=u3f0471c2-458b-4&from=drop&height=1159&id=uaa6f5a14&originHeight=1643&originWidth=1741&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44302&status=done&style=none&taskId=u9be2dc29-e87b-49a1-92c6-613327f8815&title=&width=1228)

以上配置可以通过 `/data/gitea/conf/app.ini`修改。

配置好后，可以访问Gitea主页面：<br />![Snipaste_2022-11-11_23-19-15.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668180427629-16d6fc6f-f037-431d-92d6-30fc56a8e06d.png#averageHue=%23faf9f9&clientId=u3f0471c2-458b-4&from=drop&id=u69d4a945&originHeight=891&originWidth=1563&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27863&status=done&style=none&taskId=u350c3b8a-2ff4-449f-b44d-d59b392c675&title=)

用户主页面：<br />![Snipaste_2022-11-11_23-12-42.png](https://cdn.nlark.com/yuque/0/2022/png/2213540/1668180413892-f6506c95-6077-4c0a-9593-683192fa09a7.png#averageHue=%23fcfcfc&clientId=u3f0471c2-458b-4&from=drop&id=u1e61cab5&originHeight=428&originWidth=903&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19513&status=done&style=none&taskId=u1f494d3a-5125-44f1-9ebb-2626a0ca540&title=)



