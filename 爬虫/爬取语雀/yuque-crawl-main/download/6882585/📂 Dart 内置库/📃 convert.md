API参考：[dart:convert library](https://api.dart.dev/stable/2.10.4/dart-convert/dart-convert-library.html)

引入：
```dart
import 'dart:convert';
```

<a name="I6exV"></a>
## 一、json
将字符串转换为对象：
```dart
import 'dart:convert' show json;

var jsonString = '''
[
  {"score": 40},
  {"score": 80}
]
''';

var scores = json.decode(jsonString);
assert(scores is List);
assert(scores[0] is Map);
assert(firstScore['score'] == 40);
print(scores); // [{score: 40}, {score: 80}]
```

将对象转换为字符串：
```dart
var scores = [
  {'score': 40},
  {'score': 80},
];

var jsonText = json.encode(scores);
print(jsonText); // [{"score":40},{"score":80}]
```

- `json.decode` 可以写为 `jsonDecode` 
- `json.encode` 可以写为 `jsonEncode`

<a name="K2Ebn"></a>
## 二、utf8
使用 `utf8.encode` 和 `utf8.decode` 编码和解码数据：
```dart
import 'dart:convert' show utf8;

var str = 'Hello world';

var strEncode = utf8.encode(str);
print(strEncode); // [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
print(strEncode is List<int>); // true

var strDecode = utf8.decode(strEncode);
print(strDecode == str); // true
```


