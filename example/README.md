# 示例说明

## 说明
所有的示例代码只是为了方便商户测试而提供的样例，请商户根据自己的需求按照接入文档及接口文档编写。

示例代码仅供学习和研究 Ping++ SDK 使用，仅供参考。

不要直接复制粘贴使用示例代码，请根据实际情况在相应的方法传入需要的参数。

## 文档
- [API 文档](https://www.pingxx.com/api)
- [服务端接入指南](https://www.pingxx.com/docs/server)
- [SDK 说明](/README.md)

## api_key 获取方式
1. 登录 [Dashboard](https://dashboard.pingxx.com)；
2. 点击管理平台右上角公司名称；
3. 点击企业面板；
4. 点击开发参数；
5. Test Secret Key/Live Secret Key，其中 Live Secret Key 需要经过验证才能查看。

## app_id 获取方式
1. 登录 [Dashboard](https://dashboard.pingxx.com)；
2. 在主页的相应 App 卡片上可以看到 `App ID`。

## 设置签名
设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，  
如何生成可以参考帮助中心：https://help.pingxx.com/article/123161。

生成密钥后，需要在代码中设置请求签名的私钥 `rsa_private_key.pem`。

然后按照下述步骤配置公钥。

1. 登录 [Dashboard](https://dashboard.pingxx.com)；
2. 点击管理平台右上角公司名称；
3. 点击企业面板；
4. 点击开发参数；
5. 在 `商户 RSA 公钥` 部分点击配置，再根据提示填入公钥并启用。

> 部分接口是强制开启验签功能的，不受开启关闭的控制，需要配置公钥才能使用。

## 对象里的中文编码输出
直接将对象作为 str 输出的情况下，中文会转换成 unicode 码，  
如果需要保持**中文**的形式输出，请使用 `.to_str()` 方法转成 str 再输出。

例：
```python
charge = pingpp.Charge.retrieve('ch_Tuv1y10OG0y5nD4mf90mTqnD')
print(charge.to_str())
```
