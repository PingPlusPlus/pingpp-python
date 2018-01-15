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
        channel='cb_wx_pub_scan',  # https://www.pingxx.com/api#支付渠道属性值
        currency='hkd',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 必须,客户端软件中展示的条码值，扫码设备扫描获取
            scan_code='134566668888',
            # 必须，终端号，要求不同终端此号码不一样，如A01、SH008等
            terminal_id='SH008',
            # 可选,只能填写此值 "no_credit"
            limit_pay='no_credit',
            # 必须，商品列表 上送格式为:
            #     [
            #       {"goods_name":"iPhone6s 16G","goods_num":"1"},
            #       {"goods_name":"iPhone6s 32G","goods_num":"1"}
            #     ]            # 字段解释：goods_name:商品名称，goods_num:数量 1-5500
            goods_list=[
                dict(
                    goods_name='iPhone6 16G',
                    goods_num='1',
                ),
                dict(
                    goods_name='iPhone6s 16G',
                    goods_num='1',
                )
            ]
        )
    )
    print(charge)
except Exception as e:
    raise
