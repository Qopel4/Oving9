# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:57:34 2021

@author: Erlend Tøssebro
"""

import matplotlib.pyplot as plt
import numpy as np

x_koordinater = np.linspace(0, 10, 11)
y_koordinater = x_koordinater ** 2
y_koordinater2 = x_koordinater * 2

plt.plot(x_koordinater, y_koordinater, "o-", label="x i andre")
plt.plot(x_koordinater, y_koordinater2, "o-", label="2*x")
plt.title("Enkle figurer")
plt.xlabel("Verdi")
plt.ylabel("Resultat")
plt.legend()
plt.grid(True)
# plt.savefig("flere_figurer.pdf")
plt.show()
