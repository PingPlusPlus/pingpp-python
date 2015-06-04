#!/usr/bin/env python

import pingpp

pingpp.api_key = 'APP-KEY'

# ch = pingpp.Charge.retrieve('CH-ID')
eve = pingpp.Event.all()
