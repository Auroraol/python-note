## 数据类型对应

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

| 示例 | Python类型 | JSON类型 |
| --- | --- | --- |
| {} | dict | object |
| [] | list | array |
| () | tuple | array |
| "string" | str | string |
| 1234.56 | int或float | number |
| true/false | True/False | true/false |
| null | None | null |


Python对json进行操作可以使用`json`模块

## **json.dumps()**

`json.dumps()`方法返回一个`str`，内容就是标准的JSON。

```python
import json
d = dict(name='Bob', age=20, score=88)

print(d) # {'name': 'Bob', 'age': 20, 'score': 88}
print(repr(d)) # {'name': 'Bob', 'age': 20, 'score': 88}
print(json.dumps(d)) # {"name": "Bob", "age": 20, "score": 88}
```

### 保存到文件

`json.dump()`方法可以直接把JSON写入一个`file-like Object`。

```python
f = open('./test.txt', 'w')
json.dump(d, f)
f.close()
```

###  对象转化为json

 可选参数`default`就是把任意一个对象变成一个可序列为JSON的对象

```python
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
```

通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，用来存储实例变量。也有少数例外，比如定义了`__slots__`的class。

## **json.loads()**

JSON转化为字典

`json.loads()`方法返回一个`dict`，将JSON转化为字典。

```python
import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
data = json.loads(json_str)

print (data) # {'name': 'Bob', 'age': 20, 'score': 88}
print ("data2['name']: ", data['name']) # data2['name']:  Bob
```

### 读取json文件

`json.loads()`方法可以直接把JSON文件读出，输出dict。

```python
import json

# 读取数据并反序列化
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data) # {'name': 'Bob', 'age': 20, 'score': 88}
```

data.json

```json
{"name": "Bob", "age": 20, "score": 88}
```

如果读入一个普通文本文件，也能正常解析出一个str

如果读入一个二进制文件，会报错

'gbk' codec can't decode byte 0x80 in position 0: illegal multibyte sequence

### 解析json详解

**united_states.json**：

```json
{
   "name": "United States",
   "population": 331002651,
   "capital": "Washington D.C.",
   "languages": [
      "English",
      "Spanish"
   ]
}
```

在新文件中输入此Python脚本：

```python
import json
 
with open('united_states.json') as f:
  data = json.load(f)
 
print(type(data))
```

变量**data**包含JSON，作为Python字典。这意味着可以按如下方式检查字典键：

```scss
print(data.keys())

# OUTPUT:  dict_keys(['name', 'population', 'capital', 'languages'])
```

使用此信息，**name**可以输出如下：

```haskell
data['languages'][0]
 
# OUTPUT: English
```

<font color=red>小结:  解析可以使用了python自定义属性的函数</font>
