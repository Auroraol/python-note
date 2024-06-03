基于 Redis 的 Redisson 的分布式信号量（[Semaphore](https://xie.infoq.cn/link?target=http%3A%2F%2Fstatic.javadoc.io%2Forg.redisson%2Fredisson%2F3.10.0%2Forg%2Fredisson%2Fapi%2FRSemaphore.html)）Java 对象RSemaphore采用了与java.util.concurrent.Semaphore相似的接口和用法。同时还提供了[异步（Async）](https://xie.infoq.cn/link?target=http%3A%2F%2Fstatic.javadoc.io%2Forg.redisson%2Fredisson%2F3.10.0%2Forg%2Fredisson%2Fapi%2FRSemaphoreAsync.html)、[反射式（Reactive）](https://xie.infoq.cn/link?target=http%3A%2F%2Fstatic.javadoc.io%2Forg.redisson%2Fredisson%2F3.10.0%2Forg%2Fredisson%2Fapi%2FRSemaphoreReactive.html)和[RxJava2标准](https://xie.infoq.cn/link?target=http%3A%2F%2Fstatic.javadoc.io%2Forg.redisson%2Fredisson%2F3.10.0%2Forg%2Fredisson%2Fapi%2FRSemaphoreRx.html)的接口。<br />关于信号量的使用大家可以想象一下这个场景，有三个停车位，当三个停车位满了后，其他车就不停了。可以把车位比作信号，现在有三个信号，停一次车，用掉一个信号，车离开就是释放一个信号。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/297975/1652667788423-11922210-8dc5-473c-902d-ecf9ba53d93c.png#clientId=u7dc040f2-08c6-4&from=paste&height=295&id=uc78cf009&originHeight=590&originWidth=582&originalType=url&ratio=1&rotation=0&showTitle=false&size=38800&status=done&style=none&taskId=u6cd69553-5311-4693-8984-6841d79b806&title=&width=291)

我们用 Redisson 来演示上述停车位的场景。
```java
/**
* 停车，占用停车位
* 总共 3 个车位
*/
@ResponseBody
@RequestMapping("park")
public String park() throws InterruptedException {
  // 获取信号量（停车场）
  RSemaphore park = redisson.getSemaphore("park");
  // 获取一个信号（停车位）
  park.acquire();

  return "OK";
}

```
先定义一个占用停车位的方法：
```java
/**
 * 释放车位
 * 总共 3 个车位
 */
@ResponseBody
@RequestMapping("leave")
public String leave() throws InterruptedException {
    // 获取信号量（停车场）
    RSemaphore park = redisson.getSemaphore("park");
    // 释放一个信号（停车位）
    park.release();

    return "OK";
}
```
为了简便，我用 Redis 客户端添加了一个 key：“park”，值等于 3，代表信号量为 park，总共有三个值。<br />然后用 postman 发送 park 请求占用一个停车位。

![](https://cdn.nlark.com/yuque/0/2022/png/297975/1652667871342-8dc46682-3d7e-4b3d-9a92-4c639e6cbe02.png#clientId=u7dc040f2-08c6-4&from=paste&id=u6ffec154&originHeight=680&originWidth=1782&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ub89155b4-8b8b-4c49-bc9a-a84441301ae&title=)

然后在 redis 客户端查看 park 的值，发现已经改为 2 了。继续调用两次，发现 park 的等于 0，当调用第四次的时候，会发现请求一直处于等待中，说明车位不够了。如果想要不阻塞，可以用 tryAcquire 或 tryAcquireAsync。

我们再调用离开车位的方法，park 的值变为了 1，代表车位剩余 1 个。

> [信号量](https://so.csdn.net/so/search?q=%E4%BF%A1%E5%8F%B7%E9%87%8F&spm=1001.2101.3001.7020)也可以做分布式限流

```java
@GetMapping("/park")
@ResponseBody
public String  park() throws InterruptedException {
    //在redis中存 pass = 10000，超过10000并发阻塞
    RSemaphore pack = redisson.getSemaphore("pass");
    boolean flag = pass.tryAcquire();//尝试获取一个信号量，不阻塞
    if(flag){
        //业务逻辑
    }else{
        return "error";
    }
}

```
