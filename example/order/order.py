# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入退款流程参考开发者中心：https://www.pingxx.com/docs/server ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os
import time
import random

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')
'''
    订单接口
'''

order_info = {
    "app": app_id,
    "uid": "user_test_01",  # 可选参数
    "merchant_order_no": str(int(random.uniform(100000000, 200000000))),
    "coupon": "300116082415452100000700",
    "amount": 30,
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

# 使用 Order 接口生成的订单中如果存在 charge id，不能通过charge id 来进行查询、退款操作，必须通过 Order ID 来操作

try:
    # 创建 order对象
    order = pingpp.Order.create(**order_info)  # Charge 对象的 id
    print order

    # Order 支付接口
    pay_params = {
        "charge_amount": 30,
        "channel": 'balance'
    }
    order_pay = pingpp.Order.pay(order.id, **pay_params)
    print order_pay

    # 取消 order对象
    cancel_param = {
        "user": "10000000002"  # 选填 用户 ID，传入该参数时，会检查该参数值与创建订单的用户 ID 是否一致。
    }
    cancel_result = pingpp.Order.cancel(order.id, **cancel_param)
    print cancel_result

    # 查询 order对象
    retrieve_order = pingpp.Order.retrieve("2001708150000313781")
    print retrieve_order

    # 查询order 对象列表
    order_list = pingpp.Order.list(app=app_id)
    print order_list

    # 创建商品订单退款
    params = {
        "description": "Your description",
        "refund_mode": "to_source",
        "royalty_users": [
            {
                "user": "test_user_002",
                "amount_refunded": 1,
            },
            {
                "user": "test_user_003",
                "amount_refunded": 1,
            }
        ]
    }
    order_refund = pingpp.OrderRefunds.create(order_id="2001708150000313781", **params)
    print order_refund

    # 获取 order refunds list
    order_refunds_list = pingpp.OrderRefunds.list(order_id="2001708150000313781")
    print order_refunds_list

    # 获取 order refunds
    order_refunds_detail = pingpp.OrderRefunds.retrieve(
        order_id="2001708150000313781",
        refund_id="re_HK0aXLnfjTy9u1aj14PCyzLG"
    )
    print order_refunds_detail
    # 查询order charge列表
    print("get order charge list", pingpp.Order.charge_list("2001708150000313781"))
    # 查询order charge对象
    print("retrieve order charge", pingpp.Order.charge_retrieve("2001708150000313781", "ch_SS0GqLWrrD00Ga1e1GW9WXjP"))

except Exception as e:
    print e.http_body
