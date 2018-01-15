# -*- coding: utf-8 -*-

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
Transfers 企业付款查询示例
'''

try:
    # 查询指定转账 id 信息
    transfer = pingpp.Transfer.retrieve('tr_W5Oq14e1SWnTDCWfjPXnTW1O')
    print(transfer)
except Exception as e:
    raise
