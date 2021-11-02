# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:17:32 2021

@author: Erlend Tøssebro
"""

mengde1 = set()
mengde1.add("Henrik")
mengde1.add("Nils")
mengde1.add("Olav")
mengde1.add("Anders")
mengde1.add("Henrik")

mengde1.add("Åsmund")

for element in mengde1:
    print(element)
print("\n Mengde 2: ")
mengde2 = set()
mengde2.add("Nils")
mengde2.add("Andreas")
mengde2.add("Tomas")
mengde2.add("Olav")
mengde2.add("Mads")
for element in mengde2:
    print(element)


# Mengden av alle som er med i minst en av de to
m3 = mengde1.union(mengde2)
print("\n Union: ")
for element in m3:
    print(element)

m3 = mengde1.intersection(mengde2)
print("\n Snitt: ")
for element in m3:
    print(element)

m3 = mengde1.difference(mengde2)
print("\n m1 minus m2: ")
for element in m3:
    print(element)
