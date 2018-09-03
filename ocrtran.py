#!/home/innersea/python/venv/bin/python
##!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# Author : InnerSea
# E-mail : innersea@163.com
#
# 参考文献：
# https://www.jb51.net/article/64791.htm
# http://ai.baidu.com/docs#/OCR-API/e1bd77f3
# https://www.cnblogs.com/smallfoxdog/p/8630974.html
# http://api.fanyi.baidu.com/api/trans/product/apidoc
# http://www.opython.com/868.html

import random
from urllib.parse import quote
from hashlib import md5
import os
import requests
from aip import AipOcr


# 百度ocr的 APPID AK SK
APP_ID = '11712843'
API_KEY = 'WvR2zE44UsWj3IqePedYpNhf'
SECRET_KEY = 'cT8RTTFhqLwKmffiM0ajNqCEqcM4YcBs'

# 百度翻译的 ID KEY
appid_tran = '20180822000197644'
secret_key_tran = '_sczJgqQEq7uvBQvv_c8'

# 临时截图路径
IMG_PATH = '/tmp/tmpscrot.png'


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 生成调用百度翻译API的签名
def get_sign(salt, qurey):
    sign = appid_tran + qurey + str(salt) + secret_key_tran
    m = md5()
    m.update(sign.encode('utf-8'))
    return m.hexdigest()


# 百度网页翻译，适用于单词
def baidu_translate(qurey):
    url = "http://fanyi.baidu.com/extendtrans"  # 请求的地址
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"
    }  # 设置请求的头部

    # 设置提交的数据
    posData = {"query": qurey,
               "from": "auto",
               "to": "zh"}

    response = requests.post(url=url, data=posData, headers=headers)  # 模拟请求

    return response.json()["data"]["st_tag"]


# 百度API翻译，适用于短语
def baidu_translate_api(qurey):  # 实现翻译功能
    from_lang = 'auto'
    to_lang = 'zh'
    salt = random.randint(12345, 67890)
    sign = get_sign(salt, qurey)
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate' + '?appid=' + appid_tran + '&q=' + quote(qurey) + \
            '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign

    response = requests.get(myurl)

    return response.json()['trans_result'][0]['dst']


if __name__ == "__main__":
#    while True:  # 容易陷入死循环，慎用！
        try:
            # 屏幕截图
            os.system("scrot -s {0}".format(IMG_PATH))

            # 调用百度通用文字识别API, 图片参数为本地图片
            client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
            image = get_file_content(IMG_PATH)
            origin = client.basicGeneral(image)['words_result'][0]['words']


            # 百度翻译
            result1 = baidu_translate(origin)  # type: list
            result2 = baidu_translate_api(origin)  # type: str

            # 发送桌面通知（KDE）
            if len(result1) != 0:
                os.system("kdialog --title '{0}' --passivepopup '{1}'".format(origin, str(result1)))
            else:
                os.system("kdialog --title '{0}' --passivepopup '{1}'".format(origin, str(result2)))

        except Exception as e:
            os.system("kdialog --title '取词错误' --passivepopup '请重新取词。\n{0}'".format(str(e)))
        else:
            exit()

