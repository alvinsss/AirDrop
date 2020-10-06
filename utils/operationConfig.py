#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:alvin
@file: operationConfig.py
@time: 2019/01/18
"""
import  configparser
import  os
from utils.operationTestdata import TestData

class OperationConfig(object):


    def __init__(self):
        self.testdata = TestData()

    def get_sendmail_info(self,contents="mail"):
        tmpdict={}
        config = configparser.ConfigParser()
        config.read(self.testdata.data_dir('config','config.ini'),encoding="utf-8-sig")
        # print(config)
        send_user=config.get(contents,'SEND_USER')
        send_mail_smtp=config.get(contents,'SEND_MAIL_SMTP')
        send_user_passwd=config.get(contents,'SEND_USER_PASSWD')
        tmpdict['user']=send_user
        tmpdict['smtp']=send_mail_smtp
        tmpdict['passwd']=send_user_passwd
        return tmpdict

    def get_testenv_info (self,contents="env-test-api"):
        envdic = {}
        config= configparser.ConfigParser()
        config.read(self.testdata.data_dir('config','config.ini'),encoding="utf-8-sig")
        admin_url = config.get(contents,"ADMIN_URL")
        admin_user = config.get(contents,"ADMIN_USERNAME")
        admin_password = config.get(contents,"ADMIN_PASSWD")
        # print(admin_url)

        dsp_url   = config.get(contents,"DSP_URL")
        dsp_user_cpa = config.get(contents,"DSP_USERNAME_CPA",)
        dsp_user_hx = config.get(contents,"DSP_USERNAME_HX",)
        dsp_user_cpd = config.get(contents,"DSP_USERNAME_CPD",)
        dsp_user_ad = config.get(contents,"DSP_USERNAME_AD",)
        dsp_password = config.get(contents,"DSP_PASSWD")

        media_url = config.get(contents,"MEDIA_URL")
        media_user_cpa = config.get(contents,"MEDIA_USERNAME_CPA")
        media_user_hx = config.get(contents,"MEDIA_USERNAME_HX")
        media_password = config.get(contents,"MEDIA_PASSWD")

        envdic['admin_url']=admin_url
        envdic['admin_user']=admin_user
        envdic['admin_password']=admin_password

        envdic['dsp_url']  = dsp_url
        envdic['dsp_user_cpa']=dsp_user_cpa
        envdic['dsp_user_hx']=dsp_user_hx
        envdic['dsp_user_cpd']=dsp_user_cpd
        envdic['dsp_user_ad']=dsp_user_ad
        envdic['dsp_password']=dsp_password

        envdic['media_url'] = media_url
        envdic['media_user_cpa']=media_user_cpa
        envdic['media_user_hx']=media_user_hx
        envdic['media_password']=media_password
        return envdic

    def get_testenv_mysql(self,contents="mysql"):
        '''contents config file flag'''
        mysqldic={}
        config = configparser.ConfigParser()
        config.read(self.testdata.data_dir('config','config.ini'),encoding="utf-8-sig")
        mysqlhost    = config.get(contents,'HOST')
        mysqlport    = config.get(contents,"PORT")
        mysqluser    = config.get(contents,"USER")
        mysqlpasswd  = config.get(contents,"PASSWD")
        mysqldatabases =config.get(contents,"DADABASES")
        mysqlcharset   = config.get(contents,"CHARSET")
        mysqldic['host']=mysqlhost
        mysqldic['port']=mysqlport
        mysqldic['user']=mysqluser
        mysqldic['password']=mysqlpasswd
        mysqldic['databases']=mysqldatabases
        mysqldic['charsetdb']=mysqlcharset
        return mysqldic

if __name__ == "__main__":
	a = OperationConfig()
	print(a.get_testenv_info())
	# print(a.getMailsendinfo())


