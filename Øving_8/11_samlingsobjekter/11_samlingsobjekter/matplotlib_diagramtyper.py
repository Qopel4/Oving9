# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:33:41 2021

@author: Erlend Tøssebro
"""

import matplotlib.pyplot as plt
import random

karakterer = ["A", "B", "C", "D", "E", "F"]

antall = [5, 15, 40, 24, 18, 26]

# Subplot, parametere: antall rader, antall kolonner, hvilken er dette
# For den tredje så starter nummereringen på 1 og går først horisontalt
# deretter vertikalt.
plt.subplot(1, 3, 1)
plt.bar(karakterer, antall, color=("red", "orange", "yellow", "green", "blue", "magenta"))
plt.title("Karakterfordeling, stolper")

plt.subplot(1, 3, 2)
plt.pie(antall, labels=karakterer)
plt.title("Karakterfordeling, kakediagram")

plt.subplot(1, 3, 3)
verdier = []
for i in range(20000):
    verdi = random.random() + random.random() + random.random()
    verdier.append(verdi)
plt.hist(verdier, 40)
plt.title("3 tilfeldige tall")
plt.show()
