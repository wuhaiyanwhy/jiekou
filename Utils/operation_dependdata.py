# -*-coding:utf-8 -*-
# @Author: why
# Created on: ---
import json
class OpentionDependdata:
    def __init__(self,res,file_path):
        # self.data = GetData()
        self.file_path = 'D:\daima\interface2\PublicConfig/depend.json'
        self.dataaaa = self.read_dependdata(file_path)

    # 读取json文件
    def read_dependdata(self,file_path):
        with open(self.file_path) as fp:
            dataaaa = json.load(fp)
            data1 = json.loads(dataaaa)
            return data1
    #根据关键字读取1json文件数据
    def get_dependdata(self,file_path,aaaaa):
        a = self.read_dependdata(file_path)
        dataq = a["data"][(aaaaa)]
        if dataq == '':
            return None
        else:
            json1 = json.dumps(dataq)
            return json1
    #取返回结果里的具体需要的字段值
    # def ddata(self,i,res):
    #     depend_key = self.data.get_depend_key(i)  # 依赖的返回数据
    #     res2 = json.loads(res)
    #     if res2 == '':
    #         return None
    #     else:
    #         json_exe = res2["data"][(depend_key)]
    #         print(json_exe)
    #         return json_exe

if __name__ == '__main__':
    op_dependata =  OpentionDependdata(res)
    op_dependata.write_data(res)

