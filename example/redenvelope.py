# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入红包流程参考开发者中心：https://www.pingxx.com/docs/server/red-envelope ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import random
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->开发信息->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存->先启用 Test 模式进行测试->测试通过后启用 Live 模式
'''

# 设置私钥内容方式1：通过路径读取签名私钥
pingpp.private_key_path = os.path.join(os.path.dirname(__file__),
                                       'your_rsa_private_key.pem')

orderno = random.randint(10000000, 99999999999)  # 红包使用的商户订单号。wx(新渠道)、wx_pub 规定为 1 ~ 28 位不能重复的数字

redenvelope = pingpp.RedEnvelope.create(
    order_no=orderno,
    channel='wx_pub',  # 目前支持 wx(新渠道)、 wx_pub
    amount=100,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100，金额限制在 100 ~ 20000 之间，即 1 ~ 200 元）
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='app_1Gqj58ynP0mHeX1q'),  # app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
    extra=dict(send_name='Send Name'),  # 商户名称，最多 32 个字节
    recipient='Openid',  # 接收者 id， 为用户在 wx(新渠道)、wx_pub 下的 open_id
    description='Your Description'
)
print(redenvelope)  # 输出 Ping++ 返回的红包对象 Red_envelope


reds = pingpp.RedEnvelope.all()
print(reds)
