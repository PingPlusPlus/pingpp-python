# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"

app_id = 'app_1Gqj58ynP0mHeX1q'

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

'''
分润模块对象接口示例
'''

try:
    # 创建分润结算对象
    params = {
        "app": app_id,
        "name": "Your RoyaltyTemplate Name",  # 模板名称，允许中英文等常用字符
        "rule": {
            # 分润模式。分为按订单金额（包含优惠券金额）的比例 rate 和固定金额 fixed
            "royalty_mode": "rate",
            # 退分润模式。分为退款时不退分润 no_refund、
            #     按比例退分润 proportional 和一旦退款分润全退 full_refund
            "refund_mode": "no_refund",
            # 分配模式。指当订单确定的层级如果少于模板配置层级时，
            "allocation_mode": "receipt_reserved",
            # 模板中多余的分润金额是归属于收款方 receipt_reserved 还是服务方 service_reserved。
            "data": [
                {
                    # 子商户层级值，0 表示平台， 1 表示一级子商户，取值范围 >=0
                    "level": 1,
                    # 分润数值。rate 下取值为 0~10000，单位为 0.01 %，
                    #     fixed 下取值为 0 - 1000000，单位为分
                    "value": 20
                },
                {
                    "level": 2,
                    "value": 10
                }
            ]
        }
    }
    royalty_template = pingpp.RoyaltyTemplate.create(**params)
    print('create royalty_template', royalty_template)

    print('retrieve royalty_template', pingpp.RoyaltyTemplate.retrieve(
        royalty_template.id))
    print("list royalty_templates", pingpp.RoyaltyTemplate.list(app=app_id,
                                                                per_page=3))

    update_params = {
        "name": "Your RoyaltyTemplate Name New",
        "rule": {
            "royalty_mode": "fixed",
            "refund_mode": "full_refund",
            "allocation_mode": "service_reserved",
            "data": [
                {
                    "level": 1,
                    "value": 20
                },
                {
                    "level": 2,
                    "value": 10
                }
            ]
        }
    }
    print("update royalty_template", pingpp.RoyaltyTemplate.update(
        royalty_template.id, **update_params))
    print("delete royalty_template", pingpp.RoyaltyTemplate.delete(
        royalty_template.id))
except Exception as e:
    raise
