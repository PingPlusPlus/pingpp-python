#!/usr/bin/env python
import pingpp

pingpp.api_key = 'YOUR-KEY'

redenvelope = pingpp.RedEnvelope.create(
    order_no='123456789',
    channel='wx_pub',
    amount=100,
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='YOUR-APP-ID'),
    extra=dict(nick_name='Nick Name',send_name='Send Name'),
    recipient='Openid',
    description='Your Description'
)
print redenvelope


red= pingpp.RedEnvelope.all()
print red

