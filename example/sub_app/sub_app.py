# -*- coding: utf-8 -*-

import pingpp
import os
import random
import string

pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# sub_app 接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')


def str_random(length=20):
    allchar = string.ascii_letters + string.digits
    return "".join(random.choice(allchar) for _ in range(length))


try:
    # 创建子商户
    suffix = str_random(16)
    params = {
        'display_name': 'sub_app_' + suffix,
        'user': "user_" + suffix,
        'metadata': {
            'key': 'value'
        },
        'description': 'Your description',
        # 'parent_app': 'app_rDyHSCy14aL8m9ev'
    }
    sub_app = pingpp.SubApp.create(**params)
    print('create sub_app', sub_app)

    # 更新子商户
    new_suffix = str_random(16)
    params = {
        'display_name': 'sub_app_' + new_suffix,
        'metadata': {
            'new_key': 'new_value'
        },
        'description': 'New description.',
        # 'parent_app': 'app_rDyHSCy14aL8m9ev'
    }
    sub_app = pingpp.SubApp.update(sub_app.id, **params)
    print('update sub_app', sub_app)

    # 查询子商户
    sub_app = pingpp.SubApp.retrieve(sub_app.id)
    print('retrieve sub_app', sub_app)

    # 删除子商户
    deleted = pingpp.SubApp.delete(sub_app.id)
    print('delete sub_app', deleted)

    # 获取子商户列表
    sub_app_list = pingpp.SubApp.list(per_page=3)
    print("list sub_apps", sub_app_list)
except Exception as e:
    raise
