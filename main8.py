import shutil
import os
import send2trash
import zipfile

# 1
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.ulink(filename) - видаляє файл, який знаходиться по вказаному шляху
        # os.rmdir(filename) - видаляє папку, яка знаходиться по назначеному шляху. Папка повинна бути порожня
        # shutil.rmtree(filename) - видаляє папку разом із її вмістом, яка знаходить по назначеному шляху
        print(filename)

# 2
baconFile = open('bacon.txt', 'a') # створює файл
baconFile.write('Bacon isn`t vegateble')
baconFile.close()
send2trash.send2trash('bacon.txt')

# 3
for folderName, subfolders, filenames, in os.walk('E:\\delicious'):
    print('Поточна папка - ' + folderName)

    for subfolder in subfolders:
        print('Підпапка папки ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('Файл в папці ' + folderName + ': ' + filename)

    print(' ')

# 4
os.chdir('E:\\')
exampleZip = zipfile.ZipFile('ll.zip')
an = exampleZip.namelist()

print(an)

spamInfo = exampleZip.getinfo('dfdsf_nn.txt')
al = spamInfo.file_size

print(al)

am = spamInfo.compress_size

print(am)

ag = f'Зжатий файл в {round(spamInfo.file_size/spamInfo.compress_size, 2)} менше'

print(ag)

exampleZip.close()