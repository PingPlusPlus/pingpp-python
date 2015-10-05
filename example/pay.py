#!/usr/bin/env python
import pingpp
import random
import string

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
ch = pingpp.Charge.create(
    order_no = orderno,
    channel='alipay',
    amount=1,
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='app_1Gqj58ynP0mHeX1q'),
    client_ip='127.0.0.1'
)
print ch

