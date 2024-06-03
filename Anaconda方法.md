[python3.10里没看到pip_mob649e815c3b9e的技术博客_51CTO博客](https://blog.51cto.com/u_16175466/7392579)

[开发工具 之四 Python 中的 pip 安装 及 使用详解-CSDN博客](https://blog.csdn.net/ZCShouCSDN/article/details/85002647)

# Anaconda介绍

 Anaconda，中文大蟒蛇，是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。其中，conda是一个开源的包、环境管理器，可以用于在同一个机器上安装不同版本的软件包及其依赖，并能够在不同的环境之间切换。

+ Anaconda对于python初学者而言及其友好，相比单独安装python主程序，选择Anaconda可以帮助省去很多麻烦，Anaconda里添加了许多常用的功能包，如果单独安装python，这些功能包则需要一条一条自行安装，在Anaconda中则不需要考虑这些，同时Anaconda还附带捆绑了两个非常好用的交互式代码编辑器（Spyder、Jupyternotebook）。

+ 如果我们不安装Anaconda的话，我们安装第三方库就必须要用pip install xxx去安装，当我们安装的库多了，就会形成文件紊乱和繁杂问题。而且pip install方法会默认把库安装在同一个路径中，假如当你去做项目时，别人给你的程序用的库是低版本的，而你自己通过pip安装的是高版本的库，由于存在兼容问题，你的库不能运行该程序，而你也不可能为了这个而删去你的高版本的库去下载这个符合环境的低版本库吧，所以这及其繁琐和不方便。

+ 这时Anaconda的作用就出来了！！！它能够创建一个虚拟环境，这个虚拟环境和你的主环境是分开的，就好像宿舍楼一样，一栋大宿舍楼有很多宿舍房间组成，每个房间都住着人，但是他们都是独立分开的，互不影响。如果你不想住宿，你随时可以退宿。也就是说，如果你创建的虚拟环境你不想要了，占内存了，你随时可以移走删除。

安装: [Anaconda3的安装配置及使用教程](https://blog.csdn.net/m0_59598029/article/details/132238463)

## 安装

### 第一步：下载

清华大学镜像网站下载最新版Anaconda：[点我下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)

#### 点击按日期排序，下载最新版

![image-20231106232334799](Anaconda方法.assets/image-20231106232334799.png)



<img src="Anaconda方法.assets/image-20231106232356237.png" alt="image-20231106232356237" style="zoom:67%;" />

其他选择默认

### 第二步，配置下载源

 **点击：Anaconda Prompt**

<img src="Anaconda方法.assets/image-20231106232457351.png" style="zoom:67%;" />

```cmd
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

**注意:  可以科学上网就不要设置**

### 第三步：配置环境变量

![image-20231106232628635](Anaconda方法.assets/image-20231106232628635.png)

### 第四步： 验证

 `conda --version`,如出现版本号，就是成功了~

![img](Anaconda方法.assets/(7{SBZ94HIHQSQNR{N6()Q3.png)

## 使用

### 启动Anaconda，创建一个虚拟环境：

<img src="Anaconda方法.assets/image-20231106232816085.png" alt="image-20231106232816085" style="zoom: 50%;" />

### 虚拟环境名称&语言选择&版本选择

![image-20231109214522196](Anaconda%E6%96%B9%E6%B3%95.assets/image-20231109214522196.png)

**创建的虚拟环境路径** 都是保存到anconda目录下的envs中

<img src="Anaconda方法.assets/image-20231106232936518.png" alt="image-20231106232936518" style="zoom: 67%;" />

## pycharm接入虚拟环境

![image-20231107132425040](Anaconda方法.assets/image-20231107132425040.png)

效果

![image-20231107132620002](Anaconda方法.assets/image-20231107132620002.png)

到此就可以在这里就行编码啦，如果想换一个python版本，可选择其他版本自行创建，不想用的虚拟环境可以删除

## 安装包

前提:  系统管理员权限运行anaconda

![image-20240221214542427](Anaconda%E6%96%B9%E6%B3%95.assets/image-20240221214542427.png)

# pip安装及使用详解

## 概要

pip 是 [Python](https://so.csdn.net/so/search?q=Python&spm=1001.2101.3001.7020) 的包安装程序。是 Python 标准库（The Python Standard Library）中的一个包，只是这个包比较特殊，用它可以来管理 Python 标准库（The Python Standard Library）中其他的包。

pip 支持从 [PyPI](https://pypi.org/)，版本控制，本地项目以及直接从分发文件进行安装。pip 是一个命令行程序。 安装 pip 后，会向系统添加一个 pip 命令，该命令可以从命令提示符运行。

## 安装

从 Python 2 版本 >=2.7.9 或 Python 3 版本 >=3.4 开始，官网的安装包中已经自带了 pip，在安装时用户可以直接选择安装。或者如果使用由 `virtualenv` 或者 `pyvenv` 创建的 Virtual Environment，那么 pip 也是被默认安装的。

如果没有在安装的时候，选择上安装pip，那么也可以从本地安装。例如，直接使用 `get-pip.py` 进行安装。首先从官网下载 `get-pip.py`，然后直接运行 `python get-pip.py` 即可。

更详细的安装，可以直接去官网参看[安装说明](https://pip.pypa.io/en/stable/installing/)

## 使用

安装后，在命令行中键入：`pip`+ 回车，就会出现如下使用说明：

```
Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      查看已经安装的包及版本信息
  list                        列出当前虚拟环境已经安装的包.
  show                        显示pip包所在目录及信息
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      搜索包
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                              (a)bort).
  --trusted-host <hostname>   Mark this host as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output
```


查看已安装的模块

```
pip list
```

查看待更新的模块

```
pip list-o
```

更新模块

```
pip install --U pip
```

查看pip版本

```
pip --version
```

显示已安装模块所在的目录

```
pip show -f package
```

## **通道链接**

 

| 豆瓣             | http://pypi.douban.com/simple            |
| ---------------- | ---------------------------------------- |
| 华中理工大学     | http://pypi.hustunique.com/simple        |
| 山东理工大学     | http://pypi.sdutlinux.org/simple         |
| 中国科学技术大学 | http://pypi.mirrors.ustc.edu.cn/simple   |
| 清华大学         | https://pypi.tuna.tsinghua.edu.cn/simple |

使用通道

```
pip install requests -i http://pypi.douban.com/simple
```



# Anaconda使用requirement方法

### 一、生成requirements.txt文件

用[conda](https://so.csdn.net/so/search?q=conda&spm=1001.2101.3001.7020) activate 你的环境名字，此时进入了你的环境中，然后使用代码：

```python
pip freeze > requirements.txt
```

就会生成一个所需环境包的txt文件，我的一个环境包含的包如下：

```python
backcall==0.1.0
beautifulsoup4==4.9.0
bleach==3.1.4
certifi==2020.4.5.2
colorama==0.4.3
cycler==0.10.0
decorator==4.4.2
defusedxml==0.6.0
entrypoints==0.3
ipykernel==5.1.4
ipython==7.13.0
ipython-genutils==0.2.0
jedi==0.17.0
Jinja2==2.11.2
joblib==0.15.1
jsonschema==2.6.0
jupyter-client==5.3.3
jupyter-contrib-core==0.3.3
jupyter-contrib-nbextensions==0.5.1
jupyter-core==4.5.0
jupyter-highlight-selected-word==0.2.0
jupyter-latex-envs==1.4.6
jupyter-nbextensions-configurator==0.4.1
jupyterthemes==0.20.0
kiwisolver==1.2.0
lesscpy==0.14.0
line-profiler==2.1.2
lxml==4.5.0
MarkupSafe==1.1.1
matplotlib==3.1.3
memory-profiler==0.55.0
mistune==0.8.4
mkl-fft==1.0.14
mkl-random==1.0.4
mkl-service==2.3.0
msgpack==0.6.2
nb-conda==2.2.1
nb-conda-kernels==2.2.3
nbconvert==5.6.1
nbformat==5.0.6
notebook==6.0.1
numpy==1.17.0
pandas==1.0.3
pandocfilters==1.4.2
parso==0.7.0
patsy==0.5.1
pickleshare==0.7.5
ply==3.11
prometheus-client==0.7.1
prompt-toolkit==3.0.4
psutil==5.7.0
Pygments==2.6.1
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2020.1
pywin32==227
pywinpty==0.5.7
PyYAML==5.3.1
pyzmq==18.1.1
scikit-learn==0.22.1
scipy==1.4.1
seaborn==0.10.1
Send2Trash==1.5.0
six==1.14.0
soupsieve==2.0.1
statsmodels==0.11.1
terminado==0.8.3
testpath==0.4.4
tornado==6.0.4
traitlets==4.3.3
wcwidth==0.1.9
webencodings==0.5.1
wincertstore==0.2

```

### 二、安装requirement.txt文件的扩展包

```python
pip install -r requirements.txt
```

除了使用pip命令来生成及安装requirement.txt文件以外，也可以使用conda命令来安装。

```python
conda install --yes --file requirements.txt
```

但是这里存在一个问题，如果requirements.txt中的包不可用，则会抛出“无包错误”。
使用下面这个命令可以解决这个问题

```python
$ while read requirement; do conda install --yes $requirement; done < requirements.txt
```

如果想要在conda命令无效时使用pip命令来代替，那么使用如下命令：

```python
$ while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```

有时可以导出conda环境，导出格式为.yml文件

```python
conda env export > requirements.yml
```

此时你的电脑需要这个conda环境，可以直接用这个yml文件在你的电脑上创造出一个同名字，同扩展包的环境，你只需要进入cmd，然后直接运行下面代码就可以了：

```python
conda env create -f requirements.yml
```

# Anaconda导出环境配置文件方法

## 导出环境配置

### 1. yml文件

1. 激活虚拟环境（fyp是我的虚拟环境名称，请根据你自己的名称进行修改）

```
conda activate fyp
```

1. 运行此代码

```
conda env export > environment.yml
```

### 2. req.txt文件

1. 激活虚拟环境（fyp是我的虚拟环境名称，请根据你自己的名称进行修改）

```
conda activate fyp
```

1. 运行此代码

```
conda list -e > requirements.txt
```

![image-20240421092102656](Anaconda%E6%96%B9%E6%B3%95.assets/image-20240421092102656.png)
![image-20240421092109861](Anaconda%E6%96%B9%E6%B3%95.assets/image-20240421092109861.png)

## 导入环境配置

```
conda env create -f environment.yml
```



# Anaconda navigator安装指定版本包

注:  要在打钩的地方右击，否则跳不出来右侧菜单

![image-20240420212329775](Anaconda%E6%96%B9%E6%B3%95.assets/image-20240420212329775.png)



# Windows: Pycharm terminal 无法直接进入conda虚拟环境

### 手动进入

comics是我的虚拟环境名称，请根据自己的名称进行修改

![image-20240421091607547](Anaconda%E6%96%B9%E6%B3%95.assets/image-20240421091607547.png)
