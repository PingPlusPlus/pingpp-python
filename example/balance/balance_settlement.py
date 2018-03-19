# -*- coding: utf-8 -*-

import pingpp
import os

pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

# balance_settlement 接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
余额结算查询 Demo
'''

try:
    # 获取余额结算明细
    obj = pingpp.BalanceSettlement.retrieve("670180226606668883880001")
    print(obj)

    # 获取余额结算列表
    objs = pingpp.BalanceSettlement.list(page=1, per_page=10)
    print(objs)
except Exception as e:
    print(e)
