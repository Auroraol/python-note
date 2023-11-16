<a name="EiXGn"></a>
## 函数定义

在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

使用时直接调用即可，如 `my_abs(-1)`

<a name="04ba4779"></a>
### 从模块中导入

如果将上述文件保存为 `a.py`，在同级目录下创建一个 `b.py`，输入

```python
from a import my_abs
print(my_abs(-1))
```

运行 `b.py` 将会看到控制台打印出 1

<a name="TBkU7"></a>
## 调用函数时的异常处理

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出 `TypeError`：

```python
>>> my_abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given
```

如果参数类型不对，Python解释器就无法帮我们检查。

```python
>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_abs
TypeError: unorderable types: str() >= int()
>>> abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

<a name="INf7E"></a>
### 使程序更加强健

修改一下 `my_abs` 的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数 `isinstance()` 实现：

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：

```python
>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in my_abs
TypeError: bad operand type
```

<a name="247ab92e"></a>
## 函数返回

函数正常可以返回单一值，如之前自定义的 `my_abs()`

也可以多值返回：

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y) # (151.96152422706632, 70.0)
```

事实上，函数的多值返回的值是一个tuple，只是可以省略括号。

<a name="c15287ee"></a>
## 函数的参数
<a name="2171d1b0"></a>
### 默认参数

有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。

```python
def my_print(name, age=18, sex='male'):
    print(name, age, sex)

my_print('xiaoyu') # xiaoyu 18 male
my_print('xiaozhang', 22) # xiaozhang 22 male
my_print('xiaoqiao', sex='female') # xiaoqiao 18 female
```

默认参数必须为不可变对象，否则坑了会出现意想不到的副作用

比如:

```python
def add_end(L=[]):
    L.append('END')
    return L
```

```python
>>> add_end()
['END']
>>> add_end()
['END', 'END']
```

解决方案:

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

```python
>>> add_end()
['END']
>>> add_end()
['END']
```

<a name="708af124"></a>
### 可变参数

可以使用确定的list或tuple传值，如:

```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3]) # 14
calc((1, 3, 5, 7)) # 84
```

也可使用可变参数的形式，仅仅在可变参数前面添加一个`*`号，如:

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2, 3) # 14
```

Python允许你在list或tuple前面加一个`*`号，把list或tuple的元素变成可变参数传进去：

```python
nums = [1, 2, 3]
calc(*nums) # 14
```

<a name="6bf027b8"></a>
### 关键字参数

python支持关键字参数，实际上是一个dict对象，使用两个 `**` 表示:

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

Python允许你在list或tuple前面加两个`**`号，把dict元素变成可变参数传进去：

```python
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

使用dict类型传值写法同下，不过较繁琐:

```python
def person(name, age, kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, {'gender':'M', 'job': 'Engineer'})
```

<a name="46737bb2"></a>
### 关键字参数名检查

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过`in`检查。

```python
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数的情况 do something
        pass
    if 'job' in kw:
        # 有job参数的情况 do something
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```

<a name="68cc6ed1"></a>
### 命名关键字参数

如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数，在关键字前加一个 `*` 作为参数。

```python
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer
```

如果少传指定关键字则会报错

```python
person('Jack', 24, city='Beijing')
# TypeError: person() missing 1 required positional argument: 'job'
```

如果传入关键字之外的参数则会报错

```python
person('Jack', 24, city='Beijing', sex='famale')
# person() got an unexpected keyword argument 'sex'
```

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符`*`了:

```python
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Jack', 24, 'hello', 'my', 'friend', city='Beijing', job='Engineer')
# Jack 24 ('hello', 'my', 'friend') Beijing Engineer
```

<a name="f4530777"></a>
### 参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。**但是参数定义的顺序必须是**：
```
必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
```
举例：

```python
def f1(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd=', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) d= 99 kw = {'x': '#'}
```

<a name="80690612"></a>
## 空函数

使用 `pass` 语句可以创建一个空函数

```python
def nop():
  pass
```

`pass`语句什么都不做，可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来。

`pass`还可以用在其他语句里，比如：

```python
if age >= 18:
    pass
```

缺少了`pass`，代码运行就会有语法错误。

<a name="0edb4c85"></a>
## 闭包
<a name="e0d47466"></a>
### 以函数作为返回值

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

sum = lazy_sum(1,2,3,4,5)
print(sum) # <function lazy_sum.<locals>.sum at 0x0000029DF5E930D0>
print(sum()) # 15
```

以上代码，我们在函数`lazy_sum`中又定义了函数`sum`，并且，内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，相关参数和变量都保存在返回的函数中，这种程序结构被称为“闭包（`Closure`）”。

<a name="f1e32160"></a>
### 未立即执行的函数

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

fs = count()

print(fs[0]()) # 9
print(fs[1]()) # 9
print(fs[2]()) # 9
```

以上代码，本期待获得的值为`1 4 9`，却由于未立即执行，最后获得了`9 9 9`。

原因就在于返回的函数引用了变量`i`，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量`i`已经变成了`3`，因此最终结果为`9`。

<a name="cc0d43ed"></a>
### 使用立即执行函数实现变量暂存

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

fs = count()

print(fs[0]()) # 1
print(fs[1]()) # 4
print(fs[2]()) # 9
```


<a name="6c219743"></a>
## 递归函数

在函数内部自己调用自己的函数，就是递归函数，举例：

**求阶乘**

```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```


<a name="78162069"></a>
## 内置函数
<a name="563e4c18"></a>
### 数学函数

不在`math` 下的数学函数:

- `abs(num)` 返回num的绝对值
- `min(nums)` 返回nums的最小值
- `max(nums)` 返回nums的最大值
- `round(num)` 返回num的四舍五入值

---

- `divmod(x,y)`  返回一个元组（x//y, x%y）

如 divmod(100,10)  返回一个元组（10,0），第一个元素的100/10的商，第二个元素的100/10的余数

- `pow(x,y)`  求次方，返回 x**y 的结果
- `pow(x,y,z)` 返回 x**y%z 的结果
- `range(num)` 获取随机数或随机字符 eg. range(10) 从0到10的随机数

<a name="c875eeab"></a>
### 转换函数

<a name="f3c723ec"></a>
#### 类型转换

- `int(x [,base])` 将x转换为一个整数
- `float(x)` 将x转换到一个浮点数
- `complex(real [,imag])` 创建一个复数

---

- `str(x)` 将对象x转换为字符串
- `bool(x)` 将其他数据类型的对象转化为布尔值

---

- `list(s)` 将序列s转换为一个列表
- `tuple(s)` 将序列s转换为一个元组
- `set(s)` 将序列s转换为可变集合
- `dict(d)` 创建一个字典。d 必须是一个序列 (key,value)元组
- `frozenset(s)` 转换为不可变集合

<a name="9a37f36d"></a>
#### 进制转换

- `bin()` 将一个整数转换为一个二进制字符串
- `oct()` 将一个整数转换为一个八进制字符串
- `hex()` 将一个整数转换为一个十六进制字符串

<a name="1ae3839c"></a>
#### 其它转换

- `ascii()` 将一个字符转换为它的ascii
- `bytes()` 将一个字符转换为字节码
- `chr()` 将一个整数转换为一个字符
- `ord()` 将一个字符转换为它的整数值
- `unichr(x)` 将一个整数转换为Unicode字符

<a name="2807aea8"></a>
### 集合运算

- `all()` 所有传入参数为真，才为真
   - all([True,False])返回 False
   - all([True,True])返回 True
- `any()` 任何一个传入参数为真，就为真
   - any([True,False])返回 True
   - any([False,False])返回 False

<a name="eval"></a>
### eval

- `eval()`  执行python代码，并返回其执行结果。

如

```python
eval("1+2+3")
eval("print(123)")
```

在接收用户输入时应避免使用eval，因为别有用心的用户可能借此注入恶意代码

<a name="exec"></a>
### exec

`exec()`  执行python代码（可以是编译过的，也可以是未编译的），没有返回结果（返回None）

如

```python
exec(compile("print(123)","<string>","exec"))
exec("print(123)")
```

<a name="isinstance"></a>
### isinstance

`isinstance(object, class)` 判断对象是否是某个类的实例.

如

```python
isinstance([1,2,3],list)
```

<a name="622bbf60"></a>
### 其他内置函数

- `dir()`  接收对象作为参数，返回该对象的所有属性和方法
- `help()` 接收对象作为参数，更详细地返回该对象的所有属性和方法
- `slice(起始下标，终止下标，步长)`  对序列化类型数据切片，返回一个新的对象，步长默认为1。
- `globals()`  返回一个字典，包括所有的全局变量与它的值所组成的键值对
- `locals()`  返回一个字典，包括所有的局部变量与它的值所组成的键值对
- `compile()`  接收.py文件或字符串作为传入参数，将其编译成python字节码。
- `hash()`  对传入参数取哈希值并返回
- `id()` 返回内存地址，可用于查看两个变量是否指向相同一块内存地址
- `issubclass(subclass,class)` 查看这个类是否是另一个类的派生类，如果是返回True，否则返回False
- `memoryview()` 查看内存地址
- `repr()` 执行传入对象中的_repr_方法
- `type()` 返回对象类型
- `staticmethod()` 返回静态方法
- `super()` 返回基类
- `vars()` 返回当前模块中的所有变量
- `next()`
- `iter()`
- `object()`

<a name="be10e9dd"></a>
## 高阶函数
<a name="map"></a>
### map

`map()`传入的第一个参数是`f`，即函数对象本身。返回的结果是一个`Iterator`，`Iterator`是惰性序列，需要通过`list()`函数让它把整个序列都计算出来并返回一个list。

将所有list为数值的元素转化为字符串

```python
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

求立方

```python
l = list(map(lambda x: x**3 , [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [1, 8, 27, 64, 125, 216, 343, 512, 729]
```

格式化不规范的英文名，使之首字母大写，后面的字母小写

```python
def normalize(name):
    return name[0:1].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1)) # ['Adam', 'Lisa', 'Bart']
```

<a name="reduce"></a>
### reduce

这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算。

求和

```python
from functools import reduce
s = reduce(lambda x,y: x+y, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # 45
```

最大值

```python
from functools import reduce
def max(x, y):
    if (x > y):
        return x
    return y

s = reduce(max, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s)
```

<a name="fliter"></a>
### fliter

过滤器，筛选出满足条件(返回值为True)的序列。

过滤奇数

```python
l = list(filter(lambda x: x%2==1, [1, 2, 4, 5, 6, 9, 10, 15]))
# [1, 5, 9, 15]
```

取出空字符

```python
def not_empty(s):
    return s and s.strip()

l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# ['A', 'B', 'C']
```

求素数

```python
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

<a name="sorted"></a>
### sorted

字典排序

```python
sorted([36, 5, -12, 9, -21]) # [-21, -12, 5, 9, 36]
sorted(['bob', 'about', 'Zoo', 'Credit']) # ['Credit', 'Zoo', 'about', 'bob']
```

sorted可以携带第二参数，用于对list进行处理后输出排序

```python
sorted([36, 5, -12, 9, -21], key=abs) # [5, 9, -12, -21, 36]
```

忽略英文大小写进行排序

```python
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower) # ['about', 'bob', 'Credit', 'Zoo']
```

可以传入第三个参数`reverse=True`进行反转排序

```python
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']
```

<a name="e97bc1e5"></a>
## 装饰器

本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
# call now():
# 2015-3-25
```

上面的`log`，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处即可。

调用`now()`函数，不仅会运行`now()`函数本身，还会在运行`now()`函数前打印一行日志。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。比如，要自定义log的文本：

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('print')
def now():
    print('2015-3-25')

now()
# print now():
# 2015-3-25
```

<a name="2f25bf1f"></a>
### 使用functools.wraps

普通装饰器:

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

带参数的装饰器:

```python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

<a name="5745487b"></a>
## 偏函数

比如使用int将字符串转化为数值类型，可以增加第二参数，代表转化为n进制数

```python
int('12345', base=8) # 5349
```

将之封装为一个将字符串转化为n进制的函数，方法如下:

```python
def int2(x, base=2):
    return int(x, base)

int2('1000000') # 64
```

可以使用偏函数进一步简化:

```python
import functools
int2 = functools.partial(int, base=2)

int2('1000000') # 64
```

所以，`functools.partial`的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

<a name="5d28833a"></a>
## Lambda表达式

即匿名函数，在需要传入一个函数的地方可以直接使用Lambda表达式，更方便简洁。

`lambda x: x * x`相当于:

```python
def f(x):
    return x * x
```

在map中进行迭代:

```python
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

在filter中进行过滤:

```python
def is_odd(n):
    return n % 2 == 1

list(filter(lambda n: n%2==1, range(1,20)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

闭包:

```python
def build(x, y):
    return lambda: x * x + y * y

print(build(1,2)())
```


<a name="35808e79"></a>
## 参考资料

- [python3内置函数详解](http://www.cnblogs.com/huamingao/p/5887887.html)

