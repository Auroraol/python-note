<a name="L2Vgj"></a>
## 一、什么是TCC事务
TCC是Try、Confirm、Cancel三个词语的缩写，TCC要求每个分支事务实现三个操作 ：预处理Try、确认Confirm、撤销Cancel。Try操作做业务检查及资源预留，Confirm做业务确认操作，Cancel实现一个与Try相反的操作既回滚操作。TM首先发起所有的分支事务的try操作，任何一个分支事务的try操作执行失败，TM将会发起所有分支事务的Cancel操作，若try操作全部成功，TM将会发起所有分支事务的Confirm操作，其中Confirm/Cancel操作若执行失败，TM会进行重试。

![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652183600343-21ee4eb4-c0a4-4ae7-9651-260440e70ce2.jpeg#clientId=u74d61d4e-417b-4&from=paste&id=u7c9811e2&originHeight=294&originWidth=720&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ud677ba83-793b-46e1-b9f1-ed865d1876f&title=)

分支事务失败的情况 ：

![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652183601331-94eb410d-d2da-4865-a419-ebabfe2fe024.jpeg#clientId=u74d61d4e-417b-4&from=paste&id=u8e56fefd&originHeight=312&originWidth=720&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u57e8b72d-bf1c-4710-a6ba-9622ac3eb88&title=)<br />TCC分为三个阶段 ：

1. Try阶段是做业务检查（一致性）及资源预留（隔离），此阶段仅是一个初步操作，它和后续的Confirm一起才能真正构成一个完整的业务逻辑。
2. Confirm阶段是做确认提交，Try阶段所有分支事务执行成功后开始执行Confirm。通常情况下，采用TCC则认为Confirm阶段是不会出错的。即 ：只要Try成功，Confirm一定成功。若Confirm阶段真的出错了，需引入重试机制或人工处理。
3. Cancel阶段是在业务执行错误需要回滚的状态下执行分支事务的业务取消，预留资源释放。通常情况下，采用TCC则认为Cancel阶段也是一定成功的。若Cancel阶段真的出错了，需引入重试机制或人工处理。
4. TM事务管理器<br />TM事务管理器可以实现为独立的服务，也可以让全局事务发起方充当TM的角色，TM独立出来是为了成为公用组件，是为了考虑结构和软件复用。<br />TM在发起全局事务时生成全局事务记录，全局事务ID贯穿整个分布式事务调用链条，用来记录事务上下文，追踪和记录状态，由于Confirm和Cancel失败需进行重试，因此需要实现为幂等性是指同一个操作无论请求多少次，其结果都相同。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652233540286-4142396e-954e-479e-ba85-112dbdcd8724.png#clientId=u1bcc94a8-d8be-4&from=paste&height=398&id=u14c7ddac&originHeight=438&originWidth=810&originalType=binary&ratio=1&rotation=0&showTitle=false&size=38493&status=done&style=none&taskId=ud4d92e5f-fad5-475a-b746-bac613ba70f&title=&width=736.3636204033847)
<a name="Hg5sd"></a>
## 二、TCC解决方案
目前市面上的TCC框架众多比如下面这几种 ：<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652183787284-fc8586e7-fef5-45a3-b122-a3eba7d2c36e.jpeg#clientId=u74d61d4e-417b-4&from=paste&id=u79372863&originHeight=209&originWidth=720&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ua74e1452-3341-419c-9a98-e45431bc5b3&title=)<br />Seata也支持TCC，但Seata的TCC模式对Spring Cloud并没有提供支持。我们的目标是理解TCC原理以及事务协调运作的过程，因此更倾向于轻量级易于理解的框架。

Hmily是一个高性能分布式事务TCC开源框架。基于Java语言来开发（JDK1.8），支持Dubbo，Spring Cloud等RPC框架进行分布式事务。它目前支持以下特性 ：

- 支持嵌套事务（Nested transaction support）。
- 采用disruptor框架进行事务日志的异步读写，与RPC框架的性能毫无差别。
- 支持SpringBoot-starter项目启动，使用简单。
- RPC框架支持 ：dubbo、motan、springcloud。
- 本地事务存储支持 ：redis、mongodb、zookeeper、file、mysql。
- 事务日志序列化支持 ：java、hessian、kryo、protostuff。
- 采用Aspect AOP切面思想与Spring无缝集成，天然支持集群。
- RPC事务恢复，超时异常恢复等。

Hmily利用AOP对参与分布式事务的本地方法与远程方法进行拦截处理，通过多方拦截，事务参与者能透明的调用到另一方的Try、Confirm、Cancel方法；传递事务上下文；并记录事务日志，酌情进行补偿，重试等。<br />Hmily不需要事务协调服务，但需要提供一个数据库（mysql/mongodb/zookeeper/redis/file）来进行日志存储。

Hmily实现的TCC服务与普通的服务一样，只需要暴露一个接口，也就是它的Try业务。Confirm/Cancel业务逻辑，只是因为全局事务提交/回滚的需要才提供的，因此Confirm/Cancel业务只需要被Hmily TCC事务框架发现即可，不需要被调用它的其他业务服务所感知。

<a name="uWMHH"></a>
## **三、TCC需要注意三种异常处理**
<a name="uFYxZ"></a>
### 3.1、空回滚 
空回滚：当某分支事务的try阶段阻塞时，可能导致全局事务超时而触发二阶段的cancel操作。在未执行try操作时先执行了cancel操作，这时cancel不能做回滚，就是**空回滚**。<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652184589253-164ab77a-b1bf-481d-bc40-feafc01f047e.jpeg#clientId=u74d61d4e-417b-4&from=paste&id=u37400a05&originHeight=414&originWidth=746&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u2e0b2fdb-0043-4800-8919-40ff59a9d84&title=)<br />[https://image-1-1257237419.cos.ap-chongqing.myqcloud.com/img/TCC111.gif](https://image-1-1257237419.cos.ap-chongqing.myqcloud.com/img/TCC111.gif)<br />**空回滚情况：**<br />	上方调用分支按照TCC流程正常执行，此时下方调用分支因为某种原因而阻塞了，由于长时间没有执行，这个分支发生了超时错误，由TM经过2.1步骤发送超时错误，回滚全局事务的指令给TC，TC检查分支状态2.2，发现确实有一只分支超时，发送2.3回滚指令到各分支的RM，由RM执行2.4cancel操作。

	此时对于第一个分支而言，执行cancel没有问题，因为流程正常。但对于第二个分支而言，他并没有执行第一步的try，所以此时第二个分支不能真正的执行cancel，需要执行空回滚，也就是说返回一个正常状态，且不报错。需要在cancel之前查看是否有前置的try，如果没有执行try则需要空回滚。

解决思路关键就是：要识别出这个空回滚。思路很简单就是需要知道第一阶段是否执行，如果执行了，那就是正常回滚；如果没执行，那就是空回滚。<br />前面已经说过TM在发起全局事务时生成全局事务记录，全局事务ID贯穿整个分布式事务调用链条。再额外增加一张分支事务记录表，其中有全局事务ID和分支事务ID，第一阶段Try方法里会插入一条记录，表示第一阶段执行了。Cancel接口里读取该记录，如果该记录存在，则正常回滚；如果该记录不存在，则是空回滚。
<a name="OcFlW"></a>
### 3.2、悬挂
悬挂就是对于一个分布式事务，其二阶段Cancel接口比Try接口先执行。<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652184804157-5ac5643c-3a5c-419d-9147-a45b1f5ad2da.jpeg#clientId=u74d61d4e-417b-4&from=paste&id=udb589a0a&originHeight=416&originWidth=746&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u79ac47fc-5a7c-4a81-8217-d17a3246aeb&title=)<br />悬挂的意思是：Cancel 比 Try 接口先执行，出现的原因是 Try 由于网络拥堵而超时，事务管理器生成回滚，触发 Cancel 接口，而最终又收到了 Try 接口调用，但是 Cancel 比 Try 先到。按照前面允许空回滚的逻辑，回滚会返回成功，事务管理器认为事务已回滚成功，则此时的 Try 接口不应该执行，否则会产生数据不一致，所以我们在 Cancel 空回滚返回成功之前先记录该条事务 xid 或业务主键，标识这条记录已经回滚过，Try 接口先检查这条事务xid或业务主键如果已经标记为回滚成功过，则不执行 Try 的业务操作。

假设在上方的基础上，下方分支的阻塞畅通了，此时他执行1.4去锁定资源(try)，但整个事务都已经回滚结束了，所以他不会执行第二阶段，但冻结了资源，这种情况应该进行避免。需要在try操作之前查看当前分支是否已经回滚过，如果已经回滚过则不能在执行try命令。

解决思路是：如果二阶段执行完成，那一阶段就不能再继续执行。在执行一阶段事务时判断在该全局事务下，“分支事务记录”表中是否已经有二阶段事务记录，如果有则不执行Try。<br />[https://benym.cn/archives/327/](https://benym.cn/archives/327/)
<a name="vpsqk"></a>
## <br />
