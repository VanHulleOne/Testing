# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:34:17 2016

@author: lvanhulle
"""

def deco(func):
    def inner():
        return func() + '\nRunning Inner'
        
    return inner
#@deco
def target():
    return 'Running Target'
    
target = deco(target)

print target()
