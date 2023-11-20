[dio](https://pub.dev/packages/dio) 是一个强大的 Dart Http 请求库，支持 Restful API、FormData、拦截器、请求取消、Cookie 管理、文件上传/下载、超时等。

安装：
```yaml
dependencies:
  dio: ^2.1.0
```

相关 API：

- Future get(...)
- Future post(...)
- Future put(...)
- Future delete(...)
- Future head(...)
- Future put(...)
- Future path(...)
- Future download(...)

<a name="6e9c3987"></a>
## GET 请求
```dart
import 'package:dio/dio.dart';

void getHttp() async {
  try {
    Response response = await Dio().get("https://www.baidu.com");
    print(response.data.toString());
  } catch (e) {
    print(e);
  }
}
getHttp();
```

查询字符串可通过参数传递：
```dart
response = await Dio().get("/test", queryParameters: {"id": 12, "name": "wendu"});
```

<a name="b091ff52"></a>
## POST 请求
```dart
var dio = new Dio();
Response response = await dio.post("/test", data: {"id": 12, "name": "wendu"});
print(response.data.toString());
```

发送 FormData：<br />适合于 `Content-Type` 为 `application/x-www-form-urlencoded` 或 `multipart/form-data`
```dart
FormData formData = new FormData.from({
  "name": "wendux",
  "age": 25,
});
var response = await dio.post("/info", data: formData);
```

<a name="f7232c15"></a>
## 发起多个并发请求
```dart
Response response = await Future.wait([dio.post("/info"), dio.get("/token")]);
```

<a name="e7fd6f3f"></a>
## 下载与下载
下载文件：
```dart
Response response = await dio.download("https://www.baidu.com", "./baidu.html");
```

上传文件：
```dart
FormData formData = new FormData.from({
    "name": "wendux",
    "age": 25,
    "file1": new UploadFileInfo(new File("./upload.txt"), "upload1.txt"),
    //支持直接上传字节数组 (List<int>) ，方便直接上传内存中的内容
    "file2": new UploadFileInfo.fromBytes(
        utf8.encode("hello world"), "word.txt"),
    // 支持文件数组上传
    "files": [
        new UploadFileInfo(new File("./example/upload.txt"), "upload.txt"),
        new UploadFileInfo(new File("./example/upload.txt"), "upload.txt")
    ]
});
var response = await dio.post("/info", data: formData);
```

监听上传数据进度：
```dart
var response = await dio.post(
  "http://www.dtworkroom.com/doris/1/2.0.0/test",
  data: {"aa": "bb" * 22},
  onSendProgress: (int sent, int total) {
    print("$sent $total");
  },
);
```

<a name="e2bbec61"></a>
## 请求配置
下面是所有的请求配置选项。如果请求 method 没有指定，则默认为 GET：
```dart
{
  /// Http method.
  String method;

  /// 请求基地址,可以包含子路径，如: "https://www.google.com/api/".
  String baseUrl;

  /// Http请求头.
  Map<String, dynamic> headers;

  /// 连接服务器超时时间，单位是毫秒.
  int connectTimeout;

  /// 2.x中为接收数据的最长时限.
  int receiveTimeout;

  /// 请求路径，如果 `path` 以 "http(s)"开始, 则 `baseURL` 会被忽略； 否则, 将会和baseUrl拼接出完整的的url.
  String path = "";

  /// 请求的Content-Type，默认值是 `ContentType.JSON`.
  /// 如果您想以"application/x-www-form-urlencoded"格式编码请求数据
  /// 可以设置此选项为 `ContentType.parse("application/x-www-form-urlencoded")`,  这样Dio就会自动编码请求体.
  ContentType contentType;

  /// [responseType] 表示期望以那种格式(方式)接受响应数据。
  /// 目前 [ResponseType] 接受三种类型 `JSON`, `STREAM`, `PLAIN`.
  ///
  /// 默认值是 `JSON`, 当响应头中content-type为"application/json"时，dio 会自动将响应内容转化为json对象。
  /// 如果想以二进制方式接受响应数据，如下载一个二进制文件，那么可以使用 `STREAM`.
  ///
  /// 如果想以文本(字符串)格式接收响应数据，请使用 `PLAIN`.
  ResponseType responseType;

  /// `validateStatus` 决定http响应状态码是否被dio视为请求成功， 返回`validateStatus`
  ///  返回`true` , 请求结果就会按成功处理，否则会按失败处理.
  ValidateStatus validateStatus;

  /// 用户自定义字段，可以在 [Interceptor]、[Transformer] 和 [Response] 中取到.
  Map<String, dynamic> extra;

  /// 公共query参数
  Map<String, dynamic /*String|Iterable<String>*/ > queryParameters;
}
```

完整示例：
```dart
void getHttp() async {
  try {
    var dio = new Dio(new BaseOptions(
      baseUrl: "http://172.16.10.121/",
      connectTimeout: 5000,
      receiveTimeout: 100000,
      headers: {
        'Authorization': "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      },
      contentType: ContentType.parse("application/x-www-form-urlencoded"),
      responseType: ResponseType.json,
    ));

    FormData formData = new FormData.from({
      'name': '测试',
    });
    var response = await dio.post('admin/role/add', data: formData);
    print(response.data);
  } catch (e) {
    // 比如授权认证失败: 401 进入catch
    print(e);
  }
}
getHttp();
```

针对某个请求进行配置：
```dart
var response = await dio.post(url, options: Options(
                contentType: ContentType.JSON
              ));
```

<a name="aa6070a7"></a>
## 响应数据
当请求成功时会返回一个 Response 对象，它包含如下字段：
```dart
{
  var data; // 响应数据
  HttpHeaders headers; // 响应头
  Options request; // 本次请求信息
  int statusCode; // Http status code.
  bool isRedirect; // 是否重定向
  List<RedirectInfo> redirects; // 重定向信息
  Uri realUri; // 最终真正的请求地址(因为可能会重定向)
  Map<String, dynamic> extra; // 响应对象的自定义字段（可以在拦截器中设置它），调用方可以在`then`中获取.
}
```

<a name="f7ae864d"></a>
## 拦截器

- [flutetr dio 拦截器实现 token 失效刷新](https://www.jianshu.com/p/217a968dbc80)
- [dio 文档 - 拦截器](https://github.com/flutterchina/dio/blob/master/README-ZH.md#%E6%8B%A6%E6%88%AA%E5%99%A8)
