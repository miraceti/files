# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:33:21 2019

@author: eric
"""

from os import listdir
from os.path import isfile,join

monrep = "d:\dl"
fichiers = [f for f in listdir(monrep) if isfile(join(monrep,f))]
print(fichiers)
print("terminé1")