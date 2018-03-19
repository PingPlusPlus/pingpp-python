# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = "app_1Gqj58ynP0mHeX1q"
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

# 银行卡信息查询接口示例
try:
    card_info = pingpp.CardInfo.query(
        app=app_id,
        bank_account='6214888888888888'
    )
    print('card_info', card_info.to_str())
except Exception as e:
    print(e)
