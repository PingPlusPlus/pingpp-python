# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  分润结算接口使用示例
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os
import random

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
    用户余额转账 Demo
'''
try:
    params = {
        "amount": 100,  # 必填,支付受赠余额，单位：分
        "user": "user_test_01",  # 必填,发起转账的用户 ID（可以是 customer 或 business，但不能填 0）
        "recipient": "user_test_02",  # 必填,接收转账的用户 ID（可以是 customer 或 business，可以为 0）
        "order_no": '12345678',  # 必填,商户订单号，必须在商户系统内唯一
        "description": "Your description",  # 选填,描述
        "metadata": {}  # 选填,metadata 元数据
    }
    print 'create balance_bonus', pingpp.BalanceTransfer.create(**params)
    print("retrieve balance_bonus", pingpp.BalanceTransfer.retrieve("660170815382093332480000"))
    print("list balance_bonus", pingpp.BalanceTransfer.list())
except Exception as e:
    print(e.http_body)
