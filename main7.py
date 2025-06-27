# 1
import os

path1 = os.path.join('user', 'bin', 'spam')

print(path1)

# 2
my_files = ['nik.txt', 'wat.csv', 'main.py']

for name_files in my_files:
    print(os.path.join('C:\\User\\documents', name_files))

# 3
my_cwd = os.getcwd() # подивитись cwd - current working directory, поточний робочий каталог
print(my_cwd)

change_cwd = os.chdir('C:\\Windows\\System32') # змінюємо cwd
my_cwd = change_cwd
print(my_cwd)

# 4
#my_new_folder = os.makedirs('C:\\delicious\\recipes\\dish') # створюємо папки(каталоги) на Диску С за допомогою команди os.makedirs('C:\\delicious\\recipes\\dish')

# 5
absp = os.path.abspath('path') # повертає рядок абсолютного шляху аргумента. Простий спосіб перетворення відносного шляху в абсолютний.
print (absp)

absp1 = os.path.abspath('.')
print(absp1)

isabs = os.path.isabs('path') # Перевіряє чи є рядок абсолютним шляхом аргумента
print(isabs)

isabs1 = os.path.isabs(os.path.abspath('path'))
print(isabs1)

rlp = os.path.realpath('C:\\Windows') # розв'язує символічні посилання та повертає повний шлях.
print(rlp)

# 6
path2 = 'C:\\Windows\\User\\Food\\Recipes\\recipes.docx'
srch = os.path.basename(path2) # повертає рядок, який містить в собі всю частину шляху, яка йде після останньої '\' в аргументі path
print(srch)

srch1 = os.path.dirname(path2) # повертає рядок, який містить в собі всю частину шляху, яка йде попереду останньої '\' в аргументі path
print(srch1)

srch2 = os.path.split(path2) # повертає і базове ім'я, і ім'я папки 
print(srch2)

srch3 = (os.path.dirname(path2), os.path.basename(path2)) # те саме, що і split()
print(srch3)

srch4 = path2.split(os.path.sep) # повертає саме списком
print(srch4)

# 7
size = os.path.getsize('C:\\Windows\\System32') # виводить значення, яке виводить значення про те, який розмір займає папка(каталог) або програма на компі
print(size)

lists = os.listdir('C:\\Windows\\System32') # виводить список всіх файлів 
print(lists)

# 8

totalSize = 0
for filenames in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filenames))
print(totalSize)

# 9
check =  os.path.exists('C:\\Windows\\System32') # перевіряє існування файлу чи папки
print(check)

check1 = os.path.isfile('C:\\hh_uu') # перевіряє існування файлу
print(check1)

check2 = os.path.isdir("E:\\уроки") # перевіряє існування папки
print(check2)

# 10
hello_file = open('D:\\hello.txt', 'r') # відкриває файл для читання
# print(hello_file.read()) - використовується для читання файлу в рядокому значені
print(hello_file.readlines()) # використовується для читання файлу по рядкам, створюючи список
hello_file.close() # закриває файл

new_file = open('D:\\www.txt', 'w') # відкриває файл для переписування файлу з нуля
new_file1 = open('D:\\nnn.txt', 'a') # відкриває файл для додавання об'єктів в файд

new_file.write('\nHello World!')
print(new_file)

new_file.close()

new_file1.write('an')
print(new_file1)

new_file1.close()

# 11
# import shelve
# shelf_file = shelve.open('D:\\mydata')
# cats = ['Simon', 'Steve', 'Robert']
# shelf_file['cats'] = cats
# shelf_file.close()

# 12
import pprint
my_cats = [{'cat': 'Steve', 'weight': '10kg'}, {'cat': 'Robert', 'weight': '8kg'}]
pprint.pformat(my_cats)

file_obj = open('E:\\projects\\book\\myCats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(my_cats) + '\n')
file_obj.close()

# 13
import myCats

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['cat'])

# 14
