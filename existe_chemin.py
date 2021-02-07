import os.path
path = 'd:/dl'
# Vérifier si le chemin existe ou non
if os.path.exists(path) :
    print("Chemin " , path, " existe")
else:
    print("Chemin " , path, " n'existe pas")