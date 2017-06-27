# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  使用报关接口参考文档：https://www.pingxx.com/api#api-customs
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp
import os

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->企业设置->开发设置-> Secret Key
api_key = 'sk_test_ibbTe5jLGCi5rzfH4OqPW9KC'
# app_id 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击你创建的应用->应用首页->应用 ID(App ID)
app_id = 'app_1Gqj58ynP0mHeX1q'
# 设置 API Key
pingpp.api_key = api_key

'''
  设置请求签名密钥，密钥对需要你自己用 openssl 工具生成，如何生成可以参考帮助中心：https://help.pingxx.com/article/123161；
  生成密钥后，需要在代码中设置请求签名的私钥(rsa_private_key.pem)；
  然后登录 [Dashboard](https://dashboard.pingxx.com)->点击右上角公司名称->企业设置->开发设置->商户公钥（用于商户身份验证）
  将你的公钥复制粘贴进去并且保存。
  注：报关接口，必须配置该值，不管是否启用，都需要验证签名。
'''
pingpp.private_key_path = os.path.join(
    os.path.dirname(os.getcwd()), 'your_rsa_private_key.pem')
'''
    Charges 支付Demo: https://www.pingxx.com/api#charges-支付
    创建charge对象-cmb_wallet
'''
print "创建charge对象:"
try:
    charge = pingpp.Charge.create(
        order_no='1234567890',  # 推荐使用 8-20 位，要求数字或字母，不允许其他字符
        amount=1000000,  # 订单总金额, 人民币单位：分（如订单总金额为 1 元，此处请填 100）
        app=dict(id=app_id),
        channel='cmb_wallet',  # https://www.pingxx.com/api#支付渠道属性值
        currency='cny',
        client_ip='127.0.0.1',  # 发起支付请求客户端的 IP 地址，格式为 IPV4，如: 127.0.0.1
        subject='Your Subject',
        body='Your Body',
        extra=dict(
            # 必须，交易完成跳转的地址。
            result_url='http://example.com/success',
            # 对于 p_no, seq , m_uid , mobile 这几个参数：
            # 1. 这几个参数是用户自定义的。
            # 2. 对于同一个终端用户每次请求 charge 务必使用同一套参数（确保每个参数都不变），
            # 任意参数变更都会导致用户重新签约，同一个用户和招行重新签约的次数有限制，超限制就会无法签约 ，导致用户无法使用。
            # 必须，客户协议号，不超过 30 位的纯数字字符串。
            p_no='1234567890',
            # 必须，协议开通请求流水号，不超过 20 位的纯数字字符串，请保证系统内唯一。
            seq='1234567890234567888',
            # 必须，协议用户 ID，不超过 20 位的纯数字字符串。
            m_uid='8888888888',
            # 必须，协议手机号，11 位数字。
            mobile='13088888888'
        )
    )
    print(charge)
except Exception as e:
    print(e.http_body)
