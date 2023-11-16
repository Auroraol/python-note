
Python模块(module)分为内置模块（标准模块）和自定义模块。

<a name="a80d264c"></a>
## import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。

- 将整个模块(somemodule)导入，格式为：import somemodule
- 从某个模块中导入某个函数,格式为：from somemodule import somefunction
- 从某个模块中导入多个函数,格式为：from somemodule import firstfunc, secondfunc, thirdfunc
- 将某个模块中的全部函数导入，格式为：from somemodule import *

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入，否则，搜索系统库目录，如果存在就导入。

(ps: 写习惯了js的 `import ... from ...` 感觉写着python的 `from ... import` 怪怪的，哈哈(～￣▽￣)～ )

<a name="2e8ca547"></a>
## dir()

`dir()` 函数接收一个模块名的参数，将返回指定模块内定义的所有名称。以一个字符串列表的形式返回。

```python
>>> import  sys
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
```

如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称

<a name="14ae946b"></a>
## 安装第三方模块

在Python中，安装第三方模块，是通过包管理工具pip完成的。

第三方库都会在Python官方的[pypi.python.org](https://pypi.python.org/)网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫[Pillow](https://pypi.python.org/pypi/Pillow/)，因此，安装Pillow的命令就是：

```python
pip install Pillow
```


<a name="e33257b9"></a>
## 自定义模块

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过`_`前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用，比如：`abc`，`x123`，`PI`等；

类似`__xxx__`这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的`__author__`，`__name__`就是特殊变量，`hello`模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不要用这种变量名；

类似`_xxx`和`__xxx`这样的函数或变量就是非公开的（private），不应该被直接引用，比如`_abc`，`__abc`等。

**export.py**

```python
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

我们在模块里公开`greeting()`函数，而把内部逻辑用private函数隐藏起来了，这样，调用`greeting()`函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

<a name="39ae6499"></a>
## 导入自定义模块

导出模块不需要特定的语句，整个`export.py`文件就是一个模块，比如在上述文件同级目录下有一个叫`test.py`的文件

<a name="46e8d3dc"></a>
### 使用 import 语句导入整个模块

```python
import export

hello = export.greeting('xiaoyu')
print(hello)
hello = export.greeting('a')
print(hello)
```

测试:

```bash
$ python test.py
Hello, xiaoyu
Hi, a
```

<a name="6f4045fa"></a>
### 使用 from...import 导入指定方法

```python
from export import greeting

hello = greeting('xiaoyu')
print(hello)
hello = greeting('a')
print(hello)
```

测试:

```bash
$ python test.py
Hello, xiaoyu
Hi, a
```

<a name="47336b78"></a>
### 使用 from…import * 导入所有方法

```python
from export import *

hello = greeting('xiaoyu')
print(hello)
hello = greeting('a')
print(hello)
```

测试:

```bash
$ python test.py
Hello, xiaoyu
Hi, a
```

<a name="5b89934e"></a>
## `__name__` 属性

一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用**name**属性来使该程序块仅在该模块自身运行时执行。

```python
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```

运行输出如下：

```bash
$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
```
