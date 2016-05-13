# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:57:47 2016

@author: lvanhulle
"""

from functools import wraps

m_dict = {}
g_dict = {}
def grouper(mode_dict=None, group=None, modal=True):
    mode_dict[group] = None
    def decorate(func):
        @wraps(func)
        def modes(*args):
            if mode_dict[group] == func.__name__:#code:
                active = True
            else:
                active = False
            if modal:
                mode_dict[group] = func.__name__#code
            else:
                mode_dict[group] = None
            return func(*args, active=active)
        return modes
    return decorate

def gcode(**kwargs):
    return grouper(g_dict, **kwargs)
    
def mcode(group=None, modal=None):
    return grouper(m_dict, group=group, modal=modal)
   
@gcode(group=1)
def g0(val, active=False):
    if active:
        return 'Active ' + str(val)
    return 'Not Active ' + str(val)
    
@gcode(group=1)
def g1(val, active=False):
    if active:
        return 'Active ' + str(val)
    return 'Not Active ' + str(val)
    
@gcode(group=1, modal=False)
def g2(val, active=False):
    if active:
        return 'Not good'
    return 'Working arc'

@gcode(group=2)
def g91(_, active=False):
    if active:
        return 'Active ' + str(91)
    return 'Not Active ' + str(91)
    
@gcode(group=2)
def g90(_, active=False):
    if active:
        return 'Active ' + str(90)
    return 'Not Active ' + str(90)

@mcode(group=1)
def m6(_, active=False):
    if active:
        return 'Already Changing'
    return 'Start Changing'

@mcode(group=1)    
def m5(_, active=False):
    if active:
        return 'Trying'
    return 'Stopping'

class tester():
    
    def __init__(self):
        self.codes = {'y':1, 'z':2}
        self.generics = []
        
    def x(self):
        print 'x'
    
    def over(self, code):
        def generic():
            print self.codes[code]
        return generic
            
        
    def __getattr__(self, name):
        return self.over(name)
        
#    def __class__(self):
#        print 'Ummm, here'
    