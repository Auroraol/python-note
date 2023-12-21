<a name="pHEZL"></a>

# 背景相关属性
<a name="whU0u"></a>

## 背景图大小 background-size

1. `background-size: 水平大小 垂直大小;`
- 可以写数值，也可以写百分比
- `background-size: 100px 200px;`
- `background-size: 100% 100%;`（如果不是等比例的图片，会拉伸变形）
2. `background-size: cover;` 覆盖
- 等比例拉伸到宽高**最大值** 
- 弊端：图片显示可能不完全

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642173921018-206e98a2-4d25-46f2-8c8c-1128170d1b61.png#clientId=u97ef8e6d-705a-4&from=paste&height=226&id=ub3cea68a&originHeight=565&originWidth=808&originalType=binary&ratio=1&rotation=0&showTitle=false&size=318444&status=done&style=stroke&taskId=u6ff9afae-1b88-4c6d-bdba-9ac42914e31&title=&width=323)

3. `background-size: contain;`
- 等比例拉伸到宽高**最小值 **
- 弊端：可能会遗漏背景色

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642173825785-76de4d49-7cc9-4c6c-9e69-10467076c8e1.png#clientId=u97ef8e6d-705a-4&from=paste&height=280&id=u72e83e28&originHeight=560&originWidth=631&originalType=binary&ratio=1&rotation=0&showTitle=false&size=176524&status=done&style=stroke&taskId=uc9723e8a-e3f6-4be4-a190-20c00fe753b&title=&width=315.5)
<a name="jEFLr"></a>
## 背景图原点 background-origin

1. 什么是背景图原点 ? 
- 就是背景图以哪一块为起始点，开始向四周平铺
- 默认 `padding` 区域
2. `background-origin: padding-box;` 默认值
- 背景图以 `padding` 区域为原点开始向四周平铺

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650080888803-ba59eec3-0901-457d-aa4d-1ecd36f77086.png#clientId=u45071fb1-bdfd-4&from=paste&height=250&id=uc74b2c60&originHeight=323&originWidth=453&originalType=binary&ratio=1&rotation=0&showTitle=false&size=130108&status=done&style=stroke&taskId=ua8e6097c-fbea-4da8-9ff5-5c5892be2d5&title=&width=350)

3. `background-origin: content-box;` 
- 背景图以 `contnet` 区域为原点开始向四周平铺

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642174395847-e119ce91-b399-4684-86d1-93da33f43236.png#clientId=u97ef8e6d-705a-4&from=paste&height=300&id=u3a663456&originHeight=653&originWidth=762&originalType=binary&ratio=1&rotation=0&showTitle=false&size=351945&status=done&style=stroke&taskId=ue15cf1c1-4218-48a1-90c7-824bf16265b&title=&width=350)

4. `background-origin: border-box;`
- 背景图以 `border` 区域为原点开始向四周平铺

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650081080118-cacf656f-2a54-4c55-b4c3-e318900f38a1.png#clientId=u45071fb1-bdfd-4&from=paste&height=299&id=u813a2e2b&originHeight=408&originWidth=477&originalType=binary&ratio=1&rotation=0&showTitle=false&size=194011&status=done&style=stroke&taskId=uce8435e6-494c-48df-9ee7-4945640d288&title=&width=350)
<a name="a7ohN"></a>
## 背景图裁切 background-clip: *-box;

1. `background-clip: border-box;` 默认值，背景图在边框区域裁切
2. `background-clip: padding-box;` 背景图在`padding`区域裁切
- 也就是说背景展现到`padding` 区域，`border`区域不展示背景图
3. `background-clip: content-box;` 背景图在内容`content`区域裁切  
- 也就是说背景展现到`content`区域，`padding``border`区域没有背景
<a name="a9XTM"></a>
## 多背景图的引入 background: url(图片路径), url(.图片路径);

1. 使用逗号隔开  
2. **不能**同时设置**背景颜色 **
3. 如果你想要设置背景颜色，那么在设置完多背景图之后，设置`background-color`即可
4. 示例
```css
background: url(图片路径) no-repeat left top, url(图片路径) no-repeat right bottom;
/* 如果在后续代码中想要设置背景颜色 */
background-color: green;
```
<a name="Oq18Y"></a>
## 完整代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS3背景相关属性</title>
    <style>
        div {
            width: 1900px;
            height: 1700px;
            border: 100px solid rgba(0, 0, 0, 0.5);
            padding: 200px 100px;
            margin: 0 auto;
            background: #f90 url(./g.jpg);
            /* 1、背景图大小 */
            background-size: 100px 200px;
            background-size: 100% 100%; 
            background-size: cover; 
            background-size: contain;
            /* 2、背景图原点 */
            background-origin: padding-box;
            background-origin:content-box;
            background-origin: border-box;
            /* 3、背景图裁切   默认值是显示到边框 */
            background-clip: border-box;
            background-clip: padding-box;
            background-clip: content-box; 
            /* 4、多背景图引入 */
            background: url(./1.jpg) no-repeat left top, url(./2.jpg) no-repeat right bottom;
            background-color: cyan;
        }
    </style>
</head>

<body>
    <div>我是content区域的填充文字</div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642174928202-d2b5d630-83cb-498b-a77a-0df6a6c13ff1.png#clientId=u97ef8e6d-705a-4&from=paste&height=357&id=uf7c433a4&originHeight=714&originWidth=716&originalType=binary&ratio=1&rotation=0&showTitle=false&size=157236&status=done&style=stroke&taskId=u2318eceb-c8f1-4543-997b-1679296a8f5&title=&width=358)
<a name="Qzag4"></a>
# 背景渐变
<a name="IRlOg"></a>
## 线性渐变background-image: linear-gradient(颜色，颜色);

1. 线性渐变属于背景里面的图片   
```css
/* 兼容 */
background: -webkit-linear-gradient(red,#f90);/* 谷歌 */
background: -moz-linear-gradient(red,#f90);/* 火狐 */
background: -ms-linear-gradient(red,#f90);/* IE */
background: -o-linear-gradient(red,#f90);/* 欧朋 */

```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650081387991-3d8190ab-0327-4ea6-8ffc-465f08f08d37.png#clientId=u45071fb1-bdfd-4&from=paste&height=110&id=u5c7ba3e9&originHeight=314&originWidth=783&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2786&status=done&style=stroke&taskId=ud2dfef19-c08f-4f8c-940d-cc5b7c43d77&title=&width=273.3999938964844)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650081649846-6c82fd9f-b481-419d-b7c0-9f00cec7a887.png#clientId=u45071fb1-bdfd-4&from=paste&height=108&id=u3983a812&originHeight=135&originWidth=30&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1002&status=done&style=stroke&taskId=u27208a68-9c34-4fef-914b-d2be596426c&title=&width=24)

2. 线性渐变可以分方向，**默认**是从上到下
3. 我们可以直接设置角度，角度的单位是deg
```css
background: linear-gradient(to top,red,#ff0);
background: linear-gradient(to bottom,red,#ff0);
background: linear-gradient(to left,red,#ff0);
background: linear-gradient(to right,red,#ff0);
background: linear-gradient(to right bottom,red,#ff0);
background: linear-gradient(15deg,red,#ff0,#0f0);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642175935673-b1921578-16f5-4c7d-b0d4-6ed2a386da12.png#clientId=u97ef8e6d-705a-4&from=paste&height=113&id=zx5HZ&originHeight=226&originWidth=557&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12960&status=done&style=stroke&taskId=u04f42002-b738-40bb-abd9-6fb92dc30d7&title=&width=278.5)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650081679543-a3e6b1fa-085e-4ffc-a9fe-f38ccec10e41.png#clientId=u45071fb1-bdfd-4&from=paste&height=27&id=u6a33a43e&originHeight=34&originWidth=150&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1273&status=done&style=stroke&taskId=ue29b1474-afd6-4390-a3be-9d9e97aca1d&title=&width=120)
<a name="ZlTHC"></a>
## 径向渐变background: radial-gradient
```css
section{
    width: 600px;
    height: 300px;
    background: radial-gradient(red,yellow);
}
/* 径向渐变：从起点到终点颜色从内到外进行圆形渐变。（从中间向外拉） */
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642176020442-0f133812-3755-4327-8e66-80625c998f17.png#clientId=u97ef8e6d-705a-4&from=paste&height=169&id=g8TeC&originHeight=337&originWidth=674&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39072&status=done&style=stroke&taskId=u7bb24265-79bd-46f7-98f4-3e600ba54a5&title=&width=337)
<a name="PgbU5"></a>
## 重复线性渐变 background: repeating-linear-gradient
```css
background: repeating-linear-gradient(red, yellow 10%, green 20%);
background: -webkit-repeating-linear-gradient(red, yellow 10%, green 20%);
background: -moz-repeating-linear-gradient(red, yellow 10%, green 20%);
background: -o-repeating-linear-gradient(red, yellow 10%, green 20%);
background: -ms-repeating-linear-gradient(red, yellow 10%, green 20%);
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642176109885-617c3716-b316-47a8-b312-7483ffe385d8.png#clientId=u97ef8e6d-705a-4&from=paste&height=308&id=u7285ab4b&originHeight=615&originWidth=622&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26446&status=done&style=stroke&taskId=u938b0998-7755-437b-a357-3abc6572a25&title=&width=311)
<a name="qJwmv"></a>
## 重复径向渐变 background: repeating-radial-gradient
```css
background: repeating-radial-gradient(red, yellow 10%, green 20%);
background: -webkit-repeating-radial-gradient(red, yellow 10%, green 20%);
background: -moz-repeating-radial-gradient(red, yellow 10%, green 20%);
background: -o-repeating-radial-gradient(red, yellow 10%, green 20%);
background: -ms-repeating-radial-gradient(red, yellow 10%, green 20%);
border-radius: 50%;/* 可以给图片加圆角 */
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650082122206-f95c51d0-e030-4b2f-86a1-54962dbac302.png#clientId=u45071fb1-bdfd-4&from=paste&height=174&id=u0e052ecc&originHeight=624&originWidth=625&originalType=binary&ratio=1&rotation=0&showTitle=false&size=172145&status=done&style=stroke&taskId=u976e1c6e-4e54-45bf-a98e-ad3971859f3&title=&width=174)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642176149977-b4f57e10-c0b5-4be6-bf8b-b8f650ffe830.png#clientId=u97ef8e6d-705a-4&from=paste&height=174&id=uacc3b5e1&originHeight=547&originWidth=569&originalType=binary&ratio=1&rotation=0&showTitle=false&size=121168&status=done&style=stroke&taskId=uf52b5176-f020-467e-aca6-1db96f75509&title=&width=180.5)
<a name="iJChM"></a>
## 代码汇总
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 500px;
            height: 200px;
            /* 线性渐变  它属于背景里面的图片  background-image: linear-gradient(); */
            background: linear-gradient(red,#f88);
            background:  -webkit-linear-gradient(red,#f88);
            background: -moz-linear-gradient(red,#f88);
            background: -ms-linear-gradient(red,#f88);
            background: -o-linear-gradient(red,#f88);
            /* 线性渐变  可以分方向  默认是从上到下 */
            background: linear-gradient(to top,red,#ff0);
            background: linear-gradient(to bottom,red,#ff0);
            background: linear-gradient(to left,red,#ff0);
            background: linear-gradient(to right,red,#ff0);
            background: linear-gradient(to right bottom,red,#ff0);
            /* 我们可以直接设置角度  角度的单位是deg */
            background: linear-gradient(15deg,red,#ff0,#0f0);
        }
        section{
            width: 600px;
            height: 300px;
            background: radial-gradient(red,yellow);
        }
        nav{
            width: 500px;
            height: 500px;
            /* 重复线性渐变 */
            background: repeating-linear-gradient(red, yellow 10%, green 20%);
            background: -webkit-repeating-linear-gradient(red, yellow 10%, green 20%);
            background: -moz-repeating-linear-gradient(red, yellow 10%, green 20%);
            background: -o-repeating-linear-gradient(red, yellow 10%, green 20%);
            background: -ms-repeating-linear-gradient(red, yellow 10%, green 20%);
            /* 重复径向渐变 */
            background: repeating-radial-gradient(red, yellow 10%, green 20%);
            background: -webkit-repeating-radial-gradient(red, yellow 10%, green 20%);
            background: -moz-repeating-radial-gradient(red, yellow 10%, green 20%);
            background: -o-repeating-radial-gradient(red, yellow 10%, green 20%);
            background: -ms-repeating-radial-gradient(red, yellow 10%, green 20%);
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div></div>
    <section>径向渐变</section>
    <nav></nav>
</body>
</html>
```
<a name="hZY7h"></a>
## 渐变demo-考拉网
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        ul {
            width: 100px;
            height: 400px;
            background-image: linear-gradient(to right, red, #f88);
        }
    </style>
</head>

<body>
    <ul>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
        <li>内容</li>
    </ul>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642176540390-165d9588-205b-4914-b2da-d87fdf56f541.png#clientId=u0fba3d49-88e2-4&from=paste&height=293&id=u87c1566e&originHeight=585&originWidth=204&originalType=binary&ratio=1&rotation=0&showTitle=false&size=121430&status=done&style=stroke&taskId=uedb0d23f-69b3-43ed-ad98-9f3acae08f6&title=&width=102)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642176459545-0dfb85cd-76a1-4e17-8a12-59c36a52ae94.png#clientId=u0fba3d49-88e2-4&from=paste&height=251&id=u287d9b05&originHeight=501&originWidth=175&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12528&status=done&style=stroke&taskId=u91539406-f365-4508-a63e-86b59672611&title=&width=87.5)
