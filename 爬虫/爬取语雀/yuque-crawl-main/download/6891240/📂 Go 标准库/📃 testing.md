`testing` 包用于go的单元测试。<br />引入：
```go
import "testing"
```
<a name="NS6hL"></a>
## 一、测试规则
要创建测试文件，需要将文件名设置为 `xxx_test.go` ，结尾必须是 `_test.go` 。

测试文件中的，结构必须为如下形式：
```go
func TestXXX(t *testing.T) {
    ...
}

func BenchmarkXXX(t *testing.B) {
    ...
}
```

1. 单元测试方法必须以 `Test` 开头，压力测试方法必须以 `Benchmark` 开头
2. 单元测试参数必须是 `(t *testing.T)` ，性能测试参数必须是 `(t *testing.B)`

执行测试：
```go
go test 测试文件名
```

<a name="0YDLP"></a>
## 二、单元（功能）测试
比如有如下一个程序：<br />`demo.go` 
```go
package test

func GetArea(weight int, height int) int {
	return weight * height
}
```
`demo_test.go`
```go
package test

import "testing"

func TestGetArea(t *testing.T) {
	area := GetArea(40, 50)
	if area != 2000 {
		t.Error("测试失败")
	}
}
```
执行完单元测试输出：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608795613846-fd1ed756-a5da-4d70-ac2f-8c25e44abba7.png#align=left&display=inline&height=139&originHeight=278&originWidth=735&size=27990&status=done&style=none&width=367.5)

<a name="5OAPY"></a>
## 三、性能（压力）测试
还是上面那个例子：
```go
func BenchmarkGetArea(t *testing.B) {
	for i := 0; i < t.N; i++ {
		GetArea(40, 50)
	}
}
```

在PyCharm左侧，可以看到运行按钮，直接点击即可开始测试。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608795645813-2c0d34ec-cc09-4a31-bae5-da1f50d1fd5a.png#align=left&display=inline&height=284&originHeight=568&originWidth=521&size=63035&status=done&style=none&width=260.5)

执行完压力测试输出：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608795572945-ab546827-04ab-4176-9f49-89d62b6ba68e.png#align=left&display=inline&height=183&originHeight=366&originWidth=1044&size=44709&status=done&style=none&width=522)

