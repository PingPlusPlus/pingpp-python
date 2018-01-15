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
        channel='alipay',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 可选，开放平台返回的包含账户信息的 token（授权令牌，商户在一定时间内对支付宝某些服务的访问权限）。
            #     通过授权登录后获取的 alipay_open_id，作为该参数的 value，
            #     登录授权账户即会为支付账户，32 位字符串。
            # extern_token=''
            # 可选，是否发起实名校验，T 代表发起实名校验；F 代表不发起实名校验。
            # rn_check='T'
        )
    )
    print(charge)
except Exception as e:
    raise
