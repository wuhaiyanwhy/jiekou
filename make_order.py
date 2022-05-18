# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import pymssql
import time
import random
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)[%(thread)d]-[%(levelname)s]%(message)s')

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
        sql = "select  * from tblOrderDetails where OrderNumber in ('875273')"
        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()
            for i in results:
                print(i)
        except Exception as e:
            raise e
        # finally:
        #     self.cur2.close()

    def insert_tblYzcOrders_888(self):
        cur_date = time.strftime('%m%d', time.localtime(time.time()))
        start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        for i in range(1,3001):
            OrderID = ('why'+'_'+cur_date+'_'+str(i))
            StoreID = '888'
            CreateDate = start
            sql = "INSERT INTO  tblYzcOrders(OrderID, OrdersFrom, StoreName, OrderDate, ShipName, ShipCompany, \
                                                                    ShipAddress1, ShipAddress2, ShipCity, ShipState, ShipZipCode, \
                                                                    ShipCountryCode, ShipPhone, ShipServiceLevel, ShipMethod, DiscountAmount, \
                                                                    TaxAmount, ShipAmount, OrderTotal, CustomerComments, LineItemNumber, SKU, \
                                                                    SellerSKU, AltItemID, Description, Qty, ItemUnitPrice, ItemUnitDiscount, \
                                                                    ItemUnitWeight, StoreID, OrderNumber, IsExported, ItemShipAmount, ItemTax, \
                                                                    BillEmail, RunId, SourceId, Memo, CreateDate, CreateBy, UpdateDate, UpdateBy, \
                                                                    ImageId, ParentSKU, sourceLine, sellerId, url, trackingNumber, OMDComboCode, \
                                                                    BolUrl, Warehouse, CutType, IsLtl, buyerId, ImportCheckStatus, s2sUrl, isS2S, \
                                                                    carrier, labelType, isNeedBuyLabel, billAddress1, billAddress2, billAddress3, \
                                                                    billCity, billState, billPhone, billName, billZipCode, salesChanel, \
                                                                    payAccountNumber, sourceItemNumber, sourceStoreId, re_order_flag, \
                                                                    sales_order_id, combo_info, ebay_item_id, ebay_transaction_id, \
                                                                    origin_store_id, seller_code, return_to_address) \
            VALUES('%s', N'', N'yzc', N'2022-04-12 01:28:30.727', N'test', null, N'219 Roof Garden Way', N'', \
            N'Somerset', N'PA', N'155011678', N'US', N'8144431230', null, N'', 0, 0, 0, 1, null, 1, N'W20601008', null, \
            null, N'product name', 1, 1, 0, 0, %s, 0, 0, 0, 0, N'test@qq.com', N'1649752095950', N'3181795', null, \
            N'2022-04-12 11:32:23.000', 1, N'2022-04-12 01:28:30.727', 1, null, null, 1, N'33', null, null, null, null, \
            null, null, null, 33, null, null, null, null, null, null, null, null, null, null, null, null, null, null, N'', \
            null, null, null, 0, null, null, null, null, null, N'W206', null);"%(OrderID,StoreID)
            # sqlw = "select  * from tblOrderDetails where OrderNumber in ('875273')"

            self.cur2.execute(sql)
            logging.info(OrderID)
            self.db2.commit()

    def insert_tblYzcOrders_212(self):
        cur_date = time.strftime('%m%d', time.localtime(time.time()))
        start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        for i in range(2, 5):
            OrderID = ('why' + '_' + cur_date + '_' + str(i))
            StoreID = 212
            sql = "INSERT INTO Yahoo_Integration.dbo.tblYzcOrders( OrderID, OrdersFrom, StoreName, OrderDate, ShipName, ShipCompany, \
                                               ShipAddress1, ShipAddress2, ShipCity, ShipState, ShipZipCode, \
                                               ShipCountryCode, ShipPhone, ShipServiceLevel, ShipMethod, \
                                               DiscountAmount, TaxAmount, ShipAmount, OrderTotal, CustomerComments, \
                                               LineItemNumber, SKU, SellerSKU, AltItemID, Description, Qty, \
                                               ItemUnitPrice, ItemUnitDiscount, ItemUnitWeight, StoreID, \
                                               OrderNumber, IsExported, ItemShipAmount, ItemTax, BillEmail, RunId, \
                                               SourceId, Memo, CreateDate, CreateBy, UpdateDate, UpdateBy, ImageId, \
                                               ParentSKU, sourceLine, sellerId, url, trackingNumber, OMDComboCode, \
                                               BolUrl, Warehouse, CutType, IsLtl, buyerId, ImportCheckStatus, \
                                               s2sUrl, isS2S, carrier, labelType, isNeedBuyLabel, billAddress1, \
                                               billAddress2, billAddress3, billCity, billState, billPhone, billName, \
                                               billZipCode, salesChanel, payAccountNumber, sourceItemNumber, \
                                               sourceStoreId, re_order_flag, sales_order_id, combo_info, \
                                               ebay_item_id, ebay_transaction_id, origin_store_id, seller_code, \
                                               return_to_address) \
            VALUES( N'%s', N'AmazonDropShip', N'yzc', N'Tuesday,March 22 2022 02:04 AM',  \
            N'xiaou', null, N'457 Joy Dr.', N'', N'Mc Caysville', N'GA1', N'20210419', N'US', N'15478536657', \
            N'UPS GROUND', N'SMALL PARCEL', 0, 0, 0, 1, N'US Dropship Order', 1, N'W22502246', null, null, N'item_title', 1, 1, 0, 0, %s, 0, 0, 0, 0,  \
            N'3124824650@QQ.com', N'1647940202333', N'3180197', null, N'2022-03-22 02:10:31.403', 1, N'2022-03-22 02:10:31.403', 1,  \
            '1', null, 1, N'85', N'https://b2bfiles1.gigab2b.cn/storage/dropshipPdf/2022-03-22/splitPdf/20220322020116_kzxRzOZ1Sk1DBw0ckWgH.pdf',  \
            N'1Z18Y4900392113041', null, null, N'', 1, 0, 197, null, N'', 0, \
            N'UPS', null, null, null, null, null, null, null, null, null, null, null, null, null, null, 0, null, null, null, null, null, N'W225', null);" %(OrderID,StoreID)

            self.cur2.execute(sql)
            logging.info(OrderID)
            self.db2.commit()

        # sql_select = 'select  * from tblYzcOrders where OrderID in (OrderID)'
            # self.cur.execute(sql)
            # results = self.cur.fetchall()
            # print(results)
            # self.cur.close()

if __name__ == '__main__':
    a = MakeOrder()
    a.insert_tblYzcOrders_888()



