<a name="ZFOkr"></a>
## 一、案例分析
现在有一个秒杀活动，秒杀下单减库存的案例
```java
@RestController
public class StockController {
    @Autowired
    private StringRedisTemplate redisTemplate;
    /**
     * http://localhost:8088/deductStock
     */
    @GetMapping("/deductStock")
    public String deductStock() {
        int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
        if (stock > 0) {
            int realStock = stock - 1;
            redisTemplate.opsForValue().set("stock", realStock + "");
            System.out.println("扣减库存成功，剩余库存：" + realStock);
        }else {
            System.out.println("扣减库存失败");
        }
        return "stock";
    }
}
```
如果这个代码在高并发的情况下，必然会存在超卖的情况，也就是说会出现两个线程，同时在第10行代码的位置，获取到了相同的结果，导致两个购买者购买了商品，结果看到的库存只减少了1个。所以很明显的问题。当出现这样的问题的时候，我们非常自然的想到了加上锁。代码就演变为下面的样子
```java
    @GetMapping("/deductStock")
    public String deductStock() {
        synchronized (this){
            int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
            if (stock > 0) {
                int realStock = stock - 1;
                redisTemplate.opsForValue().set("stock", realStock + "");
                System.out.println("扣减库存成功，剩余库存：" + realStock);
            }else {
                System.out.println("扣减库存失败");
            }
            return "stock";
        }
    }
```
这样的场景在单机的场景下是不会存在问题，java的synchronized以及Reentrantlock类来保证一个代码块在同一时间只能由一个线程访问。 这种方式可以保证在同一个JVM进程内的多个线程同步执行。 <br />但是在分布式的场景下。由于是多台机器一起部署的情况，由于分布式系统多线程、多进程并且分布在不同机器上，这将使原单机部署情况下的并发控制锁策略失效，所以不同实例请求过来synchronized锁是锁不住的。因此我们引入了分布式锁，其中的一种实现方式为Redis

<a name="YJCR7"></a>
## 二、基于Redis分布式锁
<a name="xC9YQ"></a>
### 2.1、setnx基础
**setnx()**<br />setnx 的含义就是 SET if Not Exists，其主要有两个参数 setnx(key, value)。该方法是原子的，如果 key 不存在，则设置当前 key 成功，返回 1；如果当前 key 已经存在，则设置当前 key 失败，返回 0。<br />**expire()**<br />expire 设置过期时间，要注意的是 setnx 命令不能设置 key 的超时时间，只能通过 expire() 来对 key 设置。<br />**del(key)**<br />delete key：删除key
<a name="Eqf7F"></a>
### 2.2、setnx加锁
我们继续的改造上面的例子，使用Redis的setnx进行加锁，当获取到锁就正常的执行，如果获取不到锁，那么我们就返回，为了防止代码执行过程中出现异常，我们需要在finally中释放锁。代码改造如下：
```java
@GetMapping("/deductStock")
public String deductStock() {
    try {
        Boolean res = redisTemplate.opsForValue().setIfAbsent("lockKey", "val");
        if (!res) {
            return "需要等待，繁忙中.....";
        }
        int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
        if (stock > 0) {
            int realStock = stock - 1;
            redisTemplate.opsForValue().set("stock", realStock + "");
            System.out.println("扣减库存成功，剩余库存：" + realStock);
        } else {
            System.out.println("扣减库存失败");
        }
    } finally {
        redisTemplate.delete("lockKey");
    }
    return "stock";
}
```
看起来好像加锁可以成功，但是会有什么问题呢？<br />1：假设代码在执行的过程中，服务实例宕机了，那么我们的Redis锁那不就永远的锁在那里了吗？其他的任务请求都获取不到Redis锁，这样就造成了死锁。我们很自然的想到给这个锁加一个超时时间。
<a name="SxYgv"></a>
### 2.3、setnx加锁+expire 过期时间
```java
public String deductStock() {
        String lockKey = "lockKey";
        try {
            Boolean res = redisTemplate.opsForValue().setIfAbsent(lockKey, "val");
            redisTemplate.expire(lockKey, 30, TimeUnit.SECONDS);
            if (!res) {
                return "需要等待，繁忙中.....";
            }
            int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
            if (stock > 0) {
                int realStock = stock - 1;
                redisTemplate.opsForValue().set("stock", realStock + "");
                System.out.println("扣减库存成功，剩余库存：" + realStock);
            } else {
                System.out.println("扣减库存失败");
            }
        } finally {
            redisTemplate.delete(lockKey);
        }
        return "stock";
    }
```
加上过期时间后我们再看一下会存在什么问题

1. 假设上面的代码在执行完加锁之后，再执行`redisTemplate.expire(lockKey, 30, TimeUnit.SECONDS);`代码的时候，机器宕机了，其实还是会发生死锁，说百了就是这两个操作不是原子性，我们需要把这两个操作保持原子性。应该使用`Boolean res = redisTemplate.opsForValue_()_.setIfAbsent_(_lockKey, "val",30,TimeUnit._SECONDS)_;`
2. 继续思考，加上了过期时间就没有问题了吗？假设在过期时间30S，第一个请求还没有执行完代码，此时锁已经释放了，那么其他的请求就会进来执行这段秒杀减库存的代码，此时还是会发生超卖的可能。
3. 继续接着2的进行思考，当再过了5s，第一个请求执行完了，第二个请求还在执行中，此时第一个请求需要删除Redis锁，那么此时删除的Redis锁是第二个请求的Redis锁。那么此时再高并发的场景下Redis锁就会永久的失效。
<a name="U5qIX"></a>
### 2.4、Redission
争夺2.3场景的问题，即过期时间需要设置的问题，在以往早期成熟的方案之前选择的是加一个分线程，定时的去监控Redis的锁所在的线程是否依然存活，会进行自动的续命，俗称watch dog。后面有人封装Java 版的 分布式锁的框架就是 Redisson。Redisson解决了上述的锁自动续命的问题<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652421884625-ea2e4273-1f29-4485-a77d-dc66f3065c7d.jpeg#clientId=u7311127c-4d07-4&from=paste&id=u08000e62&originHeight=318&originWidth=732&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u94fd787a-7e0e-425d-9f0e-9eb075a5214&title=)
<a name="ejMx5"></a>
##### 1、加锁机制
线程去获取锁，获取成功: 执行lua脚本，保存数据到redis数据库。<br />线程去获取锁，获取失败: 一直通过while循环尝试获取锁，获取成功后，执行lua脚本，保存数据到redis数据库。
<a name="YHE3B"></a>
##### 2、watch dog自动延期机制
自动对超时时间进行延期
<a name="qCJkg"></a>
##### 3、可重入加锁机制
Redisson可以实现可重入加锁机制的原因，我觉得跟两点有关：

1.  Redis存储锁的数据类型是 Hash类型     
2. Hash数据类型的key值包含了当前线程信息。

下面是redis存储的数据<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652422180598-ed95d7d3-a129-4b62-9597-f2f03332ffdc.jpeg#clientId=u7311127c-4d07-4&from=paste&id=u33ed554a&originHeight=140&originWidth=732&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u204ee6ad-2599-4cf9-af7c-2751ed0216e&title=)<br />这里表面数据类型是Hash类型,Hash类型相当于我们java的 <key,<key1,value>> 类型,这里key是指 'redisson'<br />它的有效期还有9秒，我们再来看里们的key1值为 078e44a3-5f95-4e24-b6aa-80684655a15a:45 它的组成是: guid + 当前线程的ID。后面的value是就和可重入加锁有关。<br />**举图说明**<br />![](https://cdn.nlark.com/yuque/0/2022/jpeg/297975/1652422276475-89b49593-fbb6-46a8-b20a-03ce8f850203.jpeg#clientId=u7311127c-4d07-4&from=paste&id=u7436060e&originHeight=352&originWidth=732&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u24747721-ace8-494b-96cb-0816d3efd03&title=)<br />上面这图的意思就是可重入锁的机制，它最大的优点就是相同线程不需要在等待锁，而是可以直接进行相应操作。
<a name="GoB6v"></a>
##### 4、代码修改
```java
@GetMapping("/deductStock2")
    public String deductStock2() throws InterruptedException {
        String lockKey = "lockKey";
        RLock redissonLock = redissonClient.getLock(lockKey);
        try {
            // 加锁
            redissonLock.lock( );
            int stock = Integer.parseInt(redisTemplate.opsForValue().get("stock"));
            Thread.sleep(10000);
            if (stock > 0) {
                int realStock = stock - 1;
                redisTemplate.opsForValue().set("stock", realStock + "");
                System.out.println("扣减库存成功，剩余库存：" + realStock);
            } else {
                System.out.println("扣减库存失败");
            }
        } finally {
            redissonLock.unlock();
        }
        return "stock";
    }
```
Redis存储的结构如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652422962809-ee398190-bce8-4cdb-bfdb-ca3cb44508e7.png#clientId=ue2d8e37a-b9a4-4&from=paste&height=223&id=uf8bec982&originHeight=245&originWidth=891&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15097&status=done&style=none&taskId=ucb2520f2-43b2-43d7-b82d-cb7bd64fb40&title=&width=809.9999824437232)
