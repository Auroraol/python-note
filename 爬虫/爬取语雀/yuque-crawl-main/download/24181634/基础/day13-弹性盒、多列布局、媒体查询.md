<a name="BVD6U"></a>
# 怪异盒模型 box-sizing: border-box;
1. 我希望我的盒子像`button`一样懂事，但凡设置了宽高，那么无论再怎么设置`padding`、`border`我都是之前的宽高 
2. `box-sizing: content-box;` 标准盒模型（默认值）
- 你设置的`width`从内容区算
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>怪异盒模型</title>
    <style>
        div {
            width: 300px;
            height: 300px;
            border: 10px solid #000;
            padding: 100px;
            margin: 100px;
            background: cyan;
            /* 怪异盒模型 */
            box-sizing: border-box;
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642413578535-6b1d8a87-a75d-4fbb-87d7-579644ba842f.png#clientId=u6f0cf979-13bb-4&from=paste&height=243&id=ued4380ac&originHeight=422&originWidth=1142&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37456&status=done&style=stroke&taskId=uab4855d1-f806-416e-9135-736151f7b38&title=&width=657)
<a name="KHUZp"></a>
# 弹性盒
<a name="mpXJd"></a>
## 先感受一下弹性盒的美好
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        nav {
            display: flex;
            width: 1200px;
            height: 100px;
            line-height: 100px;
            margin: 0 auto;
            text-align: center;
            background: pink;
        }

        section {
            border-right: 1px solid #000;
            flex: 1;
        }
    </style>
</head>

<body>
    <nav>
        <section>全部商品</section>
        <section>全商品</section>
        <section>商品</section>
        <section>全部的商品</section>
        <section>全商品</section>
        <section>全部商品</section>
        <section>全部商品</section>
    </nav>
</body>

</html> 
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642412869853-8058f0fa-a4c7-481d-a09b-0de9fcc4a009.png#clientId=u6f0cf979-13bb-4&from=paste&height=74&id=svumy&originHeight=147&originWidth=1520&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5416&status=done&style=stroke&taskId=u7be8c2ec-f49b-4d1f-87e4-c70461711b8&title=&width=760)
<a name="TQRgL"></a>
## 组成
```html
<div id="box">
    <div class="small">
        <div class="little"></div>
    </div>
</div>
```
<a name="peZt5"></a>
### 容器

1. 你给谁设置了`display:flex;`，那么谁就是容器
2.  一般可以视为**父元素**
3. 参考上面案例
- 假设你给`#box`设置了`display:flex;`，那么`#box`就是`.small`的容器
<a name="tXnti"></a>
### 项目

1. 容器里面的子元素，称为“项目”（`.small`就是`#box`的项目）    
2. 当然了，项目也可以设置 `display:flex;` 那么此时项目就是**孙子级**的容器
3. `.small`也可以设置`display:flex;`那么`.little`就是`.small`的项目
<a name="uYFcv"></a>
### 主轴

1. 项目排列的方向
2. 默认的方向可以理解为是**X轴**，当然，你可以更改主轴的方向
<a name="gWCNI"></a>
### 垂直交叉轴

1. 就是和主轴成90°的轴，默认是**Y轴**
2. 如果你将主轴更改了，假设将主轴更改为Y轴，那么，此时垂直交叉轴就是X轴

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642414331657-7a3f5390-20b5-4389-90e3-81544b19e0f4.png#clientId=u6f0cf979-13bb-4&from=paste&height=308&id=u5b7351f7&originHeight=616&originWidth=1105&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8700&status=done&style=stroke&taskId=u7d981de1-5850-484d-ba59-d8cb5a9e5a7&title=&width=552.5)
<a name="fZh0f"></a>
## 可以给父元素设置哪些属性呢？（弹性盒的属性）
<a name="dBKTm"></a>
### 设置弹性盒 display: flex;
<a name="OsiNy"></a>
### 更改主轴的方向 flex-direction
```css
flex-direction: row; /* 默认值  可以理解为X轴 */
/* 12345 */
flex-direction: row-reverse; /* 主轴为水平反向 */
/* 54321 */
flex-direction: column; /* 将主轴方向设置为纵向 */
/* 
1
2
3
4
5
 */
flex-direction: column-reverse; /* 将主轴方向设置为纵向反向 */
/* 
5
4
3
2
1
*/

```
<a name="HM7o1"></a>
### 项目是否折行 flex-wrap
```css
flex-wrap: nowrap;/* 默认值 项目多的时候不折行 */
flex-wrap: wrap;/* 折行 */
flex-wrap: wrap-reverse; /* 反向折行 */
```
<a name="sWani"></a>
### 复合属性 flex-flow（了解）

-    主轴的方向与项目是否折行的简写
```css
flex-flow: column wrap;
```
<a name="qaQAM"></a>
### 项目在主轴上的分布 justify-content

- 注意！设置给**容器**，是容器的属性

![9b990b0d73974284b1f40a2dc670eef.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/25380982/1658797873368-850a602f-b379-454d-9c49-00440d9638d5.jpeg#clientId=ud4348c93-e677-4&from=paste&height=470&id=VjNoE&originHeight=1200&originWidth=893&originalType=binary&ratio=1&rotation=0&showTitle=false&size=347257&status=done&style=stroke&taskId=ufc5e93f8-1c99-4b79-ad5c-4fbc6b5b1b6&title=&width=349.3999938964844)
```css
justify-content: flex-start; /* 默认值  主轴的开端 */
justify-content: center; /* 让项目整体居中于主轴 */
justify-content: flex-end; /* 让项目整体居于主轴末端 */
justify-content: space-around; /* 项目在主轴上两端环绕对齐  左右间距等宽 */
justify-content: space-between; /* 项目在主轴上两端顶格对齐 */
justify-content: space-evenly;/* 项目在主轴上两端等距对齐 */
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650204092414-03174b12-7086-4ce2-baff-4ba112c59226.png#clientId=ue6700620-fc2a-4&from=paste&height=378&id=u761f643e&originHeight=472&originWidth=1102&originalType=binary&ratio=1&rotation=0&showTitle=false&size=39444&status=done&style=stroke&taskId=uc2ad09aa-d711-4b7f-9feb-0ba08474222&title=&width=881.6)
<a name="kYy4s"></a>
### 项目在垂直交叉轴的分布情况 align-items

- 注意！设置给**容器**，是容器的属性
```css
/* 假设  你现在没有给项目(子元素)设置高度 */
align-items: stretch;/* 默认值  项目没有设置高度 高度和容器一致 */
align-items: flex-start; /* 项目们居于垂直交叉轴上方 */
align-items: center; /* 项目们居中于垂直交叉轴 */
align-items: flex-end; /* 项目们居于垂直交叉轴末端 */
align-items: baseline;
```
![align-items: stretch;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650204757680-04f261e6-db96-4b8c-b105-39542b94be36.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=u40ce3c73&originHeight=640&originWidth=799&originalType=binary&ratio=1&rotation=0&showTitle=true&size=34625&status=done&style=stroke&taskId=u41f4ea2e-e42d-4257-b929-62576fa3147&title=align-items%3A%20stretch%3B&width=187 "align-items: stretch;")![align-items: flex-start/end;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1653958109626-61eb54b0-1450-4d86-80eb-7dd07147cee5.png#clientId=u2d869714-d663-4&from=paste&height=150&id=u8fd9bec9&originHeight=645&originWidth=802&originalType=binary&ratio=1&rotation=0&showTitle=true&size=28797&status=done&style=stroke&taskId=u792dffd6-f082-4e0b-bc20-b4132ce8f64&title=align-items%3A%20flex-start%2Fend%3B&width=187 "align-items: flex-start/end;")![align-items: baseline;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650205240469-c107f3ff-55db-44f7-95cb-83423e09fec8.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=u777c6733&originHeight=719&originWidth=901&originalType=binary&ratio=1&rotation=0&showTitle=true&size=24361&status=done&style=stroke&taskId=uc9227677-ad25-4652-8a0c-aaa9f89a949&title=align-items%3A%20baseline%3B&width=188 "align-items: baseline;")
<a name="xKM84"></a>
### 多行项目在垂直交叉轴的排列方式 align-content 

- 注意！首先，项目要多；其次，需要**设置折行 **`flex-wrap: wrap;`
```css
flex-wrap: wrap;/* 先设置让它折行 */

align-content: stretch;/* 默认值  项目没有设置高度  会均分容器高度 */
align-content: flex-start; /* 项目们都在垂直交叉轴上方 */
align-content: center;/* 项目们都在垂直交叉轴中间 */
align-content: flex-end;/* 项目都在垂直交叉轴末端 */
align-content: space-around;/* 项目们在垂直交叉轴两端环绕 */
align-content: space-between;/* 项目们在垂直交叉轴两端顶格对齐 */
align-content: space-evenly;/* 等距对齐 */
```
![align-content: stretch;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650206206980-f8f3a5d3-c543-4e61-9521-bf9de2531a25.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=u5b69f01c&originHeight=722&originWidth=905&originalType=binary&ratio=1&rotation=0&showTitle=true&size=60244&status=done&style=stroke&taskId=udea7a40c-1fae-44ad-9741-44e50b12abc&title=align-content%3A%20stretch%3B&width=188 "align-content: stretch;")![align-content: flex-start/end;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650206065076-3373dda7-97ee-4f6c-b784-d65a95d5694a.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=ucad03f0f&originHeight=722&originWidth=901&originalType=binary&ratio=1&rotation=0&showTitle=true&size=107966&status=done&style=stroke&taskId=uaded6a78-db93-44ea-82f7-01c30efe64c&title=align-content%3A%20flex-start%2Fend%3B&width=187 "align-content: flex-start/end;")![align-content: center;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650205898261-8b342c08-b657-4cee-ab90-b5ae8ce04edb.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=ue1d6491b&originHeight=722&originWidth=902&originalType=binary&ratio=1&rotation=0&showTitle=true&size=70951&status=done&style=stroke&taskId=ufa999c05-b995-46b3-b6ca-72e8153356b&title=align-content%3A%20center%3B&width=187 "align-content: center;")![align-content: space-around;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1653958494383-677fff2e-ed7b-4f45-a3cc-24de1c1226ce.png#clientId=u2d869714-d663-4&from=paste&height=150&id=ud82f4f6e&originHeight=724&originWidth=904&originalType=binary&ratio=1&rotation=0&showTitle=true&size=65199&status=done&style=stroke&taskId=u75a70186-0997-469e-84f2-5f82e0fc5e6&title=align-content%3A%20space-around%3B&width=187 "align-content: space-around;")![align-content: space-between;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650206162932-3d22398d-cd25-431e-bac0-b9426a9d3275.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=u4062cbcc&originHeight=724&originWidth=902&originalType=binary&ratio=1&rotation=0&showTitle=true&size=69870&status=done&style=stroke&taskId=uf962ae3c-91e7-4a10-bf46-12daddd4b82&title=align-content%3A%20space-between%3B&width=187 "align-content: space-between;")![align-content: space-evenly;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650206370816-bbe1ac00-52f9-476c-a32e-0846d8266d0c.png#clientId=ue6700620-fc2a-4&from=paste&height=150&id=ue112d412&originHeight=722&originWidth=902&originalType=binary&ratio=1&rotation=0&showTitle=true&size=69571&status=done&style=stroke&taskId=u219caf8a-5ba9-4af1-9e93-1f4a8eb6838&title=align-content%3A%20space-evenly%3B&width=187 "align-content: space-evenly;")
<a name="FQq8Z"></a>
### 完整代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            width: 1000px;
            height: 800px;
            background: green;
            margin: 0 auto;
            /* 1、设置弹性盒 */
            display: flex;
            /* 2、更改主轴的方向 */
            flex-direction: row;/* 默认值  可以理解为X轴 */
            flex-direction: row-reverse;/* 主轴为水平反向 */
            flex-direction: column;/* 将主轴方向设置为纵向 */
            flex-direction: column-reverse;/* 将主轴方向设置为纵向反向 */
            /* 3、项目是否折行 */
            flex-wrap: nowrap;/* 默认情况下 项目多的时候 我是不折行的 */
            flex-wrap: wrap;/* 折行 */
            flex-wrap: wrap-reverse;/* 反向折行 */
            /* 4、了解  复合属性   主轴的方向 与 项目是否折行的简写 */
            flex-flow: column wrap;
            /* 5、项目在主轴上的分布 注意  设置给容器  是容器的属性 */
            justify-content: flex-start;/* 默认值  主轴的开端 */
            justify-content: center;/* 让项目整体居中于主轴 */
            justify-content: flex-end;/* 让项目整体居于主轴末端 */
            justify-content: space-around;/* 项目在主轴上两端环绕对齐 */
            justify-content: space-between;/* 项目在主轴上两端顶格对齐 */
            justify-content: space-evenly;/* 项目在主轴上两端等距对齐 */
            /* 6、项目在垂直交叉轴的分布情况  注意  设置给容器  是容器的属性 */
            /* 假设  你现在没有给项目(子元素)设置高度 */
            align-items: stretch;/* 默认值  项目没有设置高度 高度和容器一致 */
            align-items: flex-start;/* 项目们居于垂直交叉轴上方 */
            align-items: center;/* 项目们居中于垂直交叉轴 */
            align-items: flex-end;/* 项目们居于垂直交叉轴末端 */
            align-items: baseline;
            /* 7、多行项目在垂直交叉轴的排列方式  那你注意  首先  项目要多  其次  需要设置折行 */
            flex-wrap: wrap;
            align-content: stretch;/* 默认值  项目没有设置高度  会均分容器高度 */
            align-content: flex-start;/* 项目们都在垂直交叉轴上方 */
            align-content: center;/* 项目们都在垂直交叉轴中间 */
            align-content: flex-end;/* 项目都在垂直交叉轴末端 */
            align-content: space-around;/* 项目们在垂直交叉轴两端环绕 */
            align-content: space-between;/* 项目们在垂直交叉轴两端顶格对齐 */
            align-content: space-evenly;/* 等距对齐 */
        }

        section {
            width: 100px;
            height: 100px;
            border: 1px solid #000;
            /* 我希望它依旧是100*100的 */
            box-sizing: border-box;
            background: skyblue;
        }
    </style>
</head>

<body>
    <div class="big">
        <section style="line-height: 20px;">1</section>
        <section style="line-height: 40px;">2</section>
        <section style="line-height: 50px;">3</section>
        <section style="line-height: 30px;">4</section>
        <section style="line-height: 70px;">5</section>
        <section>6</section>
        <section>7</section>
        <section>8</section>
        <section>9</section>
        <section>10</section>
        <section>11</section>
        <section>12</section>
        <section>13</section>
        <section>14</section>
        <section>15</section>
        <section>16</section>
        <section>17</section>
        <section>18</section>
        <section>19</section>
        <section>20</section>
        <section>21</section>
        <section>22</section>
        <section>23</section>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650244528878-3d87dec3-55c8-4b0f-92d5-7bc6d06960dc.png#clientId=u9937b8ae-ab88-4&from=paste&height=244&id=u294ab39c&originHeight=683&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9422&status=done&style=stroke&taskId=ucafe865a-c68d-4ca2-99c4-00f85819739&title=&width=342.4000244140625)
<a name="G1JLu"></a>
### 行内弹性盒 display: inline-flex;

- `display: inline-flex;` 行内弹性盒（类似行内块）
- 可以让其他元素与弹性盒在一行内显示 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            /* 
            display: inline-flex;  行内弹性盒  类似行内块
            可以让其他元素与弹性盒在一行内显示 
            */
            display: inline-flex;
            width: 200px;
            height: 100px;
            background: hotpink;
        }

        span {
            background: pink;
        }
    </style>
</head>

<body>
    <div>
        <b>弹性盒</b>
        <b>弹性盒</b>
        <b>弹性盒</b>
        <b>弹性盒</b>
        <b>弹性盒</b>
    </div>
    <span>行内元素</span>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650242550055-21a6f250-0bd0-4b30-8753-09546f3acb85.png#clientId=u9937b8ae-ab88-4&from=paste&height=114&id=ud7db4da9&originHeight=143&originWidth=357&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4076&status=done&style=stroke&taskId=u49986a66-85e3-4cb7-b0ef-1f19f3b72de&title=&width=285.6)
<a name="K5dZb"></a>
## 可以给子元素设置哪些属性呢？（弹性盒项目的属性）
<a name="YKqRt"></a>
### 项目的排列顺序 order: auto/0/1/-1;

1. `order: auto/0;` 默认值
- 值越大越在后面，可以为负值
- 在代码中，与其他代码依次排序
2. `order: -1;` 置前
3. `order: 1;` 置后

![order: 0;（正常排序）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650244300228-78351206-0263-440a-9d2e-39db9247e574.png#clientId=u9937b8ae-ab88-4&from=paste&height=100&id=u6b7f8118&originHeight=360&originWidth=736&originalType=binary&ratio=1&rotation=0&showTitle=true&size=28855&status=done&style=stroke&taskId=u378ccf5c-9f1e-4295-8a30-1fffef14e62&title=order%3A%200%3B%EF%BC%88%E6%AD%A3%E5%B8%B8%E6%8E%92%E5%BA%8F%EF%BC%89&width=204 "order: 0;（正常排序）")![order: -1;（置前）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650244041989-bc9508e5-b76d-4d57-baca-b493bc86310d.png#clientId=u9937b8ae-ab88-4&from=paste&height=100&id=u1fb6c7a8&originHeight=405&originWidth=822&originalType=binary&ratio=1&rotation=0&showTitle=true&size=19559&status=done&style=stroke&taskId=u707cad83-1622-482a-98f5-9eefc5bf9f7&title=order%3A%20-1%3B%EF%BC%88%E7%BD%AE%E5%89%8D%EF%BC%89&width=203 "order: -1;（置前）")![order: 1;（置后）](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650244068649-d5a7c5e8-dd4e-473f-a019-1e36331083be.png#clientId=u9937b8ae-ab88-4&from=paste&height=100&id=u7e419eb7&originHeight=333&originWidth=745&originalType=binary&ratio=1&rotation=0&showTitle=true&size=22397&status=done&style=stroke&taskId=u61b9b399-6fc6-4200-93e9-a372db508e8&title=order%3A%201%3B%EF%BC%88%E7%BD%AE%E5%90%8E%EF%BC%89&width=224 "order: 1;（置后）")
<a name="Dqi1U"></a>
### 项目在垂直交叉轴的排列方向 align-self
```css
align-self: stretch;/* 默认值  不设置高度 高度和容器一致 */            
align-self: flex-start;/* 居于垂直交叉轴上方 */
align-self: center;/* 居于垂直交叉轴中间 */
align-self: flex-end;/* 居于垂直交叉轴末端 */
```
<a name="vL0GY"></a>
### 完整代码
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .big {
            width: 1000px;
            height: 500px;
            background: green;
            margin: 0 auto;
            /* 设置弹性盒 */
            display: flex;
        }

        span {
            width: 100px;
            height: 100px;
            border: 1px solid #000;
            background: hotpink;
        }

        span:nth-of-type(2) {
            /* 1、项目的排列顺序  order:auto;默认值  值越大越在后面   可以为负值 */
            order: -1;
            background: skyblue;
            /* 2、项目在垂直交叉轴的排列方向 */
            align-self: stretch; /* 默认值  不设置高度 高度和容器一致 */            
            align-self: flex-start; /* 居于垂直交叉轴上方 */
            align-self: center; /* 居于垂直交叉轴中间 */
            align-self: flex-end; /* 居于垂直交叉轴末端 */
        }
    </style>
</head>

<body>
    <div class="big">
        <span>1</span><!-- span标签在弹性盒内可设置宽高 -->
        <span>2</span>
        <span>3</span>
        <span>4</span>
        <span>5</span>
        <span>6</span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650246777641-c8d39a65-ca40-4489-9471-f7c80890622b.png#clientId=u9937b8ae-ab88-4&from=paste&height=349&id=u3f6ec2a9&originHeight=436&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3735&status=done&style=stroke&taskId=u10873c58-9797-46ac-8b88-a4c192e17cd&title=&width=767.2)
<a name="abBuO"></a>
### 超赞的 flex:1;

- `flex:1;` 均分父元素宽度
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        nav {
            /* 设置弹性盒 */
            display: flex;
            width: 1200px;
            height: 100px;
            line-height: 100px;
            margin: 0 auto;
            background: hotpink;
            text-align: center;
        }

        section {
            /* 项目的属性  也就是给子元素设置的  flex:1;均分父元素宽度 */
            flex: 1;
            border-right: 1px solid #000;
            background: skyblue;
        }
    </style>
</head>

<body>
    <nav>
        <section>全部商品</section>
        <section>VIP服务</section>
        <section>今日优品</section>
        <section>次日达</section>
        <section>我是五个字</section>
        <section>我是六个字呀</section>
        <section>商品</section>
    </nav>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650247594152-98c7d0cf-968d-4b1d-8900-218d0c538a10.png#clientId=u9937b8ae-ab88-4&from=paste&height=58&id=ub3178568&originHeight=72&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3714&status=done&style=stroke&taskId=u1dbb0d73-a39d-4695-b6e7-95c2f967c2f&title=&width=767.2)
<a name="Yz3IK"></a>
#### 复合属性 flex:1; 都代表了什么

1. `flex-grow: 1;` 放大
- 将剩余空间均分后，平均分配给每个元素
```css
b:nth-of-type(2) {
    flex-grow: 3;/* 将剩余空间分成四份  取三份 */
}

b:nth-of-type(3) {
    flex-grow: 1;/* 将剩余空间分成四份  取一份 */
}
```

2. `flex-shrink: 1;` 缩小
- 默认值，项目在超出容器宽度时，都统一缩小

![flex-shrink: 0;](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650260262315-dcb17ce2-5555-4a16-b25f-3471a79d084c.png#clientId=u9937b8ae-ab88-4&from=paste&height=100&id=pbGMm&originHeight=403&originWidth=1225&originalType=binary&ratio=1&rotation=0&showTitle=true&size=52367&status=done&style=stroke&taskId=uf8d470fc-609a-4ec7-a2d8-c77490a72c8&title=flex-shrink%3A%200%3B&width=304 "flex-shrink: 0;")

3. `flex-basis: 50%/300px;` 剩余空间
- `50%` 将剩余空间一半都给了它
- `300px` 将剩余空间中的`300px`分给它
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        section {
            /* 设置弹性盒 */
            display: flex;
            width: 1000px;
            height: 400px;
            margin: 100px auto;
            background: green;
        }

        span {
            /* flex: 1; 里面的第一个属性 */
            /* flex-shrink: 1; 默认值  项目在超出容器宽度时  都统一缩小 */
            flex-shrink: 0;
            width: 200px;
            height: 100px;
            border: 2px solid #000;
            background: hotpink;
        }

        /* 我只想让其中几个缩小 */
        span:nth-of-type(3n) {
            flex-shrink: 1;
            background: skyblue;
        }

        b {
            /* flex:1里面的第二个属性 放大 */
            flex-grow: 0;/* 默认值 都不主动进行放大 */
            flex-grow: 1;/* 将剩余空间均分后 平均分配给每个元素 */
            width: 100px;
            height: 100px;
            background: pink;
            border: 1px solid #000;
        }

        b:nth-of-type(2) {
            flex-grow: 3;/* 将剩余空间分成四份  取三份 */
        }

        b:nth-of-type(3) {
            flex-grow: 1;/* 将剩余空间分成四份  取一份 */
        }

        /* flex:1的第三个属性 设置剩余空间 */
        mark {
            width: 100px;
            height: 100px;
            border: 1px solid #000;
        }

        mark:nth-of-type(3) {
            flex-basis: 300px;
            flex-basis: 50%;/* 将剩余空间一半都给了它 */
        }
    </style>
</head>

<body>
    <section>
        <span>第一个属性</span>
        <span>第一个属性</span>
        <span>第一个属性</span>
        <span>第一个属性</span>
        <span>第一个属性</span>
        <span>第一个属性</span>
    </section>

    <section>
        <b>第二个属性</b>
        <b>第二个属性</b>
        <b>第二个属性</b>
    </section>

    <section>
        <mark>第三个属性</mark>
        <mark>第三个属性</mark>
        <mark>第三个属性</mark>
        <mark>第三个属性</mark>
    </section>
</body>

</html>


```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650252999478-fbc5703e-c2d2-427a-ae23-3b69c0bc4a57.png#clientId=u9937b8ae-ab88-4&from=paste&height=722&id=uaf24871c&originHeight=902&originWidth=738&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10882&status=done&style=stroke&taskId=ufdd0bb96-9d8f-428b-a451-6b3af7538d2&title=&width=590.4)
<a name="yyWav"></a>
#### flex 补充
| 序号 | flex | 放大 | 缩小 | 剩余空间 |
| --- | --- | --- | --- | --- |
| 0 | flex: 1; | 1 | 1 |  0% |
| 1 | flex: auto; | 1 | 1 | auto |
| 2 | flex: none; | 0 | 0 | auto |

<a name="BXCPd"></a>
## demo-骰子布局 
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>骰子布局</title>
    <style>
        div {
            /* 设置弹性盒 */
            display: flex;
            width: 200px;
            height: 300px;
            margin: 50px auto;
            background: #DDD;
            /* 水平 垂直 模糊 阴影 颜色 */
            box-shadow: 0px 0px 20px 3px #888;
            border-radius: 10px;
        }

        span {
            width: 80px;
            height: 80px;
            background: red;
            border-radius: 50%;
        }

        /* --------一筒-------- */
        div:nth-of-type(1) {
            /* 项目在主轴上水平居中 */
            justify-content: center;
            /* 项目在垂直交叉轴居中 */
            align-items: center;
        }

        /* --------二筒-------- */
        div:nth-of-type(2) {
            /* 更改主轴的方向 */
            flex-direction: column;
            /* 项目在垂直交叉轴居中 */
            align-items: center;
            /* 项目在主轴上两端环绕对齐 */
            justify-content: space-around;
        }

        /* --------三筒-------- */
        div:nth-of-type(3) {
            /* 更改主轴的方向 */
            flex-direction: column;
            /* 项目在主轴上两端环绕对齐 */
            justify-content: space-around;
        }

        div:nth-of-type(3) span:nth-of-type(2) {
            /* 单独在垂直交叉轴居中 */
            align-self: center;
        }

        div:nth-of-type(3) span:last-of-type {
            /* 单独在垂直交叉轴居中 */
            align-self: flex-end;
        }

        /* --------四筒-------- */
        div:last-of-type {
            /* 项目折行 */
            flex-wrap: wrap;
            justify-content: space-around;
            /* 多行项目  在垂直交叉轴两端环绕 */
            align-content: space-around;
        }
    </style>
</head>

<body>
    <!-- 一筒 -->
    <div>
        <span></span>
    </div>
    <!-- 二筒 -->
    <div>
        <span></span><span></span>
    </div>
    <!-- 三筒 -->
    <div>
        <span></span><span></span><span></span>
    </div>
    <!-- 四筒 -->
    <div>
        <span></span><span></span><span></span><span></span>
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1642422367135-d4747fd9-008c-4c17-b049-c8648a9db25d.png#clientId=u6f0cf979-13bb-4&from=paste&height=293&id=uecf6305b&originHeight=586&originWidth=108&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8436&status=done&style=stroke&taskId=u39778f67-ed73-43cb-9276-deebf611145&title=&width=54)
<a name="ZIfyY"></a>
# 多列布局

- 参考花瓣网图片样式

[花瓣网_陪你做生活的设计师（创意灵感天堂，搜索、发现设计灵感、设计素材）](https://huaban.com/)
<a name="GUPvR"></a>
## 可以给父元素设置哪些属性

1. `column-count: 5;` 列数
- 你想要横向排几列（设置给父元素）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650288495740-909d97ff-0cac-4532-a9c7-1898819c2360.png#clientId=u9937b8ae-ab88-4&from=paste&height=158&id=u0eb47aed&originHeight=197&originWidth=685&originalType=binary&ratio=1&rotation=0&showTitle=false&size=136421&status=done&style=stroke&taskId=u66ea73b5-7d0b-4369-8584-802f7a13bf8&title=&width=548)

2. `column-width: 600px;`  列宽
- 与列数不可同时使用
- 要么，设置列数（就是有几列）
- 要么，设置列宽
3. `column-gap: 20px;` 列间距

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650288674012-5fa85e4d-12b3-40ce-9c03-9c41ba86bc20.png#clientId=u9937b8ae-ab88-4&from=paste&height=157&id=u73fd78d5&originHeight=196&originWidth=202&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17105&status=done&style=stroke&taskId=u62e1dd1d-6f86-4eea-a86c-338a35daba7&title=&width=161.6)

4. `column-rule: 2px dotted #0f0;` 列分割线

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1650288808867-7d9c655c-e828-43d0-bb45-603db0b6c5b1.png#clientId=u9937b8ae-ab88-4&from=paste&height=146&id=u054d1252&originHeight=182&originWidth=198&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24499&status=done&style=stroke&taskId=u241b657b-f76c-48c3-a1d3-28c0e98508a&title=&width=158.4)

5. `column-fill: auto;` 列高自适应
<a name="zBEVP"></a>
## 可以给子元素设置哪些属性

1. `break-inside: avoid;` 避免在元素内出现分页现象
- 注意 一定是给每一列小块设置 
2. `column-span: all;` 横跨所有行
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>多列布局</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        main {
            width: calc(100% - 200px);
            /* 差200像素百分百 */
            height: auto;
            margin: 0 auto;
            /* 渐变 */
            background: linear-gradient(to right, #3ce, #fb6); 
            /* 你想要几列 */
            column-count: 5; 
            /* 兼容 */
            -webkit-column-count: 5;
            -moz-column-count: 5;
            -ms-column-count: 5;
            -o-column-count: 5;
            /* 1、列间距 */
            column-gap: 20px;
            /* 2、列分割线 */
            column-rule: 2px dotted #0f0;
            /* 3、列高自适应 */
            column-fill: auto;
            /* 
                * 5、注意  
                * 要么  设置列数  就是有几列  
                * 要么  就设置列宽   
                * 不可以两个一起使用 
            */
            /* column-width: 600px;  与第23行 不可以同时使用代码*/
        }

        figure {
            border: 1px solid #000;
            background: #FFF;
            /* 
                * break-inside 属性规定在指定元素内部是否应发生分页 	
                * avoid 避免在元素内出现页、列、区域中断
                * 注意 一定是给每一列小块设置 
            */
            break-inside: avoid;
        }

        img {
            /* 设置大小  只设置宽度   高度会等比例适应  */
            width: 100%; /* 就代表宽度和figure一致 */
        }

        h1 {
            /* 4、横跨几列 */
            column-span: all; /* 横跨所有行 */
        }
    </style>
</head>

<body>
    <main>
        <h1>五福临门喜迎财神五福临门喜迎财神五福临门喜迎财神</h1>
        <figure>
            <img src="./images/1.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/2.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/3.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/4.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/5.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/6.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/7.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/8.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/9.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/10.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/11.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/12.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/13.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/14.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/15.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/16.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/17.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/18.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/19.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/20.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/21.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/22.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/23.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/24.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/25.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/26.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/27.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/28.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/29.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/30.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/31.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/32.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/33.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/34.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/35.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/36.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/37.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/38.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/39.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/40.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/41.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/42.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/43.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/44.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/45.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/46.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/47.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/48.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>
            <img src="./images/49.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
        <figure>4
            <img src="./images/50.jpeg" alt="">
            <figcaption>正月里来是新年呀，大年初一头一天啊</figcaption>
        </figure>
    </main>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650273961502-f9fedddb-6f46-4117-a692-ad88ad16ecab.gif#clientId=u9937b8ae-ab88-4&from=paste&height=653&id=u9b13d06d&originHeight=816&originWidth=943&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6641480&status=done&style=stroke&taskId=u6cccb9e5-7b2a-4beb-b386-ab15691f1bc&title=&width=754.4)
<a name="I1r95"></a>
## demo-京东
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650290108737-a6174b23-1ca8-4cd4-bfaf-6a8471ca5365.gif#clientId=u9937b8ae-ab88-4&from=paste&height=494&id=u5bd307d0&originHeight=618&originWidth=943&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3550137&status=done&style=stroke&taskId=u6cc7af37-1844-4185-8c53-711b566267b&title=&width=754.4)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        main {
            width: 1275px;
            height: auto;
            margin: 0 auto;
            background: palevioletred url(../images/a.png);
            column-count: 5;
        }

        .small {
            width: 200px;
            height: 300px;
            border: 1px solid #000;
            margin-bottom: 20px;
            background: pink;
        }
    </style>
</head>

<body>
    <main>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
        <div class="small"></div>
    </main>
</body>

</html>
```
![666.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1650330652366-c0ca8b58-6cdc-4f72-b5ae-d731c82101b4.gif#clientId=u492abd00-65c9-4&from=paste&height=706&id=u87d85d72&originHeight=882&originWidth=950&originalType=binary&ratio=1&rotation=0&showTitle=false&size=752341&status=done&style=stroke&taskId=ud859cb76-0bc7-4046-ba68-f7c6981b361&title=&width=760)
<a name="sJAzp"></a>
# 媒体查询@media
参考下面的网站<br />[觉唯设计_用户体验设计分享平台](https://www.jiawin.com/)
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            width: 100%;
            height: 200px;
        }

        /* 媒体查询 @media    注意！and前后有空格 */
        @media screen and (min-width:1200px) {
            div {
                background: orangered;
            }
        }

        /* ----------------700~1200---- */
        @media screen and (max-width:1200px) and (min-width:700px) {
            div {
                background: blueviolet;
            }
        }

        /* ----------------700以下---- */
        @media screen and (max-width:700px) {
            div {
                background: orange;
            }
        }
    </style>
</head>

<body>
    <div></div>
</body>

</html>
```
![2.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642428788123-937ef317-e763-4d88-bed4-88c91a34fb05.gif#clientId=u6f0cf979-13bb-4&from=drop&id=uddaa434a&originHeight=276&originWidth=1516&originalType=binary&ratio=1&rotation=0&showTitle=false&size=436139&status=done&style=stroke&taskId=u39a5d297-efda-4be3-8758-d09df167ef8&title=)
<a name="EwiKh"></a>
## 响应式
参考下面的网站<br />[Bootstrap中文网](https://www.bootcss.com/)
```html
<!-- 练习：960以上  700~960一个  700以下一个 -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* -------这里写的 就是全局状态下 也就是大于1000  ------- */
        * {
            margin: 0;
            padding: 0;
        }

        nav {
            display: flex;/* 设置弹性盒  让头部左右两个块  横向展示 */
            justify-content: space-between;/* 项目(头部左右)两端顶格/环绕对齐 */
            width: 100%;/* 设置占一行宽度 */
            height: 60px;/* 设置高度 */
            padding: 0 10%;/* 设置内容距离左右有个间距 */
            box-sizing: border-box;/* 因为设置padding会长胖 还希望是100% 就设置了怪异盒模型 */
            background: #444;/* 设置背景色 */
            line-height: 60px;/* 设置行高=高度值 文字垂直居中 */
            /* 文字大小和颜色可以继承  直接设置给nav */
            font-size: 12px;
            color: #ccc;
        }

        .left {
            display: flex;/* 设置弹性盒子  目的是让左边的7个section横向展示 */
            /* background: #f90; */
        }

        section {
            padding: 0 10px;/* 让每个文字左右有间距 */
        }

        .left section:first-of-type {
            font-size: 18px;/* 左边第一个文字字体大 */
        }

        aside {
            display: flex;/* 右侧设置弹性盒子 */
            align-items: center;/* 让项目水平居中 其实就是为了让图片垂直居中 */
            /* background: skyblue; */
        }

        img {
            display: none;/* 图片默认不显示 */
        }

        /* 开始媒体查询  页面宽度到1000的时候  左侧第一个和右侧第一个消失 */
        @media screen and (max-width:1000px) and (min-width:700px) {

            /* 这个时候怎么了  左边第一个和右边第一个没啦 */
            section:first-of-type {
                display: none;
            }
        }

        /* -------700以下的时候  左边只剩下第一个section   右边呢  出现一张图片  剩下其他的都没啦*/
        @media screen and (max-width:700px) {
            section {
                display: none;/* 所有的section都消失 */
            }

            .left section:first-of-type {
                display: block;/* 左边第一个section是出现的  我们再设置一下 让人家出现 */
            }

            img {
                display: block;/* 右边的图片显示 */ 
            }
        }
    </style>https://www.bootcss.com/
</head>

<body>
    <nav>
        <!-- 头部左侧 -->
        <div class="left">
            <section>Bootstrap中文网</section>
            <section>Bootstrap3中文文档</section>
            <section>Bootstrap4中文文档</section>
            <section>Sass 教程</section>
            <section>Less 教程</section>
            <section>jQuery API</section>
            <section>网站实例</section>
        </div>
        <!-- 头部右侧 -->
        <aside>
            <!-- 用div标签也可以 -->
            <section>关于</section>
            <img src="../images/4.png" alt="">
        </aside>
    </nav>
</body>

</html>
```
<a name="fKfiY"></a>
## ![3.gif](https://cdn.nlark.com/yuque/0/2022/gif/25380982/1642430766367-1c3e75e1-5ece-4750-aa42-fe810f940ce7.gif#clientId=u6f0cf979-13bb-4&from=drop&id=u2672ab15&originHeight=276&originWidth=1393&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1560840&status=done&style=stroke&taskId=u715ec94b-6ae8-4265-8c2c-4d8e61609ba&title=)
<a name="df7q2"></a>
## 响应式布局特点

1. 设计特点：
- 面对不同分辨率设备灵活性强
- 能够快捷解决多设备显示适应问题
2. 缺点
- 兼容各种设备工作量大，效率低下
- 代码累赘，会出现隐藏无用的元素，加载时间加长
- 其实这是一种折中性质的设计解决方案，多方面因素影响而达不到最佳效果
- 一定程度上改变了网站原有的布局结构，会出现用户混淆的情况
