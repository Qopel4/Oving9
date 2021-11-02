# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:03:56 2021

@author: Erlend Tøssebro
"""


def endrer_liste(liste):
    liste.append(10)
    liste.append(12)
    liste = [3, 4, 5]
    print(liste)


if __name__ == "__main__":
    liste1 = [2, 4, 6, 8]
    print(liste1)
    endrer_liste(liste1)
    print(liste1)
