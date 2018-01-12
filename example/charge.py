# -*- coding: utf-8 -*-

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

"""
Charges 支付 Demo:https://www.pingxx.com/api#charges-支付
创建 charge 对象，查询 charge 对象，查询 charge 对象列表
"""

print("创建charge对象:")
try:
    charge = pingpp.Charge.create(
        order_no='20181234567890',
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
    print(e)

print("获取Charge对象:")
try:
    charge = pingpp.Charge.retrieve('ch_Tuv1y10OG0y5nD4mf90mTqnD')
    print(charge.to_str())
except Exception as e:
    print(e)

print("获取Charge对象列表:")
try:
    params = {
        'app[id]': app_id,
        'limit': 3,
    }
    charges = pingpp.Charge.list(**params)
    print(charges)
except Exception as e:
    print(e)
