from os import listdir
from os.path import isfile, join
monRepertoire = "d:\dl"
fichiers = [f for f in listdir(monRepertoire) if isfile(join(monRepertoire, f))]
print(fichiers)