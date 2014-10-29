#!/usr/bin/env python

import pingpp

pingpp.api_key = 'API-KEY'

ch = pingpp.Charge.retrieve("CH-ID")
re = ch.refunds.create(description='desc', amount=1)
