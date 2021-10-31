import os

print(os.getcwd())

os.unlink('d:\\temp2\\t1.txt')

os.rmdir('d:\\temp2')  #uniquement si dossier vide

os.rmtree('d:\\temp2') #supprime tout le ontenu du dossier même si il y a des fichiers dedans

#module send2trash
import send2trash
send2trash.send2trash('d:\\temp2\\t1.txt')
