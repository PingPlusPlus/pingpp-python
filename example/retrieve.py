#!/usr/bin/env python

import pingpp

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

ch = pingpp.Charge.retrieve('ch_a9CmfHTGGaz1urHiL8m5OiX1')
eve = pingpp.Event.all()
