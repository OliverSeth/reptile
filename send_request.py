import requests
import json

from encrypt import *

url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1344340338?csrf_token='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.87 Safari/537.36'}
text = {'username': '', 'password': '', 'rememberLogin': 'true', 'offset': 2}
text = json.dumps(text)
seckey = create_secretkey(16)
encText = aes_encrypt(aes_encrypt(text, nonce), seckey)
encseckey = rsa_encrypt(seckey, pubKey, modulus)
payload = {'params': encText, 'encSecKey': encseckey}
res = requests.post(url=url, data=payload, headers=headers)
dic = json.loads(res.text)
comment = dic['comments']
for com in comment:
    print(com)
