# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
app_id = "app_1Gqj58ynP0mHeX1q"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
批量转账-对象列表
'''
try:
    # 查询批量批量转账列表
    batch_transfers = pingpp.BatchTransfer.list(per_page=3, app=app_id)
    print('>> batch transfer list', batch_transfers.to_str())
except Exception as e:
    raise
