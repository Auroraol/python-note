通过 Dio 我们可以将文件上传到阿里OSS。
```dart
import 'dart:convert';
import 'dart:io';
import 'package:crypto/crypto.dart';
import 'package:dio/dio.dart';
import 'package:uuid/uuid.dart';

class HttpUtil {
  static HttpUtil instance;
  Dio dio;
  BaseOptions options;

  // oss相关参数
  static String ossPath = 'https://xxx.oss-cn-shenzhen.aliyuncs.com';
  static String accesskeyId= 'your accesskeyId';
  static String accesskeySecret= 'your accesskeySecret';
  static String uploadBaseUrl = 'test/flutter';
  static String policyText = '{"expiration": "2020-01-01T12:00:00.000Z","conditions": [["content-length-range", 0, '
      '1048576000]]}'; // 验证文本域

  // 签名相关
  static List<int> policyText_utf8 = utf8.encode(policyText); // 进行utf8编码
  static String policy_base64 = base64.encode(policyText_utf8); // 进行base64编码
  static List<int> policy = utf8.encode(policy_base64); // 再次进行utf8编码
  static List<int> key = utf8.encode(accesskeySecret); // 进行utf8 编码
  static List<int> signature_pre  = new Hmac(sha1, key).convert(policy).bytes; // 通过hmac,使用sha1进行加密
  String signature = base64.encode(signature_pre); // 最后一步，将上述所得进行base64 编码

  HttpUtil() {
    options = BaseOptions(
      connectTimeout: 10000,
      receiveTimeout: 10000,
      headers: {},
    );
    dio = new Dio(options);
  }

  oss(File file) async { // 接受一个 File 类型的参数
    var ext = file.path.split('.').last; // 获取文件扩展名
    var userId = (await Storage.get('userInfo'))['id'].toString();
    var now = (new DateTime.now()).toString();
    var uuid = new Uuid();
    var filename = uuid.v5(Uuid.NAMESPACE_URL, now + userId); // 通过当前时间和userId生成uuid

    // 构建 FormData
    FormData data = new FormData.from({
      'Filename': '文件名，随意',
      'key' : "$uploadBaseUrl/$filename.$ext",
      'policy': policy_base64,
      'OSSAccessKeyId': accesskeyId,
      'success_action_status' : '200', // 让服务端返回200，不然，默认会返回204
      'signature': signature,
      'file': new UploadFileInfo(file, "imageFileName")
    });

    try {
      Response response = await dio.post(ossPath, data: data);
      var uploadPath = "$ossPath/$uploadBaseUrl/$filename.$ext";
      print("上传成功: $uploadPath");
      return uploadPath; // 返回上传路径
    } on DioError catch(e) {
      print("上传失败: $e");
    }
  }
}
```

使用的时候：
```dart
Future getImage() async {
  try {
    File image = await ImagePicker.pickImage(source: ImageSource.gallery);
    var uploadPath = await HttpUtil().oss(image);
    print(uploadPath);
  } catch (e) {}
}
```

这里, 使用了 [ImagePicker](https://pub.dev/packages/image_picker) 从相册或拍照获取文件, 需要引入包：
```dart
import 'package:image_picker/image_picker.dart';
```

本文使用到的一些依赖：
```yaml
dependencies:
  dio: ^2.1.0
  image_picker: ^0.6.1+4
  crypto: ^2.1.3
  uuid: ^2.0.1
```

