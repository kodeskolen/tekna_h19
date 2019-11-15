# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:55:28 2019

@author: Marie
"""

# Erik setter inn 10 000 kroner på BSU med 3,45% rente
# Hvor mye penger har Erik etter 10 år?

penger = 10000
rente_veksten = 1.0345

antall_år = 10

for år in range(1, antall_år + 1):
    penger *= rente_veksten
    print(f'Etter {år} år er det {penger:.2f} kr.')