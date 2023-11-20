<a name="PHG3V"></a>
## 📃 Echarts简介
`Apache ECharts` 是一个基于 JavaScript 的开源可视化图表库。

Echarts官网：<br />[Apache ECharts](https://echarts.apache.org/)

<a name="WognO"></a>
## 📃 Echarts使用
首先，在 [https://www.jsdelivr.com/package/npm/echarts](https://www.jsdelivr.com/package/npm/echarts) 选择 `dist/echarts.js`，点击并保存为 `echarts.js` 文件。

基础示例：
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>ECharts</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.js"></script>
  </head>
  <body>
    <!-- 为 ECharts 准备一个定义了宽高的 DOM -->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
      // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(document.getElementById('main'));

      // 指定图表的配置项和数据
      let option = {
        title: {
          text: '国家人口与GDP'
        },
        tooltip: {},
        legend: {
          data: ['GDP', '人口']
        },
        xAxis: {
          data: ['中国', '美国', '印度', '英国', '日本', '韩国']
        },
        yAxis: {},
        series: [
          {
            name: 'GDP',
            type: 'bar',
            data: [20, 30, 15, 10, 16, 18]
          },
          {
            name: '人口',
            type: 'bar',
            data: [50, 40, 45, 10, 8, 5]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    </script>
  </body>
</html>
```
[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/wvpRNNy)

通过npm的方式安装：
```html
yarn add echarts
```
使用：
```javascript
import * as echarts from 'echarts';

// 基于准备好的dom，初始化echarts实例
let myChart = echarts.init(document.getElementById('main'));
// 绘制图表
myChart.setOption({
  title: {
    text: 'ECharts 入门示例'
  },
  tooltip: {},
  xAxis: {
    data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
});
```

如果在DOM中没有定义容器的宽高，可以在初始化的时候指定其宽高：
```javascript
  let myChart = echarts.init(document.getElementById('main'), null, {
    width: 600,
    height: 400
  });
```

<a name="AADmI"></a>
## 📃 Echarts基本概念
<a name="ltBwa"></a>
### ✨  主题
可以在初始化的时候，指定echarts的主题，默认支持深色主题：
```javascript
let chart = echarts.init(dom, 'dark');
```

<a name="jmMev"></a>
#### 加载外部主题
如果默认主题不满足用户使用，可以到以下链接创建自己的主题，导出为json<br />[主题编辑器 - Apache ECharts](https://echarts.apache.org/zh/theme-builder.html)

导出json后，如果是通过包管理工具加载，可以直接引入：
```javascript
import vintage from 'vintage.json'

echarts.registerTheme('vintage', vintage);
let chart = echarts.init(dom, 'vintage');
```
如果没有使用打包工具，则可以通过网络请求的方式获取并加载：
```javascript
// 假设主题名称是 "vintage"
$.getJSON('vintage.json', function(themeJSON) {
  echarts.registerTheme('vintage', JSON.parse(themeJSON));
  let chart = echarts.init(dom, 'vintage');
});
```

<a name="VIXGN"></a>
### ✨  数据集
数据集有两种设置方式：`dataset.source`和`series.data`。

<a name="lJJRk"></a>
#### dataset.source
一种是通过`dataset.source`设置：
```javascript
option = {
  legend: {},
  tooltip: {},
  dataset: {
    // 提供一份数据。
    source: [
      ['product', '2015', '2016', '2017'],
      ['Matcha Latte', 43.3, 85.8, 93.7],
      ['Milk Tea', 83.1, 73.4, 55.1],
      ['Cheese Cocoa', 86.4, 65.2, 82.5],
      ['Walnut Brownie', 72.4, 53.9, 39.1]
    ]
  },
  // 声明一个 X 轴，类目轴（category）。默认情况下，类目轴对应到 dataset 第一列。
  xAxis: { type: 'category' },
  // 声明一个 Y 轴，数值轴。
  yAxis: {},
  // 声明多个 bar 系列，默认情况下，每个系列会自动对应到 dataset 的每一列。
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
};
```
可以为对象数组形式：
```javascript
option = {
  legend: {},
  tooltip: {},
  dataset: {
    // 用 dimensions 指定了维度的顺序。直角坐标系中，如果 X 轴 type 为 category，
    // 默认把第一个维度映射到 X 轴上，后面维度映射到 Y 轴上。
    // 如果不指定 dimensions，也可以通过指定 series.encode 完成映射。
    dimensions: ['product', '2015', '2016', '2017'],
    source: [
      { product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7 },
      { product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1 },
      { product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5 },
      { product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1 }
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
};
```
也可以按维度的形式展开：
```javascript
option = {
  legend: {},
  tooltip: {},
  dataset: {
    dimensions: ['product', '2015', '2016', '2017'],
    source: {
      product: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie'],
      2015: [43.3, 83.1, 86.4, 72.4],
      2016: [85.8, 73.4, 65.2, 53.9],
      2017: [93.7, 55.1, 82.5, 39.1]
    }
  },
  xAxis: { type: 'category' },
  yAxis: {},
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
};
```

效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/WNdLBOX)

<a name="e8WE4"></a>
#### series.data
另一种是通过`series.data`设置：
```javascript
option = {
  xAxis: {
    type: 'category',
    data: ['Matcha Latte', 'Milk Tea', 'Cheese Cocoa', 'Walnut Brownie']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      name: '2015',
      data: [89.3, 92.1, 94.4, 85.4]
    },
    {
      type: 'bar',
      name: '2016',
      data: [95.8, 89.4, 91.2, 76.9]
    },
    {
      type: 'bar',
      name: '2017',
      data: [97.7, 83.1, 92.5, 78.1]
    }
  ]
};
```

<a name="l19AG"></a>
### ✨  数据转换
在dataset中可以定义多个数据集，通过`transform`指定数据转换方法。

<a name="Vxsbw"></a>
#### 过滤器
将`transform`的type设置为`filter`，可以指定数据转换器为过滤器；`dimension`为要筛选的维度；`value`为筛选维度的值。
```javascript
option = {
  dataset: [
    {
      // 这个 dataset 的 index 是 `0`。
      source: [
        ['Product', 'Sales', 'Price', 'Year'],
        ['Cake', 123, 32, 2011],
        ['Cereal', 231, 14, 2011],
        ['Tofu', 235, 5, 2011],
        ['Dumpling', 341, 25, 2011],
        ['Biscuit', 122, 29, 2011],
        ['Cake', 143, 30, 2012],
        ['Cereal', 201, 19, 2012],
        ['Tofu', 255, 7, 2012],
        ['Dumpling', 241, 27, 2012],
        ['Biscuit', 102, 34, 2012],
        ['Cake', 153, 28, 2013],
        ['Cereal', 181, 21, 2013],
        ['Tofu', 395, 4, 2013],
        ['Dumpling', 281, 31, 2013],
        ['Biscuit', 92, 39, 2013],
        ['Cake', 223, 29, 2014],
        ['Cereal', 211, 17, 2014],
        ['Tofu', 345, 3, 2014],
        ['Dumpling', 211, 35, 2014],
        ['Biscuit', 72, 24, 2014]
      ]
      // id: 'a'
    },
    {
      // 这个 dataset 的 index 是 `1`。
      // 这个 `transform` 配置，表示，此 dataset 的数据，来自于此 transform 的结果。
      transform: {
        type: 'filter',
        config: { dimension: 'Year', value: 2011 }
      }
      // 我们还可以设置这些可选的属性： `fromDatasetIndex` 或 `fromDatasetId`。
      // 这些属性，指定了，transform 的输入，来自于哪个 dataset。例如，
      // `fromDatasetIndex: 0` 表示输入来自于 index 为 `0` 的 dataset 。又例如，
      // `fromDatasetId: 'a'` 表示输入来自于 `id: 'a'` 的 dataset。
      // 当这些属性都不指定时，默认认为，输入来自于 index 为 `0` 的 dataset 。
    },
    {
      // 这个 dataset 的 index 是 `2`。
      // 同样，这里因为 `fromDatasetIndex` 和 `fromDatasetId` 都没有被指定，
      // 那么输入默认来自于 index 为 `0` 的 dataset 。
      transform: {
        // 这个类型为 "filter" 的 transform 能够遍历并筛选出满足条件的数据项。
        type: 'filter',
        // 每个 transform 如果需要有配置参数的话，都须配置在 `config` 里。
        // 在这个 "filter" transform 中，`config` 用于指定筛选条件。
        // 下面这个筛选条件是：选出维度（ dimension ）'Year' 中值为 2012 的所有
        // 数据项。
        config: { dimension: 'Year', value: 2012 }
      }
    },
    {
      // 这个 dataset 的 index 是 `3`。
      transform: {
        type: 'filter',
        config: { dimension: 'Year', value: 2013 }
      }
    }
  ],
  series: [
    {
      type: 'pie',
      radius: 50,
      center: ['25%', '50%'],
      // 这个饼图系列，引用了 index 为 `1` 的 dataset 。也就是，引用了上述
      // 2011 年那个 "filter" transform 的结果。
      datasetIndex: 1
    },
    {
      type: 'pie',
      radius: 50,
      center: ['50%', '50%'],
      datasetIndex: 2
    },
    {
      type: 'pie',
      radius: 50,
      center: ['75%', '50%'],
      datasetIndex: 3
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/bGazveM)

<a name="QDJQr"></a>
#### 排序
将`transform`的type设置为`sort`，可以为指定的维度进行排序；其中 `asc`升序，`desc`降序。
```javascript
option = {
  dataset: [
    {
      source: [
        // 原始数据
      ]
    },
    {
      transform: {
        type: 'sort',
        config: { dimension: 'Year', order: 'desc' }
      }
    }
  ],
  series: {
    type: 'pie',
    // 这个系列引用上述 transform 的结果。
    datasetIndex: 1
  }
};
```

<a name="kChb2"></a>
#### 链式操作
transform可以是一个数组，多个转换器可以进行链式操作，上一个的输出是下一个的输入。
```javascript
option = {
  dataset: [
    {
      source: [
        // 原始数据
      ]
    },
    {
      // 几个 transform 被声明成 array ，他们构成了一个链，
      // 前一个 transform 的输出是后一个 transform 的输入。
      transform: [
        {
          type: 'filter',
          config: { dimension: 'Product', value: 'Tofu' }
        },
        {
          type: 'sort',
          config: { dimension: 'Year', order: 'desc' }
        }
      ]
    }
  ],
  series: {
    type: 'pie',
    // 这个系列引用上述 transform 的结果。
    datasetIndex: 1
  }
};
```

<a name="qDinZ"></a>
### ✨  坐标轴
x 轴和 y 轴都由轴线、刻度、刻度标签、轴标题四个部分组成。部分图表中还会有网格线来帮助查看和计算数据。<br />![charts_axis_img02.webp](https://cdn.nlark.com/yuque/0/2022/webp/2213540/1650435176513-60d0fe7c-59fd-4e4b-b878-948066682a7f.webp#clientId=udc2cb11b-0b71-4&from=drop&id=u5c010898&originHeight=567&originWidth=1457&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23304&status=done&style=none&taskId=u07dc0d6b-7163-4d01-92be-ef6d3e22baf&title=)

通过 `xAxis``yAxis`设置两条坐标轴信息：
```javascript
option = {
  xAxis: {
    type: 'time',
    name: '销售时间'
  },
  yAxis: {
    type: 'value',
    name: '销售数量'
  }
};
```

<a name="zhp2E"></a>
#### 多条轴线
可以为X、Y两个方向设置多个轴线（数组形式），两个 Y 轴显示在上下，两个 Y 轴显示在左右两侧。
```javascript
option = {
  xAxis: {
    type: 'time',
    name: '销售时间'
  },
  yAxis: [
    {
      type: 'value',
      name: '销售数量'
    },
    {
      type: 'value',
      name: '销售金额'
    }
  ]
};
```
多于两个 x/y 轴需要通过配置 [offset](https://echarts.apache.org/option.html#xAxis.offset) 属性防止同个位置多个轴的重叠。

<a name="Q1tle"></a>
#### 轴线样式
通过 [axisLine](https://echarts.apache.org/option.html#xAxis.axisLine) 为轴线设置样式。比如轴线带箭头，并设置为虚线：
```javascript
option = {
  xAxis: {
    type: 'time',
    name: '销售时间',
    axisLine: {
      symbol: 'arrow',
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  yAxis: {
    type: 'value',
    name: '销售数量',
    axisLine: {
      symbol: 'arrow',
      lineStyle: {
        type: 'dashed'
      }
    }
  }
};
```

通过 [axisTick](https://echarts.apache.org/option.html#xAxis.axisTick) 为刻度线设置样式。比如刻度线宽度、刻度线样式等：
```javascript
option = {
  xAxis: {
    axisTick: {
      length: 30,
      lineStyle: {
        type: 'dashed'
      }
    }
  },
  yAxis: {
    axisTick: {
      length: 30,
      lineStyle: {
        type: 'dashed'
      }
    }
  }
};
```

<a name="US1yL"></a>
#### 刻度标签
通过 [axisLabel](https://echarts.apache.org/option.html#xAxis.axisLabel) 设置相应坐标轴标签，例如文字对齐方式，自定义刻度标签内容等：
```javascript
option = {
  xAxis: {
    axisLabel: {
      formatter: '{value} kg',
      align: 'center'
    }
  },
  yAxis: {
    axisLabel: {
      formatter: '{value} 元',
      align: 'center'
    }
  }
};
```

<a name="CxfyY"></a>
### ✨  图例
通说`legend`设置图例，包括其排列方向、位置信息：
```javascript
option = {
  legend: {
    type: 'scroll', // 可滚动翻页的图例
    orient: 'vertical', // or 'horizontal'
    right: 'center',
    top: 'top',
    data: ['Evaporation', 'Precipitation', 'Temperature'], // 若省略，则显示所有图例
  },
}
```
一个复杂一点的图例示例：
```javascript
let option = {
  legend: {
    type: 'scroll', // 可滚动翻页的图例
    orient: 'vertical', // or 'horizontal'
    right: 'center',
    top: 'top',
    data: [{
      name: 'Evaporation',
      icon: 'rect', // 图例样式
    }, {
      name: 'Precipitation',
      icon: 'roundRect',
    }, {
      name: 'Temperature',
      icon: 'pin',
    }],
    // 图例背景
    backgroundColor: '#000',
    // 图例样式
    textStyle: {
      color: '#fff'
      // ...
    },
    // 设置默认显示隐藏的图例
    selected: {
      Evaporation: true,
      Precipitation: true,
      Temperature: false
    }
  },
}
```
其中：

- `orient`设置图例方向
- `data`可以设置显示的图例，不设置此项则显示全部图例
- `data.icon`设置图例图标，可选 `circle`, `rect`, `roundRect`, `triangle`, `diamond`, `pin`, `arrow`, `none`
- `selected`设置默认选中的图例

示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/XWVOBEb)<br />以上示例，设置了轴线和刻度线的样式，Y轴设置了两条轴线，图例垂直方向排布。

<a name="JElt5"></a>
## 📃 Echarts应用
Echarts示例参考：<br />[Examples - Apache ECharts](https://echarts.apache.org/examples/zh/index.html)

<a name="EJqKp"></a>
### ✨  柱状图
在 `series`中将`type`设置为`bar`即可添加柱状图。

示例：
```javascript
option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
```

<a name="TZ9nR"></a>
#### 横向柱状图
将 `yAxis`设置为 `{ type: 'category' }`，在 `series`中将`encode`的x轴和y轴分别设置为source中的维度。
```javascript
let option = {
  dataset: {
    source: [
      ['score', 'amount', 'product'],
      [89.3, 58212, 'Matcha Latte'],
      [57.1, 78254, 'Milk Tea'],
      [74.4, 41032, 'Cheese Cocoa'],
      [50.1, 12755, 'Cheese Brownie'],
      [89.7, 20145, 'Matcha Cocoa'],
      [68.1, 79146, 'Tea'],
      [19.6, 91852, 'Orange Juice'],
      [10.6, 101852, 'Lemon Juice'],
      [32.7, 20112, 'Walnut Brownie']
    ]
  },
  xAxis: {},
  // 将 类目轴（category） 映射到y轴
  yAxis: { type: 'category' },
  series: [
    {
      type: 'bar',
      encode: {
        // 将 "amount" 列映射到 X 轴。
        x: 'amount',
        // 将 "product" 列映射到 Y 轴。
        y: 'product'
      }
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/GRyPbQd)

<a name="GAykT"></a>
#### 堆叠柱状图
通过`stack`可将柱状图分组，只要名称一致即可。
```javascript
option = {
  xAxis: {
    data: ['<20', '20-30', '30-40', '40-50', '>50']
  },
  yAxis: {},
  series: [
    // 男性
    {
      data: [10, 22, 28, 43, 49],
      type: 'bar',
      stack: 'sex'
    },
    // 女性
    {
      data: [5, 4, 3, 5, 10],
      type: 'bar',
      stack: 'sex'
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/wvpNQQQ)

<a name="cBlYC"></a>
#### 动态排序柱状图
动态设置数据，可以在图标中看到动效；添加`realtimeSort`选项，可以进行实时排序：
```javascript
let myChart = echarts.init(document.getElementById('main'));

let option = {};

let data = [];
for (let i = 0; i < 5; ++i) {
  data.push(Math.round(Math.random() * 200));
}

option = {
  xAxis: {
    max: 'dataMax'
  },
  yAxis: {
    type: 'category',
    data: ['A', 'B', 'C', 'D', 'E'],
    inverse: true,
    animationDuration: 300,
    animationDurationUpdate: 300,
    max: 2 // only the largest 3 bars will be displayed
  },
  series: [
    {
      realtimeSort: true,
      name: 'X',
      type: 'bar',
      data: data,
      label: {
        show: true,
        position: 'right',
        valueAnimation: true
      }
    }
  ],
  legend: {
    show: true
  },
  animationDuration: 3000,
  animationDurationUpdate: 3000,
  animationEasing: 'linear',
  animationEasingUpdate: 'linear'
};

myChart.setOption(option);

function update() {
  let data = option.series[0].data;
  for (let i = 0; i < data.length; ++i) {
    if (Math.random() > 0.9) {
      data[i] += Math.round(Math.random() * 2000);
    } else {
      data[i] += Math.round(Math.random() * 200);
    }
  }
  myChart.setOption(option);
}

setInterval(function () {
  update();
}, 3000);
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/mdpgyga)

<a name="N3f0p"></a>
#### 阶梯瀑布流
阶梯瀑布流的原理，是将堆叠柱状图的颜色设置为透明（关注代码高亮部分）。注意，这里使用了一个help数组以存放颜色透明的数据。
```javascript
let myChart = echarts.init(document.getElementById('main'));

let option = {};

var data = [900, 345, 393, -108, -154, 135, 178, 286, -119, -361, -203];
var help = [];
var positive = [];
var negative = [];
for (var i = 0, sum = 0; i < data.length; ++i) {
  if (data[i] >= 0) {
    positive.push(data[i]);
    negative.push('-');
  } else {
    positive.push('-');
    negative.push(-data[i]);
  }

  if (i === 0) {
    help.push(0);
  } else {
    sum += data[i - 1];
    if (data[i] < 0) {
      help.push(sum + data[i]);
    } else {
      help.push(sum);
    }
  }
}

option = {
  title: {
    text: 'Waterfall'
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    splitLine: { show: false },
    data: (function () {
      var list = [];
      for (var i = 1; i <= 11; i++) {
        list.push('Oct/' + i);
      }
      return list;
    })()
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      type: 'bar',
      stack: 'all',
      itemStyle: {
        normal: {
          barBorderColor: 'rgba(200,0,0,0)',
          color: 'rgba(200,0,0,0)'
        },
        emphasis: {
          barBorderColor: 'rgba(0,0,0,0)',
          color: 'rgba(0,0,0,0)'
        }
      },
      data: help
    },
    {
      name: 'positive',
      type: 'bar',
      stack: 'all',
      data: positive
    },
    {
      name: 'negative',
      type: 'bar',
      stack: 'all',
      data: negative,
      itemStyle: {
        color: '#f33'
      }
    }
  ]
};

myChart.setOption(option);
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/oNpRXBy)

<a name="tfEyo"></a>
### ✨  折线图
在 `series`中将`type`设置为`line`即可添加折线图。

示例：
```javascript
option = {
  xAxis: {
    type: 'category',
    data: ['A', 'B', 'C']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [120, 200, 150],
      type: 'line',
      lineStyle: {
        normal: {
          color: 'green',
          width: 4,
          type: 'dashed'
        }
      }
    }
  ]
};
```

其中：

- `[lineStyle](https://echarts.apache.org/zh/option.html#series-line.lineStyle)`设置线条样式，`type`可以为：solid、dashed、dotted

<a name="rDIZE"></a>
#### 在图表中添加折线
折线图可以和柱状图在同一个图表中，指定`series`为数组，可以创建多序列柱状图/折线图。

- 可以自定义Y轴坐标，通过`{value}`指定Y轴刻度；
- 通过`tooltip`的`valueFormatter`指定弹出工具箱格式化数值显示；

比如有如下配置：
```javascript
let option = {
  tooltip: {
    trigger: 'axis'
  },
  legend: {},
  xAxis: [
    {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      axisPointer: {
        type: 'shadow'
      }
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: 'Precipitation',
      alignTicks: true,
      axisLabel: {
        formatter: '{value} ml'
      }
    },
    {
      type: 'value',
      name: 'Temperature',
      axisLabel: {
        formatter: '{value} °C'
      }
    }
  ],
  series: [
    {
      name: 'Evaporation',
      type: 'bar',
      tooltip: {
        valueFormatter: value => value + ' ml'
      },
      data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    },
    {
      name: 'Precipitation',
      type: 'bar',
      tooltip: {
        valueFormatter: value => value + ' ml'
      },
      data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    },
    {
      name: 'Temperature',
      type: 'line',
      yAxisIndex: 1,
      tooltip: {
        valueFormatter: value => value + ' °C'
      },
      data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/wvpROPQ)

<a name="DeVRT"></a>
#### 笛卡尔坐标系中的折线图
将数据设置为二维数组，每一项即可表示一个坐标点，折线将在笛卡尔坐标系中连接这些坐标点：
```javascript
option = {
  xAxis: {},
  yAxis: {},
  series: [
    {
      data: [
        [20, 120],
        [50, 200],
        [40, 50]
      ],
      type: 'line'
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/RwxmPJm)

<a name="ZO0qA"></a>
#### 空数据
使用 `-`表示空数据
```javascript
option = {
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E']
  },
  yAxis: {},
  series: [
    {
      data: [0, 22, '-', 23, 19],
      type: 'line'
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/eYyqYEy)

<a name="gXccH"></a>
#### 堆叠折线图
跟堆叠柱状图类似，只需要指定相同的stack即可，可以使用`areaStyle`参数添加区域填充色：
```javascript
option = {
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E']
  },
  yAxis: {},
  series: [
    {
      data: [10, 22, 28, 43, 49],
      type: 'line',
      stack: 'x',
      areaStyle: {}
    },
    {
      data: [5, 4, 3, 5, 10],
      type: 'line',
      stack: 'x',
      areaStyle: {}
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/zYpgjxM)

<a name="peJxc"></a>
#### 区域面积图
跟堆叠折线图不同的是，区域面积图不需要指定stack，而是将areaStyle设置为透明，这样就可以直观得看出各块区域的面积区别。
```javascript
option = {
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E']
  },
  yAxis: {},
  series: [
    {
      data: [10, 22, 28, 23, 19],
      type: 'line',
      areaStyle: {}
    },
    {
      data: [25, 14, 23, 35, 10],
      type: 'line',
      areaStyle: {
        color: '#ff0',
        opacity: 0.5
      }
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/dyJxeGb)

<a name="eiXTU"></a>
#### 平滑曲线图
添加`smooth: true`选项，可以创建平滑曲线图：
```javascript
option = {
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E']
  },
  yAxis: {},
  series: [
    {
      data: [10, 22, 28, 23, 19],
      type: 'line',
      smooth: true
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/xxpvjgN)

<a name="c88BS"></a>
#### 阶梯线图
指定`step`参数，可以创建阶梯线图，可取值`start``middle``end`
```javascript
option = {
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: 'Step Start',
      type: 'line',
      step: 'start',
      data: [120, 132, 101, 134, 90, 230, 210]
    },
    {
      name: 'Step Middle',
      type: 'line',
      step: 'middle',
      data: [220, 282, 201, 234, 290, 430, 410]
    },
    {
      name: 'Step End',
      type: 'line',
      step: 'end',
      data: [450, 432, 401, 454, 590, 530, 510]
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/oNpKydG)

<a name="lS28x"></a>
### ✨  饼图
将 `series`的 `type`设置为 `pie`即可创建饼图。

<a name="ml0cB"></a>
#### 基础饼图
通过`dataset.source`设置数据：
```javascript
let option = {
  dataset:  {
    source: [
      ['Product', 'Sales'],
      ['Cake', 123],
      ['Cereal', 231],
      ['Tofu', 235],
      ['Dumpling', 341],
      ['Biscuit', 122],
    ]
  },
  series: [
    {
      type: 'pie',
      radius: 100,
    },
  ]
};
```

通过`series.data`设置数据：
```javascript
option = {
  series: [
    {
      type: 'pie',
      // label: {
      //   show: false
      // },
      data: [
        {
          value: 335,
          name: '直接访问'
        },
        {
          value: 234,
          name: '联盟广告'
        },
        {
          value: 1548,
          name: '搜索引擎'
        }
      ]
    }
  ]
};
```

效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/XWVOrMy)

对一些设置的说明：

- `radius`指定饼图半径
- 当 `label.show`设置为false的时候，不显示饼图标签

<a name="HRc3S"></a>
#### 平分饼图
如果一个饼图的各项数据value都相同，即便为0，则这个饼图被平分：
```javascript
option = {
  series: [
    {
      type: 'pie',
      // stillShowZeroSum: false,
      data: [
        {
          value: 0,
          name: '直接访问'
        },
        {
          value: 0,
          name: '联盟广告'
        },
        {
          value: 0,
          name: '搜索引擎'
        }
      ]
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/OJzKEad)

如果设置了`stillShowZeroSum: false`选项，则数据和为0的时候不会显示饼图。

<a name="i1eGA"></a>
#### 圆环图
将radius设置为数组，分别代表内外半径，即可表示一个圆环图
```javascript
option = {
  title: {
    text: '圆环图',
    left: 'center',
    top: 'center'
  },
  series: [
    {
      type: 'pie',
      data: [
        {
          value: 335,
          name: 'A'
        },
        {
          value: 234,
          name: 'B'
        },
        {
          value: 1548,
          name: 'C'
        }
      ],
      radius: ['40%', '70%']
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/PoEMBog)

如果想要在鼠标划上去的时候，高亮显示选中部分信息，实现思路为：将label.show默认设置为false，在label.emphasis.show将其设置为true，将label.position设置为center。
```javascript
option = {
  legend: {
    orient: 'vertical',
    x: 'left',
    data: ['A', 'B', 'C', 'D', 'E']
  },
  series: [
    {
      type: 'pie',
      radius: ['50%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center',
        emphasis: {
          show: true,
          fontSize: '50',
          fontWeight: 'bold' 
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 335, name: 'A' },
        { value: 310, name: 'B' },
        { value: 234, name: 'C' },
        { value: 135, name: 'D' },
        { value: 1548, name: 'E' }
      ]
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/BaJXOyQ)

<a name="ysZNJ"></a>
#### 玫瑰图（南丁格尔图）
设置`roseType: 'area'`，即可表现为玫瑰图：
```javascript
option = {
  series: [
    {
      type: 'pie',
      data: [
        {
          value: 100,
          name: 'A'
        },
        {
          value: 200,
          name: 'B'
        },
        {
          value: 300,
          name: 'C'
        },
        {
          value: 400,
          name: 'D'
        },
        {
          value: 500,
          name: 'E'
        }
      ],
      roseType: 'area'
    }
  ]
};
```

<a name="Kvlzi"></a>
### ✨  散点图
将 `series`的 `type`设置为 `scatter` 即可创建散点图。
```javascript
option = {
  xAxis: {
    data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  },
  yAxis: {},
  series: [
    {
      type: 'scatter',
      data: [220, 182, 191, 234, 290, 330, 310]
    }
  ]
};
```
示例：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/rNJBjRJ)

<a name="ROIxg"></a>
#### 笛卡尔坐标系下的散点图
将数据设置为二维数组，每一项即可表示一个坐标点，散点图将标记这些点：
```javascript
option = {
  xAxis: {},
  yAxis: {},
  series: [
    {
      type: 'scatter',
      data: [
        [10, 5],
        [0, 8],
        [6, 10],
        [2, 12],
        [8, 9]
      ]
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/YzeKNMb)

<a name="ROrAa"></a>
#### 设置散点图形
使用 `symbol`可以指定SVG图形为散点图形，使用`symbolSize`指定图形大小：
```javascript
option = {
  xAxis: {
    data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  },
  yAxis: {},
  series: [
    {
      type: 'scatter',
      data: [220, 182, 191, 234, 290, 330, 310],
      symbol: 'path://M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905 c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478 c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014 C52.216,18.553,51.97,16.611,51.911,16.242z',
      symbolSize: function (value) {
        return value / 10;
      }
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/oNEvBrV)

symbol除了设置为svg的path路径之外，还可以从本地加载图片或从网络加载图片。

示例：使用svg的path作为散点图形：
```javascript
symbol: 'path://M51.911,16.242C51.152,7.888,45.239,1.827,37.839,1.827c-4.93,0-9.444,2.653-11.984,6.905 c-2.517-4.307-6.846-6.906-11.697-6.906c-7.399,0-13.313,6.061-14.071,14.415c-0.06,0.369-0.306,2.311,0.442,5.478 c1.078,4.568,3.568,8.723,7.199,12.013l18.115,16.439l18.426-16.438c3.631-3.291,6.121-7.445,7.199-12.014 C52.216,18.553,51.97,16.611,51.911,16.242z'
```
示例：从本地加载图片作为散点图形：
```javascript
symbol: 'image://../image/love.svg'
```
示例：从网络加载图片作为散点图形：
```javascript
symbol: 'image://https://iconfont.alicdn.com/t/122897f9-f664-4e46-82d8-07e7144ff003.png'
```

<a name="XdSHA"></a>
### ✨  地图
地图数据可以到阿里数据可视化平台DataV.GeoAtlas中获取：<br />[DataV.GeoAtlas地理小工具系列](https://datav.aliyun.com/portal/school/atlas/area_selector)


<a name="fE8za"></a>
## 📃 图表样式配置
<a name="YIXcb"></a>
### ✨  标签
通过`label`可以设置标签样式，将其`show`设置为true，显示数值：
```javascript
option = {
  xAxis: {
    data: ['A', 'B', 'C', 'D', 'E']
  },
  yAxis: {},
  series: [
    {
      data: [10, 22, 28, 23, 19],
      type: 'bar',
      label: {
        show: true,
        position: 'top',
        textStyle: {
          fontSize: 20
        }
      }
    }
  ]
};
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/bGaXGoe)

label常见的参数配置如下：

| 选项 | 类型 | 说明 | 取值说明 |
| --- | --- | --- | --- |
| <a name="hjfVi"></a>
#### [show](https://echarts.apache.org/zh/option.html#series-line.label.show)
 | boolean | 是否显示标签。 |  |
| <a name="KPl68"></a>
#### [position](https://echarts.apache.org/zh/option.html#series-line.label.position)
 | string Array | 标签的位置。 | 字符串示例：<br />top / left / right / bottom / inside / insideLeft / insideRight / insideTop / insideBottom / insideTopLeft / insideBottomLeft / insideTopRight / insideBottomRight<br />数组示例：<br />[10, 10] / ['50%', '50%'] |
| <a name="hkeGe"></a>
#### [distance](https://echarts.apache.org/zh/option.html#series-line.label.distance)
 | number | 距离图形元素的距离。 | 当 position 为字符描述值（如 'top'、'insideRight'）时候有效。 |
| <a name="mlxJ4"></a>
#### [rotate](https://echarts.apache.org/zh/option.html#series-line.label.rotate)
 | number | 标签旋转。 | 从 -90 度到 90 度。正值是逆时针。 |
| <a name="rhvPK"></a>
#### [formatter](https://echarts.apache.org/zh/option.html#series-line.label.formatter)
 | string Function | 标签内容格式器。 | 支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \\n 换行。 |
| <a name="VPq8C"></a>
#### [color](https://echarts.apache.org/zh/option.html#series-line.label.color)
 | Color | 如果设置为 'inherit'，则为视觉映射得到的颜色，如系列色。 |  |
| <a name="uCTv8"></a>
#### [fontStyle](https://echarts.apache.org/zh/option.html#series-line.label.fontStyle)
 | string | 文字字体的风格。 | normal / italic / oblique |
| <a name="J8FcX"></a>
#### [fontWeight](https://echarts.apache.org/zh/option.html#series-line.label.fontWeight)
 | string number | 文字字体的粗细。 | normal / bold / bolder / lighter<br />100 &#124; 200 &#124; 300 &#124; 400 ... |
| <a name="CUkGd"></a>
#### [fontFamily](https://echarts.apache.org/zh/option.html#series-line.label.fontFamily)
 | string | 文字的字体系列。 | 'serif' , 'monospace', 'Arial', 'Courier New', 'Microsoft YaHei', ... |


label配置项包括：位置、偏移、宽高、字体、大小、颜色、边框、描边、阴影、溢出隐藏、富文本标签等。

label更多的配置项详见文档：

- [series-line.label](https://echarts.apache.org/zh/option.html#series-line.label)
- [series-bar.label](https://echarts.apache.org/zh/option.html#series-bar.label)
- [series-pie.label](https://echarts.apache.org/zh/option.html#series-pie.label)
- [series-scatter.label](https://echarts.apache.org/zh/option.html#series-scatter.label)
- [series-effectScatter.label](https://echarts.apache.org/zh/option.html#series-effectScatter.label)
- [series-map.label](https://echarts.apache.org/zh/option.html#series-map.label)

示例：[bar-label-rotation](https://echarts.apache.org/examples/zh/editor.html?c=bar-label-rotation)<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/wvpVavE)

示例：[label-position](https://echarts.apache.org/examples/zh/editor.html?c=doc-example/label-position)<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/BaJXNNO)


<a name="RmIFk"></a>
## 📃 一些有趣的特性
<a name="e32Lx"></a>
### ✨  富文本标签
参考：[富文本标签](https://echarts.apache.org/zh/tutorial.html#%E5%AF%8C%E6%96%87%E6%9C%AC%E6%A0%87%E7%AD%BE)


<a name="CtJtk"></a>
### ✨  异步加载图表
如果数据为异步获取，可以先渲染一个空的坐标系，待数据响应后，再填充数据。在数据获取期间，可以显示loading图以表示数据获取中。

示例：使用setTimeout模拟数据获取的过程
```javascript
let myChart = echarts.init(document.getElementById('main'));

// 显示loading占位
myChart.showLoading();

// 显示标题，图例和空的坐标轴等
myChart.setOption({
  title: {
    text: '异步数据加载示例'
  },
  tooltip: {},
  xAxis: {
    data: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  },
  yAxis: {},
  series: [
    {
      type: 'scatter',
      data: []
    }
  ]
});

setTimeout(() => {
  // 隐藏loading
  myChart.hideLoading();
  // 设置数据
  myChart.setOption({
    series: [
      {
        type: 'scatter',
        data: [220, 182, 191, 234, 290, 330, 310],
        symbol: 'image://https://iconfont.alicdn.com/t/122897f9-f664-4e46-82d8-07e7144ff003.png',
        symbolSize: function (value) {
          return value / 10;
        }
      }
    ]
  });
}, 3000)
```
效果：<br />[点击查看【codepen】](https://codepen.io/quanzaiyu/embed/poazeLV)


<a name="aVpL8"></a>
## 📃 在微信小程序中使用echarts

使用 [echarts-for-weixin](https://github.com/ecomfe/echarts-for-weixin) 可以在微信小程序中使用echarts


<a name="kEdu0"></a>
## 📃 服务器端渲染echarts图表
服务器端渲染只需要将ssr设置为true，选择渲染模式renderer为svg或canvas即可。

示例：通过node.js开启服务，服务器端创建图表，通过svg渲染并返回数据：
```javascript
var http = require("http");
var echarts = require("echarts");

function renderChart() {
  const chart = echarts.init(null, null, {
    renderer: "svg",
    ssr: true,
    width: 400,
    height: 300
  });

  chart.setOption({
    legend: {
      orient: "vertical",
      x: "left",
      data: ["A", "B", "C", "D", "E"]
    },
    series: [
      {
        type: "pie",
        radius: ["50%", "70%"],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: "center",
          emphasis: {
            show: true,
            fontSize: "50",
            fontWeight: "bold"
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 335, name: "A" },
          { value: 310, name: "B" },
          { value: 234, name: "C" },
          { value: 135, name: "D" },
          { value: 1548, name: "E" }
        ]
      }
    ]
  });

  return chart.renderToSVGString();
}

http
  .createServer(function (req, res) {
    res.writeHead(200, {
      "Content-Type": "application/xml"
    });
    res.write(renderChart());
    res.end();
  })
  .listen(8000);
```

现在已知的问题是：使用服务器端渲染，用户交互不生效。

参考：[服务端渲染 ECharts 图表](https://echarts.apache.org/handbook/zh/how-to/cross-platform/server)

<a name="CrM6Q"></a>
## 📃 图表示例站点

- [Made a pie](https://madeapie.com/#/)
- [DataInsight](http://analysis.datains.cn/finance-admin/index.html#/chartLib/all)

[PPChart - 让图表更简单](http://ppchart.com/#/)<br />[EChartsDemo集](https://www.isqqw.com/)

<a name="FWOYT"></a>
## 📃 大屏展示项目

- [GItee: Lang / 大屏数据展示模板](https://gitee.com/lvyeyou/DaShuJuZhiDaPingZhanShi)
- [Gitee: 陌生人 / BigDataView](https://gitee.com/iGaoWei/big-data-view)



