# -*- coding: utf-8 -*-

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

"""
创建 agreement 对象，查询 agreement 对象，查询 agreement 对象列表
"""

agreement = pingpp.Agreement.create(
    app=app_id,  # App ID
    contract_no='2018123456789',  # 签约协议号
    channel='qpay',  # 签约渠道
    extra={
        'display_account': '测试商户名称'
    },  # 附加信息
    metadata={},  # metadata 元数据
)
print("创建 agreement 对象:")
try:
    print(agreement)
except Exception as e:
    print(e)

print("获取 Agreement 对象:")
try:
    agreement = pingpp.Agreement.retrieve('agr_19EEDSHUw3jXRF')
    print(agreement.to_str())
except Exception as e:
    print(e)

print("解约 agreement ：")
try:
    agreement = pingpp.Agreement.cancel('agr_19EEDSHUw3jXRF')
    print(agreement.to_str())
except Exception as e:
    print(e)

print("获取 Agreement 对象列表:")
try:
    params = {
        'app': app_id,
        'per_page': 10,
    }
    charges = pingpp.Agreement.list(**params)
    print(charges)
except Exception as e:
    print(e)
