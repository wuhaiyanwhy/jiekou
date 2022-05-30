# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---

from wuhaiyan.api import *
dict1 = search_order()
dict2 = search_order2()

def cmp(order1, order2):
    if isinstance(order1, dict):
        """若为dict格式"""
        for key in order1:
            if key not in order2:
                print("order2不存在这个key",key)
        for key in order1:
            if key in order2:
                """递归"""
                cmp(order1[key], order2[key])
            else:
                print("order2不存在这个key",key)


    elif isinstance(order1, list):
        """若为list格式"""
        if len(order1) != len(order2):
            print("list len: '{}' != '{}'".format(len(order1), len(order2)))
        for src_list, dst_list in zip(sorted(order1), sorted(order2)):
            """递归"""
            cmp(src_list, dst_list)
    else:
        if str(order1) != str(order2):
            print(order1)


cmp(dict1,dict2)






