#!/usr/bin/env python
import pingpp

pingpp.api_key = 'API-KEY'

ch = pingpp.Charge.create(
    order_no='1234567890',
    channel='alipay',
    amount=1,
    subject='test-subject',
    body='test-body',
    currency='cny',
    app=dict(id='APP-ID'),
    client_ip='CLIENT-ID'
)

print ch
