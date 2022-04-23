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
# czy to co jest wewnatrz katalogu to plik czy katalog
# wypisujemy tez wszystko co jest wewnatrz katalogow