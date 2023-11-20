sort 包内置的提供了根据一些排序函数来对任何序列排序的功能。它的设计非常独到。在很多语言中，排序算法都是和序列数据类型关联，同时排序函数和具体类型元素关联。

相比之下，Go语言的 sort.Sort 函数不会对具体的序列和它的元素做任何假设。相反，它使用了一个接口类型 sort.Interface 来指定通用的排序算法和可能被排序到的序列类型之间的约定。这个接口的实现由序列的具体表示和它希望排序的元素决定，序列的表示经常是一个切片。

一个内置的排序算法需要知道三个东西：序列的长度，表示两个元素比较的结果，一种交换两个元素的方式；这就是 sort.Interface 的三个方法：
```go
package sort
type Interface interface {
    Len() int            // 获取元素数量
    Less(i, j int) bool // i，j是序列元素的指数。
    Swap(i, j int)        // 交换元素
}
```

<a name="MyTkS"></a>
## 一、自定义实现排序接口
比如我们自定义一个字符串数组类型，要对字符串数组中的每一条字符串进行排序：
```go
// 将[]string定义为MyStringList类型
type StringList []string

// 实现sort.Interface接口的获取元素数量方法
func (m StringList) Len() int {
	return len(m)
}

// 实现sort.Interface接口的比较元素方法
func (m StringList) Less(i, j int) bool {
	return m[i] < m[j]
}

// 实现sort.Interface接口的交换元素方法
func (m StringList) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func StringSort() {
	// 准备一个内容被打乱顺序的字符串切片
	names := StringList{
		"3. Triple Kill",
		"5. Penta Kill",
		"2. Double Kill",
		"4. Quadra Kill",
		"1. First Blood",
	}
	// 使用sort包进行排序
	sort.Sort(names)
	// 遍历打印结果
	for _, v := range names {
		fmt.Printf("%s\n", v)
	}
}
```

<a name="NKlWS"></a>
## 二、使用内置接口实现排序
sort 包中的 `StringSlice` 的代码与上面自定义的 StringList 的实现代码几乎一样。因此，只需要使用 sort 包的 StringSlice 就可以更简单快速地进行字符串排序。
```go
	names := sort.StringSlice{
		"3. Triple Kill",
		"5. Penta Kill",
		"2. Double Kill",
		"4. Quadra Kill",
		"1. First Blood",
	}
	sort.Sort(names)
	fmt.Println(names)
```

sort 包在 sort.Interface 对各类型的封装上还有更进一步的简化，下面使用 sort.Strings 继续对上述代码进行简化：
```go
	names := []string{
		"3. Triple Kill",
		"5. Penta Kill",
		"2. Double Kill",
		"4. Quadra Kill",
		"1. First Blood",
	}
	sort.Strings(names)
	fmt.Println(names)
```

<a name="rGSOk"></a>
## 三、sort 包中内建的类型排序接口
Go语言中的 sort 包中定义了一些常见类型的排序方法，如下表所示。

| 类  型 | 实现 sort.lnterface 的类型 | 直接排序方法 | 说  明 |
| --- | --- | --- | --- |
| 字符串（String） | StringSlice | sort.Strings(a [] string) | 字符 ASCII 值升序 |
| 整型（int） | IntSlice | sort.Ints(a []int) | 数值升序 |
| 双精度浮点（float64） | Float64Slice | sort.Float64s(a []float64) | 数值升序 |


<a name="IcDuu"></a>
## 四、对结构体进行排序
除了基本类型的排序，也可以对结构体进行排序。结构体比基本类型更为复杂，排序时不能像数值和字符串一样拥有一些固定的单一原则。结构体的多个字段在排序中可能会存在多种排序的规则，例如，结构体中的名字按字母升序排列，数值按从小到大的顺序排序。一般在多种规则同时存在时，需要确定规则的优先度，如先按名字排序，再按年龄排序等。

示例：
```go
type HeroKind int
const (
	None HeroKind = iota
	Tank
	Assassin
	Mage
)

type Hero struct {
	Name string
	Kind HeroKind
}

type Heros []*Hero

// 实现sort.Interface接口取元素数量方法
func (s Heros) Len() int {
	return len(s)
}

// 实现sort.Interface接口比较元素方法
func (s Heros) Less(i, j int) bool {
	// 如果英雄的分类不一致时, 优先对分类进行排序
	if s[i].Kind != s[j].Kind {
		return s[i].Kind < s[j].Kind
	}
	// 默认按英雄名字字符升序排列
	return s[i].Name < s[j].Name
}

// 实现sort.Interface接口交换元素方法
func (s Heros) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func SortStruct1() {
	// 准备英雄列表
	heros := Heros{
		&Hero{"吕布", Tank},
		&Hero{"李白", Assassin},
		&Hero{"妲己", Mage},
		&Hero{"貂蝉", Assassin},
		&Hero{"关羽", Tank},
		&Hero{"诸葛亮", Mage},
	}
	// 使用sort包进行排序
	sort.Sort(heros)
	// 遍历英雄列表打印排序结果
	for _, v := range heros {
		fmt.Printf("%+v\n", v)
	}
}
```

<a name="0yiln"></a>
## 五、sort.Slice
从 Go 1.8 开始，Go语言在 sort 包中提供了 sort.Slice() 函数进行更为简便的排序方法。sort.Slice() 函数只要求传入需要排序的数据，以及一个排序时对元素的回调函数，类似于JavaScript中的 `Array.prototype.sort`。<br />函数的定义如下：
```go
func Slice(slice interface{}, less func(i, j int) bool)
```
示例：
```go
type HeroKind int
const (
	None HeroKind = iota
	Tank
	Assassin
	Mage
)

type Hero struct {
	Name string
	Kind HeroKind
}

func SortStruct2() {
	heros := []*Hero{
		{"吕布", Tank},
		{"李白", Assassin},
		{"妲己", Mage},
		{"貂蝉", Assassin},
		{"关羽", Tank},
		{"诸葛亮", Mage},
	}
	sort.Slice(heros, func(i, j int) bool {
		if heros[i].Kind != heros[j].Kind {
			return heros[i].Kind < heros[j].Kind
		}
		return heros[i].Name < heros[j].Name
	})
	for _, v := range heros {
		fmt.Printf("%+v\n", v)
	}
}
```

<a name="qVLol"></a>
## 参考资料

- [Go语言排序（借助sort.Interface接口）](http://c.biancheng.net/view/81.html)

