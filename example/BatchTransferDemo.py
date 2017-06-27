# -*- coding: utf-8 -*-

'''
批量付款接口使用参考
具体使用请参考 (https://www.pingxx.com/docs/server)
'''

import pingpp
import random
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
'''
    批量转账
'''

batch_no = 'batchtrans' + str(random.randint(1, 10000))
# 创建
req_params = {
    'recipients': [
        {
            "account": "account01@alipay.com",
            "amount": 5000,
            "name": "张三"
        },
        {
            "account": "account02@alipay.com",
            "amount": 3000,
            "name": "李四"
        }
    ],
    'type': 'b2c',
    'channel': 'alipay',
    'amount': 8000,
    "app": app_id,
    "batch_no": "batchtrans20160801001",
    "description": "Batch trans description."
}

try:
    # 创建批量批量转账
    bt = pingpp.BatchTransfer.create(**req_params)
    print ">> batch transfer instance ", bt

    # 查询指定批量批量转账 id 信息
    bt_single = pingpp.BatchTransfer.retrieve('1801612281141104543')
    print ">> batch transfer single ", bt_single

    # 查询批量批量转账列表
    bt_list = pingpp.BatchTransfer.list()
    print ">> batch transfer list ", bt_list

    # 更新批量付款对象 (仅unionpay渠道支持)
    bt_update = pingpp.BatchTransfer.cancel('1801612281141104543')
except Exception as e:
    print(e.http_body)
