# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---

import random



class UserAgent:
    def get_headers(self):
        """随机生成请求头中的User-Agent以应对服务判断"""
        headers = {"Content-Type":"application/json;charset=UTF-8"}
        return headers


useragent = UserAgent().get_headers()

if __name__ == '__main__':
    print(get_headers())
