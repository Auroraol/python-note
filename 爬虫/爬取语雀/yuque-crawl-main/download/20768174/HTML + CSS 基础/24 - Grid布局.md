![grid.jpg](https://cdn.nlark.com/yuque/0/2021/jpeg/22608300/1637300756612-b2d47f62-3048-4a8e-82cb-4258da2d2d9c.jpeg#averageHue=%23f4f8f4&clientId=uc72f45e1-fe5c-4&from=ui&height=274&id=u442e07e1&originHeight=347&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13450&status=done&style=none&taskId=u610a94b2-92e3-49db-a4ff-1a03b97a3e6&title=&width=600)

- flex是一维布局,grid是二维布局，横纵两个方向总是同时存在的
<a name="tkded"></a>

# 1.作用在grid容器

- display:gird;
- grid-template-columns 对网格进行纵划分,单位可以是px,%,自适应auto,fr(网格剩余空间比例单位)
- grid-template-rows 对网格进行横划分,单位可以是px,%,自适应auto,fr
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				/*grid-template-rows:100px 150px 100px 200px 20px 30px;
				grid-template-columns:100px auto ;*/
				/*grid-template-rows:1fr 2fr 3fr 4fr;
				grid-template-columns:1fr 2fr 3fr ;*/
				grid-template-rows:repeat(4,1fr);
				grid-template-columns:repeat(3,1fr);
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
			<div>2</div>
			<div>3</div>
			<div>4</div>
			<div>5</div>
			<div>6</div>
			<div>7</div>
			<div>8</div>
			<div>9</div>
			<div>10</div>
			<div>11</div>
			<div>12</div>
		</div>
	</body>
</html>

```

- grid-template-areas：grid子项只要使用 grid-area 属性指定其隶属于哪个区
   - grid-template以上三个的简写形式
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				/*grid-template-rows:repeat(3,1fr);
				grid-template-columns:repeat(3,1fr);
				grid-template-areas:
				"a1 a1 a1"
				"a2 a2 a3"
				"a2 a2 a3";*/
				grid-template:
				"a1 a1 a1" 1fr
				"a2 a2 a3" 1fr
				"a2 a2 a3" 1fr
				/1fr 1fr 1fr;
			}
			.box>div{
				border:1px solid red ;
			}
			.box>div:nth-child(1){
				grid-area:a1;
			}
			.box>div:nth-child(2){
				grid-area:a2;
			}
			.box>div:nth-child(3){
				grid-area:a3;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
			<div>2</div>
			<div>3</div>
		</div>
	</body>
</html>

```

- grid-column-gap 定义网格间隙
- grid-row-gap 定义网格间隙
   - grid-gap以上两个简写，先写行间距，再写列间距
- justify-items网格元素内容水平呈现方式：拉伸stretch/左中右对齐start/end/center
- align-items网格元素内容垂直呈现方式：拉伸stretch/上中下对齐start/end/center
   - place-items以上两个简写，第一个垂直，第二个水平
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				grid-template-rows:repeat(3,1fr);
				grid-template-columns:repeat(3,1fr);
				justify-items:center;
				align-items:center;
			}
			.box>div{
				border:1px solid red ;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
			<div>2</div>
			<div>3</div>
			<div>4</div>
			<div>5</div>
			<div>6</div>
			<div>7</div>
			<div>8</div>
			<div>9</div>
		</div>
	</body>
</html>

```

- 容器需要调大下使用：
- justify-content网格元素水平分布方式stretch/start/end/center/space-between/space-around/space-evenly
- align-content网格元素垂直分布方式
   - place-content以上简写
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				grid-template-rows:repeat(3,100px);
				grid-template-columns:repeat(3,100px);
				justify-content:space-evenly;
			}
			.box>div{
				border:1px solid red ;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
			<div>2</div>
			<div>3</div>
			<div>4</div>
			<div>5</div>
			<div>6</div>
			<div>7</div>
			<div>8</div>
			<div>9</div>
		</div>
	</body>
</html>

```
<a name="thOaB"></a>
# 2.作用在grid子项上

- 1.grid-column-start水平方向上占据的起始位置
- 2.grid-column-end水平方向上占据的结束位置(span属性)向后添加的个数
- 3.grid-row-start垂直方向上占据的起始位置
- 4.grid-row-end垂直方向上占据的结束位置(span属性)
   - grid-column：1和2的缩写
   - grid-row：3和4的缩写
      - 例grid-column:2 / 4;
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000;
				display: grid;
				grid-template-rows:repeat(3,1fr);
				grid-template-columns:repeat(3,1fr);
			}
			.box>div{
				border:1px solid red ;
				grid-column-start:2;
				grid-row-start:2;
				grid-column-end:4;
				/*grid-row-end:4;*/
				grid-row-end:span 2;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
		</div>
	</body>
</html>

```

- 5.grid-area当前网格所占用的区域
   - grid-area：3横向起始/2纵向起始/4横向结束/4纵向结束
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				grid-template-rows:repeat(3,1fr);
				grid-template-columns:repeat(3,1fr);
			}
			.box>div{
				border:1px solid red ;
				grid-area:3/2/4/4;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
		</div>
	</body>
</html>

```

- 6.justify-self单个网格元素的水平对齐方式start/end/center
- 7.align-self单个网格元素的垂直对齐方式
   - place-self：6和7的缩写，先写垂直，再写水平
```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<style type="text/css">
			.box{
				width: 600px;
				height: 600px;
				border:1px dashed #000 ;
				display: grid;
				grid-template-rows:repeat(3,1fr);
				grid-template-columns:repeat(3,1fr);
			}
			.box>div{
				background-color: red;
				border:1px solid #000 ;
			}
			.box>div:nth-child(2){
				justify-self:start;
				align-self:end;
			}
		</style>
	</head>
	<body>
		<div class="box">
			<div>1</div>
			<div>2</div>
			<div>3</div>
			<div>4</div>
			<div>5</div>
			<div>6</div>
			<div>7</div>
			<div>8</div>
			<div>9</div>
		</div>
	</body>
</html>

```
