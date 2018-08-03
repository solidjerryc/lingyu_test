# lingyu_test

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Fri Aug  3 12:12:11 2018

    @author: jerryc
    """

    import scipy
    import numpy as np
    import multiprocessing

    kernal = np.array([1]*49).reshape((7,7))

    def _calculate(in_array,i):
        d=ascent.copy()
        d[d!=i]=0
        d=d//i
        return scipy.ndimage.convolve(d, kernal,mode='constant', cval=0)

    # two processes
    def lalalala(in_array):
        c=list(set(list(ascent.reshape(-1))))
        c.sort()
        manager = multiprocessing.Manager()
        out1=manager.list()#多进程共享变量
        out2=manager.list()
        def thread1():
            for i in c[:len(c)//2]:
                out1.append(_calculate(in_array,i))
        def thread2():
            for i in c[len(c)//2:]:
                out2.append(_calculate(in_array,i))

        p1 = multiprocessing.Process(target = thread1)
        p2 = multiprocessing.Process(target = thread2)
        p1.start()
        p2.start()
        while (p1.is_alive() or p2.is_alive()):
            pass
        out=[]
        out.extend(out1)
        out.extend(out2)
        del out1,out2
        return np.array(out)

    # single process
    def lalalala2(in_array):
        c=list(set(list(ascent.reshape(-1))))
        c.sort()
        out=[]
        for i in c:
            d=ascent.copy()
            d[d!=i]=0
            d=d//i
            out.append(scipy.ndimage.convolve(d, kernal,mode='constant', cval=0))
            del d
        return out


    ascent = np.array(np.random.randint(1,11,(10000,10000)),dtype=np.int16)*10 #random matrix
    a=lalalala(ascent)
    #b=lalalala2(ascent)


