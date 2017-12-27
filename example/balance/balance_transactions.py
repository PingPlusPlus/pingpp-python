# -*- coding: utf-8 -*-

import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')
'''
    用户账户交易明细 Demo
'''
try:
    # 获取账户交易明细信息
    retr_bt = pingpp.BalanceTransaction.retrieve(app=app_id, id="600170825551333980160001")
    print(retr_bt)

    # 获取账户交易明细列表
    bt_list = pingpp.BalanceTransaction.list(app=app_id)
    print(bt_list)
except Exception as e:
    print(e.http_body)
