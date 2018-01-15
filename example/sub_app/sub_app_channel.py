# -*- coding: utf-8 -*-

import pingpp
import os

# 设置 API Key 该接口仅支持 Live Key
pingpp.api_key = "sk_test_ibbTe5jLGCi5rzfH4OqPW9KC"
# sub_app 渠道参数接口支持全局配置 app_id
pingpp.app_id = "app_1Gqj58ynP0mHeX1q"

pingpp.private_key_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'your_rsa_private_key.pem')

"""
transfer_channel 接口与 channel 接口调用方法相同，方法为：
    pingpp.SubApp.create_transfer_channel("SUB_APP_ID")
    pingpp.SubApp.retrieve_transfer_channel("SUB_APP_ID", "CHANNEL")
    pingpp.SubApp.update_transfer_channel("SUB_APP_ID", "CHANNEL")
    pingpp.SubApp.delete_transfer_channel("SUB_APP_ID", "CHANNEL")
"""

try:
    # 创建子商户渠道参数
    params = {
        "banned_msg": None,
        "channel": "alipay",
        "description": "Your description",
        "params": {
            "alipay_account": "example@example.com",
            "alipay_app_id": "2016666666666666",
            "alipay_app_public_key": None,
            "alipay_app_public_key_rsa2": """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg3sPgpSdkpuy97Tfq3zA
BUaiN6Egkx21Wf2gHV6c/vIpxHfJDXcKJgnaOmJpWBwsrRGiqC89T0efT2Z7RO9c
D5BP8n3O8ok9xkxRhT/ptXjC8Ly5TmOha/p09qzhM0nczVEhBtisR7uAubl+RwKD
/x4K/PEX4TRdjvxKHJhIBC0wJYWPANhPJJoCi9Mua6wP4kmUbrVXcs7V4pLA3yke
DC+gg9vsdD8NYiJ7AQu169LxLanSF1r9pUkZIiOuRwwjwE/TwaKYAE22eLmBG70J
TukYulv5BK2qLlZtNM1NQQTc2CdJBmF3r080x6UACddzRs0UkhinijlESpt+bHFj
gwIDAQAB
-----END PUBLIC KEY-----
""",
            "alipay_mer_app_private_key": None,
            "alipay_mer_app_private_key_rsa2": """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3CN8dCG9bpWSR
HMypeUAl9CspbovXJVVmqmkhMnalb+07t6bJB35KgYRnoi3iyArZDQiiSADIhWb8
63zOPaiyg8SQCqwNRwqOedMPDNz/wyrmGncECvv4Oyp2PoW/1t6TPljfwZIJO5f0
KZnVqsMqkr0F71eQ00FEZKR/xT+QkoJ74/BGmqs73NIe4wxg9QxLJJLFLsZxA9bW
7qNAsiLIu9nPG7+8Heewqlrva3SmFXBVuZ48TeRH0HetKam3Vvl72KkylEb8s1iu
09NUMBiFf77rA43hiUhDHKIYL2Gsf0MZKQksOcln5WCJWouQKH5Qk2iR5JDE6aEs
i/pp0SKVAgMBAAECggEAObM+QrTKBiYZkfV2P2bN5ikXAjSrOOO4DGlkQubZqEWk
j9LRbUZDddFmoBTsSjWt1cbaFe6E8LG9SbYi3hFqAPyxFoeGvZjLpyaYdoIjmS05
dNia9FdSH2rnc+c52sQt3lUlR0SKeQakXIBQ0p7Gb8FafWh6Plmalaj0gqL36ub7
dOhKXvXMtPaEWU913A50RwKYjWABRpP26XQ9mqURHpu4qEV8EUozo+HLjZ7ZiLwl
9Jqpt/ISTdn2PYNqcTdy7zRlyKbWiMJwHQZxAcMrlf7pkoYgIkqNmjwBMII/jlsh
+Dm2e2/FutYrZhEuwSfDx/+qvSVPq2jV5K7fB9rHAQKBgQDzmDod9gPDl+5Ob4GI
mz7opIMoNxbjZ8DMGogjzGwH6xSBYOHA/U4BiCmhAGLoGVXaxWES+HoNruS+AiRx
weCHeV8tKc8/74TKnBUZThw3yc+Fjlvuf8+DhNA1M+G+NOCwCBDkckeIA+VHdNtq
ofAvhqFTC1l46VmsCNc4Cq8XJQKBgQDAWx3cVgoYuXPG2NGwb5CQuVSMHElea2JM
cNNA96LLEjsnztm8pERdIu8QSDgw3GCilweG66eytrSoechN9SRQuBYx33mNFBvb
v0vpDsx9C3TAjkW/5AvylKUBCIqzeBTuH95RXp7sWvsdJDOIZFmnKkGNKfTafPAL
+Ec5vQj6sQKBgQDcJ+XGtFT8jrDbhN2+eAjoO98qFngCOQA/t275Y8TzdxxGPihq
wsSgj86H65B4koVMvv0YJygwe7PSop8LjRz/c8t4RwQ/lZsffud2wmiwZx2+aEZg
DHWhOQTwQJ6yyJmVnwSdY0eQ/2xWI6A3BHrOiU/+fRB1PflEiYzx4n4SXQKBgCFh
bownDjd+L15JkBILOk4zKz3pRr4w6m0Tg0WZ89FDx6o/1j9LTmXPQydTMRUhmU99
4BuE16RG2pEGGUGWEghD+e4Ltv9JhxAaYWT/YXMtwsQLrIUBYSVmsD++qLs+UnuE
YkNCpVek7kD/YEYCDCDbT2bc6hXkao/ZNRsK9/zxAoGBAJLf2Ib+xuHLO9OQHG1R
2gBMV/OdX62sjtdCyVfe4YM+q2GmGxjiAwOqx1vH7pccAMNB0lCpspcZXqeujC47
hmZoNZWwW3qU3ye21oMRn+eWV43x3ldNeh7D2S8vAcC8ggZz8yDfugl3wl3R3S1/
bBavQFwAoGqxxYGqi/8Qf+Dt
-----END PRIVATE KEY-----
""",
            "alipay_pid": "2088111111111111",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "usrakrbci3nfa5x1pracb52xcs9lh8gu",
            "alipay_sign_type": "rsa2",
            "alipay_version": 2,
            "fee_rate": 80
        }
    }
    channel = pingpp.SubApp.create_channel('app_eyj5qX1ndWLdmXxH', **params)
    print('create sub_app channel:', channel)

    # 更新子商户渠道参数
    updateParams = {
        'description': 'Your Channel description',
        "params": {
            "alipay_account": "example2@example.com",
            "alipay_app_id": "2016666666666668",
            "alipay_app_public_key": None,
            "alipay_app_public_key_rsa2": """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg3sPgpSdkpuy97Tfq3zA
BUaiN6Egkx21Wf2gHV6c/vIpxHfJDXcKJgnaOmJpWBwsrRGiqC89T0efT2Z7RO9c
D5BP8n3O8ok9xkxRhT/ptXjC8Ly5TmOha/p09qzhM0nczVEhBtisR7uAubl+RwKD
/x4K/PEX4TRdjvxKHJhIBC0wJYWPANhPJJoCi9Mua6wP4kmUbrVXcs7V4pLA3yke
DC+gg9vsdD8NYiJ7AQu169LxLanSF1r9pUkZIiOuRwwjwE/TwaKYAE22eLmBG70J
TukYulv5BK2qLlZtNM1NQQTc2CdJBmF3r080x6UACddzRs0UkhinijlESpt+bHFj
gwIDAQAB
-----END PUBLIC KEY-----
""",
            "alipay_mer_app_private_key": None,
            "alipay_mer_app_private_key_rsa2": """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC3CN8dCG9bpWSR
HMypeUAl9CspbovXJVVmqmkhMnalb+07t6bJB35KgYRnoi3iyArZDQiiSADIhWb8
63zOPaiyg8SQCqwNRwqOedMPDNz/wyrmGncECvv4Oyp2PoW/1t6TPljfwZIJO5f0
KZnVqsMqkr0F71eQ00FEZKR/xT+QkoJ74/BGmqs73NIe4wxg9QxLJJLFLsZxA9bW
7qNAsiLIu9nPG7+8Heewqlrva3SmFXBVuZ48TeRH0HetKam3Vvl72KkylEb8s1iu
09NUMBiFf77rA43hiUhDHKIYL2Gsf0MZKQksOcln5WCJWouQKH5Qk2iR5JDE6aEs
i/pp0SKVAgMBAAECggEAObM+QrTKBiYZkfV2P2bN5ikXAjSrOOO4DGlkQubZqEWk
j9LRbUZDddFmoBTsSjWt1cbaFe6E8LG9SbYi3hFqAPyxFoeGvZjLpyaYdoIjmS05
dNia9FdSH2rnc+c52sQt3lUlR0SKeQakXIBQ0p7Gb8FafWh6Plmalaj0gqL36ub7
dOhKXvXMtPaEWU913A50RwKYjWABRpP26XQ9mqURHpu4qEV8EUozo+HLjZ7ZiLwl
9Jqpt/ISTdn2PYNqcTdy7zRlyKbWiMJwHQZxAcMrlf7pkoYgIkqNmjwBMII/jlsh
+Dm2e2/FutYrZhEuwSfDx/+qvSVPq2jV5K7fB9rHAQKBgQDzmDod9gPDl+5Ob4GI
mz7opIMoNxbjZ8DMGogjzGwH6xSBYOHA/U4BiCmhAGLoGVXaxWES+HoNruS+AiRx
weCHeV8tKc8/74TKnBUZThw3yc+Fjlvuf8+DhNA1M+G+NOCwCBDkckeIA+VHdNtq
ofAvhqFTC1l46VmsCNc4Cq8XJQKBgQDAWx3cVgoYuXPG2NGwb5CQuVSMHElea2JM
cNNA96LLEjsnztm8pERdIu8QSDgw3GCilweG66eytrSoechN9SRQuBYx33mNFBvb
v0vpDsx9C3TAjkW/5AvylKUBCIqzeBTuH95RXp7sWvsdJDOIZFmnKkGNKfTafPAL
+Ec5vQj6sQKBgQDcJ+XGtFT8jrDbhN2+eAjoO98qFngCOQA/t275Y8TzdxxGPihq
wsSgj86H65B4koVMvv0YJygwe7PSop8LjRz/c8t4RwQ/lZsffud2wmiwZx2+aEZg
DHWhOQTwQJ6yyJmVnwSdY0eQ/2xWI6A3BHrOiU/+fRB1PflEiYzx4n4SXQKBgCFh
bownDjd+L15JkBILOk4zKz3pRr4w6m0Tg0WZ89FDx6o/1j9LTmXPQydTMRUhmU99
4BuE16RG2pEGGUGWEghD+e4Ltv9JhxAaYWT/YXMtwsQLrIUBYSVmsD++qLs+UnuE
YkNCpVek7kD/YEYCDCDbT2bc6hXkao/ZNRsK9/zxAoGBAJLf2Ib+xuHLO9OQHG1R
2gBMV/OdX62sjtdCyVfe4YM+q2GmGxjiAwOqx1vH7pccAMNB0lCpspcZXqeujC47
hmZoNZWwW3qU3ye21oMRn+eWV43x3ldNeh7D2S8vAcC8ggZz8yDfugl3wl3R3S1/
bBavQFwAoGqxxYGqi/8Qf+Dt
-----END PRIVATE KEY-----
""",
            "alipay_pid": "2088111111111112",
            "alipay_refund_nopwd": False,
            "alipay_security_key": "a5srakrbci3nf1pracb52xcs9xlhu8ga",
            "alipay_sign_type": "rsa2",
            "alipay_version": 2,
            "fee_rate": 80
        },
        'banned': False,
    }
    channel = pingpp.SubApp.update_channel('app_eyj5qX1ndWLdmXxH',
                                           'alipay',
                                           **updateParams)
    print('update sub_app channel:', channel)

    # 查询子商户渠道参数
    channel = pingpp.SubApp.retrieve_channel('app_eyj5qX1ndWLdmXxH', 'alipay')
    print('retrieve sub_app channel:', channel)

    # 删除子商户渠道参数
    deleted = pingpp.SubApp.delete_channel('app_eyj5qX1ndWLdmXxH', 'alipay')
    print('delete sub_app channel:', deleted)
except Exception as e:
    raise
