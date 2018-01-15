# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

try:
    # 查询指定批量退款 id 信息
    batch_refund = pingpp.BatchRefund.retrieve("1501712011126518350")
    print(">> batch refund retrieve ", batch_refund)
except Exception as e:
    raise
