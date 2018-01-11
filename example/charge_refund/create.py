# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
创建 Refund 对象 Demo: https://www.pingxx.com/api#创建-refund-对象
'''

print("创建Refund对象:")
try:
    # 通过发起一次退款请求创建一个新的 refund 对象，
    # 只能对已经发生交易并且没有全额退款的 charge 对象发起退款
    # amount 为退款的金额, 单位为对应币种的最小货币单位，
    # 例如：人民币为分（如退款金额为 1 元，此处请填 100）。
    # 必须小于等于可退款金额，默认为全额退款
    re = pingpp.Charge.refund('ch_Ti1eD0WP08eDPSSqnTOmLWHK',
                              description='Your Descripton',
                              amount=1)
    print(re)  # 输出 Ping++ 返回的退款对象 Refund
except Exception as e:
    print(e)
