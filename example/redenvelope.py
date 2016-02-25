#!/usr/bin/env python
import pingpp
import random
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = 'your_rsa_private_key.pem'

orderno = random.randint(10000000, 99999999999)

redenvelope = pingpp.RedEnvelope.create(
    order_no=orderno,
    channel='wx_pub',
    amount=100,
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='app_1Gqj58ynP0mHeX1q'),
    extra=dict(nick_name='Nick Name',send_name='Send Name'),
    recipient='Openid',
    description='Your Description'
)
print redenvelope


red= pingpp.RedEnvelope.all()
print red

