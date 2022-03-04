#README
```
基于Python+requests的数据驱动接口自动化测试框架

确定整体设计思路：
优势1：实现数据分离
在python进行接口自动化测试时，为了方便管理和存储测试用例数据，一般 将测试数据编写存储在excel文件中，测试脚本通过读取excel文件来实现测试数据加载，并运行得出测试用例数据执行的结果，并回写测试结果到excel文件中，这样就实现了测试脚本和数据的分离。
优势2：维护性强，可实现定制化
缺点：基于代码维护，不依靠测试工具


1.环境准备：
python3.7
requests
ddt
openpyxl
HTMLTestRunner_api

2.目前实现的功能：
封装requests请求方法
在excel填写接口请求参数
用unittest+ddt数据驱动模式执行
HTMLTestRunner生成可视化的html报告
token关联
数据依赖
logging日志文件

3.模块介绍

Base

--Base-request.py    	对requests模块的封装


Data

--depend_data.py       对依赖数据的封装


Logs

--Logger_func.py   		logging模块封装


PublicConfig

--Path_var.py				工程变量
--Public_config.ini			公用配置文件
--Useragent_config.py		User-Agents数据封装


Run

--Run_main.py   脚本主程序


Testcase

--testcase.xlsx   测试用例


Testreport

--测试报告


UnittestCase

--test_case.py   测试用例集


Utils

--Config_parser.py   	配置文件解析模块
--Cookie_handle.py   	Cookie数据保存与写入模块
--Data_structure.py     测试数据组合模块
--Database_opt.py   	数据库操作模块
--Email_handle.py   	封装发送测试报告邮件模块
--Encryption.py   		数据加密模块
--Excel_handle.py   	excel文件解析模块
--Json_diff.py   		Json数据对比模块
--Json_handle.py   		Json文件解析模块


4.测试报告样式




