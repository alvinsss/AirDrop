#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:alvin
@file: sendmail.py
@time: 2019/01/18
"""
import smtplib
from email.mime.text import MIMEText
from utils.operationConfig import OperationConfig


class Mail(object):
	def __init__(self):
		self.mailinfo = OperationConfig()

	def send_mail(self, to_user, sub, content):
		'''
		发送邮件内容
		:param to_user:发送邮件的人
		:param sub:主题
		:param content:邮件内容
		'''
		global send_mail_smtp
		global send_user
		send_mail_smtp   = self.mailinfo.getMailsendinfo().get('smtp')
		send_user        = self.mailinfo.getMailsendinfo().get('user')
		send_user_passwd = self.mailinfo.getMailsendinfo().get('passwd')

		message = MIMEText(content, _subtype='plain', _charset='utf-8')
		message['Subject'] = sub
		message['From'] = send_user
		message['To'] = to_user
		server = smtplib.SMTP()
		server.connect(send_mail_smtp)
		server.login( send_user,send_user_passwd )
		server.sendmail(send_user, to_user, message.as_string())
		server.close()

if __name__ == "__main__":
	m = Mail()
	m.send_mail('6449694@qq.com', '接口自动化测试报告', "qatest")
