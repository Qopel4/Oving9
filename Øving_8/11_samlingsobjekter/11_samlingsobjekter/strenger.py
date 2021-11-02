# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:54:47 2021

@author: Erlend Tøssebro
"""

streng = "En tekst med noen ord"

#Splitetr strengen i dens enkelte ord
splittet_streng = streng.split()

# Viser arbeidsflyten i norn filer
streng2 = "    verdi1;verdi2;verdi3;\n"

# Kan fjerne whitespace fra starten og slutten med strip()
strippet_streng = streng2.strip()

# Kan bruke strip for å fjerne andre tegn ved å oppgi tegnet
# som parameter.
strippet_streng = strippet_streng.strip(";")

# Kan splitte på et annet tegn enn whitespace
komponenter = strippet_streng.split(";")

for element in komponenter:
    print(element)
