# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
批量转账-查询批量转账
'''

try:
    # 查询指定批量批量转账 id 信息
    batch_transfer = pingpp.BatchTransfer.retrieve('1801801151458487285')
    print('>> batch transfer retrieve %s', batch_transfer.to_str())
except Exception as e:
    raise
