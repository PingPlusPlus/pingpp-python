#!/usr/bin/env python
import pingpp

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = 'your_rsa_private_key.pem'

try:
    red = pingpp.RedEnvelope.create(
        subject='Your Subject',
        body='Your Body',
        amount=100,
        order_no='12345676',
        currency='cny',
        extra=dict(nick_name='Nick Name', send_name='Send Name'),
        recipient='Openid',
        channel='wx_pub',
        app=dict(id='app_1Gqj58ynP0mHeX1q'),
        description='Your Description',
    )
    print red
except pingpp.InvalidRequestError as ire:
    print ire.http_body
except pingpp.AuthenticationError as ae:
    print ae.http_body
