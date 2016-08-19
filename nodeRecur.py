# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:13:24 2016

@author: lvanhulle
"""

import random


class test:
    def __init__(self):
        self.l1 = [7,6,1,5,5,6,7,8]
        self.l2 = [5,2,5,8,7,2,4]
        self.tally = 0
        print 'sum: ' + str(sum(self.l1))
        try:
            print self.mys(self.l1, 0, len(self.l1)-1)
        except Exception as e:
            pass
        print 'Tally: %d'%self.tally
    def mys(self, A, first, last):
        self.tally += 1
        if first == last: return A[first]
        middle = (first+last)/2
        return self.mys(A, first, middle) + self.mys(A, middle+1, last)
#        head = node()
#        prevNode = head
#    
#        for i in range(10):
#            curr = node(random.randint(1,4))
#            prevNode.nextNode=curr
#            prevNode = curr
#        
#        self.printList(head)
#        
#            
#        head = self.mc(head,4)
#        print '\nList2:'
#        self.printList(head)
#        
#        
#    def printList(self, curr):
#        while curr.nextNode is not None:
#            curr = curr.nextNode
#            print curr.data
#        
#    def mc(self, curr, x):
#        if curr is None: return None
#        if curr.data == x:
#            return self.mc(curr.nextNode, x)
#        curr.nextNode = self.mc(curr.nextNode, x)
        return curr

class node(object):
    def __init__(self, data=None, nextNode=None):
        self.nextNode = nextNode
        self.data = data
        
if __name__=='__main__':
    t = test()