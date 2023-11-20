![dart.webp](https://cdn.nlark.com/yuque/0/2020/webp/2213540/1608168492081-bfcf4d72-4d75-4372-8941-8a9b6a309c84.webp#align=left&display=inline&height=471&originHeight=1500&originWidth=1000&size=61492&status=done&style=none&width=314)
<a name="TpwMX"></a>
## 一、下载与安装
到如下地址下载最新版的Dart SDK安装即可：

- [Get the Dart SDK](https://dart.dev/get-dart)
- [Dart Windows 下载地址](http://www.gekorm.com/dart-windows/)

![image.png](https://cdn.nlark.com/yuque/0/2020/png/2213540/1608196478111-e13bcdb3-223f-47ce-89ef-4346800721ea.png#align=left&display=inline&height=22&originHeight=44&originWidth=597&size=13421&status=done&style=none&width=298.5)

如果是使用 `zip` 包解压的，需要手动将安装路径下的 `bin` 添加到环境变量。

<a name="5zqJO"></a>
## 二、第一个Dart程序
安装好Dart SDK后, 编写一个 `test.dart` 文件, 输入:
```dart
main() {
  print("Hello, World!");
}
```

执行 `dart test.dart`, 控制台输入 `Hello, World!`

<a name="HphEv"></a>
## 三、命令行工具
<a name="H1QO6"></a>
### dart
```bash
$ dart
A command-line utility for Dart development.

Usage: dart [<vm-flags>] <command|dart-file> [<arguments>]      

Global options:
-h, --help                 Print this usage information.        
-v, --verbose              Show additional command output.      
    --version              Print the Dart SDK version.
    --enable-analytics     Enable anonymous analytics.
    --disable-analytics    Disable anonymous analytics.

Available commands:
  analyze   Analyze the project's Dart code.
  compile   Compile Dart to various formats.
  create    Create a new project.
  format    Idiomatically format Dart source code.
  pub       Work with packages.
  run       Run a Dart program.
  test      Run tests in this package.

Run "dart help <command>" for more information about a command. 
See https://dart.dev/tools/dart-tool for detailed documentation.
```

<a name="bI65a"></a>
### pub
pub 是 Dart 的包管理工具。
```bash
$ pub
Pub is a package manager for Dart.

Usage: pub <command> [arguments]

Global options:
-h, --help             Print this usage information.
    --version          Print pub version.
    --[no-]trace       Print debugging information when an error occurs.    --verbosity        Control output verbosity.

          [all]        Show all output including internal tracing       
                       messages.
          [error]      Show only errors.
          [io]         Also show IO operations.
          [normal]     Show errors, warnings, and user messages.        
          [solver]     Show steps during version resolution.
          [warning]    Show only errors and warnings.

-v, --verbose          Shortcut for "--verbosity=all".

Available commands:
  cache       Work with the system cache.
  deps        Print package dependencies.
  downgrade   Downgrade the current package's dependencies to oldest    
              versions.
  get         Get the current package's dependencies.
  global      Work with global packages.
  logout      Log out of pub.dartlang.org.
  outdated    Analyze your dependencies to find which ones can be       
              upgraded.
  publish     Publish the current package to pub.dartlang.org.
  run         Run an executable from a package.
  upgrade     Upgrade the current package's dependencies to latest      
              versions.
  uploader    Manage uploaders for a package on pub.dartlang.org.       
  version     Print pub version.

Run "pub help <command>" for more information about a command.
See https://dart.dev/tools/pub/cmd for detailed documentation.
```

安装：
```bash
pub global activate webdev
pub global activate stagehand
```

Windows 注意将 `~\AppData\Roaming\Pub\Cache\bin` 或 `~\AppData\Local\Pub\Cache\bin` 添加到环境变量，以便使用pub安装的全局应用。

<a name="J74wQ"></a>
## 参考资料

- [Dart 官网](https://dart.dev/)
- [Dart 中文网](http://dart.goodev.org/)
- [DartPad](https://dartpad.dartlang.org/)
- [Dart Apis v2.4.1](https://api.dartlang.org/stable/2.4.1/index.html)<br />

