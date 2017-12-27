# -*- coding: utf-8 -*-

import pingpp
import os

'''
    优惠券模板接口
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

# app_id 支持全局配置
pingpp.app_id = app_id
try:
    params = {
        "name": "25OFF",  # 优惠券模板名称
        "type": 2,  # 优惠券模板的类型 1：现金券；2：折扣券,
        "percent_off": 25,  # 折扣百分比, 如 20 表示 8 折, 100 表示免费。当 type 为 2 时，必传。
        "amount_available": 10000,  # 订单金额大于等于该值时，优惠券有效（适用于满减）；0 表示无限制
        "max_circulation": 1000,  # 优惠券最大生成数量，当已生成数量达到最大值时，不能再生成优惠券；默认 null，表示可以无限生成
        # "amount_off": 10,  # 折扣金额。当 type 为 1 时，必传。
        "metadata": {
        },
        "expiration": {
            "time_start": 1503658305,  # 指定起始时间戳（time_start）、结束时间戳（time_end），如果不指定，表示没有限制。
            "time_end": 1506250305,
        },
        "refundable": True  # 退款时是否恢复优惠券
    }
    # 创建优惠券模板
    new_coupon = pingpp.CouponTemplate.create(app=app_id, **params)
    print(new_coupon)

    # 获取优惠券模板列表
    coupon_templ_list = pingpp.CouponTemplate.list()
    print(coupon_templ_list)

    # 查询优惠券模板
    retr_coupon_templ = pingpp.CouponTemplate.retrieve(new_coupon.id)
    print(retr_coupon_templ)

    # 更新优惠券模板
    update_coupon_tpl_params = {
        'metadata': {
            'key': 'value'
        }
    }
    update_coupon_templ = pingpp.CouponTemplate.update(new_coupon.id, **update_coupon_tpl_params)
    print(update_coupon_templ)

    # 批量创建优惠券
    create_params = {
        "users": [
            "test_user_001",
            "test_user_002"
        ]
    }
    batch_create_coupons = pingpp.CouponTemplate.create_coupons(app=app_id, coupon_tmpl=new_coupon.id,
                                                                **create_params)
    print(batch_create_coupons)

    # 查询模板下的优惠券
    tmpl_coupon_list = pingpp.CouponTemplate.retrieve_coupons(coupon_tmpl=new_coupon.id)
    print(tmpl_coupon_list)

    # 删除优惠券模板
    delete_coupon_templ = pingpp.CouponTemplate.delete(new_coupon.id)
    print delete_coupon_templ
except Exception as e:
    print(e.http_body)
