# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:20:15 2019

@author: Marie
"""

maks_forsøk = 10
min_tall = 0
maks_tall = 100

def midtpunkt(a, b):
    # Tar inn to tall, returner midtpunktet
    return (a + b)/2

print(f'Tenk på et tall mellom {min_tall} og {maks_tall}')

for forsøk in range(1, maks_forsøk + 1):
    gjett = int(midtpunkt(min_tall, maks_tall))
    print(f'Tenker du på {gjett}?')
    
    svar = input('Var dette for høyt, for lavt eller riktig?')
    if svar == 'riktig':
        print(f'Jippi! Jeg greide det på {forsøk} forsøk!')
        break
    elif svar == 'for høyt':
        maks_tall = gjett
    elif svar == 'for lavt':
        min_tall = gjett
    else:
        print('Beep boop! Jeg skjønner ingenting!')
        print('Du må skrive "riktig", "for høyt" eller "for lavt"')
else: 
    print('Jeg fikk det ikke til :(')
    print(f'Svaret ligger mellom {min_tall} og {maks_tall}')