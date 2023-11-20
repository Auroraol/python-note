<a name="b35d3983"></a>
## su

使用 su 命令可以切换到不同的用户进行登录:

```bash
[admin@node1 ~]$ su root
password:
[root@node1 ~]# exit
[admin@node1 ~]$
```

使用 exit 命令将退出此用户对话。

如果在上面的su命令与用户名之间加一个减号（-），这意味着完全切换到新的用户，即把环境变量信息也变更为新用户的相应信息，而不是保留原始的信息。强烈建议在切换用户身份时添加这个减号（-）。

```
[admin@node1 ~]$ su - root
```

<a name="sudo"></a>
## sudo

在普通用户时, 如果想要**临时获取root权限**来执行某条命令, 可以使用 `sudo` 前缀, 比如:

```bash
sudo vim /etc/hosts
```

<a name="4719334e"></a>
## sudo -Hu

如果想以某用户身份执行某些命令, 可以使用 `sudo -Hu [username] [command]`, 比如在 root 用户下使用 quanzaiyu 用户执行某条命令

```bash
sudo -Hu quanzaiyu mkdir -p /home/quanzaiyu/data
```

<a name="2b992488"></a>
## sudo 授权

个人用户的权限只可以在本home下有完整权限，其他目录要看别人授权。而经常需要root用户的权限，这时候sudo可以化身为root来操作。我记得我曾经sudo创建了文件，然后发现自己并没有读写权限，因为查看权限是root创建的。

这是未授权之前 quanzaiyu 用户使用 sudo 命令时提示

```
quanzaiyu is not in the sudoers file.  This incident will be reported.
```

新创建的用户并不能使用sudo命令，需要给他添加授权。

sudo命令的授权管理是在sudoers文件里的。可以看看sudoers:

```bash
$ whereis sudoers
sudoers: /etc/sudoers /etc/sudoers.d /usr/libexec/sudoers.so /usr/share/man/man5/sudoers.5.gz
```

找到这个文件位置之后再查看权限:

```bash
$ ls -l /etc/sudoers
-r--r----- 1 root root 4251 9月  25 15:08 /etc/sudoers
```

可以看到，只有只读的权限，如果想要修改的话，需要先添加w权限:

```bash
$ chmod -v u+w /etc/sudoers
mode of "/etc/sudoers" changed from 0440 (r--r-----) to 0640 (rw-r-----)
```

然后就可以添加内容了，在下面的一行下追加新增的用户:

```bash
$ vim /etc/sudoers
# Allow root to run any commands anywher
root    ALL=(ALL)       ALL
quanzaiyu  ALL=(ALL)       ALL  # 这个是新增的用户
```

wq保存退出，这时候要记得将写权限收回:

```bash
$ chmod -v u-w /etc/sudoers
mode of "/etc/sudoers" changed from 0640 (rw-r-----) to 0440 (r--r-----)
```

或 `chmod 0440 sudoers`

这时候使用新用户登录，使用sudo:

```bash
$ sudo cat /etc/passwd
[sudo] password for linuxidc:

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.
```

第一次使用会提示你，你已经化身超人，身负责任。而且需要输入密码才可以下一步。

如果不想需要输入密码，将最后一个 ALL 修改成 NOPASSWD: ALL

```
quanzaiyu ALL=(ALL)     NOPASSWD:ALL
```

也可以使用 `visudo` 命令直接编辑 sudoers 文件
