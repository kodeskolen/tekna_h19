# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:37:50 2019

@author: Marie
"""

# Vi skal regne volum av en kule med radius 1.1cm
# volum: (4/3)pi r^3

from math import pi

radius = 1.1 #cm

volum = (4/3)*pi*radius**3

print(f'Volumet av en kule med radius {radius} er {volum:.0f}')