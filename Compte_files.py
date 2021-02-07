import fnmatch
import os

pth = "C:\Windows"
print(len(fnmatch.filter(os.listdir(pth), "*")))