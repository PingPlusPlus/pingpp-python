# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = "app_1Gqj58ynP0mHeX1q"

# 设置 API Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

# 查询 Transfer 对象列表
try:
    transfers = pingpp.Transfer.list(app={"id": app_id}, limit=3)
    print(transfers)
except Exception as e:
    raise
