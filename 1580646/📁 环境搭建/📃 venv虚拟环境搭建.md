在开发Python应用程序的时候，系统安装的 Python3 只有一个版本, 比如3.7。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个 Python，就是安装在系统的 Python3。如果应用A需要 jinja 2.7，而应用B需要jinja 2.6 怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。`virtualenv` 就是用来为一个应用创建一套“隔离”的Python运行环境。(可理解成每个 node 项目下的 node_modules)

<a name="ffc80d46"></a>
## 通过virtualenv创建
安装 virtualenv
```bash
pip install virtualenv
# or
conda install virtualenv
```

进入项目目录, 创建一个独立的Python运行环境，命名为venv
```bash
virtualenv --no-site-packages venv
```

加上 `--no-site-packages` 选项，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

安装成功后, 可以在项目目录下看到一个 venv 文件夹, 激活后终端也可看到加了 (venv) 前缀：
```bash
PS D:\Documents> & d:/Documents/venv/Scripts/activate.ps1
(venv) PS D:\Documents>
```

默认应该会自动激活 venv 环境, 如果没有激活, 可执行：
```bash
./venv/Scripts/activate
```

如果在 Windows 上使用 PowerShell 的时候激活失败, 会提示：
```bash
PS D:\Documents\crawler> & d:/Documents/venv/Scripts/activate.ps1                                                                 在此系统上禁止运行脚本。有关详细
& : 无法加载文件 D:\Documents\venv\Scripts\activate.ps1，因为_Execution_Policies。在此系统上禁止运行脚本。有关详细
信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
所在位置 行:1 字符: 3                                                ion
+ & d:/Documents/venv/Scripts/activate.ps1
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) []，PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

此时, 需要使用管理员打开 PS, 并执行 `Set-ExecutionPolicy RemoteSigned`, 输入 y 即可：
```bash
PS C:\Windows\system32> Set-ExecutionPolicy RemoteSigned

执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): y
```

如果安装不成功, 可能需要先更新 pip
```bash
python -m pip install --upgrade pip
```

编写代码的时候, 可以安装 pylint 以进行代码检查
```bash
python -m pip install -U pylint
```

<a name="rV928"></a>
### requirements.txt
`requirements.txt` 是用于记录所有依赖包及其精确的版本号，以便在新环境部署。

在虚拟环境下生成 `requirements.txt` ：
```bash
(venv) D:\Workplace\learning\python_learning>pip freeze > requirements.txt
```
注意，如果不是在虚拟环境下生成 `requirements.txt` ，则将导出python主环境下的所有包到文件。

生成的 `requirements.txt` 长这样：
```
appdirs==1.4.4
certifi==2020.6.20
distlib==0.3.1
filelock==3.0.12
numpy==1.19.1
six==1.15.0
virtualenv-clone==0.5.4
```

重新部署时，通过 `requirements.txt` 安装依赖包：
```bash
pip install -r requirements.txt
```

<a name="ME99W"></a>
## 通过conda创建
如果是通过 Anaconda 安装的, 可以使用以下命令创建 venv 环境:
```bash
conda create --name yourEnvName
# or
conda create -n yourEnvName
```

指定Python版本：
```bash
conda create -n py38 python=3.8 -y
conda create -n py37 python=3.7 -y
```

创建详情：
```
$ conda create -n py38 python=3.8 -y
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 22.11.1

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: D:\Development\stable-diffusion\stable-diffusion-webui1\venv\py38

  added / updated specs:
    - python=3.8


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2023.01.10 |       haa95532_0         121 KB  defaults
    certifi-2022.12.7          |   py38haa95532_0         148 KB  defaults
    libffi-3.4.2               |       hd77b12b_6         109 KB  defaults
    openssl-1.1.1s             |       h2bbff1b_0         5.5 MB  defaults
    pip-22.3.1                 |   py38haa95532_0         2.7 MB  defaults
    python-3.8.16              |       h6244533_2        18.9 MB  defaults
    setuptools-65.6.3          |   py38haa95532_0         1.1 MB  defaults
    sqlite-3.40.1              |       h2bbff1b_0         889 KB  defaults
    wincertstore-0.2           |   py38haa95532_2          15 KB  defaults
    ------------------------------------------------------------
                                           Total:        29.5 MB

done
#
# To activate this environment, use
#
#     $ conda activate py38
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

若想要在创建环境同时安装python的一些包：
```bash
conda create -n yourEnvName numpy pandas
conda create -n py38 python=3.8 numpy pandas
```

通过以上方式创建的虚拟环境，会在conda程序目录下，比如：
```
C:\ProgramData\Miniconda3\envs
```

创建的虚拟环境列表可从 `~/.conda/environments` 中查看。

<a name="lUHbR"></a>
### 在指定路径下创建虚拟环境
要指定虚拟环境路径，使用 `--prefix` 或 `-p` 参数：
```bash
conda create --prefix=./venv

conda create -p D:\Users\quanzaiyu\.conda\envs\py38 python=3.8 -y
conda create -p D:\Users\quanzaiyu\.conda\envs\py37 python=3.7 -y
```
以上命令，在当前目录先创建了一个虚拟环境，要激活指定的虚拟环境，在 `activate` 后面带上路径即可：
```bash
conda activate ./venv
```
此时在激活的虚拟环境下，终端显示如下：
```bash
(venv) D:\Workplace>
```

<a name="aX25m"></a>
### 修改虚拟环境默认路径
修改 `~/.condarc` ，添加以下内容：
```yaml
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
envs_dirs:
  - D:\Users\quanzaiyu\.conda\envs
pkgs_dirs:
  - D:\Users\quanzaiyu\.conda\pkgs
```

<a name="jkoQF"></a>
### 激活虚拟环境
```bash
conda activate venv
```
在激活的虚拟环境下，终端显示如下：
```bash
(venv) D:\Workplace>
```

<a name="nPbLf"></a>
### 退出虚拟环境
```bash
(venv) $ conda deactivate
```

<a name="SFjRh"></a>
### 删除虚拟环境
```bash
conda env remove -n yourEnvName
```

<a name="38aVD"></a>
### 查看虚拟环境信息
查看所有的虚拟环境, 使用 `conda info --envs` 或 `conda env list`:
```bash
$ conda info --envs
$ conda env list
# conda environments:
#
base                  *  C:\ProgramData\Anaconda3
paddle                   C:\ProgramData\Anaconda3\envs\paddle
```

查看当前conda环境信息：
```bash
$ conda info

     active environment : None
       user config file : C:\Users\quanzaiyu\.condarc
 populated config files : C:\Users\quanzaiyu\.condarc
          conda version : 4.8.3
    conda-build version : not installed
         python version : 3.8.3.final.0
       virtual packages : __cuda=10.1
       base environment : C:\ProgramData\Miniconda3  (read only)
           channel URLs : https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/noarch
          package cache : C:\ProgramData\Miniconda3\pkgs
                          C:\Users\quanzaiyu\.conda\pkgs
                          C:\Users\quanzaiyu\AppData\Local\conda\conda\pkgs
       envs directories : C:\Users\quanzaiyu\.conda\envs
                          C:\ProgramData\Miniconda3\envs
                          C:\Users\quanzaiyu\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/4.8.3 requests/2.23.0 CPython/3.8.3 Windows/10 Windows/10.0.19041
          administrator : False
             netrc file : None
           offline mode : False
```

参考: [conda创建新环境](https://blog.csdn.net/SARACH_WONG/article/details/89328307)

<a name="XS23l"></a>
## 通过pipenv创建
最近发现了一个全新的Python包管理器，叫做pipenv，集合了所有编程语言的包管理器的优点，是kennethreitz大神的一个周末项目。它的工作方式就像Node.js里的npm或者yarn，很容易就解决Python2/3混合使用产生的版本问题。

安装：
```bash
pip install pipenv
# or
conda install pipenv
```

<a name="JxBr4"></a>
### 生成虚拟环境
在你的项目的根目录下面运行以下命令来生成Python3的虚拟环境：
```
python -m pipenv --three
```
输出信息如下：
```
Creating a virtualenv for this project…
Pipfile: D:\Workplace\learning\python_learning\Pipfile
Using C:/Program Files/Anaconda3/python.exe (3.8.3) to create virtualenv…
[   =] Creating virtual environment...Already using interpreter C:\Program Files\Anaconda3\python.exe
Using base prefix 'C:\\Program Files\\Anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in C:\Users\quanzaiyu\.virtualenvs\python_learning-bS3XAWRQ\Scripts\python.exe
copying C:\Program Files\Anaconda3\python.exe => C:\Users\quanzaiyu\.virtualenvs\python_learning-bS3XAWRQ\Scripts\python.exe
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter C:/Program Files/Anaconda3/python.exe

Successfully created virtual environment!
Virtualenv location: C:\Users\quanzaiyu\.virtualenvs\python_learning-bS3XAWRQ
```
可以看到，在windows下使用pipenv时，虚拟环境文件夹会在用户目录下默认创建，为了方便管理，将这个虚环境的文件的位置更改一下。

类似地，使用  `python -m pipenv --two`  生成Python2环境。

<a name="77sy1"></a>
### 修改虚拟环境路径
新建一个名为 `WORKON_HOME` 的环境变量，然后将环境变量的值设置为指定路径，以后pipenv默认就将虚拟环境生成到此路径。<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596790620560-4cc337bd-a73d-4ed4-929e-d1a8d28ac18e.png#averageHue=%23ececeb&height=190&id=PlPtQ&originHeight=190&originWidth=667&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=667)<br />或者使用命令：
```bash
setx WORKON_HOME D:\Users\quanzaiyu\.conda\envs
```

再次生成虚拟环境，可以看到已经到指定的路径下：
```
$ python -m pipenv --three
Creating a virtualenv for this project…
Pipfile: D:\Workplace\learning\python_learning\Pipfile
Using C:/Program Files/Anaconda3/python.exe (3.8.3) to create virtualenv…
[ ===] Creating virtual environment...Already using interpreter C:\Program Files\Anaconda3\python.exe
Using base prefix 'C:\\Program Files\\Anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in D:\py_envs\python_learning-bS3XAWRQ\Scripts\python.exe
copying C:\Program Files\Anaconda3\python.exe => D:\py_envs\python_learning-bS3XAWRQ\Scripts\python.exe
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter C:/Program Files/Anaconda3/python.exe

Successfully created virtual environment!
Virtualenv location: D:\py_envs\python_learning-bS3XAWRQ
```

<a name="5BlcY"></a>
### 进入虚拟环境
运行以下命令进入虚拟环境：
```
python -m pipenv shell
```
输入 `exit` 退出。

如果之前没有创建虚拟环境，则通过shell命令会指定创建一个虚拟环境，并使用此虚拟环境。

<a name="e655a410"></a>
### 安装与卸载依赖
伪类方便起见，以下命令，省略 `python -m` 。

`pipenv install` 可以一键安装所有依赖包，还会生成 `pipfile.lock` 文件，里面记录了这次安装时的依赖包。

比如：
```
pipenv install flask
```
以上命令可以安装Flask到生产环境，再加 `--dev` 参数，比如以下命令就会安装到开发环境：
```
pipenv install flask --dev
```
指定镜像源安装依赖：
```
pipenv install --pypi-mirror https://mirrors.aliyun.com/pypi/simple
```

类似地，把上面的install改成uninstall就会卸载依赖包。

卸载项目下所有的包：
```
pipenv uninstall --all
```

更多的命令请查看[pipenv官网](https://docs.pipenv.org/)。

<a name="B1wuD"></a>
### Pipfile

`Pipfile` 与 `Pipfile.lock` 是社区拟定的依赖管理文件，用于替代过于简陋的 `requirements.txt` 文件。

通过pipenv创建的虚拟环境，会自动生成Pipfile，可以看出，跟 `package.json` 差不多：
```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
appdirs = "==1.4.4"
certifi = "==2020.6.20"
distlib = "==0.3.1"
filelock = "==3.0.12"
numpy = "==1.19.1"
six = "==1.15.0"
virtualenv-clone = "==0.5.4"

[requires]
python_version = "3.8"
```

Pipfile 文件有以下特点：

- `Pipfile` 文件是 [TOML](https://github.com/toml-lang/toml) 格式而不是 `requirements.txt` 这样的纯文本。
- 一个项目对应一个 `Pipfile`，支持开发环境与正式环境区分。默认提供 `default` 和 `development` 区分。
- 提供版本锁支持，存为 `Pipfile.lock`。

通过Pipfile进行安装：
```
python -m pipenv install
```

<a name="d97GL"></a>
## 在PyCharm中配置Python解释环境
配置路径：File | Settings | Project: xxx | Project Interpreter<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596764699938-47a31ee4-f400-4e31-898a-ea93e4835742.png#averageHue=%233c4043&height=711&id=Gfitv&originHeight=711&originWidth=998&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=998)<br />如果没有虚拟环境，可以选择创建虚拟环境：<br />![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596791671382-0f41f51a-76a4-4daa-9add-a428d02cd95b.png#averageHue=%233c4043&height=578&id=ShfC2&originHeight=578&originWidth=854&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=854)

<a name="Edfiv"></a>
## 常见错误处理
<a name="UDsjO"></a>
### Your shell has not been properly configured to use 'conda activate'
错误详情：
```python
$ conda activate modelscope

CommandNotFoundError: Your shell has not been properly configured to
 use 'conda activate'.
If using 'conda activate' from a batch script, change your
invocation to 'CALL conda.bat activate'.

To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - cmd.exe
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after runnin
g 'conda init'.
```

解决方案：根据自己的shell初始化脚本。

比如在CMD中执行：
```bash
conda init powershell
```

<a name="hPn7f"></a>
## 参考资料

- [Pipenv：新一代Python项目环境与依赖管理工具](https://zhuanlan.zhihu.com/p/37581807)
- [pip 与 Pipfile](https://blog.windrunner.me/python/pip.html) 





