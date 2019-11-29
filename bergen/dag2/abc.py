# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:14:52 2019

@author: Marie
"""

# Oppgave 9

from math import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

diskriminant = b**2 - 4*a*c

if diskriminant < 0:
    print(f'{a}x^2 + {b}x + c = 0 har dessverre ingen reelle løsninger')
elif diskriminant == 0:
    løsning = -b/(2*a)
    print(f'{a}x^2 + {b}x + c = 0 har løsningen {løsning}')
else:
    løsning1 = (-b  + sqrt(diskriminant))/(2*a)
    løsning2 = (-b  - sqrt(diskriminant))/(2*a)
    
    print(f'Løsningene for likningen {a}x^2 + {b}x + {c} = 0')
    print(f'er {løsning1} og {løsning2}')





