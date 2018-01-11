# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  使用报关接口参考文档：https://www.pingxx.com/api#api-customs
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import random
import string
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
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
    批量提现确认
'''

params = {
    "withdrawals": [
        "1701708281440143131",
        "1701708281440122654"
    ]
}
try:
    # 创建批量提现确认
    batch_withdrawal = pingpp.BatchWithdrawal.create(app=app_id, **params)
    print(batch_withdrawal)  # // 输出 Ping++ 返回的批量提现 withdrawals

    # 获取 批量提现确认
    retreive_batch_withdrawal = pingpp.BatchWithdrawal.retrieve("1901707171732385074", app=app_id)
    print retreive_batch_withdrawal

    # 获取 批量提现列表
    list_param = {
        'page': 1,
        'per_page': 10
    }
    batch_withdrawal_list = pingpp.BatchWithdrawal.list(app=app_id, **list_param)
    print batch_withdrawal_list.to_str()
except Exception as e:
    print(e.http_body)
