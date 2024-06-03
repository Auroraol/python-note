<a name="wXsvj"></a>
# 一. Spring事务分类
Spring 提供了两种事务管理方式：声明式事务管理和编程式事务管理。
<a name="sgVt9"></a>
## 1. 编程式事务
在 Spring 出现以前，编程式事务管理对基于 POJO 的应用来说是唯一选择。我们需要在代码中显式调用 beginTransaction()、commit()、rollback() 等事务管理相关的方法，这就是编程式事务管理。<br />简单地说，编程式事务就是在代码中显式调用开启事务、提交事务、回滚事务的相关方法。
<a name="OtjJr"></a>
## 2. 声明式事务
Spring 的声明式事务管理是建立在 Spring AOP 机制之上的，其本质是对目标方法前后进行拦截，并在目标方法开始之前创建或者加入一个事务，在执行完目标方法之后根据执行情况提交或者回滚事务。而Spring 声明式事务可以采用 **基于 XML 配置** 和 **基于注解** 两种方式实现<br />简单地说，声明式事务是编程式事务 + AOP 技术包装，使用注解进行扫包，指定范围进行事务管理。
<a name="nOQcg"></a>
# 二、Spring声明式事务配置
在配置文件上加入注解 @EnableTransactionManagement
```java
@ComponentScan("com.huanghe")
@EnableTransactionManagement // 开启注解事务
public class AppConfig {
}
```
在使用的地方加上注解 `@Transactional`，该注解可以加在类上，也可以加在方法上
```java
@Transactional(isolation = Isolation.SERIALIZABLE)
public int insertUser(User user){
    return userDao.insertUser(user);
}
```
<a name="UxmXb"></a>
## @Transactional注解含义
| 参数 | 含义 |
| --- | --- |
| isolation | 事务隔离级别，默认为DEFAULT |
| propagation | 事务传播机制，默认为REQUIRED |
| readOnly | 事务读写性，默认为false |
| noRollbackFor | 一组异常类，遇到时不回滚，默认为{} |
| noRollbackForClassName | 一组异常类名，遇到时不回滚，默认为{} |
| rollbackFor | 一组异常类，遇到时回滚，默认为{}<br />`[@Transactional](mailto:%C2%A0%C2%A0%C2%A0%C2%A0@Transactional)(rollbackFor={IOException.class,FileNoteFoundException})` |
| rollbackForClassName | 一组异常类名，遇到时回滚，默认为{} |
| timeout | 超时时间，以秒为单位 |
| value | 可选的限定描述符，指定使用的事务管理器，默认为“” |

<a name="CAblT"></a>
# 三、事务传播机制
<br />所谓事务的传播机制是指，如果在开始当前事务之前，一个事务上下文已经存在，此时有若干选项可以指定一个事务性方法的执行行为。<br />Propagation 的 Eum 类中定义了“七个”表示隔离级别的值，如下：<br />【1】死活不要事务的

- Propagation.NEVER：以非事务方式执行，且必须在一个没有的事务中执行，如果当前存在事务，抛出异常
- Propagation.NOT_SUPPORTED：以非事务方式执行，如果当前存在事务，就把当前事务挂起

【2】可有可无

- Propagation.SUPPORTS：持当前事务，如果当前有事务，就以事务方式执行；如果当前没有事务，就以非事务方式执行

【3】必须有事务

- Propagation.REQUIRED：如果当前没有事务，就新建一个事务，如果已经存在一个事务中，加入到这个事务中。这是 最常见的选择，也是Spring【默认】的传播机制
- Propagation.REQUIRES_NEW：不管是否存在事务，都创建一个新的事务，原来的挂起，新的执行完毕，继续执行老的事务
- Propagation.MANDATORY：使用当前的事务，且必须在一个已有的事务中执行，如果当前不存在事务，否则抛出异常
- Propagation.NESTED：如果当前存在事务，则在嵌套事务内执行；如果当前没有事务，则执行与【Propagation.REQUIRED 】类似的操作
<a name="fCimf"></a>
# 四. 事务失效的原因
<a name="DtLSZ"></a>
## 1. 数据库引擎不支持事务
以 MySQL 为例，其 MyISAM 引擎是不支持事务操作的，InnoDB 才是支持事务的引擎，一般要支持事务都会使用 InnoDB。 MySQL从5.5.5 开始的默认存储引擎是：InnoDB，之前默认的都是MyISAM。
<a name="lQKOk"></a>
## 2. 事务所在的类没有被Spring托管
<a name="VKWo2"></a>
## 3. 方法的标注修饰无效
Spring AOP对于**接口-实现类**这种方式是基于JDK动态代理的方式实现的，由于接口定义的方法是public的，java要求实现类所实现接口的方法必须是public的（不能是protected，private等），同时不能使用static的修饰符。所以，可以实施接口动态代理的方法只能是使用“public”或“public final”修饰符的方法，其它方法不可能被动态代理，相应的也就不能实施AOP增强，也即不能进行Spring事务增强。
<a name="koBF5"></a>
## 4. 方法自调用
如下面的代码，在update中调用updateOrder是无法使用事务的，事务不起作用其根本原因就是未通过代理调用，因为事务是在代理中处理的，没通过代理，也就不会有事务的处理。

