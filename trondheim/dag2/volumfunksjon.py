# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:44:16 2019

@author: Marie
"""

# Vi skal regne ut volum av klinkekule, tennisball og bowlingball

from math import pi

def kulevolum(kuleradius):
    # Tar inn radius til en kule og regner ut volum
    return (4/3)*pi*kuleradius**3

radius_klinkekule = 1 #cm
radius_tennisball = 2.5 #cm
radius_bowlingball = 7 #cm

volum_klinkekule = kulevolum(radius_klinkekule)
volum_tennisball = kulevolum(radius_tennisball)
volum_bowlingball = kulevolum(radius_bowlingball)
