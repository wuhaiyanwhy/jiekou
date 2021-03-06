# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---

from Utils.Config_parser import config
from Utils.Excel_handle import HandleExcel


def get_case_data():
    """构造请求数据"""
    data = HandleExcel().get_all_data()
    # url = config.config_parse('server')
    data_list = []
    case_numbers = len(data)
    for index in range(case_numbers):
        case = []
        if data[index][3] == 'yes':
            case.append(data[index][0])
            case.append(data[index][1])
            case.append(data[index][2])
            case.append(data[index][4])
            case.append(data[index][5])
            case.append(data[index][6])
            case.append(data[index][7])
            case.append(data[index][8])
            case.append(data[index][9])
            case.append(data[index][10])
            case.append(data[index][11])
            case.append(data[index][12])
            data_list.append(case)
    print(data_list)
    return data_list