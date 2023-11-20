<a name="VWCkM"></a>
## 从一个简单的示例讲起
以下是一个使用了语音合成API的网页：
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <input id="input" />
  <button onclick="read()">阅读</button>

  <script>
    function read() {
      let input = document.getElementById('input');
      let inputValue = input.value;
      console.log(inputValue);
      let voiceValue = new SpeechSynthesisUtterance(inputValue);
      speechSynthesis.speak(voiceValue);
    }
  </script>
</body>
</html>
```
在输入框中输入值，点击“阅读”按钮，可以在浏览器中发出阅读输入的值。













<a name="q9ene"></a>
## 参考资料

- [MDN：SpeechSynthesisUtterance](https://developer.mozilla.org/zh-CN/docs/Web/API/SpeechSynthesisUtterance)
- [MDN：SpeechSynthesis](https://developer.mozilla.org/zh-CN/docs/Web/API/SpeechSynthesis)
- [HTML5语音合成Speech Synthesis API简介](https://www.zhangxinxu.com/wordpress/2017/01/html5-speech-recognition-synthesis-api/)





