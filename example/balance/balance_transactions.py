# -*- coding: utf-8 -*-

import pingpp
import os

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
    用户账户交易明细 Demo
'''

try:
    # 获取账户交易明细信息
    obj = pingpp.BalanceTransaction.retrieve("600180111625778739200001",
                                             app=app_id)
    print(obj)

    # 获取账户交易明细列表
    objs = pingpp.BalanceTransaction.list(app=app_id, **{"per_page": 3})
    print(objs)
except Exception as e:
    print(e)
