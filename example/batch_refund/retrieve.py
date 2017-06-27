# -*- coding: utf-8 -*-

'''
Batch Refunds 批量退款接口-查询批量退款接口 使用参考

具体使用请参考 (https://www.pingxx.com/api#查询-batch-refund-对象)
'''

import pingpp
import random
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

try:
    # 查询指定批量退款 id 信息
    br_single = pingpp.BatchRefund.retrieve("1501703152006460585")
    print ">> batch refund single ", br_single
except Exception as e:
    print e.http_body
