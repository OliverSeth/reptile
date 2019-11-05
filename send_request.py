import requests
import json

from encrypt import *
from write_in_database import write_comments


def get_comments(pages):
    offset = int(pages) / 10
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1344340338?csrf_token='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/78.0.3904.87 Safari/537.36'}
    comments = []
    for i in range(int(offset)):
        text = {'username': '', 'password': '', 'rememberLogin': 'true', 'offset': i * 10}
        text = json.dumps(text)
        seckey = create_secretkey(16)
        encText = aes_encrypt(aes_encrypt(text, nonce), seckey)
        encseckey = rsa_encrypt(seckey, pubKey, modulus)
        payload = {'params': encText, 'encSecKey': encseckey}
        res = requests.post(url=url, data=payload, headers=headers)
        dic = json.loads(res.text)
        # print(type(dic['comments']))
        comment = dic['comments']
        comments = comments+comment
    return comments


page = input('请输入评论数:')
comments = get_comments(page)
write_comments(comments)
# print('共有' + str(len(comments)) + '条评论')
# for com in comments:
#     print('用户:' + com['user']['nickname'], '评论:' + com['content'])
