<a name="Ig4Pu"></a>
## 判断是否是微信内置浏览器打开
```typescript
function isWeixn(){
  var ua = navigator.userAgent.toLowerCase();
  if(ua.match(/MicroMessenger/i)=="micromessenger") {
    return true;
  } else {
    return false;
  }
}
```


<a name="aF8N1"></a>
## 生成有序数组
有以下几种方式生成有序数组，结果都一样：
```javascript
// const generateArray = (start, end) => Array.from(new Array(end + 1).keys()).slice(start)
// const generateArray = (start, end) => new Array(end - start + 1).fill().map((item, i) => start + i)
const generateArray = (start, end) => Array.from({ length: end - start + 1 }).fill().map((item, i) => start + i)

console.log(generateArray(2000, 2010))
```




