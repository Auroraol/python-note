dart:math 库提供通用的功能，例如，正弦和余弦， 最大值和最小值，以及数学常数，例如 _pi_ 和 _e_。 大多数在 Math 库中的功能是作为顶级函数实现的。

引入：
```dart
import 'dart:math';
```

<a name="nZFQT"></a>
## 一、数学常量及方法<br />
相关常量：
```dart
const double e = 2.718281828459045;
const double ln10 = 2.302585092994046;
const double ln2 = 0.6931471805599453;
const double log2e = 1.4426950408889634;
const double log10e = 0.4342944819032518;
const double pi = 3.1415926535897932;
const double sqrt1_2 = 0.7071067811865476;
const double sqrt2 = 1.4142135623730951;
```

相关方法：
```dart
external T min<T extends num>(T a, T b);
external T max<T extends num>(T a, T b);

external double atan2(num a, num b);
external num pow(num x, num exponent);

external double sin(num radians);
external double cos(num radians);
external double tan(num radians);
external double acos(num x);
external double asin(num x);
external double atan(num x);

external double sqrt(num x);
external double exp(num x);
external double log(num x);
```

<a name="Wthe2"></a>
## 二、随机数
使用 Random 类产生随机数。 可以为 Random 构造函数提供一个可选的种子参数。

生成数字随机数：
```dart
var random = Random();
random.nextDouble(); // Between 0.0 and 1.0: [0, 1)
random.nextInt(10); // Between 0 and 9.
```

生成布尔随机数：
```dart
var random = Random();
random.nextBool(); // true or false
```

