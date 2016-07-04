#!/usr/bin/env python

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入企业付款流程参考开发者中心：https://www.pingxx.com/docs/server/transfer ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import random
import string

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->开发信息->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存->先启用 Test 模式进行测试->测试通过后启用 Live 模式
'''
pingpp.private_key_path = 'your_rsa_private_key.pem'


# 企业转账使用的商户内部订单号。wx(新渠道)、wx_pub 规定为 1 ~ 50 位不能重复的数字字母组合
orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
'''
extra 字段说明:
    user_name: 收款人姓名。当该参数为空，则不校验收款人姓名，选填;
    force_check: 是否强制校验收款人姓名。仅当 user_name 参数不为空时该参数生效，选填
'''
tr = pingpp.Transfer.create(
    order_no=orderno,
    channel='wx_pub',  # 目前支持 wx(新渠道)、 wx_pub
    amount=100,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100,企业付款最小发送金额为 1 元）
    currency='cny',
    app=dict(id='app_1Gqj58ynP0mHeX1q'),  # app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
    type='b2c',  # 付款类型，当前仅支持 b2c 企业付款
    recipient='youropenid',  # 接收者 id， 为用户在 wx(新渠道)、wx_pub 下的 open_id
    extra=dict(user_name='User Name', force_check=True),
    description='description'
)
print(tr)  # // 输出 Ping++ 返回的企业付款对象 Transfer
