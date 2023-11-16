<a name="261b8a9f"></a>
## 切片

list 和 tuple 都可以进行切片操作，操作的结果仍是list或tuple。

```python
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]) # ['Michael', 'Sarah', 'Tracy']
```

如果省略起始索引，那么默认从0开始

```python
print(L[:3]) # ['Michael', 'Sarah', 'Tracy']
```

同样的，省略结束索引，将切片到最后一个元素

```python
print(L[1:]) # ['Sarah', 'Tracy', 'Bob', 'Jack']
```

如果传入负数，则从list最后一个元素开始取

```python
print(L[-2:]) # ['Bob', 'Jack']
```

切片可以有第三个参数，表示步长，每隔多少位元素取一个

```python
print(L[:4:2]) # ['Michael', 'Tracy'] 前4位元素每隔2位取一位
print(L[::2]) # ['Michael', 'Tracy', 'Jack'] 所有元素每隔2位取一位
```

如果什么都不写，只写`[:]`就可以原样复制

```python
print(L[:])
```

字符串也可以进行切片操作

```python
'ABCDEFG'[:3] # 'ABC'
```

其实其他语言中的字符串截取操作，如`substring`就是一种切片操作

<a name="07d72669"></a>
## 生成式
<a name="b28ec500"></a>
### 列表生成式

普通生成列表的方式:

```python
list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

使用列表生成式生成列表:

```python
[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

嵌套列表解析:

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

a = [[row[i] for row in matrix] for i in range(2)]
# [[1, 5, 9], [2, 6, 10]]
```

组合多级循环生成:

```python
[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

<a name="22bacb46"></a>
### 列表生成式的应用

遍历当前目录下所有文件:

```python
[d for d in os.listdir('.')]
# ['.vscode', '01_test.py', 'learning.py', 'test.md']
```

迭代map:

```python
d = {'x': 'A', 'y': 'B', 'z': 'C' }
ret = [k + '=' + v for k, v in d.items()]
print(ret) # ['y=B', 'x=A', 'z=C']
```

列表元素转化:

```python
L = ['Hello', 'World', 'IBM', 'Apple']
ret = [s.lower() for s in L]
print(ret) # ['hello', 'world', 'ibm', 'apple']
```

<a name="8b552d80"></a>
### 集合/字典生成式

set() 集合也支持类似的操作

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
# {'r', 'd'}
```

map() 字典也支持类似的操作

```python
a = {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
```

<a name="1a34b8d9"></a>
## 生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的`[]`改成`()`，就创建了一个generator：

```python
g = (x * x for x in range(10))
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 4
print(next(g)) # 9
print(next(g)) # 16
```

generator保存的是算法，每次调用`next(g)`，就计算出`g`的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出`StopIteration`的错误。

generator也是一个可迭代对象:

```python
for n in g:
	print(n)
```


<a name="EQ1Hq"></a>
### 带yield的生成器

以斐波那契数列为例：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
```

将之转化为生成器`generator`，使用`yield`即可

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

a = fib(10)
print(a) # <generator object fib at 0x00000269D81DA7D8>
for i in a:
  print(i) # 1 1 2 3 5 8 13 21 34 55
```

但是用`for`循环调用generator时，发现拿不到generator的`return`语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中：

```python
g = fib(6)
while True:
  try:
    x = next(g)
    print('g:', x)
    except StopIteration as e:
      print('Generator return value:', e.value)
      break

# g: 1 g: 1 g: 2 g: 3 g: 5 g: 8
# Generator return value: done
```

<a name="4c718d0b"></a>
## 可迭代对象

可以直接作用于`for`循环的数据类型有以下两种:

- 一类是集合数据类型，如`list`、`tuple`、`dict`、`set`、`str`等；
- 一类是`generator`，包括生成器和带`yield`的generator function。

这些可以直接作用于`for`循环的对象统称为可迭代对象：`Iterable`。

可以使用`isinstance()`判断一个对象是否是`Iterable`对象：

```python
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

<a name="bd7709dc"></a>
### list及tuple迭代

```python
l = [1, 2, 3, 4, 5]
for item in l:
  print(item)
```

<a name="17bdb7e6"></a>
#### 带下标的迭代

使用Python内置的`enumerate`函数可以把一个list变成索引-元素对。

```python
for i, item in enumerate(['one','two','three']):
    print(i, item)
```

打印

```
0 one
1 two
2 three
```

<a name="76cb6e23"></a>
#### 多变量遍历

如果一个list或tuple包含子项list或tuple，则可以使用多变量遍历。

```python
for x, y in [(1, 1), (2, 4), (3, 9)]:
  print(x, y)
```

<a name="1df04406"></a>
#### 反向遍历

先使用 `reversed` 反转一个序列再进行遍历。

```python
for i in reversed(range(1, 10, 2)):
    print(i)
```

<a name="fdfe0651"></a>
#### 按字典顺序遍历

首先将一个list转化为set (目的是为了去重)，再进行sorted排序后遍历。

```python
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
  print(f)
```

输出

```
apple
banana
orange
pear
```

<a name="95c3bce2"></a>
### dict迭代

默认字典迭代只遍历其中的key

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)
```

如果要迭代其中的value，则:

```python
for value in d.values():
  print(value)
```

如果要同时迭代其中的key和value，则:

```python
for value in d.items():
  print(value)
```

或者

```python
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
  print(k, '=', v)
```

<a name="bdcda011"></a>
### str迭代

```python
for ch in 'ABCD':
  print(ch)
```

<a name="1ac06a1b"></a>
### zip()

同时遍历两个或更多的序列，可以使用 zip() 组合：

```python
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```

输出

```
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

<a name="fc761423"></a>
### 判断一个对象是可迭代对象

通过`collections`模块的`Iterable`类型判断

```python
from collections import Iterable
print(isinstance('abc', Iterable)) # True
print(isinstance([1,2,3], Iterable)) # True
print(isinstance(123, Iterable)) # False
```



<a name="LSJlJ"></a>
## 迭代器

生成器不但可以作用于`for`循环，还可以被`next()`函数不断调用并返回下一个值，直到最后抛出`StopIteration`错误表示无法继续返回下一个值了。

可以被`next()`函数调用并不断返回下一个值的对象称为**迭代器**：`Iterator`。

可以使用`isinstance()`判断一个对象是否是`Iterator`对象：

```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter`函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

<a name="czF0b"></a>
### 关于Iterable和Iterator的总结

- 凡是可作用于`for`循环的对象都是`Iterable`类型；
- 凡是可作用于`next()`函数的对象都是`Iterator`类型，它们表示一个惰性计算的序列；
- `generator` 是 `Iterator`，`Iterator`一定是 `Iterable` ；
- 集合数据类型如`list`、`dict`、`str`等是`Iterable`但不是`Iterator` ；
- 可以通过`iter()`函数将 `Iterable` 转换为 `Iterator` 对象。



