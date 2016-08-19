# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:42:58 2016

@author: lvanhulle
"""

import random
import time

HIGHER = 1
LOWER = -1
CORRECT = 0
MAX = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

def checker_Coro():
    num = random.randint(0,MAX)
    print 'Enter your first guess'
    guess = yield
    numGuesses = 1
    while guess != num:        
        if guess < num:
            print "Guess Higher"
            guess = yield HIGHER           
        else:
            print "Guess Lower"
            guess = yield LOWER
        numGuesses += 1
    print 'Correct! The number was %e' %num
    print 'It took you %d tries' %numGuesses
    yield 0
    
def guesser_Coro():
    low = 0
    high = MAX
    result = -2
    numGuesses = 0
    while result != CORRECT:
        numGuesses += 1
        guess = (high - low)/2 + low
        print 'My guess is : %d\n' %guess
        result = yield guess
        if result == HIGHER:
            low = guess
        elif result == LOWER:
            high = guess
    print 'It took me %d tries but I got it.' %numGuesses
    
guesser = guesser_Coro()
checker = checker_Coro()
next(checker)

result = None
n = 1
while n > 0:
    try:        
        result = checker.send(guesser.send(result))
    except:
        n = -1
