# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import ddt
import json
import unittest
from Logs.Logger_func import Logger
from Base.Base_request import request
from Utils.Data_structure import get_case_data
from PublicConfig.Useragent_config import useragent
from Utils.operation_header import OperationHeader
from Utils.operation_json import OperationJson
from Data.depend_data import OpentionData
from Utils.operation_dependdata import OpentionDependdata
logger = Logger(logger='test_case01').getlog()
data = get_case_data()


@ddt.ddt
class TestCase01(unittest.TestCase):
    @ddt.data(*data)
    def test_case(self, data):
        logger.info("""
                         _    _         _      _____         _
          __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
         / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
        | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
         \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
              |_|
              Starting      ...     ...     ...
            """)
        logger.info('用例序号:{}'.format(data[0]))
        logger.info('用例名称:{}'.format(data[1]))
        logger.info('请求url:{}'.format(data[2]))
        logger.info('请求数据:{}'.format(data[3]))
        logger.info('请求方式:{}'.format(data[4]))
        logger.info('请求头:{}'.format(data[5]))
        logger.info('依赖:{}'.format(data[6]))
        logger.info('依赖的返回数据:{}'.format(data[7]))
        logger.info('数据依赖字段:{}'.format(data[8]))
        logger.info('预期结果:{}'.format(data[9]))

        if data[5] == "header":
            res = request.run(data[4],url=data[2], data=data[3], headers=useragent)
            print(type(res))
            op_header = OperationHeader(res)
            op_header.write_token()
            if data[7] != None:
                op = OpentionData()
                op.write_data(res)

        elif data[5] == "yes":
            op_json = OperationJson('D:\daima\interface2\PublicConfig/token.json')
            token = op_json.get_data('Authorization')
            header = {
                "Content-type": "application/json;charset=UTF-8",
                "Authorization": 'Bearer ' + eval(token)
            }
            if data[7] == None :
                res = request.run(data[4], url=data[2], data=data[3], headers=header)

            elif data[7] != None and data[6] != None:
                op_dependata = OpentionDependdata('res','D:\daima\interface2\PublicConfig/depend.json')
                op_dependata.read_dependdata('D:\daima\interface2\PublicConfig/depend.json')
                depend_response_data = op_dependata.get_dependdata(data[7], aaaaa=data[7])
                depend_field = data[8]
                request_data2 = {depend_field: eval(depend_response_data)}  # 请求数据=依赖的返回数据
                request_data = json.dumps(request_data2)
                res = request.run(data[4],url = data[2], data=request_data, headers=header)

        else:
            op_json = OperationJson('D:\daima\interface2\PublicConfig/token.json')
            token = op_json.get_data('Authorization')
            header = {
                "Content-type": "application/json;charset=UTF-8",
                "Authorization": 'Bearer ' + eval(token)
            }
            result = request.run(url=data[2], data=data, headers=header)
            res = json.dumps(result)

        logger.info('返回结果为:{}'.format(res))
        # logger.info('返回状态码为:{}'.format(response.json.loads().status_code))
        self.assertEqual(json.loads(res)[data[9]], "0000", msg='预期和返回不一致')
        # HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 11, "pass")

        # try:
        #     # self.assertEqual(200, response.status_code)
        #     self.assertTrue(json_diff(data[0], response.json()))
        #     HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 11, 'Pass')
        # except AssertionError as e:
        #     logger.error(e)
        #     HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 11, 'Failed')
        # self.assertEqual(200, response.status_code)
        # self.assertTrue(json_diff(data[0], response.json()))


if __name__ == '__main__':
    unittest.main()
