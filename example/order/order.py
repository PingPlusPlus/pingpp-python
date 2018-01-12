# -*- coding: utf-8 -*-

import pingpp
import os
import time
import random

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
订单接口
'''

params = {
    "app": app_id,
    "uid": "user_001",  # 可选参数
    "merchant_order_no": str(int(random.uniform(100000000, 200000000))),
    # "coupon": "300116082415452100000700",
    "amount": 100,
    "client_ip": "127.0.0.1",
    "currency": "cny",
    "subject": "test1",
    "body": "test1body1",
    "description": "test1-description",
    "time_expire": int(time.time()) + 1000,
    "metadata": {},
    "receipt_app": app_id,  # 收款方应用
    "service_app": app_id,  # 服务方应用
    "royalty_users": [  # 分润的用户列表,默认为 []，不分润
        {
            "user": "test_user_002",
            "amount": 1
        },
        {
            "user": "test_uer_003",
            "amount": 1
        }
    ]
}

# 创建 order对象
order = pingpp.Order.create(**params)  # Charge 对象的 id
print("Create Order:", order)

# Order 支付接口
pay_params = {
    "charge_amount": 100,
    "channel": "wx",
    # "combined_with": {  # 组合支付相关参数
    #     "channel": "balance",
    #     "charge_amount": 40
    # }
}
order = pingpp.Order.pay(order.id, **pay_params)
print("Pay Order:", order)

# 取消 order对象
cancel_param = {
    "user": "user_001"  # 选填 用户 ID，传入该参数时，会检查该参数值与创建订单的用户 ID 是否一致。
}
order = pingpp.Order.cancel(order.id, **cancel_param)
print("Cancel Order:", order)

# 查询 order 对象
order = pingpp.Order.retrieve("2001801120000091311")
print("Retrieve Order:", order)

# 查询 order 对象列表
orders = pingpp.Order.list(app=app_id, per_page=3)
print("List Orders:", orders)

# 查询 order charge 列表
print("Get Order Charge List:",
      pingpp.Order.list_charges("2001801120000091311", per_page=3))

# 查询 order charge 对象
print("Retrieve Order Charge:",
      pingpp.Order.retrieve_charge("2001801120000091311",
                                   "ch_LSyzPGezX1iLuL8GaHqH4eDK"))
