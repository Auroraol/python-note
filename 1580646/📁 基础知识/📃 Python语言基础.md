
<a name="jucwT"></a>
## 输入输出语句

<a name="8l91c"></a>
### 输出

用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。

```python
print('hello world')
```

`print()` 函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出。print()会依次打印每个字符串，遇到逗号“,”会输出一个空格。

```python
print('hello', 'world')
```

<a name="SX9nm"></a>
### 输入

Python提供了一个 `input()`，可以让用户输入字符串，并存放到一个变量里。

```python
name = input()
print('hello', name)
```

也可使用 `sys.stdout` 命名空间下的输出语句:

```python
import sys;
x = 'hello world';
sys.stdout.write(x + '\n')
```


<a name="gzyW3"></a>
## 注释

使用`#`开始的语句就是注释语句。

通常在文件开头写上这两行：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

第一行注释是为了告诉`Linux/OS X`系统，这是一个`Python`可执行程序，`Windows`系统会忽略这个注释；

第二行注释是为了告诉`Python`解释器，按照`UTF-8`编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

申明了`UTF-8`编码并不意味着你的`.py`文件就是`UTF-8`编码的，必须并且要确保文本编辑器正在使用`UTF-8 without BOM`编码。

如果`.py`文件本身使用`UTF-8`编码，并且也申明了`# -*- coding: utf-8 -*-`，打开命令提示符测试就可以正常显示中文。

<a name="kYzQW"></a>
### 字符串注释

任何模块代码的第一个字符串都被视为模块的文档注释。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
```

<a name="YnseB"></a>
### 三引号注释

三引号注释可以实现多行注释，而不必在每一行都加上 #

```python
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
"""
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
"""
```

<a name="9DwHX"></a>
## 变量、常量声明

不同于其他语言，变量不需要显式声明，比如 `js` 中的 `var`，`php` 中的 `$`，Python中直接对变量进行赋值即可使用。

```python
a = 1
PI = 3.14159265359
a = True
```

习惯性的，变量使用小写，常量使用大写。但事实上，并不能将常量的值定死，还能重新对常量进行赋值，因此在后面使用如下语句仍然有效:

```python
PI = 1
```

这种变量本身类型不固定的语言称之为`动态语言`，与之对应的是静态语言。

<a name="Q3tzH"></a>
## 保留字

先导入 `keyword` 模块，输入 `keyword.kwlist` 即可输出系统保留字

```python
import keyword
keyword.kwlist
# 输出
['False', 'None', 'True', 'and', 'as',
'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from',
'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
```

本文陆续会讲到这些保留字的用法

这里分下类：

- 数据类型相关 False、True、None
- 运算符相关 or、and、not
- 控制流程相关 break、continue、if、elif、else、for、while、return
- 函数、模块、面向对象相关 class、def、import、from、pass、lambda
- 异常处理相关 try、finally
- 文件操作相关 with、as
- 其他 del、in、is、assert、async、await、except、global、nonlocal、raise、yield


<a name="ghbZW"></a>
## 分支语句

<a name="ZDrMu"></a>
### if...elif...else

这个很简单，同其他语言一样，不过注意不是花括号语法，而是使用冒号 `:` 开始一段代码块，使用缩进代码块的风格添加语句。

分为以下几种使用场景:

1. 单if语句

```python
if condition:
  # some code
```

2. if-else语句

```python
if condition:
  # some code
elif:
  # some code
```

3. if-elif-else语句

```python
if condition:
  # some code
elif condition:
  # some code
else:
  # some code
```

示例如下:

```python
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```

```python
x = True
if x:
    print('True')
```

<a name="hsgVe"></a>
### 与input一起使用

```python
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
```

因为`input()`返回的数据类型是`str`，`str`不能直接和整数比较，必须先把`str`转换成整数。Python提供了`int()`函数将str转化为int。

<a name="86sz0"></a>
## 循环语句

<a name="u7RYI"></a>
### for...in

可以直接作用于`for`循环的数据类型有以下两种:

- 一类是集合数据类型，如`list`、`tuple`、`dict`、`set`、`str`等；
- 一类是`generator`，包括生成器和带`yield`的generator function。

这些可以直接作用于`for`循环的对象统称为可迭代对象：`Iterable`。

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

```python
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
```

<a name="YaFv8"></a>
### range()

使用range()函数可以生成一个整数序列，再通过list()函数可以转换为list。

```python
>>> a = range(5)
>>> print(list(a))
[0, 1, 2, 3, 4]
```

range() 可以直接作为可迭代对象

带一个参数，表示0-max

```python
sum = 0
for x in range(100):
    sum = sum + x
print(sum)
```

带两个参数，表示min-max

```python
sum = 0
for x in range(10, 20):
    sum = sum + x
print(sum)
```

<a name="TJQNR"></a>
### while

对于不能确定循环次数的循环，可以使用while循环，只要条件满足，就不断循环，条件不满足时退出循环。

```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```

<a name="nWtvf"></a>
### break

使用break终止循环。

```python
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
```

<a name="10lQH"></a>
### continue

使用continue终止当前循环，直接进入下一次循环。

```python
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```



