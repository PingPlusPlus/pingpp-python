# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

try:
    # 查询分润结算明细对象列表
    params = {
        "page": 1,
        "per_page": 3
    }
    royalty_transaction_list = pingpp.RoyaltyTransaction.list(**params)
    print(royalty_transaction_list)

    # 查询单个分润结算明细对象
    royalty_transaction = pingpp.RoyaltyTransaction.retrieve(
        '440170908211000001')
    print(royalty_transaction)
except Exception as e:
    raise
