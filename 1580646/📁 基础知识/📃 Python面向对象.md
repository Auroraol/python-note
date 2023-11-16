<a name="bMg1w"></a>
## 面向对象技术简介

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **类属性:** 类属性在整个实例化的对象中是公用的，定义在类中且在函数体之外，在python中类的实例也能访问类属性。
- **实例属性:** 定义在方法中的变量，只作用于当前实例的类。
- **实例方法:** 类中定义的函数。
- **对象:** 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
- **方法重写(override):** 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖，也称为方法的重写。
- **继承:** 即一个**派生类**（derived class）继承**基类**（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
- **实例化:** 创建一个类的实例，类的具体对象。

Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。

对象可以包含任意数量和类型的数据。

<a name="b0v2a"></a>
## 类的创建

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score() # Bart Simpson: 59
lisa.print_score() # Lisa Simpson: 87
```

`self` 指向当前创建的类的实例本身 (其他语言一般叫`this`) 。`__init__`方法、实例方法的第一个参数永远是`self`，调用的时候不需要显式传入。

注意，python实例化一个对象不需要关键字`new`。

<a name="u0Gpw"></a>
## 类属性

类属性在整个实例化的对象中是公用的，定义在类中且在函数体之外，在python中类的实例也能访问类属性。

```python
class Student(object):
    name = 'Student'

print(Student.name)  # Student

s = Student()
print(s.name)  # Student
```

<a name="BcQv4"></a>
## 类的专有方法

- `__init__` : 构造函数，在生成对象时调用
- `__del__`: 析构函数，释放对象时使用
- `__repr__` : 打印，转换
- `__setitem__` : 按照索引赋值
- `__getitem__`	: 按照索引获取值
- `__len__`: 获得长度
- `__cmp__`: 比较运算
- `__call__`: 函数调用
- `__add__`: 加运算
- `__sub__`: 减运算
- `__mul__`: 乘运算
- `__div__`: 除运算
- `__mod__`: 求余运算
- `__pow__`: 乘方
- `__str__`: 字符串化

<a name="qLNiK"></a>
## 访问限制

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个**私有变量**（private），也可以使用`def`结合两个下划线`__`定义一个私有方法，只有内部可以访问，外部不能访问。

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self.__score__ = score
    def print_score(self):
        print('my score is %s' % (self.__score))
    def __print_name(self):
        print('my name is %s' % (self.name))
    def print_name(self):
        self.__print_name()

bart = Student('Bart Simpson', 59)

print(bart.name) # Bart Simpson
print(bart.print_score()) # my score is 59

# print(bart.__score) # ERROR: AttributeError: 'Student' object has no attribute '__score'
# print(bart.__print_name()) # ERROR: AttributeError: 'Student' object has no attribute '__print_name'

print(bart.print_name()) # my name is Bart Simpson

print(bart.__score__) # 59
```

在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量

如果看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

:::info
**事实上并不存在私有属性和方法**
:::

其实私有属性和私有方法并不存在，不能直接访问**name是因为Python解释器对外把**name变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问__name变量，同样的，可以使用 `_Student__print_name()` 访问私有方法，但是不建议这样做，而且不同的编译器可能解释不同(官方的是CPython)。

```python
print(bart._Student__score) # 59
print(bart._Student__print_name()) # my name is Bart Simpson
```

<a name="oiKaA"></a>
## 对象相关的一些函数
<a name="SB0fB"></a>
### isinstance

判断一个变量是否是某个类型可以用`isinstance()`判断：

```python
dog = Dog()
cat = Cat()
print(isinstance(dog, Dog)) # True
print(isinstance(dog, Cat)) # False
print(isinstance(dog, Animal)) # True
```

<a name="type"></a>
### type

用type来输出对象的类型。

```python
print(type(dog)) # <class '__main__.Dog'>
print(type('')) # <class 'str'>
print(type(1)) # <class 'int'>
```

<a name="dir"></a>
### dir

获得一个对象的所有属性和方法，可以使用`dir()`函数，它返回一个包含字符串的list。

```python
print(dir(dog))
```

<a name="f04f7a21"></a>
### hasattr、setattr、getattr

判断对象是否包含属性、属性设置与获取。

```python
print(hasattr(dog, 'x')) # False
print(hasattr(dog, 'eat')) # True
setattr(dog, 'y', 19) # 设置一个属性'y'
print(hasattr(dog, 'y')) # True
print(getattr(dog, 'y')) # 19
```

<a name="cdxyn"></a>
## 运算符重载

以前学习C++的时候就很惊羡其运算符重载，Python也同样支持运算符重载。

```python
#!/usr/bin/python3

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2) # Vector (7, 8)
```

使用 `__str__(self)` 将对象字符串化，比如print函数打印的时候可以自动转化为字符串。

使用 `__add__(self,other)` 将 `+` 运算符重载。

<a name="2dde3029"></a>
## 继承

在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

继承什么类就在括号里写对应的类名，同其他编程语言一样，子类可以对父类的方法进行重写。

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

<a name="918a3677"></a>
### 多继承

Python同样有限的支持多继承形式，不过需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

```python
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

#另一个类，多重继承之前的准备
class speaker(people):
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个程序员，我使用的是 %s"%(self.name,self.topic))

#多重继承
class sample1(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test1 = sample1("Xiaoyu",22,80,4,"Python")
test1.speak()   # 方法名同，默认调用的是在括号中排前地父类的方法
# 我叫 Xiaoyu，我是一个程序员，我使用的是 Python

class sample2(student,speaker):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test2 = sample2("Xiaoqiao",20,80,4,"Python")
test2.speak()   # 方法名同，默认调用的是在括号中排前地父类的方法
# Xiaoqiao 说: 我 20 岁了，我在读 4 年级
```

<a name="154ae683"></a>
## 多态

类的定义见最顶部

```python
>>> dog = Dog()
>>> isinstance(dog, Animal)
True
>>> isinstance(dog, Dog)
True
```

可以看出dog不仅仅是Dog，还是Animal！

当我们创建了一个Dog的实例dog时，dog的数据类型是Dog没错，但dog同时也是Animal也没错，Dog本来就是Animal的一种！所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行。

Dog可以看成Animal，但Animal不可以看成Dog。

多态的好处挺多的，比如我们定义一个函数，接受一个Animal的实例作为参数

```python
def run_twice(animal):
    animal.run()
    animal.run()
```

使用的时候:

```python
>>> run_twice(Dog())
Dog is running...
Dog is running...
```

```python
>>> run_twice(Cat())
Cat is running...
Cat is running...
```

这样就不必关心具体是什么动物，因为不管是Dog还是Cat都是属于Animal类型。


