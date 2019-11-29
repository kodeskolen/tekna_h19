# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:29:20 2019

@author: Marie
"""

from pylab import arange, plot, show

# Vi skal plotte funksjonen f(x) = x^2 - 1
# fra x = 0 til x = 10

x = arange(0, 11)

y = x**2 - 1

print(x)
print(y)

plot(x, y)
show()
