# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:06
# @Author  : alvin
# @File    : sidc.py
# @Software: PyCharm
# import  unittest
import  time as t
import random
from selenium import webdriver
from utils.public import data_dir_file,get_extend_chromedriver_file
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
        self.filename = data_dir_file(dirPath='TYF',fileName="ETH_ad.txt")
        self.drexepath = get_extend_chromedriver_file()
        self.url = "https://www.tyfcoin.com/index/index/index/code/692"
        self.log = Logger()

    def get_ETH_Address(self):
        '''获取文件eth地址'''
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
        '''空投页面提交eth地址'''
        fmt='%Y-%m-%d %H:%M:%S'      #定义时间显示格式
        count=0
        eth_ads = Test_Airdrop.get_ETH_Address(self)
        for address in eth_ads:
            #处理每一行eth地址数据
            dr = webdriver.Chrome(self.drexepath)
            dr.get(self.url)
            dr.implicitly_wait(5)
            dr.maximize_window()
            t.sleep(random.randrange(3, 5, 1))
            jsCode = "var q=document.documentElement.scrollTop=1200"
            dr.execute_script(jsCode)
            count = count+1
            dr.find_element_by_xpath("//*[@type='text']").clear()
            t.sleep(random.randrange(1,2))
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            print(t.strftime(fmt,t.localtime(t.time()))+":NO is:"+str(count)+ ",current address->"+address+"  submit is start ....")
            # self.log.info(t.strftime(fmt,t.localtime(t.time()))+":NO is:"+str(count)+ ",current address->"+address+"  submit is start ....")
            t.sleep(random.randrange(3,61))#随机9-61秒之间
            dr.find_element_by_id("btn").click()
            self.log.info(t.strftime(fmt,t.localtime(t.time()))+"_TYF_current address->"+address+"_submit is end")
            dr.refresh()
            t.sleep(random.randrange(1, 3, 1))
            dr.get("http://www.sidc.pro")
            dr.implicitly_wait(5)
            dr.maximize_window()
            t.sleep(random.randrange(1, 3, 1))
            jsCode = "var q=document.documentElement.scrollTop=1200"
            dr.execute_script(jsCode)
            dr.find_element_by_xpath("//*[@type='text']").clear()
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            t.sleep(random.randrange(3,62))#随机9-61秒之间
            dr.find_element_by_xpath("//body/a[@id='airdrop']/div[1]/div[@class='container']/div[@class='row c-row1']/div[@class='col-md-2']/p[1]").click()
            self.log.info(t.strftime(fmt,t.localtime(t.time()))+"_SIDC_current address->"+address+"_submit is end")
            dr.close()
        self.log.info("total:"+count+"  address tranf over !")
        dr.close()

if __name__ == '__main__':
    Test_Ad = Test_Airdrop()
    Test_Ad.Participate_Airdrop()