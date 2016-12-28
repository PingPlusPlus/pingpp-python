# -*- coding: utf-8 -*-

'''
批量退款接口使用参考
注意:
    1, 批量退款接口，目前只支持全额退款（已经有部分退款的，会把剩余的金额全部退完）；
    2, 目前支持三个渠道的订单 alipay, alipay_wap, alipay_pc_direct；

具体使用请参考 (https://www.pingxx.com/docs/server)
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
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

batch_no = 'batchrefund' + str(random.randint(1, 10000))
# 创建
req_params = {
    "app": app_id,
    "batch_no": "batchrefund20160801001",
    "description": "Batch refund description.",
    "charges": [
        "ch_K88Sa58OKqbPLG0ufLyH04W1",
        "ch_Civ1O8880Wf1KmbPCCGujf5S"
    ]
}

try:
    # 创建 Batch refund 对象
    br = pingpp.BatchRefund.create(**req_params)
    print ">> batch transfer instance ", br

    # 查询指定批量退款 id 信息
    br_single = pingpp.BatchRefund.retrieve("151608161453545102")
    print ">> batch refund single ", br_single

    # 查询批量退款列表
    br_list = pingpp.BatchRefund.list()
    print ">> batch refunds list ", br_list
except Exception as e:
    print e.http_body
