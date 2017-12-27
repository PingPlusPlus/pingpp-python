# -*- coding: utf-8 -*-

"""
Batch Transfers 批量企业付款接口使用参考 具体使用请参考 (https://www.pingxx.com/api#创建-batch-transfer-对象)
"""

import pingpp
import random
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = "app_1Gqj58ynP0mHeX1q"
# 设置 API Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), "your_rsa_private_key.pem")
"""
    批量转账-创建(balance 余额渠道)
"""

batch_no = "batchtrans" + str(random.randint(1, 10000))
# 创建
req_params = {
    "recipients": [
        {
            # 必须，接收者用户 ID。
            "user": "user_test_01",
            # 必须，金额，单位为分。
            "amount": 5000,
            # 可选，批量付款描述，最多 100 个 Unicode 字符。
            "description": "Your description",
            # 可选，订单号， 1 ~ 64 位不能重复的数字字母组合。
            # "order_no": "201708086666666"
        },
        {
            "user": "user_test_02",
            "amount": 3000,
            "description": "Your description"
        }
    ],
    "type": "b2c",  # 付款类型 (当前 alipay、wx_pub 仅支持: b2c, unionpay、allinpay、jdpay 支持:  b2b、b2c)
    "channel": "balance",  # 目前支持 渠道。支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay 余额：balance。
    "amount": 8000,  # 批量付款总金额，单位为分。为 recipients 中 amount 的总和。
    "app": app_id,
    "batch_no": batch_no,  # 批量转账批次号，3-24位，允许字母和英文
    "description": "Batch trans description."  # 批量转账详情，最多 255 个 Unicode 字符
}

try:
    # 创建批量批量转账
    bt = pingpp.BatchTransfer.create(**req_params)
    print(">> batch transfer instance %s" % bt)
except Exception as e:
    print(e.http_body)
