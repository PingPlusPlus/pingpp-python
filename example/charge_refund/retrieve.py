# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
查询 Refund 对象 Demo: https://www.pingxx.com/api#查询-refund-对象
'''

print("查询 Refund 对象:")
try:
    refund = pingpp.Charge.retrieve_refund('ch_Ti1eD0WP08eDPSSqnTOmLWHK',
                                           're_irb1COq1ezTCXP0WfPervbHK')
    print(refund)
except Exception as e:
    raise
