# -*- coding: utf-8 -*-

import pingpp
import os

app_id = 'app_1Gqj58ynP0mHeX1q'

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# 用户结算账号接口 app_id 支持全局配置
pingpp.app_id = app_id
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

user_id = "user_001"

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
    # `pingpp.app_id` 设置后，方法中的 `app=` 参数可不传
    settle_account = pingpp.SettleAccount.create(user_id, **params)
    print('create settle_account channel unionpay:', settle_account)
except Exception as e:
    print(e)

try:
    # 创建结算账号-支付宝渠道
    params = {
        "channel": "alipay",
        "recipient": {
            "account": "account@domain.com",
            "name": "李四",
            "type": "b2c"  # 转账类型。b2c：企业向个人付款。
        }
    }
    settle_account = pingpp.SettleAccount.create(user_id, **params)
    print('create settle_account channel alipay:', settle_account)
except Exception as e:
    print(e)

try:
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
    settle_account = pingpp.SettleAccount.create(user_id, **params)
    print('create settle_account - wx_pub:', settle_account)
except Exception as e:
    print(e)

try:
    # 查询结算账号
    settle_account = pingpp.SettleAccount.retrieve(user_id,
                                                   '320118011511463800000601')
    print('retrieve settle_account:', settle_account)
except Exception as e:
    print(e)

try:
    # 删除结算账号
    settle_account = pingpp.SettleAccount.delete(user_id,
                                                 '320118011511463800000601')
    print('delete settle_account:', settle_account)
except Exception as e:
    print(e)

try:
    # 获取结算账号列表
    settle_account_list = pingpp.SettleAccount.list(user_id)
    print('list settle_accounts', settle_account_list)
except Exception as e:
    print(e)
