# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:16:22 2015

@author: lvanhulle
"""
#import itertools
#from collections import namedtuple
#import random
#from operator import itemgetter
#


#def endPoints(points):
#    end = []
#    current = [] 
#    num = 0
#    for cur_point in points:
#        num+=1
#        if(num==1): 
#            first = cur_point 
#        previous = current 
#        current = [] 
#        previous.append(cur_point) 
#        current.append(cur_point) 
#        if(num>1): 
#            end.append(previous) 
#    current.append(first)
#    end.append(current) 
#    return end
#

def pairwise1(itr):
    return list(zip(itr[:-1], itr[1:]))

def pairwise_gen(l1):
    l1Iter = iter(l1)
    pre = next(l1Iter)
    for curr in l1Iter:
       yield pre, curr
       pre = curr

def pairwise(l1):
    l1Iter = iter(l1)
    pre = next(l1Iter)
    result = []
    for curr in l1Iter:
        result.append([pre, curr])
        pre = curr
    return result
    
#def pairwise(l1):
#    l1Iter = iter(l1)
#    first = pre = next(l1Iter)
#    result = []
#    for curr in l1Iter:
#        result.append([pre, curr])
#        pre = curr
#    result.append([pre, first])
#    return result
#    
#def pairwise_gen(l1):
#    l1Iter = iter(l1)
#    first = pre = next(l1Iter)
#    for curr in l1Iter:
#       yield pre, curr
#       pre = curr
#    yield pre, first
    
#NT = namedtuple('NT', 'letter number')
#l1 = [i for i in 'edcba']
#l2 = [i for i in range(len(l1))]
#l3 = [NT._make(i) for i in zip(l1,l2)]
    
#NT = namedtuple('NT', 'X Y Z')
#NT_One = namedtuple('NT_One', 'Only')
#
#x = [1,2]
#y = ['a','b','c']
#z = ['V','W','X','Y','Z']
#
#def var_gen(inputLists):
#    if iter(inputLists) is iter(inputLists):
#        # Tests if inputLists is a generator
#        iterType = tuple
#    else:
#        iterType = type(inputLists)
#    cycles = map(itertools.cycle, inputLists)
#        
#    while 1:
#        try:
#            # This is the logic for a named tuple
#            yield iterType._make(map(next, cycles))
#        except Exception:
#            yield iterType(map(next, cycles))
#        
#test = []
#test.append(var_gen(NT(x,y,z))) # namedtuple with multiple fields
#test.append(var_gen(NT_One(x))) # namedtuple with only one field
#test.append(var_gen((x,y,z)))   # regular tuple
#test.append(var_gen([x,y,z]))   # list
#test.append(var_gen((i for i in (x,y,z)))) # generator
#
#for gen in test:
#    print 'Next Test:'
#    for i in xrange(10):
#        print next(gen)
#    print ' '




    