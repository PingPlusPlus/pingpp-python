# -*- coding: utf-8 -*-
import pingpp
import os

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'

# 用户接口 app_id 支持全局配置
pingpp.app_id = app_id

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
    用户 Demo
'''

# id 唯一, 测试需重新生成
user_id = "user_001"

params = {
    "id": user_id,
    "address": "Address",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {},
    "mobile": None,
    "name": "Your Name"
}

# 可以变动app_id
try:
    # 创建 user
    user = pingpp.User.create(app=app_id, **params)
    print(user)
except Exception as e:
    print(e)

# 获取user 列表
user_list = pingpp.User.list(app=app_id, per_page=3)
print(user_list)

# 获取指定 user 信息
retrieved_user = pingpp.User.retrieve(user_id, app=app_id)
print(retrieved_user)

# 更新 user
params = {
    "address": "New Address",
    "avatar": None,
    "email": None,
    "gender": "MALE",
    "metadata": {"birthday": "2017-12-24"},
    "mobile": None,
    "name": "Your New Name",
}
user = pingpp.User.update(user_id, app=app_id, **params)
print(user)
