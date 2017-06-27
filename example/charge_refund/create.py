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
    Charges 支付Demo: https://www.pingxx.com/api#创建-refund-对象
    创建Refund对象
'''
print "创建Refund对象:"
try:
    # 通过发起一次退款请求创建一个新的 refund 对象，只能对已经发生交易并且没有全额退款的 charge 对象发起退款
    ch = pingpp.Charge.retrieve("ch_Ti1eD0WP08eDPSSqnTOmLWHK")  # Charge 对象的 id
    # amount 为退款的金额, 单位为对应币种的最小货币单位，例如：人民币为分（如退款金额为 1 元，此处请填 100）。必须小于等于可退款金额，默认为全额退款
    re = ch.refunds.create(description='Your Descripton', amount=1)
    print(re)  # 输出 Ping++ 返回的退款对象 Refund
except Exception as e:
    print e.http_body
