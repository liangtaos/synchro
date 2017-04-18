#!/usr/bin/python
#coding:utf8

import threading
import time
import os
import paramiko
import sys

def func(ip,user,cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    ssh.connect(hostname=ip,username=user,pkey=key)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print '%s %s : \n %s'%(ip, cmd, stdout.read().strip())
    ssh.close()




if __name__ == '__main__':
    cmd = ' '.join(sys.argv[1:])
    print cmd
    ips = ['47.90.44.152', '118.26.161.27']
    user = 'root'
    for ip in ips:
	th = threading.Thread(target=func,args=(ip, user, cmd)) 
        th.start()

