#!/usr/bin/env python
import pingpp

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = 'your_rsa_private_key.pem'

try:
    tr = pingpp.Transfer.create(
        amount=100,
        order_no='12345678',
        currency='cny',
        channel='wx_pub',
        app=dict(id='app_1Gqj58ynP0mHeX1q'),
        type='b2c',
        recipient='o9zpMs9jIaLynQY9N6yxcZ',
        description='testing',
        extra=dict(user_name='User Name', force_check=False)
    )
    print tr
except pingpp.InvalidRequestError as ire:
    print ire.http_body
except pingpp.AuthenticationError as ae:
    print ae.http_body
