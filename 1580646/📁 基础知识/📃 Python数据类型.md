Python有如下一些基本的数据类型

- **Number** （数字）
   - 整数(int): 1，100，-8080，0，0xff00，0xa5b4c3d2
   - 浮点数(float): 1.23，3.14，-9.01，1.23e9，1.2e-5
   - 复数(complex): 1 + 2j、 1.1 + 2.2j
- **String** （字符串str）: 'abc'，"xyz"，'I'm "OK"!'
- **Boolean** （布尔值bool）: True、False（注意首字母是大写）
- **None** （空值）: None
- **List** （列表list）
- **Tuple** （元组tuple）
- **Set** （集合set）
- **Dictionary** （字典dict）

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597152451093-6d58737e-a29a-44cb-95ac-6f7a6e75a627.png)
<a name="383949bc"></a>
##   布尔值(**Boolean**)

布尔值和布尔代数的表示完全一致，一个布尔值只有 `True` 、 `False` 两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），布尔值可以用and、or和not运算。

**转化为布尔值**

使用转换函数 `bool()` 即可将其他数据类型的对象转化为布尔值

```python
>>> bool(1)
True
```

<a name="b614b0b0"></a>
##   空值(None)

空值是Python里一个特殊的值，用 `None` 表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

<a name="XcHaI"></a>
##   数字(Number)

Python支持int, float, complex三种不同的数字类型。

<a name="v876p"></a>
### 整数(int)

Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样，例如：1，100，-8080，0，等等。

计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

**转化为int**

使用转换函数 `int()` 即可将其他数据类型的对象转化为整数

```python
>>> int(1.2)
1
>>> int(False)
0
>>> int('4')
4
>>> int({'a', 'b', 'c'})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
```

注意到，只能将一个 string，bytes-like object，number转化为int，否则会报错。

<a name="bfMIA"></a>
### 浮点数(float)

浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。

整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

**转化为float**

使用转换函数 `float()` 即可将其他数据类型的对象转化为浮点数

```python
>>> float('1.2222')
1.2222
>>> float(False)
0.0
```

<a name="8QK5H"></a>
### 复数(complex)

python的强大之处在于其可以直接支持复数的运算和操作，在做科学计算时很有帮助，本人并不深入研究复数，就不展开说明。

**转化为complex**

使用转换函数 `complex()` 即可将其他数据类型的对象转化为复数

```python
>>> complex(1)
(1+0j)
```

<a name="9061c9c5"></a>
##   字符串(**String**)

字符串是以单引号`'`或双引号`"`括起来的任意文本，比如`'abc'`，`"xyz"`等等。

- Python中的字符串可以使用单引号、双引号和三引号（三个单引号或三个双引号）括起来，使用反斜杠\转义特殊字符。
- Python3源码文件默认以UTF-8编码，所有字符串都是unicode字符串。
- 支持字符串拼接、截取等多种运算。

`''`或`""`本身只是一种表示方式，不是字符串的一部分，因此，字符串`'abc'`只有`a`，`b`，`c`这3个字符。如果`'`本身也是一个字符，那就可以用`""`括起来，比如`"I'm OK"`包含的字符是`I`，`'`，`m`，空格，`O`，`K`这6个字符。

> **字符转义**


如果字符串内部既包含`'`又包含`"`怎么办？可以用转义字符`\`来标识，比如：

```python
'I\'m \"OK\"!'
```

表示的字符串内容是：

```python
I'm "OK"!
```

转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`。

> **十六进制表示**


```python
>>> '\u4e2d\u6587'
'中文'
```

> **bytes字节码**


Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

在bytes中，无法显示为ASCII字符的字节，用\x###显示。

```python
b'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'
```
**
> **多行语句，在行尾使用反斜杠  ****`\`**** 进行多行语句的连接**


```python
total = item_one + \
        item_two + \
        item_three
```

> **在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 ****`\`**


```python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```

> **自然字符串，使用 r'' 表示引号内部的字符串默认不转义**


```python
>>> print('\\\t\\')
\       \
>>> print(r'\\\t\\')
\\\t\\
```

> **使用三引号 ''' 表示多行内容**


```python
>>> print('''line1
    line2
    line3''')
line1
line2
line3
```

<a name="Dzt6M"></a>
### 常用方法

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597152594255-9809474d-0037-4fb5-be7c-35d1f1800544.png)
**示例**

```python
>>> '   Abc   '.strip(' c')
'Ab'
>>> 'abc'.replace('a', 'A')
'Abc'
>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']
```

**字符串查找 find**

find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

```python
str.find(str, beg=0, end=len(string))
```

- str -- 指定检索的字符串
- beg -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。

```python
>>> '   Abc   '.find('c')
5
```

**字符串统计 count**

count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

```python
str.count(sub, start= 0,end=len(string))
```

- sub -- 搜索的子字符串
- start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
- end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

```python
>>> 'absasbsa'.count('a')
3
```

更多方法参看 [http://www.runoob.com/python3/python3-string.html](http://www.runoob.com/python3/python3-string.html)

<a name="015f2cbb"></a>
### 字符编码转化

- `ord()` 函数获取字符的整数表示
- `chr()` 函数把编码转换为对应的字符

```python
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

<a name="kWkHo"></a>
### encode 和 decode

- `encode()` 将以Unicode表示的str编码为指定的bytes
- `decode()` 把bytes转化为为str

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('gb2312')
b'\xd6\xd0\xce\xc4'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

如果bytes中包含无法解码的字节，decode() 方法会报错：

```python
>>> b'\xe4\xb8\xad\xff'.decode('utf-8')
Traceback (most recent call last):
  ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
```

如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节:

```python
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
```

<a name="2154c04e"></a>
### 计算字符串的长度

`len()` 计算str的字符数，或者bytes的字节数（在python3中以字符为单位，在python2中以字节为单位）

```python
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
```

<a name="fa177520"></a>
### 字符串格式化

可以在表达式后添加 `%` 以填充使用占位符表示的值，如果是多个占位符可以使用 `% ( )` 的形式填充多个值。

| 占位符 | 替换内容 |
| --- | --- |
| %d | 整数 |
| %f | 浮点数 |
| %s | 字符串 |
| %x | 十六进制整数 |


```python
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
```

如果字符串里面的%是一个普通字符，这个时候就需要转义，用`%%`来表示一个%：

```python
>>> 'growth rate: %d%%' % 7
'growth rate: 7%'
```

字符串对象的 `rjust()` 方法, 它可以将字符串靠右, 并在左边填充空格。<br />还有类似的方法, 如 `ljust()` 和 `center()`。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

如打印平方立方表

```python
for x in range(1, 11):
    print(repr(x).ljust(5), repr(x*x).ljust(5), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(5))
```

```bash
$ python test.py
1     1         1
2     4         8
3     9        27
4     16       64
5     25      125
6     36      216
7     49      343
8     64      512
9     81      729
10    100    1000
```

<a name="601c4195"></a>
#### format()

另一种格式化字符串的方法是使用字符串的`format()`方法，它会用传入的参数依次替换字符串内的占位符`{0}、{1}……`，不过这种方式写起来比%要麻烦得多：

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

<a name="d1bb2865"></a>
### 将其他数据类型转化为字符串

使用转换函数 `str()` 即可将其他数据类型的对象转化为字符串

```python
>>> str(1.22)
'1.22'
>>> str({'a', 'b', 'c'})
"{'b', 'a', 'c'}"
>>> str(False)
'False'
>>> str('hello, python3\n')
'hello, python3\n'
```

`repr()` 函数可以转义字符串中的特殊字符

```python
>>> repr('hello, python3\n')
"'hello, python3\\n'"
```

<a name="6d180c13"></a>
##   列表(List)

list是一种有序的集合，可以随时添加和删除其中的元素。

- 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
- 列表是写在方括号[]之间、用逗号分隔开的元素列表。
- 列表索引值以0 为开始值，-1 为从末尾的开始位置。
- 列表可以使用+操作符进行拼接，使用*表示重复。

<a name="fe5f7c47"></a>
### 列表的创建

创建的时候使用方括号`[ ]`即可创建元组。

```python
classmates = ['Michael', 'Bob', 'Tracy']
```

列表支持使用+操作符进行拼接
```python
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list + tinylist)
# ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
```
列表支持使用*操作符表示重复
```python
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list * 2)
# ['abcd', 786, 2.23, 'runoob', 70.2, 'abcd', 786, 2.23, 'runoob', 70.2]
```

<a name="bdfda086"></a>
### 获取列表的长度

可以用 `len()` 函数获得list元素的个数

```python
>>> len(classmates)
3
```

<a name="7d7aba6e"></a>
### 访问指定下标的元素

通过下标访问list元素，如果下标是正数则从0开始依次向右索引递增，如果是负数则从-1开始依次向左索引递减，如果超过下标边界则报错。

```python
>>> classmates[0]
'Michael'
>>> classmates[-1]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

当索引超出了范围时，`Python`会报一个`IndexError`错误，要确保索引不要越界，记得最后一个元素的索引是`len(classmates) - 1`

<a name="e44aa234"></a>
### 列表的普通操作

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> classmates.index('Tracy')
2
>>> classmates.remove('Bob')
>>> classmates
['Michael', 'Tracy']
>>> classmates.extend([0,5,6])
>>> classmates
['Michael', 'Tracy', 0, 5, 6]
>>> classmates.count(5)
1
>>> classmates.clear()
>>> classmates
[]
```

- `insert(index, ele)` 往指定位置添加元素。
- `pop(index)` 带上index参数则删除指定位置元素，返回删除的元素。
- `index(el)` 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
- `remove(el)` 删除值为el的第一个元素。如果没有匹配的元素就会返回一个错误。
- `extend(list)` 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
- `count(el)` 返回el在列表中出现的次数。
- `clear()`	移除列表中的所有项，等于del a[:] 。

---

- `sort()`	对列表中的元素进行排序。
- `reverse()`	倒排列表中的元素。
- `copy()`	返回列表的浅复制，等于a[:]。

<a name="be13021c"></a>
### 列表的栈操作

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

- `append(ele)` 进栈操作
- `pop(index)` 出栈操作

<a name="0c6f650d"></a>
### 列表的队列操作

可以引入 collections 下的 `deque` 模块针对列表做队列操作

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

- `deque()` 将一个list转换为队列的形式
- `queue.append(ele)` 入列操作
- `queue.popleft()` 出列操作

<a name="2a592df3"></a>
### 多维列表的创建

```python
>>> s = ['python', 'java', ['asp', 'php'], 'scheme', 123, True] # 多维数组
>>> s[2][0]
'asp'
```

<a name="98be3596"></a>
### 列表排序

```python
>>> a.sort() # 排序
>>> a
['a', 'b', 'c']
```

- `sort()` 列表排序

<a name="794987a0"></a>
### del语句

使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。可以用 del 语句结合着切片从列表中删除一个元素，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

<a name="53a918da"></a>
##   元组(Tuple)

- tuple与list类似，不同之处在于tuple一旦初始化就**不能修改**。
- tuple写在小括号里，元素之间用逗号隔开。
- 元组的元素不可变，但可以包含可变对象，如list。

:::info
tuple不支持del，因为它是不可变的。
:::

<a name="220747f6"></a>
### 元组的创建

创建的时候使用圆括号`( )`即可创建元组，也可省略圆括号直接使用逗号分隔创建。

```python
>>> classmates = ('Michael', 'Bob', 'Tracy')
>>> t = (1,) # 定义只有一个元素的元组，如果不加逗号则括号被解析为数学计算意义上的括号

>>> t = 12345, 54321, 'hello!'
>>> t
(12345, 54321, 'hello!')
```

tuple没有append()，insert()这样的方法。

获取元素的方法和list是一样的，可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

:::warning
注意：定义一个只有1个元素的tuple，必须加逗号。
:::

多维元组

多维元组，如果内部包含list，则list里面的元素可更改

```python
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

之所以能改变tuple 中的 list，内存原理图如下:

未改变前的tuple:<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597041376901-05e91a69-71eb-4c21-86d6-844c222b4103.png#align=left&display=inline&height=260&originHeight=260&originWidth=350&size=0&status=done&style=none&width=350)

改变后的tuple:<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597041390358-9cd88a3e-b21b-42c7-900c-ead56e659fbe.png#align=left&display=inline&height=260&originHeight=260&originWidth=350&size=0&status=done&style=none&width=350)

<a name="c062c820"></a>
##   字典(Dict)

Python内置字典dict的支持，dict全称dictionary，在其他语言中也称为map（JS中称为对象，数据结构中称为哈希表、散列表），使用键-值（key-value）存储，具有极快的查找速度。

- 字典是无序的对象集合，使用键-值（key-value）存储，具有极快的查找速度。
- 键(key)必须使用不可变类型。
- 同一个字典中，键(key)必须是唯一的。

序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。在同一个字典之内，关键字必须是互不相同。

<a name="8cf36547"></a>
### 字典的创建

<a name="7563af8c"></a>
#### 字面量创建

```python
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
```

<a name="e177d82c"></a>
#### 构造函数创建

传入一个list，内含多个tuple

```python
dic = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```

<a name="1317457f"></a>
### 获取字典元素

获取指定key对应的value，使用中括号语法。

```python
>>> d['Michael']
95
```

也可以使用get方法获取指定的key，如果不存在默认返回 None，可以自定义返回值。

```python
>>> d.get('Thomas') # 使用get()方法，如果key不存在，返回None
>>> d.get('Thomas', -1) # 返回自己指定的value
-1
>>> d.get('Bob', -1) # 如果存在，则返回对应的value
75
```

<a name="39850649"></a>
### 对指定的字典元素重新赋值

对指定的key重新赋值，使用中括号语法。

```python
>>> d['Adam'] = 67
>>> d['Adam']
67
```

<a name="66ed6523"></a>
### 判断指定的key是否存在

使用 `in` 操作符即可判断制定的 key 是否存在。

```python
>>> 'Thomas' in d # 通过in判断key是否存在
False
```

<a name="ovBuD"></a>
### del语句

del语句也可以删除一个字典key对应的值。

```python
>>> a = {'a': 9, 'b': 0}
>>> del a['a']
>>> a
{'b': 0}
```

<a name="3acc134b"></a>
##   集合(Set)

- set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
- set是无序的，重复元素在set中自动被过滤。

:::info
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集（&）、并集（|）、差集（-）等操作。
:::

<a name="8b3406f3"></a>
### set的创建

<a name="ai2Kr"></a>
#### 字面量创建

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
```

<a name="R0W46"></a>
#### 构造函数创建

使用set()构造函数创建，传入一个list

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

如果要创建一个空集合，必须用 set() 而不是 {} ；后者创建一个空的字典。

<a name="313b7484"></a>
### set元素的增加与删除

```python
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(4)
>>> s
{1, 2, 3}
```

- `add(key)`  可以添加元素到set中，可以重复添加，但不会有效果
- `remove(key)`  可以删除元素

<a name="9cdd4a78"></a>
##   运算符  

<a name="c3ff9dcf"></a>
### 运算符分类

- 算术运算符 `+`、`-`、`*`、`/`、`%`、`**`(幂)、`//`(取整除)
- 比较运算符 `==`、`!=`、`>`、`<`、`>=`、`<=`
- 赋值运算符 `=`、`+=`、`-=`、`*=`、`/=`、`%=`、`**=`、`//=`
- 位运算符 `&`、`|`、`~`、`^`、`<<`、`>>`
- 逻辑运算符 `and`、`or`、`not`
- 成员运算符 `in`、`not in`
- 身份运算符 `is`、`is not`

<a name="be9368fe"></a>
### 成员运算符

- in : 如果在指定的序列中找到值返回 True，否则返回 False。
- not in : 如果在指定的序列中没有找到值返回 True，否则返回 False。

```python
a = 10
b = 1
list = [1, 2, 3, 4, 5 ]
print(a in list) # False
print(b in list) # True
print(a not in list) # True
print(b not in list) # False
```

<a name="bffd2d46"></a>
### 身份运算符

- is : 判断两个标识符是不是引用自一个对象
- is not : 是判断两个标识符是不是引用自不同对象

```python
a = 20
b = 20
print(a is b) # True
print(a is not b) # False
a = 10
print(a is b) # False
print(a is not b) # True
```

<a name="451c57e1"></a>
### Python运算符优先级

| 运算符 | 描述 |
| --- | --- |
| ** | 指数 (最高优先级) |
| ~ + - | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
| * / % // | 乘，除，取模和取整除 |
| + - | 加法减法 |
| >> << | 右移，左移运算符 |
| & | 位 'AND' |
| ^ &#124; | 位运算符 |
| <= < > >= | 比较运算符 |
| <> == != | 等于运算符 |
| = %= /= //= -= += *= **= | 赋值运算符 |
| is is not | 身份运算符 |
| in not in | 成员运算符 |
| not or and | 逻辑运算符 |







