# -*- coding: utf-8 -*-

import pingpp
import os

'''
优惠券接口
'''

pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

# coupon 接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"

params = {
    "coupon_template": "300118011516532300004701",
    "metadata": {
        "key": "value"
    }
}

try:
    # 创建优惠券
    coupon = pingpp.Coupon.create("user_001", **params)
    print(coupon)

    # 查询
    coupon = pingpp.Coupon.retrieve("user_001", "300318011517060000088302")
    print(coupon)

    # 获取列表
    coupon_list = pingpp.Coupon.list("user_001",
                                     per_page=3)
    print(coupon_list)

    # 更新优惠券
    update_params = {
        "metadata": {
            "new_key": "new_value"
        }
    }
    updated_coupon = pingpp.Coupon.update("user_001",
                                          coupon.id,
                                          **update_params)
    print(updated_coupon)

    # 删除优惠券
    deleted = pingpp.Coupon.delete("user_001", coupon.id)
    print(deleted)
except Exception as e:
    raise
