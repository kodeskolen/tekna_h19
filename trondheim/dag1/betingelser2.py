# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:26:44 2019

@author: Marie
"""

# sjekke om tall er positivt

tall = float(input('Skriv inn et tall:'))

if tall > 0:
    print('Tallet er større enn null')
elif tall == 0:
    print('Tallet er lik null')
else:
    print('Tallet er negativt')