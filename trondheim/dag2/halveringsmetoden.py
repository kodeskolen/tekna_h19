# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:43:15 2019

@author: Marie
"""
from pylab import log, sign

def f(x):
    return -((x/100)**5 - 0.1*log((x + 1)/100) - 0.5)
    
def midtpunkt(a, b):
    return (a + b)/2

min_tall = 0
maks_tall = 100

maks_forsøk = 100

feil_terskel = 0.000000000000001

for forsøk in range(1, maks_forsøk + 1):
    gjett = midtpunkt(min_tall, maks_tall)
    print(f'Jeg gjetter {gjett}')
    
    if abs(f(gjett)) < feil_terskel:
        print(f'Jippi! jeg greide det på {forsøk} forsøk!')
        print(f'Jeg er en flink datamaskin!')
        print(f'f({gjett}) = {f(gjett)}')
        break
    elif sign(f(gjett)) == sign(f(maks_tall)):
        maks_tall = gjett
    else:
        min_tall = gjett
else:
    print(f'Jeg brukte opp alle {maks_forsøk} forsøk')
    print(f'nullpunktet er et sted mellom {min_tall} og {maks_tall}')
    