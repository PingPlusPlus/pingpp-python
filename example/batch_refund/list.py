# -*- coding: utf-8 -*-

import pingpp
import os

app_id = "app_1Gqj58ynP0mHeX1q"
# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

try:
    # 查询批量退款列表
    objs = pingpp.BatchRefund.list(per_page=3, app=app_id)
    print(">> batch refunds list ", objs)
except Exception as e:
    raise
