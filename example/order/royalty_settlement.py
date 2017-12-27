# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  分润结算接口使用示例
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
分润结算对象接口示例
'''

try:
    # 创建分润结算对象
    params = {
        "payer_app": pingpp.app_id,
        "method": "unionpay",
        "recipient_app": pingpp.app_id,
        "created": {
            "gt": 1488211200,
            "lte": 1488297600
        },
        'is_preview': True  # 是否预览，选择预览不会真实创建分润结算对象，也不会修改分润对象的状态
    }
    royalty_settlement = pingpp.RoyaltySettlement.create(**params)
    print royalty_settlement

    # 查询分润结算列表
    params = {
        "page": 1,
        "per_page": 10,
        "payer_app": pingpp.app_id
    }
    royalty_settlement = pingpp.RoyaltySettlement.all(**params)
    print(royalty_settlement)

    # 查询分润结算对象
    royalty_settlement = pingpp.RoyaltySettlement.retrieve(id='430170320150300001')
    print(royalty_settlement)

    # 更新分润结算对象-确认
    royalty_settlement = pingpp.RoyaltySettlement.confirm(id='430170320150300001')
    print(royalty_settlement)

    # 更新分润结算对象-取消
    royalty_settlement = pingpp.RoyaltySettlement.cancel(id='430170320150300001')
    print(royalty_settlement)
except Exception as e:
    print(e.http_body)
