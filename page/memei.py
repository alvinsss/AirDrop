# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 17:01
# @Author  : alvin
# @File    : media_path.py
# @Software: PyCharm
import requests
from   utils.operationConfig import OperationConfig
from   utils.logger import Logger

class GetPathInfo(object):

    def __init__(self):
        self.getenvinfo = OperationConfig()
        self.log = Logger()

    def get_channel_path_dic(self):
        dic = {
            "add_channel":"/wrap/add",
            "update_channel":"/wrap/update_no_auditing",
        }
        return dic

    def get_admaterial_path_dic(self):
        dic = {
            "add_admaterial":"/admaterial/add",
        }
        return dic