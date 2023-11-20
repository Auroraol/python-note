查看系统中所有的 shell 解释器

```bash
$ cat /etc/shells
/bin/sh
/bin/bash
/sbin/nologin
/usr/bin/sh
/usr/bin/bash
/usr/sbin/nologin
/bin/tcsh
/bin/csh
```

<a name="8b4c8c40"></a>
## shell 基础

<a name="ddc7d28b"></a>
### 变量

声明变量直接赋值即可，通过 $var 引用一个变量，比如：

```bash
name=quanzaiyu

$ echo $name
quanzaiyu
```

<a name="50387244"></a>
### 命令结果

使用 $(command) 引用命令执行的结果，比如：

```bash
$ echo $(pwd)
/home
```

使用 `command` 也是引用命令执行的结果，比如：

```bash
$ echo `pwd`
/home
```

<a name="bfac9666"></a>
### 逻辑连接

使用一些逻辑运算符执行多条命令，比如：

```bash
$ echo 123 && echo 456
123
456
$ lll && echo ok
bash: lll: 未找到命令...
$ lll || echo ok
bash: lll: 未找到命令...
ok
```

<a name="d3e31548"></a>
### 分支结构

if 条件：

```bash
$ vim if.sh
read -p 'Please enter a:' a
if [ $a == 5 ]
  then
    echo 5
else
  echo !5
fi

$ sh for.sh
Please enter a:5
5
$ sh for.sh
Please enter a:1
!5
```

<a name="037bdbce"></a>
### 循环结构

for 循环：

```bash
$ vim for.sh
for i in {1..3};
  do echo hello $i;
done;

$ sh for.sh
hello 1
hello 2
hello 3
```

while 循环：

```bash
$ vim while.sh
a=1
while [ $a -eq 1 ]
  do echo hello world!
  a+=1
done

$ sh while.sh
hello world!
```

```bash
$ vim while.sh
a=1
while [ $a -le 5 ]
  do echo hello world!
  a=$((a+1))
done

$ sh while.sh
hello world!
hello world!
hello world!
hello world!
hello world!
```

<a name="fa53508d"></a>
## shell 脚本编写

一个简单的 shell 脚本格式如下：

```bash
#!/bin/bash

echo hello world!
```

<a name="db0c4285"></a>
## 解释器的区别

文件的第一句为声明执行器路径，不同的执行器可能产生不同的结果

- `#!/bin/sh` 当某行代码出错时，不继续往下解释，等价于 `#!/bin/bash --posix`
- `#!/bin/bash` 忽略出错的行继续解释代码
