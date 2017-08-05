#!/usr/bin/python
#-*-coding:utf-8-*-

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child Process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process is %s'% os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('Child process end')
