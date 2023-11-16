Python是一门动态语言。变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

Python的3.0版本，常被称为Python 3000，或简称Py3k。相对于Python的早期版本，这是一个较大的升级。相对于Python2 (最新版本为2.7) ，有了更多的特性，很多语法规则也有了改变，在设计的时候没有考虑向下兼容。

<a name="3fc3058f"></a>
## 安装Python
Python下载链接: [Python Download Python.org](https://www.python.org/downloads/)

安装并添加到环境变量，一般安装的时候勾选 `Add Python to Environment variables` 即可(Windows)

Linux 一般系统自带 Python，不过只是 Python2，需要使用 Python3 需自行安装。

如果安装请使用以下命令:
```bash
apt-get install python3 -y
apt-get install build-essential -y
apt-get install python-pip -y
pip install --upgrade pip
```

<a name="6b5b908f"></a>
## 交互模式
使用 `python` 进入交互模式，使用 `exit()` 退出交互模式，使用 `python -V` 查看python版本号。
```bash
$ python
Python 3.7.0a2 (v3.7.0a2:f7ac4fe, Oct 17 2017, 17:06:29) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
# 查看所有已安装的模块
>>> help('modules')
...
# 退出Python交互模式
>>> exit()
# 查看python 版本，注意是大写的V
$ python -V
Python 3.7.0a2
```

安装 pylint (用于python代码检测)
```bash
python -m pip install pylint
```

<a name="169a49f1"></a>
## 执行py文件
执行.py文件，直接在 python 后跟上文件名(绝对路径或相对路径)即可，注意必须带上.py扩展名。
```bash
python test.py
```

<a name="jhGtF"></a>
### 创建可交互的Python文件
在py文件中，使用 `#%%` 可定义可执行块，按下 `Ctrl + Enter` 执行代码：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597739458359-8f583485-204e-4f0a-9319-6d6484cb8ab9.png#align=left&display=inline&height=424&originHeight=424&originWidth=1714&size=0&status=done&style=none&width=1714)<br />在VSCode中，右侧会生成一个预览区域，跟Jupyter Notebook运行效果一致。

<a name="fa25c15d"></a>
## 常见命令
<a name="48261538"></a>
### 查看已安装的模块
```css
python -m pydoc modules
```

<a name="YX5Dg"></a>
## 安装Python时的常见错误
<a name="UnicodeDecodeError"></a>
### UnicodeDecodeError
如果安装后使用的时候会报以下错误：
```bash
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa1 in position 43: invalid start byte
```
解决方法如下：<br />打开`c:\program files\python36\lib\site-packages\pip\compat\__init__.py`约75行

```python
return s.decode('utf_8')
```

改为
```python
return s.decode('cp936')
```

参考：

- [Windows上Python3.6 通过pip安装第三方库时出现UnicodeDecodeError的解决方法](http://blog.csdn.net/qq_25191257/article/details/56488662)
- [Python3解决UnicodeDecodeError: 'utf-8' codec can't decode byte..问题 终极解决方案](https://blog.csdn.net/wang7807564/article/details/78164855)

<a name="6Pylh"></a>
## IPython
[IPython](https://ipython.org/) 是一种基于Python的交互式解释器，提供了强大的编辑和交互功能。

IPython拥有：

1. 满足你各种需求的交互式shell
2. 火爆数据科学社区的Jupyter内核（供Jupyter Notebook使用）
3. 对交互式数据可视化和GUI工具的完美支持
4. 简单易用的高性能并行计算工具

IPython中的 `I` ，即代表交互的意思，所以IPython提供了丰富的工具，能更好地与python进行交互。<br />大家经常遇到的魔法命令，就是IPython的众多功能之一。

安装ipython：
```bash
pip install ipython
```

进入ipython交互模式：
```bash
$ ipython
Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```
输入 `?` 查看帮助， 输入 `exit` 退出交互模式。

参考：

- [使用IPython有哪些好处？](https://www.zhihu.com/question/51467397/answer/1098115714)

<a name="TvoHw"></a>
## Cython
[Cython](https://cython.org/)语言是Python的一个超集，编译成C语言，产生的性能提升可以从几个百分点到几个数量级，具体取决于手头的任务。 对于受Python原生对象类型约束的工作，加速将不会很大。 但是对于数值操作，或任何不涉及Python自身内部的操作，收益可能是巨大的。 这样，许多Python的本地限制可以被绕过或完全超越。

安装 cython：
```bash
pip install cython
```

查看 cython 版本：
```bash
$ cython -V
Cython version 0.29.21
```

除了能够加速已经编写的代码之外，Cython还具有其他几个优点：

- 使用外部C库可以更快
- 可以同时使用C和Python内存管理
- 可以根据需要选择安全性或速度
- Cython可以使用Python类型的提示语法

参考:

- [windows cython快速入门](https://blog.csdn.net/qq_33353186/article/details/80296691)
- [用Cython加速Python到“起飞”](https://www.jianshu.com/p/fc5025094912)
- [什么是Cython？让Python有C语言的速度](https://blog.csdn.net/qq_41597912/article/details/79494117)
- [Cython三分钟入门 - 伯乐在线](http://python.jobbole.com/87368/)

