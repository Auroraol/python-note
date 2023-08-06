# python中表当前项目文件路径 代码

```python
import os

current_directory = os.getcwd()
print("Current project file path:", current_directory)

```

# python 字符串拼接

**使用运算符：`+`**

```
蟒Copy codestr1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

**通过F-strings拼接**

==F-strings效率最高==

```python
s1 = 'Hello'
s2 = 'World'
f'{s1} {s2}!'

#运行结果
'Hello World!'
```

在F-strings中我们也可以执行函数：

```python
def power(x):
    return x*x
 
x = 5
f'{x} * {x} = {power(x)}'
 
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
