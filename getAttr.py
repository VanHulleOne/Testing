# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:57:47 2016

@author: lvanhulle
"""

from functools import wraps
from classImport import c1

m_dict = {}
g_dict = {}
def grouper(mode_dict=None, group=None, modal=True, name=None):
    mode_dict[group] = None
    def decorate(func):
        @wraps(func)
        def modes(*args):
            if name is None:
                funcName = func.__name__
            else:
                funcName = name
            if mode_dict[group] == funcName:#code:
                active = True
            else:
                active = False
            if modal:
                mode_dict[group] = funcName#code
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
def g91(active=False):
    if active:
        return 'Active ' + str(91)
    return 'Not Active ' + str(91)
    
@gcode(group=2)
def g90(active=False):
    if active:
        return 'Active ' + str(90)
    return 'Not Active ' + str(90)

@mcode(group=1)
def m6(_, active=False):
    if active:
        return 'Already Changing'
    return 'Start Changing'

@mcode(group=1)    
def m5(active=False):
    if active:
        return 'Trying'
    return 'Stopping'

class tester(object):
    
    def __init__(self):
        self.codes = {'g93': 1, 'g94': 1, 'x':4}
        for code, group in self.codes.iteritems():
            self.__dict__[code] = self.over(code, group)
        
    def x(self):
        print 'x'
    
    def over(self, code, group):
        @gcode(group=group, name=code)
        def generic(active=False):
            print 'Is Active: ' + str(active)
#            print code
            return code #self.codes[code]
#        print 'Leaving over'
        return generic
