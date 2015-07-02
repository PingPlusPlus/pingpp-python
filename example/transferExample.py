
#!/usr/bin/env python
import pingpp

pingpp.api_key = 'YOUR-KEY'
a = True
tr = pingpp.Transfer.create(
    order_no='1234567890',
    channel='wx_pub',
    amount=100,
    currency='cny',
    app=dict(id='YOUR-APP-ID'),
    type='b2c',
    recipient='youropenid',
    extra=dict(user_name='User Name', force_check=True),
    description='description'
)
print tr