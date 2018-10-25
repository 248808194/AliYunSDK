# coding=utf-8
# File Name：     sendmail
# Author :       zhoutao
# date：          2018/10/25    18:44

# coding=utf-8
# File Name：     1
# Author :       zhoutao
# date：          2018/10/25    18:24

# -*- coding:utf-8 -*-
import urllib, urllib2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
# 发件人地址，通过控制台创建的发件人地址
username = 'zhou.tao@wowoohr.com'
# 发件人密码，通过控制台创建的发件人密码
password = '111qqq...'
# 收件人地址列表，支持多个收件人，最多30个
rcptlist = ['zhou.tao@wowoohr.com']
receivers = ','.join(rcptlist)
# 构建 multipart 的邮件消息
msg = MIMEMultipart('mixed')
msg['Subject'] = Header('统计信息', 'utf-8').encode()
msg['From'] = username
msg['To'] = receivers
# 构建 multipart/alternative 的 text/plain 部分
alternative = MIMEMultipart('alternative')
textplain = MIMEText('纯文本部分',_charset='utf8')
alternative.attach(textplain)
# 构建 multipart/alternative 的 text/html 部分
texthtml = MIMEText('超文本部分', 'html')
alternative.attach(texthtml)
# 将 alternative 加入 mixed 的内部
msg.attach(alternative)
# 附件类型
# xlsx 类型的附件
# xlsxpart = MIMEApplication(open('1.xlsx', 'rb').read())
# xlsxpart.add_header('Content-Disposition', 'attachment', filename='1.xlsx')
# msg.attach(xlsxpart)
# # jpg 类型的附件
# jpgpart = MIMEApplication(open('2.jpg', 'rb').read())
# jpgpart.add_header('Content-Disposition', 'attachment', filename='2.jpg')
# msg.attach(jpgpart)
# # mp3 类型的附件
# mp3part = MIMEApplication(open('3.mp3', 'rb').read())
# mp3part.add_header('Content-Disposition', 'attachment', filename='3.mp3')
# msg.attach(mp3part)
# # 发送邮件

txtpart = MIMEApplication(open('log.txt', 'rb').read())
txtpart.add_header('Content-Disposition', 'attachment', filename='log.txt')
msg.attach(txtpart)
try:
    client = smtplib.SMTP()
    #python 2.7以上版本，若需要使用SSL，可以这样创建client
    #client = smtplib.SMTP_SSL()
    client.connect('smtp.mxhichina.com',80)
    client.login(username, password)
    #发件人和认证地址必须一致
    client.sendmail(username, rcptlist, msg.as_string())
    client.quit()
    print '邮件发送成功！'
except smtplib.SMTPRecipientsRefused:
    print '邮件发送失败，收件人被拒绝'
except smtplib.SMTPAuthenticationError:
    print '邮件发送失败，认证错误'
except smtplib.SMTPSenderRefused:
    print '邮件发送失败，发件人被拒绝'
except smtplib.SMTPException,e:
    print '邮件发送失败, ', e.message
