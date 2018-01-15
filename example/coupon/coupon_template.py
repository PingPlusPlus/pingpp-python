# -*- coding: utf-8 -*-

import pingpp
import os

'''
优惠券模板接口
'''

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

# coupon_template 接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"

try:
    params = {
        "name": "25OFF",  # 优惠券模板名称
        "type": 2,  # 优惠券模板的类型 1：现金券；2：折扣券,
        "percent_off": 25,  # 折扣百分比, 如 20 表示 8 折, 100 表示免费。当 type 为 2 时，必传。
        # 订单金额大于等于该值时，优惠券有效（适用于满减）；0 表示无限制
        "amount_available": 10000,
        # 优惠券最大生成数量，当已生成数量达到最大值时，不能再生成优惠券；默认 null，表示可以无限生成
        "max_circulation": 1000,
        # "amount_off": 10,  # 折扣金额。当 type 为 1 时，必传。
        "metadata": {
        },
        "expiration": {
            # 指定起始时间戳（time_start）、结束时间戳（time_end），如果不指定，表示没有限制。
            # "time_start": 1503658305,
            # "time_end": 1506250305,
        },
        "refundable": True  # 退款时是否恢复优惠券
    }
    # 创建优惠券模板
    coupon_template = pingpp.CouponTemplate.create(**params)
    print(coupon_template)

    # 获取优惠券模板列表
    coupon_template_list = pingpp.CouponTemplate.list(per_page=3)
    print(coupon_template_list)

    # 查询优惠券模板
    coupon_template = pingpp.CouponTemplate.retrieve(coupon_template.id)
    print(coupon_template)

    # 更新优惠券模板
    update_params = {
        "metadata": {
            "new_key": 'new_value'
        }
    }
    updated_coupon_template = pingpp.CouponTemplate.update(coupon_template.id,
                                                           **update_params)
    print(updated_coupon_template)

    # 批量创建优惠券
    create_coupons_params = {
        "users": [
            "user_001",
            "user_002"
        ]
    }
    batch_create_coupons = pingpp.CouponTemplate.create_coupons(
        coupon_template.id, **create_coupons_params)
    print(batch_create_coupons)

    # 查询模板下的优惠券
    coupon_list = pingpp.CouponTemplate.list_coupons(
        coupon_template.id)
    print(coupon_list)

    # 删除优惠券模板
    deleted = pingpp.CouponTemplate.delete(coupon_template.id)
    print(deleted)
except Exception as e:
    raise
