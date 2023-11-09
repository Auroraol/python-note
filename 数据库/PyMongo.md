# 连接mongo

```
from pymongo import MongoClient

client = MongoClient(
    host='localhost',
    port=27017,
)
```

## 指定数据库

●如果数据库不存在则创建数据库

```
db = client['python_test']
```

# 指定集合

●如果集合不存在则创建集合

```
collection = db['user']
```

# 插入数据

## 插入单条数据

```
llection.insert_one({'name': '请求', 'age': 21})
```

## 插入多条数据

```
data = [{'name': 'qq', 'age': 21}, {'name': 'ss', 'age': 22}]
collection.insert_many(data)
```

# 查询数据

##  查询一条数据

```
res = collection.find_one({'name': 'ss'})
print(res)
```

## 查询多条数据

```
datas = collection.find({'age': 21})
for item in datas:
	print(item)
```

# 更新数据

## 更新一条数据

```
collection.update_one({'name': 'ss'}, {'$set': {'age': 22}})
```

## 更新多条数据

```
collection.update_many({'age': 22}, {'$set': {'age': 21}})
```

# 删除数据

##  删除一条数据

```
collection.delete_one({'name': 'ss'}
```

## 删除多条数据

```
collection.delete_many({'age': 21})
```

