# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:48:14 2018

@author: JerryC
"""

import scipy
import scipy.ndimage
import numpy as np
import multiprocessing


class Neighbourhood:
    def __init__(self,in_array,kernal=None):
        self.__in_array=in_array
        if not kernal:
            self.__kernal = np.array([1]*49).reshape((7,7))
        else:
            self.__kernal = kernal
        self.__c=[]

    def __calculate(self,in_array,i):
        d=in_array.copy()
        d[d!=i]=0
        d=d//i
        return scipy.ndimage.convolve(d, self.__kernal,mode='constant', cval=0)
    
    def _thread1(self,out,c,in_array):
        for i in c[:len(c)//2]:
            out.append(self.__calculate(in_array,i))
    def _thread2(self,out,c,in_array):
        for i in c[len(c)//2:]:
            out.append(self.__calculate(in_array,i))
            
        
    def _thread3(self,out,c,in_array):
        for i in c[:len(c)//3]:
            out.append(self.__calculate(in_array,i))
    def _thread4(self,out,c,in_array):
        for i in c[len(c)//3:2*len(c)//3]:
            out.append(self.__calculate(in_array,i))
    def _thread5(self,out,c,in_array):
        for i in c[2*len(c)//3:]:
            out.append(self.__calculate(in_array,i))
        
    # two processes
    def lalalala2(self):
        c=list(set(self.__in_array.reshape(-1)))
        c.sort()
        self.__c=c
        manager = multiprocessing.Manager()
        out1=manager.list()#多进程共享变量
        out2=manager.list()
        
        p1 = multiprocessing.Process(target = self._thread1,args=(out1,c,self.__in_array,))
        p2 = multiprocessing.Process(target = self._thread2,args=(out2,c,self.__in_array,))
        p1.start()
        p2.start()
    #    print(out1[0])
        p1.join()
        p2.join()
        out=[]
        out.extend(out1)
        del out1
        out.extend(out2)
        del out2
        return np.array(out)
    
    # three processes
    def lalalala3(self):
        c=list(set(self.__in_array.reshape(-1)))
        c.sort()
        self.__c=c
        manager = multiprocessing.Manager()
        out1=manager.list()#多进程共享变量
        out2=manager.list()
        out3=manager.list()
        p1 = multiprocessing.Process(target = self._thread3,args=(out1,c,self.__in_array,))
        p2 = multiprocessing.Process(target = self._thread4,args=(out2,c,self.__in_array,))
        p3 = multiprocessing.Process(target = self._thread5,args=(out3,c,self.__in_array,))
        p1.start()
        p2.start()
        p3.start()
    #    print(out1[0])
        p1.join()
        p2.join()
        p3.join()
        out=[]
        out.extend(out1)
        del out1
        out.extend(out2)
        del out2
        out.extend(out3)
        del out3
        return np.array(out)
    
    def getClasses(self):
        return self.__c
    
    # single process
    def lalalala(self):
        c=list(set(self.__in_array.reshape(-1)))
        c.sort()
        self.__c=c
        out=[]
        for i in c:
            d=self.__in_array.copy()
            d[d!=i]=0
            d=d//i
            out.append(scipy.ndimage.convolve(d, self.__kernal,mode='constant', cval=0))
            del d
        return np.array(out)

if __name__=='__main__':
    ascent = np.array(np.random.randint(1,11,(1000,1000)),dtype=np.int16)*10 #random matrix
    a=Neighbourhood(ascent)
    b=a.lalalala2()
    c=a.lalalala()
    
