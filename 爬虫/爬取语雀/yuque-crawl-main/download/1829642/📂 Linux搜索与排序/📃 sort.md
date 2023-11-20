`sort` 将文件/文本的每一行作为一个单位，相互比较，比较原则是从首字符向后，依次按ASCII码值进行比较，最后将他们按升序输出。

```bash
ls | sort # 正序输出
ls | sort -r # 逆序输出
sort sort.txt # 正序输出sort.txt中每一行的内容
sort -u sort.txt # 忽略相同行，或者使用 uniq
uniq sort.txt # 忽略相同行
```
