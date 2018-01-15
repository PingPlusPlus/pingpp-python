# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

# 设置 API Key
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
Transfer API 文档: https://www.pingxx.com/api#创建-transfer-对象
创建 Transfer 对象 - wx_pub
'''
try:
    tr = pingpp.Transfer.create(
        # 付款使用的商户内部订单号: wx_pub 规定为 1 ~ 50 位不能重复的数字字母组合
        order_no=str_random(20),
        # 目前支持支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay，余额:balance
        channel='wx_pub',
        # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100,企业付款最小发送金额为1 元）
        amount=100,
        # 三位 ISO 货币代码，目前仅支持人民币: cny 。
        currency='cny',
        app=dict(id='app_1Gqj58ynP0mHeX1q'),
        # 付款类型 (当前 alipay、wx_pub 仅支持: b2c,
        #     unionpay、allinpay、jdpay 支持:  b2b、b2c)
        type='b2c',
        # 接收者 id， 微信企业付款时为用户在 wx_pub 下的 open_id
        recipient='o9zp9jIaL6yMynQY9NxcZ',
        # 备注信息: 渠道为 wx_pub 时，最多 99 个英文和数字的组合或最多 33 个中文字符，不可以包含特殊字符；
        description='Your description',
        extra=dict(
            # 可选，收款人姓名。当该参数为空，则不校验收款人姓名。
            user_name='张三',
            # 可选，是否强制校验收款人姓名。仅当  user_name 参数不为空时该参数生效。
            force_check=False
        ),
    )
    print(tr.to_str())  # 输出 Ping++ 返回的企业付款对象 Transfer
except Exception as e:
    raise
