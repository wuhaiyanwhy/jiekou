import json
class OpentionData:
    def __init__(self):
        self.file_path = 'D:\daima\interface2\PublicConfig/depend.json'
    # 写json
    def write_data(self,response):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(response))

if __name__ == '__main__':
    op_dependata =  OpentionData()
    op_dependata.write_data(response)
