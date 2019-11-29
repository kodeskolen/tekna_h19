# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:45:46 2019

@author: Marie
"""

from math import pi

#Vi skal regne ut volum av klinkekule, tennisball
#og bowlingball

def kulevolum(kuleradius):
    # Tar inn en radius, returner tilhørende volum
    return (4/3)*pi*kuleradius**3

radius_klinkekule = 1 #cm
radius_tennisball = 2.5 #cm
radius_bowlingball = 7 #cm

volum_klinkekule = kulevolum(radius_klinkekule)
volum_tennisball = kulevolum(radius_tennisball)
volum_bowlingball = kulevolum(radius_bowlingball)


