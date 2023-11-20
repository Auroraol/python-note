在实际开发中，可能会遇到这样一个问题：

某个页面请求的接口都需要携带token，而此页面同时调用了多个接口。如果token失效，将会发起“刷新token”的请求。但只是一个接口还好，刷新token后返回的就是最新的token，而多个接口一起访问都返回401后，将会去刷新token，导致第一次返回了刷新后的token，后面调用的接口都将刷新失败。

第一个接口访问，token过期，返回401：<br />![Snipaste_2021-02-22_09-10-42.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956339202-6d792fc5-b57c-45fb-a2ed-2e461050b72c.png#align=left&display=inline&height=241&originHeight=241&originWidth=809&size=7665&status=done&style=none&width=809)<br />第二个接口访问，token过期，返回401：![Snipaste_2021-02-22_09-11-01.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956339888-06481725-10da-4ecd-9d94-d812af0029a0.png#align=left&display=inline&height=248&originHeight=248&originWidth=824&size=7821&status=done&style=none&width=824)<br />第一个接口触发的刷新token，正常返回：<br />![Snipaste_2021-02-22_09-11-23.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956340567-41100603-277f-47bd-ae8b-233acc776e6d.png#align=left&display=inline&height=353&originHeight=353&originWidth=1168&size=16583&status=done&style=none&width=1168)<br />![Snipaste_2021-02-22_09-13-43.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956461113-5ab893da-13f9-47ff-a053-2ac38288bc7c.png#align=left&display=inline&height=255&originHeight=255&originWidth=1127&size=11478&status=done&style=none&width=1127)

第二个接口触发的刷新token，由于携带的还是之前的token，导致返回401：<br />![Snipaste_2021-02-22_09-11-40.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956341632-02ec9e34-ee5a-4523-a240-c4bd8bac5f1f.png#align=left&display=inline&height=367&originHeight=367&originWidth=1192&size=14948&status=done&style=none&width=1192)<br />![Snipaste_2021-02-22_09-13-57.png](https://cdn.nlark.com/yuque/0/2021/png/2213540/1613956465905-13e1ce56-ff35-4ff7-af61-c6d08e035e0d.png#align=left&display=inline&height=223&originHeight=223&originWidth=829&size=6013&status=done&style=none&width=829)

每次刷新token之后，localstorage将会存储最新获取到的token，但由于第二次刷新token后返回的是401，所以存储的token将会被清空，然后退出到登录页面。大致逻辑如下：<br />![Snipaste_2021-02-22_09-20-55.webp](https://cdn.nlark.com/yuque/0/2021/webp/2213540/1613956869852-ffc63ac0-d57d-4c2f-b410-d54bcf06a829.webp#align=left&display=inline&height=244&originHeight=244&originWidth=599&size=18492&status=done&style=none&width=599)

解决思路：<br />...

