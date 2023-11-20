相关站点：

- Docs: [Introduction | Manual | Deno](https://deno.land/manual)
- Modules:
   - [Third Party Modules | Deno](https://deno.land/x/)
   - [https://deno.land/std/](https://deno.land/std/)
- Bugs: [https://github.com/denoland/deno/issues](https://github.com/denoland/deno/issues)

<a name="mm0bg"></a>
## ✨ Deno简介
官方简介：
```javascript
A modern JavaScript and TypeScript runtime
```

Deno （/ˈdiːnoʊ/ ） 是一个建立在V8，Rust和Tokio之上的 JavaScript、TypeScript 和 WebAssembly 运行时，具有安全和出色的开发人员体验。

<a name="eTO56"></a>
## ✨ Deno的安装和基本用法
在Windows下，通过scoop安装deno：
```bash
scoop install deno # 安装
scoop update deno # 升级
```

在Windows下，通过choco安装deno：
```javascript
choco install deno
```

<a name="msR8C"></a>
### 检测安装版本
```javascript
$ deno --version
deno 1.16.4 (release, x86_64-pc-windows-msvc)
v8 9.7.106.15
typescript 4.4.2
```

<a name="Du7ua"></a>
### 查看帮助
```javascript
deno -h
```

<a name="etrHc"></a>
### 查看文档
要查看基础库的文档，使用`deno doc`。

示例：
```bash
$ deno doc https://deno.land/std/fs/move.ts
Defined in https://deno.land/std/fs/move.ts:20:0

async function move(src: string | URL, dest: string | URL, {overwrite}: MoveOptions)
  Moves a file or directory.

Defined in https://deno.land/std/fs/move.ts:64:0

function moveSync(src: string | URL, dest: string | URL, {overwrite}: MoveOptions)
  Moves a file or directory synchronously.
```

<a name="HafC3"></a>
### 创建项目
通过`deno init`可以创建一个deno项目：
```bash
$ deno init
✅ Project initialized
Run these commands to get started

// Run the program
deno run main.ts

// Run the program and watch for file changes
deno task dev

// Run the tests
deno test

// Run the benchmarks
deno bench

$ deno run main.ts
Add 2 + 3 = 5

$ deno test
Check file:///dev/main_test.ts
running 1 test from main_test.ts
addTest ... ok (6ms)

ok | 1 passed | 0 failed (29ms)
```

<a name="WLCWU"></a>
## ✨ 执行文件
<a name="Zq6pl"></a>
### 执行远程脚本
```javascript
deno run https://deno.land/std/examples/welcome.ts
```

<a name="lvXAm"></a>
### 执行控制台脚本
```javascript
deno eval "console.log('hello world')"
```

<a name="uWKN2"></a>
### 执行本地文件
执行本地文件，以下两种写法是等效的，默认工作目录就在当前目录：
```javascript
deno run ./index.js
deno run index.js 
```
注意：必须加上扩展名。

监视本地文件变化，添加`--watch`选项：
```typescript
deno run --watch main.ts
```

<a name="Kac3I"></a>
### 执行npm脚本
```typescript
❯ deno run --allow-env --allow-read npm:cowsay@1.5.0/cowthink What to eat?
 ______________
( What to eat? )
 --------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

<a name="AkNob"></a>
### REPL模式
进入REPL模式：
```javascript
deno
```
进入REPL模式之后，使用 `Ctrl+D`退出交互式命令行。

<a name="KTIhD"></a>
## ✨ 加载文件
<a name="P3xb5"></a>
### 加载本地文件
比如本地导出一个文件：
```typescript
export default {
  add(a: number, b: number): number {
    return a + b
  },
  PI: 3.14
}

export let a = 1
export let b = 2
```
本地导入此文件：
```typescript
import d, * as num from './components/export_demo.ts'

console.log(d.add(num.a, num.b))
console.log(d.PI)
```

编辑器可获取到完整的代码提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1672726217706-4ceaf6c1-4b78-40ea-a2bc-0bb39fa4c086.png#averageHue=%23252422&clientId=uc0eac5b5-0422-4&from=paste&height=140&id=u3abd33b5&originHeight=140&originWidth=723&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23668&status=done&style=none&taskId=u810955db-d0f0-46a9-a47f-c8f7dba0128&title=&width=723)

<a name="fgf71"></a>
### 加载远程文件
可以直接通过URL加载远程文件。

示例1：在控制台通过指定颜色输出
```javascript
import { red } from "https://deno.land/std@0.55.0/fmt/colors.ts";
console.log(red("hello world"));
```
执行：
```javascript
deno run main.ts
```

示例2：通过加载远程的基础库文件，获取拷贝文件的能力
```tsx
import { copy } from "https://deno.land/std@0.117.0/fs/copy.ts";

copy("package.json", "package_copy.json");
```
执行，注意需要添加权限：
```bash
deno run --allow-read --allow-write --unstable main.ts

# 或
deno run -A --unstable main.ts
```
参考：[https://deno.land/manual@v1.16.4/standard_library](https://deno.land/manual@v1.16.4/standard_library)


<a name="HZNq9"></a>
### 加载npm包
可以通过`npm:`前缀引入npm包：
```javascript
import chalk from "npm:chalk@5";

console.log(chalk.green("Hello!"));
```
执行：
```javascript
deno run main.ts
```

npm包引入格式：
```typescript
npm:<package-name>[@<version-requirement>][/<sub-path>]
```

<a name="rq20z"></a>
## ✨ 配置
<a name="hACUf"></a>
### 配置文件
deno的默认配置文件为 `deno.jsonc`或 `deno.json`，示例如下：
```json
{
  "tasks": {
    "dev": "deno run --watch main.ts"
  },
  "compilerOptions": {
    "allowJs": true,
    "lib": [
      "deno.window"
    ],
    "strict": true
  },
  "importMap": "import_map.json",
  "lint": {
    "files": {
      "include": [
        "src/"
      ],
      "exclude": [
        "src/testdata/"
      ]
    },
    "rules": {
      "tags": [
        "recommended"
      ],
      "include": [
        "ban-untagged-todo"
      ],
      "exclude": [
        "no-unused-vars"
      ]
    }
  },
  "fmt": {
    "files": {
      "include": [
        "src/"
      ],
      "exclude": [
        "src/testdata/"
      ]
    },
    "options": {
      "useTabs": true,
      "lineWidth": 80,
      "indentWidth": 4,
      "singleQuote": true,
      "proseWrap": "preserve"
    }
  },
  "test": {
    "files": {
      "include": [
        "src/"
      ],
      "exclude": [
        "src/testdata/"
      ]
    }
  }
}
```

从 Deno v1.18 起如果不是默认的配置文件，可以通过 `--config path/to/file.json`指定。

从 Deno v1.22 起可以通过`--no-config` 不指定配置文件。

<a name="p66e7"></a>
### 权限
默认情况下, Deno 是安全的。因此，除非显式的启用它，否则 Deno 模块不具备访问文件、网络或环境的权限。当需要访问安全敏感区域或功能，需要在命令行上显示的授予 deno 进程相应的权限。

权限清单如下：

- `-A`, `--allow-all`: 启用所有权限。这将禁用所有安全性。
- `--allow-env`: 启用环境访问权限, 例如获取和设置环境变量。
- `--allow-hrtime`: 启用高分辨率时间测量权限。高分辨率时间测量可用于定时攻击和指纹识别。
- `--allow-net=\<allow-net>`: 启用网络访问权限。您可以指定一个可选的, 用逗号分隔的域名列表, 以提供可访问的域名白名单。
- `--allow-plugin`: 启用加载插件功能权限。请注意该功能不稳定。
- `--allow-read=\<allow-read>`: 启用文件系统读取权限。您可以指定一个可选的, 用逗号分隔的目录或文件列表, 以提供允许使用文件系统读取权限的白名单。
- `--allow-run`: 启用运行子进程权限。请注意, 子进程不是在沙箱中运行的, 因此没有与 Deno 进程相同的安全限制。请谨慎使用。
- `--allow-write=\<allow-write>`: 启用文件系统写入权限。您可以指定一个可选的, 用逗号分隔的目录或文件列表, 以提供允许使用文件系统写入权限的白名单。

<a name="XwU40"></a>
#### 权限白名单
可以在具体的权限后添加权限白名单，如果有多个，可以使用逗号`,`分割，比如：
```javascript
deno run --allow-read=/etc https://deno.land/std/examples/cat.ts /etc/passwd // Linux、MacOS
deno run --allow-read=D:\Projects https://deno.land/std/examples/cat.ts ./index.html // Windows
deno run --allow-net=github.com,deno.land fetch.ts
```

<a name="mbbnf"></a>
#### 控制台权限提示
在最新版的deno（笔者2023-1-1书写，版本为1.29.1），在未指定权限的情况下会在控制台提示是否启用权限，输入`y`即可：
```bash
❯ deno run main.ts
⚠️  ┌ Deno requests read access to <CWD>.
├ Requested by `Deno.cwd()` API
├ Run again with --allow-read to bypass this prompt.
└ Allow? [y/n] (y = yes, allow; n = no, deny) >
```

<a name="l1KSI"></a>
#### 读写权限
涉及到需要访问文件系统的程序，需要添加`--allow-read`（读）、`--allow-write`（写）
```typescript
import { copy } from "https://deno.land/std@0.117.0/fs/copy.ts";

copy("package.json", "package_copy.json");
```
运行：
```bash
deno run --allow-read --allow-write --unstable main.ts

# 或
deno run -A --unstable main.ts
```

<a name="pzmih"></a>
#### 网络权限
涉及到需要访问网络的程序，需要添加`--allow-net`
```javascript
const result = await fetch("https://deno.land/");
```

运行：
```bash
# Multiple hostnames, all ports allowed
deno run --allow-net=github.com,deno.land fetch.js

# A hostname at port 80:
deno run --allow-net=deno.land:80 fetch.js

# An ipv4 address on port 443
deno run --allow-net=1.1.1.1:443 fetch.js

# A ipv6 address, all ports allowed
deno run --allow-net=[2606:4700:4700::1111] fetch.js

# Allow net calls to any hostname/ip
deno run --allow-net fetch.js
```


<a name="AzPok"></a>
#### 运行权限
涉及到通过子进程执行命令的程序，需要添加`--allow-run`
```javascript
const proc = Deno.run({ cmd: ["whoami"] });
```

运行：
```bash
# Allow only spawning a `whoami` subprocess:
deno run --allow-run=whoami run.js

# Allow running any subprocess:
deno run --allow-run run.js
```

<a name="NjHjj"></a>
#### 环境变量权限
涉及到获取环境变量的程序，需要添加`--allow-env`
```javascript
Deno.env.get("HOME");
```

运行：
```bash
# Allow all environment variables
deno run --allow-env env.js

# Allow access to only the HOME env var
deno run --allow-env=HOME env.js
```

<a name="x4gmp"></a>
### 导入映射
Deno可以通过 CLI 并使用 `--importmap=<FILE>` 来导入映射。

一个引入deno标准库的示例：
```javascript
{
  "imports": {
     "fmt/": "https://deno.land/std@0.55.0/fmt/"
  }
}
```
在程序中只需要使用map指定的别名即可：
```javascript
import { red } from "fmt/colors.ts";
console.log(red("hello world"));
```
这是一个不稳定的特性，所以执行的时候需要加上`--unstable`选项：
```javascript
deno run --allow-net --importmap=import_map.json --unstable index.ts
```

---


一个引入lodash的示例：
```json
{
  "imports": {
     "lodash": "https://cdn.skypack.dev/lodash"
  }
}
```
引入lodash：
```javascript
import _ from "lodash";

console.log(_.add(1, 2))
```
运行：
```javascript
deno run --import-map ./import_map.json index.ts
```

---


在最新的deno中（截止2023-1-1已更新到1.29.1），在`deno.jsonc`中指定了`importMap`，则可以不需要添加` --import-map`选项，可直接运行 `deno run index.ts`。

<a name="Zk3WH"></a>
### TypeScript类型定义
有一些包自带类型定义，可以直接引入：
```typescript
import chalk from "npm:chalk@5";
```

有一些包，需要通过引入[类型定义文件](https://www.typescriptlang.org/docs/handbook/2/type-declarations.html#definitelytyped--types)获取完整的类型定义，通过注释`[@deno-types](https://deno.land/manual@v1.29.1/advanced/typescript/types)`加载：
```typescript
// @deno-types="npm:@types/express@^4.17"
import express from "npm:express@^4.17";
```


<a name="khsjf"></a>
## ✨ 生命周期
官方文档：[program_lifecycle](https://deno.land/manual/runtime/program_lifecycle)

主文件：
```typescript
import "./imported.ts";

const handler = (e: Event): void => {
  console.log(`got ${e.type} event in event handler (main)`);
};

globalThis.addEventListener("load", handler);

globalThis.addEventListener("beforeunload", handler);

globalThis.addEventListener("unload", handler);

globalThis.onload = (e: Event): void => {
  console.log(`got ${e.type} event in onload function (main)`);
};

globalThis.onbeforeunload = (e: Event): void => {
  console.log(`got ${e.type} event in onbeforeunload function (main)`);
};

globalThis.onunload = (e: Event): void => {
  console.log(`got ${e.type} event in onunload function (main)`);
};

console.log("log from main script");
```
引入的文件：
```typescript
const handler = (e: Event): void => {
  console.log(`got ${e.type} event in event handler (imported)`);
};

globalThis.addEventListener("load", handler);
globalThis.addEventListener("beforeunload", handler);
globalThis.addEventListener("unload", handler);

globalThis.onload = (e: Event): void => {
  console.log(`got ${e.type} event in onload function (imported)`);
};

globalThis.onbeforeunload = (e: Event): void => {
  console.log(`got ${e.type} event in onbeforeunload function (imported)`);
};

globalThis.onunload = (e: Event): void => {
  console.log(`got ${e.type} event in onunload function (imported)`);
};

console.log("log from imported script");
```

运行结果：
```typescript
$ deno run index.ts
log from imported script
log from main script
got load event in event handler (imported)
got load event in onload function (main)
got load event in event handler (main)
got beforeunload event in event handler (imported)
got beforeunload event in onbeforeunload function (main)
got beforeunload event in event handler (main)
got unload event in event handler (imported)
got unload event in onunload function (main)
got unload event in event handler (main)
```

可以看出：

1. 先执行非生命周期中的程序代码
2. 生命周期执行顺序：load -> beforeunload -> unload
3. 同一个生命周期的执行顺序：引入文件 -> 主文件的on[event]方法 -> 主文件的addEventListener
4. 引入文件的 on[event] 不会被执行

<a name="ICjc3"></a>
## ✨ 应用
<a name="SiLkL"></a>
### 开启HTTP服务
<a name="iUlYA"></a>
#### 开启本地服务
编写一个脚本，开启本地服务：
```javascript
const hostname = "0.0.0.0";
const port = 8080;
const listener = Deno.listen({ hostname, port });
console.log(`Listening on ${hostname}:${port}`);
for await (const conn of listener) {
  Deno.copy(conn, conn);
}
```
或者获取通过加载远程库开启服务：
```javascript
import { serve } from "https://deno.land/std@0.118.0/http/server.ts";

console.log("http://localhost:8000/");
serve((req) => new Response("Hello World\n"), { addr: ":8000" });
```
要运行此脚本，需要携带 `--allow-net`参数以开启访问网络的权限：
```javascript
deno run --allow-net index.js
```
如果不携带此参数，则控制台报错：
```javascript
PermissionDenied: Requires net access to "0.0.0.0:8000", run again with the --allow-net flag
```

以上示例是Deno官方示例的一个变更：
```javascript
deno run --allow-net https://deno.land/std/examples/echo_server.ts
```

<a name="XGYgV"></a>
#### 获取远程资源
deno支持直接通过fetch请求远程资源（deno支持根级async...await）：
```javascript
const url = Deno.args[0];
const res = await fetch(url);

const body = new Uint8Array(await res.arrayBuffer());
await Deno.stdout.write(body);
```
其中`Deno.stdout.write()`跟`console.log()`有相同的效果。

运行，通过参数传入url，比如获取百度首页的HTML：
```bash
$ deno run --allow-net index.js https://www.baidu.com
<html>
<head>
        <script>
                location.replace(location.href.replace("https://","http://"));
        </script>
</head>
<body>
        <noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>
```
其实这是deno官方的一个示例：
```bash
deno run --allow-net https://deno.land/std/examples/curl.ts https://www.baidu.com
```

<a name="pS8mw"></a>
#### 通过第三方库创建服务
比如通过express创建HTTP服务：
```typescript
// @deno-types="npm:@types/express@^4.17"
import express from "npm:express@^4.17";
const app = express();

app.get("/", (req, res) => {
  res.send("Hello World");
});

app.listen(3000);
console.log("listening on http://localhost:3000/");
```
运行：
```bash
$ deno run --A main.ts
listening on http://localhost:3000/
```

<a name="ByVkl"></a>
### 读取文件
可以通过 `Deno.open` 打开本地文件：
```javascript
const filenames = Deno.args;
for (const filename of filenames) {
    const file = await Deno.open(filename);
    await Deno.copy(file, Deno.stdout);
    file.close();
}
```
执行的时候必须携带`--allow-read`参数，以开启访问本地文件的权限，否则将报错。
```javascript
deno run --allow-read ./index.js index.html
```
其实这也是Deno官方的一个示例，执行结果同：
```bash
deno run --allow-read https://deno.land/std/examples/cat.ts ./index.html
```

<a name="wP94a"></a>
### 获取环境变量
<a name="wYv2d"></a>
#### 系统环境变量
设置和获取系统环境变量：
```typescript
Deno.env.set("FIREBASE_API_KEY", "examplekey123");
Deno.env.set("FIREBASE_AUTH_DOMAIN", "firebasedomain.com");

console.log(Deno.env.get("FIREBASE_API_KEY")); // examplekey123
console.log(Deno.env.get("FIREBASE_AUTH_DOMAIN")); // firebasedomain.com
```
运行：
```typescript
deno run --allow-env index.ts
```

<a name="AYkwd"></a>
#### .env 文件环境变量
比如有以下`.env`文件：
```typescript
PASSWORD=Geheimnis
```
读取`.env`文件：
```typescript
import { load } from "https://deno.land/std@0.170.0/dotenv/mod.ts";

const configData = await load();
const password = configData["PASSWORD"];

console.log(password); // "Geheimnis"
```
运行：
```bash
deno run --allow-env --allow-read index.ts
```
注意：因为是读取`.env`文件，所以需要添加`--allow-read`。

<a name="fLo4y"></a>
### 获取命令行参数
<a name="FR8vk"></a>
#### 通过Deno.args获取命令行参数
[Deno.args](https://deno.land/api?s=Deno.args)
```typescript
const args = Deno.args;

console.log(args)
```
运行：
```typescript
deno run index.ts 1 2 3
```
返回：
```typescript
[ "1", "2", "3" ]
```

<a name="C06yr"></a>
#### 通过std/flags/mod获取命令行参数
编写程序，需要引入[/flags/mod.ts](https://deno.land/std@0.170.0/flags/mod.ts)，读取输入时的参数
```typescript
import { parse } from "https://deno.land/std@0.170.0/flags/mod.ts";

console.dir(parse(Deno.args));
```
运行：
```typescript
deno run -A index.ts -x 1 -y 2 -a --beep=boop foo bar baz
```
同运行官方示例中：
```typescript
deno run https://deno.land/std/examples/flags.ts -x 1 -y 2 -a --beep=boop foo bar baz
```
返回：
```typescript
{
  _: [ "foo", "bar", "baz" ],
  x: 1,
  y: 2,
  a: true,
  beep: "boop"
}
```
<a name="eoj0N"></a>
#### 
<a name="BuEdb"></a>
## ✨ 运行时API

- [https://doc.deno.land/deno/stable](https://doc.deno.land/deno/stable)

<a name="emgz7"></a>
## ✨ 标准库

- [https://github.com/denoland/deno_std](https://github.com/denoland/deno_std)
- [https://deno.land/std](https://deno.land/std)

<a name="qrbqb"></a>
### /std/node
[/std/node](https://deno.land/std/node/) 移植了一套兼容Node.js的标准库。

参考文档：[https://deno.land/manual/node/std_node](https://deno.land/manual@v1.29.1/node/std_node)

<a name="fyik8"></a>
### /fmt/color
[/fmt/color](https://deno.land/std/fmt/colors.ts)用于控制控制台颜色。

示例：
```javascript
import { bgBlue, bgRgb24, bgRgb8, bold, italic, red, rgb24, rgb8 } from "https://deno.land/std@0.170.0/fmt/colors.ts";

console.log(bgBlue(italic(red(bold("Hello, World!")))));

// also supports 8bit colors
console.log(rgb8("Hello, World!", 42));

console.log(bgRgb8("Hello, World!", 42));

// and 24bit rgb
console.log(rgb24("Hello, World!", {
  r: 41,
  g: 42,
  b: 43,
}));

console.log(bgRgb24("Hello, World!", {
  r: 41,
  g: 42,
  b: 43,
}));
```
输出：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1672795285865-afad444b-c66c-4054-87ca-a355b833133e.png#averageHue=%23252423&clientId=u97d76201-c759-4&from=paste&height=171&id=u40f6c07f&originHeight=171&originWidth=631&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22941&status=done&style=none&taskId=u6653a419-f7b4-4c8f-8fad-7b58f9e6ee3&title=&width=631)

<a name="jsVBx"></a>
### /fmt/printf
[/fmt/printf](https://deno.land/std/fmt/printf.ts)格式化输出语句。

- printf 直接输出格式化字符串
- sprintf 返回格式化字符串

示例：
```javascript
import { printf, sprintf } from "https://deno.land/std@0.170.0/fmt/printf.ts";

printf('我叫%s，今年%d岁.', 'quanzaiyu', 18)
const str: string = sprintf('我叫%s，今年%d岁.', 'quanzaiyu', 18)

console.log('\n')
console.log(str)
```
输出：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1672795878838-31d02b9e-2631-49d2-be2a-75a64b7e506a.png#averageHue=%231f1d1c&clientId=u97d76201-c759-4&from=paste&height=124&id=ud5fc99e9&originHeight=124&originWidth=651&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24586&status=done&style=none&taskId=ud0de1b83-c78e-4422-a955-d9f73a13726&title=&width=651)

<a name="XadWe"></a>
## ✨ 在VSCode中进行deno开发
VSCode插件：[Deno - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=denoland.vscode-deno)

<a name="ZkEqk"></a>
### 完整的代码提示
可在编辑器中获得完整的代码提示：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1672725322001-c593e5b1-909f-4f14-b271-dc757be89946.png#averageHue=%23252322&clientId=uc0eac5b5-0422-4&from=paste&height=226&id=u7f15ee88&originHeight=226&originWidth=1217&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54670&status=done&style=none&taskId=u8d222646-0d87-464c-a961-3c9db1b774c&title=&width=1217)

<a name="Rmv82"></a>
### 缓存npm包
如果在编辑器中报找不到npm包，如图所示：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/2213540/1672725137720-7e96fe95-045a-4f2c-a76e-6129af84fa26.png#averageHue=%2392aaa1&clientId=uc0eac5b5-0422-4&from=paste&height=144&id=ue0b0fcd0&originHeight=144&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24751&status=done&style=none&taskId=ud3d6d4d7-fe7c-4fb9-8b2a-c5cbb38b011&title=&width=860)<br />可以通过`deno cache`命令缓存指定的包即可：
```json
deno cache npm:chalk@5
```

或者直接缓存 `main.ts`，这样所有引入的npm包也会被缓存。
```bash
deno cache main.ts
```

<a name="H3maF"></a>
## 参考资料

- [Deno手册 - 语雀](https://www.yuque.com/u239523/gurg7y)
- [Deno教程 - w3cschool](https://www.w3cschool.cn/denohandbook/denohandbook-w1pm37oa.html)



