# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:19:18 2019

@author: Marie
"""

def midtpunkt(a, b):
    # Tar inn to tall, returnerer midtpunktet
    return (a + b)/2

maks_tall = 100
min_tall  = 0

maks_forsøk = 10

print(f'Tenk på et tall mellom {min_tall} og {maks_tall}')

for forsøk in range(1, maks_forsøk + 1):
    gjett = int(midtpunkt(min_tall, maks_tall))
    print(f'Tenker du på {gjett}?')
    
    svar = input('Var dette riktig, for høyt eller for lavt?')
    if svar == 'riktig':
        print(f'Jippi, jeg greide det på {forsøk} forsøk!')
        print(f'Jeg er en flink datamaskin!')
        break
    elif svar == 'for høyt':
        maks_tall = gjett
    elif svar == 'for lavt':
        min_tall = gjett
    else:
        print('Beep boop! Jeg skjønner ikke hva du sier!')
        print('Du må svare "for høyt", "for lavt" eller "riktig"')
else:
    print(f'Jeg brukte opp alle {maks_forsøk} forsøk')
    print(f'uten å finne nullpunktet')
    print(f'det er et sted mellom {min_tall} og {maks_tall}')