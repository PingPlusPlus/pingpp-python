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
        channel='yeepay_wap',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 必须，商品类别码，商品类别码参考链接 ：https://www.pingxx.com/api#易宝支付商品类型码。
            product_category='1',
            # 必须，用户标识,商户生成的用户账号唯一标识，最长 50 位字符串。
            identity_id='88888888',
            # 必须，用户标识类型，用户标识类型参考链接: https://www.pingxx.com/api#易宝支付用户标识类型码
            identity_type=1,
            # 必须，终端类型，对应取值 0:IMEI, 1:MAC, 2:UUID, 3:other。
            terminal_type=1,
            # 必须，终端 ID。
            terminal_id=666666,
            # 必须，用户使用的移动终端的 UserAgent 信息。
            user_ua='Chrome/58.0.3029.81',
            # 必须，前台通知地址。
            result_url='http://example.com/success'
        )
    )
    print(charge)
except Exception as e:
    raise
