# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='*missing_padding
    return base64.decodestring(data)


def verify(sig):
    signs = decode_base64(sig)
    datas = open('message.json').read()
    data = datas.encode('utf-8')
    pubkey = RSA.importKey(open('my-server.pub').read())
    digest = SHA256.new(data)
    pkcs = PKCS1_v1_5.new(pubkey)
    return pkcs.verify(digest, signs)

datas = open('message.json').read()
sign="PcU0SMJhbPObiIVinNnalZOjI02koWozxLrxa3WQW3rK/n7I+EuVGuXvhsq2MIfUaNiHZDgRFYybGtKr1uuFzEXjA4PwmnDHfWgwRPdjgseoU0eke6ZqGpklBRVTbF6PUy6/vAqur4xb7h1wpdrteUpCPafzDmVPsQLicdojJ/TF9ACjQW8gTNiS6tE9gL5hxy0RJ3/okRJo6dz2pvJBWkjCrgp/r98z/LQijA1o//atZrH63+DcL/GwEOgaymqbodzusXF+g6WMJ/GTJgjdPRHvpO9UAAUKkOQqvwthJvsXIH/L1xqvy+tFpo2J0Ptwg85bowKoyy1qC5ak3sqWqw=="
print verify(sign)





