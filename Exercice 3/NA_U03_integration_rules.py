#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:02:27 2017

numerical integration with several different integration rules

@author: sarradj
"""

from numpy import *
from pylab import *

# transfers local r-coordinate to global coordinate
def glob_koord(r,xL,xR):
    NL = 0.5 * (1-r)
    NR = 0.5 * (1+r)
    return NL*xL + NR*xR

# general integration function
# integrates f from xL to xR using rule
def integrate(f,xL,xR,rule):
    r,h = rule()
    x = glob_koord(r,xL,xR)
    I = (xR-xL)/2.0*(h*f(x)).sum()
    return I


# coordinates and weights for the integration

# Newton-Cotes rules
def trapez():
    r = array((-1.0,1.0))
    h = array((1.0,1.0))
    return r,h

def simpson():
    r = array((-1.0,0,1.0))
    h = array((1.0,4.0,1.0))/3.
    return r,h
    
def nc4():
    r = array((-1.0,-1/3.0,1/3.0,1.0))
    h = array((1.0,3.0,3.0,1.0))/4.
    return r,h

# Gauss rules
def gauss1():
    r = array((0.0,))
    h = array((2.0,))
    return r,h

def gauss2():
    r = array((-1.0,1.0))/sqrt(3)
    h = array((1.0,1.0))
    return r,h
    
def gauss3():
    r = array((-1.0,0,1.0))*sqrt(0.6)
    h = array((5.0,8.0,5.0))/9.0
    return r,h


#function 1 (a)
def fa(x):
    return x**4.0-1.0

xaL,xaR = 0, 4.0


#function 2 (b)
def fb(x):
    return sin(x)**2

xbL,xbR = 0, pi


print('')
funct, xL, xR = fa, xaL, xaR
exact = 200.8

print('=== function 1 ===')
for rule in (trapez,simpson,nc4,gauss1,gauss2,gauss3):
    I = integrate(funct,xL,xR,rule)
    print('%s: %f, error: %f, rel. error: %f' % (rule.__name__,I,I-exact,(I-exact)/exact))
    

print('')
funct, xL, xR = fb, xbL, xbR
exact = pi/2

print('=== function 2 ===')
for rule in (trapez,simpson,nc4,gauss1,gauss2,gauss3):
    I = integrate(funct,xL,xR,rule)
    print('%s: %f, error: %f, rel. error: %f' % (rule.__name__,I,I-exact,(I-exact)/exact))
