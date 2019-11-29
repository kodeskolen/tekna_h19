# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:43:32 2019

@author: Marie
"""
from pylab import log, sign

def f(x):
    return -((x/100)**5 - 0.1*log((x + 1)/100) - 0.5)

def midtpunkt(a, b):
    return (a+b)/2

maks_tall = 100
min_tall = 0

maks_forsøk = 100

feilterskel = 0.00000000001

for forsøk in range(1, maks_forsøk+1):
    gjett = midtpunkt(min_tall, maks_tall)
    print(f'Jeg gjetter {gjett}')
    
    if abs(f(gjett)) < feilterskel:
        print(f'Jippi, jeg greide det på {forsøk} forsøk')
        print(f'f({gjett}) = {f(gjett)}')
        break
    elif sign(f(gjett)) == sign(f(maks_tall)):
        maks_tall = gjett
    else:
        min_tall = gjett
else:
    print(f'Jeg brukte opp alle {maks_forsøk} forsøk')
    print(f'Nullpunktet er et sted mellom {min_tall} og {maks_tall}')
    