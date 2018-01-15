# -*- coding: utf-8 -*-

'''
请求认证接口接口使用参考
API文档页面https://www.pingxx.com/api#请求认证接口
'''

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
# 该接口仅支持 Live Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

params = {
    "app": app_id,
    "data": {
        "id_name": "张三",
        "id_number": "320291198811110000",
        "card_number": "6201111122223333"
    },
    "type": "bank_card"
}
try:
    identification = pingpp.Identification.create(**params)
    print("identification result\n", identification)
except Exception as e:
    raise
