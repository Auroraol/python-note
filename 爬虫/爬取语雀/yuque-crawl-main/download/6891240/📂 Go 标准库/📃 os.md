相关的包：
```go
import (
	"fmt"
	"io/ioutil"
	"os"
)
```
<a name="xSobX"></a>
## 一、获取当前工作路径
```go
currentPath, _ := os.Getwd()
fmt.Println(currentPath)
```

<a name="PZ2Zn"></a>
## 二、获取文件（夹）信息
```go
	filePath := "c:/windows/notepad.exe"
	stat, _ := os.Stat(filePath)
	fmt.Println("文件（夹）名：", stat.Name())
	fmt.Println("文件大小：", stat.Size())
	fmt.Println("权限：", stat.Mode())
	fmt.Println("是否是文件夹：", stat.IsDir())
	fmt.Println("修改时间：", stat.ModTime())
```
输出：
```go
文件名： notepad.exe
文件大小： 202240
权限： -rw-rw-rw-
是否是文件夹： false
修改时间： 2020-09-15 14:16:51.9560539 +0800 CST
```

先读取文件再获取文件信息：
```go
	filePath := "c:/windows"
	file, _ := os.Open(filePath)
	fmt.Println(file.Name())
	fmt.Println(file.Stat())
```

<a name="vo17s"></a>
## 三、列出子文件（夹）
只列出子文件（夹）名字：
```go
	filePath := "c:/windows"
	file, _ := os.Open(filePath)
	for i := 1; ; i++{
		names, err := file.Readdirnames(10 * i)
		if err != nil {
			break
		}
		for _, name := range names{
			fmt.Println(name)
		}
	}
```

获取所有子文件：
```go
	filePath := "c:/windows"
	file, _ := os.Open(filePath)
	for i := 1; ; i++{
		names, err := file.Readdir(10 * i)
		if err != nil {
			break
		}
		for _, file := range names{
			if file.IsDir() {
				continue
			}
			fmt.Println(file.Name())
		}
	}
```

<a name="Gu9i4"></a>
## 四、创建、修改、删除、拷贝、重命名
创建文件夹：
```go
	err := os.Mkdir("d:/test", 0666)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("创建文件夹成功")
```

创建文件：
```go
	_, err := os.Create("d:/test")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("创建文件成功")
```
:::info
注意：如果有同名的文件夹存在，创建同名文件将会失败
:::

重命名（移动文件）：
```go
	err := os.Rename("d:/test", "d:/test1")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("重命名成功")
```

删除文件：
```go
	err := os.Remove("d:/test")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("删除文件成功")
```

拷贝文件：暂时没有发现现成的API，可以自己封装一个拷贝文件的方法。
```go
func CopyFile(srcPath string, destPath string) {
	data, err := ioutil.ReadFile(srcPath)
	fmt.Println(string(data))
	if err != nil {
		fmt.Printf("文件打开失败=%v\n", err)
		return
	}
	err = ioutil.WriteFile(destPath, data, 0666)
	if err != nil {
		fmt.Printf("文件拷贝失败=%v\n", err)
		return
	}
	fmt.Println("拷贝成功")
}

// 调用
CopyFile("d:/test", "d:/test1")
```

