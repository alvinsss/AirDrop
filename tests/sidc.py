# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:06
# @Author  : alvin
# @File    : test_cpa_main_flow.py
# @Software: PyCharm
# import  unittest
import  time as t
import random
from selenium import webdriver
from utils.public import data_dir_file
from   utils.logger import Logger


class Test_Airdrop():
    '''
    进行SIDC业务
    :return:
    '''
    def setUp(self):
        pass

    def __init__(self):
        '''初始配置'''
        self.filename = data_dir_file(dirPath='SIDC',fileName="ETH_ad.txt")
        self.drexepath = "D:\\UserData\git\WebStorm\AirDrop\extend\chromedriver.exe"
        self.mmurl = "http://www.sidc.pro"
        self.log = Logger()

    def get_ETH_Address(self):
        lines=[]
        with open(self.filename,'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                lines.append(line)
            return lines

    def Participate_Airdrop(self):
        fmt='%Y-%m-%d %H:%M:%S'      #定义时间显示格式
        count=0
        dr = webdriver.Chrome(self.drexepath)
        dr.get(self.mmurl)
        dr.implicitly_wait(5)
        dr.maximize_window()
        t.sleep(random.randrange(3, 5, 1))
        jsCode = "var q=document.documentElement.scrollTop=1200"
        dr.execute_script(jsCode)
        eth_ads = Test_Airdrop.get_ETH_Address(self)

        for address in eth_ads:
            #处理提交数据请求
            count = count+1
            dr.find_element_by_xpath("//*[@type='text']").clear()
            t.sleep(random.randrange(1,3))
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            # print(t.strftime(fmt,t.localtime(t.time()))+":NO is:"+str(count)+ ",current address->"+address+"  submit is start ....")
            self.log.info(t.strftime(fmt,t.localtime(t.time()))+":NO is:"+str(count)+ ",current address->"+address+"  submit is start ....")
            t.sleep(random.randrange(2,100))#随机9-61秒之间
            dr.find_element_by_xpath("//body/a[@id='airdrop']/div[1]/div[@class='container']/div[@class='row c-row1']/div[@class='col-md-2']/p[1]").click()
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            self.log.info("current address->"+address+"_submit is end")
        self.log.info("total:"+count+"  address tranf over !")
        dr.close()

if __name__ == '__main__':
    Test_Ad = Test_Airdrop()
    Test_Ad.Participate_Airdrop()