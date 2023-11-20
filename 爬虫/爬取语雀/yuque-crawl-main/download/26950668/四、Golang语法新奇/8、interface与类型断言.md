
Golang的语言中提供了断言的功能。golang中的所有程序都实现了interface{}的接口，这意味着，所有的类型如string,int,int64甚至是自定义的struct类型都就此拥有了interface{}的接口，这种做法和java中的Object类型比较类似。那么在一个数据通过func funcName(interface{})的方式传进来的时候，也就意味着这个参数被自动的转为interface{}的类型。

```go
func funcName(a interface{}) string {
     return string(a)
}
```

编译器会返回

```go
cannot convert a (type interface{}) to type string: need type assertion
```

此时，意味着整个转化的过程需要类型断言。类型断言有以下几种形式：

1）直接断言使用

```go
var a interface{}


fmt.Println("Where are you,Jonny?", a.(string))
```

但是如果断言失败一般会导致panic的发生。所以为了防止panic的发生，我们需要在断言前进行一定的判断

```go
value, ok := a.(string)
```

如果断言失败，那么ok的值将会是false,但是如果断言成功ok的值将会是true,同时value将会得到所期待的正确的值。示例：

```go
value, ok := a.(string)
if !ok {
    fmt.Println("It's not ok for type string")
    return
}
fmt.Println("The value is ", value)
```

完整例子如下：

```go
package main


import "fmt"


/*
func funcName(a interface{}) string {
        return string(a)
}
*/


func funcName(a interface{}) string {
        value, ok := a.(string)
        if !ok {
                fmt.Println("It is not ok for type string")
                return ""
        }
        fmt.Println("The value is ", value)


        return value
}


func main() {
        //      str := "123"
        //      funcName(str)
        //var a interface{}
        //var a string = "123"
        var a int = 10
        funcName(a)
}
```

2）配合switch使用

```go
var t interface{}
t = functionOfSomeType()
switch t := t.(type) {
default:
    fmt.Printf("unexpected type %T", t)       // %T prints whatever type t has
case bool:
    fmt.Printf("boolean %t\n", t)             // t has type bool
case int:
    fmt.Printf("integer %d\n", t)             // t has type int
case *bool:
    fmt.Printf("pointer to boolean %t\n", *t) // t has type *bool
case *int:
    fmt.Printf("pointer to integer %d\n", *t) // t has type *int
}
```

或者如下使用方法

```go
func sqlQuote(x interface{}) string {
    if x == nil {
        return "NULL"
    } else if _, ok := x.(int); ok {
        return fmt.Sprintf("%d", x)
    } else if _, ok := x.(uint); ok {
        return fmt.Sprintf("%d", x)
    } else if b, ok := x.(bool); ok {
        if b {
            return "TRUE"
        }
        return "FALSE"
    } else if s, ok := x.(string); ok {
        return sqlQuoteString(s) // (not shown)
    } else {
        panic(fmt.Sprintf("unexpected type %T: %v", x, x))
    }
}
```
