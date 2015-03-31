# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.


from multiprocessing import Pool 
import numpy as np
import numexpr as ne
import os


def randomArrays(n):
    
    arr1 = np.random.random((n,n))
    arr2 = np.random.random((n,n))
    
    return arr1, arr2

def launchComputation(n):
    pid = os.getpid()
    
    print "\tCreating random arrays - Pid: %i" % (pid)
    
    arrlist = randomArrays(n)
    
    arr1 = arrlist[0]
    arr2 = arrlist[1]
        
    print "\tStarting computations... - Pid: %i" % (pid)
    
    # Several computations for testing
    a = ne.evaluate("sin(arr1) + arr1**3 + sqrt(arr2)")
    b = ne.evaluate("(arr1**3) * (arr2**3)")
    c = ne.evaluate("a * b")
    
    sz = c.size
    
    print "\tProcess completed successfully! - Pid: %i\n\tArray size: %i" % (pid, sz)

if __name__ == '__main__':
    
    arrs_input = [5000] * 30
    
    pool = Pool(processes=4)
    pool.map(launchComputation, arrs_input)
    pool.close() 
    pool.join()
    

