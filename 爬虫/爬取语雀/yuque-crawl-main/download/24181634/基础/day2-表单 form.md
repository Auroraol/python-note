<a name="paIZo"></a>

# 表单<form>

1. 作用：用来收集用户信息
- 里面填写姓名、性别、年龄... 的信息
- 当你提交时，我`form`直接打包，把整体信息传到数据库
2. 属性
- `action`="表单数据提交的URL地址"（比如注册信息提交到世纪佳缘数据库）
- `method`="数据提交过去的方式" 有两种值 
   - `post` 稳、慢、可携带数据量没有限制
   - `get` 快、不安全、存在数据泄露的风险（因为快，所以可携带数据有限制，不能超过4kb）
- `name`="表单名字" 为了区分种类
```html
<form action="世纪佳缘数据库地址" method="传送数据的方式" name="表单名字"></form>
```
<a name="pyVru"></a>
# 文本框<input type="text">

1. `value="实心的提示信息"`
2. `placeholder="虚焦的提示信息"`
```html
<p>姓名：<input type="text"></p>
<p>性别：<input type="text" value="请输入"></p><!-- 属性 value -->
<p>电话：<input type="text" placeholder="请输入"></p><!-- 属性 placeholder -->
<p>住址：<input type="text"></p>
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640914806414-b482595e-5896-43dd-8102-f7c79def42ad.png#clientId=ub256d156-3b19-4&from=paste&height=166&id=u7e3eb977&originHeight=204&originWidth=307&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4708&status=done&style=stroke&taskId=u8f888c67-8d13-4a41-bbf2-b332e99b77b&title=&width=250.5)
<a name="RXYk2"></a>
# 密码框<input type="password">
```html
<p>密码：<input type="password" placeholder="请输入密码"></p>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649047003236-895cc977-3eec-4ed6-b6fe-bcd56d323e30.gif#clientId=ua0c96833-df6c-4&from=paste&height=48&id=u76beb5ed&originHeight=140&originWidth=860&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24089&status=done&style=stroke&taskId=u8c5540a7-4bc1-4baa-9199-d1106f5e176&title=&width=292.3999938964844)
<a name="GqrGc"></a>
# 按钮
<a name="edx3M"></a>
## 普通按钮<input type="button">

- 建议结合`value`使用
```html
<input type="button">
<input type="button" value="上一页">
<input type="button" value="下一页">
```
<a name="A1WhV"></a>
## 普通中的战斗机按钮<button>

- 只是会跳转到`form`里面的`action`所指的路径中
- 什么也不干，提交不了数据。
```html
<button>战斗机</button>
```
<a name="xbleO"></a>
## 重置按钮<input type="reset">

- 注意：重置按钮一定要写在`form`里面，重置的是`form`里面的内容。
```html
<input type="reset">
<input type="reset" value="hello">
```
<a name="J2SJz"></a>
## 提交按钮<input type="submit">

- 跳转到`action`所指的路径中，并提交了`form`里面所有数据
```html
<input type="submit">
<input type="submit" value="免费注册">
```
<a name="eCrmi"></a>
## 代码汇总
```html
<form action="世纪佳缘数据库地址" method="传送数据的方式" name="表单名字">
    <!-- 文本框 -->
    <input type="text">
    <p>姓名：<input type="text"></p>
    <!-- 属性value -->
    <p>性别：<input type="text" value="请输入"></p>
    <!-- 属性placeholder -->
    <p>电话：<input type="text" placeholder="请输入"></p>
    <p>住址：<input type="text"></p>
    <!-- 密码框 -->
    <input type="password">
    <p>密码：<input type="password" placeholder="请输入密码"></p>
    <!-- 按钮 -->
    <!-- 普通按钮 -->
    <input type="button">
    <input type="button" value="上一页">
    <input type="button" value="下一页">
    <!-- 战斗机 -->
    <button>战斗机</button>
    <!-- 重置按钮 -->
    <input type="reset">
    <input type="reset" value="hello">
    <!-- 提交按钮 -->
    <input type="submit">
    <input type="submit" value="免费注册">
</form>
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/25380982/1640918068271-c8699275-07d6-459b-a441-0d548d80c88f.png#clientId=ub256d156-3b19-4&from=paste&height=67&id=pl9aR&originHeight=61&originWidth=539&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3921&status=done&style=stroke&taskId=u37fc2ab4-2e66-4454-89fd-3ba525c87b5&title=&width=591.5)
<a name="ZMgth"></a>
# 扩展按钮
<a name="nLBqj"></a>
## 单选框<input type="radio">

1. 注意！单选按钮有一个属性`**name**`**必须写**，**并且同一组的**`**name**`**值相同**。
2. 属性
- 默认选中 `checked="checked"`
- 禁止使用 `disabled="disabled"`
- 注意！`XHTML`必须这么写，在`HTML5`中自由一些，可简写为`checked`、`disabled`。
```html
<input type="radio" name="cc" checked="checked">未婚
<input type="radio" name="cc">离异
<input type="radio" name="cc">丧偶
<br>
<input type="radio" name="sex">男生
<input type="radio" name="sex">女生
<input type="radio" name="sex" disabled>其他
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649047709526-12f71676-85c3-4deb-ba47-795c37d40b3d.gif#clientId=ua0c96833-df6c-4&from=drop&height=63&id=uff02b728&originHeight=152&originWidth=592&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60778&status=done&style=stroke&taskId=u146746ae-da14-458e-b0cc-ac63d9260ed&title=&width=245)
<a name="AWQFU"></a>
## 复选框<input type="checkbox">

1. 注意！属性`name`必须写，并且同一组的`name`值相同。
2. 属性
- 默认选中 `checked="checked"`
- 禁止使用 `disabled="disabled"`
- 注意！`XHTML`必须这么写，在`HTML5`中自由一些，可简写为`checked`、`disabled`。

```html
<input type="checkbox" name="study">HTML
<input type="checkbox" name="study">Css
<input type="checkbox" name="study">Js
<input type="checkbox" name="study" checked>Java
<input type="checkbox" name="study">Python
<input type="checkbox" name="study" disabled>js
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649047901958-f6dc65e6-5749-4e8b-9026-5c396f67f5e4.gif#clientId=ua0c96833-df6c-4&from=drop&height=44&id=u7c4e3b52&originHeight=72&originWidth=732&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54694&status=done&style=stroke&taskId=u5c3db025-ff5c-4dc1-aebf-23320301a93&title=&width=451.3999938964844)
<a name="FjSUI"></a>
# 表单扩展及汇总
```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        legend {
            text-align: right;/* center */
        }

        /* 让多行文本域不能自定义大小 */
        textarea {
            resize: none;
        }
    </style>
</head>

<body>
    <form action="将数据传送到哪里的url" method="将数据传送过去的方式post/get" name="表单名字" id="">
        <!-- 表单字段集 是包裹里面所有表单控件 -->
        <fieldset>
            <!-- 表单字段集标题  必须是fieldset里面第一个子元素 -->
            <legend>个人简介</legend><!-- 默认水平居左 -->
            <!-- 1、文本框 -->
            <p><input type="text"></p>
            <p><input type="text" value="实心的提示信息"></p>
            <p><input type="text" placeholder="虚焦的提示信息"></p>
            <!-- 2、密码框 -->
            <p><input type="password"></p>
            <!-- 3、按钮 -->
            <!-- 普通按钮 -->
            <input type="button" value="普通按钮">
            <button>战斗机 只跳转不提交  跳转到action所指的url中</button>
            <!-- 重置按钮  必须写在form里面 -->
            <input type="reset">
            <input type="reset" value="自定义文字">
            <!-- 提交按钮 既跳转又提交 -->
            <input type="submit">
            <input type="submit" value="自定义文字">
            <hr>
            <!-- 
                * 4、单选按钮/单选框  有一个属性name必须写  并且同一组的name值相同 
                * <label>信息提示标签  设置后可以点选文字  扩大了元素的可点击区域 
            -->
            <label><input type="radio" name="boy">火锅</label>
            <label><input type="radio" name="boy">烤肉</label>
            <label><input type="radio" name="boy" disabled>米线</label>
            <label><input type="radio" name="boy">炸鸡</label>
            <label><input type="radio" name="boy" checked="checked">韩料</label>
            <hr>
            <!-- 5、多选按钮/复选框  有一个属性name必须写  并且同一组的name值相同 -->
            <input type="checkbox" name="girl">芝麻酱
            <input type="checkbox" name="girl" checked>韭菜
            <input type="checkbox" name="girl" disabled>蒜泥
            <input type="checkbox" name="girl">香油
            <input type="checkbox" name="girl">葱花
            <input type="checkbox" name="girl">腐乳
            <!-- 6、下拉框 -->
            <select name="" id="">
                <!-- 注意  <option>具有属性value值  暂时不建议写  js会获取option里面的内容  会获取到value值为空 -->
                <option>2000</option>
                <option>2001</option>
                <option>2002</option>
                <option>2003</option>
                <option>2004</option>
                <option>2005</option>
                <option>2006</option>
            </select>
            <!-- 
                * 7、多行文本域 
                * cols="30"字符宽度  也就是说 一行可以显示30个英文字母  一个中文占两个字符宽度 
                * rows="10"行数  超过10行 出现滚动条 
            -->
            <textarea name="" id="" cols="30" rows="10"></textarea>
            <!-- 8、上传文件 -->
            <input type="file">
            <!-- 9、图像域 -->
            <input type="image" src="../1.png" width="100" height="100">
            <!-- 10、隐藏文本框 -->
            <input type="hidden" value="999999"><!-- 获取传参用 -->
        </fieldset>
    </form>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641994711302-92dcc991-9d13-45b0-8323-c1b589d215b2.png#clientId=u237e32c2-4181-4&from=paste&height=565&id=ubdd2ed48&originHeight=718&originWidth=953&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68537&status=done&style=stroke&taskId=ue4424529-fda5-4238-be5c-6a58a19b382&title=&width=750)
<a name="pqCFa"></a>
# <label>信息提示标签
```html
<input type="radio" name="rel" id="ipt1">
<label for="ipt1">男生</label>

<input type="radio" name="rel" id="ipt2">
<label for="ipt2">女生</label>

<input type="radio" name="rel" id="ipt3">
<label for="ipt3">其他</label>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1649048689443-d9dea85b-2d9c-4f41-ade3-85f3d1776a33.gif#clientId=ua0c96833-df6c-4&from=drop&height=39&id=uf83bc5d5&originHeight=82&originWidth=487&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24365&status=done&style=stroke&taskId=u544d2c2b-7333-4586-beff-47101c7cf0b&title=&width=230)
<a name="UG2eC"></a>
# 扩展
<a name="crJ2O"></a>
## Form中的获取数据的两个方式get和post的区别？

```html
<form name="表单名称" method="post/get" action=""></form>
```

1. `get` 请求通常是从服务器上获取数据
- `post` 请求通常表示向服务器提交数据
2. `get` 请求发送的数据都写在地址栏上，用户可见
- `post` 请求发送的数据，用户不可见
3. `get` 请求不能提交大量的数据
- 但`post`可以，因此不要混用
<a name="zGaWM"></a>
### 建议

1. `get`方式的安全性较`Post`方式要差些
- 包含机密信息的话，建议用`Post`数据提交方式；
2. 在做数据查询时，建议用`Get`方式；
- 而在做数据添加、修改或删除时，建议用`Post`方式；
