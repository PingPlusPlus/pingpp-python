# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
线下渠道charge撤销接口
此接口仅接受线下 isv_scan、isv_wap、isv_qr 渠道的订单调用
本接口有两重作用，对于未成功付款的订单进行撤销，则关闭交易，使用户后期不能支付成功；
对于成功付款的订单进行撤销，系统将订单金额返还给用户，相当于对此交易做退款。
'''

print("撤销 Charge 对象:")
try:
    charge = pingpp.Charge.reverse('ch_vrf1OGefXnXTCGKWjT5evHuT')
    print(charge)
except Exception as e:
    raise
