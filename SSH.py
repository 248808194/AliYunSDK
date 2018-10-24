    # coding=utf-8
# File Name：     SSH
# Author :       zhoutao
# date：          2018/10/22    17:53

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-09-09:23
# Python 3.5


import paramiko
import os,sys
import subprocess
import tkFileDialog



class SSH(object):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self,host,port,username,password):
        self.host = host
        self.port = port
        self.username = username
        self.password= password


    # @property
    def comm(self,cmmd='df -h'):
        cmmd = 'sudo su - root -c "' + cmmd + '"'
        print cmmd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        self.stdin,self.stdout,self.shderr = self.ssh.exec_command(cmmd,get_pty=True) #python3.4 db.py
        self.stdin.write(self.password + '\n')
        self.out = str(self.stdout.read())
        print(self.out)
        self.ssh.close()


    def upload_download_init(self):

        self.t = paramiko.Transport((self.host,self.port))
        self.t.connect(username=self.username,password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)
        return self.sftp


    def upload(self,remotepath):
        default_dir = r"C:\Users\Administrator\Desktop"  # 设置默认打开目录
        fname = tkFileDialog.askopenfilename(title=u"选择文件")
        print fname  # 返回文件全路径
        upload_sftp = self.upload_download_init()
        remotepath = remotepath + "/" + fname
        print remotepath
        upload_sftp.put(fname,remotepath)


    def download(self,files,localpath):
        download_sftp = self.upload_download_init()
        download_sftp.get(files,localpath)
        download_sftp.close()



S=SSH('10.61.100.33',22,'zhoutao','1')
S.upload('/tmp')
S.comm(cmmd='ls /tmp')
# server1 = SSH('180.153.238.109',23432,'root')

# server1.comm
# server1.download('/tmp/test.txt','/tmp/test.txt')
# server1.upload('/tmp/test.txt','/tmp/123test.txt')


