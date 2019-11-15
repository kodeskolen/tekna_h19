# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:57:27 2019

@author: Marie
"""

stort_tall = 10000
print(f'{stort_tall:,}')
from math import pi

# Programmet tar inn en radius og skriver ut tilhørende volum

radius = float(input('Gi meg en radius: '))

volum = (4/3)*pi*radius**3

print(f'Volumet av en kule med radius {radius} er {volum:.2f}')

