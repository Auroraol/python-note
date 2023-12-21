<a name="MX6tB"></a>
# 小米里面input框
1. 用一个`<p>`标签包裹他们两个（`input`+`button`）
2. 给`input`和`button`设置浮动
3. 注意！一定要给`input`和`button`设置相同高度
4. 一定要给`input`和`button`去除边框！（`**button**`**怪异盒模型**，设置完高度，再设置`padding border`的话，自己会做宽高减法，来维持总的宽高不变）
5. 外边的边框，给`<p>`设置来模拟
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        input {
            width: 244px;
            height: 50px;
            background: #ffffff;
            float: left;
            border: 0;
        }

        button {
            width: 50px;
            height: 50px;
            background: #f2f2f2;
            float: left;
            border: 0;
        }

        p {
            width: 294px;
            height: 50px;
            border: 1px solid #e0e0e0;
        }

        /* 
            * 必须这样子写 用一个p标签包裹他们两个（input+button）
            * 给input和button设置浮动
            * 注意！
            * 一定要给input和button设置相同高度
            * 一定要给input和button去除边框！（button怪异盒模型 设置完高度 再设置padding border 自己会做减法 总的宽高不变--委屈自己）
            * 外边的边框 给p设置来模拟 */
    </style>
</head>

<body>
    <p>
        <input type="text" placeholder="红米">
        <button><img src="../1.jpg" alt=""></button>
    </p>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641604873966-d18c44b7-48af-4fa3-a568-b395d6dad018.png#clientId=u9c5b4989-1e2a-4&from=paste&height=86&id=u7380cec2&originHeight=171&originWidth=929&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9745&status=done&style=stroke&taskId=u97f47a31-6e29-47da-8aa1-e28746b3437&title=&width=464.5)
