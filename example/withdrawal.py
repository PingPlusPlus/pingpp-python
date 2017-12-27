# -*- coding: utf-8 -*-

import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')
'''
    余额提现 Demo
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(__file__), 'your_rsa_private_key.pem')

request_info = {
    "amount": 20000,
    "user_fee": 50,
    'order_no': '1234567890',
    "description": "Your description",
    'channel': 'unionpay',  # channel值必须是 银联：unionpay，支付宝：alipay，微信：wx_pub，通联：allinpay，京东：jdpay其中一种
    "extra": {
        "card_number": "622123456789",  # 提现订单号，为长度不大于 16 的数字
        "user_name": "姓名",
        "open_bank_code": "0102",
        "prov": "上海",
        "city": "上海"
    },
    # "settle_account": "320217022818035400000601", # 使用结算账户提现，不需要填写 channel 和 extra 相关参数，同时填写时，结算账号不生效
}
# app_id 支持全局配置
pingpp.app_id = app_id
try:
    # 余额提现申请创建
    new_wd = pingpp.Withdrawal.create(user="user_id_001", **request_info)
    print(new_wd)

    # 余额提现列表
    retrieve_wd_list = pingpp.Withdrawal.list(user="user_id_001")
    print(retrieve_wd_list)

    # 获取余额提现申请信息
    retrieve_wd = pingpp.Withdrawal.retrieve("withDrawal_0002", app=app_id, user="user_id_001")
    print(retrieve_wd)

    # 余额提现取消
    cancel_wd_result = pingpp.Withdrawal.cancel("withDrawal_0002", app=app_id, user="user_id_001")
    pingpp.Withdrawal.cancel("withDrawl_0002")
    print(cancel_wd_result)

    # 余额提现确认
    confirm_wd_result = pingpp.Withdrawal.confirm("withDrawal_0002", app=app_id, user="user_id_001")
    print(confirm_wd_result)
except Exception as e:
    print(e.http_body)
