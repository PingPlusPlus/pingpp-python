# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
查询 Refund 对象列表 Demo: https://www.pingxx.com/api#查询-refund-对象列表
'''

try:
    params = {
        'limit': 3,
    }
    refunds = pingpp.Charge.refund_list('ch_W5CCe9uPujnDLqvbvH9OOS8S',
                                        **params)
    print(refunds)
except Exception as e:
    raise
