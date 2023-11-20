<a name="d0083d7f"></a>
## 三、Golang语言特性

<a name="cb22423c"></a>
### 1、Golang的优势

![3-golang优势1.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650470888012-e20eedfd-9064-4d4e-b040-d6878aaa96ad.png#averageHue=%23fcfcfc&clientId=ufc63140c-62ef-4&from=drop&id=u011fd7b7&originHeight=824&originWidth=1414&originalType=binary&ratio=1&rotation=0&showTitle=false&size=130914&status=done&style=none&taskId=ufd2d1231-0d89-47b4-ae6a-77786c1757a&title=)


---

![7-golang优势2.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471318257-8884275c-9fe9-41de-8251-1bb828d50aa6.png#averageHue=%23fcfcfc&clientId=ufc63140c-62ef-4&from=drop&id=uefc1afca&originHeight=642&originWidth=2312&originalType=binary&ratio=1&rotation=0&showTitle=false&size=128087&status=done&style=none&taskId=uc6e7e31b-2a52-463e-9000-1cc12d63e49&title=)

![6-golang优势2.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471330308-12d4e2a3-7355-46f6-9af4-1ed10e39538e.png#averageHue=%23461836&clientId=ufc63140c-62ef-4&from=drop&id=ucc2a10f4&originHeight=512&originWidth=730&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3649557&status=done&style=none&taskId=u0a1cd683-18f0-4df3-94c9-d18a96713a4&title=)

---

![5-golan优势1.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471363769-9ded1e7a-acb0-4d6c-b4c1-61f9b77589b0.png#averageHue=%23fdfdfd&clientId=ufc63140c-62ef-4&from=drop&id=u30b116a5&originHeight=1158&originWidth=1752&originalType=binary&ratio=1&rotation=0&showTitle=false&size=141835&status=done&style=none&taskId=udfde902c-51a2-4061-b898-088df7f4570&title=)

```go
package main
  
import (
    "fmt"
    "time"
)

func goFunc(i int) {
    fmt.Println("goroutine ", i, " ...")
}

func main() {
    for i := 0; i < 10000; i++ {
        go goFunc(i) //开启一个并发协程
    }

    time.Sleep(time.Second)
}
```

![8-golang优势3.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471374246-adf62ac5-7eba-45c9-bcd7-ccc2f8141640.png#averageHue=%23461936&clientId=ufc63140c-62ef-4&from=drop&id=u06474c23&originHeight=520&originWidth=732&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2110181&status=done&style=none&taskId=u95896c9e-1a5f-4286-959b-659573870c1&title=)

---

![9-golang优势4.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471446832-5722e0a9-5522-469b-9ea9-296c373e3d66.png#averageHue=%23fcfcfc&clientId=ufc63140c-62ef-4&from=drop&id=u3921d4e9&originHeight=1024&originWidth=1836&originalType=binary&ratio=1&rotation=0&showTitle=false&size=174599&status=done&style=none&taskId=u9c1a75cb-7b7f-41b7-b0ec-09d4a75a23f&title=)

![10-golang优势5.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471454878-bf9c4abc-62c5-42f8-b595-b16d99d10743.png#averageHue=%23130b03&clientId=ufc63140c-62ef-4&from=drop&id=u7cd58575&originHeight=659&originWidth=967&originalType=binary&ratio=1&rotation=0&showTitle=false&size=126762&status=done&style=none&taskId=u9f5f8689-8f3a-43f6-8de6-d86f1ee70ed&title=)

---

![11-golang优势6.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471465058-b5db8451-e1d8-4ce4-a572-cc3d8be9bdc1.png#averageHue=%23fcfcfc&clientId=ufc63140c-62ef-4&from=drop&id=u1909868d&originHeight=1108&originWidth=2326&originalType=binary&ratio=1&rotation=0&showTitle=false&size=213709&status=done&style=none&taskId=u6ce64e07-a408-4ce3-a27d-cdbc629197c&title=)

---

![12-golang优势7.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471474504-6de5ec53-2447-4bdd-8a08-36ae40283ece.png#averageHue=%23fcf8f5&clientId=ufc63140c-62ef-4&from=drop&id=u3fa3cacd&originHeight=1184&originWidth=2684&originalType=binary&ratio=1&rotation=0&showTitle=false&size=893819&status=done&style=none&taskId=u8d1639ff-0bcf-457c-803a-3aaeefa48c6&title=)

<a name="8f2e1f77"></a>
### 2、Golang适合做什么

**(1)、云计算基础设施领域**

代表项目：docker、kubernetes、etcd、consul、cloudflare CDN、七牛云存储等。

**(2)、基础后端软件**

代表项目：tidb、influxdb、cockroachdb等。

**(3)、微服务**

代表项目：go-kit、micro、monzo bank的typhon、bilibili等。

**(4)、互联网基础设施**

代表项目：以太坊、hyperledger等。

---

<a name="92261373"></a>
### 3、Golang明星作品

![13-golang优势8.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471498432-166e36fd-6294-460c-bbcd-96f6e784f8a9.png#averageHue=%23fefefe&clientId=ufc63140c-62ef-4&from=drop&id=uefe79d8b&originHeight=570&originWidth=730&originalType=binary&ratio=1&rotation=0&showTitle=false&size=162652&status=done&style=none&taskId=ua789ba45-79b4-4727-9e2d-41ee3da9302&title=)

![14-golang优势9.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471506905-c3bf704e-d2fc-41e1-8e01-0a4907ae28fc.png#averageHue=%23fcfdf7&clientId=ufc63140c-62ef-4&from=drop&id=uf3ab4570&originHeight=552&originWidth=856&originalType=binary&ratio=1&rotation=0&showTitle=false&size=152174&status=done&style=none&taskId=ue7a5eb4f-8aca-4254-ac50-61a1b58496e&title=)

![15-golang优势10.png](https://cdn.nlark.com/yuque/0/2022/png/26269664/1650471515654-27569b7e-d67a-45f6-8d8f-54bd616da975.png#averageHue=%23edeaea&clientId=ufc63140c-62ef-4&from=drop&id=u2a429ae0&originHeight=302&originWidth=992&originalType=binary&ratio=1&rotation=0&showTitle=false&size=66414&status=done&style=none&taskId=ubf5e2818-a5c5-4b0e-9b2a-b69326bedf5&title=)

<a name="e1c0d206"></a>
### 4、Golang的不足

1、包管理，大部分包都在**github**上

~~2、无泛化类型~~<br />(Golang 1.18+已经支持泛型)

3、所有**Excepiton**都用**Error**来处理(比较有争议)。

4、对**C**的降级处理，并非无缝，没有**C**降级到**asm**那么完美(序列化问题)

