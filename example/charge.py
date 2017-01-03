# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  使用报关接口参考文档：https://www.pingxx.com/api#api-customs
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->企业设置->开发设置-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->企业设置->开发设置->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存。
  注：报关接口，必须配置该值，不管是否启用，都需要验证签名。
'''
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
'''
    Charges 支付Demo:https://www.pingxx.com/api#charges-支付
    创建charge对象,查询charge对象,查询charge对象列表
    创建Refund对象,查询Refund对象,查询Refund对象列表
'''
print "创建charge对象:"
try:
    charge = pingpp.Charge.create(
        order_no='1234567890',
        amount=1000000,
        app=dict(id=app_id),
        channel='alipay',
        currency='cny',
        client_ip='127.0.0.1',
        subject='Your Subject',
        body='Your Body',
    )
    print(charge)
except Exception as e:
    print(e.http_body)

print "获取Charge对象:"
try:
    charge_info = pingpp.Charge.retrieve('ch_Civ1O8880Wf1KmbPCCGujf5S')
    print charge_info
except Exception as e:
    print e.http_body

print "获取Charge对象列表:"
try:
    params = {
        'app': {
            'id': app_id
        }
    }
    params = {}
    charge_list = pingpp.Charge.all(**params)
    print charge_list
except Exception as e:
    print e.http_body

print "创建Refund对象:"
try:
    charge_info = pingpp.Charge.retrieve('ch_W5CCe9uPujnDLqvbvH9OOS8S')
    charge_refund_params = {
        'description': 'Your description',
        'amount': 10
    }
    charge_refund = charge_info.refund(**charge_refund_params)
    print charge_refund
except Exception as e:
    print e.http_body


print "查询Refund对象列表:"
try:
    charge_info = pingpp.Charge.retrieve('ch_W5CCe9uPujnDLqvbvH9OOS8S')
    charge_refund_list_params = {
        'limit': 1,
    }
    charge_refund_list = charge_info.refund_list(**charge_refund_list_params)
    print charge_refund_list
except Exception as e:
    print e.http_body

print "查询Refund对象:"
try:
    charge_info = pingpp.Charge.retrieve('ch_W5CCe9uPujnDLqvbvH9OOS8S')
    charege_refund_retrieve = charge_info.refund_retrieve('re_GKOuf1a9408OazbbPKS0CqX5')
    print charge_info
except Exception as e:
    print e.http_body
