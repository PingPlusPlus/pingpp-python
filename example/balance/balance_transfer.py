# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# balance_transfer 接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
    用户余额转账 Demo
'''

try:
    params = {
        "amount": 100,  # 必填,支付受赠余额，单位：分
        # 必填,发起转账的用户 ID（可以是 customer 或 business，不能为 0）
        "user": "user_001",
        # 必填,接收转账的用户 ID（可以是 customer 或 business，可以为 0）
        "recipient": "user_002",
        "order_no": str_random(20),  # 必填,商户订单号，必须在商户系统内唯一
        "description": "Your description",  # 选填,描述
        "metadata": {}  # 选填,metadata 元数据
    }
    balance_transfer = pingpp.BalanceTransfer.create(**params)
    print('create balance_bonus', balance_transfer)

    print("retrieve balance_bonus",
          pingpp.BalanceTransfer.retrieve(balance_transfer.id))

    print("list balance_bonuses", pingpp.BalanceTransfer.list(per_page=3))
except Exception as e:
    print(e)
