# -*- coding: utf-8 -*-
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
    用户Demo
'''
# id 唯一, 测试需重新生成
request_info = {
    "id": "test_user_0010",
    "address": "address_1",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your user name"
}

# app_id 支持全局配置
pingpp.app_id = app_id
# 可以变动app_id
try:
    # 创建user
    user = pingpp.User.create(app=app_id, **request_info)
    print(user)

    # 获取user 列表
    user_list = pingpp.User.list()
    print(user_list)

    # 获取指定 user id 信息
    retrieve_user = pingpp.User.retrieve("test_user_01", app=app_id)
    print(retrieve_user)

    # 更新user 信息
    update_param = {
        "address": "new address_1",
        "avatar": None,
        "email": None,
        "gender": "MALE",
        "metadata": {},
        "mobile": None,
        "name": "Your new name"
    }
    user_update = pingpp.User.update(app=app_id, user="test_user_0005", **update_param)
    print(user_update)

except Exception as e:
    print(e.http_body)
