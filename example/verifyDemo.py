# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入 webhooks 流程参考开发者中心：https://www.pingxx.com/docs/webhooks/webhooks
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
import os

'''
  验证 webhooks 签名方法：
  data：Ping++ 请求 body 的原始数据即 event ，不能格式化；
  sig：Ping++ 请求 header 中的 x-pingplusplus-signature 对应的 value 值；
  pub_key_path：读取你保存的 Ping++ 公钥的路径；
  pingpp_public_key.pem：Ping++ 公钥，获取路径：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Ping++ 公钥
'''


def decode_base64(data):
    remainder = len(data) % 4
    if remainder:
        data += '=' * (4 - remainder)
    return base64.decodestring(data.encode('utf-8'))


def verify(data, sig):
    signs = decode_base64(sig)
    data = data.decode('utf-8') if hasattr(data, "decode") else data
    pubkeystr = open(os.path.join(os.path.dirname(__file__),
                     'pingpp_public_key.pem')).read()
    pubkey = RSA.importKey(pubkeystr)
    digest = SHA256.new(data.encode('utf-8'))
    pkcs = PKCS1_v1_5.new(pubkey)
    return pkcs.verify(digest, signs)

# 示例
data = open(os.path.join(os.path.dirname(__file__), 'message.json')).read()
sign = "\
PcU0SMJhbPObiIVinNnalZOjI02koWozxLrxa3WQW3rK/n7I+EuVGuXvhsq2MIf\
UaNiHZDgRFYybGtKr1uuFzEXjA4PwmnDHfWgwRPdjgseoU0eke6ZqGpklBRVTbF\
6PUy6/vAqur4xb7h1wpdrteUpCPafzDmVPsQLicdojJ/TF9ACjQW8gTNiS6tE9g\
L5hxy0RJ3/okRJo6dz2pvJBWkjCrgp/r98z/LQijA1o//atZrH63+DcL/GwEOga\
ymqbodzusXF+g6WMJ/GTJgjdPRHvpO9UAAUKkOQqvwthJvsXIH/L1xqvy+tFpo2\
J0Ptwg85bowKoyy1qC5ak3sqWqw==\
"
# 验证
if verify(data, sign):
    print("Signature verification succeeded")
else:
    print("Signature verification failed")
