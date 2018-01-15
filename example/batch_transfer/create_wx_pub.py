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
批量转账-创建(wx_pub)
"""

# 创建
req_params = {
    "recipients": [
        {
            # 必须，接收者 id，为用户在 wx_pub 下的 open_id。
            "open_id": "openidxxxxxxxxxxxx",
            # 必须，金额，单位为分。
            "amount": 5000,
            # 可选，收款人姓名。当该参数为空，则不校验收款人姓名。
            "name": "张三",
            # 可选，批量企业付款描述，最多 99 个英文和数字的组合或最多 33 个中文字符，不可以包含特殊字符。
            # 不填默认使用外层参数中的 description。
            "description": "Your description",
            # 可选，是否强制校验收款人姓名。布尔类型，仅当 name 参数不为空时该参数生效。
            "force_check": False,
            # 可选，订单号， 1 ~ 32 位不能重复的数字字母组合。
            "order_no": "123456789"
        },
        {
            "open_id": "openidxxxxxxxxxxxx",
            "amount": 3000,
        }
    ],
    # 付款类型 (当前 alipay、wx_pub 仅支持: b2c, unionpay、allinpay、jdpay 支持:  b2b、b2c)
    "type": "b2c",
    # 渠道。支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay 余额：balance。
    "channel": "wx_pub",
    "amount": 8000,  # 批量付款总金额，单位为分。为 recipients 中 amount 的总和。
    "app": app_id,
    "batch_no": str_random(20),  # 批量转账批次号，3-24位，允许字母和英文
    "description": "Batch transfer description."  # 批量转账详情，最多 255 个 Unicode 字符
}

try:
    # 创建批量批量转账
    bt = pingpp.BatchTransfer.create(**req_params)
    print(">> batch transfer instance %s" % bt)
except Exception as e:
    raise
