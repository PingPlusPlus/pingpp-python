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
        channel='cmb_wallet',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 必须，交易完成跳转的地址。
            result_url='http://example.com/success',
            # 对于 p_no, seq , m_uid , mobile 这几个参数：
            # 1. 这几个参数是用户自定义的。
            # 2. 对于同一个终端用户每次请求 charge 务必使用同一套参数（确保每个参数都不变），
            # 任意参数变更都会导致用户重新签约，同一个用户和招行重新签约的次数有限制，超限制就会无法签约 ，导致用户无法使用。
            # 必须，客户协议号，不超过 30 位的纯数字字符串。
            p_no='1234567890',
            # 必须，协议开通请求流水号，不超过 20 位的纯数字字符串，请保证系统内唯一。
            seq='1234567890234567888',
            # 必须，协议用户 ID，不超过 20 位的纯数字字符串。
            m_uid='8888888888',
            # 必须，协议手机号，11 位数字。
            mobile='13088888888'
        )
    )
    print(charge)
except Exception as e:
    raise
