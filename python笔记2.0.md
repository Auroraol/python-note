# 基础

## 注释

**单行注释**

```python
# 我是一个注释
print('Hello world')
```

**多行注释**

```python
"""
在三引号中的注释被称之为多行注释
可以写很多行的功能说明
"""
```

## 变量

命名规则

+ 大驼峰：ClassName
+ 小驼峰：myNameValue 
+ 蛇形：name_value (python代码里个人推荐)

```python
name = 'wuhaopeng' 
wechat = 'weicreates' 
print(name)  # wuhaopeng
print(wechat)  # weicreates
```

## **运算符**

**算数运算符**

![image-20231107224946346](python笔记.assets/image-20231107224946346.png)

**赋值运算符**

![image-20231107225012918](python笔记.assets/image-20231107225012918.png)

**比较运算符**

![](python笔记.assets/image-20231107225040431.png)

**逻辑运算符**

![image-20231107225234629](python笔记.assets/image-20231107225234629.png)

**成员运算符**

**in**

+ 某值或元素是否在指定字符串、序列中

```python
String = '123456'
print('123' in String)  # True
```

**not in**

+ 某值或元素是否不在指定字符串、序列中

```python
String = '123456'
print('321' not in String)  # True
```

**身份运算符**

 **is**

+ 判断两个标识符是不是引用自一个对象
+ 相当于 id(x) == id(y)

```python
a = 1
b = 1
print(a is b)  # True
```

**is not**

+ 判断两个标识符是不是引用自不同对象

```python
a = 1
b = 2
print(a is not b)  # True
```

##  if、elif、else 条件判断

```python
name = '阿'
wechat = 'weieates'
if name == '阿':
    if wechat == 'weieates':
        print('wechat True')  # wechat True
    else:
        print('wechat False')
    print('name True')  # name True
else:
    print('name False')
```

## **for循环、while循环**

### for循环

#### **range 范围限制**

+ range(开始值, 结束值, 步长)
+ step可不写，默认值为1

```python
for y in range(1, 10):
    for x in range(1, y + 1):
        z = x * y
        print(str(x) + '*' + str(y) + '=' + str(z), end=' ')
    print()
```

#### 遍历字符串

```python
String = 'Hello world'
for i in String:
	print(i)  # H e l l o  w o r l d
```

#### 遍历列表

```python
# name_list = ["zhangsan", "lisi", "wangwu"]
# for 循环内部使用的变量 in 列表
for name in name_list:
    循环内部针对列表元素进行操作
    print(name)

# for 循环内部使用的变量 in 列表
for name not in name_list:
   循环内部针对列表元素进行操作
	print(name)
    
```

####  遍历字典

```python
Dict = {1: 1, 2: 2, 3: 3}
for i in Dict:
	print(Dict[i])  # 1 2 3
```

#### **遍历字典的键值**

```python
Dict = {1: 'first', 2: 'second', 3: 'third'}
for k, v in Dict.items():
	print(k, v)
# 1 first
# 2 second
# 3 third
```

### **while 循环**

####  **无限循环**

```python
while True:
	print('Hello world')
```

#### **while 判断语句**

```python
n = 0
while n < 10:
	n = n + 1
	print(n)  # 1 2 3 4 5 6 7 8 9 10
```

### **break 语句**

退出循环

```python
for i in range(5):
	print(i)
	if i == 3:
		break
# 0 1 2 3
```

### **continue 语句**

跳过本次循环

```python
n = 0
while n < 15:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)  # 1 3 5 7 9 11 13 15
```

### **pass 语句**

不执行任何操作

```python
for i in range(5):
    if i == 4:
        print(i)
    else:
        pass
# 4
```

### **else 语句**

循环判断条件为False后执行(没啥用)

break 影响else语句的执行，continue 不影响else语句的执行

```python
n = 0
while n < 10:
	n += 1
	print(n)
else:
	print('n>=10')

# 1 2 3 4 5 6 7 8 9 10 n>=10

for i in range(5):
	number = int(input('输入数字0：'))
	if number == 0:
		print('输入了0')
		break
else:
	print('错误5次！')
```

# 输入输出

## **格式化输出**:crossed_swords:

![](python笔记.assets/image-20231107224532869.png)

**格式字符的使用**

```python
String = 'world'
print('字符串：hello %s' % String)  # 字符串：hello world
print('字符串前三位：hello %.3s' % String)  # 字符串前三位：hello wor
print('字符串三到五位：hello %3.5s' % String)  # 字符串三到五位：hello world

Int = 1
print('整数：%d' % Int)  # 整数：1

Float = 0.0123
print('浮点数：%f' % Float)  # 浮点数：0.012300
print('浮点数前两位小数：%.2f' % Float)  # 浮点数前两位小数：0.01
print('浮点数前二到四位小数：%2.4f' % Float)  # 浮点数前二到四位小数：0.0123

print(f'{String},{Int},{Float}')  # world,1,0.0123
print('{0},{1},{2}'.format(String, Int, Float))  # world,1,0.0123
```

<font color=red>注意:  推荐使用f'{}'</font>

## **print 函数**

```python
print("格式化字符串 %s %s" % (变量1, 变量2...))
print("格式化字符串 %s %s " % (变量1, 变量2...),  end="")   #不换行输出
print("{}\r\n".format("电影名, 详情页, 豆瓣评分, 封面图片"))
print(f'格式化字符串{变量1} {变量2}!')  #推荐!!!!
```

print("格式化字符串 %s %s" % (变量1, 变量2...))需要用到以下格式化字符

| 格式化字符 | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| %s         | 字符串                                                       |
| %d         | 有符号十进制整数，`%06d` 表示输出的整数显示位数，不足的地方使用 `0` 补全 |
| %f         | 浮点数，`%.2f` 表示小数点后只显示两位                        |
| %%         | 输出 `%`                                                     |

 补充:

**pprint 模块**

pprint(object)  数据结构较为复杂的可以使用pprint优化输出

```python
from pprint import pprint
pprint("""Hello
world""") 
# 'hello \nworld'
```

## Input 函数

默认返回字符串类型, 可在外部转换为其它数据类型

```python 
name = input('请输入姓名：')            #
age = int(input('请输入年龄：'))        #
money = float(input('请输入财富：'))    #

print('你的姓名是：%s' % name)
print('你的年龄是：%d' % age)
print('你的财富是：%f' % money)
```

# 数据类型

| 类型      | 例子                     |
| --------- | ------------------------ |
| 整数      | `-100`                   |
| 浮点数    | `3.1416`                 |
| 字符串    | `'hello'`                |
| 列表      | `[1, 1.2, 'hello']`      |
| 字典      | `{'dogs': 5, 'pigs': 3}` |
| Numpy数组 | `array([1, 2, 3])`       |

| 类型       | 例子                      |
| ---------- | ------------------------- |
| 长整型     | `1000000000000L`          |
| 布尔型     | `True, False`             |
| 元组       | `('ring', 1000)`          |
| 集合       | `{1, 2, 3}`               |
| Pandas类型 | `DataFrame, Series`       |
| 自定义     | `Object Oriented Classes` |

## 字符串操作

> ''和""都能表示字符串但是python中推荐使用''

### 字符串拼接

**使用运算符：`+`**  不用

```
Copy codestr1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

**通过F-strings拼接**

==F-strings效率最高==

```python
s1 = 'Hello'
s2 = 'World'
print(f'{s1} {s2}!')

#运行结果
'Hello World!'
```

在F-strings中我们也可以执行函数：

```python
def power(x):
    return x*x
 
x = 5
print(f'{x} * {x} = {power(x)}')
 
#运行结果
'5 * 5 = 25'
```

**通过str.join()方法拼接**

==高效列表==

```python
list1 = ["1","2","3"]
str1 = "".join(list1)
 # 注意：使用join的时候,列表里面的每一项都必须是str类型
# 否则会出错
# 比如:
list2  = ["1",2]
str2 = "".join(list2)

#例子:              
str_list = ["Hello", "World"]
result = " ".join(str_list)
print(result)  # Output: Hello World
```

 使用略微复杂，但对于多个字符串进行拼接时，效率很高，只会有一次内存的申请。所以很擅长对列表的处理。

### **字符串的切片**

一种能够从数据中取出一部分数据的操作

+ 字符串[开始索引:结束索引:步长]
+ 左闭右开
+ <img src="python%E7%AC%94%E8%AE%B0.assets/image-20231108134253043.png" alt="image-20231108134253043" style="zoom: 67%;" />

```python
num_str = "0123456789"

# 1. 截取从 2 ~ 5 位置 的字符串
print(num_str[2:6])

# 2. 截取从 2 ~ `末尾` 的字符串
print(num_str[2:])

# 3. 截取从 `开始` ~ 5 位置 的字符串
print(num_str[:6])

# 4. 截取完整的字符串
print(num_str[:])

# 5. 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 6. 从索引 1 开始，每隔一个取一个
print(num_str[1::2])

# 倒序切片
# -1 表示倒数第一个字符
print(num_str[-1])

# 7. 截取从 2 ~ `末尾 - 1` 的字符串
print(num_str[2:-1])

# 8. 截取字符串末尾两个字符
print(num_str[-2:])

# 9. 字符串的逆序（面试题）
print(num_str[::-1])
```

### 常用方法

#### 1) 判断类型

| 方法               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| string.isspace()   | 如果 string 中只包含空格，则返回 True                        |
| string.isalnum()   | 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True |
| string.isalpha()   | 如果 string 至少有一个字符并且所有字符都是字母则返回 True    |
| string.isdecimal() | 如果 string 只包含数字则返回 True，`全角数字`                |
| string.isdigit()   | 如果 string 只包含数字则返回 True，`全角数字`、`⑴`、`\u00b2` |
| string.isnumeric() | 如果 string 只包含数字则返回 True，`全角数字`，`汉字数字`    |
| string.istitle()   | 如果 string 是标题化的 (每个单词的首字母大写) 则返回 True    |
| string.islower()   | 如果 string 中包含至少一个区分大小写的字符，并且所有这些 (区分大小写的) 字符都是小写，则返回 True |
| string.isupper()   | 如果 string 中包含至少一个区分大小写的字符，并且所有这些 (区分大小写的) 字符都是大写，则返回 True |

#### 2) 查找和替换

| 方法                                                    | 说明                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| string.startswith(str)                                  | 检查字符串是否是以 str 开头，是则返回 True                   |
| string.endswith(str)                                    | 检查字符串是否是以 str 结束，是则返回 True                   |
| string.find(str, start=0, end=len(string))              | 检测 str 是否包含在 string 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 `-1` |
| string.rfind(str, start=0, end=len(string))             | 类似于 find ()，不过是从右边开始查找,不过如果 str 不在 string 会返回-1 |
| string.index(str, start=0, end=len(string))             | 跟 find () 方法类似，不过如果 str 不在 string 会报错         |
| string.rindex(str, start=0, end=len(string))            | 类似于 index ()，不过是从右边开始                            |
| string.replace(old_str, new_str, num=string.count(old)) | 把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次,返回一个新的字符串 |

#### 3) 大小写转换

| 方法                | 说明                             |
| ------------------- | -------------------------------- |
| string.capitalize() | 把字符串的第一个字符大写         |
| string.title()      | 把字符串的每个单词首字母大写     |
| string.lower()      | 转换 string 中所有大写字符为小写 |
| string.upper()      | 转换 string 中的小写字母为大写   |
| string.swapcase()   | 翻转 string 中的大小写           |

#### 4) 文本对齐

| 方法                 | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| string.ljust(width)  | 返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串 |
| string.rjust(width)  | 返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串 |
| string.center(width) | 返回一个原字符串居中，并使用空格填充至长度 width 的新字符串  |

#### 5) 去除空白字符

| 方法            | 说明                               |
| --------------- | ---------------------------------- |
| string.lstrip() | 截掉 string 左边（开始）的空白字符 |
| string.rstrip() | 截掉 string 右边（末尾）的空白字符 |
| string.strip()  | 截掉 string 左右两边的空白字符     |

#### 6) 拆分和连接

| 方法                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| string.partition(str)     | 把字符串 string 分成一个 3 元素的元组 (str 前面，str, str 后面) |
| string.rpartition(str)    | 类似于 partition () 方法，不过是从右边开始查找               |
| string.split(str="", num) | 以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 'r', 't', 'n' 和空格, 返回列表 |
| string.splitlines()       | 分隔 ['r', 'n', 'rn'] ，构造出一个新的字符串                 |
| string.join(seq)          | 以 string 作为分隔符，将 seq 中所有的元素（的字符串表示）合并为一个新的字符串 |

split 方法

+ str.split(sep,maxsplit)

+ 以sep为分隔符切片为列表，如果maxsplit有指定值，则仅分割 maxsplit 个字符串

+ ```python
  Str = '1,2,3,4,5,6,7,8,9'
  List = Str.split(',', 7)
  print(List)  # ['1', '2', '3', '4', '5', '6', '7', '8,9']
  ```

 splitlines 方法

+ str.splitlines()

+ 按照行分隔，返回一个包括各行作为元素的列表

+ ```python
  Str = '''123
  456
  789
  '''
  List = Str.splitlines()
  print(List)  # ['123', '456', '789']
  ```

 join 方法

+ sep.join(sequence)

+ 分隔 ['r', 'n', 'rn'] ，构造出一个新的字符串

+ ```python
  List = ['甲', '乙', '丙', '丁', 'World']
  Str = ' '.join(List)
  print(Str)  # 甲 乙 丙 丁 World
  ```

## 列表

> 使用 **最频繁** 的数据类型，在其他语言中通常叫做 **数组**

### **列表的使用**

+ list = [val,val...]

```python
List = [1, '2', {3: 2}, 4]
print(List)  # [1, '2', {3: 2}, 4]
```

### 列表的切片

一种能够从数据中取出一部分数据的操作

+ 列表[开始索引:结束索引:步长]
+ 左闭右开

```python 
List = [1, 2, 3, 4, 5]

#取全部元素
print(List[:]) # [1, 2, 3, 4, 5]

#取第二个元素
print(List[1]) # 2

#取第二元素到最后一个
print(List[1:]) # [2, 3, 4, 5]

#取到最后第二个元素
print(List[:-1]) # [1, 2, 3, 4]

#反向取全部元素
print(List[::-1]) # [5, 4, 3, 2, 1]
```

### 常用方法

**增加**

| 方法                     | 说明                      |
| ------------------------ | ------------------------- |
| 列表.insert (索引，数据) | 在指定位置插入数据        |
| 列表.append (数据)       | 在末尾追加数据            |
| 列表.extend (列表 2)     | 将列表 2 的数据追加到列表 |

  **删除**

| 方法               | 说明                     |
| ------------------ | ------------------------ |
| 列表.remove [数据] | 删除第一个出现的指定数据 |
| 列表.pop           | 删除末尾数据             |
| 列表.pop (索引)    | 删除指定索引数据         |
| del 列表 [索引]    | 删除指定索引的数据       |
| 列表.clear         | 清空列表                 |

del 方法(不推荐)

+ 删除列表除最后一个元素

+ ```python
  List = [1, 2, 3, 4]
  del List[:-1]  # i < len -1 ---> 0,1,2,3
  print(List)  # [4]
  ```

**修改**

| 方法               | 说明               |
| ------------------ | ------------------ |
| 列表 [索引] = 数据 | 修改指定索引的数据 |

**统计**

| 方法               | 说明                     |
| ------------------ | ------------------------ |
| 列表. index(value) | 获取元素在列表中的索引值 |
| 列表.count (数据)  | 数据在列表中出现的次数   |

**排序**

| 方法                     | 说明     |
| ------------------------ | -------- |
| 列表.sort (reverse=True) | 降序排序 |
| 列表.reverse ()          | 反转     |

sort 方法

+ 二维列表

+ ```python
  # 根据整数排序
  List = [2, 1, 3, 5, 4]
  List.sort(key=int, reverse=False)
  print(List)  # [1, 2, 3, 4, 5]
  
  #根据二维列表的内列表索引排序
  List = [
      [1,2],
      [3,1],
      [2,3],
      [4,2]
  ]
  List.sort(key=lambda x:x[0], reverse=False)
  print(List)  # [[1, 2], [2, 3], [3, 1], [4, 2]]
  
  #根据二维列表嵌套字典的指定键排序
  List = [
      {"index":1,"value":2},
      {"index":3,"value":1},
      {"index":2,"value":3},
      {"index":4,"value":2}
  ]
  List.sort(key=lambda x:x["index"], reverse=False)
  print(List)
  
  # [
  # {'index': 1, 'value': 2},
  # {'index': 2, 'value': 3}, 
  # {'index': 3, 'value': 1}, 
  # {'index': 4, 'value': 2}
  # ]
  ```

## 元组

> 元组是储存不能被修改的多个数据的一种方式

### 元组的使用

+ tuple = (val,val...)
+ 当元组的元素只有一个时，需加逗号

```python
tuple = ("zhangsan", 18, 1.75) #
tuple = ()  # 创建空元组
tuple = (50, ) #只包含一个元素添加逗号
```

### 元组的切片

一种能够从数据中取出一部分数据的操作

+ 列表[开始索引:结束索引:步长]
+ 左闭右开

```python
tuple = (1, 2, 3, 4, 5)
#取全部元素
print(tuple[:]) # (1, 2, 3, 4, 5)

#取第二个元素
print (tuple[1]) # 2

#取第二元素到最后一个
print(tuple[1:]) # (2, 3, 4, 5)

#取到最后第二个元素
print(tuple[:-1]) # (1, 2, 3, 4)

#反向取全部元素
print(tuple[::-1]) # (5, 4, 3, 2, 1)

#每隔一个元素取
print(tuple[::2]) # (1, 3, 5)
```

### count 方法

+ tuple.count(value)
+ 查询元素在元组中的个数

```python
Tuple = (1, 1, 2, 3, 4, 5)
count = Tuple.count(1)
print(count)  # 2
```

### index方法

+ tuple.index(value)

+ 获取元素在元组中的索引值

```python
Tuple = (1, '2', 3, 4)
index = Tuple.index('2')
print(index)  # 1
```

##  字典

> 字典是储存能被修改的多个数据的一种方式

### **字典的使用**

dict={key:val,key:val...}

+ 字典只要储存一个数据，就必须要有键值对

```python
Dict = {1: 1, 2: 2, 3: '3', '4': 4}
print(Dict)   # {1: 1, 2: 2, 3: '3', '4': 4}
```

### **数据获取**

#### 获取字典的值

##### **键名获取**

+ 通过键名获取字典中key对应的值

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
value = Dict[1]
print(value) # 1
```

##### get方法

+ dict.get(key,default)

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
value = Dict.get(5, 4)
print(value) # 4
```

#### keys 方法

+ dict.keys() 通过keys方法获取字典的键名，返回可迭代对象

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
keys = Dict.keys()
for key in keys:
print(key) # 1 2 3 4
```

#### values 方法

+ dict.values() 通过keys方法获取字典的所有值，返回可迭代对象

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
values = Dict.values()
for value in values:
print(value) # 1 2 3 4
```

#### items 方法

+ dict.items() 通过keys方法获取字典的键值对,返回元组型的可迭代对象

```python
Ddict = {1: 1, 2: 2, 3: 3, 4: 4}
items = Dict.items()
for key,value in items:
    print(key,value)

# 1 1
# 2 2
# 3 3
# 4 4
```

###  数据增加

#### 键名添加

+ dict[key]=value 通过键名向字典添加数据

```python
Dict = {1: 1, 2: '2'}
print(Dict)  # {1: 1, 2: '2'}
Dict[3] = '3'
Dict['4'] = 4
print(Dict)  # {1: 1, 2: '2', 3: '3', '4': 4}
```

####  **setdefault 方法**

+ dict.setdefault(key,default)如果key键名不存在，则向字典添加键并设置默认值default

```python
Dict = {1: 1, 2: '2'}
print(Dict)  # {1: 1, 2: '2'}
Dict.setdefault('3',3)
print(Dict)  # {1: 1, 2: '2', '3': 3}
```

#### update 方法

+ dict.update(dict) 通过update方法将另一个字典添加到字典中

```python
Dict = {1: 1, 2: 2}
Dict.update({3: 3, 4: 4})
print(Dict)  # {1: 1, 2: 2, 3: 3, 4: 4}
```

###  数据删除

#### del 方法

+ del dict[key] 通过del方法删除字典对应的键值对

```python
Dict = {1: 1, 2: '2'}
print(Dict)  # {1: 1, 2: '2'}
del Dict[2]
print(Dict)  # {1: 1}
```

```python
Dict = {1: 1, 2: '2'}
print(Dict)  # {1: 1, 2: '2'}
del Dict
print(Dict)  # 报错
```

#### popitem 方法

+ dict.popitem() 删除并取出最后一个键值对，返回元组类型

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
item = Dict.popitem()
print(item)  # (4, 4)
```

#### clear 方法

+ dict.clear() 通过clear方法清空字典所有的键值对

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
Dict.clear()
print(Dict)  # {}
```

###  copy 方法

+ dict.copy() 浅拷贝字典

```python
Dict = {1: 1, 2: 2, 3: 3, 4: 4}
newDict = Dict.copy()
print(newDict)  # {1: 1, 2: 2, 3: 3, 4: 4}
```







## 集合

### **集合的使用**

+ set = {val,val...}
+ 集合是一种能够储存多个数据的方式
+ 集合的特性：数据不能重复，集合是无序的
+ 通过set()方法创建空集

```python
Set = {1, 2, 3, 4, 5}
print(Set)  # {1,2,3,4,5}

Set = set()  
print(Set)  # {}
```

### 数据获取

交集

+ set.intersection(set)
+ set & set
+ 获取两个集合中共有的元素

```
Set = {1, 2, 3, 4, 5}
Set2 = {1, 2, 4}
print(Set.intersection(Set2))
print(Set & Set2)
```

并集

+ set.union(set)
+ set | set
+ 获取两个集合中所有的元素

```
Set = {1, 2, 3, 4, 5}
Set2 = {1, 2, 4}
print(Set.union(Set))
print(Set | Set2)
```

差集

+ set.difference(set)
+ set1 - set2
+ 获取源集合有而目标集合没有的元素

```
Set1 = {1, 2, 3, 4, 5}
Set2 = {1, 2, 4}
print(Set.difference(Set2))
print(Set - Set2)
```

亦或集

+ 用法：set ^ set
+ 获取两个集合中非共有的元素

```
Set = {1, 2, 3}
Set2 = {1, 2, 3, 4, 5}
print(Set ^ Set2)
```

###  数据判断

判断子集

+ 用法：set.issubset(set)

+ 源集合是否为目标集合的子集

```
Set = {1, 2, 3}
Set2 = {1, 2, 3, 4, 5}
print(Set.issubset(Set2))
```

 判断超集

+ 用法：set.issuperset(set)
+ 源集合是否为目标集合的超集

```
Set = {1, 2, 3}
Set2 = {1, 2, 3, 4, 5}
print(Set2.issuperset(Set))
```

### **数据增加**

####  add 方法

+ set.add(value)
+ 通过add方法可以向集合添加元素

```
Set = {1, 2, 3, 4, 5}
Set.add(6)
print(Set)  # {1,2,3,4,5}
```

#### update 方法

+ set.update(set)
+ 通过update方法可以将另一个集合合并到该集合

```
set = {1, 2, 3, 4, 5}
set.update({6, 7, 8})
print(Set)  # {1,2,3,4,5,6,7,8}
```

### 数据删除

#### remove 方法

+ set.remove(value)
+ 通过元素的值进行删除

```
Set = {1, 2, 3, 4, 5}
Set.remove(1)
print(Set)  # {1,2,3,4}
```

#### pop 方法

+ set.pop()
+ 删除并取出最后一个元素

```
Set = {1, 2, 3, 4, 5}
value =Set.pop()
print(value)  # 5
```

## 转换:crossed_swords:

### 字符串和数字之间的转换

```python
# 字符串转换为数字
num_str = "1234"
num = int(num_str)  #!!!
print("Converted number:", num)
print("Type of converted number:", type(num))

# 数字转换为字符串
num = 5678
num_str = str(num)  #!!!
print("Converted string:", num_str)
print("Type of converted string:", type(num_str))
```

```
Converted number: 1234
Type of converted number: <class 'int'>
Converted string: 5678
Type of converted string: <class 'str'>
```

注意:  

```python
num = 000000
num_str = str(num)
print(num_str)
print("Type of converted string:", type(num_str))
```

```python
0
Type of converted string: <class 'str'>
```

### 元组和列表之间的转换

- 使用 `list` 函数可以把元组转换成列表

```python
list(元组) 
```

- 使用 `tuple` 函数可以把列表转换成元组

```python
tuple(列表)
```

### 字典和列表之间的转换

 **list 方法**

+ list(dict)
+ 通过list方法将字典的键名转换为列表

```python
Dict = {1: 1, 2: 2, 3: 3}
List = list(Dict)
print(List) # [1, 2, 3]
```

**sorted 方法**

+ sorted(dict)
+ 通过sorted方法将字典的键名转换为有序列表

```python
Dict = {1: 1, 3: 3, 2: 2}
List = sorted(Dict)
print(List) # [1, 2, 3]
```

### 其它类型转换成集合

+ set(object) 通过set()方法将其它类型转换成集合类型

```python
{'2', '3', '1', '4'} {1, 2} {1, 2}Str = '1234'
List = [1, 2]
Dict = {1: 11, 2: 22}
Set1 = set(Str)
Set2 = set(List)
Set3 = set(Dict)
print(Set1,Set2, Set3)
#{'2', '3', '1', '4'} {1, 2} {1, 2}
```

# **推导式、拆包:crossed_swords:**

## 推导式

> 推导式就是一种能够快速生产数据的方式

**列表推导式**

```python
List = [i for i in range(10) if i % 2 == 0]
print(List)  # [0, 2, 4, 6, 8]
```

**嵌套列表推导式**

```python
List = [[i, y] for i in range(3) for y in range(3, 6)]
print(List)
# [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
```

 **字典推导式**

```python
List = [0, 1, 2, 3, 4, 5]
Dict = {key: str(key) for key in List}
print(Dict)  # {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'} 
```

**生成器推导式**

```python
generator = (i for i in range(10) if i % 2 == 0)
for item in generator:
    print(item)  # 0 2 4 6 8
```

## 拆包

> 拆包是一种快速提取数据的方式

**元组拆包**

```python
x, y, z = (1, 2, 3)
print(x, y, z)
```

**列表拆包**

```python
List = [3, 2, 1]
a, b, c = List
print(a, b, c)
```

**集合拆包**

```python
Set = {2, 3}
a, b = Set
print(a, b)
```

**字典拆包**

字典拆包获取的是字典的键名

```python
Dict = {'1': 1, '2': 2, '3': 3}
k1, k2, k3 = Dict
```

交换两个变量的值

```python
a= 1
b=2
print(a, b)
a, b = b, a
print(a, b)
```

# **函数**

> **定义、参数、返回值、拆包、作用域、引用**

##  定义函数

使用def关键字定义函数

```python
def test():
	print('Hello world')
```

## 函数的调用

```python
def test():
	print('Hello world')

test()  # Hello world
```

## **函数参数**

+ 形参：定义函数时()中定义的变量
+ 实参：调用函数时()中传递的数据

### 不可变类型和可变类型:crossed_swords:

- **不可变类型**，内存中的数据不允许被修改： **——— 按"值"传递**

  - 数字类型 `int`, `bool`, `float`, `complex`, `long(2.x)`
  - 字符串 `str`
  - 元组 `tuple`

- **可变类型**，内存中的数据可以被修改：   **——— 按引用传递**

  - 列表 `list`

  - 字典 `dict`

  - ```python
    def saveResult(res, result):
        # 识 成功
        if res["code"] == 100:
            index = 1
            for line in res["data"]:
                result.append(f"{index}-置信度：{round(line['score'], 2)}，文本：{line['text']}\n")
                index += 1
        elif res["code"] == 200:
            print("图片中未识别出文字。")
    
    result = []  # 用于保存结果的列表
    saveResult(res, result)
    
    final_result = "".join(result)  # 将列表转换为字符串
    print(final_result)
    ```

### **传递实参**

```python
def add(num1, num2):
    print(num1 + num2)

add(1, 2)  # 3
```

### 缺省参数(默认值)

+ 当调用函数时，有些参数不必传递，而是用默认值，则用缺省参数
+ 调用函数时缺省参数可以传递新值
+ 缺省参数必须在形参后面定义，否则会报错

```python
def info(name, age = 20):
    print(name,age)

info('小')  # 小 20
info('小', 21)  # 小 21
```

### 命名参数

+ 命名参数能够在调用函数的时候，不受位置的影响

```python
def test(num1, num2):
    print(num1, num2)

test(num2=21, num1=11)  # 11 21
```

###  不定长参数

+ *args：表示调用函数时多余的未命名参数以元组的方式存储到args中
+ **kwargs：表示调用函数时多余的命名参数以键值对的方式存储到kwargs中

#### **可变参数**

```python
def text(person, *others):
	print('person:' + person)
	for other in others:
		print('other:' + other)

text('甲', '乙', '丙', '丁')

# person:甲
# other:乙
# other:丙
# other:丁
```

#### **关键字可变参数**

```python
def test(person, **others):
	print('person:' + person)
	for other in others:
		print(other + ':' + others[other])

test('甲', others1='乙', others2='丙', others3='丁')

# person:甲
#others1:乙
#others2:丙
#others3:丁
```

## 函数返回值

### 返回单个值

```python
def age(value):
	print(f'你是{value}岁！')
	if value < 12:
		return '儿童'
	elif value < 25:
		return '成人'
	else:
		return '步入社会'

print(age(21))

# 儿童
# 成人
```

### 返回多个值

+ return关键字以==元组类型==返回多个值

```python
def test(a,b,c):
    return a,b,c

test(1,2,3)  # (1 2 3)
```

可以用返回值拆包的方式接受返回的多个值

## **函数拆包**

### 返回值拆包

+ 通过函数返回值拆包，可以快速的将具体的数据用变量进行存储，这样对数据的处理会更加方便

```python
def test():
    return 1, 2, 3

a, b, c = test()
print(a, b, c)  # 1 2 3
```

### 参数拆包

#### 元组拆包

通过*tuple对元组拆包，返回等长的参数

+ 元组的元素个数和函数参数一一对应

```python
def test(a, b, c):
	print(a, b, c)

Tuple = (1, 2, 3)
test(*Tuple)  # 1 2 3


#
def test(*args):
	print(args)

Tuple = (1, 2, 3)
test(*Tuple)  # (1, 2, 3)
```

#### 字典拆包

通过**dict对字典拆包，返回key=value形式的参数

+ 字典的key和函数参数一一对应

```python
def test1(a,b,c):
    print(f"传递a是 {a},  传递b是 {b}, 传递c是 {c}")
    
Dict = {'a': 'first', 'b': 'second', 'c': 'third'}
test1(**Dict)
#传递a是 first,  传递b是 second, 传递c是 third


#
def test(**kwargs):
	print(kwargs)

Dict = {'a': 'first', 'b': 'second', 'c': 'third'}
test(**Dict)  # {'a': 'first', 'b': 'second', 'c': 'third'}
```

## **作用域**

+ 局部变量：函数中定义的变量，包括形参变量也是局部变量，只能在定义它的函数中使用

+ 全局变量：在当前文件都生效的变量

### global 关键字

+ 可在函数内部修改全局变量(默认是不能修改的,这个和c++不一样)

```python
content = 123
print(content)  # 123

def test():
	global content #
	content = 321
	print(content)  # 321

test()
print(content)  # 321
```

### nonlocal 关键字

+ 可在内部函数中修改外部函数的变量

```python
def test():
	a = 10
	print(a)  # 10
	def func():
      nonlocal a
      a = 20
      print(a)  # 20

  func()
  print(a)  # 20
  
test()
```

###  locals 关键字

+ 返回当前作用域的命名空间，返回字典类型

```
def test():
	a = 1
	namespace = locals()
	print(namespace)  # {'a': 1}

test()
```

## **引用**

+ 引用就是地址，地址是存放数据的空间在内存中的编号
+ Python中的变量并不是真正存储数据，而是存储的数据所在内存中的地址，称为引用。

引用

```python
a = 100
b = a
print(id(a))  # 2008501062992
print(id(b))  # 2008501062992
print(a is b)  # True
```

**引用当做实参**

```python
def test(n):
	print(n)
num = 100
test(num) # 100 引用num当做实参
```

**引用函数名**

```python
def test1(n):
    print(n)

test2 = test1  # 将test1函数引用给test2
```

 **函数做容器类元素**

+ 函数可以当做容器类元素被存储与传递

```python
def test1():
	print(1)

def test2():
	print(2)

List = [test1, test2]
for test in List:
	test()  # 1 2
```

## **高阶函数(类似函数指针)**

+ 将另一个函数作为参数传递给函数

```python
def test(f, num):
	return f() + num

def test2():
	return 100

print(test(test2, 100))  # 200
```

## 匿名函数

+ 没有名字的函数，用lambda定义
+ 可以用一行代码完成简单的函数定义
+ 可以当做实参快速传递到函数中去

### **lambda**





### **sort + lambda**



## **递归函数**





## **迭代器:crossed_swords:**





## **生成器**:crossed_swords:





## **装饰器**:crossed_swords:













## 补充说明

### 函数注释 —文档字符串

+ help(object)  用于简要解释函数的作用

```python
def test():
"""这是一个函数"""

help(test)    #

# Help on function test in module main

# test()
#	这是一个函数
```

### pass 关键字

+ pass关键字占用位置

```python
def test()
	pass
```

### **内置函数**

#### **数学运算**

complex
●创建复数：a+bj



abs

●获取一个整数的绝对值



 round
●round(n,m)
●四舍五入，如果有指定m则返回m为小数，否则返回整数



math.floor
●对一个浮点数向下取整



math.ceil
●对一个浮点数向上取整



divmod
●divmod(x,y)
●x除以y，以元组类型返回商和余数







 sum
●获取序列类型的总和









# 文件读取

```python
from os import path as osp

save_folder = "xxx/目录名"
# 创建目录
if not osp.exists(save_folder):
    os.mkdir(save_folder)


save_folder = save_folder if save_folder is not None else 'download'  #保存目录
#创建子文档,参数:父级目录,子目录名称
save_folder = osp.join(save_folder, chapter_title)
if not osp.exists(save_folder):
    os.mkdir(save_folder)
   
//写
with open(save_path, 'wb') as fp:
     fp.write(content)
except Exception as et:
   	logging.error(et, exc_info=True)
```





## 文件中读取数据

pi_digits.txt的文本文件，里面的数据如下：

```txt
3.1415926535
8979323846
2643383279
```

### 读取整个文件

```python
with open('pi_digits.txt') as f: # 默认模式为‘r’，只读模式
    contents = f.read() # 读取文件全部内容
    print(contents) # 输出时在最后会多出一行（read()函数到达文件末会返回一个空字符，显示出空字符就是一个空行）
    print('------------')
    print(contents.rstrip()) # rstrip()函数用于删除字符串末的空白
```

```
3.1415926535
8979323846
2643383279

------------
3.1415926535
8979323846
2643383279
```

### 逐行读取

```python 
with open('pi_digits.txt') as f:
    for line1 in f:
        print line1    # 每行末尾会有一个换行符
    print '------------'

with open('pi_digits.txt') as f: # 需要重新打开文本进行读取
    for line2 in f:
        print line2.rstrip() # 删除字符串末尾的空白
```

```
3.1415926535

8979323846

2643383279

------------
3.1415926535
8979323846
2643383279
```

**使用readline()函数**

```python
with open('pi_digits.txt') as f:
    while True:
        # 读取一行内容
        text = f.readline()
        # 判断是否读到内容
        if not text:
            break
            # 每读取一行的末尾已经有了一个 `\n`
            print(text, end="")
```

```
3.1415926535
8979323846
2643383279
```

**使用readlines()函数**

```python
with open('pi_digits.txt') as f:
    lines = f.readlines() # 读取文本中所有内容，并保存在一个列表中，列表中每一个元素对应一行数据
    
print(lines) # 每一行数据都包含了换行符

print('------------')
for line in lines:
    print(line.rstrip())

print('------------')
pi_str = ''  # 初始化为空字符
for line in lines:
    pi_str += line.rstrip() #字符串连接
    print(pi_str)
```

```
['3.1415926535\n', '8979323846\n', '2643383279\n']
------------
3.1415926535
8979323846
2643383279
------------
3.141592653589793238462643383279
```

## 写数据到文件

<font color=red>核心使用 newStr = f"{Parma1},{Parma2},{Parma3},…,{ParmaN}"  自定义写入格式</font>

写数据有几种不同的模式，最常用的是w’, ‘a’, 分别表示擦除原有数据再写入和将数据写到原数据之后：

```python
filename = 'write_data.txt'
with open(filename,'w', newline='' ,encoding='utf-8') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write("I am Meringue.\n")
    NJTECH='NJTECH'
    f.write(f"I am now studying in {NJTECH}.\n")
```

注意:

+ `newline=''`: 通过将`newline`参数设置为空字符串，您可以确保不进行特定的行尾字符转换，以兼容不同操作系统。例如在Windows上通常使用"\r\n"（回车换行），而在Linux和macOS上使用"\n"（换行符）。
+ `encoding='utf-8'`: 这是用于指定文件的编码方式。

创建一个write_data.txt的文本文件，里面的数据如下：

```
I am Meringue.
I am now studying in NJTECH.
```

追加

```python
with open(filename,'a') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
    f.write("I major in Machine learning and Computer vision.\n")
```



# 生成随机数模块random 

[python 生成随机数模块random 常用方法总结 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/34395664)

```
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# 输出测线距中心点处的距离
ws['A1'] = "测线距中心点处的距离/m"
for i, item in enumerate(data, start=2):
    ws.cell(row=i, column=1, value=item['distance_from_center'])

# 输出海水深度
ws['B1'] = "海水深度/m"
for i, item in enumerate(data, start=2):
    ws.cell(row=i, column=2, value=item['depth'])

# 输出覆盖宽度
ws['C1'] = "覆盖宽度/m"
for i, item in enumerate(data, start=2):
    ws.cell(row=i, column=3, value=item['coverage_width'])

# 输出与前一条测线的重叠率
ws['D1'] = "与前一条测线的重叠率/%"
for i, item in enumerate(data, start=2):
    ws.cell(row=i, column=4, value=item['overlap_percentage'])

wb.save("result1.xlsx")

```





```
from openpyxl import load_workbook

# 打开现有的工作簿
wb = load_workbook("result1.xlsx")

# 选择要写入的工作表
ws = wb.active

# 写入 'depth' 值
for i, item in enumerate(data, start=2):
    ws.cell(row=2, column=i, value=item['depth'])

# 写入 'coverage_width' 值
for i, item in enumerate(data, start=2):
    ws.cell(row=3, column=i, value=item['coverage_width'])

# 写入 'overlap_percentage' 值
for i, item in enumerate(data, start=2):
    if item['overlap_percentage'] == 0:
        # ws.cell(row=4, column=i, value='——')
        pass
    else:
        ws.cell(row=4, column=i, value=item['overlap_percentage'])

# 保存更改
wb.save("result1.xlsx")

```

![image-20230908142945578](python笔记.assets/image-20230908142945578.png)





```
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# 定义参数
D_center = 70  # 海域中心点处的海水深度
theta = math.radians(120)  # 换能器开角转换为弧度
alpha = math.radians(1.5)  # 坡度转换为弧度
distances = np.array([-800, -600, -400, -200, 0, 200, 400, 600, 800])  # 测线距中心点处的距离

# 计算每个距离的海水深度、覆盖宽度
sea_depth = D_center - distances * np.tan(alpha)
coverage_width = 2 * sea_depth * np.tan(theta / 2)
# 计算重叠率
overlap_rate = np.zeros(len(distances))
overlap_rate[1:] = 100 * (coverage_width[:-1] - distances[1:] + distances[:-1]) / coverage_width[:-1]

# 存储结果
data = pd.DataFrame({
    'distance': distances,
    'sea_depth': sea_depth,
    'coverage_width': coverage_width,
    'overlap_rate': overlap_rate
})

# 打印结果
print(data)

# 保存到Excel文件
wb = load_workbook("result1.xlsx") # 打开现有的工作簿
# 选择要写入的工作表
ws = wb.active
# 写入 'depth' 值
for i, item in enumerate(data['depth'], start=2):
    # ws.cell(row=2, column=i, value=item['depth'])
    ws.cell(row=2, column=i, value=item)
# 写入 'coverage_width' 值
for i, item in enumerate(data['coverage_width'], start=2):
    # ws.cell(row=3, column=i, value=item['coverage_width'])
    ws.cell(row=3, column=i, value=item)
# 写入 'overlap_percentage' 值
for i, item in enumerate(data['overlap'], start=2):
    if item == 0:
        # ws.cell(row=4, column=i, value='——')
        pass
    else:
        ws.cell(row=4, column=i, value=item)
# 保存更改
wb.save("result1.xlsx")

```





遍历

```
for i in range(8):
```





# 当前项目文件路径

```python
import os

current_directory = os.getcwd()
print("Current project file path:", current_directory)
```

#





