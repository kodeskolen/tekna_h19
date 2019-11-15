# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:28:33 2019

@author: Marie
"""

# Lage en tabell over tall, kvadrattal og kubikktall
# for tall fra 1 til 10

print('n | n^2 | n^3')
print('-------------')

for tall in range(1, 11):
    kvadrattall = tall**2
    kubikktall = tall**3
    print(f'{tall:2} {kvadrattall:3} {kubikktall:4}')
    