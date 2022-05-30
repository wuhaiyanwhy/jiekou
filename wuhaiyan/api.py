# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---

import requests
import json
import logging

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)-[%(levelname)s]%(message)s')

def user_logging():
    url = 'http://uat.drp.orsd.tech/drpapi/oauth/loginOauth'
    data = json.dumps({
        "username": "wuhaiyan",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    })
    header = {"Content-Type":"application/json;charset=UTF-8"}
    res = requests.post(url= url,data= data,headers = header).json()
    accesstoken = res.get('data')['accessToken']
    return accesstoken

def search_order():
    url = 'http://uat.drp.orsd.tech/drpapi/orderManage/new/searchOrder?startTime=&endTime=&salesOrderNumber=why_0520_1&omdOrderNumber=&trackingNumber=&orderDate=&orderStatus=&itemCode=&storeId=888&ebayUserId=&billZipCode=&billName=&billPhone=&shipZipCode=&shipName=&shipPhone=&orderStarred=&flagOrder=&backOrdered=&radio=&orderNumber=876744'
    header = {
        "Content-type": "application/json;charset=UTF-8",
        "Authorization": 'Bearer ' + str(user_logging())
    }
    res = requests.get(url,params=None,headers= header).json()
    orderid = res.get('data')['salesOrderNumber']
    print(type(res))
    return res

def search_order2():
    url = 'http://uat.drp.orsd.tech/drpapi/orderManage/new/searchOrder?startTime=&endTime=&salesOrderNumber=why_0520_2&omdOrderNumber=&trackingNumber=&orderDate=&orderStatus=&itemCode=&storeId=888&ebayUserId=&billZipCode=&billName=&billPhone=&shipZipCode=&shipName=&shipPhone=&orderStarred=&flagOrder=&backOrdered=&radio=&orderNumber=876743'
    header = {
        "Content-type": "application/json;charset=UTF-8",
        "Authorization": 'Bearer ' + str(user_logging())
    }
    res = requests.get(url,params=None,headers= header).json()
    orderid = res.get('data')['salesOrderNumber']
    return res


