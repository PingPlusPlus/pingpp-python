# -*- coding: utf-8 -*-

import pingpp
import random
import string
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
app_id = "app_1Gqj58ynP0mHeX1q"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


"""
批量转账-创建(jdpay)
"""

# 创建
req_params = {
    "recipients": [
        {
            # 必须，接收者银行卡账号。
            "account": "656565656565656565656565",
            # 必须，金额，单位为分。
            "amount": 5000,
            # 必须，接收者姓名。
            "name": "张三",
            # 必须，4位，开户银行编号。具体值参考此链接：https://www.pingxx.com/api#银行编号说明
            "open_bank_code": "0308",
            # 可选，批量付款描述，最多 100 个 Unicode 字符。
            # "description": "Your description",
            # 可选，订单号，jdpay 限长1-64位不能重复的数字字母组合。
            # "order_no": "12345678",
        },
        {
            "account": "656565656565656565656565",
            "amount": 3000,
            "name": "李四",
            "open_bank_code": "0308",
        }
    ],
    # 付款类型 (当前 alipay、wx_pub 仅支持: b2c, unionpay、allinpay、jdpay 支持:  b2b、b2c)
    "type": "b2c",
    # 渠道。支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay 余额：balance。
    "channel": "jdpay",
    "amount": 8000,  # 批量付款总金额，单位为分。为 recipients 中 amount 的总和。
    "app": app_id,
    "batch_no": str_random(20),  # 批量转账批次号，3-24位，允许字母和英文
    "description": "Batch transfer description."  # 批量转账详情，最多 255 个 Unicode 字符
}

try:
    # 创建批量批量转账
    batch_transfer = pingpp.BatchTransfer.create(**req_params)
    print(">> batch transfer jdpay", batch_transfer.to_str())
except Exception as e:
    raise
