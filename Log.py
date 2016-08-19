# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:08:47 2016

@author: lvanhulle
"""
import numba
#def coro():
#    result = []
#    hold = yield
#    while not (hold is None):
#        result.append('C_'+hold)
#        hold = yield
#    return result
#    
#def delGen():
#    genList = yield from coro()
#    yield genList
#    
#l1 = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3', 'b4']]
#
#out = []
#for sub in l1:
#    dg = delGen()
#    next(dg)
#    for s in sub:
#        print(s)
#        dg.send(s)
#    out.extend(dg.send(None))
#    
#print(out)
#        


@numba.jit
def stuff(x):
    v = []
    for i in range(x):
        v.append(x**2)
    return v