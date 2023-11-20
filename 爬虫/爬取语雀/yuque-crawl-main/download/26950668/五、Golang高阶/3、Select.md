<a name="63649ebb"></a>
#### select作用

Go里面提供了一个关键字select，通过select可以监听channel上的数据流动。

有时候我们希望能够借助channel发送或接收数据，并避免因为发送或者接收导致的阻塞，尤其是当channel没有准备好写或者读时。select语句就可以实现这样的功能。

select的用法与switch语言非常类似，由select开始一个新的选择块，每个选择条件由case语句来描述。

与switch语句相比，select有比较多的限制，其中最大的一条限制就是每个**case语句里必须是一个IO操作**，大致的结构如下：

```go
    select {
    case <- chan1:
        // 如果chan1成功读到数据，则进行该case处理语句
    case chan2 <- 1:
        // 如果成功向chan2写入数据，则进行该case处理语句
    default:
        // 如果上面都没有成功，则进入default处理流程
    }
```

在一个select语句中，Go语言会按顺序从头至尾评估每一个发送和接收的语句。

如果其中的任意一语句可以继续执行(即没有被阻塞)，那么就从那些可以执行的语句中任意选择一条来使用。

如果没有任意一条语句可以执行(即所有的通道都被阻塞)，那么有两种可能的情况：

l 如果给出了default语句，那么就会执行default语句，同时程序的执行会从select语句后的语句中恢复。

l 如果没有default语句，那么select语句将被阻塞，直到至少有一个通信可以进行下去。

示例代码：

```go
package main
 
import (
    "fmt"
)
 
func fibonacci(c, quit chan int) {
    x, y := 1, 1
    for {
        select {
        case c <- x:
            x, y = y, x+y
        case <-quit:
            fmt.Println("quit")
            return
        }
    }
}
 
func main() {
    c := make(chan int)
    quit := make(chan int)
 
    go func() {
        for i := 0; i < 6; i++ {
            fmt.Println(<-c)
        }
        quit <- 0
    }()
 
    fibonacci(c, quit)
}
```

运行结果如下：

![29-select1.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650606871451-8fcc3dd6-d3fc-40c1-b781-d996c7563e53.png#clientId=u8ede45a4-446d-4&from=drop&id=ueb38335c&originHeight=266&originWidth=206&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33118&status=done&style=none&taskId=uecf821e9-7095-4c99-94ac-11de292c92e&title=)
