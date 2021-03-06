# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:06
# @Author  : alvin
# @File    : sidc.py
# @Software: PyCharm
# import  unittest

import time as t
import random
import requests
import json
import datetime
from utils.logger import Logger
from utils.public import data_dir_file
from utils.operationExcel_writedata import Data_Excel_Action
from utils.operationemail import MyMail

class Test_Mainbi():
    '''
    进行mainbi
    :return:
    '''

    def setUp(self):
        pass

    def __init__(self):
        '''初始配置'''
        self.log = Logger()
        self.filename = data_dir_file( dirPath='MainBi',
                                       fileName="ManinBi_demo.xlsx" )
        self.excel = Data_Excel_Action()
        self.mailaction= MyMail()


    def write_mainbi_data(self):
        '''接口数据'''
        fileName="mainbi"
        tableTitle = ['日期','排名', '全名', '币种', '市值','币价RMB','币价USDT','换手率','BTC兑换个数']
        res = requests.get(
            "https://dncapi.bqrank.net/api/coin/web-coinrank?page=1&type=-1&pagesize=100&webp=1" )
        if 200 == res.json()['code']:
            if res.json()['msg'] == "success":
                data = []
                for i in range( int( res.json()['maxpage'] ) ):
                    list_data = []
                    list_data.append( (datetime.datetime.now()).strftime(
                        "%Y-%m-%d %H:%M:%S" ) )
                    list_data.append( res.json()['data'][i]['rank'] )
                    list_data.append( res.json()['data'][i]['fullname'] )
                    list_data.append( res.json()['data'][i]['name'] )
                    list_data.append( res.json()['data'][i]['market_value'] )
                    list_data.append( res.json()['data'][i]['current_price'] )
                    list_data.append( res.json()['data'][i]['current_price_usd'] )
                    list_data.append( res.json()['data'][i]['turnoverrate'] )
                    # 增加兑换数量
                    if 0 == i:
                        list_data.append(
                            (res.json()['data'][i]['current_price']) / (res.json()['data'][i]['current_price']) )
                    else:
                        '''非btc数据兑换处理'''
                        f_number=format((res.json()['data'][0]['current_price']) / (res.json()['data'][i]['current_price']),'.3f' )
                        list_data.append( f_number )
                        '''针对个币数据处理发邮件'''
                        if res.json()['data'][i]['name'] == 'ETH':
                            msg="1 btc exchange->" +f_number+  "  ETH"
                            '''小于10个发邮件，注意牛市尾期 根据历史牛市数据'''
                            if float(f_number) <= 10:
                                self.mailaction.send_mail(msg,'BTC exchange ETH mail info ')
                            else:
                                self.log.info("1 btc exchange->" +f_number+ "   eth" )

                        if res.json()['data'][i]['name'] == 'BCH':
                            msg="1 btc exchange->" +f_number+  "  BCH"
                            if float(f_number) >= 83.3:
                                self.mailaction.send_mail(msg,'BTC exchange BCH mail info ')
                            else:
                                self.log.info("1 btc exchange->" +f_number+ "   BCH" )
                        if res.json()['data'][i]['name'] == 'LTC':
                            msg="1 btc exchange->" +f_number+  "  LTC"
                            if float(f_number) >= 250:
                                self.mailaction.send_mail(msg,'BTC exchange LTC mail info ')
                            else:
                                self.log.info("1 btc exchange->" +f_number+ "   LTC" )
                    data.append( list_data )
                    '''btc可兑换eth单独写文件方便后续展示'''
                    # print(data)
                    if res.json()['data'][i]['name'] == 'ETC':
                        self.excel.awrite_ethhistorydata( data[0] )
                        self.excel.awrite_ethhistorydata( data[1] )
                        self.excel.awrite_ethhistorydata( data[3] )
                        self.excel.awrite_ethhistorydata( data[7] )
                        self.excel.awrite_ethhistorydata( data[8] )
                        self.excel.awrite_ethhistorydata( data[11] )
                self.excel.write_data(fileName,data,tableTitle )
            else:
                print("request mainbi is failed!")

    def vix_data(self,createV,reduceV,safetyV):
        '''接口数据 http://wx.heyuedi.com/alarm/fng/h5
          连续低于66可以建仓，70-90之间持币待涨，连续大于90
          注意回调风险   数据分析整体 仅供参考！'''
        tableTitle = ['日期', '币价USDT', '恐慌贪婪值']
        fileName = "vix"
        res = requests.get(
            "http://wx.heyuedi.com/alarm/fng/getFng" )
        if 0 == res.json()['code']:
            if res.json()['msg'] == "成功":
                data = []
                count = 0
                lens=len( res.json()['data'] )
                for i in range( lens ):
                    list_data = []
                    list_data.append( res.json()['data'][i]['date'] )
                    list_data.append( res.json()['data'][i]['btc_price'] )
                    list_data.append( res.json()['data'][i]['value'] )
                    data.append( list_data )
                    if (int( res.json()['data'][lens-1]['value'] ) <= createV):
                        print("create one's position size")
                    if (int( res.json()['data'][lens-1]['value'] ) >= reduceV):
                        print("reduce one's position size")
                    if (int( res.json()['data'][i]['value'] ) >= safetyV):
                        count = count +1
                self.excel.write_data(fileName,data,tableTitle )
                if count > 0:
                    data[lens-1].append(count)
                    self.excel.awrite_ethhistorydata( data[lens-1] )
        else:
            print("request vix is failed!")

    def tran_histydata(self):

        tableTitle = ['日期', '开盘价', '收盘价', '最高价', '最低价']
        fileName = "cspr"
        res = requests.get(
            "https://dncapi.bqrank.net/api/v3/coin/history?coincode=casper&begintime=20210411&endtime=20210511&page=1&per_page=1000&webp=1" )
        if 200 == res.json()['code']:
            if res.json()['msg'] == "success":
                # print(res.json())
                data = []
                count = 0
                lens=len( res.json()['data']['list'] )
                print(lens)
                for i in range( lens ):
                    list_data = []
                    list_data.append( res.json()['data']['list'][i]['tickertime'] )
                    list_data.append( res.json()['data']['list'][i]['openprice'] )
                    list_data.append( res.json()['data']['list'][i]['closeprice'] )
                    list_data.append( res.json()['data']['list'][i]['high'] )
                    list_data.append( res.json()['data']['list'][i]['low'] )
                    data.append( list_data )
                print(data)
                self.excel.write_data(fileName,data,tableTitle )
        else:
            print("request vix is failed!")

    def new_vix_data(self):
        tableTitle = ['日期', '恐慌贪婪值', '恐慌贪婪值对应文字']
        fileName = "new_vix"
        res = requests.get("https://history.btc126.com/zhishu/api.php")
        # print(res.json())
        if 1 == res.json()['code']:
            if res.json()['msg']=="sucess":
                print(res.json()['msg'])
                data=[]
                lens = len(res.json()['data'])
                for i in range(lens):
                    list_data = []
                    list_data.append(res.json()['data'][i]['datetime'])
                    list_data.append(res.json()['data'][i]['value'])
                    list_data.append(res.json()['data'][i]['result'])
                    data.append( list_data )
                self.excel.write_data(fileName,data,tableTitle )
        else:
            print("request new vix is failed!")

if __name__ == '__main__':
    Test = Test_Mainbi()
    # Test.tran_histydata()
    # Test.vix_data(50,90,90)
    Test.new_vix_data()
