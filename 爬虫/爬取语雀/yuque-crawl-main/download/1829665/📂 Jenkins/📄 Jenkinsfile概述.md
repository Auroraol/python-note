- [流水线语法](https://www.jenkins.io/zh/doc/book/pipeline/syntax/)

<a name="xFEOA"></a>
## 声明式流水线
声明式 Jenkinsfile (Declarative Pipeline)示例：
```groovy
pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}

```

所有有效的声明式流水线必须包含在一个 pipeline 块中, 比如:
```yaml
pipeline { /* insert Declarative Pipeline here */ }
```

在声明式流水线中有效的基本语句和表达式遵循与 [Groovy的语法](http://groovy-lang.org/syntax.html)同样的规则， 有以下例外:

- 流水线顶层必须是一个 block, 特别地: `pipeline { }`
- 没有分号作为语句分隔符，，每条语句都必须在自己的行上。
- 块只能由 [节段](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#declarative-sections), [指令](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#declarative-directives), [步骤](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#declarative-steps), 或赋值语句组成。 
- 属性引用语句被视为无参方法调用。 例如, `input`被视为 `input()`

<a name="mDAjh"></a>
### agent（代理）
`agent` （代理）部分指定了整个流水线或特定的部分, 将会在Jenkins环境中执行的位置，这取决于 `agent` 区域的位置。该部分必须在 `pipeline` 块的顶层被定义, 但是 stage 级别的使用是可选的。

| 必填 | 是 |
| --- | --- |
| 参数 | any/none/label/docker/dockerfile |
| 允许的位置 | 在顶层的 `pipeline`块或每一个`stage`块 |


<a name="E4hI6"></a>
#### 可用代理
为了支持作者可能有的各种各样的用例流水线, `agent` 部分支持一些不同类型的参数。这些参数应用在`pipeline`块的顶层, 或 `stage` 指令内部。

-  **any**<br />在任何可用的代理上执行流水线或阶段。例如: `agent any` 
-  **none**<br />当在 `pipeline` 块的顶部没有全局代理， 该参数将会被分配到整个流水线的运行中并且每个 `stage` 部分都需要包含他自己的 `agent` 部分。比如: `agent none` 
-  **label**<br />在提供了标签的 Jenkins 环境中可用的代理上执行流水线或阶段。 例如: `agent { label 'my-defined-label' }` 
-  **node**<br />`agent { node { label 'labelName' } }` 和 `agent { label 'labelName' }` 一样, 但是 `node` 允许额外的选项 (比如 `customWorkspace` )。 
-  **docker**<br />使用给定的容器执行流水线或阶段。该容器将在预置的 [node](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#../glossary#node) 上，或在匹配可选定义的`label` 参数上，动态的供应来接受基于Docker的流水线。 `docker` 也可以选择的接受 `args` 参数，该参数可能包含直接传递到 `docker run` 调用的参数, 以及 `alwaysPull` 选项, 该选项强制 `docker pull` ，即使镜像名称已经存在。 比如: `agent { docker 'maven:3-alpine' }` 或
```groovy
pipeline {
    agent {
        docker {
            image 'maven:3-alpine'
            label 'my-defined-label'
            args  '-v /tmp:/tmp'
        }
    }
    stages {
        stage('Example Build') {
            steps {
                sh 'mvn -B clean verify'
            }
        }
    }
}
```

-  **dockerfile**<br />执行流水线或阶段, 使用从源代码库包含的 `Dockerfile` 构建的容器。为了使用该选项， `Jenkinsfile` 必须从多个分支流水线中加载, 或者加载 "Pipeline from SCM." 通常，这是源代码仓库的根目录下的 `Dockerfile` : `agent { dockerfile true }`. 如果在另一个目录下构建 `Dockerfile` , 使用 `dir` 选项: `agent { dockerfile {dir 'someSubDir' } }`。如果 `Dockerfile` 有另一个名称, 你可以使用 `filename` 选项指定该文件名。你可以传递额外的参数到 `docker build ...` 使用 `additionalBuildArgs` 选项提交, 比如 `agent { dockerfile {additionalBuildArgs '--build-arg foo=bar' } }`。 例如, 一个带有 `build/Dockerfile.build` 的仓库,期望一个构建参数 `version`:
```groovy
agent {
    // Equivalent to 
    // docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile.build'
        dir 'build'
        label 'my-defined-label'
        additionalBuildArgs  '--build-arg version=1.0.2'
    }
}
```

<a name="D6l7v"></a>
#### 常见选项
有一些应用于两个或更多 `agent` 的实现的选项。他们不被要求，除非特别规定。

-  **label**<br />一个字符串。该标签用于运行流水线或个别的 `stage`。该选项对 `node`, `docker` 和 `dockerfile` 可用, `node`要求必须选择该选项。 
-  **customWorkspace**<br />一个字符串。在自定义工作区运行应用了 `agent` 的流水线或个别的 `stage`, 而不是默认值。 它既可以是一个相对路径, 在这种情况下，自定义工作区会存在于节点工作区根目录下, 或者一个绝对路径。比如:
```groovy
agent {
    node {
        label 'my-defined-label'
        customWorkspace '/some/other/path'
    }
}
```
该选项对 `node`, `docker` 和 `dockerfile` 有用 。 

-  **reuseNode**<br />一个布尔值, 默认为false。 如果是true, 则在流水线的顶层指定的节点上运行该容器, 在同样的工作区, 而不是在一个全新的节点上。这个选项对 `docker` 和 `dockerfile` 有用, 并且只有当 使用在个别的 `stage` 的 `agent` 上才会有效。 

<a name="o0jiQ"></a>
#### 阶段级别的 `agent` 部分
```groovy
pipeline {
    agent none 
    stages {
        stage('Example Build') {
            agent { docker 'maven:3-alpine' } 
            steps {
                echo 'Hello, Maven'
                sh 'mvn --version'
            }
        }
        stage('Example Test') {
            agent { docker 'openjdk:8-jre' } 
            steps {
                echo 'Hello, JDK'
                sh 'java -version'
            }
        }
    }
}
```

1. 在流水线顶层定义 `agent none`确保 [an Executor](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#../glossary#executor) 没有被分配。 使用 `agent none` 也会强制 `stage`部分包含他自己的 `agent`部分。
2. 使用镜像在一个新建的容器中执行该阶段的该步骤。
3. 使用一个与之前阶段不同的镜像在一个新建的容器中执行该阶段的该步骤。

<a name="z4Vc5"></a>
### post（后触发器）
`post` 部分定义一个或多个 [steps](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#declarative-steps) ，这些阶段根据流水线或阶段的完成情况而 运行(取决于流水线中 `post` 部分的位置). `post` 支持以下 [post-condition](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#post-conditions) 块中的其中之一: `always`, `changed`, `failure`, `success`, `unstable`, 和 `aborted`。这些条件块允许在 `post` 部分的步骤的执行取决于流水线或阶段的完成状态。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块或每一个`stage`块 |


**条件：**

-  `always`<br />无论流水线或阶段的完成状态如何，都允许在 `post` 部分运行该步骤。 
-  `changed`<br />只有当前流水线或阶段的完成状态与它之前的运行不同时，才允许在 `post` 部分运行该步骤。 
-  `failure`<br />只有当前流水线或阶段的完成状态为"failure"，才允许在 `post` 部分运行该步骤, 通常web UI是红色。 
-  `success`<br />只有当前流水线或阶段的完成状态为"success"，才允许在 `post` 部分运行该步骤, 通常web UI是蓝色或绿色。 
-  `unstable`<br />只有当前流水线或阶段的完成状态为"unstable"，才允许在 `post` 部分运行该步骤, 通常由于测试失败,代码违规等造成。通常web UI是黄色。 
-  `aborted`<br />只有当前流水线或阶段的完成状态为"aborted"，才允许在 `post` 部分运行该步骤, 通常由于流水线被手动的aborted。通常web UI是灰色。 

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post { 
        always { 
            echo 'I will always say Hello again!'
        }
    }
}
```
按照惯例, `post`部分应该放在流水线的底部。

<a name="mEW40"></a>
### stages（阶段聚合）
包含一系列一个或多个 [stage](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#stage) 指令, `stages` 部分是流水线描述的大部分"work" 的位置。 建议 `stages` 至少包含一个 [stage](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#stage) 指令用于连续交付过程的每个离散部分,比如构建, 测试, 和部署。

| 必填 | 是 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块中，仅出现一次 |


示例：
```groovy
pipeline {
    agent any
    stages { 
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```
`stages`部分通常会遵循诸如 `agent`, `options`等的指令。

<a name="dxZzm"></a>
#### stage（阶段）
`stage` 指令在 `stages` 部分进行，应该包含一个 实际上, 流水巷所做的所有实际工作都将封装进一个或多个 `stage` 指令中。

| 必填 | 是（至少一次） |
| --- | --- |
| 参数 | _阶段名字（string）_ |
| 允许的位置 | 在 `stages`块中 |


示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

<a name="mDdMS"></a>
#### steps（步骤）
`steps` 部分在给定的 `stage` 指令中执行的定义了一系列的一个或多个[steps](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#declarative-steps)。

| 必填 | 是 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在每个 `stage` 块中 |


示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps { 
                echo 'Hello World'
            }
        }
    }
}
```
`steps`部分必须包含一个或多个步骤。

<a name="Z8bhd"></a>
### environment（环境变量）
`environment` 指令制定一个 键-值对序列，该序列将被定义为所有步骤的环境变量，或者是特定于阶段的步骤， 这取决于 `environment` 指令在流水线内的位置。

该指令支持一个特殊的助手方法 `credentials()` ，该方法可用于在Jenkins环境中通过标识符访问预定义的凭证。对于类型为 "Secret Text"的凭证, `credentials()` 将确保指定的环境变量包含秘密文本内容。对于类型为 "Standard username and password"的凭证, 指定的环境变量指定为 `username:password` ，并且两个额外的环境变量将被自动定义 :分别为 `MYVARNAME_USR` 和 `MYVARNAME_PSW` 。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块或每一个`stage`块 |


示例：
```groovy
pipeline {
    agent any
    environment { 
        CC = 'clang'
    }
    stages {
        stage('Example') {
            environment {
                AN_ACCESS_KEY = credentials('my-prefined-secret-text') 
            }
            steps {
                sh 'printenv'
            }
        }
    }
}
```

- 顶层流水线块中使用的 `environment`指令将适用于流水线中的所有步骤。
- 在一个 `stage`中定义的 `environment`指令只会将给定的环境变量应用于 `stage`中的步骤。
- `environment`块有一个 助手方法 `credentials()`定义，该方法可以在 Jenkins 环境中用于通过标识符访问预定义的凭证。

<a name="zPwkD"></a>
### options（选项）
`options` 指令允许从流水线内部配置特定于流水线的选项。 流水线提供了许多这样的选项, 比如 `buildDiscarder`,但也可以由插件提供, 比如 `timestamps`.

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块，仅出现一次 |


<a name="fFEKJ"></a>
#### 可用选项

-  buildDiscarder<br />为最近的流水线运行的特定数量保存组件和控制台输出。例如: `options { buildDiscarder(logRotator(numToKeepStr: '1')) }` 
-  disableConcurrentBuilds<br />不允许同时执行流水线。 可被用来防止同时访问共享资源等。 例如: `options { disableConcurrentBuilds() }` 
-  overrideIndexTriggers<br />允许覆盖分支索引触发器的默认处理。 如果分支索引触发器在多分支或组织标签中禁用, `options { overrideIndexTriggers(true) }` 将只允许它们用于促工作。否则, `options { overrideIndexTriggers(false) }` 只会禁用改作业的分支索引触发器。 
-  skipDefaultCheckout<br />在`agent` 指令中，跳过从源代码控制中检出代码的默认情况。例如: `options { skipDefaultCheckout() }` 
-  skipStagesAfterUnstable<br />一旦构建状态变得UNSTABLE，跳过该阶段。例如: `options { skipStagesAfterUnstable() }` 
-  checkoutToSubdirectory<br />在工作空间的子目录中自动地执行源代码控制检出。例如: `options { checkoutToSubdirectory('foo') }` 
-  timeout<br />设置流水线运行的超时时间, 在此之后，Jenkins将中止流水线。例如: `options { timeout(time: 1, unit: 'HOURS') }` 
-  retry<br />在失败时, 重新尝试整个流水线的指定次数。 For example: `options { retry(3) }` 
-  timestamps<br />预谋所有由流水线生成的控制台输出，与该流水线发出的时间一致。 例如: `options { timestamps() }` 

示例：
```groovy
pipeline {
    agent any
    options {
        timeout(time: 1, unit: 'HOURS') 
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

- 指定一个小时的全局执行超时, 在此之后，Jenkins 将中止流水线运行。

<a name="HkgWs"></a>
#### 阶段选项
`stage` 的 `options` 指令类似于流水线根目录上的 `options` 指令。然而， `stage` -级别 `options` 只能包括 `retry`, `timeout`, 或 `timestamps` 等步骤, 或与 `stage` 相关的声明式选项，如 `skipDefaultCheckout`。

在`stage`, `options` 指令中的步骤在进入 `agent` 之前被调用或在 `when` 条件出现时进行检查。

可选的阶段选项：

-  skipDefaultCheckout<br />在 `agent` 指令中跳过默认的从源代码控制中检出代码。例如: `options { skipDefaultCheckout() }` 
-  timeout<br />设置此阶段的超时时间, 在此之后， Jenkins 会终止该阶段。 例如: `options { timeout(time: 1, unit: 'HOURS') }` 
-  retry<br />在失败时, 重试此阶段指定次数。 例如: `options { retry(3) }` 
-  timestamps<br />预谋此阶段生成的所有控制台输出以及该行发出的时间一致。例如: `options { timestamps() }` 

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            options {
                timeout(time: 1, unit: 'HOURS') 
            }
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

- 指定 `Example`阶段的执行超时时间, 在此之后，Jenkins 将中止流水线运行。

<a name="OZ8gT"></a>
### parameters（参数）
`parameters` 指令提供了一个用户在触发流水线时应该提供的参数列表。这些用户指定参数的值可通过 `params` 对象提供给流水线步骤。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块，仅出现一次 |


可用参数：

-  string<br />字符串类型的参数, 例如: `parameters { string(name: 'DEPLOY_ENV', defaultValue: 'staging', description: '') }` 
-  booleanParam<br />布尔参数, 例如: `parameters { booleanParam(name: 'DEBUG_BUILD', defaultValue: true, description: '') }` 

示例：
```groovy
pipeline {
    agent any
    parameters {
        string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"
            }
        }
    }
}
```

<a name="NEU6I"></a>
### triggers（触发器）
`triggers` 指令定义了流水线被重新触发的自动化方法。对于集成了源（ 比如 GitHub 或 BitBucket）的流水线, 可能不需要 `triggers` ，因为基于 web 的集成很肯能已经存在。 当前可用的触发器是 `cron`, `pollSCM` 和 `upstream`。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块，仅出现一次 |


可用选项：

-  cron<br />接收 cron 样式的字符串来定义要重新触发流水线的常规间隔 ,比如: `triggers { cron('H */4 * * 1-5') }` 
-  pollSCM<br />接收 cron 样式的字符串来定义一个固定的间隔，在这个间隔中，Jenkins 会检查新的源代码更新。如果存在更改, 流水线就会被重新触发。例如: `triggers { pollSCM('H */4 * * 1-5') }` 
-  upstream<br />接受逗号分隔的工作字符串和阈值。 当字符串中的任何作业以最小阈值结束时，流水线被重新触发。例如: `triggers { upstream(upstreamProjects: 'job1,job2', threshold: hudson.model.Result.SUCCESS) }` 

示例：
```groovy
pipeline {
    agent any
    triggers {
        cron('H */4 * * 1-5')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
```

<a name="w8orM"></a>
### tools（工具）
定义自动安装和放置 `PATH` 的工具的一部分。如果 `agent none` 指定，则忽略该操作。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在顶层的 `pipeline`块或每一个`stage`块 |


支持工具：

- maven
- jdk
- gradle

**工具名称需到 **`**Manage Jenkins** → **Global Tool Configuration**`**中配置，可安装其他工具，比如NodeJS。**

示例：
```groovy
pipeline {
    agent any
    tools {
        maven 'apache-maven-3.0.1' 
    }
    stages {
        stage('Example') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}
```

<a name="lfu3h"></a>
### input（输入）
`stage` 的 `input` 指令允许你使用 `input`提示输入。 在应用了 `options` 后，进入 `stage` 的 `agent` 或评估 `when` 条件前， `stage` 将暂停。 如果 `input` 被批准, `stage` 将会继续。 作为 `input` 提交的一部分的任何参数都将在环境中用于其他 `stage`。

配置项：

-  message<br />必需的。 这将在用户提交 `input` 时呈现给用户。 
-  id<br />`input` 的可选标识符， 默认为 `stage` 名称。 
-  ok<br />`input`表单上的"ok" 按钮的可选文本。 
-  submitter<br />可选的以逗号分隔的用户列表或允许提交 `input` 的外部组名。默认允许任何用户。 
-  submitterParameter<br />环境变量的可选名称。如果存在，用 `submitter` 名称设置。 
-  parameters<br />提示提交者提供的一个可选的参数列表。  

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                }
            }
            steps {
                echo "Hello, ${PERSON}, nice to meet you."
            }
        }
    }
}
```

<a name="fkrnA"></a>
### when（条件）
`when` 指令允许流水线根据给定的条件决定是否应该执行阶段。 `when` 指令必须包含至少一个条件。 如果 `when` 指令包含多个条件, 所有的子条件必须返回True，阶段才能执行。 这与子条件在 `allOf` 条件下嵌套的情况相同。

使用诸如 `not`, `allOf`, 或 `anyOf` 的嵌套条件可以构建更复杂的条件结构 can be built 嵌套条件可以嵌套到任意深度。

| 必填 | 否 |
| --- | --- |
| 参数 | _无_ |
| 允许的位置 | 在`stage`块中 |


内置条件：

-  branch<br />当正在构建的分支与模式给定的分支匹配时，执行这个阶段, 例如: `when { branch 'master' }`。注意，这只适用于多分支流水线。 
-  environment<br />当指定的环境变量是给定的值时，执行这个步骤, 例如: `when { environment name: 'DEPLOY_TO', value: 'production' }` 
-  expression<br />当指定的Groovy表达式评估为true时，执行这个阶段, 例如: `when { expression { return params.DEBUG_BUILD } }` 
-  not<br />当嵌套条件是错误时，执行这个阶段,必须包含一个条件，例如: `when { not { branch 'master' } }` 
-  allOf<br />当所有的嵌套条件都正确时，执行这个阶段,必须包含至少一个条件，例如: `when { allOf { branch 'master'; environment name: 'DEPLOY_TO', value: 'production' } }` 
-  anyOf<br />当至少有一个嵌套条件为真时，执行这个阶段,必须包含至少一个条件，例如: `when { anyOf { branch 'master'; branch 'staging' } }` 

在进入 `stage` 的 `agent` 前评估 `when`<br />默认情况下, 如果定义了某个阶段的代理，在进入该`stage` 的 `agent` 后该 `stage` 的 `when` 条件将会被评估。但是, 可以通过在 `when` 块中指定 `beforeAgent` 选项来更改此选项。 如果 `beforeAgent` 被设置为 `true`, 那么就会首先对 `when` 条件进行评估 , 并且只有在 `when` 条件验证为真时才会进入 `agent` 。

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'production'
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

```groovy
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'production'
                environment name: 'DEPLOY_TO', value: 'production'
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

```groovy
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                allOf {
                    branch 'production'
                    environment name: 'DEPLOY_TO', value: 'production'
                }
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

```groovy
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'production'
                anyOf {
                    environment name: 'DEPLOY_TO', value: 'production'
                    environment name: 'DEPLOY_TO', value: 'staging'
                }
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

```groovy
pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                expression { BRANCH_NAME ==~ /(production|staging)/ }
                anyOf {
                    environment name: 'DEPLOY_TO', value: 'production'
                    environment name: 'DEPLOY_TO', value: 'staging'
                }
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

```groovy
pipeline {
    agent none
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            agent {
                label "some-label"
            }
            when {
                beforeAgent true
                branch 'production'
            }
            steps {
                echo 'Deploying'
            }
        }
    }
}
```

<a name="ltHvd"></a>
### parallel（并行）
声明式流水线的阶段可以在他们内部声明多隔嵌套阶段, 它们将并行执行。 注意，一个阶段必须只有一个 `steps` 或 `parallel` 的阶段。 嵌套阶段本身不能包含进一步的 `parallel` 阶段, 但是其他的阶段的行为与任何其他 `stage` 相同。任何包含 `parallel` 的阶段不能包含 `agent` 或 `tools` 阶段, 因为他们没有相关 `steps`。

另外, 通过添加 `failFast true` 到包含 `parallel`的 `stage` 中， 当其中一个进程失败时，你可以强制所有的 `parallel` 阶段都被终止。

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Non-Parallel Stage') {
            steps {
                echo 'This stage will be executed first.'
            }
        }
        stage('Parallel Stage') {
            when {
                branch 'master'
            }
            failFast true
            parallel {
                stage('Branch A') {
                    agent {
                        label "for-branch-a"
                    }
                    steps {
                        echo "On Branch A"
                    }
                }
                stage('Branch B') {
                    agent {
                        label "for-branch-b"
                    }
                    steps {
                        echo "On Branch B"
                    }
                }
            }
        }
    }
}
```

<a name="52b36576"></a>
### script（脚本）
声明式流水线可能使用在 [流水线步骤引用](https://www.jenkins.io/doc/pipeline/steps) 中记录的所有可用的步骤, 它包含一个完整的步骤列表, 其中添加了下面列出的步骤，这些步骤只在声明式流水线中 **only supported** 。

`script` 步骤需要 [[scripted-pipeline]](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#scripted-pipeline)块并在声明式流水线中执行。 对于大多数用例来说,应该声明式流水线中的“脚本”步骤是不必要的， 但是它可以提供一个有用的"逃生出口"。 非平凡的规模和/或复杂性的 `script` 块应该被转移到 [共享库](https://www.jenkins.io/zh/doc/book/pipeline/syntax/#shared-libraries#) 。

示例：
```groovy
pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'

                script {
                    def browsers = ['chrome', 'firefox']
                    for (int i = 0; i < browsers.size(); ++i) {
                        echo "Testing the ${browsers[i]} browser"
                    }
                }
            }
        }
    }
}
```

<a name="szdvK"></a>
## 脚本化流水线
脚本化 Jenkinsfile (Scripted Pipeline)示例：
```yaml
node { 
    stage('Stage 1') {
        echo 'Hello World' 
    }
}
```
