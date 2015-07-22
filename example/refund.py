 #!/usr/bin/env python

import pingpp

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

ch = pingpp.Charge.retrieve('CH-ID')
re = ch.refunds.create(description='desc', amount=1)
