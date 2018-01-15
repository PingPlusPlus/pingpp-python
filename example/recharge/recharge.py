# -*- coding: utf-8 -*-

import pingpp
import os
import random
import time
import string

# 用户充值接口示例

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
time_expire 订单失效时间，用 Unix 时间戳表示。时间范围在订单创建后的 5 分钟到 1 天，
默认为 1 天，创建时间以 Ping++ 服务器时间为准。 微信对该参数的有效值限制为 2 小时内；
银联对该参数的有效值限制为 1 小时内。
metadata，extra 参照 charge 中的参数
'''

# 创建 recharge
try:
    params = {
        "user": "user_001",
        "charge": {
            "amount": 10000,
            "channel": "alipay",
            "order_no": str_random(20),
            "subject": "Your subject",
            "body": "Your body",
            "time_expire": int(time.time()) + 3600,
            "client_ip": "127.0.0.1",
            "extra": {}
        },
        # "user_fee": 0,
        # "balance_bonus": {
        #     "amount": 100,
        # },
        # "from_user": "user_002",
        "description": "Your description",
        "metadata": {}
    }

    recharge = pingpp.Recharge.create(**params)
    print(">> create recharge ", recharge)

    print(">> retrieve recharge", pingpp.Recharge.retrieve(recharge.id))
    params = {
        "page": 1,
        "per_page": 3,
    }
    print(">> list recharges", pingpp.Recharge.list(**params))
except Exception as e:
    print(e)

try:
    params = {
        "description": "Your description",
        "metadata": {}
    }
    refund = pingpp.Recharge.refund(recharge.id, **params)
    print(">> create recharge refund", refund)

    refund = pingpp.Recharge.retrieve_refund(recharge.id,
                                             refund.id)
    print(">> retrieve recharge refund", refund)

    print(">> retrieve recharge refund", pingpp.Recharge.list_refunds(
        recharge.id, per_page=3))
except Exception as e:
    print(e)
