#!/usr/bin/env python
import pingpp
import random
import string

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = 'your_rsa_private_key.pem'

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
ch = pingpp.Charge.create(
    subject='Your Subject',
    body='Your Body',
    amount=1,
    order_no=orderno,
    currency='cny',
    channel='alipay',
    client_ip='127.0.0.1',
    app=dict(id='app_1Gqj58ynP0mHeX1q')
)
print ch
