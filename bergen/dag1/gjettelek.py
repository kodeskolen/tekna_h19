# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:41:03 2019

@author: Marie
"""

# Vi skal lage en gjettelek
# Vi tenker på et tall mellom 0 og 100
# Brukeren får 10 gjett 
# Vi ser om det er for stort eller for lite
# spillet er over når brukeren har gjettet rett
# eller når brukeren er tom for forsøk

from random import randint
fasit = randint(0, 100)

maks_forsøk = 10

for forsøk in range(1, maks_forsøk+1):
    gjett = float(input('Gjett et tall mellom 0 og 100: '))
    
    if gjett == fasit:
        print('Du klarte det! Gratulerer!')
        break
    elif gjett > fasit:
        print('Det er for høyt')
    else:
        print('Det er for lavt')
else:
    print(f'Du har brukt opp dine {maks_forsøk} forsøk! GAME OVER!!!!')
    print(f'Svaret var {fasit}')
        
        