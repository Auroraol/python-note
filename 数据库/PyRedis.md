# 安装redis模块

```mysql
pip install redis
```

# 连接redis数据库

```mysql
from redis import Redis

redis = Redis(
    host='localhost',
    port=6379,
    db=1
)
```

# 字符串类型

## 添加/修改数据

```mysql
redis.set('name', 'ahao')
data = {'age': 21, 'gender': 'man'}

redis.mset(data)
redis.setex('test', 30, 'abc')
```

##  获取数据

```mysql
name = redis.get('name')
print(name.decode())

age, gender = redis.mget('age', 'gender')
print(age.decode(), gender.decode())
```

## 删除数据

```mysql
redis.delete('name')
redis.delete('age', 'gender')
```

## 获取keys

```mysql
keys = redis.keys()

items = []
for item in keys:
	items.append(item.decode())

print(items)
```

## 判断键是否存在

+ 存在则返回1，否则返回0

```
print(redis.exists('name'))
```

# hash 类型

## 添加/修改数据

```
redis.hset('user', 'name', 'ahao')

data = {'name': 'ahao', 'age': 21, 'gender': 'man'}
redis.hset('user2', mapping=data)
```

## 获取数据

```mysql
name = redis.hget('user', 'name')
print(name.decode())

age, gender = redis.hmget('user2', 'age', 'gender')
print(age.decode(), gender.decode())
```

## 删除数据

```mysql
redis.hdel('user', 'name')
redis.hdel('user2', 'age', 'gender')
```

# **list 类型**

**添加/修改数据**

```
lst1 = ['a', 'b'] * 3
redis.lpush('lst1', *lst1)
redis.rpush('lst2', *lst1)
```

 **获取数据**

```
lst_res = redis.lrange('lst1', 0, -1)

items = []
for item in lst_res:
	items.append(item.decode())

print(items)

lst_res2 = redis.lrange('lst2', 0, -1)

items2 = []
for item in lst_res2:
	items2.append(item.decode())

print(items2)
```

**删除数据**

```
redis.lrem('lst1', -2, 'b')
redis.lrem('lst2', 2, 'a')
```

# set  

## **添加/修改数据**类型

```
set1 = {1, 2, 3, 4, 5}
redis.sadd('set1', *set1)
```

##  **获取数据**

```
set_res = redis.smembers('set1')

items = []
for item in set_res:
	items.append(item.decode())

print(items)
```

## **删除数据**

```
del_set = {3, 4}
redis.srem('set1', *del_set)
```

# **zset 类型**

## **添加/修改数据**

```
data = {'ahao': 3, 'aqi': 1, 'adian': 2, 'atong': 4}
print(data)
redis.zadd('zset1', data)
```

##  获取数据

```
zset_res = redis.zrange('zset1', 0, -1)

items = []
for item in zset_res:
	items.append(item.decode())

print(items)
```

 ## **删除数据**

```
del_zset = {3, 4}
redis.zrem('zset1', *del_zset)
```

