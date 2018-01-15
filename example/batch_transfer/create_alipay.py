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
批量转账-创建(alipay)
"""

# 创建
params = {
    "recipients": [
        {
            # 必须，接收者支付宝账号。
            "account": "account01@alipay.com",
            # 必须，金额，单位为分。
            "amount": 5000,
            # 必须，接收者姓名。
            "name": "李四",
            # 可选，批量企业付款描述，最多 200 字节。
            # "description": "Your description",
            # 可选，账户类型，alipay 2.0 渠道会用到此字段，取值范围：
            #    1、ALIPAY_USERID：支付宝账号对应的支付宝唯一用户号。以2088开头的16位纯数字组成。
            #    2、ALIPAY_LOGONID（默认值）：支付宝登录号，支持邮箱和手机号格式。
            # "account_type": "ALIPAY_LOGONID",
            # 可选，订单号， 1 ~ 64 位不能重复的数字字母组合。
            # "order_no": "123456789"
        },
        {
            "account": "account02@alipay.com",
            "amount": 3000,
            "name": "张三"
        }
    ],
    # 付款类型。当前 alipay、wx_pub 仅支持: b2c，
    #    unionpay、allinpay、jdpay 支持:  b2b、b2c
    "type": "b2c",
    # 渠道。支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay 余额：balance。
    "channel": "alipay",
    "amount": 8000,  # 批量付款总金额，单位为分。为 recipients 中 amount 的总和。
    "app": app_id,
    "batch_no": str_random(20),  # 批量转账批次号，3-24位，允许字母和英文
    "description": "Batch transfer description."  # 批量转账详情，最多 255 个 Unicode 字符
}

try:
    # 创建批量批量转账
    batch_transfer = pingpp.BatchTransfer.create(**params)
    print(">> batch transfer alipay", batch_transfer.to_str())
except Exception as e:
    raise
