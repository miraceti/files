# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:37:14 2019

@author: eric
"""

from os import walk
listefichier =[]
for (repertoire, sousrepertoire, fichiers) in walk(monrep):
    listefichier.extend(fichiers)
    
print(listefichier)