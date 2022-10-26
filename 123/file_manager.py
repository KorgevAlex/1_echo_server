import os
import shutil
from distutils.dir_util import copy_tree


class FileManager:
    def __init__(self):
        with open('path.txt', 'r') as path:
            self.home = str(f'{path.readline()}')
            print(self.home)
            os.chdir(self.home)
        self.path_length = len(self.home.split('/'))

    def menu(self):
        while True:
            print('Содержимое текущей папки: ')
            print()
            files = str(os.listdir(path='.')).replace('[', '').replace(']', '').replace("""'""", '')
            print(files)

            menu ="""
    1. Создание папки
    2. Удаление папки по имени
    3. Перемещение между папками
    4. Создание пустых файлов с указанием имени
    5. Запись текста в файл
    6. Просмотр содержимого текстового файла
    7. Удаление файлов по имени
    8. Копирование файлов из одной папки в другую
    9. Перемещение файлов
    10. Переименование файлов
    11. Перемещение вверх по директории
    12. Выход из программы
    """
            print(menu)

            choice = str(input("Выберите действие: "))
            if choice == '1':
                self.make_folder()
            elif choice == '2':
                self.delete_folder()
            elif choice == '3':
                self.change_folder()
            elif choice == '4':
                self.create_file()
            elif choice == '5':
                self.export_text()
            elif choice == '6':
                self.open_file()
            elif choice == '7':
                self.remove_file()
            elif choice == '8':
                self.copy_files()
            elif choice == '9':
                self.move_files()
            elif choice == '10':
                self.rename_file()
            elif choice == '11':
                self.move_up()
            elif choice == '12':
                break
            else:
                print("Неправильный ввод! Попробуйте снова.")

    def make_folder(self):
        folder_name = str(input("Введите название папки: "))
        try:
            if '/' in folder_name:
                print('Ошибка! Вы указали путь, а не название папки.')
            else:
                os.mkdir(folder_name)
        except FileExistsError:
            print("Такая папка уже существует!")

    def delete_folder(self):
        folder_name = str(input("Введите название папки: "))
        try:
            if '/' in folder_name:
                print('Ошибка! Вы указали путь, а не название папки.')
            else:
                os.rmdir(folder_name)
        except FileNotFoundError:
            print("Такой папки не существует!")

    def change_folder(self):
        next_folder = str(input("Введите название папки: "))
        move = str(self.home) + str(f'/{next_folder}')
        try:
            os.path.isdir(move)
            self.home += str(f'/{next_folder}')
            os.chdir(self.home)
            print("Переход выполнен")
        except FileNotFoundError:
            print("Такой папки не существует!")
        except OSError as e:
            print(f'{e.filename} - {e.strerror}')

    def create_file(self):
        file_name = str(input("Введите название файла (вместе с расширением): "))
        try:
            if not os.path.exists(f'{file_name}'):
                new_file = open(f'{file_name}', "w")
                new_file.close()
            else:
                print('Такой файл уже существует! ')
        except OSError as e:
            print(f'{e.filename} - {e.strerror}')

    def export_text(self):
        file_name = str(input("Введите название файла (вместе с расширением): "))
        try:
            with open(f'{file_name}', "w") as f:
                f.write(str(input("Введите текст для записи: ")))
                f.close()
                print("Текст записан")
        except FileNotFoundError:
            print("Файл не найден!")
        except OSError as e:
            print(f'{e.filename} - {e.strerror}')

    def open_file(self):
        file_name = str(input("Введите название файла (вместе с расширением): "))
        try:
            with open(f'{file_name}', "r") as f:
                read = f.read()
                for i in read.splitlines():
                    print(i)
        except FileNotFoundError:
            print("Файл не найден!")
        except OSError as e:
            print(f'{e.filename} - {e.strerror}')

    def remove_file(self):
        file_name = str(input("Введите название файла (вместе с расширением): "))
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("Файл не найден!")
        except OSError as e:
            print(f'{e.filename} - {e.strerror}')

    def copy_files(self):
        first_folder = str(input("Введите название папки, которую требуется скопировать: "))
        second_folder = str(input("Введите название папки, в которую требуется скопировать файлы: "))
        start_path = f"{self.home}/{first_folder}"
        new_path = f"{self.home}/{second_folder}"
        try:
            copy_tree(start_path, new_path)
        except OSError as e:
            print(f'Ошибка: {e.filename} - {e.strerror}')
        else:
            print('Успешное копирование')

    def move_files(self):
        first_folder = str(input("Введите название папки, которую требуется скопировать: "))
        second_folder = str(input("Введите название папки, в которую требуется скопировать файлы: "))
        start_path = f"{self.home}/{first_folder}"
        new_path = f"{self.home}/{second_folder}"
        try:
            shutil.move(start_path, new_path)
        except OSError as e:
            print(f'Ошибка: {e.filename} - {e.strerror}')
        else:
            print('Успешное перемещение')

    def rename_file(self):
        old_file_name = str(input("Введите название файла (с расширением): "))
        new_file_name = str(input("Введите новое название файла (с расширением): "))
        try:
            os.rename(old_file_name, new_file_name)
        except FileNotFoundError:
            print("Файл не найден!")
        except OSError as e:
            print(f'Ошибка: {e.filename} - {e.strerror}')
        else:
            print("Файл переименован")

    def move_up(self):
        current_folder = self.home.split('/')
        if self.path_length < len(current_folder):
            current_folder.pop()
            up = '/'.join(current_folder)
            self.home = up
            os.chdir(self.home)
            print("Успешный переход")
        else:
            print("Ошибка доступа!")

def main():
    execute = FileManager()
    execute.menu()

if __name__ == '__main__':
    main()