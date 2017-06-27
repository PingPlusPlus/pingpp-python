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
    批量转账-创建(unionpay)
"""

batch_no = "batchtrans" + str(random.randint(1, 10000))
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
            # 可选，批量企业付款描述，最多 200 字节。
            # "description": "Your description",
            # open_bank_code 和 open_bank 两个参数必传一个，建议使用 open_bank_code ，若都传参则优先使用 open_bank_code 读取规则。
            # 具体值参考此链接：https://www.pingxx.com/api#银行编号说明
            # 条件可选，1~50位，开户银行。
            "open_bank": "招商银行",
            # 条件可选，4位，开户银行编号。
            "open_bank_code": "0308",
            # 可选，订单号， 1 ~ 16 位数字。
            # "order_no": "123456789"
        },
        {
            "account": "656565656565656565656565",
            "amount": 3000,
            "name": "李四",
            "open_bank": "招商银行",
            "open_bank_code": "0308",
        }
    ],
    "type": "b2c",  # 付款类型 (当前 alipay、wx_pub 仅支持: b2c, unionpay、allinpay、jdpay 支持:  b2b、b2c)
    "channel": "unionpay",  # 目前支持 渠道。支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay
    "amount": 8000,  # 批量付款总金额，单位为分。为 recipients 中 amount 的总和。
    "app": app_id,
    "batch_no": "batchtrans20160801001",  # 批量转账批次号，3-24位，允许字母和英文
    "description": "Batch trans description."  # 批量转账详情，最多 255 个 Unicode 字符
}

try:
    # 创建批量批量转账
    bt = pingpp.BatchTransfer.create(**req_params)
    print(">> batch transfer instance %s" % bt)
except Exception as e:
    print(e.http_body)
