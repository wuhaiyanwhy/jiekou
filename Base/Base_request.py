# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import requests
import json
class BaseRequest:

    def send_post(self,url,data=None,header=None):
        # res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

    def send_get(self,url,data=None, headerValue=None, header=None):
        # res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=headerValue).json()
        else:
            res = requests.get(url=url,data=data).json()
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

    def run(self,method,url,data=None,headers=None):
        # res = None
        if method == 'GET':
            res = self.send_get(url, data, headers)
        elif method == 'POST':
            res = self.send_post(url, data, headers)
        else:
            res = self.send_put(url, data, headers)
        return res
request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
