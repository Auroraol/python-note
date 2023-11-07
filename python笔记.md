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

## **数据类型**

| 类型   | 关键字  |
| ------ | ------- |
| 字符串 | string  |
| 整数   | int     |
| 浮点数 | float   |
| 复数   | complex |
| 列表   | list    |
| 元组   | tuple   |
| 字典   | dict    |
| 集合   | set     |

```python
String = 'Hello world'
Int = 1
Float = 1.2
Complex = 1+2j
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
List = [1, 2, 3, 4]
for i in List:
	print(i)  # 1 2 3 4
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



# 当前项目文件路径

```python
import os

current_directory = os.getcwd()
print("Current project file path:", current_directory)
```

# 字符串操作

## 字符串和数字相互转换

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

# python 字符串拼接

**使用运算符：`+`**

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

# 参数

- **不可变类型**，内存中的数据不允许被修改：

  - 数字类型 `int`, `bool`, `float`, `complex`, `long(2.x)`
  - 字符串 `str`
  - 元组 `tuple`

- **可变类型**，内存中的数据可以被修改：

  - 列表 `list`

  - 字典 `dict`

  - ```python
    def saveResult(res, result):
        # 识别成功
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







函数之间空两格







