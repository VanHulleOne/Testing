# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 15:07:15 2016

@author: lvanhulle
"""

numDiscs = 3
names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']

class Disc(object):
    
    pegs = set(range(3))
    
    def __init__(self, name, smallerDisc):
        self.name = names[name]
        self.tabs = '\t'*(numDiscs-name-1)
        self.smallerDisc = smallerDisc
        self.currPeg = 0
        
    def move(self, dest):
        print self.tabs + self.name + ' asked to move to: ' + str(dest)        
        if self.smallerDisc is not None:
            openPeg = (self.pegs - {self.currPeg, dest}).pop()
            print (self.tabs + self.name + ' asking ' + self.smallerDisc.name +
                    ' to move to: ' + str(openPeg))
            self.smallerDisc.move(openPeg)
            print self.tabs + self.name + ' moving to ' + str(dest)
            self.currPeg = dest
            print self.tabs + self.name + ' asking ' + self.smallerDisc.name + ' to move to ' + str(dest)
            self.smallerDisc.move(dest)
        else:
             print self.tabs + self.name + ' moving to ' + str(dest)
             self.currPeg = dest        
        
def createDiscs(num=numDiscs-1):
    if num < 0:
        return None
    return Disc(num, createDiscs(num-1))
    
bottomDisc = createDiscs()
    
bottomDisc.move(3)