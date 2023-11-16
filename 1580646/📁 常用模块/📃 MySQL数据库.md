PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库。

- [PyMySQL 官网文档](https://pymysql.readthedocs.io/en/latest/index.html)
- [Python3 MySQL 数据库连接 - PyMySQL 驱动](http://www.runoob.com/python3/python3-mysql.html)

安装:

```bash
$ pip3 install PyMySQL
```

- 连接: 与数据库建立的通讯, 使用完后需要关闭
- 游标: 处理数据的一种方法，游标提供了在结果集中一次一行或者多行前进或向后浏览数据的能力

<a name="cdf2858c"></a>
## 简单使用

使用步骤:

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
```

或

```python
#!/usr/bin/python3
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `img` WHERE `title` like %s"
        cursor.execute(sql, ('%大%',))
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
```

1. pymysql.connect 链接数据库, 顺序传入 `host, user, password, db`, 也可使用命名参数的方式传递
2. db.cursor 创建游标, 以操作数据库
3. cursor.execute 执行 SQL 语句
4. fetchone/fetchall 查询一条或多条数据

<a name="CRUD"></a>
## CRUD

<a name="a3585778"></a>
### 1. 创建数据表

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """
      CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT
      )
      """

cursor.execute(sql)

# 关闭数据库连接
db.close()
```

<a name="91ea53ad"></a>
### 2. 插入数据

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """
        INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
        VALUES ('Mac', 'Mohan', 20, 'M', 2000)
      """
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()
```

以上 SQL 语句也可写为:

```python
sql = """
        INSERT INTO EMPLOYEE(FIRST_NAME,
        LAST_NAME, AGE, SEX, INCOME)
        VALUES (%s, %s,  %s,  %s,  %s )
      """
cursor.execute(sql, ('Mac', 'Mohan', 20, 'M', 2000))
```

<a name="dede8c33"></a>
### 3. 查询数据

- fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
- fetchall(): 接收全部的返回结果行.
- rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
      # 打印结果: fname=Mac,lname=Mohan,age=20,sex=M,income=2000.0
except:
   print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()
```

<a name="20ad14d4"></a>
### 4. 更新操作

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = "UPDATE EMPLOYEE SET INCOME = INCOME + 100 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
```

<a name="882e3d83"></a>
### 5. 删除操作

```python
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","root","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE >= %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()
```

<a name="575a0d5d"></a>
## 使用参考

1. 事务

- cursor.commit() 方法提交游标的所有更新操作
- cursor.rollback() 方法回滚当前游标的所有操作

2. 查询

- cursor.fetchone() 返回第一条查询结果
- cursor.fetchall() 返回所有查询结果

3. 执行

- cursor.execute() 执行SQL语句

4. 连接与关闭

- pymysql.connect(host, user, password, db) 连接数据库
- connection.close() 关闭数据库
- connection.cursor() 创建游标
