<a name="ffda6cb4"></a>
## 抽象语法树（AST）
抽象语法树（Abstract Syntax Tree，AST），或简称语法树（Syntax tree），是源代码语法结构的一种抽象表示。它以树状的形式表现编程语言的语法结构，树上的每个节点都表示源代码中的一种结构。之所以说语法是“抽象”的，是因为这里的语法并不会表示出真实语法中出现的每个细节。比如，嵌套括号被隐含在树的结构中，并没有以节点的形式呈现；而类似于 if-condition-then 这样的条件跳转语句，可以使用带有两个分支的节点来表示。(来源：百度百科)

<a name="55ae1504"></a>
## Babel 的处理步骤
Babel 的三个主要处理步骤分别是：** 解析（parse）**，**转换（transform）**，**生成（generate）**。.

<a name="aa357cb9"></a>
### 解析
解析步骤接收代码并输出 AST。 这个步骤分为两个阶段：**词法分析（Lexical Analysis）** 和 **语法分析（Syntactic Analysis）**。

**词法分析**<br />词法分析阶段把字符串形式的代码转换为令牌（tokens）流。

**语法分析**<br />语法分析阶段会把一个令牌流转换成 AST 的形式。 这个阶段会使用令牌中的信息把它们转换成一个 AST 的表述结构，这样更易于后续的操作。

<a name="ea20dffc"></a>
### 转换
转换步骤接收 AST 并对其进行遍历，在此过程中对节点进行添加、更新及移除等操作。 这是 Babel 或是其他编译器中最复杂的过程 同时也是插件将要介入工作的部分，这将是本手册的主要内容，因此让我们慢慢来。

<a name="4dfe7036"></a>
### 生成
代码生成步骤把最终（经过一系列转换之后）的 AST 转换成字符串形式的代码，同时创建源码映射（source maps）。

代码生成其实很简单：深度优先遍历整个 AST，然后构建可以表示转换后代码的字符串。

<a name="6c60f805"></a>
## AST 示例
有以下一段 JS 代码
```javascript
function square(n) {
  return n * n;
}
```

同样的程序可以表述为下面的列表：
```yaml
- FunctionDeclaration:
  - id:
    - Identifier:
      - name: square
  - params [1]
    - Identifier
      - name: n
  - body:
    - BlockStatement
      - body [1]
        - ReturnStatement
          - argument
            - BinaryExpression
              - operator: *
              - left
                - Identifier
                  - name: n
              - right
                - Identifier
                  - name: n
```

或是如下所示的 JavaScript Object（对象）：
```javascript
{
  type: "FunctionDeclaration",
  id: {
    type: "Identifier",
    name: "square"
  },
  params: [{
    type: "Identifier",
    name: "n"
  }],
  body: {
    type: "BlockStatement",
    body: [{
      type: "ReturnStatement",
      argument: {
        type: "BinaryExpression",
        operator: "*",
        left: {
          type: "Identifier",
          name: "n"
        },
        right: {
          type: "Identifier",
          name: "n"
        }
      }
    }]
  }
}
```

AST 的每一层都拥有相同的结构：
```javascript
{
  type: "FunctionDeclaration",
  id: {...},
  params: [...],
  body: {...}
}
{
  type: "Identifier",
  name: ...
}
{
  type: "BinaryExpression",
  operator: ...,
  left: {...},
  right: {...}
}
```

这样的每一层结构也被叫做 节点（Node）。 一个 AST 可以由单一的节点或是成百上千个节点构成。 它们组合在一起可以描述用于静态分析的程序语法。

每一个节点都有如下所示的接口（Interface）：
```typescript
interface Node {
  type: string;
}
```

字符串形式的 type 字段表示节点的类型（如： "FunctionDeclaration"，"Identifier"，或 "BinaryExpression"）。 每一种类型的节点定义了一些附加属性用来进一步描述该节点类型。

Babel 还为每个节点额外生成了一些属性，用于描述该节点在原始代码中的位置。
```javascript
{
  type: ...,
  start: 0,
  end: 38,
  loc: {
    start: {
      line: 1,
      column: 0
    },
    end: {
      line: 3,
      column: 1
    }
  },
  ...
}
```
每一个节点都会有 start，end，loc 这几个属性。

<a name="c1aac8b6"></a>
## 解析 AST
<a name="d6a65316"></a>
### Visitors（访问者）
当我们谈及“进入”一个节点，实际上是说我们在访问它们。

访问者是一个用于 AST 遍历的跨语言的模式。简单的说它们就是一个对象，定义了用于在一个树状结构中获取具体节点的方法。
```javascript
const visitor = {
  Identifier() {
    console.log("Called!");
  }
};
```
这是一个简单的访问者，把它用于遍历中时，每当在树中遇见一个 Identifier 的时候会调用 Identifier() 方法。

:::info
`Identifier() { ... }` 是 `Identifier: { enter() { ... } }` 的简写形式。
:::

```javascript
const visitor = {
  Identifier: {
    enter() {
      console.log("Entered!");
    },
    exit() {
      console.log("Exited!");
    }
  }
};
```

比如在下面一段代码中, `Entered!` 和 `Exited!` 会交替打印 4 次:
```javascript
function square(n) {
  return n * n;
}
```

其解析为 AST：
```javascript
- FunctionDeclaration
  - Identifier (id)
  - Identifier (params[0])
  - BlockStatement (body)
    - ReturnStatement (body)
      - BinaryExpression (argument)
        - Identifier (left)
        - Identifier (right)
```

<a name="1ad4ad1a"></a>
### Paths（路径）
Path 是一个对象，它表示两个节点之间的连接。

举例来说如果我们有以下的节点和它的子节点：
```javascript
{
  type: "FunctionDeclaration",
  id: {
    type: "Identifier",
    name: "square"
  },
  ...
}
```

将子节点 Identifier 表示为路径的话，看起来是这样的：
```javascript
{
  "parent": {
    "type": "FunctionDeclaration",
    "id": {...},
    ....
  },
  "node": {
    "type": "Identifier",
    "name": "square"
  }
}
```

同时它还有关于该路径的附加元数据：
```javascript
{
  "parent": {...},
  "node": {...},
  "hub": {...},
  "contexts": [],
  "data": {},
  "shouldSkip": false,
  "shouldStop": false,
  "removed": false,
  "state": null,
  "opts": null,
  "skipKeys": null,
  "parentPath": null,
  "context": null,
  "container": null,
  "listKey": null,
  "inList": false,
  "parentKey": null,
  "key": null,
  "scope": null,
  "type": null,
  "typeAnnotation": null
}
```

路径是对于节点在数中的位置以及其他各种信息的响应式表述。 当你调用一个方法更改了树的时候，这些信息也会更新。

<a name="60814acf"></a>
### Paths in Visitors（存在于访问者中的路径）
当你有一个拥有 Identifier() 方法的访问者时，你实际上是在访问路径而不是节点。 如此一来你可以操作节点的响应式表述（译注：即路径）而不是节点本身。
```javascript
const MyVisitor = {
  Identifier(path) {
    console.log("Visiting: " + path.node.name);
  }
};
```

比如有以下语句：
```javascript
a + b + c;
```

打印出：
```
Visiting: a
Visiting: b
Visiting: c
```

