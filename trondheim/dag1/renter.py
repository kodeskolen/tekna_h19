# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:48:55 2019

@author: Marie
"""

# Erik setter inn 10 000 kroner på BSU med 3,45% rente
# Hvor mye penger har Erik etter 10 år?

penger = 10000
rente_vekst = 1.0345
antall_år = 1000

for år in range(1, antall_år + 1):
    penger *= rente_vekst
    print(f'Etter {år} år er {penger:,.2f} kr.')