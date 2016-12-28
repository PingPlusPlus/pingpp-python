# -*- coding: utf-8 -*-

'''
请求认证接口接口使用参考
API文档页面https://www.pingxx.com/api#请求认证接口
'''

import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q '
# 设置 API Key
pingpp.api_key = api_key
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
req_params = {
    "app": app_id,
    "data": {
        "id_name": "张三",
        "id_number": "320291198811110000",
        "card_number": "6201111122223333"
    },
    "type": "bank_card"
}
try:
    identification = pingpp.Identification.create(**req_params)
    print "identification  instance \n", identification

except Exception as e:
    print e
