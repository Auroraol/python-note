<a name="e5Jbj"></a>
## 一、业务说明
本示例通过Seata中间件实现分布式事务，模拟三个账户的转账交易过程。两个账户在三个不同的银行(张三在bank1、李四在bank2)，bank1和bank2是两个个微服务。交易过程是，张三给李四转账指定金额。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652238378883-e8c91ab5-7503-4f47-8a32-2f1311f331de.png#clientId=u68846d35-fec6-4&from=paste&id=u3301b7b0&originHeight=126&originWidth=694&originalType=url&ratio=1&rotation=0&showTitle=false&size=15804&status=done&style=none&taskId=u84998b09-a4a4-4a5c-b8ff-5659d3f269f&title=)<br />上述交易步骤，要么一起成功，要么一起失败，必须是一个整体性的事务。
<a name="Na2ze"></a>
## 二、程序组成部分
微服务框架：spring-boot-2.1.3、spring-cloud-Greenwich.RELEASE<br />seata客户端（RM、TM）：spring-cloud-alibaba-seata-2.1.0.RELEASE<br />seata服务端(TC)：seata-server-0.7.1

微服务及数据库的关系 ：<br />dtx/dtx-seata-demo/seata-demo-bank1 银行1，操作张三账户， 连接数据库bank1<br />dtx/dtx-seata-demo/seata-demo-bank2 银行2，操作李四账户，连接数据库bank2<br />服务注册中心：dtx/discover-server

本示例程序技术架构如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652238455459-a0160b5e-394f-4fd8-a01d-f9bcd81c67bb.png#clientId=u68846d35-fec6-4&from=paste&height=293&id=u23f1c03c&originHeight=390&originWidth=652&originalType=url&ratio=1&rotation=0&showTitle=false&size=54031&status=done&style=none&taskId=ud8ad15db-8c07-4e63-846f-3c1049ee4b6&title=&width=489)<br />交互流程如下：<br />1、请求bank1进行转账，传入转账金额。<br />2、bank1减少转账金额，调用bank2，传入转账金额<br />[<br />](https://blog.csdn.net/jokeMqc/article/details/117331251)
<a name="GdWP5"></a>
## 三、代码实现
<a name="jL5HI"></a>
### 3.1、创建数据库
导入数据库脚本：[bank1.sql](https://github.com/huanghe1993/seata-demo/blob/master/sql/bank1.sql)、[bank2.sql](https://github.com/huanghe1993/seata-demo/blob/master/sql/bank2.sql)<br />分别在bank1、bank2库中创建undo_log表，此表为seata框架使用：

<a name="N9Xy1"></a>
### 3.2、启动TC(事务协调器)
（1）下载seata服务器<br />下载地址：[https://github.com/seata/seata/releases/download/v0.7.1/seata-server-0.7.1.zip,](https://github.com/seata/seata/releases/download/v0.7.1/seata-server-0.7.1.zip,)<br />（2）解压并启动
```shell
[seata服务端解压路径]/bin/seata-server.bat -p 8888 -m file
注：其中8888为服务端口号；file为启动模式，这里指seata服务将采用文件的方式存储信息。
```
[<br />](https://blog.csdn.net/jokeMqc/article/details/117331251)
<a name="mXMit"></a>
### 2.3、工程代码导入
discover-server是服务注册中心，测试工程将自己注册至discover-server。<br />dtx-seata-demo是seata的测试工程，根据业务需求需要创建两个dtx-seata-demo工程。<br />dtx/dtx-seata-demo/dtx-seata-demo-bank1 ，操作张三账户，连接数据库bank1<br />dtx/dtx-seata-demo/dtx-seata-demo-bank2 ，操作李四账户，连接数据库bank2<br />代码仓：[https://github.com/huanghe1993/seata-demo/blob/master/dtx/pom.xml](https://github.com/huanghe1993/seata-demo/blob/master/dtx/pom.xml)<br />seat需要使用到pom依赖如下：
```xml
<dependency>
    <groupId>com.alibaba.cloud</groupId>
    <artifactId>spring‐cloud‐alibaba‐dependencies</artifactId>
    <version>2.1.0.RELEASE</version>
    <type>pom</type>
    <scope>import</scope>
</dependency>
```

<a name="kLRPb"></a>
### 2.4、配置seata
在`src/main/resource`中，新增`registry.conf、file.conf`文件，内容可拷贝`seata-server-0.7.1`中的配置文件。在registry.conf中registry.type使用file：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652238983783-a9af87d5-f6cd-433d-9115-047373989beb.png#clientId=u68846d35-fec6-4&from=paste&height=153&id=udd6b5798&originHeight=168&originWidth=602&originalType=binary&ratio=1&rotation=0&showTitle=false&size=20237&status=done&style=none&taskId=ucaf4c9e7-bb71-4185-b685-76e6f328e29&title=&width=547.2727154109106)

 在`file.conf`中更改`service.vgroup_mapping.[springcloud服务名]-fescar-service-group = "default"`，并修改`service.default.grouplist =[seata服务端地址]`<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652239049871-29a27684-369d-4242-a6f2-a43aa348d9a6.png#clientId=u68846d35-fec6-4&from=paste&height=274&id=ubb54046e&originHeight=301&originWidth=952&originalType=binary&ratio=1&rotation=0&showTitle=false&size=58979&status=done&style=none&taskId=uc5b546fa-04bb-4d3b-8791-6efd5c52694&title=&width=865.4545266963238)

关于vgroup_mapping的配置：
```shell
vgroup_mapping.事务分组服务名=Seata Server集群名称（默认名称为default）
default.grouplist = Seata Server集群地址
```
[<br />](https://blog.csdn.net/jokeMqc/article/details/117331251)<br />在` org.springframework.cloud:spring-cloud-starter-alibaba-seata` 的`org.springframework.cloud.alibaba.seata.GlobalTransactionAutoConfiguration` 类中，默认会使用`${spring.application.name}-fescar-service-group `作为事务分组服务名注册到 Seata Server上，如果和`file.conf` 中的配置不一致，会提示 `no available server to connect` 错误,也可以通过配置 `spring.cloud.alibaba.seata.tx-service-group `修改后缀，但是必须和` file.conf `中的配置保持一致。
<a name="ZA7sW"></a>
### 2.5、创建代理数据源
新增DatabaseConfiguration.java，Seata的RM通过DataSourceProxy才能在业务代码的事务提交时，通过这个切入点，与TC进行通信交互、记录undo_log等。
```java
/**
 * 数据源配置
 */
@Configuration
public class DatabaseConfiguration {
 
    @Bean
    @ConfigurationProperties("spring.datasource.ds0")
    public DruidDataSource ds0(){
        DruidDataSource druidDataSource =  new DruidDataSource();
        return druidDataSource;
    }
 
    /**
     * seata框架代理数据源
     * @param ds0
     * @return
     */
    @Primary
    @Bean
    public DataSource dataSource(DruidDataSource ds0)  {
        DataSourceProxy pds0 = new DataSourceProxy(ds0);
        return pds0;
    }
}
```
<a name="fG3BA"></a>
## 四、Seata执行流程
<a name="aptJ0"></a>
### 4.1、正常提交流程
![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652239262797-7b55e3ea-d424-4935-b0dc-b5b51a2ff2e2.png#clientId=u68846d35-fec6-4&from=paste&id=ue3c0aac5&originHeight=813&originWidth=686&originalType=url&ratio=1&rotation=0&showTitle=false&size=83991&status=done&style=none&taskId=ue226f183-3474-462b-b630-0d4ccd0c3bc&title=)
<a name="Kyq3v"></a>
### 4.2、回滚流程
回滚流程省略前的RM注册过程。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652239263046-ac67aab3-5142-4cd3-9e3f-7de3191645db.png#clientId=u68846d35-fec6-4&from=paste&id=ucad02d69&originHeight=889&originWidth=682&originalType=url&ratio=1&rotation=0&showTitle=false&size=94132&status=done&style=none&taskId=u4d2f6ef6-d664-487a-aa1f-30aefc3ba17&title=)<br />要点说明：

1. 每个RM使用DataSourceProxy连接数据库，其目的是使用ConnectionProxy，使用数据源和数据连接代理的目的就是在第一阶段将undo_log和业务数据放在一个本地事务提交，这样就保存了只要有业务操作就一定有undo_log。
2. 在第一阶段undo_log中存放了数据修改前和修改后的值，为事务回滚作好准备，所以第一阶段完成就已经将分支事务提交，也就释放了锁资源。
3. TM开启全局事务开始，将XID全局事务id放在事务上下文中，通过feign调用也将XID传入下游分支事务，每个分支事务将自己的Branch ID分支事务ID与XID关联。
4. 第二阶段全局事务提交，TC会通知各各分支参与者提交分支事务，在第一阶段就已经提交了分支事务，这里各各参与者只需要删除undo_log即可，并且可以异步执行，第二阶段很快可以完成。
5. 第二阶段全局事务回滚，TC会通知各各分支参与者回滚分支事务，通过 XID 和 Branch ID 找到相应的回滚日志，通过回滚日志生成反向的 SQL 并执行，以完成分支事务回滚到之前的状态，如果回滚失败则会重试回滚操作。
<a name="ek11m"></a>
## [<br />](https://blog.csdn.net/jokeMqc/article/details/117331251) 五、主要实现代码
dtx-seata-demo-bank1实现如下功能：1、张三账户减少金额，开启全局事务。2、远程调用bank2向李四转账。
```java
@Service
@Slf4j
public class AccountInfoServiceImpl implements IAccountInfoService {
    @Autowired
    private AccountDao accountDao;
    @Autowired
    private Bank2Client bank2Client;
 
    /**
     * 扣减金额
     * @param accountNo
     * @param amount
     */
    @Override
    @Transactional
    @GlobalTransactional // 开启全局事务
    public void updateAccountBalance(String accountNo, Double amount) {
        log.info("bank1 service begin,XID：{}", RootContext.getXID());
        accountDao.updateAccountBalance(accountNo,amount*-1);
 
        // 远程调用bank2服务进行增加金额
        String transfer = bank2Client.transfer(amount);
        if("fallback".equals(transfer)){
            //调用李四微服务异常
            throw new RuntimeException("调用李四微服务异常");
        }
 
        if(amount == 2){
            //人为制造异常,调试使用
            throw new RuntimeException("bank1 make exception..");
        }
    }
}
```
将`@GlobalTransactional`注解标注在全局事务发起的`Service`实现方法上，开启全局事务：`GlobalTransactionalInterceptor`会拦截`@GlobalTransactional`注解的方法，生成全局事务ID(XID)，XID会在整个<br />分布式事务中传递。在远程调用时，`spring-cloud-alibaba-seata`会拦截Feign调用将XID传递到下游服务。<br />[<br />](https://blog.csdn.net/jokeMqc/article/details/117331251)<br />dtx-seata-demo-bank2实现如下功能：1、李四账户增加金额。dtx-seata-demo-bank2在本账号事务中作为分支事务不使用@GlobalTransactional。
<a name="NScQc"></a>
## 六、小结
Seata实现2PC要点：<br />1、全局事务开始使用 @GlobalTransactional标识 。<br />2、每个本地事务方案仍然使用@Transactional标识。<br />3、每个数据都需要创建undo_log表，此表是seata保证本地事务一致性的关键。<br />[https://github.com/huanghe1993/DistributeTranaction](https://github.com/huanghe1993/DistributeTranaction)
