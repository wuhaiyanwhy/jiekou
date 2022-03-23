# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import json
from Utils.operation_json import OperationJson
'''
写入header 中的 token，在token.json文件中
'''
class OperationHeader:
    def __init__(self,res):
        self.res = json.loads(res)

    def get_response_token(self):
        '''
        获取登录返回的accessToken
        '''
        token1 = self.res['data']['accessToken']

        # token1 = self.json.loads['data']['accessToken']
        token = {
            "Authorization":token1
        }
        # token1 = json.loads(json_data)["orderList"]

        return token
    def write_token(self):
        token = self.get_response_token()
        op_json = OperationJson()
        op_json.write_data(token)

if __name__ == '__main__':
    op_header = OperationHeader(res)
    op_header.write_token(res)
