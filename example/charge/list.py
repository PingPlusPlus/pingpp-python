# -*- coding: utf-8 -*-

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
查询 charge 对象列表：https://www.pingxx.com/api#charges-支付
'''

print("获取 Charge 对象列表:")
try:
    params = {
        'app[id]': app_id,  # 必传
        'limit': 3,
        'paid': True,
        'refunded': False,
    }
    charges = pingpp.Charge.list(**params)
    print(charges)
except Exception as e:
    raise
