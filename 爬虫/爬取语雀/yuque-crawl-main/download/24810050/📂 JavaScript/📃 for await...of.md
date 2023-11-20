- [MDN：for...await](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for-await...of)


<a name="P8Kfz"></a>
## 迭代异步可迭代对象

- [MDN：asyncIterator](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator)

`Symbol.asyncIterator` 符号指定了一个对象的默认异步迭代器。如果一个对象设置了这个属性，它就是异步可迭代对象，可用于[for await...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of)循环。

定义一个异步可迭代对象：
```javascript
let asyncIterable = {
  [Symbol.asyncIterator]() {
    return {
      i: 0,
      next() {
        if (this.i < 3) {
          return Promise.resolve({ value: this.i++, done: false });
        }

        return Promise.resolve({ done: true });
      }
    };
  }
};

```
使用for...await可以迭代异步可迭代对象：
```javascript

(async function() {
   for await (num of asyncIterable) {
     console.log(num);
   }
})();
```

<a name="XHq99"></a>
## 迭代异步生成器
定义一个生成器
```javascript
async function* asyncGenerator() {
  let i = 0;
  while (i < 3) {
    yield i++;
  }
}
```
也可以通过以下方式定义异步可迭代生成器：
```javascript
const asyncGenerator = new Object();
asyncGenerator[Symbol.asyncIterator] = async function*() {
  let i = 0;
  while (i < 3) {
    yield i++;
  }
};
```
使用for...await可以迭代异步生成器：
```javascript
(async function() {
  for await (num of asyncGenerator()) {
    console.log(num);
  }
})();
```



