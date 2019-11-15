# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:35:24 2019

@author: Marie
"""

# Vi skal lage en gjettelek
# Vi tenker på et tall mellom 0 og 100
# Brukeren får et gitt antall forsøk til å gjette tallet
# Vi sier om tallet er for stort eller for lite
# Spillet er over når brukeren gjetter rett eller har gått
# tom for forsøk

from random import randint

fasit = randint(0,100)

maks_forsøk = 10

for forsøk in range(1, maks_forsøk+1):
    gjett = float(input('Gjett et tall mellom 0 og 100'))
    if gjett == fasit:
        print('Du klarte det! Gratulerer!')
        break
    elif gjett > fasit:
        print('Det var for høyt')
    else:
        print('Det var for lavt')
    print(f'Du har nå brukt {forsøk} forsøk')
else:
    print(f'Du har brukt opp dine {maks_forsøk} forsøk')
    print('Game over!!!')
    print(f'Rett svar var {fasit}')