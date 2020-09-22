import sys
from core_cfm import list_folder, create_folder, create_file, delete_f, \
    copy_f, save_info, current_dir, change_dir, game


command = None
save_info('Старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствует команда для выполнения')
else:
    if command == 'list':
        list_folder()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
            text = input('Введите текст для записи в файл: ')
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name, text)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete_f':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            if name == 'main.py' or name == 'core_cfm.py' or name == 'log.txt':
                print('Файл защищён')
            else:
                delete_f(name)
    elif command == 'copy_f':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести имя файла/папки и имя копии')
        else:
            copy_f(name, new_name)
    elif command == 'help':
        print('list - список папок и файлов')
        print('create_file - создание нового файла')
        print('create_folder - создание новой папки')
        print('delete_f - удаление файла или папки')
        print('copy_f - копирование файла или папки')
        print('change_dir - смена текущей директории')
        print('game - игра "Угадай число "наоборот"')
    elif command == 'change_dir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указана директория')
        else:
            change_dir(name)
            current_dir()
    elif command == 'game':
        game()
    else:
        print('Неизвестная команда')


save_info('Конец')
