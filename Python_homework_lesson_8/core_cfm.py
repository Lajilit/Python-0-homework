import os
import shutil
import datetime
import random


def list_folder(folders_only=False):
    result = [folder for folder in os.listdir() if os.path.isdir(folder)] if folders_only else os.listdir()
    # result = os.listdir()
    # if folders_only:
    #     result = [folder for folder in result if os.path.isdir(folder)]
    for r in result:
        if os.path.isdir(r):
            print(f'   {r}')
    print('__________')
    for r in result:
        if not os.path.isdir(r):
            print(f'   {r}')


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(f'Папка с именем "{name}" уже существует')


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as file:
        if text:
            file.write(text)


def delete_f(name):
    try:
        os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    except FileNotFoundError:
        print(f'Имя "{name}" не найдено')


def copy_f(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print(f'Папка с именем "{new_name}" уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


def current_dir():
    result = os.getcwd()
    print(result)


def change_dir(name):
    if os.path.exists(name) and os.path.isdir(name):
        os.chdir(name)
    else:
        print('Некорректный путь')


def game():
    a = 1  # min number
    b = 100  # max number
    print(f'Давай поиграем? Загадай число от {a} до {b}, а я его угадаю.\n'
          f'Когда загадаешь, нажми "Enter"')
    input()
    print('Если твоё число больше моего, пиши ">".\n'
          'Если твоё число меньше моего, пиши "<".\n'
          'Если я угадал, напиши "="')

    answer = None
    number = None
    while answer != '=':
        try:
            number = random.randint(a, b)
        except ValueError:
            print('Что-то здесь не так... Кажется, ты забыла загаданное '
                  'число. Поиграем в другой раз')
            break
        else:
            #    print(f'от {a} до {b}')
            print(f'Ты загадала число {number}?')
            answer = input()
            if answer == '>':
                print(f'Больше, чем {number}? Попробую ещё раз.')
                a = number + 1
            elif answer == '<':
                print(f'Меньше, чем {number}? Хм, нужно подумать.')
                b = number - 1
    else:
        print(f'Это правда {number}? Ура, я угадал!!!')

if __name__ == '__main__':
    create_folder('test')
    create_file('new_file.txt', 'text1')
    delete_f('name3')
    copy_f('new_file.txt', 'new_file1.txt')
    save_info('message')
    list_folder()
    change_dir('test')
    game()
