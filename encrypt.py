import os
from Crypto.Cipher import AES
import base64
import codecs


def aes_encrypt(text, seckey):
    pad = 16 - len(text) % 16
    if isinstance(text, bytes):
        print("type(text)=='bytes'")
        text = text.decode('utf-8')
    # print(type(text))
    text = text + str(pad * chr(pad))
    encryptor = AES.new(seckey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return str(ciphertext, 'utf-8')


def rsa_encrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'


def create_secretkey(size):
    return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]
