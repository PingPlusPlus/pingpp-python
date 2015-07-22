
#!/usr/bin/env python
import pingpp
import random
import string


pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
tr = pingpp.Transfer.create(
    order_no=orderno,
    channel='wx_pub',
    amount=100,
    currency='cny',
    app=dict(id='app_1Gqj58ynP0mHeX1q'),
    type='b2c',
    recipient='youropenid',
    extra=dict(user_name='User Name', force_check=True),
    description='description'
)
print tr