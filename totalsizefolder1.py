import os

def folderSize(folder):
    totalsize = 0
    for filename in os.listdir(folder):
        if not os.path.isfile(os.path.join(folder, filename)):
            continue
        totalsize = totalsize + os.path.getsize(os.path.join(folder, filename))
    return totalsize

folder = 'D:\\dl'
sizefolder = folderSize(folder)
print(f'{sizefolder:,}')