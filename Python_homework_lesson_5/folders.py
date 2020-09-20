# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os

def create_dir():
    for i in range (1,10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(new_path)

def remove_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.rmdir(new_path)

if __name__ == '__main__':
    create_dir()
    print(os.listdir())
    remove_dir()
