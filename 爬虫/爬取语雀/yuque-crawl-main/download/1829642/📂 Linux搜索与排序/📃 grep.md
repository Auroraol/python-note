**grep** （global search regular expression(RE) and print out the line，全面搜索正则表达式并把行打印出来）是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来。

> 在文件中搜索一个单词，命令会返回一个包含 **match_pattern** 的文本行


```bash
grep match_pattern file_name
grep "match_pattern" file_name
```

> 在多个文件中查找


```bash
grep "match_pattern" file_1 file_2 file_3 ...
```

> **-v** 反转查找


输出除匹配之外的所有行 **-v** 选项

```bash
grep -v "match_pattern" file_name
ls | egrep -v '*\.txt'
```

> **--color=auto** 标记匹配颜色


```bash
grep "match_pattern" file_name --color=auto
```

> **-E** 使用正则表达式


```bash
$ grep -E "[1-9]+"
# 或
egrep "[1-9]+"
```

> **-o** 只输出文件中匹配到的部分


```bash
$ echo this is a test line. | grep -o -E "[a-z]+\."
line.

$ echo this is a test line. | egrep -o "[a-z]+\."
line.
```

> **-c** 统计文件或者文本中包含匹配字符串的行数


```bash
grep -c "text" file_name
ls | egrep -c '*\.txt'
```

> **-n** 输出包含匹配字符串的行数


```bash
$ grep "text" -n file_name
# 或
cat file_name | grep "text" -n

# 多个文件
grep "text" -n file_1 file_2
```

> **-bo** 打印样式匹配所位于的字符或字节偏移


```bash
$ echo gun is not unix | grep -bo "not"
7:not
```

一行中字符串的字符便宜是从该行的第一个字符开始计算，起始值为0

> 搜索多个文件并查找匹配文本在哪些文件中


```bash
grep -l "text" file1 file2 file3... # 显示哪些文件包含搜索内容
grep -bon "text" file1 file2 file3... # 同时输出行列号
```

> **-r** 在多级目录中对文本进行递归搜索


```bash
grep "text" . -r -n
```

> **-i** 忽略大小写


```bash
$ echo "hello world" | grep -i "HELLO"
hello
```

> **-e** 指定多个匹配


```bash
$ echo this is a text line | grep -e "is" -e "line" -o
is
line
```

也可以使用 `-f` 选项来匹配多个样式，在样式文件中逐行写出需要匹配的字符。

```bash
$ cat patfile
aaa
bbb

echo aaa bbb ccc ddd eee | grep -f patfile -o
```

> **-q** 静默输出


```bash
grep -q "test" filename

#不会输出任何信息，如果命令运行成功返回0，失败则返回非0值。一般用于条件测试。
```

> 在 grep 搜索结果中包括或者排除指定文件


```bash
#只在目录中所有的.php和.html文件中递归搜索字符"main()"
grep "main()" . -r --include *.{php,html}

#在搜索结果中排除所有README文件
grep "main()" . -r --exclude "README"

#在搜索结果中排除filelist文件列表里的文件
grep "main()" . -r --exclude-from filelist
```

> 使用 0 值字节后缀的 grep 与 xargs


```bash
#测试文件：
echo "aaa" > file1
echo "bbb" > file2
echo "aaa" > file3

grep "aaa" file* -lZ | xargs -0 rm

#执行后会删除file1和file3，grep输出用-Z选项来指定以0值字节作为终结符文件名（\0），xargs -0 读取输入并用0值字节终结符分隔文件名，然后删除匹配文件，-Z通常和-l结合使用。
```

> 打印出匹配文本之前或者之后的行


```bash
#显示匹配某个结果之后的3行，使用 -A 选项：
seq 10 | grep "5" -A 3
5
6
7
8

#显示匹配某个结果之前的3行，使用 -B 选项：
seq 10 | grep "5" -B 3
2
3
4
5

#显示匹配某个结果的前三行和后三行，使用 -C 选项：
seq 10 | grep "5" -C 3
2
3
4
5
6
7
8

#如果匹配结果有多个，会用“--”作为各匹配结果之间的分隔符：
echo -e "a\nb\nc\na\nb\nc" | grep a -A 1
a
b
--
a
b
```

