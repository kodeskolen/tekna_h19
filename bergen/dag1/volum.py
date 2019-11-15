# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:34:29 2019

@author: Marie
"""

# Finn volum av kule med radius 1.1 cm
# (4/3)*pi*r^3

from math import pi

radius = 1.1 #cm

volum = (4/3)*pi*radius**3

print(f'Volumet av en kule med radius {radius} er {volum:.1f}')