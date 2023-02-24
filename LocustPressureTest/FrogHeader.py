# -*- coding: UTF-8 -*-
'''
@Project ：FrogApiAutoTest 
@File    ：FrogHeader.py
@IDE     ：PyCharm 
@Author  ：luxiaosan
@Date    ：2021/11/16 9:06 下午 
'''
# from config.FrogConf import frog
import time
import hashlib


class FrogHeader:

    @staticmethod
    def get_header():
        key = "846d2cb0c7f09c3ae582c421696d308c"
        timestamp = str(int(round(time.time() * 1000)))
        # timestamp = "1636961923178"
        id = timestamp

        # md5加密
        m = hashlib.md5()
        union_str = id + ":" + key + ":" + timestamp
        m.update(union_str.encode(encoding="utf-8"))
        str_md5 = m.hexdigest()
        # print(str_md5)
        header = {
            "caller": "app",
            "ex": """{"CurrentLanguage":"en","CurrentCountry":"CN","VersionNumber":"15.0.2","AppName":"Frog","AppBuild":"20211206001","PhoneVersion":"iPhone9,1"}""",
            "os": "15.0.2",
            "platform": "iOS",
            "ver": "1.8.50",
            "encrypt": "md5",
            "etag": "qqq",  # 不为空，任意值，与其他接口请求头一致
            "id": id,  # 任意数字
            "sign": str_md5,  # id+key+timestamp加密处理
            "timestamp": timestamp,
            "language": "en",
            "content-type": "application/json"
        }
        return header
