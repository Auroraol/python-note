# python中表当前项目文件路径 代码

```python
import os

current_directory = os.getcwd()
print("Current project file path:", current_directory)

```

# Python中将字符串转换为数字并将数字转换为字符串

```python
# 字符串转换为数字
num_str = "1234"
num = int(num_str)
print("Converted number:", num)
print("Type of converted number:", type(num))

# 数字转换为字符串
num = 5678
num_str = str(num)
print("Converted string:", num_str)
print("Type of converted string:", type(num_str))

```

```
Converted number: 1234
Type of converted number: <class 'int'>
Converted string: 5678
Type of converted string: <class 'str'>
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

写数据有几种不同的模式，最常用的是w’, ‘a’, 分别表示擦除原有数据再写入和将数据写到原数据之后：

```python
filename = 'write_data.txt'
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write("I am Meringue.\n")
    f.write("I am now studying in NJTECH.\n")
```

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



# python 生成随机数模块random 常用方法总结

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

