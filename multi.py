#!/usr/bin/env python
#coding:utf-8

from threading import Thread
import time
import os
import sys
import paramiko
import multiprocessing

def getdata(ip, cmd, username='root'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    ssh.connect(hostname=ip, username = username, pkey = key, timeout=10)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    data = stdout.read()
    if data:
        print '"\033[1;4;33;40;4m主机:%s   命令:%s\033[0m": \n %s'%(ip, cmd, data),
        ssh.close()
    else:
	print '%s %s: \n %s'%(ip, cmd, stderr.read()[:-1]),
        ssh.close()



if __name__ == '__main__':
    #getdata('192.168.13.1','date')
    paramiko.util.log_to_file('filename.log')
    cmd = ' '.join(sys.argv[1:])
    pool = multiprocessing.Pool(50)
    ips = [ '192.168.13.'+ str(i) for i in xrange(1,201) ]
    for ip in ips:
	pool.apply_async(getdata, args=(ip, cmd))
    pool.close()
    pool.join()
    print 'Done'
