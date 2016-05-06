# -*- coding: utf-8 -*-

import pingpp
import random
import string
import os

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
ch = pingpp.Charge.create(
    subject='Your 订单',
    body='Your 内容',
    amount=100,
    order_no=orderno,
    currency='cny',
    channel='alipay',
    client_ip='192.168.0.9',
    app=dict(id='app_1Gqj58ynP0mHeX1q')
)
print(ch.to_str())
