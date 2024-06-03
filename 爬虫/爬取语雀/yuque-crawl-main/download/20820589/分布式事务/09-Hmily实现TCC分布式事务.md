<a name="o3uDI"></a>
## 一、业务说明
本实例通过Hmily实现TCC分布式事务，模拟两个账户的转账交易过程。<br />两个账户分别在不同的银行(张三在bank1、李四在bank2)，bank1、bank2是两个微服务。交易过程是，张三给李四转账指定金额。上述交易步骤，要么一起成功，要么一起失败，必须是一个整体性的事务。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652240897973-09b8220c-dace-4b26-8305-8ca9cad15b3e.png#clientId=ue776d265-24ee-4&from=paste&id=ub0e2083b&originHeight=228&originWidth=663&originalType=url&ratio=1&rotation=0&showTitle=false&size=26508&status=done&style=none&taskId=ue91c4d59-09b0-4400-8432-45085cea199&title=)
<a name="fKKDk"></a>
## 2、程序组成部分
Hmily：hmily-springcloud.2.0.4-RELEASE<br />微服务及数据库的关系 ：<br />dtx/dtx-tcc-demo/dtx-tcc-demo-bank1 银行1，操作张三账户， 连接数据库bank1<br />dtx/dtx-tcc-demo/dtx-tcc-demo-bank2 银行2，操作李四账户，连接数据库bank2<br />服务注册中心：dtx/discover-server
<a name="aUtut"></a>
### 2.1、创建数据库
每个数据库都创建try、confirm、cancel三张日志表：
```sql
CREATE TABLE `local_try_log` (
  `tx_no` varchar(64) NOT NULL COMMENT '事务id',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`tx_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `local_confirm_log` (
  `tx_no` varchar(64) NOT NULL COMMENT '事务id',
  `create_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE `local_cancel_log` (
  `tx_no` varchar(64) NOT NULL COMMENT '事务id',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`tx_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
<a name="UjMBI"></a>
### 2.2、maven依赖
```xml
<dependency>
    <groupId>org.dromara</groupId>
    <artifactId>hmily‐springcloud</artifactId>
    <version>2.0.4‐RELEASE</version>
</dependency>
```
<a name="drMjX"></a>
### 2.3、配置hmily
```yaml
org:
  dromara:
    hmily :
      serializer : kryo
      recoverDelayTime : 128
      retryMax : 30
      scheduledDelay : 128
      scheduledThreadMax :  10
      repositorySupport : db
      started: true
      hmilyDbConfig :
        driverClassName  : com.mysql.jdbc.Driver
        url :  jdbc:mysql://localhost:3306/bank?useUnicode=true
        username : root
        password : root
```
新增配置类接收application.yml中的Hmily配置信息，并创建HmilyTransactionBootstrap Bean：
```java
@Bean
    public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyInitService hmilyInitService){
        HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyInitService);
        hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmily.serializer"));
        hmilyTransactionBootstrap.setRecoverDelayTime(Integer.parseInt(env.getProperty("org.dromara.hmily.recoverDelayTime")));
        hmilyTransactionBootstrap.setRetryMax(Integer.parseInt(env.getProperty("org.dromara.hmily.retryMax")));
        hmilyTransactionBootstrap.setScheduledDelay(Integer.parseInt(env.getProperty("org.dromara.hmily.scheduledDelay")));
        hmilyTransactionBootstrap.setScheduledThreadMax(Integer.parseInt(env.getProperty("org.dromara.hmily.scheduledThreadMax")));
        hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
        hmilyTransactionBootstrap.setStarted(Boolean.parseBoolean(env.getProperty("org.dromara.hmily.started")));
        HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
        hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
        hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
        hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
        hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
        hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
        return hmilyTransactionBootstrap;
    }
```
启动类增加@EnableAspectJAutoProxy并增加org.dromara.hmily的扫描项：
```java
@SpringBootApplication
@EnableDiscoveryClient
@EnableHystrix
@EnableFeignClients(basePackages = {"cn.itcast.dtx.tccdemo.bank1.spring"})
@ComponentScan({"cn.itcast.dtx.tccdemo.bank1","org.dromara.hmily"})
public class Bank1TccServer {
 
	public static void main(String[] args) {
		SpringApplication.run(Bank1TccServer.class, args);
	}
}

```
<a name="f3NJN"></a>
## 三、事务业务代码
<a name="y081r"></a>
### 3.1、dtx-tcc-demo-bank1
```shell
try：
  try幂等校验
  try悬挂处理
  检查余额是够扣减金额
  扣减金额
confirm：
  空
cancel：
  cancel幂等校验
  cancel空回滚处理
  增加可用余额
```
dtx-tcc-demo-bank1实现try和cancel方法，如下：
```java
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {
   private Logger logger = LoggerFactory.getLogger(AccountInfoServiceImpl.class);
   
   @Autowired
   private AccountInfoDao accountInfoDao;
    
   @Autowired
   private Bank2Client bank2Client;
    
   @Override
   @Transactional
   @Hmily(confirmMethod = "commit", cancelMethod = "rollback")
   public void updateAccountBalance(String accountNo, Double amount) {
      // 事务id
      String transId = HmilyTransactionContextLocal.getInstance().get().getTransId();
      log.info("******** Bank1 Service  begin try...  "+transId );
      int existTry = accountInfoDao.isExistTry(transId);
      // try幂等校验
      if(existTry>0){
         log.info("******** Bank1 Service 已经执行try，无需重复执行，事务id:{}  "+transId );
         return ;
      }
      // try悬挂处理
      if(accountInfoDao.isExistCancel(transId)>0 || accountInfoDao.isExistConfirm(transId)>0){
         log.info("******** Bank1 已经执行confirm或cancel，悬挂处理，事务id:{}  "+transId);
         return ;
      }
      // 从账户扣减
      if(accountInfoDao.subtractAccountBalance(accountNo ,amount )<=0){
         // 扣减失败
         throw new HmilyRuntimeException("bank1 exception，扣减失败，事务id:{}"+transId);
      }
      // 增加本地事务try成功记录，用于幂等性控制标识
      accountInfoDao.addTry(transId);
      // 远程调用bank2
      if(!bank2Client.test2(amount,transId)){
         throw new HmilyRuntimeException("bank2Client exception，事务id:{}"+transId);
      }
      if(amount==10){ //异常一定要抛在Hmily里面
         throw new RuntimeException("bank1 make exception  10");
      }
      log.info("******** Bank1 Service  end try...  "+transId );
   }
    
    
   @Transactional
   public  void commit( String accountNo, double amount) {
      String localTradeNo = HmilyTransactionContextLocal.getInstance().get().getTransId();
      logger.info("******** Bank1 Service begin commit..."+localTradeNo );
   }
    
    
   @Transactional
   public void rollback( String accountNo, double amount) {
      String localTradeNo = HmilyTransactionContextLocal.getInstance().get().getTransId();
      log.info("******** Bank1 Service begin rollback...  " +localTradeNo);
      // 空回滚处理，try阶段没有执行什么也不用做
      if(accountInfoDao.isExistTry(localTradeNo) == 0){ 
         log.info("******** Bank1 try阶段失败... 无需rollback "+localTradeNo );
         return;
      }
      if(accountInfoDao.isExistCancel(localTradeNo) > 0){ //幂等性校验，已经执行过了，什么也不用做
         log.info("******** Bank1 已经执行过rollback... 无需再次rollback " +localTradeNo);
         return;
      }
      // 再将金额加回账户
      accountInfoDao.addAccountBalance(accountNo,amount);
      // 添加cancel日志，用于幂等性控制标识
      accountInfoDao.addCancel(localTradeNo);
      log.info("******** Bank1 Service end rollback...  " +localTradeNo);
   }
}
```

Feign的远程调用代码：
```java
@FeignClient(value = "seata‐demo‐bank2", fallback = Bank2Fallback.class)
public interface Bank2Client {
    @GetMapping("/bank2/transfer")
    @Hmily
    Boolean transfer(@RequestParam("amount") Double amount);
}
```
<a name="s2c48"></a>
### 3.2、dtx-tcc-demo-bank2
dtx-tcc-demo-bank2实现如下功能：
```shell
try：
  空
confirm：
  confirm幂等校验
  正式增加金额
cancel：
  空
```
```java
@Service
@Slf4j
public class AccountInfoServiceImpl implements AccountInfoService {
   @Autowired
   private AccountInfoDao accountInfoDao;
    
   @Override
   @Transactional
   @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
   public void updateAccountBalance(String accountNo, Double amount) {
      String localTradeNo = HmilyTransactionContextLocal.getInstance().get().getTransId();
      log.info("******** Bank2 Service Begin try ..."+localTradeNo);
   }
    
   @Transactional
   public void confirmMethod(String accountNo, Double amount) {
      String localTradeNo = HmilyTransactionContextLocal.getInstance().get().getTransId();
      log.info("******** Bank2 Service commit...  " +localTradeNo);
      // 幂等性校验，已经执行过了，什么也不用做
      if(accountInfoDao.isExistConfirm(localTradeNo) > 0){ 
         log.info("******** Bank2 已经执行过confirm... 无需再次confirm "+localTradeNo );
         return ;
      }
      //正式增加金额
      accountInfoDao.addAccountBalance(accountNo,amount);
      //添加confirm日志
      accountInfoDao.addConfirm(localTradeNo);
   }
   @Transactional
   public  void cancelMethod(String accountNo, Double amount) {
      String localTradeNo = HmilyTransactionContextLocal.getInstance().get().getTransId();
      log.info("******** Bank2 Service begin cancel...  "+localTradeNo );
   }
}
```
<a name="bMqGU"></a>
## 参考
[分布式事务 Seata TCC 模式深度解析](https://www.bilibili.com/video/BV1pK411s7MS?from=search&seid=10347207598851791940)<br />[<br />](https://www.bilibili.com/video/BV1pK411s7MS?from=search&seid=10347207598851791940)
