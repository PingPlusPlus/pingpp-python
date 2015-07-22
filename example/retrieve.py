#!/usr/bin/env python

import pingpp

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

ch = pingpp.Charge.retrieve('ch_ejbLGCCaDWjT0ijzDSybL0mT')
eve = pingpp.Event.all()
