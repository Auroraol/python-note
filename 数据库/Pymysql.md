# 常见异常

| StandardError     | 所有异常的泛型基类         |
| ----------------- | -------------------------- |
| Warning           | 在非致命错误发生时引发     |
| Error             | 错误异常基类               |
| InterfaceError    | 数据库接口错误             |
| DataBaseError     | 与数据库相关的错误基类     |
| DataError         | 处理数据时出错             |
| OperationalError  | 数据库执行命令时出错       |
| IntegrityError    | 数据完整性错误             |
| InternalError     | 数据库内部出错             |
| ProgrammingError  | SQL执行失败                |
| NotSupportedError | 试图执行数据库不支持的特性 |

# 创建数据库对象

+ 使用 pymysql.connect() 方法 连接数据库

```mysql
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123123',
    db='python_test',  # 数据库名称
    autocommit=False  # 取消自动提交事务
)
```

# 获取游标对象

+ 使用 db.cursor() 方法 获取游标对象

+ 游标对象用于执行sql语句

```mysql
cursor = db.cursor()
```

# 执行sql语句

## execute方法

+ 使用 cursor.execute(sql语句) 方法 执行sql语句

```mysql
sql = "insert into students(name,age,height,gender,class_id) values" 
"('%s',%s,%s,'%s',%s)" % ('阿典', 21, 170.01, '男', 1)

cursor.execute(sql)
```

## executemany方法

+ 使用 cursor.executemany(sql语句) 方法 重复执行sql语句

+ 使用 executemany 方法下的sql语句的%s不需要加引号

```mysql
data = [('阿柒', '男'), ('阿典', '男')]
sql = "insert into students(name,gender) values(%s,%s)"
cursor.executemany(sql, data)
```

# 提交事务

+ 使用 db.commit() 方法 提交事务

```mysql
db.commit()
```

# 回滚事务

+ 使用 db.rollback() 方法 回滚事务

```mysql
sql = "delete from students where name='%s'" % '阿柒'
cursor.execute(sql)
db.rollback()
```

# 获取数据

##  fetchone方法

+ 使用 cursor.fetchone() 方法 获取单条数据

```mysql
cursor.execute('select * from students')
result = cursor.fetchone()
print(result)
```

## fetchmany方法

+ 使用 fetchmany(size) 方法 获取指定条数的数据

```mysql
cursor.execute('select * from students')
results = cursor.fetchmany(3)
print(results)
```

## fetchall方法

+ 使用 cursor.fetchone() 方法 获取所有数据

```mysql
cursor.execute('select * from students')
datas = cursor.fetchall()
print('序号|姓名|年龄|身高|性别|班级|是否删除')
for item in datas:
    aid = item[0]
    name = item[1]
    age = item[2]
    height = item[3]
    gender = item[4]
    class_id = item[5]
    is_delete = item[6]
    print(aid, name, age, height, gender, class_id, is_delete, sep='|')
```

# 关闭游标对象

+ 使用 cursor.close() 方法 关闭游标对象

```mysql
cursor.close()
```

## 关闭数据库

+ 使用 db.close() 方法 关闭数据库

```mysql
db.close()
```

# 封装数据库函数

```mysql
import pymysql

def create_table(name):
	# 连接数据库
    db = pymysql.connect(
    host='localhost',
    user='root',
    password='123123',
    db='python_test',
    autocommit=False
	)

    # 获取游标对象
    cursor = db.cursor()
    
    # 定义sql语句
    sql = """create table %s(
        id int primary key not null ,
        name varchar(10) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('男','女'),
        class_id int signed default 0
    )""" % name
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行成功 提交
        db.commit()
        print('执行成功！')
    except Exception as e:
        # 执行失败 回滚
        print('执行失败：', e)
        db.rollback()
    finally:
        # 关闭数据库
        cursor.close()
        db.close()

if __name__ == '__main__':
	create_table('stu_test')
```

