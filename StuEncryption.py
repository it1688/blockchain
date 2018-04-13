"""
椭圆曲线加密
"""
import base58
import ecdsa
import binascii
import hashlib
import random


# 生成秘钥
def create_private_key():
    digits = ['%x' % random.randrange(16) for _ in range(64)]
    return ''.join(digits)


# 生成公钥
def create_publice_key(priv_key):
    buff = bytes.fromhex(priv_key)
    print(type(buff))
    print(buff)
    sk = ecdsa.SigningKey.from_string(buff, curve - ecdsa.SECP256k1)
    pub_key = b'\x04'


print(create_private_key())
