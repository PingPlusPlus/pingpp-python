# -*- coding: utf-8 -*-

import pingpp
import os

'''
优惠券接口
'''
# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
app_id = 'app_1Gqj58ynP0mHeX1q'
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')

# app_id 支持全局配置
pingpp.app_id = app_id

params = {
    "coupon_template": "300117082817355900186301",
    "metadata": {
        "key": "value"
    }
}

try:
    # 创建优惠券
    new_coupon = pingpp.Coupon.create(user="user_test_001", **params)
    print(new_coupon)

    # 查询
    retr_coupon = pingpp.Coupon.retrieve(new_coupon.id, user="user_test_001")
    print(retr_coupon)

    # 获取列表
    coupon_list = pingpp.Coupon.list(user="user_test_001")
    print(coupon_list)

    # 更新优惠券
    update_params = {
        "metadata": {
            "key": "value"
        }
    }
    update_coupon = pingpp.Coupon.update(new_coupon.id, user="user_test_001", **update_params)
    print(update_coupon)

    # 删除优惠券
    delete_coupon = pingpp.Coupon.delete(new_coupon.id, user="user_test_001")
    print(delete_coupon)
except Exception as e:
    print(e.http_body)
