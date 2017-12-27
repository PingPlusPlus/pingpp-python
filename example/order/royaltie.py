# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  批量更新分润对象,查询,查询列表示例
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

'''
分润接口示例
'''
try:
    params = {
        "ids": [
            "170301124238000111",
            "170301124238000211"
        ],
        "method": "manual",
        "description": "Your description"
    }
    # 批量更新分润对象
    royalties = pingpp.Royaltie.update(**params)
    print royalties
    # 查询分润对象列表
    params = {
        'page': 1,
        'per_page': 15
    }
    royalties = pingpp.Royaltie.all(**params)
    print royalties
    # 查询分润对象
    royaltie = pingpp.Royaltie.retrieve('410170320160900002')
    print royaltie
except Exception as e:
    print e.http_body
