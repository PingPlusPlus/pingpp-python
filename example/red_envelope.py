# -*- coding: utf-8 -*-

import pingpp
import random
import string
import os

pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = "app_1Gqj58ynP0mHeX1q"
# 设置私钥内容方式1：通过路径读取签名私钥
pingpp.private_key_path = os.path.join(os.path.dirname(__file__),
                                       'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.digits
    return "".join(random.choice(allchar) for _ in range(length))


print("创建 Red Envelope 对象:")

try:
    red_envelope = pingpp.RedEnvelope.create(
        order_no=str_random(16),
        channel='wx_pub',  # 目前支持 wx、 wx_pub
        # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100，金额限制在 100 ~ 20000 之间，即 1 ~ 200 元）
        amount=100,
        subject='Your Subject',
        body='Your Body',
        currency='cny',
        app=dict(id=app_id),
        extra=dict(send_name='Send Name'),  # 商户名称，最多 32 个字节
        recipient='Openid',  # 接收者 id， 为用户在 wx(新渠道)、wx_pub 下的 open_id
        description='Your Description'
    )
    print(red_envelope)  # 输出 Ping++ 返回的红包对象 Red_envelope
except Exception as e:
    print(e)

print("获取 Red envelope 对象列表:")
try:
    red_envelopes = pingpp.RedEnvelope.list(app={"id": app_id}, limit=3)
    print(red_envelopes)
except Exception as e:
    print(e)

print("获取 Red envelope 对象:")
try:
    red_envelope = pingpp.RedEnvelope.retrieve('red_mDmLS89C4u9KCKSyzHGCOO0C')
    print(red_envelope)
except Exception as e:
    print(e)
