# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# withdrawal 接口支持全局配置 app_id
pingpp.app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
余额提现 Demo
'''

params = {
    "user": "user_001",
    "amount": 100,
    "user_fee": 0,
    'order_no': str_random(16),
    "description": "Your description",
    # channel 值必须是 银联：unionpay，支付宝：alipay，微信：wx_pub，通联：allinpay，京东：jdpay其中一种
    'channel': 'unionpay',
    "extra": {
        "account": "6226234567890006",  # 提现订单号，为长度不大于 16 的数字
        "name": "姓名",
        "open_bank_code": "0102",
    },
    # 使用结算账户提现，不需要填写 extra 相关参数，同时填写时，结算账号不生效
    # "settle_account": "320217022818035400000601",
}

try:
    # 余额提现申请创建
    withdrawal = pingpp.Withdrawal.create(**params)
    print(withdrawal)

    # 余额提现列表
    withdrawals = pingpp.Withdrawal.list(user="user_001", per_page=3)
    print(withdrawals)

    # 获取余额提现申请信息
    withdrawal = pingpp.Withdrawal.retrieve(withdrawal.id)
    print(withdrawal)

    # 余额提现取消
    withdrawal = pingpp.Withdrawal.cancel(withdrawal.id)
    print(withdrawal)

    # 余额提现确认
    withdrawal = pingpp.Withdrawal.confirm(withdrawal.id)
    print(withdrawal)
except Exception as e:
    raise
