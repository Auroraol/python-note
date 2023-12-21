<a name="Pyply"></a>
# 文本溢出的处理-溢出隐藏
<a name="kAcdE"></a>
## 溢出默认 overflow: visible; 
<a name="AjJD2"></a>
## 滚动条 overflow: scroll;

- 无论文字是否溢出，都出现滚动条
<a name="VlCUb"></a>
## 检测溢出 overflow: auto

- 溢出滚动，不溢出什么也没有
<a name="rpI0q"></a>
## 溢出隐藏 overflow: hidden;

- 一刀切，超出部分直接切割掉![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641742614346-ce36cc96-1401-4fd9-9aab-33ae3128f78f.png#clientId=u2b811117-368d-4&from=paste&height=30&id=ud3dd64cb&originHeight=112&originWidth=175&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2943&status=done&style=stroke&taskId=u8739f08c-de10-4b68-90fd-ea1d1f35c87&title=&width=46.5)
```html
<head>
    <meta charset="UTF-8">
    <title>溢出隐藏</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            background: tomato;
            /* 文本溢出的处理 */
            overflow: visible;	/* 默认值 溢出 */
            overflow: scroll;		/* 无论你文字是否溢出 我都出现滚动条 */
            overflow: auto;			/* 会检测 溢出时 出现滚动条 */
            overflow: hidden;		/* 溢出隐藏 */
            /* 
                * 可以分x轴和y轴
                * 如果想要实现纵向滚动 
            */
            overflow-x: hidden;
            overflow-y: auto;
        }
    </style>
</head>

<body>
    <div>
        qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素
    </div>
</body>
```
![a9430417f2947704847d05ebc6fb303.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641533293833-48312161-2117-430a-95fc-ff42ab734cfe.png#clientId=u0598b96e-f1a1-4&from=paste&height=385&id=u0ef3c16b&originHeight=769&originWidth=1280&originalType=binary&ratio=1&rotation=0&showTitle=false&size=170427&status=done&style=stroke&taskId=ud1bd8f08-2f5d-4088-a4b6-cf30fb6be2f&title=&width=640)
<a name="yOYSU"></a>
# 让文本在一行显示 white-space: nowrap;
```css
white-space: normal; /* 默认值 页面正常解析 */
white-space: pre; /* 文本原样输出 就是在编辑器什么样子 浏览器就呈现什么样子 */
white-space: pre-line; /* 文本原样输出 但是超出区域会折行 会识别掉空格 */
white-space: pre-wrap; /* 文本原样输出 但是超出区域会折行 其余的不变 */
white-space: nowrap;/* 重点！ 让文本在一行显示 */
```
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
            width: 200px;
            height: 200px;
            background: pink;
            white-space: normal; /* 默认值 页面正常解析 */
            white-space: pre; /* 文本原样输出 就是在编辑器什么样子 浏览器就呈现什么样子 */
            white-space: pre-line; /* 文本原样输出 但是超出区域会折行 会识别掉空格 */
            white-space: pre-wrap; /* 文本原样输出 但是超出区域会折行 其余的不变 */
            /* 重点 让文本在一行显示 */
            white-space: nowrap;
        }
    </style>
</head>

<body>
    <div>
        小幸运

        失恋无罪
    
        失恋阵线联盟
    
            听歌识曲
                
                在线播放  
    </div>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641534086020-add22da6-4668-4ee4-99d1-642478f87a1d.png#clientId=u0598b96e-f1a1-4&from=paste&height=170&id=uf3375cbd&originHeight=273&originWidth=282&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7413&status=done&style=stroke&taskId=u61eaa840-1a39-4fa9-84e8-7a2e4b1014f&title=&width=176)
<a name="Rcnuo"></a>
## 空余空间/文本原样输出 <pre>

- `<pre>`是一个废弃标签，和`<font></font>`一样，禁止使用
```html
<pre>
        小幸运

        失恋无罪
    
        失恋阵线联盟
    
            听歌识曲
                
                在线播放    
</pre>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641533849908-94cf9d3b-33c2-4804-88ec-78039582c840.png#clientId=u0598b96e-f1a1-4&from=paste&height=155&id=TiKjU&originHeight=200&originWidth=233&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2031&status=done&style=stroke&taskId=u017ccd5c-e6a8-46d8-a95b-e1104d94a72&title=&width=180.5)
<a name="YDjv1"></a>
# 单行文本省略号

1. `text-overflow: ellipsis;` 溢出部分以“...”显示
- 单独使用无效
2. `text-overflow: clip;`（默认值）裁剪区域不显示
3. 四个步骤：
- `width: value;` 设置宽高
- `white-space: nowrap;` 让文本在一行显示（因为是单行）
- `overflow: hidden;` 溢出隐藏（一刀切）
- `text-overflow: ellipsis;` 将隐藏部分以“...”形式呈现
```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        div {
            background: pink;
            /* 1.设置宽高 */
            width: 200px;
            /* 2.让文本在一行显示 */
            white-space: nowrap;
            /* 3.溢出隐藏 */
            overflow: hidden;
            /* 4.将隐藏部分...显示 */
            text-overflow: ellipsis;/* 默认值是clip 裁剪 */
        }
    </style>
</head>

<body>
    <div>
        块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素块状元素
    </div>
</body>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641534870054-997c06b2-9f40-496c-a6bd-62a6c2fca16d.png#clientId=u0598b96e-f1a1-4&from=paste&height=46&id=ua881fa34&originHeight=46&originWidth=269&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1550&status=done&style=stroke&taskId=ucd477513-f594-4bc2-8047-b620ce8166d&title=&width=270.5)
<a name="ARTkU"></a>
# 小结[文本溢出 孙多多.png](https://www.yuque.com/attachments/yuque/0/2022/png/25380982/1641956673448-9ac9f6d9-cc51-4693-9f71-c8644abfcbef.png?_lake_card=%7B%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2022%2Fpng%2F25380982%2F1641956673448-9ac9f6d9-cc51-4693-9f71-c8644abfcbef.png%22%2C%22name%22%3A%22%E6%96%87%E6%9C%AC%E6%BA%A2%E5%87%BA%20%E5%AD%99%E5%A4%9A%E5%A4%9A.png%22%2C%22size%22%3A394824%2C%22type%22%3A%22image%2Fpng%22%2C%22ext%22%3A%22png%22%2C%22status%22%3A%22done%22%2C%22taskId%22%3A%22u8ca98154-d2a2-4dcc-938c-22d6ea16510%22%2C%22taskType%22%3A%22upload%22%2C%22id%22%3A%22ue8b3bd59%22%2C%22card%22%3A%22file%22%7D)
