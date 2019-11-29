# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:35:46 2019

@author: Marie
"""
from pylab import *

x = arange(0, 8, 0.1)
y1 = sin(x)
y2 = cos(x)

print(x)
print(y1)

plot(x, y1, label='pendel1')
plot(x, y2, label='pendel2')
plot(1, sin(1), 'ro', label='sin(1)')

xlim(0, 7.9)
xlabel('Tid')
ylabel('Høyde')
title('Posisjon til pendel som funksjon av tid')
legend()
show()