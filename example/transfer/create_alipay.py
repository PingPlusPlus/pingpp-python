# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string


# 设置 API Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
Transfer API 文档: https://www.pingxx.com/api#创建-transfer-对象
创建 Transfer 对象 - alipay
'''
try:
    tr = pingpp.Transfer.create(
        # 付款使用的商户内部订单号: alipay 为 1 ~ 64 位不能重复的数字字母组合
        order_no=str_random(20),
        # 目前支持支付宝：alipay，银联：unionpay，微信公众号：wx_pub，通联：allinpay，京东：jdpay，余额:balance
        channel='alipay',
        # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100,企业付款最小发送金额为1 元）
        amount=100,
        # 三位 ISO 货币代码，目前仅支持人民币: cny 。
        currency='cny',
        app=dict(id='app_1Gqj58ynP0mHeX1q'),
        # 付款类型 (当前 alipay、wx_pub 仅支持: b2c,
        #     unionpay、allinpay、jdpay 支持:  b2b、b2c)
        type='b2c',
        # 接收者 id，渠道为 alipay 时，若 type 为 b2c，为个人支付宝账号，若 type 为 b2b，为企业支付宝账号
        recipient='user001@gmail.com',
        extra=dict(
            # 必须，收款人姓名，1~50位。
            recipient_name='张三',
            # 可选，收款方账户类型。可取值：1、ALIPAY_USERID：支付宝账号对应的支付宝唯一用户号。
            #     以2088开头的16位纯数字组成。 2、ALIPAY_LOGONID（默认值）：支付宝登录号，支持邮箱和手机号格式。
            # recipient_account_type='ALIPAY_LOGONID',
        ),
        description='description'
    )
    print(tr.to_str())  # 输出 Ping++ 返回的企业付款对象 Transfer
except Exception as e:
    raise
