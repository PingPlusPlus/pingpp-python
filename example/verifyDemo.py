# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64
import os


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

data = open(os.path.join(os.path.dirname(__file__), 'message.json')).read()
sign = "\
PcU0SMJhbPObiIVinNnalZOjI02koWozxLrxa3WQW3rK/n7I+EuVGuXvhsq2MIf\
UaNiHZDgRFYybGtKr1uuFzEXjA4PwmnDHfWgwRPdjgseoU0eke6ZqGpklBRVTbF\
6PUy6/vAqur4xb7h1wpdrteUpCPafzDmVPsQLicdojJ/TF9ACjQW8gTNiS6tE9g\
L5hxy0RJ3/okRJo6dz2pvJBWkjCrgp/r98z/LQijA1o//atZrH63+DcL/GwEOga\
ymqbodzusXF+g6WMJ/GTJgjdPRHvpO9UAAUKkOQqvwthJvsXIH/L1xqvy+tFpo2\
J0Ptwg85bowKoyy1qC5ak3sqWqw==\
"
if verify(data, sign):
    print("Signature verification succeeded")
else:
    print("Signature verification failed")
