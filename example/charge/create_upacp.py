# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
Charge 支付 API 文档：https://www.pingxx.com/api#charges-支付
创建 charge 对象
'''

print("创建 charge 对象:")
try:
    charge = pingpp.Charge.create(
        order_no=str_random(20),  # 推荐使用 8-20 位，要求数字或字母，不允许其他字符
        amount=10000,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        app=dict(id=app_id),
        channel='upacp',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
    )
    print(charge)
except Exception as e:
    raise
