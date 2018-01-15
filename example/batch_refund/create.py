# -*- coding: utf-8 -*-

import pingpp
import random
import os
import string


app_id = "app_1Gqj58ynP0mHeX1q"
# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


batch_no = str_random(20)

params = {
    "app": app_id,
    "batch_no": batch_no,
    "description": "Batch refund description.",
    "charges": [
        "ch_GebHC888m5mPSmPCG48K4Gq9",
        "ch_LizXT0CabDSKOG8CuDKOm1eT",
        "ch_b50e1O0K8a1GWzrX1GqHKSK0"
    ]
}

try:
    # 创建 Batch refund 对象
    br = pingpp.BatchRefund.create(**params)
    print(">> batch transfer instance", br)
except Exception as e:
    raise
