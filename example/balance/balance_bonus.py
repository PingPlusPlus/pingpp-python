# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 支持全局配置
pingpp.app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

"""
用户余额赠送 Demo
"""

try:
    params = {
        "amount": 100,  # 支付受赠余额，单位：分
        "user": "user_test_01",  # 受赠的用户 ID
        "order_no": '12345678',  # 商户订单号，必须在商户系统内唯一
        "description": "Your description",  # 描述
        "metadata": {}  # metadata 元数据
    }
    balance_bonus = pingpp.BalanceBonus.create(**params)
    print(balance_bonus)

    balance_bonus = pingpp.BalanceBonus.retrieve("650180111631193620480001")
    print(balance_bonus)

    params = {"per_page": 3}
    balance_bonuses = pingpp.BalanceBonus.list(**params)
    print(balance_bonuses)
except Exception as e:
    print(e)
