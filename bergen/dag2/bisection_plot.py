# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 06:35:24 2019

@author: Marie
"""
 
from pylab import *

def f(x):
    return (x/100)**5 - 0.1 * log((x + 1)/100) - 0.5

def g(x):
    return -f(x)

def midtpunkt(a, b):
    return (a+b)/2

maks_tall = 100
min_tall = 0

maks_forsøk = 100
feilterskel = 0.001

x = arange(0, 100)
y = g(x)

for forsøk in range(1, maks_forsøk+1):
    gjett = midtpunkt(min_tall, maks_tall)
    print(f'Jeg gjetter {gjett}!')
   
    cla()
    plot(x, y)
    axhline(0, color='k')
    axvline(min_tall, color='orange', linestyle='--')
    axvline(maks_tall, color='orange', linestyle='--')
    plot(gjett, g(gjett), 'ro')
    title(f'Gjett nr: {forsøk}')
    savefig(f'bisection_{forsøk}.png')
    pause(1)

    if abs(g(gjett)) < feilterskel:
        print(f'Jippi, jeg greide det på {forsøk} forsøk, f({gjett})={f(gjett)}!')
        break
    elif sign(g(gjett)) == sign(g(maks_tall)):
        maks_tall = gjett
    else:
        min_tall = gjett
else:
    print(f'Jeg brukte opp alle {maks_forsøk} forsøk uten å finne nullpunktet')
   