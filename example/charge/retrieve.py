# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
API 文档：https://www.pingxx.com/api#charges-支付
查询 Charge 对象
'''

print("获取 Charge 对象:")
try:
    charge = pingpp.Charge.retrieve('ch_Civ1O8880Wf1KmbPCCGujf5S')
    print(charge.to_str())
except Exception as e:
    raise
