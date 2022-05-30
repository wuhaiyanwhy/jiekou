# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import pymssql
import time
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)-[%(levelname)s]%(message)s')
class MakeOrder():

    def __init__(self):

        # T1
        self.db1 = pymssql.connect(
            host="192.168.20.242",
            user="wostest",
            password="wos@123",
            port=1433,
            database="Yahoo_Integration",
            charset="utf8",
        )
        self.cur1 = self.db1.cursor()

        # T2数
        self.db2 = pymssql.connect(
            host="192.168.20.69",
            user="wostest",
            password="wos@123",
            port=1433,
            database="Yahoo_Integration",
            charset="utf8",
        )
        self.cur2 = self.db2.cursor()



    def select(self):
        # p = search_order()[0]
        # p = 'why_0520_1'
        sql = "select  * from tblorders where PayPalTxID = 'why_0520_1'"
        try:
            self.cur2.execute(sql)
            results = self.cur2.fetchall()
            for i in results:
                print(i)
        except Exception as e:
            raise e
        # finally:
        #     self.cur2.close()

if __name__ == '__main__':
    a = MakeOrder()
    a.select()



