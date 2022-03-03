# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import ddt
import json
import unittest
from Logs.Logger_func import Logger
from Base.Base_request import request
from Utils.Json_diff import json_diff
from Utils.Excel_handle import HandleExcel
from Utils.Data_structure import get_case_data

logger = Logger(logger='test_case01').getlog()
data = get_case_data()


@ddt.ddt
class TestCase01(unittest.TestCase):
    @ddt.data(*data)
    def test_case(self, data):
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

        response = request.run(data[4], data[2], data[3], data[5],data[7],data[6],data[8])
        logger.info('返回结果为:{}'.format(response))
        # logger.info('返回状态码为:{}'.format(response.json.loads().status_code))

        res = json.loads(response)
        print(res)
        # print(type(res))
        self.assertEqual(res[data[9]], "0000", msg='预期和返回不一致')
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
