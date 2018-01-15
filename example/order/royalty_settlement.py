# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
分润结算对象接口示例
'''

try:
    # 创建分润结算对象
    # params = {
    #     "payer_app": app_id,
    #     "method": "unionpay",
    #     "recipient_app": app_id,
    #     "created": {
    #         "gt": 1488211200,
    #         "lte": 1488297600
    #     },
    #     # 'is_preview': True  # 是否预览，选择预览不会真实创建分润结算对象，也不会修改分润对象的状态
    # }
    # royalty_settlement = pingpp.RoyaltySettlement.create(**params)
    # print(royalty_settlement)

    # 查询分润结算列表
    params = {
        "page": 1,
        "per_page": 3,
        "payer_app": app_id
    }
    royalty_settlement = pingpp.RoyaltySettlement.list(**params)
    print(royalty_settlement)

    # 查询分润结算对象
    royalty_settlement = pingpp.RoyaltySettlement.retrieve(
        '430170908211000001')
    print(royalty_settlement)

    # 更新分润结算对象-确认
    royalty_settlement = pingpp.RoyaltySettlement.confirm(
        '430170908211000001')
    print(royalty_settlement)

    # 更新分润结算对象-取消
    royalty_settlement = pingpp.RoyaltySettlement.cancel(
        '430170908211000001')
    print(royalty_settlement)
except Exception as e:
    raise
