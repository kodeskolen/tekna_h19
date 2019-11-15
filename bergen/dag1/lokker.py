# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:28:43 2019

@author: Marie
"""
# Skrive ut tabell med tall, tall^2, tall^3
# for tall fra 1 til 100
tall_header = 'tall'
kvadrattall_header = 'kvadrattall'
kubikktall_header = 'kubikktall'

print(f'{tall_header:4}|{kvadrattall_header:12}|{kubikktall_header:12}')
for tall in range(1, 101):
    kvadrattall = tall**2
    kubikktall = tall**3
    print(f'{tall:4} {kvadrattall:12} {kubikktall:12}')