- 快捷键：六行四列，`table>tr*6>td*4` 按`tab`键
<a name="W5QrF"></a>
# 表格标签自带的非CSS属性
```html
<table width="500" height="400" border="1" bgcolor="green" bordercolor="yellow" cellspacing="0" cellpadding="0" align="center"></table>
```

1. `width="500"` 表格的宽
2. `height="400"` 表格的高
3. `border="1"` 表格的边框
4. `bgcolor="pink"` 表格的背景色
5. `bordercolor="cyan"` 表格的边框颜色
6. `cellspacing="0"`单元格和单元格之间的距离
7. `cellpadding="0"` 内容到单元格之间的距离
8. `align="left/center/right"` 表格内容**水平**居左/中/右
- 可以给 `table``tr``td` 设置（`tr`行 `td`单元格 ）
9. `valign="top/middle/bottom"` 表格内容**垂直**居上/中/下
- 可以给 `tr``td` 设置
- 不能给 `table` 设置
```html
<tr align="center">
    <td align="center" valign="bottom">1-1</td>
</tr>
```

10. 组分割线（下文有介绍）
```html
<table width="500" height="400" border="1" bgcolor="green" bordercolor="yellow" cellspacing="0" cellpadding="0"
    align="center">
    <!-- 行是tr   单元格是td -->
    <tr>
        <td align="center" valign="bottom">1-1</td>
        <td align="right">1-2</td>
        <td>1-3</td>
        <td>1-4</td>
        <td>1-5</td>
    </tr>
    <tr align="center">
        <td>2-1</td>
        <td>2-2</td>
        <td>2-3</td>
        <td>2-4</td>
        <td>2-5</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td>3-2</td>
        <td>3-3</td>
        <td>3-4</td>
        <td>3-5</td>
    </tr>
</table>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649293525818-44159374-f028-4dc7-a436-97549a6beec5.png#clientId=u4036e036-28bc-4&from=paste&height=334&id=u3e8ee1cf&originHeight=417&originWidth=959&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5962&status=done&style=stroke&taskId=ud201549b-343d-4931-952a-d880ba76efe&title=&width=767.2)
<a name="pSHxU"></a>
# 表格的合并
<a name="ert30"></a>
## 合并列 colspan="value"

- 同行操作`td`叫合并列`colspan`
- 合并了哪一个`td`，需要将哪一个`td`删除
<a name="zYJy7"></a>
## 合并行 rowspan="value"

- 跨行操作`td`叫合并行`rowspan`
- 合并了哪一个`td`，需要将哪一个`td`删除
```html
<table width="500" height="400" border="1" cellspacing="0">
    <tr>
        <td colspan="2">1-1</td>
        <!-- <td>1-2</td> -->
        <!-- 要把这行注释掉 -->
        <td>1-3</td>
        <td>1-4</td>
    </tr>
    <tr>
        <td colspan="3">2-1</td>
        <!-- <td>2-2</td>
            <td>2-3</td> -->
        <td>2-4</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td colspan="3">3-2</td>
        <!-- <td>3-3</td>
            <td>3-4</td> -->
    </tr>
    <tr>
        <td rowspan="2">4-1</td><!-- 把4-1和5-1合并 -->
        <td>4-2</td>
        <td>4-3</td>
        <td>4-4</td>
    </tr>
    <tr>
        <!-- <td>5-1</td> -->
        <td>5-2</td>
        <td>5-3</td>
        <td>5-4</td>
    </tr>
    <tr>
        <td>6-1</td>
        <td>6-2</td>
        <td>6-3</td>
        <td>6-4</td>
    </tr>
</table>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649294605700-4a426c55-3e7e-434d-8f66-ba903f7005b3.png#clientId=u4036e036-28bc-4&from=paste&height=279&id=u6a966778&originHeight=516&originWidth=646&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9664&status=done&style=stroke&taskId=ua7c952c0-3ef2-4e65-ae08-4316de598d9&title=&width=348.79998779296875)
<a name="mLOef"></a>
## demo
```html
<!-- 同行操作td  合并列 colspan -->
<!-- 跨行操作td 合并行  rowspan -->
<table width="600" height="500" border="1" cellspacing="0" bgcolor="yellow">
    <tr>
        <td colspan="2" bgcolor="red"></td>
        <!-- <td></td> -->
        <td></td>
        <td rowspan="5" bgcolor="cyan"></td>
    </tr>
    <tr>
        <td></td>
        <td colspan="2" bgcolor="red"></td>
        <!-- <td></td> -->
        <!-- <td></td> -->
    </tr>
    <tr>
        <td></td>
        <td colspan="2" rowspan="2" bgcolor="springgreen"></td>
        <!-- <td></td> -->
        <!-- <td></td> -->
    </tr>
    <tr>
        <td></td>
        <!-- <td colspan="2"></td> -->
        <!-- <td></td> -->
        <!-- <td></td> -->
    </tr>
    <tr>
        <td rowspan="4" bgcolor="cyan"></td>
        <td></td>
        <td></td>
        <!-- <td></td> -->
    </tr>
    <tr>
        <!-- <td></td> -->
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <!-- <td></td> -->
        <td colspan="3" bgcolor="red"></td>
        <!-- <td></td> -->
        <!-- <td></td> -->
    </tr>
    <tr>
        <!-- <td></td> -->
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641988444170-86aec830-8c8b-4a69-834a-fe2c0630c436.png#clientId=u237e32c2-4181-4&from=paste&height=319&id=ue40c241d&originHeight=637&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3896&status=done&style=stroke&taskId=u871e8c35-3230-4a55-84c7-de56c6b6fd8&title=&width=380.5)
<a name="CNsFD"></a>
# 表格的行分组 <thead/tbody/tfoot>
<a name="Tog3I"></a>
## <caption> 表格标题

- 水平居中在表格上方
<a name="PLacB"></a>
## <thead> 表头

- `<tr>``<th>` `</th>``</tr>`
- 注意！`<th>`为表头单元格，**默认加粗，水平居中**
- 高度由内容撑开
<a name="qGdox"></a>
## <tbody> 表主体

- `<tr>行``<td>列` `</td>``</tr>`
- 均分总高度
<a name="Mbbpg"></a>
## <tfoot> 表尾

- `<tr>``<td>` `</td></tr>`
- 高度由内容撑开
<a name="hlTPY"></a>
## 示例
```html
<!-- 表格可以分 表头thead 表主体tbody 表尾tfoot -->
<table width="500" height="400" border="1" cellspacing="0">
    <!-- 2、 表格标题 -->
    <caption>项目增补单</caption>
    <!-- 1、表头 -->
    <thead>
        <tr>
            <th>姓名</th><!-- th表头单元格 默认加粗 水平居中 -->
            <th>年龄</th>
            <th>身高</th>
            <th>户籍</th>
        </tr>
    </thead>
    <!-- 表主体 -->
    <tbody>
        <tr>
            <td>张三</td>
            <td>24</td>
            <td>160</td>
            <td>辽宁</td>
        </tr>
        <tr>
            <td>张三</td>
            <td>24</td>
            <td>160</td>
            <td>辽宁</td>
        </tr>
        <tr>
            <td>张三</td>
            <td>24</td>
            <td>160</td>
            <td>辽宁</td>
        </tr>
    </tbody>
    <!-- 表尾 -->
    <tfoot>
        <tr>
            <td>总结</td>
            <td>总结</td>
            <td>总结</td>
            <td>总结</td>
        </tr>
    </tfoot>
</table>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641989044732-276bd481-8282-48aa-8ca4-36263aee226b.png#clientId=u237e32c2-4181-4&from=paste&height=271&id=u005aba70&originHeight=542&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=22264&status=done&style=stroke&taskId=uc3494fcb-9234-486d-86fe-39e547d0486&title=&width=393)
<a name="X2uIY"></a>
# 表格的列分组 <colgroup span="value"></colgroup>

- `value` 的值为“几列为一组”
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=table, initial-scale=1.0">
    <title>Document</title>
    <style>
        .col1 {
            background: pink;
        }

        .col2 {
            background: skyblue;
        }

        .col3 {
            background: #f90;
        }
    </style>
</head>

<body>
    <table width="600" height="400" border="1" cellspacing="0">
        <!-- 列分组 -->
        <colgroup span="3" class="col1"></colgroup>
        <colgroup span="2" class="col2"></colgroup>
        <colgroup span="4" class="col3"></colgroup><!-- 余下列数不够四列  剩多少就给你呈现多少列颜色 -->
        <tr>
            <td>01</td>
            <td>02</td>
            <td>03</td>
            <td>04</td>
            <td>05</td>
            <td>06</td>
            <td>07</td>
            <td>08</td>
        </tr>
        <tr>
            <td>09</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
        </tr>
    </table>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649311090988-d46053c2-e3e2-4da1-9496-6a05a4594ba4.png#clientId=u4036e036-28bc-4&from=paste&height=202&id=ucb063538&originHeight=514&originWidth=764&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8621&status=done&style=stroke&taskId=u4e4caca0-9bb3-46a3-9c5b-1c7a6890d37&title=&width=300)![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641989943024-8ffc2fa3-ed1c-4b95-893c-e9de4a1fd653.png#clientId=u237e32c2-4181-4&from=paste&height=201&id=u4f2dcd2d&originHeight=511&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3037&status=done&style=stroke&taskId=u1134ee3d-7063-4941-8af1-b067c045944&title=&width=300)
<a name="mksUw"></a>
# 表格的组分割线 rules= "all/cols/rows/groups"

1. `table`标签自带一个属性叫**组分割线**`rules`
2. `rules= "all"` 横向纵向都有边框（默认值）
3. `rules= "cols"` 纵向有边框

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641991912855-ff9ff0b7-123a-4efa-a8fd-4992c8769d9c.png#clientId=u237e32c2-4181-4&from=paste&height=112&id=u2e9b0bf1&originHeight=781&originWidth=1059&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31934&status=done&style=stroke&taskId=u8184f469-c769-409f-9810-f9b0919f797&title=&width=151.5)

4. `rules= "rows"` 横向有边框

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641991884110-a8679711-bc42-4fc2-a221-e29db2bb3e32.png#clientId=u237e32c2-4181-4&from=paste&height=126&id=uce1da5b2&originHeight=634&originWidth=759&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6430&status=done&style=stroke&taskId=u027ee878-25c3-436a-a344-effbb0e3dd3&title=&width=150.5)

5. `rules= "groups"` 组分割线

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641992002462-57841955-5418-49d2-a577-0b4fe64831d8.png#clientId=u237e32c2-4181-4&from=paste&height=320&id=u3c509d5a&originHeight=759&originWidth=1020&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37511&status=done&style=stroke&taskId=u9841e715-5b02-484c-a5ca-51c2540a757&title=&width=430)

6. 示例
```html
<table width="600" height="500" border="1" cellspacing="0" rules="groups">
    <colgroup span="3"></colgroup>
    <colgroup span="3"></colgroup>
    <colgroup span="3"></colgroup>
    <thead>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
    </tfoot>
</table>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641992047800-1dbe87af-71dc-49ea-92d1-2a73f2260322.png#clientId=u237e32c2-4181-4&from=paste&height=271&id=ud09176cd&originHeight=637&originWidth=764&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5053&status=done&style=stroke&taskId=u52757d9f-3442-4ea3-b892-5c041e154d1&title=&width=325)
<a name="zW4az"></a>
# 表格的CSS属性

1. `border-spacing: 0;` 单元格和单元格之间的距离
2. `**border-collapse: collapse;**`** 表格边框的合并**
3. `table-layout: fixed;` 固定单元格宽度，文字超出则折行
4. `table-layout: auto;` 默认值，自动，流式
-  相对友好一些，会根据文字调整宽度（见图例）

![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1641992981067-037e37e4-5c18-45ca-8a66-6e9d3e39852b.png#clientId=u237e32c2-4181-4&from=paste&height=103&id=agoHP&originHeight=310&originWidth=1516&originalType=binary&ratio=1&rotation=0&showTitle=false&size=109944&status=done&style=stroke&taskId=ucaebb2d2-67d8-48d0-af79-13d17642f97&title=&width=505.4000244140625)

5. `empty-cells: hide;` 空单元格不显示
- 不可以与合并表格边框`border-collapse: collapse;` 一起使用
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table {
            width: 500px;
            height: 5px;
            border: 1px solid pink;
            border-spacing: 0; /* 1、单元格和单元格之间的距离 */
            /* border-collapse: collapse; 2、表格边框合并 */
            /* table-layout: auto; 3、默认值 自动 流式 */
            table-layout: fixed;/* 4、固定单元格宽度，文字超出则折行 */
            /* 5、空单元格不显示 注意 不可以与合并表格边框border-collapse: collapse;一起使用 */
            empty-cells: hide;
        }

        td {
            border: 1px solid skyblue;
            background: #f90;
        }
    </style>
</head>

<body>
    <table>
        <tr>
            <td>1234567890哈哈哈哈哈哈哈哈哈</td><!-- 纯数字/英文不折行 -->
            <td>1</td>
            <td>1</td>
            <td></td>
            <td>1</td>
        </tr>
        <tr>
            <td>2</td>
            <td>2</td>
            <td></td>
            <td></td>
            <td>2</td>
        </tr>
        <tr>
            <td></td>
            <td>3</td>
            <td>3</td>
            <td>3</td>
            <td>3</td>
        </tr>
        <tr>
            <td>4</td>
            <td></td>
            <td></td>
            <td>4</td>
            <td>4</td>
        </tr>
    </table>
</body>

</html>
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/25380982/1649742133326-6b650010-14ee-4639-a9f0-6d08bd5ccd23.png#clientId=u5d223aca-c61d-4&from=paste&height=455&id=ua863b1af&originHeight=569&originWidth=1900&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26138&status=done&style=stroke&taskId=ue95d00dc-44e2-46ca-9d49-1dceffc27a6&title=&width=1520)
<a name="KmZWa"></a>
# 表格的应用

- 后台
- 购物车
