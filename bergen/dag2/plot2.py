# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:39:23 2019

@author: Marie
"""

from pylab import *

x = arange(0, 10, 0.1)


y1 = sin(x)
y2 = cos(x)

print(x)
print(y1)
print(y2)

plot(x, y1)
show()
figure()

plot(x, y2)
xlim(0, 9.9)
xlabel('Tid')
ylabel('Høyde')
title('Posisjon til pendel som funksjon av tid')
show()