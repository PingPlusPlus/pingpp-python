# -*- coding: utf-8 -*-

import pingpp
import random
import string
import os

# API Key & APP ID
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key
# 设置请求签名私钥路径
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
# 或者设置请求签名私钥内容
# pingpp.private_key = '''-----BEGIN RSA PRIVATE KEY-----
# 私钥内容字符串
# -----END RSA PRIVATE KEY-----'''

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
try:
    ch = pingpp.Charge.create(
        subject='Your Subject',
        body='Your Body',
        amount=100,
        order_no=orderno,
        currency='cny',
        channel='alipay',
        client_ip='192.168.0.9',
        app=dict(id=app_id)
    )
    print(ch.to_str())
except Exception as e:
    print(e.message)
