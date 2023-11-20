<a name="p9b4p"></a>
## 概述
[dart:core 库](https://api.dart.dev/stable/2.10.4/dart-core/dart-core-library.html)提供了一个少量但是重要的内置功能集合。 该库会被自动导入每个 Dart 程序。

包括：内置类型，集合和其他核心功能。 

<a name="0W1Dm"></a>
## 控制台打印
顶级 `print()` 方法接受一个参数 任意对象） 并输出显示这个对象的字符串值(由 `toString()` 返回) 到控制台。
```dart
  var name = "xiaoyu";
  print('My name is $name.');
```


通过 `$` 可以在字符串中引入变量名。

<a name="nG6wt"></a>
## 数字
相关内容：<br />[📃 数据类型](https://www.yuque.com/xiaoyulive/dart/kpt7ev?inner=531aadcd&view=doc_embed)

参考：[数字](https://www.dartcn.com/guides/libraries/library-tour#%E6%95%B0%E5%AD%97)

<a name="AQ2Oy"></a>
## 字符串
相关内容：<br />[📃 数据类型](https://www.yuque.com/xiaoyulive/dart/kpt7ev?inner=cc4dd1da&view=doc_embed)

<a name="7zOb5"></a>
### StringBuffer
要以代码方式生成字符串，可以使用 StringBuffer 。 在调用 `toString()` 之前， StringBuffer 不会生成新字符串对象。 `writeAll()` 的第二个参数为可选参数，用来指定分隔符， 下例中使用空格作为分隔符。
```dart
var sb = StringBuffer();
sb
  ..write('Use a StringBuffer for ')
  ..writeAll(['efficient', 'string', 'creation'], ' ')
  ..write('.');

var fullString = sb.toString();

print(fullString); // Use a StringBuffer for efficient string creation.
```

<a name="iKLyv"></a>
### 正则表达式
RegExp类提供与JavaScript正则表达式相同的功能。 使用正则表达式可以对字符串进行高效搜索和模式匹配。
```dart
// 下面正则表达式用于匹配一个或多个数字。
var numbers = RegExp(r'\d+');

var allCharacters = 'llamas live fifteen to twenty years';
var someDigits = 'llamas live 15 to 20 years';

// contains() 能够使用正则表达式。
print(allCharacters.contains(numbers)); // false
print(someDigits.contains(numbers)); // true

// 替换所有匹配对象为另一个字符串。
var exedOut = someDigits.replaceAll(numbers, 'XX');
print(exedOut); // llamas live XX to XX years
```

直接使用正则表达式中的某些方法（hasMatch、allMatches）：
```dart
var numbers = RegExp(r'\d+');
var someDigits = 'llamas live 15 to 20 years';

// 检查正则表达式是否在字符串中匹配到对象。
print(numbers.hasMatch(someDigits)); // true

// 迭代所有匹配对象
for (var match in numbers.allMatches(someDigits)) {
  print(match.group(0)); // 15, then 20
}
```

参考：[字符和正则表达式](https://www.dartcn.com/guides/libraries/library-tour#%E5%AD%97%E7%AC%A6%E5%92%8C%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F)

<a name="TuVzd"></a>
## URI
[Uri 类](https://api.dart.dev/stable/2.10.4/dart-core/Uri-class.html) 提供对字符串的编解码操作。 这些函数用来处理 URI 特有的字符，例如 `＆` 和 `=` 。 Uri 类还可以解析和处理 URI—host，port，scheme等组件。

<a name="d8U6o"></a>
### 编码和解码
使用 `encodeFull()` 和 `decodeFull()` 方法， 对 URI 中除了特殊字符（例如 `/`， `:`， `&`， `#`）以外的字符进行编解码， 这些方法非常适合编解码完整合法的 URI，并保留 URI 中的特殊字符。
```dart
var uri = 'http://example.org/api?foo=some message';

var encoded = Uri.encodeFull(uri); // http://example.org/api?foo=some%20message
print(encoded);

var decoded = Uri.decodeFull(encoded);
print(uri == decoded); // true
```
使用 `encodeComponent()` 和 `decodeComponent()` 方法， 对 URI 中具有特殊含义的所有字符串字符，特殊字符包括（但不限于）`/`， `&`， 和 `:`。
```dart
var uri = 'http://example.org/api?foo=some message';

var encoded = Uri.encodeComponent(uri);
print(encoded); // http%3A%2F%2Fexample.org%2Fapi%3Ffoo%3Dsome%20message

var decoded = Uri.decodeComponent(encoded);
print(uri == decoded); // true
```

<a name="p5xUY"></a>
### 解析URI
使用 Uri 对象的字段（例如 `path`）， 来获取一个 Uri 对象或者 URI 字符串的一部分。 使用 `parse()` 静态方法，可以使用字符串创建 Uri 对象。
```dart
var uri = Uri.parse('http://example.org:8080/foo/bar#frag');

print(uri.scheme); // http
print(uri.host); // example.org
print(uri.path); // /foo/bar
print(uri.fragment); // frag
print(uri.origin); // http://example.org:8080
```
<a name="hErRb"></a>
#### 
<a name="1ic1Y"></a>
### 构建URI
使用 `Uri()` 构造函数，可以将各组件部分构建成 URI 。<br />
```dart
  var uri = Uri(scheme: 'http', host: 'example.org', path: '/foo/bar', fragment: 'frag');
  assert(uri.toString() == 'http://example.org/foo/bar#frag');
```

参考：[URI](https://www.dartcn.com/guides/libraries/library-tour#uri)

<a name="Ufg8a"></a>
## DateTime和Duration
<a name="4dvv0"></a>
### 创建日期时间对象
```dart
// 获取当前时刻。
var now = DateTime.now();
print(now); // 2020-12-17 16:28:20.650318

// 根据本地时区创建 DateTime 对象。
var y2k = DateTime(2000);
print(y2k); // 2000-01-01 00:00:00.000

// 指定年月日。
y2k = DateTime(2000, 1, 2);
print(y2k); // 2000-01-02 00:00:00.000

// 将日期指定为 UTC 时区。
y2k = DateTime.utc(2000);
print(y2k); // 2000-01-01 00:00:00.000Z

// 指定自Unix纪元以来，以毫秒为单位的日期和时间。
y2k = DateTime.fromMillisecondsSinceEpoch(946684800000, isUtc: true);
print(y2k); // 2000-01-01 00:00:00.000Z

// 解析ISO 8601日期。
y2k = DateTime.parse('2000-01-01T00:00:00Z');
print(y2k); // 2000-01-01 00:00:00.000Z
```

<a name="J6O8D"></a>
### 日期时间计算
在Dart中的日期时间计算尤其简单，通过简单的 `add` 和 `subtract` 结合 `Duration` 对象即可完成。
```dart
var y2k = DateTime.utc(2000);

// 增加一年。
var y2001 = y2k.add(const Duration(days: 366));
print(y2001.year); // 2001

// 减少30天。
var december2000 = y2001.subtract(const Duration(days: 30));
print(december2000.year); // 2000
print(december2000.month); // 12

// 计算两个时刻之间的查，
// 返回 Duration 对象。
var duration = y2001.difference(y2k);
print(duration.inDays); // 366 (y2k was a leap year.)
```

参考：[日期和时间](https://www.dartcn.com/guides/libraries/library-tour#%E6%97%A5%E6%9C%9F%E5%92%8C%E6%97%B6%E9%97%B4)、[DateTime](https://api.dart.dev/stable/2.10.4/dart-core/DateTime-class.html)、[Duration](https://api.dart.dev/stable/2.10.4/dart-core/Duration-class.html)

<a name="hmt1L"></a>
## 比较（Comparable）
如果实现了 [Comparable](https://api.dartlang.org/stable/dart-core/Comparable-class.html) 接口， 也就是说可以将该对象与另一个对象进行比较， 通常用于排序。 `compareTo()` 方法在 _小于_ 时返回 < 0， 在 _相等_ 时返回 0， 在 _大于_ 时返回 > 0。
```dart
void main() {
  var short = const Line(1);
  var long = const Line(100);
  print(short.compareTo(long)); // -99
}

class Line implements Comparable<Line> {
  final int length;
  const Line(this.length);

  @override
  int compareTo(Line other) => length - other.length;
}
```

<a name="55iCP"></a>
## 迭代（Iterator）
Iterable][] 和 [Iterator](https://api.dart.dev/stable/2.10.4/dart-core/Iterator-class.html) 类支持 for-in 循环。 当创建一个类的时候，继承或者实现 Iterable，可以为该类提供用于 for-in 循环的 Iterators。 实现 Iterator 来定义实际的遍历操作。

比如迭代一个很长的字符串，遇到空格则进入下一次迭代，每次返回当前空格前的字符串：
```dart
void main() {
  const myString = 'This is a long string that I want to iterate over.';
  final myIterable = TextRuns(myString);
  for (var textRun in myIterable) {
    print(textRun);
  }
}

class TextRuns extends Iterable<String> {
  TextRuns(this.text);
  final String text;

  @override
  Iterator<String> get iterator => TextRunIterator(text);
}

class TextRunIterator implements Iterator<String> {
  TextRunIterator(this.text);
  final String text;

  String _currentTextRun;
  int _startIndex = 0;
  int _endIndex = 0;

  final breakChar = RegExp(' ');

  // 当前迭代的元素
  @override
  String get current => _currentTextRun;

  // 下一次迭代
  @override
  bool moveNext() {
    _startIndex = _endIndex;

    // 迭代结束（迭代出口：当前文本已遍历完成）
    if (_startIndex == text.length) {
      _currentTextRun = null;
      return false;
    }

    // 获取下一个迭代元素（遇到空格就返回一次）
    final next = text.indexOf(breakChar, _startIndex);
    _endIndex = (next != -1) ? next + 1 : text.length;
    _currentTextRun = text.substring(_startIndex, _endIndex);
    return true;
  }
}
```
输出：
```dart
This 
is 
a 
long 
string 
that 
I 
want 
to 
iterate 
over.
```

如果需要在循环中添加循环条件，可以使用 `where` ：
```dart
  myIterable
      .where((str) => str.length > 3)
      .forEach((element) => print(element));
```
输出：
```dart
This 
long 
string 
that 
want 
iterate 
over.
```

