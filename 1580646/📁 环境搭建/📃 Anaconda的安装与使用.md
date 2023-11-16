[Anaconda](https://www.anaconda.com/)指的是一个开源的Python发行版本，支持 Linux, Mac, Windows, 其包含了conda、Python等180多个科学包及其依赖项。因为包含了大量科学计算、数据分析的 Python 包，Anaconda 的下载文件比较大（约 531 MB），如果只需要某些包，或者需要节省带宽或存储空间，也可以使用Miniconda这个较小的发行版（仅包含conda和 Python）。

Anaconda 安装包可以到 [清华镜像站](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/) [https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D) 下载。

相关链接：

- [https://www.anaconda.com/](https://www.anaconda.com/)
- [https://docs.conda.io/en/latest/index.html](https://docs.conda.io/en/latest/index.html)
- [https://conda.io/projects/conda/en/latest/index.html](https://conda.io/projects/conda/en/latest/index.html)

<a name="d2b5b0b6"></a>
## conda包管理工具
conda 是 Anaconda 的包管理工具

<a name="6lEKn"></a>
### 查看conda版本
```bash
conda -V
```

<a name="84c1e457"></a>
### 查看已安装的包
```bash
conda list
```

<a name="03070d08"></a>
### 安装依赖包
使用以下命令安装需要的包：
```bash
conda install <packageName>
```

安装本地包：
```bash
conda install --use-local XXX.tar.bz2
```

<a name="d02bd59f"></a>
### 升级依赖包
使用以下命令升级已安装的包：
```bash
conda update <packageName>
conda update --all # 更新所有包
```

举例：
```bash
conda update conda # 升级conda(升级Anaconda前需要先升级conda)
conda update anaconda # 升级anaconda
conda update python # 升级python
conda update spyder # 升级spyder
```

<a name="uqtk3"></a>
## conda换源
首先使用以下命令生成一个 `~/.condarc` 文件 (位于用户目录下)
```bash
 conda config --set show_channel_urls yes
```
将文件改为以下内容：
```yaml
channels:
  - defaults
show_channel_urls: true
channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
也可以通过命令添加：
```bash
conda config --add channels - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
```

<a name="juMW2"></a>
## miniconda
[miniconda](https://docs.conda.io/en/latest/miniconda.html) 安装包比较大，包括了众多的科学计算库，若只需要conda进行包管理，可以安装miniconda，缩减不必要的包体积。

<a name="mkZxI"></a>
## conda常见错误
<a name="ajfH2"></a>
### CondaHTTPError: HTTP 000 CONNECTION FAILED for url ...
错误详情：
```
Collecting package metadata (repodata.json): failed

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch/repodata.json>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.
'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch'
```
解决方案：
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

conda config --set ssl_verify no
conda config --set show_channel_urls yes
```

<a name="HWq7R"></a>
### CondaSSLError: Encountered an SSL error
错误详情：
```
> conda create -p D:\Environment\stable-diffusion\stable-diffusion-webui\venv python=3.10 -y
Collecting package metadata (current_repodata.json): failed

CondaSSLError: Encountered an SSL error. Most likely a certificate verification issue.

Exception: HTTPSConnectionPool(host='repo.anaconda.com', port=443): Max retries exceeded with url: /pkgs/main/win-64/current_repodata.json (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
```
解决方案：关闭翻墙软件，包括Watt Toolkit。


<a name="Hlrg2"></a>
### pip is configured with locations that require TLS/SSL
错误详情：
```
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```

解决方案：<br />步骤一：[安装OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)<br />![1675831109261.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1675831116217-572856e4-8111-403d-b00e-16863fd2da01.png#averageHue=%23eae6dc&clientId=uc6eb378d-9aee-4&from=paste&height=542&id=u51ab743d&originHeight=542&originWidth=1534&originalType=binary&ratio=1&rotation=0&showTitle=false&size=113097&status=done&style=none&taskId=u73b22766-94b3-4dd1-b6bd-11c6e6e3378&title=&width=1534)

步骤二：添加环境变量
```
C:\Program Files\OpenSSL-Win64\bin
D:\Environment\scoop\apps\anaconda3\current\Scripts
D:\Environment\scoop\apps\anaconda3\current\Library
D:\Environment\scoop\apps\anaconda3\current\Library\bin
D:\Environment\scoop\apps\anaconda3\current\Lib\site-packages
D:\Environment\scoop\apps\anaconda3\current\Library\mingw-w64\bin
```
![1675831022690.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1675831034857-08abf1d8-2523-465e-aee1-21e1965a7f3d.png#averageHue=%23f4eeec&clientId=uc6eb378d-9aee-4&from=paste&height=562&id=u707848ed&originHeight=562&originWidth=531&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27145&status=done&style=none&taskId=u4e24fa1f-5ea5-466d-a0c6-fb2e39bb460&title=&width=531)


参考：[解决 pip is configured with locations that require TLS/SSL, however the ssl module in Python is not_orac-min的博客-CSDN博客](https://blog.csdn.net/qq_49580107/article/details/126380616)

<a name="QHNYa"></a>
### Solving environment: failed with initial frozen solve. Retrying with flexible solve.
错误详情：
```
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
```
解决方案：
```bash
conda config --set channel_priority flexible
```
其实这个不用管也行，他会自动尝试使用flexible解决。

<a name="fBn3u"></a>
### dll load failed while importing _ssl
错误详情：
```
import error: dll load failed while importing _ssl
```

解决方案：将完整的anconda路径添加到环境变量：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1677998458274-0240d31b-3694-49c4-8a26-7125aad46056.png#averageHue=%23f4f3f2&clientId=uad09b1e9-7f27-4&from=paste&height=569&id=ue5cc2fdc&originHeight=569&originWidth=531&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33828&status=done&style=none&taskId=u37b1bc4e-a637-4406-b838-52756e780d9&title=&width=531)

<a name="GvXRt"></a>
## Spyder
随 Anaconda 安装的还有 Spyder, 一个用于书写Python项目的IDE

如果是普通python安装，可以使用pip进行安装：
```
pip install spyder
```

![](https://cdn.nlark.com/yuque/0/2020/png/2213540/1596785420038-02508d9d-89b7-4e42-a640-be9b50f90902.png#averageHue=%23faf9f9&height=1017&id=lNiZL&originHeight=1017&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1920)



