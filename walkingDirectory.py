import os
import shutil

for foldername, subfolders, filenames in os.walk('d:\\temp2'):
    print("f1 : ", foldername)
    print("sf2 : ", subfolders)
    print("files : ", filenames)
    print()

    for subfolder in subfolders:
        print(subfolder)
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for filename in filenames:
        print(filename)
        if filename.endswith('.py'):
            shutil.copy(os.join(foldername, filename),
                        os.join(foldername, filename + '.bak'))
