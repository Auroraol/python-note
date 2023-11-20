<a name="8dcb0465"></a>
## passwd && shadow

在 Linux 中，用户及密码文件位于 `/etc/passwd` 中，

```bash
$ cat -n /etc/passwd
     1	root:x:0:0:root:/root:/bin/bash
     2	bin:x:1:1:bin:/bin:/sbin/nologin
     3	daemon:x:2:2:daemon:/sbin:/sbin/nologin
     4	adm:x:3:4:adm:/var/adm:/sbin/nologin
     5	lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
     6	sync:x:5:0:sync:/sbin:/bin/sync
     7	shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
     8	halt:x:7:0:halt:/sbin:/sbin/halt
     9	mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    10	operator:x:11:0:operator:/root:/sbin/nologin
    11	games:x:12:100:games:/usr/games:/sbin/nologin
    12	ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
    13	nobody:x:99:99:Nobody:/:/sbin/nologin
    14	systemd-bus-proxy:x:999:998:systemd Bus Proxy:/:/sbin/nologin
    15	systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
    16	dbus:x:81:81:System message bus:/:/sbin/nologin
    17	polkitd:x:998:997:User for polkitd:/:/sbin/nologin
    18	tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
    19	sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    20	postfix:x:89:89::/var/spool/postfix:/sbin/nologin
    21	chrony:x:997:995::/var/lib/chrony:/sbin/nologin
    22	quanzaiyu:x:1000:1000:quanzaiyu:/home/quanzaiyu:/bin/bash
    23	dockerroot:x:996:993:Docker User:/var/lib/docker:/sbin/nologin
    24	ftper:x:1001:1001::/home/ftper:/bin/bash
    25	nginx:x:995:991:nginx user:/var/cache/nginx:/sbin/nologin
    26	mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false
    27	apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
    28	git:x:1002:1002::/home/git:/usr/bin/git-shell
```

<a name="47ab3dfd"></a>
### `/etc/passwd` 中的字段分析

- ACCOUNT：用户名
- PASSWORD：密码占位符
- UID：用户 ID
- GID：用户组 ID
- COMMAND：注释信息
- HOME DIR：用户家目录
- SHELL：用户的默认 shell

<a name="952ee8d6"></a>
### `/etc/shadow`

密码占位符，其值是 x，显然这不是真正的密码。真正的密码保存在哪里呢？在 /etc/shadow 文件中，此文件中保存的也不是明文密码，而是经过加密处理之后的密码。我们来看一下 `/etc/shadow` 中的内容（root only）：

```bash
$ cat /etc/shadow
     1	root:$6$gV.KVvRI/4wSk3fS$s3GXP7hk4qtqyrL1cichXmbfaJuxUd4Z/dW9GsgzYOGBNZU.eKyi.IhRyukZj0coReMxYQ8eYBuzS0bUDAKs/1::0:99999:7:::
     2	bin:*:17110:0:99999:7:::
     3	daemon:*:17110:0:99999:7:::
     4	adm:*:17110:0:99999:7:::
     5	lp:*:17110:0:99999:7:::
     6	sync:*:17110:0:99999:7:::
     7	shutdown:*:17110:0:99999:7:::
     8	halt:*:17110:0:99999:7:::
     9	mail:*:17110:0:99999:7:::
    10	operator:*:17110:0:99999:7:::
    11	games:*:17110:0:99999:7:::
    12	ftp:*:17110:0:99999:7:::
    13	nobody:*:17110:0:99999:7:::
```

<a name="bab42f4d"></a>
### 密码过期策略

阿里云会建议用户设置密码过期时间为 90 天, 如果觉得 3 个月改一次很烦, 可以设置为密码过期时间为无限期:

```bash
$ chage -l root
Last password change					: Aug 27, 2019
Password expires					: Nov 25, 2019
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 7
Maximum number of days between password change		: 90
Number of days of warning before password expires	: 7
chage -M 99999 root
$ chage -l root
Last password change					: Aug 27, 2019
Password expires					: never
Password inactive					: never
Account expires						: never
Minimum number of days between password change		: 7
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7
```

<a name="8cOZ0"></a>
## 参考资料

- [Linux(CentOS)用户修改密码有效期（chage 命令）](https://www.cnblogs.com/beyang/p/10116567.html)
