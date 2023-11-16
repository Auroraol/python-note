包(package)是一种管理 Python 模块命名空间的形式，从文件存储的角度看，包就是一个个文件夹。

比如有如下一个目录结构

```
sound/                          # 顶层包
      __init__.py               # 初始化 sound 包
      formats/                  # 文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  # 声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  # filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

<a name="h3dVH"></a>
## 使用 import 导入子包

要使用 import 导入包中的某个模块，只需要用点 `.` 分割即可，要使用其中的方法，必须带上包全名。

如:

```python
import sound.effects.echo

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

<a name="b1wl3"></a>
## 使用 from...import 导入子包

还有一种导入子模块的方法是使用 from...import 导入，此时使用子包中的方法只需带上引入的模块名即可。

```python
from sound.effects import echo

echo.echofilter(input, output, delay=0.7, atten=4)
```

<a name="7uZuh"></a>
## 使用 from...import 导入子包中的方法

此时要访问指定方法只需使用方法名即可 !

```python
from sound.effects.echo import echofilter

echofilter(input, output, delay=0.7, atten=4)
```

<a name="9HySH"></a>
## 使用 from package import * 导入包中所有模块

导入语句遵循如下规则：如果包定义文件 `__init__.py` 存在一个叫做 `__all__` 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。

比如在 `sounds/effects/__init__.py` 中包含如下代码:

```python
__all__ = ["echo", "surround", "reverse"]
```

这表示当你使用`from sound.effects import *`这种用法时，只会导入包里面这三个子模块。

如果 `__all__` 真的没有定义，那么使用 `from sound.effects import *` 这种语法的时候，就不会导入包 `sound.effects` 里的任何子模块。他只是把包 `sound.effects` 和它里面定义的所有内容导入进来（可能运行 `__init__.py` 里定义的初始化代码）。

比如在 `__init__.py` 中包含以下代码

```python
import sound.effects.echo
import sound.effects.surround
```

将会引入代码中提及的两个模块

如果代码改为

```python
from sound.effects import *
```

这将导入指定包下的所有模块。
