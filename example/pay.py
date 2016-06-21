# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入支付流程参考开发者中心：https://www.pingxx.com/docs/server/charge ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import random
import string
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->开发信息->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存->先启用 Test 模式进行测试->测试通过后启用 Live 模式
'''
# 设置私钥内容方式1：通过路径读取签名私钥
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 设置私钥内容方式2：直接设置请求签名私钥内容
# pingpp.private_key = '''-----BEGIN RSA PRIVATE KEY-----
# 私钥内容字符串
# -----END RSA PRIVATE KEY-----'''

# 订单号推荐使用 8-20 位，要求数字或字母，不允许其他字符
orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
try:
    ch = pingpp.Charge.create(
        subject='Your Subject',
        body='Your Body',
        amount=100,# 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        order_no=orderno,
        currency='cny',
        channel='alipay',# 支付使用的第三方支付渠道取值，请参考：https://www.pingxx.com/api#api-c-new
        client_ip='192.168.0.9',# 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        app=dict(id=app_id)
    )
    print(ch.to_str()) # 输出 Ping++ 返回的支付凭据 Charge
except Exception as e:
    print(e.message)
