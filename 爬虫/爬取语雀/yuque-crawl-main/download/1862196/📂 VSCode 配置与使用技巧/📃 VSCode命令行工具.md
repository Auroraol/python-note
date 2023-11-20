`code` 命令可以直接打开一个VSCode窗口。如果找不到命令，将以下路径添加到PATH：
```bash
C:\Users\quanzaiyu\AppData\Local\Programs\Microsoft VS Code
```

<a name="nho4N"></a>
## 查看帮助
```bash
$ code -h
Visual Studio Code 1.50.1

Usage: code.exe [options][paths...]

To read output from another program, append '-' (e.g. 'echo Hello World | code.exe -')

Options
  -d --diff <file> <file>           Compare two files with each other.
  -a --add <folder>                 Add folder(s) to the last active window.
  -g --goto <file:line[:character]> Open a file at the path on the specified
                                    line and character position.
  -n --new-window                   Force to open a new window.
  -r --reuse-window                 Force to open a file or folder in an
                                    already opened window.
  --folder-uri <uri>                Opens a window with given folder uri(s)
  --file-uri <uri>                  Opens a window with given file uri(s)
  -w --wait                         Wait for the files to be closed before
                                    returning.
  --locale <locale>                 The locale to use (e.g. en-US or zh-TW).
  --user-data-dir <dir>             Specifies the directory that user data is
                                    kept in. Can be used to open multiple
                                    distinct instances of Code.
  -h --help                         Print usage.

Extensions Management
  --extensions-dir <dir>
      Set the root path for extensions.
  --list-extensions
      List the installed extensions.
  --show-versions
      Show versions of installed extensions, when using --list-extension.
  --category
      Filters installed extensions by provided category, when using --list-extension.
  --install-extension <extension-id[@version] | path-to-vsix>
      Installs or updates the extension. Use `--force` argument to avoid prompts. The identifier of an extension is always `${publisher}.${name}`. To install a specific version provide `@${version}`. For example: 'vscode.csharp@1.2.3'.
  --uninstall-extension <extension-id>
      Uninstalls an extension.
  --enable-proposed-api <extension-id>
      Enables proposed API features for extensions. Can receive one or more extension IDs to enable individually.

Troubleshooting
  -v --version                       Print version.
  --verbose                          Print verbose output (implies --wait).
  --log <level>                      Log level to use. Default is 'info'.
                                     Allowed values are 'critical', 'error',
                                     'warn', 'info', 'debug', 'trace', 'off'.
  -s --status                        Print process usage and diagnostics
                                     information.
  --prof-startup                     Run CPU profiler during startup
  --disable-extensions               Disable all installed extensions.
  --disable-extension <extension-id> Disable an extension.
  --sync <on> <off>                  Turn sync on or off
  --inspect-extensions <port>        Allow debugging and profiling of
                                     extensions. Check the developer tools for
                                     the connection URI.
  --inspect-brk-extensions <port>    Allow debugging and profiling of
                                     extensions with the extension host being
                                     paused after start. Check the developer
                                     tools for the connection URI.
  --disable-gpu                      Disable GPU hardware acceleration.
  --max-memory                       Max memory size for a window (in Mbytes).
  --telemetry                        Shows all telemetry events which VS code
                                     collects.
```

<a name="v6Bx0"></a>
## 打开项目
打开最近打开的项目：
```bash
code
```
在当前路径下打开项目：
```bash
code .
```
打开新窗口：
```bash
code -n
```
以指定的语言打开项目：
```bash
code --locale=en
code --locale=zh-cn
```

<a name="QWeQt"></a>
## 扩展目录
指定扩展路径：
```bash
code --extensions-dir %CD%
code --extensions-dir D:\Users\quanzaiyu\.vscode\extensions
```

禁用所有扩展：
```bash
code --disable-extensions .
```


<a name="pGdea"></a>
## 参考资料

- [command-line](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-line)
