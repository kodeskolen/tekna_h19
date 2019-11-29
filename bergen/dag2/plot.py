# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:32:42 2019

@author: Marie
"""

from pylab import arange, plot, show, grid

# Vi skal plotte funksjonen f(x) = x^2-1
# for x fra 0 til 10

x = arange(0, 11)

y = x**2 - 1
print(x)
print(y)
plot(x, y, 'o-')
grid()
show()