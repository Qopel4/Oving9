# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:36:04 2021

@author: Erlend Tøssebro
"""

import numpy as np

# Lager en numpy array med 5 0-ere
nullere = np.zeros(5)

# En for-loop med steglengde 0.1
for i in np.arange(1, 5, 0.1):
    print(f"{i:5.2f}")

# Lager en numpy array med 4 elementer. Det første er 1,
# det siste er 10, og de to mellom er jevnt spredd mellom
# 1 og 10
test = np.linspace(1, 10, 4)
for element in test:
    print(test)

# Lager en numpy array fra ei liste
oddetall = np.array([1, 3, 5, 7, 9])
 
# Lager ei liste fra en numpy array
liste = list(test)

# Kan lage matrise med å oppgi et tuppel til np.zeros. Ekseplet
# lager en 4x3 matrise
matrise = np.zeros((4, 3))

# Lan lage en matrise fra ei liste av lister så lenge
# de indre listene alle er like lange
matrise2 = np.array([[1, 2, 3], [2, 2, 2], [3, 2, 1]])

