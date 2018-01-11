# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  结算账号接口示例
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
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')
try:
    # 创建结算账号-中国银联渠道
    params = {
        "channel": "bank_account",
        "recipient": {
            "account": "6214850266666666",
            "name": "张三",
            "type": "b2c",  # 转账类型。b2c：企业向个人付款，b2b：企业向企业付款。
            "open_bank": "招商银行",
            "open_bank_code": "0308"
        }

    }
    settle_account = pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_004', **params)
    print('create settle_account - unionpay:', settle_account)
    # 创建结算账号-支付宝渠道
    params = {
        "channel": "alipay",
        "recipient": {
            "account": "account@domain.com",
            "name": "李四",
            "type": "b2c"  # 转账类型。b2c：企业向个人付款。
        }

    }
    settle_account = pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_004', **params)
    print('create settle_account -alipay:', settle_account)
    # 创建结算账号-微信渠道
    params = {
        "channel": "wx_pub",
        "recipient": {
            "account": "your_open_id",
            "name": "王五",
            "type": "b2c",  # 转账类型。b2c：企业向个人付款。
            "force_check": False
        }

    }
    settle_account = pingpp.SettleAccount.create(app=pingpp.app_id, user='test_user_004', **params)
    print('create settle_account - wx_pub:', settle_account)
    # 查询结算账号
    settle_account = pingpp.SettleAccount.retrieve(app=pingpp.app_id, user='test_user_004',
                                                   settle_account_id='320117082519305500005901')
    print('retrieve settle_account:', settle_account)
    # 删除结算账号
    settle_account = pingpp.SettleAccount.delete(app=pingpp.app_id, user='test_user_004',
                                                 settle_account_id='320117082519305500005901')
    print('delete settle_account - wx_pub:', settle_account)

    # 获取结算账号列表
    settle_account_list = pingpp.SettleAccount.list(app=pingpp.app_id, user='test_user_004')
    print('retrieve all settle_accounts', settle_account_list)

except Exception as e:
    print(e.http_body)
