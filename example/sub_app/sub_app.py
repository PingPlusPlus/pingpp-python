# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  子商户接口使用示例
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->企业设置->开发设置-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key
# app_id 支持全局配置
pingpp.app_id = app_id
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

try:
    # 创建子商户
    params = {
        'display_name': 'sub_app_display_name',
        'user': 'test_user_004',
        'metadata': {
            'key': 'value'
        },
        'description': 'Your description',
        # 'parent_app': 'app_rDyHSCy14aL8m9ev'
    }
    sub_app = pingpp.SubApp.create(app=pingpp.app_id, **params)
    print('create sub_app', sub_app)

    # 更新子商户
    params = {
        'display_name': 'sub_app_display_name2',
        'metadata': {
            'key': 'value2'
        },
        'description': 'Your description2',
        # 'parent_app': 'app_rDyHSCy14aL8m9ev'
    }
    sub_app = pingpp.SubApp.update(app=app_id, id=sub_app.id, **params)
    print('update sub_app ', sub_app)

    # 查询子商户
    sub_app = pingpp.SubApp.retrieve(app=pingpp.app_id, id=sub_app.id)
    print('retrieve sub_app', sub_app)

    # 删除子商户
    sub_app = pingpp.SubApp.delete(app=app_id, id=sub_app.id)
    print('delete sub_app ', sub_app)

    # 获取子商户列表
    sub_app_list = pingpp.SubApp.list(app=pingpp.app_id)
    print("retrieve sub_app list", sub_app_list)
except Exception as e:
    print e.http_body
