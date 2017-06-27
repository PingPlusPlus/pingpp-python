# -*- coding: utf-8 -*-

'''
Batch Transfers 批量企业付款接口使用参考 具体使用请参考 (https://www.pingxx.com/api#查询-batch-transfer-对象列表)
'''

import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')
'''
    批量转账-对象列表
'''
try:
    # 查询批量批量转账列表
    bt_list = pingpp.BatchTransfer.list()
    print('>> batch transfer list:%s ' % bt_list)
except Exception as e:
    print(e.http_body)
