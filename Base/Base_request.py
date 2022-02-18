# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11
# coding:utf-8

import requests
import json
from PublicConfig.Useragent_config import useragent
from Utils.Cookie_handle import get_cookie_value, write_cookie
from Utils.operation_header import OperationHeader
from Utils.operation_json import OperationJson
from Data.depend_data import OpentionData
from Utils.operation_dependdata import OpentionDependdata
class BaseRequest:
    def send_post(self, url, data=None, header=None,key7=None,key6=None,key8=None):
        res = None
        if header == "header":
            result = requests.post(url=url, data=data, headers = useragent).json()
            res = json.dumps(result)
            op_header = OperationHeader(res)
            op_header.write_token()
            if key7 != None:
                op = OpentionData()
                op.write_data(res)

        elif header == "yes":
            op_json = OperationJson('D:\daima\Data-DrivenFramework-master\PublicConfig/token.json')
            token = op_json.get_data('Authorization')
            header = {
                "Content-type": "application/json;charset=UTF-8",
                "Authorization": 'Bearer ' + eval(token)
            }
            if key7 != None and key6 != None:
                op_dependata = OpentionDependdata(res, 'D:\daima\Data-DrivenFramework-master\PublicConfig/depend.json')
                op_dependata.read_dependdata('D:\daima\Data-DrivenFramework-master\PublicConfig/depend.json')
                depend_response_data = op_dependata.get_dependdata(key7, aaaaa=key7)
                depend_field = key8
                request_data2 = {depend_field: eval(depend_response_data)}  # 请求数据=依赖的返回数据
                request_data = json.dumps(request_data2)
                result = requests.post(url=url, data=request_data, headers=header).json()
                res = json.dumps(result)
            else:
                result = requests.post(url=url, data=data, headers=header).json()
                res = json.dumps(result)
        return res

    def send_get(self, url, data=None, header=None,key7=None,key6=None,key8=None):
        res = None
        if header == "yes":
            op_json = OperationJson('D:\daima\Data-DrivenFramework-master\PublicConfig/token.json')
            token = op_json.get_data('Authorization')
            header = {
                "Content-type": "application/json;charset=UTF-8",
                "Authorization": 'Bearer ' + eval(token)
            }
            if key7 != None and key6 != None:
                op_dependata = OpentionDependdata(res, 'D:\daima\Data-DrivenFramework-master\PublicConfig/depend.json')
                op_dependata.read_dependdata('D:\daima\Data-DrivenFramework-master\PublicConfig/depend.json')
                depend_response_data = op_dependata.get_dependdata(key7, aaaaa=key7)
                depend_field = key8
                request_data2 = {depend_field: eval(depend_response_data)}  # 请求数据=依赖的返回数据
                request_data = json.dumps(request_data2)
                result = requests.get(url=url, data=request_data, headers=header).json()
                res = json.dumps(result)
            else:
                result = requests.get(url=url, data=data, headers=useragent).json()
                res = json.dumps(result)
        return res

    def send_put(self, url, data, cookie_id):
        res = None
        if cookie_id == 0:
            res = requests.put(url=url, params=data, cookies=None, headers=useragent, verify=False)
        elif cookie_id == 1:
            cookie = get_cookie_value('cookie')
            res = requests.put(url=url, params=data, cookies=cookie, headers=useragent, verify=False)
        elif cookie_id == 2:
            res = requests.put(url=url, params=data, cookies=None, headers=useragent, verify=False)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            write_cookie(cookie, 'cookies')
        return res

    def run(self, method, url, data, cookie_id, key7,key6,key8):
        if method == 'GET':
            res = self.send_get(url, data, cookie_id)
        elif method == 'POST':
            res = self.send_post(url, data, cookie_id,key7,key6,key8)
        else:
            res = self.send_put(url, data, cookie_id)
        return res


request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    # response = request.run('GET','http://api.nnzhp.cn/api/user/stu_info', {'stu_name': 'b'}, 0)
    # res = request.run('GET','http://api.nnzhp.cn/api/user/stu_info', {'stu_name': 'b'}, 0).json()
    # print(res)
    # print(response.status_code)

# a = {'error_code': 0, 'stu_info': [{'id': 1043, 'name': 'B', 'sex': '?', 'age': 18, 'addr': '????', 'grade': '??', 'phone': '13197390530', 'gold': 100}]}
