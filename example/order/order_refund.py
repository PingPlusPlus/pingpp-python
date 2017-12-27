# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入退款流程参考开发者中心：https://www.pingxx.com/docs/server ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os
import time

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

# 使用 Order 接口生成的订单中如果存在 charge id，不能通过charge id 来进行查询、退款操作，必须通过 Order ID 来操作

try:
    # 创建 order refunds
    params = {
        "description": "Your description"
    }
    order_refund = pingpp.OrderRefunds.create(order_id="2001708250000304601", **params)
    print ("create order refunds:\n", order_refund)
    # 获取 order refunds list
    order_refunds_list = pingpp.OrderRefunds.list(order_id="2001708250000304601")
    print(order_refunds_list)

    # 获取 order refunds
    order_refunds_detail = pingpp.OrderRefunds.retrieve(order_id="2001708250000304601",
                                                        refund_id="re_9yDmD8fDmf50P8mvHCiDC0aD")
    print order_refunds_detail
except Exception as e:
    print(e.http_body)
