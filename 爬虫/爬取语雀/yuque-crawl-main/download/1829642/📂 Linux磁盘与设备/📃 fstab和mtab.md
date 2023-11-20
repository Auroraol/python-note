<a name="b55cf848"></a>
## /etc/fstab文件的作用

记录了计算机上硬盘分区的相关信息，启动 Linux 的时候，检查分区的 fsck 命令，和挂载分区的 mount 命令，都需要 fstab 中的信息，来正确的检查和挂载硬盘。

<a name="1b41736b"></a>
## /etc/mtab文件的作用

记载的是现在系统已经装载的文件系统，包括操作系统建立的虚拟文件等；而/etc/fstab是系统准备装载的。 每当 mount 挂载分区、umount 卸载分区，都会动态更新 mtab，mtab 总是保持着当前系统中已挂载的分区信息，fdisk、df 这类程序，必须要读取 mtab 文件，才能获得当前系统中的分区挂载情况。当然我们自己还可以通过读取/proc/mount也可以来获取当前挂载信息

<a name="f6eaf712"></a>
## 开机自动挂载

如果我们想实现开机自动挂载某设备，只要修改 `/etc/fstab` 文件即可。

文件挂载的配置文件：`/etc/fstab`

每行定义一个要挂载的文件系统；

格式例如：

| 要挂载的设备或伪文件系统 | 挂载点 | 文件系统类型 | 挂载选项 | 转储频率 | 自检次序 |
| --- | --- | --- | --- | --- | --- |
| UUID=6efb8a23-bae1-427c-ab10-3caca95250b1 | /boot | xfs | defaults | 0 | 0 |
| /dev/mapper/cl-root | / | xfs | defaults | 0 | 0 |
| UUID=01758f71-af40-4a56-8763-bd2272746772 | /boot | xfs | defaults | 0 | 0 |
| /dev/mapper/cl-swap | swap | swap | defaults | 0 | 0 |
| /dev/cdrom | /mnt/cdrom | auto | defaults | 0 | 0 |


- **要挂载的设备或伪文件系统** 设备文件、LABEL(LABEL="")、UUID(UUID="")、伪文件系统名称(proc, sysfs)
- **挂载点** 指定的文件夹
- **挂载选项** 可指定多项，用英文逗号分隔，如 auto, ro
   - auto 开机自动挂载
   - default 按照大多数永久文件系统的缺省值设置挂载定义
   - noauto 开机不自动挂载
   - nouser 只有超级用户可以挂载
   - ro 按只读权限挂载
   - rw 按可读可写权限挂载
   - user 任何用户都可以挂载
- **转储频率**
   - 0：不做备份
   - 1：每天转储
   - 2：每隔一天转储
- **自检次序**
   - 0：不自检
   - 1：首先自检；一般只有rootfs才用1；
