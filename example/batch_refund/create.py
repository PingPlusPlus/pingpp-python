# -*- coding: utf-8 -*-

'''
Batch Refunds 批量退款接口使用参考
注意:
    1, 批量退款接口，目前只支持全额退款（已经有部分退款的，会把剩余的金额全部退完）；
    2, 目前支持三个渠道的订单 alipay, alipay_wap, alipay_pc_direct；

具体使用请参考 (https://www.pingxx.com/api#创建-batch-refund-对象)
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

batch_no = 'batchrefund' + str(random.randint(1, 10000))

req_params = {
    "app": app_id,
    "batch_no": "batchrefund20160801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_L8qn10mLmr1GS8e5OODmHaL4",
        "ch_fdOmHaLmLmr1GOD4qn1dS8e5"
    ]
}

try:
    # 创建 Batch refund 对象
    br = pingpp.BatchRefund.create(**req_params)
    print ">> batch transfer instance ", br
except Exception as e:
    print e.http_body
