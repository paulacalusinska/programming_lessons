import os
path = 'nowy.py'
print(os.path.isdir(path))

def listdir_if_dir(path):
    if os.path.isdir(path):
        print(os.listdir(path))
    else:
        print(f'Path {path} is not directory')
listdir_if_dir(path)

# wypisać wszystkie pliki z katalogu w kolejnosci alfabetycznej
def listdir_in_order(path):
    if os.path.isdir(path):
        print(sorted(os.listdir(path)))
    else:
        print(f'Path {path} is not directory')

# czy to co jest wewnatrz katalogu to plik czy katalog

dirs = os.listdir(path)
for file in dirs:
    print(os.path.isdir(file))

# wypisujemy tez wszystko co jest wewnatrz katalogow

dirs2 = os.listdir(path)
for file in dirs2:
    if os.path.isdir(file):
        print(os.listdir(file))
    else:
        print(file)