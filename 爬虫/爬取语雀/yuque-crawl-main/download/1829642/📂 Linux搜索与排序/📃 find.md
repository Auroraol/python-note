**find** 命令用来在指定目录下查找文件。任何位于参数之前的字符串都将被视为欲查找的目录名。如果使用该命令时，不设置任何参数，则find命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

<a name="9bd86151"></a>
## 常用选项

- **-name** 文件或目录
- **-path** 路径
- **-size** 文件大小
- **-regex** 正则匹配
- **-iregex** 此参数的效果和指定“-regex”参数类似，但忽略字符大小写的差别
- **-user** 用户

<a name="f3215c97"></a>
## 根据类型进行匹配

**-type** 用于匹配文件类型

- `b` 特殊块文件(缓冲的)
- `c` 特殊字符文件(不缓冲)
- `d` 目录
- `p` 命名管道 (FIFO)
- `f` 普通文件
- `l` 符号链接
- `s` 套接字
- `D` 门 (Solaris 特有)

<a name="0f9f17d7"></a>
## 根据时间进行匹配

UNIX/Linux文件系统每个文件都有三种时间戳

- **访问时间**（-atime/天，-amin/分钟）用户最近一次访问时间
- **修改时间**（-mtime/天，-mmin/分钟）文件最后一次修改时间
- **变化时间**（-ctime/天，-cmin/分钟）文件数据元（例如权限等）最后一次修改时间

<a name="01deb75d"></a>
## 根据文件大小进行匹配

```bash
find . -type f -size 文件大小单元
```

文件大小单元：

- **b** —— 块（512字节）
- **c** —— 字节
- **w** —— 字（2字节）
- **k** —— 千字节
- **M** —— 兆字节
- **G** —— 吉字节

<a name="d19f2c10"></a>
## 基本使用

```bash
find . # 列出当前目录及子目录下所有文件和文件夹, 其中 `.` 可省略

find / -path '*.repo' # 匹配所有指定路径的文件
find / -name '*.repo' # 同上
find /usr -path "*local*" # 搜索路径中包含 local 的文件
find /home -name "*.txt" # 在 `/home` 目录下查找以 .txt 结尾的文件名, 其中引号可省略
find /home -iname "*.txt" # 同上，但忽略大小写

find . -type f -size +10k # 搜索大于10KB的文件
find . -type f -size -10k # 搜索小于10KB的文件
find . -type f -size 10k # 搜索等于10KB的文件

find . -type f -atime -7 # 搜索最近7天内被访问过的所有文件
find . -type f -atime 7 # 搜索恰好在7天前被访问过的所有文件
find . -type f -atime +7 # 搜索超过7天内被访问过的所有文件
find . -type f -mtime -10 # 搜索在10天内被创建或者修改过的所有文件
find . -type f -amin +10 # 搜索访问时间超过10分钟的所有文件
find . -type f -newer file.log # 找出比file.log修改时间更长的所有文件

find . -name "*.txt" -o -name "*.pdf" # 当前目录及子目录下查找所有以 .txt 和 .pdf 结尾的文件
find . \( -name "*.txt" -o -name "*.pdf" \) # 同上

find . -regex ".*\(\.txt\|\.pdf\)$" # 基于正则表达式匹配文件路径
find . -iregex ".*\(\.txt\|\.pdf\)$" # 同上，但忽略大小写

find . -maxdepth 3 -type f # 向下最大深度限制为3
find . -mindepth 2 -type f # 搜索出深度距离当前目录至少2个子目录的所有文件

find . -type f -perm 777 # 当前目录下搜索出权限为777的文件
find . -type f -user tom # 找出当前目录用户tom拥有的所有文件
find . -type f -group sunk # 找出当前目录用户组sunk拥有的所有文件
```

<a name="deb55e9e"></a>
## 借助 `-exec` 选项与其他命令结合使用

> 找出当前目录下所有用户权限为root的文件，并把所有权更改为用户tom


```bash
find . -type f -user root -exec chown tom {} \;
```

上例中，**{}** 用于与 **-exec** 选项结合使用来匹配所有文件，然后会被替换为相应的文件名。

> 找出自己家目录下所有的 .txt 文件并删除


```bash
find $HOME/. -name "*.txt" -ok rm {} \;
```

上例中，**-ok**和**-exec**行为一样，不过它会给出提示，是否执行相应的操作。

> 查找当前目录下所有.txt文件并把他们拼接起来写入到 all.txt 文件中


```bash
find . -type f -name "*.txt" -exec cat {} \;> all.txt
```

> 将30天前的.log文件移动到old目录中


```bash
find . -type f -mtime +30 -name "*.log" -exec cp {} old \;
```

> 找出当前目录下所有.txt文件并以“File:文件名”的形式打印出来


```bash
find . -type f -name "*.txt" -exec printf "File: %s\n" {} \;
```

> 因为单行命令中-exec参数中无法使用多个命令，以下方法，将多条命令写在 .sh 文件中，可以实现在-exec之后接受多条命令


```bash
find . -type f -name "*.txt" -exec ./text.sh {} \;
```

<a name="c38f15ed"></a>
## 否定参数

```bash
find /home ! -name "*.txt" # 找出/home下不是以.txt结尾的文件
find . -type f -name "*.php" ! -perm 644 # 找出当前目录下权限不是644的 php 文件
```

<a name="d51a0b34"></a>
## 删除匹配文件

删除当前目录下所有.txt文件

```bash
find . -type f -name "*.txt" -delete
```

<a name="bab52e17"></a>
## 要列出所有长度为零的文件

```bash
find . -empty
```

