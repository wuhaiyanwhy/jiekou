#coding:utf-8
import json
# 简单的写法
# fp = open('D:\daima\ORSD\dataconfig\data.json')
# data = json.load(fp)
#
# print data['searchtest1']

class OperationJson():

    def __init__(self,file_path=None):
        self.file_path = 'D:\daima\Data-DrivenFramework-master\PublicConfig/token.json'
        # if file_path == None:
        #     self.file_path = 'D:\daima\Data-DrivenFramework-masterRSD\PublicConfig\search.json'
        # else:
        #     self.file_path = file_path
        self.data = self.read_data()
    #写json
    def write_data(self,token):
        with open(self.file_path,'w') as fp:
            fp.write(json.dumps(token))

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
            # data1 = self.data[id]
    # 根据关键字读取token json文件数据
    def get_data(self,id):
        data1 = self.data.get(id)
        if data1 == '':
            return None
        else:
            json1 = json.dumps(data1)
            return json1

if __name__ == '__main__':
    opjson = OperationJson('D:\daima\Data-DrivenFramework-master\PublicConfig/token.json')
    opjson.get_data("Authorization")

