# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:55:49 2019

@author: Marie
"""

def legg_sammen(ledd1, ledd2):
    return ledd1 + ledd2

def maks(a, b):
    # Ta inn to tall, returner det største av dem
    if a > b:
        størst = a
    else:
        størst = b
    return størst

print(legg_sammen(1, 2))

print(maks(3, 3))