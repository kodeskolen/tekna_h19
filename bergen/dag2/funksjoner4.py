# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 17:57:49 2019

@author: Marie
"""

def maks(a, b):
    # Tar inn to tall, returner det høyeste
    if a > b:
        størst = a
    else:
        størst = b
    return størst

print(maks(-1, 3))