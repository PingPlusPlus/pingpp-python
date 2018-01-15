# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# batch_withdrawal 接口支持全局配置 app_id
pingpp.app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
批量提现确认
'''

params = {
    "withdrawals": [
        "1701801151516122316",
        "1701801151516092099"
    ]
}

try:
    # 创建批量提现确认
    batch_withdrawal = pingpp.BatchWithdrawal.create(**params)
    print(batch_withdrawal)  # 输出 Ping++ 返回的批量提现

    # 获取批量提现
    batch_withdrawal = pingpp.BatchWithdrawal.retrieve(batch_withdrawal.id)
    print(batch_withdrawal)

    # 获取批量提现列表
    params = {
        'page': 1,
        'per_page': 3
    }
    batch_withdrawals = pingpp.BatchWithdrawal.list(**params)
    print(batch_withdrawals.to_str())
except Exception as e:
    raise
