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
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from utils.public import data_MEMEIdir_file

class Test_Airdrop():
    '''
    进行MM业务
    :return:
    '''
    def setUp(self):
        pass

    def __init__(self):
        self.filename = data_MEMEIdir_file(fileName="ETH_ad.txt")
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
        dr.implicitly_wait(10)
        dr.maximize_window()
        t.sleep(random.randrange(5, 10, 1))
        jsCode = "var q=document.documentElement.scrollTop=1200"
        dr.execute_script(jsCode)
        eth_ads = Test_Airdrop.get_ETH_Address(self)
        for address in eth_ads:
            print("current ads is:"+address)
            dr.find_element_by_xpath("//*[@type='text']").send_keys(address)
            dr.find_element_by_id("subeth").click()
            # # 切换iframe
            # try:
            #     iframe = dr.find_element_by_xpath('//iframe')
            # except Exception as e:
            #     print ('get iframe failed: ', e)
            # t.sleep(2)	# 等待资源加载
            # dr.switch_to.frame(iframe)
            t.sleep(1)
            # 等待图片加载出来
            WebDriverWait(dr, 5, 0.5).until(
                EC.presence_of_element_located((By.ID, "dx_captcha_basic_bar_1"))
            )
            try:
                button = dr.find_element_by_id('dx_captcha_basic_bar_1')
            except Exception as e:
                print ('get button failed: ', e)
            # 开始拖动 perform()用来执行ActionChains中存储的行为
            flag = 0
            distance = 135
            offset = 5
            times = 0
            while 1:
                action = ActionChains(dr)
                action.click_and_hold(button).perform()
                action.reset_actions()	# 清除之前的action
                print ("distance",distance)
                track = Test_Airdrop.get_track(distance)
                print(track)
                for i in track:
                    action.move_by_offset(xoffset=i, yoffset=0).perform()
                    action.reset_actions()
                t.sleep(0.2)
                action.release().perform()
                t.sleep(2)

                # 判断某元素是否被加载到DOM树里，并不代表该元素一定可见
                try:
                    alert = dr.find_element_by_class_name('dx_captcha_basic_box').text
                except Exception as e:
                    alert = ''
                    alert = ''
                if alert:
                    print (u'滑块位移需要调整: %s' % alert)
                    distance -= offset
                    times += 1
                    t.sleep(5)
                else:
                    print ('滑块验证通过')
                    flag = 1
                    dr.switch_to.parent_frame()    # 验证成功后跳回最外层页面
                    break

            t.sleep(2)
        dr.quit()




if __name__ == '__main__':
    Test_Ad = Test_Airdrop()
    # Test_Ad.get_ETH_Address()
    Test_Ad.Participate_Airdrop()