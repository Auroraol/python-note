使用Anaconda安装的Python, 自带一个[Jupyter Notebook](https://jupyter.org/), Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596785247291-c9055aa5-b6d3-4fe8-97fa-e1b5d6ce7cdc.png#align=left&display=inline&height=117&originHeight=117&originWidth=111&size=0&status=done&style=none&width=111)

如果是普通python安装包的话, 可以使用pip进行安装:

```bash
pip install jupyter
```

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596785170936-17d85318-6cda-499d-8c0d-7a0a2e640845.png#align=left&display=inline&height=459&originHeight=459&originWidth=873&size=0&status=done&style=none&width=873)

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596785150076-2a06a4e5-902f-4d72-9373-7c3a8342147b.png#align=left&display=inline&height=456&originHeight=456&originWidth=570&size=0&status=done&style=none&width=570)

Jupyter Notebook 有两种键盘输入模式。编辑模式，允许你往单元中键入代码或文本；这时的单元框线是绿色的。命令模式，键盘输入运行程序命令；这时的单元框线是灰色。

Jupyter Notebook 还是一个虚拟机, 可以在里面直接运行系统命令, 只需要在前面加上 `!` 即可:

```bash
!cd
!pip install numpy
```

如果本地没有安装 Python 环境, 我们可以使用在线版的 [Colab](https://colab.research.google.com/), 体验跟 Jupyter Notebook 一致

<a name="3heBA"></a>
## 修改默认工作路径

创建快捷方式, 将

```
C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"
```

中的 `%USERPROFILE%` 改为自己希望的路径, 比如:

```
C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py "D:/jupyter_notebook/"
```

运行此快捷方式即可

<a name="p5Jc1"></a>
## 通用命令

- `Alt-Enter` 运行代码块, 并在下面插入代码块
- `Shift-Enter` 运行代码块, 并选择下面的代码块
- `Ctrl-Enter` 运行选中的代码块

<a name="YuPEe"></a>
## 命令行模式(按 Esc 生效)

--- 编辑 ---

- `X` 剪切选择的代码块
- `C` 复制选择的代码块
- `V` 粘贴到下面
- `Shift-V` 粘贴到上面
- `D,D` 删除选中单元格
- `Z` 撤销删除
- `F` 查找并且替换
- `S` 保存并检查
- `L` 切换行号
- `Shift-L` 在所有单元格中切换行号，并保持设置
- `O` 选择单元格的输出
- `R` 清除代码块格式

--- 控制 ---

- `A` 在上面插入代码块
- `B` 在下面插入代码块
- `上` 或 `K` 选择上面的代码块
- `下` 或 `J` 选择下面的代码块
- `Enter` 进入编辑模式
- `Esc` 关闭页面
- `P` 打开命令配置
- `H` 显示快捷键
- `Shift-空格` 向上滚动
- `空格` 向下滚动

--- Markdown ---

- `M` 把代码块变成标签
- `1` 把代码块变成heading 1
- `2` 把代码块变成heading 2
- `3` 把代码块变成heading 3
- `4` 把代码块变成heading 4
- `5` 把代码块变成heading 5
- `6` 把代码块变成heading 6

<a name="lxMNQ"></a>
## 编辑模式(按 Enter 生效)

--- 控制 ---

- `Esc` 或 `Ctrl-M` 进入命令行模式
- `Ctrl-Shift-F` 或 `Ctrl-Shift-P` 打开命令配置
- `Alt-Enter` 运行代码块, 并在下面插入代码块
- `Shift-Enter` 运行代码块, 并选择下面的代码块
- `Ctrl-Enter` 运行选中的代码块

--- 编辑 ---

- `Ctrl-D` 删除整行
- `Ctrl-U` 撤销
- `Ctrl-Y` 重做

<a name="qYnwE"></a>
## 在PyCharm中使用Jupyter Notebook

首先在venv中安装Jupyter Notebook：
```bash
(venv) D:\Workplace\learning\python_learning> pip install jupyter
```
在PyCharm中打开并运行 `ipynb` 文件，会自动创建一个Jupyter Server：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597197824596-2ddc6877-399d-492b-a1a5-934ba7479e3b.png#align=left&display=inline&height=240&originHeight=240&originWidth=548&size=0&status=done&style=none&width=548)<br />可以在底部控制台看到：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597197872098-375daddb-8f62-4c74-9e65-f85c826f56b3.png#align=left&display=inline&height=504&originHeight=504&originWidth=1672&size=0&status=done&style=none&width=1672)<br />在浏览器打开此地址即可：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597197909845-0d27cfa5-979a-47be-8f8b-a93287243a3b.png#align=left&display=inline&height=613&originHeight=613&originWidth=1355&size=0&status=done&style=none&width=1355)<br />可以在PyCharm中直接编辑内容，其中：

- `#%%` 插入Python代码
- `#%% md` 插入Markdown

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1597739259522-a726e6b0-bc79-489a-8851-d7628ddc2237.png#align=left&display=inline&height=196&originHeight=196&originWidth=1127&size=0&status=done&style=none&width=1127)

按下 `Ctrl + Enter` 可以直接执行。

<a name="ebI8U"></a>
## 参考资料

- [JupyterNotebook](https://www.osgeo.cn/jupyter/index.html)


