#!/usr/bin/python
#-*- coding:utf-8 -*-

from multiprocessing import Pool
import os,random,time

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__ == '__main__':
    print('Parent process is %s' % os.getpid())
    p = Pool()
    for i in range(9):
        #p.apply(long_time_task,args=(i,))          #use cpu one core
        p.apply_async(long_time_task,args=(i,))     #use cpu multi core
    print('Waiting for all processing done...')
    p.close()
    p.join()
    print('All subprocess done')

