#!/usr/bin/python
#-*-coding:utf-8-*-

import os
print('process %s start... ' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process : %s \n parent process : %s' % (os.getpid(),os.getppid()))
else:
    print('I am parent process : %s \n child process : %s' % (os.getpid(),pid))
