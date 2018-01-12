# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

'''
分润接口示例
'''
try:
    params = {
        "ids": [
            "170301124238000111",
            "170301124238000211"
        ],
        "method": "manual",
        "description": "Your description"
    }
    # 批量更新分润对象
    royalties = pingpp.Royalty.update(**params)
    print(royalties)
    # 查询分润对象列表
    params = {
        'page': 1,
        'per_page': 3
    }
    royalties = pingpp.Royalty.list(**params)
    print royalties
    # 查询分润对象
    royalty = pingpp.Royalty.retrieve('410170320160900002')
    print(royalty)
except Exception as e:
    print(e)
