# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:51:58 2019

@author: Marie
"""

# Tar inn en radius
# Gir ut volum av kule med den radiusen

from math import pi
radius = float(input('Gi meg en radius'))
volum = (4/3)*pi*radius**3

print(f'Volumet av en kule med radius {radius} er {volum:.2f}')