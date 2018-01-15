# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


'''
Charge 支付 API 文档：https://www.pingxx.com/api#charges-支付
创建 charge 对象
'''

print("创建 charge 对象:")
try:
    charge = pingpp.Charge.create(
        order_no=str_random(20),  # 推荐使用 8-20 位，要求数字或字母，不允许其他字符
        amount=10000,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        app=dict(id=app_id),
        channel='jdpay_wap',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 必须，支付完成的回调地址。
            success_url='http://example.com/success',
            # 必须，支付失败页面跳转路径。
            fail_url='http://example.com/fail',
            # 可选，用户交易令牌，用于识别用户信息，支付成功后会调用 success_url 返回给商户。商户可以记录这个  token 值，
            # 当用户再次支付的时候传入该  token ，用户无需再次输入银行卡信息，直接输入短信验证码进行支付。32 位字符串。
            # token='dsafadsfasdfadsjuyhfnhujkijunhaf',
            # 可选，订单类型，值为0表示实物商品订单，值为 1 代表虚拟商品订单，该参数默认值为 0 。
            # order_type=0,
            # 可选，设置是否通过手机端发起支付，值为 true 时调用手机 h5 支付页面，
            #     值为 false 时调用 PC 端支付页面，该参数默认值为  true 。
            # is_mobile=True,
            # 可选，用户账号类型，取值只能为：BIZ。
            #     传参存在问题请参考帮助中心：https://help.pingxx.com/article/1012535/。
            # user_type='BIZ',
            # 可选，商户的用户账号。
            #     传参存在问题请参考帮助中心：https://help.pingxx.com/article/1012535/。
            # user_id='your user_id'
        )
    )
    print(charge)
except Exception as e:
    raise
