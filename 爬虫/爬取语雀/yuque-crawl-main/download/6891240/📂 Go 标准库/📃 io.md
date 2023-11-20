相关的包：
```go
import (
	"archive/zip"
    "archive/tar"
	"bytes"
	"bufio"
    "encoding/gob"
	"encoding/binary"
	"encoding/json"
	"encoding/xml"
	"io/ioutil"
	"fmt"
	"io"
	"os"
	"strings"
)
```
<a name="vf7bj"></a>
## 一、从字符串读取数据
先封装自定义一个读取器，后面有很多地方会用到：
```go
func ReadFrom(reader io.Reader, num int) ([]byte, error) {
	p := make([]byte, num)
	n, err := reader.Read(p)
	if n > 0 {
		return p[:n], nil
	}
	return p, err
}
```
从字符串读取数据：
```go
	strReader := strings.NewReader("Hello world")
	data, _ := ReadFrom(strReader, 12)
	fmt.Println(data)
	fmt.Println(string(data))
```

<a name="fctZ2"></a>
## 二、从命令行读取数据
<a name="Bf2g5"></a>
### 从命令行输入数据
通过 `os.Stdin` 获取标准输入，下面程序可以在命令行中获取用户输入：
```go
	fmt.Print("Please input some words: ")
	data, _ := ReadFrom(os.Stdin, 12)
	fmt.Println(data)
	fmt.Println("你输入的数据为：", string(data))
```

<a name="mHdb9"></a>
### 从命令行参数读取数据
通过 `os.Args` 获取命令行参数。
```go
func main() {
	if len(os.Args) < 3 {
		fmt.Println("命令行参数不能小于2个")
		return
	}
	fmt.Println("参数0：", os.Args[0])
	fmt.Println("参数1：", os.Args[1])
	fmt.Println("参数2：", os.Args[2])
}
```
运行是携带参数
```go
$ go run main.go hello world
参数0： C:\Users\QUANZA~1\AppData\Local\Temp\go-build085958702\b001\exe\main.exe
参数1： hello
参数2： world
```
看到，第一个命令行参数就是这个程序生成的可自行文件，每个参数使用空格区分开来。

<a name="zxLw3"></a>
## 三、缓冲IO
<a name="a9rag"></a>
### 读数据
读取一个字符串，放入缓存中，然后逐步取出缓存的数据：
```go
func main() {
	strReader := strings.NewReader("Hello world")
	bufReader := bufio.NewReader(strReader) // 将整个字符串做个缓存
	data, _ := bufReader.Peek(5) // 从缓存中读取12个字符，只读不取
	fmt.Println(data)
	fmt.Println(bufReader.Buffered()) // 缓存了多少数据
	fmt.Println(string(data))

	str1, _ := bufReader.ReadString(' ') // 读取缓冲区的数据，到空格为止，并立即取出数据
	fmt.Println(bufReader.Buffered())    // 由于数据已经取出，所以缓存区大小变小了
	fmt.Println(str1)

	str2, _ := bufReader.ReadString('\n') // 再次取剩下的数据
	fmt.Println(bufReader.Buffered()) // 缓存区已经清空
	fmt.Println(str2)
}
```
输出：
```go
[72 101 108 108 111]
11
Hello
5
Hello
0
world
```
用 `Peek` 方法每次只从缓存中读取数据，但不取出数据，所以缓冲大小是整个字符串的长度。<br />用 `ReadString` 每次都会从缓冲区读取并取出数据，所以缓冲区大小会减小。

<a name="lHVbF"></a>
### 写数据
向标准输出中写数据：
```go
func main() {
	bufWriter := bufio.NewWriter(os.Stdout)
	fmt.Fprint(bufWriter, "Hello ") // 向文件中写数据，延续Linux的概念，输出设备也是一种文件
	fmt.Fprint(bufWriter, "world!")
	bufWriter.Flush() // 提交到输出设备
}
```

这里说一下几种 `fmt` 的区别：

- 以 `F` 开头的，将输出到文件
- 以 `S` 开头的，将输出到字符串
- 不加前缀的，输出到标准输出

举例：
```go
str := fmt.Sprintf("pi is %f", 3.14159)
fmt.Print(str)

fmt.Fprintln(os.Stdout, "Hello world\n")
```

<a name="6lTG0"></a>
## 四、文本文件的读写
`os.Open` 打开文件，文件路径是相对于项目根路径的。 
```go
	file, _ := os.Open("res/demo.txt")
	data, _ := ReadFrom(file, 12)
	fmt.Println(data)
	fmt.Println(string(data))
```

<a name="wQ3ql"></a>
### 读取文本文件
下面示例，将读取文本文件并统计其行数。将文件读取到缓存中，通过 `reader.ReadLine` 读取每一行的数据。
```go
func main() {
	file, err := os.Open("res/demo.txt")
    if err != nil {
        fmt.Println("读取文件失败：", err)
        return
    }
    defer file.Close()

    var lineCount int
    reader := bufio.NewReader(file)
    for {
        line, isPrefix, err := reader.ReadLine() // 逐行读取

        if err != nil {
            break
        }

        if !isPrefix {
            lineCount++
            fmt.Println(string(line))
        }
    }

    fmt.Printf("共有%d行", lineCount)
}
```
其中， `ReadLine` 返回三个值，line和err不用说，一个是当前行的byte数据，一个是错误信息。<br />`isPrefix` 是指如果文件中的某一行超过行缓冲大小（默认为4096），则会设置为true，否则为false。如果是true，则在下一次调用 `ReadLine` 的时候返回剩下的数据。

除了使用 `ReadLine` 之外，还可以使用 `ReadString('\n')`来逐行读取 ：
```go
	for {
		str, err := reader.ReadString('\n') // 读到一个换行就结束
		fmt.Print(str)
		if err == io.EOF {                  // io.EOF 表示文件的末尾
			break
		}
	}
```

<a name="rgiHN"></a>
### 写入文本文件
在打开文件的时候，指定文件处理模式为 `os.O_WRONLY | os.O_CREATE`，并设置权限为 `0666` ，则可以往文件中写入数据。
```go
func main() {
	filePath := "output/output.txt"
	file, err := os.OpenFile(filePath, os.O_WRONLY | os.O_CREATE, 0666)
	if err != nil {
		fmt.Printf("打开文件错误= %v \n", err)
		return
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	writer.WriteString("Hello world\r\nHow are you")
	writer.Flush()
}
```
`writer.Flush()`：因为 writer 是带缓存的，因此在调用 WriterString 方法时，内容是先写入缓存的，所以要调用 flush方法，将缓存的数据真正写入到文件中。

<a name="RPpi4"></a>
### 追加文件内容
跟写文件差不多，只需要将文件处理模式设置为 `os.O_APPEND` 即可
```go
func main()  {
	filePath := "res/demo.txt"
	file, err := os.OpenFile(filePath, os.O_APPEND, 0666)
	if err != nil {
		fmt.Printf("打开文件错误= %v \n", err)
		return
	}
	defer file.Close()

	write := bufio.NewWriter(file)
	write.WriteString("\r\nNew line.\r\n")
	write.Flush()
}
```

<a name="KxXqp"></a>
### 文件处理参数
下面列举了一些常用的 flag 文件处理参数：

- **O_RDONLY**：只读模式打开文件；
- **O_WRONLY**：只写模式打开文件；
- **O_RDWR**：读写模式打开文件；
- **O_APPEND**：写操作时将数据附加到文件尾部（追加）；
- **O_CREATE**：如果不存在将创建一个新文件；
- **O_EXCL**：和 O_CREATE 配合使用，文件必须不存在，否则返回一个错误；
- **O_SYNC**：当进行一系列写操作时，每次都要等待上次的 I/O 操作完成再进行；
- **O_TRUNC**：如果可能，在打开时清空文件。

<a name="V3gh3"></a>
## 五、二进制文件的读写
<a name="u8Tap"></a>
### 读取二进制文件（以BMP文件为例）
下面以读取BMP图片文件头为例。<br />BMP的文件头定义可以参考微软文档中C++中的定义：

- [BITMAPFILEHEADER](https://docs.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapfileheader)
- [BITMAPCOREHEADER](https://docs.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608710474993-6ee89f54-6dac-4f80-bf36-138005eb4d4c.png#align=left&display=inline&height=73&originHeight=146&originWidth=511&size=10304&status=done&style=none&width=255.5)<br />C++中的 `WORD` 对应 Go 中的 `uint16` ，也就是2个 `byte` ，C++中的 `DWORD` 对应Go 中的 `uint32` ，也就是4个 `byte` 。<br />

先看一个手动逐个字节读取文件头的例子：
```go
func main() {
	file, err := os.Open("demo.bmp")

    if err != nil {
        fmt.Println("打开文件失败：", err)
        return
    }

    defer file.Close()

    var headA, headB byte
    binary.Read(file, binary.LittleEndian, &headA)
    binary.Read(file, binary.LittleEndian, &headB)

    var size uint32
    binary.Read(file, binary.LittleEndian, &size)

    var reserveA, reserveB uint16
    binary.Read(file, binary.LittleEndian, &reserveA)
    binary.Read(file, binary.LittleEndian, &reserveB)

    var offbits uint32
    binary.Read(file, binary.LittleEndian, &offbits)

    fmt.Printf(" 标识1：%c \n 标识2：%c \n 文件大小：%d \n ReservedA：%d \n ReservedB：%d \n 数据偏移：%d",
           headA, headB, size, reserveA, reserveB, offbits)
}
```
输出信息：
```go
 标识1：B
 标识2：M
 文件大小：786486
 ReservedA：0
 ReservedB：0
 数据偏移：54
```

这样做非常麻烦，我们可以先定义一个结构体，然后用结构体去接收相应的信息。
```go
type BitmapHeader struct {
	HeadA     byte   // B
	HeadB     byte   // M
	Size      uint32 // 文件大小
	ReservedA uint16 // 0
	ReservedB uint16 // 0
	OffBits   uint32 // 数据偏移
}

type BitmapInfoHeader struct {
	Size           uint32 // 结构体大小
	Width          int32  // 宽度
	Height         int32  // 高度
	Planes         uint16 // 面， 恒定为1
	BitCount       uint16 // 每个像素占用的字节数
	Compression    uint32 // 压缩类型
	SizeImage      uint32 // 图形大小
	XPerlsPerMeter int32  // 水平分辨率 每米的像素数
	YPerlsPerMeter int32  // 每米的像素数
	ClrUsed        uint32 // 颜色数
	ClrImportant   uint32 // 调色版
}

func main() {
	file, err := os.Open("demo.bmp")

	if err != nil {
		fmt.Println("打开文件失败：", err)
		return
	}

	defer file.Close()

	bitmapHeader := new(BitmapHeader)
	if err := binary.Read(file, binary.LittleEndian, bitmapHeader); err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(bitmapHeader)

	bitmapInfoHeader := new(BitmapInfoHeader)
	if err := binary.Read(file, binary.LittleEndian, bitmapInfoHeader); err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(bitmapInfoHeader)

	fmt.Println("size", binary.Size(bitmapHeader), binary.Size(bitmapInfoHeader))
}
```
输出：
```go
&{66 77 786486 0 0 54}
&{40 512 512 1 24 0 786432 0 0 0 0}
size 14 40
```

<a name="scTmJ"></a>
### 普通二进制文件的写入
这里用到了 `bytes` 包，以写入3个int32类型（4 bytes）的数据为例：
```go
func main()  {
	file, err := os.Create("output/output.bin")

	info := []int32{25, 30, 255}
	if err != nil {
		fmt.Println("文件创建失败 ", err.Error())
		return
	}
	defer file.Close()

	var binBuf bytes.Buffer
	binary.Write(&binBuf, binary.LittleEndian, info)
	_, err = file.Write(binBuf.Bytes())
	if err != nil {
		fmt.Println("编码失败", err.Error())
		return
	}
	fmt.Println("编码成功")
}
```

<a name="DXrzO"></a>
### 普通二进制文件的读取
```go
func NormalBinaryFileRead()  {
	file, err := os.Open("output/output.bin")
	if err != nil {
		fmt.Println("文件打开失败", err.Error())
		return
	}
	defer file.Close()

	for i := 0; i < 3; i++ {
		data := make([]byte, 4)
		_, err = file.Read(data)
		if err != nil {
			fmt.Println("解码失败", err)
			return
		}
		fmt.Println(data)

		var m int32
		buffer := bytes.NewBuffer(data)
		err = binary.Read(buffer, binary.LittleEndian, &m)
		if err != nil {
			fmt.Println("二进制文件读取失败", err)
			return
		}
		fmt.Println(m)
	}
}
```
输出：
```go
编码成功
[25 0 0 0]
25
[30 0 0 0]
30
[255 0 0 0]
255
```

<a name="jUkWj"></a>
## 六、json文件的读写
<a name="3nRRP"></a>
### 读取json文件
比如有如下json文件：
```go
[{"name":"Golang","course":["Golang基础课程","Golang高级课程"]},{"name":"Java","course":["Java基础课程","Java基础课程"]}]
```
需要先声明一个结构体来接收json数据，然后创建一个json解码器，来解码json数据。
```go
type Courses struct {
	Name   string `json:"name"`
	Course []string `json:"course"`
}

func ReadJsonFile() {
	filePtr, err := os.Open("res/demo.json")
	if err != nil {
		fmt.Println("文件打开失败 [Err:%s]", err.Error())
		return
	}
	defer filePtr.Close()

	var data []Courses
	// 创建json解码器
	decoder := json.NewDecoder(filePtr)
	err = decoder.Decode(&data)
	if err != nil {
		fmt.Println("解码失败", err.Error())
	} else {
		fmt.Println("解码成功")
		fmt.Println(data)
	}
}
```
读出的数据为：
```go
[{Golang [Golang基础课程 Golang高级课程]} {Java [Java基础课程 Java基础课程]}]
```

<a name="WzC0g"></a>
### 写入json文件
在写入json文件之前，需要创建一个json编码器，来编码json数据。
```go
type Courses struct {
	Name   string `json:"name"`
	Course []string `json:"course"`
}

func main() {
	info := []Courses{
		{"Golang", []string{"Golang基础课程", "Golang高级课程"}},
		{"Java", []string{"Java基础课程", "Java基础课程"}}}
	// 创建文件
	filePtr, err := os.Create("reoutput/output.json")
	if err != nil {
		fmt.Println("文件创建失败", err.Error())
		return
	}
	defer filePtr.Close()

	// 创建Json编码器
	encoder := json.NewEncoder(filePtr)
	err = encoder.Encode(info)
	if err != nil {
		fmt.Println("编码错误", err.Error())
	} else {
		fmt.Println("编码成功")
	}
}
```

<a name="nbpH6"></a>
## 七、xml文件的读写
xml文件的读写跟json差不多，只需要将编码器/解码器改为xml的即可。
<a name="JgMnE"></a>
### 读取xml文件
比如有如下xml文件：
```go
<courses name="Golang"><course>Golang基础课程</course><course>Golang高级课程</course></courses>
```
首先需要修改一下 `Courses` 结构体的标签：
```go
type Courses struct {
	Name   string   `json:"name" xml:"name,attr"`
	Course []string `json:"course" xml:"course"`
}
```
这里将name字段修改为了courses 一个属性。<br />关于Tag的相关资料参考：[Golang 中的标签（Tags in Golang）](https://studygolang.com/articles/17951)

读取xml文件的核心逻辑如下：
```go

func main() {
	filePtr, err := os.Open("res/demo.xml")
	if err != nil {
		fmt.Println("文件打开失败 [Err:%s]", err.Error())
		return
	}
	defer filePtr.Close()

	var data Courses
	// 创建json解码器
	decoder := xml.NewDecoder(filePtr)
	err = decoder.Decode(&data)
	if err != nil {
		fmt.Println("解码失败", err.Error())
	} else {
		fmt.Println("解码成功")
		fmt.Println(data)
	}
}
```
读出的数据为：
```go
{Golang [Golang基础课程 Golang高级课程]}
```

<a name="EmFqW"></a>
### 写入xml文件
跟写json文件类似：
```go
func main() {
	info := Courses{"Golang", []string{"Golang基础课程", "Golang高级课程"}}
	// 创建文件
	filePtr, err := os.Create("output/output.xml")
	if err != nil {
		fmt.Println("文件创建失败", err.Error())
		return
	}
	defer filePtr.Close()

	// 创建Json编码器
	encoder := xml.NewEncoder(filePtr)
	err = encoder.Encode(info)
	if err != nil {
		fmt.Println("编码错误", err.Error())
	} else {
		fmt.Println("编码成功")
	}
}
```

<a name="gTsHy"></a>
## 八、Gob文件
<a name="06QF0"></a>
### 什么是Gob文件
Gob 是Go语言自己以二进制形式序列化和反序列化程序数据的格式，可以在 encoding 包中找到。这种格式的数据简称为 Gob（即 Go binary 的缩写）。类似于 Python 的“pickle”和 Java 的“Serialization”。

Gob 和 JSON 的 pack 之类的方法一样，由发送端使用 Encoder 对数据结构进行编码。在接收端收到消息之后，接收端使用 Decoder 将序列化的数据变化成本地变量。

Go语言可以通过 JSON 或 Gob 来序列化 struct 对象，虽然 JSON 的序列化更为通用，但利用 Gob 编码可以实现 JSON 所不能支持的 struct 的方法序列化，利用 Gob 包序列化 struct 保存到本地也十分简单。

Gob 不是可外部定义、语言无关的编码方式，它的首选的是二进制格式，而不是像 JSON 或 XML 那样的文本格式。Gob 并不是一种不同于 Go 的语言，而是在编码和解码过程中用到了 Go 的反射。

Gob 通常用于远程方法调用参数和结果的传输，以及应用程序和机器之间的数据传输。Gob 特定的用于纯 Go 的环境中，例如两个用Go语言写的服务之间的通信。这样的话服务可以被实现得更加高效和优化。

Gob 文件或流是完全自描述的，它里面包含的所有类型都有一个对应的描述，并且都是可以用Go语言解码，而不需要了解文件的内容。

只有可导出的字段会被编码，零值会被忽略。在解码结构体的时候，只有同时匹配名称和可兼容类型的字段才会被解码。当源数据类型增加新字段后，Gob 解码客户端仍然可以以这种方式正常工作。解码客户端会继续识别以前存在的字段，并且还提供了很大的灵活性，比如在发送者看来，整数被编码成没有固定长度的可变长度，而忽略具体的 Go 类型。

<a name="SXpIE"></a>
### 创建Gob文件
可以往gob中写任何类型的数据，包括字符串、Map、结构体等。以Map为例：
```go
func main() {
	info := map[string]interface{}{
		"name": "小昱",
		"sex": "男",
		"age": 18,
	}
	name := "output/demo.gob"
	File, _ := os.OpenFile(name, os.O_RDWR|os.O_CREATE, 0777)
	defer File.Close()
	enc := gob.NewEncoder(File)
	if err := enc.Encode(info); err != nil {
		fmt.Println(err)
	}
}
```

<a name="UpkpL"></a>
### 读取Gob文件
```go
func main() {
	var M map[string]interface{}
	File, _ := os.Open("output/demo.gob")
	D := gob.NewDecoder(File)
	D.Decode(&M)
	fmt.Println(M)
}
```
读取结果为：
```go
map[age:18 name:小昱 sex:男]
```

<a name="QXq5l"></a>
## 九、zip文件的读写
这里需要用到 `"archive/zip"` 这个包。
<a name="fgR9p"></a>
### 写入zip文件
```go
func main() {
	// 创建一个缓冲区用来保存压缩文件内容
	buf := new(bytes.Buffer)
	// 创建一个压缩文档
	w := zip.NewWriter(buf)
	// 将文件加入压缩文档
	var files = []struct {
		Name, Body string
	}{
		{ "test1.txt", "Hello world" },
		{ "test2.txt", "How are you" },
	}
	for _, file := range files {
		f, err := w.Create(file.Name)
		if err != nil {
			fmt.Println(err)
		}
		_, err = f.Write([]byte(file.Body))
		if err != nil {
			fmt.Println(err)
		}
	}
	// 关闭压缩文档
	err := w.Close()
	if err != nil {
		fmt.Println(err)
	}
	// 将压缩文档内容写入文件
	f, err := os.OpenFile("output/output.zip", os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		fmt.Println(err)
	}
	buf.WriteTo(f)
}
```
创建好的压缩文件目录结构：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608777371633-3f4826c6-d221-4e58-b813-8bd0a6c645bc.png#align=left&display=inline&height=167&originHeight=333&originWidth=492&size=44984&status=done&style=none&width=246)

<a name="BNdkU"></a>
### 读取zip文件
```go
func main() {
	// 打开一个zip格式文件
	r, err := zip.OpenReader("output/output.zip")
	if err != nil {
		fmt.Printf(err.Error())
	}
	defer r.Close()

	// 迭代压缩文件中的文件，打印出文件中的内容
	for _, f := range r.File {
		fmt.Printf("文件名: %s\n", f.Name)

		rc, err := f.Open()
		if err != nil {
			fmt.Printf(err.Error())
		}
		fmt.Printf("文件内容：")
		_, err = io.CopyN(os.Stdout, rc, int64(f.UncompressedSize64))
		fmt.Println("")

		if err != nil {
			fmt.Printf(err.Error())
		}
		rc.Close()
	}
}
```

<a name="LFp2b"></a>
## 十、tar文件的读写
tar 是一种打包格式，但不对文件进行压缩，所以打包后的文档一般远远大于 zip 和 tar.gz，因为不需要压缩的原因，所以打包的速度是非常快的，打包时 CPU 占用率也很低。

创建 tar 归档文件与创建 .zip 归档文件非常类似，主要不同点在于我们将所有数据都写入相同的 writer 中，并且在写入文件的数据之前必须写入完整的头部，而非仅仅是一个文件名。

tar 打包实现原理如下：

- 创建一个文件 x.tar，然后向 x.tar 写入 tar 头部信息；
- 打开要被 tar 的文件，向 x.tar 写入头部信息，然后向 x.tar 写入文件信息；
- 当有多个文件需要被 tar 时，重复第二步直到所有文件都被写入到 x.tar 中；
- 关闭 x.tar，完成打包。

<a name="Isvjj"></a>
### 写入tar文件
```go
func main() {
	f, err := os.Create("output/output.tar") //创建一个 tar 文件
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	tw := tar.NewWriter(f)
	defer tw.Close()

	filePath := "res/demo.txt" // 需要打包的文件路径
	fileInfo, err := os.Stat(filePath) //获取文件相关信息
	if err != nil {
		fmt.Println(err)
	}

	hdr, err := tar.FileInfoHeader(fileInfo, "")
	if err != nil {
		fmt.Println(err)
	}

	err = tw.WriteHeader(hdr) //写入头文件信息
	if err != nil {
		fmt.Println(err)
	}

	f1, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
		return
	}

	m, err := io.Copy(tw, f1) //将main.exe文件中的信息写入压缩包中
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(m)
}
```
打包好的文件：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608778002423-f9022bdf-0209-464f-be3c-bda7ab225237.png#align=left&display=inline&height=166&originHeight=332&originWidth=477&size=45501&status=done&style=none&width=238.5)

<a name="6R0B4"></a>
### 读取tar文件
```go
func main() {
	f, err := os.Open("output/output.tar")
	if err != nil {
		fmt.Println("文件打开失败", err)
		return
	}
	defer f.Close()

	r := tar.NewReader(f)
	for hdr, err := r.Next(); err != io.EOF; hdr, err = r.Next() {
		if err != nil {
			fmt.Println(err)
			return
		}
		fileinfo := hdr.FileInfo()
		fmt.Println(fileinfo.Name())
		f, err := os.Create("output/" + fileinfo.Name())
		if err != nil {
			fmt.Println(err)
		}
		defer f.Close()

		_, err = io.Copy(f, r)
		if err != nil {
			fmt.Println(err)
		}
	}
}
```

<a name="7K1cp"></a>
## 十一、文件操作工具类
需要借助于 `"io/ioutil"` 这个包可以很容易地完成文件操作：读写文件、复制文件等。
<a name="f72yU"></a>
### 复制文件
下面这个例子展示了适用工具类读写文件、复制文件的操作。
```go
func CopyTextFile() {
	srcFilePath := "res/demo.txt"
	destFilePath := "output/demo.txt"
	data, err := ioutil.ReadFile(srcFilePath)
	fmt.Println(string(data)) // 打印内容
    
	if err != nil {
		fmt.Printf("文件打开失败=%v\n", err)
		return
	}
	err = ioutil.WriteFile(destFilePath, data, 0666)
	if err != nil {
		fmt.Printf("文件打开失败=%v\n", err)
	}
}
```
这不光适用于文本文件，任何文件都适用。如果是文本文件，打开时还可以直接转化为字符串输出

<a name="jYMmG"></a>
## 参考资料

- [Go语言数据I/O对象及操作](http://c.biancheng.net/view/5569.html)
- [Go语言文件处理](http://c.biancheng.net/golang/102/)

