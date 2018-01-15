# -*- coding: utf-8 -*-

'''
报关接口参考文档：https://www.pingxx.com/api#api-customs
'''

import pingpp
import random
import string
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 商户报关订单号，8~20位
trade_no = ''.join(random.sample(string.ascii_letters + string.digits, 8))

# 请求报关接口
try:
    customs = pingpp.Customs.create(
        app=app_id,
        charge='ch_i2PKhP1qDWNPK9CoqTKQsqb5',
        channel='alipay',
        amount=100,  # 报关金额, 人民币单位：分
        customs_code='GUANGZHOU',
        trade_no=trade_no
    )
    print(customs)  # // 输出 Ping++ 返回的报关对象 Transfer
except Exception as e:
    print(e)

# 查询报关接口
try:
    customs = pingpp.Customs.retrieve("14201607013878045463")
    print(customs)
except Exception as e:
    print(e)
