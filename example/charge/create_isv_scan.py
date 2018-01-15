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
        amount=1000000,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        app=dict(id=app_id),
        channel='isv_scan',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            scan_code='286801346868493272',  # 必须，客户端软件中展示的条码值，扫码设备扫描获取。
            terminal_id='SH008',  # 必须，终端号，要求不同终端此号码不一样，会显示在对账单中，如A01、SH008等。
            # 可选，商品列表，上送格式参照下面示例。
            # 字段解释：goods_id:商户定义商品编号（一般商品条码）
            #     unified_goods_id:统一商品编号(可选)，
            #     goods_name:商品名称，goods_num:数量
            #     price:单价(单位分)，goods_category:商品类目(可选)，
            #     body:商品描述信息(可选)，show_url:商品的展示网址(可选)
            goods_list=[
                dict(
                    goods_id='iphone6s16G',
                    unified_goods_id='1001',
                    goods_name='iPhone6s 16G',
                    goods_num=1,
                    price='528800',
                    goods_category='123456',
                    body='苹果手机16G',
                    show_url='https://www.example.com'
                ),
                dict(
                    goods_id='iphone6s32G',
                    unified_goods_id='1002',
                    goods_name='iPhone6s 32G',
                    goods_num=1,
                    price='608800',
                    goods_category='123789',
                    body='苹果手机32G',
                    show_url='https://www.example.com'
                )]
        )
    )
    print(charge.to_str())
except Exception as e:
    raise
