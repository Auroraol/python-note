Linux用户分为：**属主**、**属组**(Group)、**其他**(other)，Linux系统中，预设的情況下，系统中所有的帐号与一般身份使用者，以及root的相关信息，都是记录在`/etc/passwd`文件中。每个人的密码则是记录在`/etc/shadow`文件下。 此外，所有的组群名称记录在`/etc/group`內！

linux文件的用户权限的分析图<br />![008.gif](https://cdn.nlark.com/yuque/0/2020/gif/2213540/1601198433774-14fed27a-7fd9-4f37-881d-23975399b4c4.gif#align=left&display=inline&height=214&originHeight=214&originWidth=583&size=4034&status=done&style=none&width=583)<br />例：rwx　rw-　r--  // 值 764

- **r** 读取属性	// 值＝4
- **w** 写入属性	// 值＝2
- **x** 执行属性	// 值＝1

第一个字符意义

- **-** 普通文件
- **d** 目录
- **l** 软链接
- **b** 块设备文件
- **c** 字符设备文件
- **p** 管道文件

例: `lrwxrwxrwx. 1 root root 1 Apr 1 01:18 d -> b`

<a name="8e502d00"></a>
## 用户特征码

操作系统时通过用户特征码来识别用户的。对于人类，我们识别用户是通过用户名，因为用户名（字符串）好记。而计算机觉得数字更好记一些，于是在创建用户时系统会为其分配一个唯一的特征码，用以识别该用户，这个特征码也叫**UID**。同样的，用户组也有特征码，叫做GID。

Linux 系统中，UID以如下的方式划分：

- 0 表示管理员（root）
- 1 - 999 表示系统用户
- 1000 - 65535 表示普通用户

注：不同的 Linux 发行版，这些数字可能不一样

UID是不能冲突的，而且管理员创建的普通用户的UID默认是从1000开始的（即使前面有闲置的号码）。

<a name="ac5b586c"></a>
## 创建用户

- `adduser username` 添加用户

在Linux系统中创建每个用户时，将自动创建一个与其同名的**基本用户组**，而且这个基本用户组只有该用户一个人。如果该用户以后被归纳入其他用户组，则这个其他用户组称之为**扩展用户组**。一个用户只有一个基本用户组，但是可以有多个扩展用户组，从而满足日常的工作需要。

在创建用户的时候, 可以指定用户目录、UID以及Shell解释器:

```bash
useradd -d /home/admin -u 8888 -s /sbin/nologin linuxprobe
```

:::info
`/sbin/nologin` 是终端解释器中的一员，与Bash解释器有着天壤之别。一旦用户的解释器被设置为nologin，则代表该用户不能登录到系统中
:::

使用 id 命令查看用户的uid及所属的组：

```bash
$ id admin
uid=1000(admin) gid=1000(admin) groups=1000(admin)
```

<a name="10991ce4"></a>
## 删除用户

`userdel` 命令用于删除用户，格式为 `userdel [选项] 用户名`。

参数如下:

- **-f**	强制删除用户
- **-r**	同时删除用户及用户家目录

```bash
userdel -r username # 删除一个用户 ( '-r' 排除主目录)
```

<a name="cd8b2fea"></a>
## 设置登录密码

`passwd` 命令用于修改用户密码、过期时间、认证信息等，格式为 `passwd [选项] [用户名]`。

普通用户只能使用passwd命令修改自身的系统密码，而root管理员则有权限修改其他所有人的密码。更酷的是，root管理员在Linux系统中修改自己或他人的密码时不需要验证旧密码，这一点特别方便。既然root管理员可以修改其他用户的密码，就表示完全拥有该用户的管理权限。

参数如下:

- **-l**	锁定用户，禁止其登录
- **-u**	解除锁定，允许用户登录
- **--stdin**	允许通过标准输入修改用户密码，如 `echo "NewPassWord" | passwd --stdin Username`
- **-d**	使该用户可用空密码登录系统
- **-e**	强制用户在下次登录时修改密码
- **-S**	显示用户的密码是否被锁定，以及密码所采用的加密算法名称

在修改用户密码时，通常都需要输入两次密码以进行确认，这在编写自动化脚本时将成为一个非常致命的缺陷。通过把管道符和passwd命令的--stdin参数相结合，我们可以用一条命令来完成密码重置操作：

```bash
$ echo "root" | passwd --stdin root
Changing password for user root.
passwd: all authentication tokens updated successfully.
```

<a name="19352b51"></a>
## 更改用户设置

`usermod` 命令用于修改用户的基本信息。usermod命令不允许你改变正在线上的使用者帐号名称。当usermod命令用来改变user id，必须确认这名user没在电脑上执行任何程序。

**修改用户名**

我们可以用 `-l` 参数修改用户帐号名称, 格式为

```bash
usermod -l newUserName userName
```

**修改组信息**

我们可以用 `-g` 参数修改用户的基本组ID，用 `-G` 参数修改用户扩展组ID。

```bash
usermod -G admins admin
$ id admin
uid=1000(admin) gid=1000(admin) groups=1000(admin),1002(admins)
```

以上命令, 将用户 admin 添加到组 admins 中, 使用 id 查看其修改后的状态

**锁定/解锁账号**

- **-L** 锁定用户，禁止其登录系统
- **-U** 解锁用户，允许其登录系统

```bash
usermod -L userName
usermod -U userName
```

**修改用户的shell**

`-s` 参数用于修改用户登入后所使用的shell

```bash
usermod -s /sbin/nologin ftpuser
```

<a name="4b0ab7ba"></a>
## 群组

使用 `groupadd groupname` 添加一个群组

<a name="w6UGS"></a>
## 参考资料

- [Linux 文件基本属性 - 菜鸟学院](https://www.runoob.com/linux/linux-file-attr-permission.html)
- [Linux 用户和用户组管理 - 菜鸟学院](https://www.runoob.com/linux/linux-user-manage.html)<br />
- [用户和工作组管理](http://man.linuxde.net/sub/%E7%94%A8%E6%88%B7%E5%92%8C%E5%B7%A5%E4%BD%9C%E7%BB%84%E7%AE%A1%E7%90%86)
- [Linux基础知识之用户和用户组以及 Linux 权限管理](https://www.linuxidc.com/Linux/2016-10/136251.htm)
- [CentOS 7中添加一个新用户并授权](https://www.linuxidc.com/Linux/2016-11/137549.htm)
