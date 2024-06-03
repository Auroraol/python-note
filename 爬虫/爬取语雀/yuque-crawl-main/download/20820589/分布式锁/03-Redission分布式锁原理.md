<a name="xuozg"></a>
## 1、lock
```java
/**
* leaseTime:表示持锁时间，默认-1表示不指定redis的锁的超时时间
* timeUnit:时间单位
* interruptibly：是否响应中断
*/
private void lock(long leaseTime, TimeUnit unit, boolean interruptibly) throws InterruptedException {
        // 获取到线程id
        long threadId = Thread.currentThread().getId();
        // 尝试获取锁，这个下面详解 ******
        Long ttl = tryAcquire(-1, leaseTime, unit, threadId);
        // lock acquired
        if (ttl == null) {
            return;
        }

        RFuture<RedissonLockEntry> future = subscribe(threadId);
        if (interruptibly) {
            commandExecutor.syncSubscriptionInterrupted(future);
        } else {
            commandExecutor.syncSubscription(future);
        }
```
<a name="QkeBi"></a>
## 2、`tryAcquire()`获取锁
1：leaseTime不为-1，也就是我们自己设置的锁的超时时间<br />2：leaseTime为-1，使用默认的超时时间为30S<br />3： leaseTime 是 -1，所以触发的是 else 分支中的 scheduleExpirationRenewal 代码。<br />4：leaseTime 不是 -1，触发不了看门狗的能力
```java
private <T> RFuture<Long> tryAcquireAsync(long waitTime, long leaseTime, TimeUnit unit, long threadId) {
        RFuture<Long> ttlRemainingFuture;
        if (leaseTime != -1) {
            // 2.1 我们先分析其指定了获取锁超时时间的代码（leaseTime!=-1）。
            ttlRemainingFuture = tryLockInnerAsync(waitTime, leaseTime, unit, threadId, RedisCommands.EVAL_LONG);
        } else {
            // 2.1 没有指定超时时间获取锁
            ttlRemainingFuture = tryLockInnerAsync(waitTime, internalLockLeaseTime,
                    TimeUnit.MILLISECONDS, threadId, RedisCommands.EVAL_LONG);
        }
        
        // 2.2 锁续命
        ttlRemainingFuture.onComplete((ttlRemaining, e) -> {
            if (e != null) {
                return;
            }

            // lock acquired
            if (ttlRemaining == null) {
                // 当leaseTime不为-1，也就是自己设置过期时间，是不会触发看门狗的
                if (leaseTime != -1) {
                    internalLockLeaseTime = unit.toMillis(leaseTime);
                } else {
                    scheduleExpirationRenewal(threadId);
                }
            }
        });
        return ttlRemainingFuture;
    }
```
<a name="Cw7s8"></a>
### 2.1、tryLockInnerAsync
```java
<T> RFuture<T> tryLockInnerAsync(long waitTime, long leaseTime, TimeUnit unit, long threadId, RedisStrictCommand<T> command) {
        return evalWriteAsync(getRawName(), LongCodec.INSTANCE, command,
                "if (redis.call('exists', KEYS[1]) == 0) then " +
                        "redis.call('hincrby', KEYS[1], ARGV[2], 1); " +
                        "redis.call('pexpire', KEYS[1], ARGV[1]); " +
                        "return nil; " +
                        "end; " +
                        "if (redis.call('hexists', KEYS[1], ARGV[2]) == 1) then " +
                        "redis.call('hincrby', KEYS[1], ARGV[2], 1); " +
                        "redis.call('pexpire', KEYS[1], ARGV[1]); " +
                        "return nil; " +
                        "end; " +
                        "return redis.call('pttl', KEYS[1]);",
                Collections.singletonList(getRawName()), unit.toMillis(leaseTime), getLockName(threadId));
    }
```
里面执行的是Lua脚本，先对Lua脚本做基本说明：
> - key：表示在脚本中用到的Redis 键(key)，这些键名参数可以在Lua中通过全局变量KEYS数组访问，下标从1开始，如： KEYS[1]、KEYS[2]
> - arg：参数，在Lua中通过全局变量ARGV数组访问，下标从1开始，如：ARGV[1]、ARGV[2]

1. keys[1]:`getRawName()`，什么是rawName？其实就是我上面写代码的 `lockKey` 这个字符串
2. ARGV[1]:就是`leaseTime`，锁的持锁超时时间
3. AGRV[2]:这个就有点东西了，锁名称，`getLockName(threadId)`，这个名称是`UUID+":"+threadId`

**第一段 Lua脚本：**

- 其先判断是否存在`lockKey` 在redis中，如果不存在？
- 就创建一个`lockKey` 为key的redis的map数据，且为filed为`UUID+":"+threadId`，赋予值+1操作
- 并且创建成功后，设置其超时时间为`leaseTime`
- 返回一个null

**第二段Lua脚本：**

1. 假如上一步不成功，其判断anyLock1中存的`filed：UUID+":"+threadId`是否为自身的值。
2. 如果是，我就进行对`lockKey` 的`filed`的值进行+1操作
3. 并且重新设置持锁的超时时间
4. 并返回null，表示持锁成功
<a name="Iv4Yz"></a>
### 2.2、scheduleExpirationRenewal 锁续命
分析到获取锁成功，我们进`入scheduleExpirationRenewal`锁续命方法看看里面的实现：
```java
protected void scheduleExpirationRenewal(long threadId) {
        ExpirationEntry entry = new ExpirationEntry();
        ExpirationEntry oldEntry = EXPIRATION_RENEWAL_MAP.putIfAbsent(getEntryName(), entry);
        // 重入加锁
        if (oldEntry != null) {
            oldEntry.addThreadId(threadId);
        } else {
            // 第一次加锁触发定时任务
            entry.addThreadId(threadId);
            renewExpiration();
        }
    }
```
看到这里会发现，这个里面多了一个`ConcurrentMap<String, ExpirationEntry> EXPIRATION_RENEWAL_MAP`的集合变量。其中这个`map`的key是当前线程，value是`ExpirationEntry`对象，这个对象维护的是当前线程的加锁次数。其中`ExpirationEntry`类的模型如下：
```java
public static class ExpirationEntry {
        // 1、threadIds用于记录其线程的重入锁次数。（redisson的锁是可重入的）
        private final Map<Long, Integer> threadIds = new LinkedHashMap<>();
        // 2、Timeout其超时任务（即在指定时间内，重新执行操作），其采用netty的TimerTask进行创建的
        private volatile Timeout timeout;
```
<a name="bFA7W"></a>
### 2.2.1、第一次加锁触发看门狗定时任务
我们先看`scheduleExpirationRenewal`方法里面，调用 `map` 的 `putIfAbsent` 方法后，返回的 `oldEntry `为空的情况。这种情况说明是第一次加锁，会触发 `renewExpiration` 方法，这个方法里面就是看门狗的核心逻辑。<br />而在 `scheduleExpirationRenewal `方法里面，不管前面提到的 `oldEntry` 是否为空，都会触发 `addThreadId` 方法：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652669496834-2bedccc6-5fe5-462d-b30e-8ea9c0d2b83e.webp#clientId=u76f6b25b-b9b4-4&from=paste&id=u67482494&originHeight=312&originWidth=690&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=udb497251-bcb0-45c7-b8f2-1c47aefb363&title=)<br />从源码中可以看出来，这里仅仅对当前线程的加锁次数进行一个维护。这个维护很好理解，因为要支持锁的重入嘛，就得记录到底重入了几次。加锁一次，次数加一。解锁一次，次数减一。接着看 `renewExpiration` 方法，这就是看门狗的真面目了：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652669661899-0c7d0b6e-0dc8-4890-acfb-cdfc675613d1.webp#clientId=u76f6b25b-b9b4-4&from=paste&id=u819bfd9a&originHeight=666&originWidth=648&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u093ff84d-5462-4650-811e-9bff77a052b&title=)<br /> ④ ：这个定时任务触发的时间条件：internalLockLeaseTime / 3。创建一个Timeout指定其超时任务（Timeout对象，其采用netty的TimerTask进行创建的） 

 ①、② ：干的是同一件事，就是检查当前线程是否还有效。就是看前面提到的 MAP 中是否还有当前线程对应的 `ExpirationEntry` 对象。没有，就说明是被 remove 了。那么问题就来了，你看源码的时候非常自然而然的就应该想到这个问题：什么时候调用这个 MAP 的 remove 方法呢？

  ③ ：能走到 ③ 这里说明当前线程的业务逻辑还未执行完成，还需要继续持有锁。首先看 `renewExpirationAsync` 方法，从方法命名上我们也可以看出来，这是在重置过期时间：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652669826694-bb969d0d-7efa-4d21-b5d3-e5ef81f98756.webp#clientId=u76f6b25b-b9b4-4&from=paste&id=u4f145ea0&originHeight=193&originWidth=635&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u2a7fab14-3966-43e4-a062-1fb7b2869a9&title=)<br />上面的源码主要是一个 lua 脚本，而这个脚本的逻辑非常简单。就是判断锁是否还存在，且持有锁的线程是否是当前线程。如果是当前线程，重置锁的过期时间，并返回 1，即返回 true。<br />1、判断其`lockKey`,中UUID:threadId的fieldId是否存在，如果存在对其进行重新设置超时时间<br />2、如果是当前线程，重置锁的过期时间，并返回 1，即返回 true；如果不存在直接返回false

接着继续执行，里面首先判断了执行 `renewExpirationAsync `方法是否有异常。那么问题就来了，会有什么异常呢？

- 如果出现异常了，则执行下面这行码：`EXPIRATION_RENEWAL_MAP.remove(getEntryName());`这个就是romve操作
- 如果执行 renewExpirationAsync 方法的时候没有异常。这个时候的返回值就是 true 或者 false。如果是 true，说明续命成功，则再次调用 renewExporation 方法，等待着时间轮触发下一次。如果是 false，说明这把锁已经没有了，或者易主了。那么也就没有当前线程什么事情了，啥都不用做，默默的结束就行了。

<a name="BF9NR"></a>
## 三、unlock 
![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652670558036-eac9220c-9637-4c89-bb23-b59a88cfb9a9.webp#clientId=u67a7354d-9c05-4&from=paste&id=u20d6a252&originHeight=214&originWidth=499&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u1d3f9cc1-cf3b-4758-aa1e-5b5e491e93b&title=)<br />首先是 unlockInnerAsync 方法，这里面就是 lua 脚本释放锁的逻辑：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652670569750-021156bb-16be-40dd-874d-1ebab04d3de4.webp#clientId=u67a7354d-9c05-4&from=paste&id=ue2232e2b&originHeight=387&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=uc1305df6-3cb8-4ba4-9f75-8054aa8da0b&title=)<br />这个方法返回的是 Boolean，有三种情况。

- 返回为 null，说明锁不存在，或者锁存在，但是 value 不匹配，表示锁已经被其他线程占用。
- 返回为 true，说明锁存在，线程也是对的，重入次数已经减为零，锁可以被释放。
- 返回为 false，说明锁存在，线程也是对的，但是重入次数还不为零，锁还不能被释放。

但是你看 unlockInnerAsync 是怎么处理这个返回值的：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652670744985-a35f29bf-6bfb-41b5-aac3-10b2b34d2853.webp#clientId=u67a7354d-9c05-4&from=paste&id=ub48b5153&originHeight=582&originWidth=728&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u8c4c76d6-59f6-45fd-8e1f-2ef085d170b&title=)<br />返回值，也就是 opStatus，仅仅是判断了返回为 null 的情况，抛出异常表明这个锁不是被当前线程持有的，完事。它并不关心返回为 true 或者为 false 的情况。然后再看我框起来的` cancelExpirationRenewal(threadId); `方法：<br />![](https://cdn.nlark.com/yuque/0/2022/webp/297975/1652670778269-8cc86e4a-6015-436f-ae73-10697e2932e4.webp#clientId=u67a7354d-9c05-4&from=paste&id=ub59c3450&originHeight=408&originWidth=587&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue64df4da-bc83-46bb-9a09-8d19c7b5d67&title=)<br />这里面就有` remove` 方法。而前面铺垫了这么多其实就是为了引出这个` cancelExpirationRenewal `方法。

[https://juejin.cn/post/7094102614203170824#heading-3](https://juejin.cn/post/7094102614203170824#heading-3)<br />[https://juejin.cn/user/4054654615298685/posts](https://juejin.cn/user/4054654615298685/posts)
