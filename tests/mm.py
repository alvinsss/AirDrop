# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 15:06
# @Author  : alvin
# @File    : test_cpa_main_flow.py
# @Software: PyCharm
# import  unittest
import  time as t
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from utils.public import data_dir_file
from PIL import Image
from io import BytesIO
import re
import numpy as np
from io import BytesIO
import time, requests


class Test_Airdrop():
    '''
    进行MM业务
    :return:
    '''
    def setUp(self):
        pass

    def __init__(self):
        self.filename = data_dir_file(dirPath='MEMEI',fileName="ETH_ad.txt")
        self.drexepath = "D:\\UserData\git\WebStorm\AirDrop\extend\chromedriver.exe"
        self.mmurl = "https://memei.io/?share=RH06q5S"

    def get_track(distance):
        track = []
        current = 0
        mid = distance * 3 / 4
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move))
        return track

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
        dr = webdriver.Chrome(self.drexepath)
        dr.get(self.mmurl)
        print("111")
        dr.implicitly_wait(5)
        dr.maximize_window()
        t.sleep(random.randrange(3, 5, 1))
        jsCode = "var q=document.documentElement.scrollTop=1200"
        dr.execute_script(jsCode)
        eth_ads = Test_Airdrop.get_ETH_Address(self)
        for address in eth_ads:
            print("current ads is:"+address)
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            dr.find_element_by_id("subeth").click()
            t.sleep(1)
            dr.quit()




if __name__ == '__main__':
    Test_Ad = Test_Airdrop()
    # Test_Ad.get_ETH_Address()
    Test_Ad.Participate_Airdrop()