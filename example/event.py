# -*- coding: utf-8 -*-

import pingpp
import os

pingpp.log = "debug"

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

'''
Events 事件
'''

# 查询 Event 对象
try:
    event = pingpp.Event.retrieve('evt_401180116154930078262236')
    print(event)
except Exception as e:
    raise
