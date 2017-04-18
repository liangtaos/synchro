#!/usr/bin/python
#coding:utf8

import threading
import time
import os
import paramiko
import sys

#def func(ip,user,cmd):
#    ssh = paramiko.SSHClient()
#    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#    key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#    ssh.connect(hostname=ip,username=user,pkey=key)
#    stdin, stdout, stderr = ssh.exec_command(cmd)
#    print '%s %s : \n %s'%(ip, cmd, stdout.read().strip())
#    ssh.close()
class MyCmd(threading.Thread):
    def __init__(self, ip, user, cmd):
        threading.Thread.__init__(self)
        self.ip = ip
        self.user = user
        self.cmd = cmd

    def run(self):
	ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        try:
            ssh.connect(hostname=self.ip,username=self.user,pkey=key, timeout=1)
	except:
	    print '%s \n TIMEOUT or NOT PRIVILEGES'%(self.ip)
            sys.exit()
        stdin, stdout, stderr = ssh.exec_command(self.cmd)
        if stdout.read():
            print  '%s %s : \n %s'%(self.ip, self.cmd, stdout.read().strip())
            ssh.close()
        else:
	    print  '%s %s : \n %s'%(self.ip, self.cmd, stderr.read().strip())
            ssh.close()
         
    

if __name__ == '__main__':
    cmd = ' '.join(sys.argv[1:])
    print '执行的命令 %s '% cmd
    ips = ['47.90.44.152', '118.26.161.27']
    user = 'root'
    th = []
    for ip in ips:
        #print ip
	mycmd = MyCmd(ip, user, cmd) 
        th.append(mycmd)
        mycmd.start()
    for i in th:
       i.join()
    print 'Done!'
