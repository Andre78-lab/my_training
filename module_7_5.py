import os
import time

print(os.getcwd())
directory = os.getcwd()
#directory = os.path.dirname(directory)

for root, dirs, files in os.walk(directory):
    # перебрать каталоги
    for dirname in dirs:
        dirpath = os.path.join(root, dirname)
        dirtime = os.path.getmtime(dirpath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(dirtime))
        parent_dir = os.path.dirname(dirpath)
        print(f'Каталог: {dirpath}, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    # перебрать файлы
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

