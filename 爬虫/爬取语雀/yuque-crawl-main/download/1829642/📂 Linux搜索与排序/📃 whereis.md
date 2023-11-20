**whereis** 命令用来定位指令的二进制程序、源代码文件和man手册页等相关文件的路径。

whereis命令只能用于程序名的搜索，而且只搜索二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s）。如果省略参数，则返回所有信息。

和[find](http://man.linuxde.net/find)相比，whereis 查找的速度非常快，这是因为linux系统会将系统内的所有文件都记录在一个数据库文件中，当使用 whereis 时，会从数据库中查找数据，而不是像find命令那样，通过遍历硬盘来查找，效率自然会很高。但是该数据库文件并不是实时更新，默认情况下时一星期更新一次，因此，我们在用whereis和locate 查找文件时，有时会找到已经被删除的数据，或者刚刚建立文件，却无法查找到，原因就是因为数据库文件没有被更新。

**常用选项**

- **-b** 只查找二进制文件
- **-m** 只查找说明文件
- **-s** 只查找原始代码文件
- **-f** 不显示文件名前的路径名称
- **-u** 查找不包含指定类型的文件

**示例**

```bash
$ whereis svn
svn: /usr/bin/svn /usr/local/svn /usr/share/man/man1/svn.1.gz
$ whereis -b svn
svn: /usr/bin/svn /usr/local/svn
$ whereis -m svn
svn: /usr/share/man/man1/svn.1.gz
$ whereis -s svn
svn:
```

说明：`whereis -m svn`查出说明文档路径，`whereis -s svn`找source源文件。

