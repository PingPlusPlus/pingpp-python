# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
  子商户渠道设置接口示例
'''
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->企业设置->开发设置-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key
# app_id 支持全局配置
pingpp.app_id = app_id
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

try:
    # 创建子商户渠道参数
    params = {
        "banned_msg": None,
        "channel": "alipay",
        "description": "Your description",
        "params": {
            "alipay_account": "example@example.com",
            "alipay_app_id": "2016666666666666",
            "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFYBbIo698oeToWRvAcqTw4TEZKa\nwKPIJrZ4pbZPooSriP6aqXIqRnM3734/gcJso24IZheM+sgz0An8+wN4bQ2Y/qO8\nSOh3HNDPzYuhR+CRajIOkGWUjxmqmi14zcLgWgURrgmdBIccM5BnRSFWdUWZTzez\ngl75CdmtXHmst7LNAgMBAAE=\n-----END PUBLIC KEY-----",
            "alipay_app_public_key_rsa2": None,
            "alipay_mer_app_private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+KDkMaoEy1t+0\nN5tYCgsHJRDogpknCoUVA5aiGBl4E8SyC3gWRB9j6/FUCKYWobUnZoFur3XDd7Bs\ni57vJRQmEow1dYA3PIHAaLE3fzDTm1joJqExfctrS27AqxDWKcKxgDE8hcbhMCgN\nq24BHl+KVCSG7c3X1yY+lO393m7x6CVpSVPerx7PMaW28M+zRdIMHTLPG6v/0r6r\ny/yodjWKoZU7KlpQndgTzChIZIxb0hC578DAaTVBQv9lWenG84S3/s/kzO9j7YFR\nF3dn5XFx5LhzQdfctXmLmyqfUoL23FxDlI3BApAHjKCXdStZdWqFBeffdDK9WZ1/\n7qKigV93AgMBAAECggEABbXPgL/yAUTSkubYk1w52I0UZOcHElUOigMBkvyGR0TQ\ns0gE4yZIiweax5s64ZMZjYVWfaxnLOd7NMc8jpHeeQY1j6VnpED85HpAWBpJrREN\nKmt+i63rXd12BfMdHlFCt3HSCK87uadojICJXR88XzsHncWmWMTtMRPn0afMTRdO\nPwzTqVzRsavl6fuzhgufwMc9ZRJDcEZBAfXcvmGTj8xVqW7G3hsys7rXYODAgLdT\nThXaNaOqjm5VGaQE+oPHQsMiBbd+ojzA8swPMIiFfcCVoiI3tHx39iwhEsRnoHLU\n3IAPNBB7EG4AY1ljxSJFHHWkUu8jYZjXEfk6ethrgQKBgQDtRVkUpQqaz7HbGMfY\nSffopdkDMRdfBoRXXzEhJlLrIzEJ9JyIgWBZXo6M0oO30tZ7nQuCZCpy2NXRRA4h\nglHNFXobZeTpKc9C2ipBDZBzc5Pqn/MbeJ7aTIowXbuW91cYi/wjRfWX8G/E9PvK\ne8/JzNpRMYZhXOWruzY6zXElRQKBgQDNKtLBisA3L66stuzu2+MC19QIjWktbJkp\n33vOd/MrAXgotEkY+q3HsWXJzlEKdTuUaLVgP2IdtlwSCTcmHgd4WFIhp0tcYC56\n4XZR2l6db/8xX9CT+WYsbmdzHX6s7YJ+FJ0jLhVoXLKa8Eqp50SOJylnxnRH6k9v\nUjW+t4xHiwKBgQCnG3li1d5DLFZaNfjCN05X1z6hRdjs/z0EADIs473wh4eJOHNq\nnJwMNVF2kulb9S1EQFYTzpIq8tacnS7KoOsV4rNuSnRPVzf3IIoz6Oa8uUELNP3W\ncjyHCPMmn014RNldm3HIMgSHrzo44EXZ1RuCSDnWh2faeL/1FFRcU8cFdQKBgGxd\nPPoaxhGf7rus1pIGs+2Rf52Qy0fBv1g9gQ/5jQde/E9LgfxekyERUrj3bxh9+R0W\n/Q28DJ+y7Qhds7I/VCS9SYwa55P//SzMHwl2tFilif1TJUCzDsNTAPLtVjYSMMVV\nL/Yf5hC8PV3WoykATNZkWttEF7DQUmpy2o5ENiSnAoGBAMsuflxpK6Apkp35EpgF\n+72JCTbHUZxdFa8O4K6SHg3+gbxedJu4LrUpMu5LBDeNDlugqH4XqcPm1cl8Fozm\ntDwJfYhVb7FZ1bmkBu+FzjywnHIDzAOlErVqo4Abl1ch2t9kDkfuT5L+1JHpHX0K\nHSzBs2bCJaGq5Lm+K3je8GNr\n-----END PRIVATE KEY-----",
            "alipay_mer_app_private_key_rsa2": None,
            "alipay_pid": "2088111111111111",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "a5srakrbci3nf1pracb52xcs9xlhu8gu",
            "alipay_sign_type": "rsa",
            "alipay_version": 1,
            "fee_rate": 80
        }
    }
    channel = pingpp.Channel.create(app=pingpp.app_id, sub_app_id='app_ibXHGCzPaLe9fLqH', **params)
    print('create sub_app channel:', channel)

    # 更新子商户渠道参数
    updateParams = {
        'description': 'Your Channel description',
        "params": {
            "alipay_account": "example2@example.com",
            "alipay_app_id": "2016666666666668",
            "alipay_app_public_key": "-----BEGIN PUBLIC KEY-----\nMIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFYBbIo698oeToWRvAcqTw4TEZKa\nwKPIJrZ4pbZPooSriP6aqXIqRnM3734/gcJso24IZheM+sgz0An8+wN4bQ2Y/qO8\nSOh3HNDPzYuhR+CRajIOkGWUjxmqmi14zcLgWgURrgmdBIccM5BnRSFWdUWZTzez\ngl75CdmtXHmst7LNAgMBAAE=\n-----END PUBLIC KEY-----",
            "alipay_app_public_key_rsa2": None,
            "alipay_mer_app_private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+KDkMaoEy1t+0\nN5tYCgsHJRDogpknCoUVA5aiGBl4E8SyC3gWRB9j6/FUCKYWobUnZoFur3XDd7Bs\ni57vJRQmEow1dYA3PIHAaLE3fzDTm1joJqExfctrS27AqxDWKcKxgDE8hcbhMCgN\nq24BHl+KVCSG7c3X1yY+lO393m7x6CVpSVPerx7PMaW28M+zRdIMHTLPG6v/0r6r\ny/yodjWKoZU7KlpQndgTzChIZIxb0hC578DAaTVBQv9lWenG84S3/s/kzO9j7YFR\nF3dn5XFx5LhzQdfctXmLmyqfUoL23FxDlI3BApAHjKCXdStZdWqFBeffdDK9WZ1/\n7qKigV93AgMBAAECggEABbXPgL/yAUTSkubYk1w52I0UZOcHElUOigMBkvyGR0TQ\ns0gE4yZIiweax5s64ZMZjYVWfaxnLOd7NMc8jpHeeQY1j6VnpED85HpAWBpJrREN\nKmt+i63rXd12BfMdHlFCt3HSCK87uadojICJXR88XzsHncWmWMTtMRPn0afMTRdO\nPwzTqVzRsavl6fuzhgufwMc9ZRJDcEZBAfXcvmGTj8xVqW7G3hsys7rXYODAgLdT\nThXaNaOqjm5VGaQE+oPHQsMiBbd+ojzA8swPMIiFfcCVoiI3tHx39iwhEsRnoHLU\n3IAPNBB7EG4AY1ljxSJFHHWkUu8jYZjXEfk6ethrgQKBgQDtRVkUpQqaz7HbGMfY\nSffopdkDMRdfBoRXXzEhJlLrIzEJ9JyIgWBZXo6M0oO30tZ7nQuCZCpy2NXRRA4h\nglHNFXobZeTpKc9C2ipBDZBzc5Pqn/MbeJ7aTIowXbuW91cYi/wjRfWX8G/E9PvK\ne8/JzNpRMYZhXOWruzY6zXElRQKBgQDNKtLBisA3L66stuzu2+MC19QIjWktbJkp\n33vOd/MrAXgotEkY+q3HsWXJzlEKdTuUaLVgP2IdtlwSCTcmHgd4WFIhp0tcYC56\n4XZR2l6db/8xX9CT+WYsbmdzHX6s7YJ+FJ0jLhVoXLKa8Eqp50SOJylnxnRH6k9v\nUjW+t4xHiwKBgQCnG3li1d5DLFZaNfjCN05X1z6hRdjs/z0EADIs473wh4eJOHNq\nnJwMNVF2kulb9S1EQFYTzpIq8tacnS7KoOsV4rNuSnRPVzf3IIoz6Oa8uUELNP3W\ncjyHCPMmn014RNldm3HIMgSHrzo44EXZ1RuCSDnWh2faeL/1FFRcU8cFdQKBgGxd\nPPoaxhGf7rus1pIGs+2Rf52Qy0fBv1g9gQ/5jQde/E9LgfxekyERUrj3bxh9+R0W\n/Q28DJ+y7Qhds7I/VCS9SYwa55P//SzMHwl2tFilif1TJUCzDsNTAPLtVjYSMMVV\nL/Yf5hC8PV3WoykATNZkWttEF7DQUmpy2o5ENiSnAoGBAMsuflxpK6Apkp35EpgF\n+72JCTbHUZxdFa8O4K6SHg3+gbxedJu4LrUpMu5LBDeNDlugqH4XqcPm1cl8Fozm\ntDwJfYhVb7FZ1bmkBu+FzjywnHIDzAOlErVqo4Abl1ch2t9kDkfuT5L+1JHpHX0K\nHSzBs2bCJaGq5Lm+K3je8GNr\n-----END PRIVATE KEY-----",
            "alipay_mer_app_private_key_rsa2": None,
            "alipay_pid": "2088111111111112",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "a5srakrbci3nf1pracb52xcs9xlhu8ga",
            "alipay_sign_type": "rsa",
            "alipay_version": 1,
            "fee_rate": 80
        },
        'banned': False,
    }
    channel = pingpp.Channel.update(app=pingpp.app_id, sub_app_id='app_ibXHGCzPaLe9fLqH', channel='alipay',
                                    **updateParams)
    print('update sub_app channel :', channel)

    # 查询子商户渠道参数
    channel_list = pingpp.Channel.retrieve(app=pingpp.app_id, sub_app_id='app_ibXHGCzPaLe9fLqH', channel='alipay')
    print('retrieve sub_app channel list:', channel_list)

    # 删除子商户渠道参数
    channel_del = pingpp.Channel.delete(app=pingpp.app_id, sub_app_id='app_ibXHGCzPaLe9fLqH', channel='alipay')
    print('delete sub_app channel:', channel_del)

except Exception as e:
    print(e.http_body)
