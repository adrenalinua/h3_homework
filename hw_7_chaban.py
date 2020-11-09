import os

# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test string" в "<i><b>test string</b></i>"

# def str_to_html(tags):
#     def decorator(func):
#         tag_base = {
#             "italic": f"<i>%text%</i>",
#             "bold": f"<b>%text%</b>",
#             "underline": f"<u>%text%</u>",
#         }
#         def wrapper(text):
#             # your code here
#         return wrapper
#     return decorator
#
#
# @str_to_html(["italic", "bold"])
# def get_text(text):
#     return text


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных


def log_reading_decorator(func):
    def log_reading_func(*args):
        file_log_list = [file for file in func(*args) if '.log' in file]
        for file in file_log_list:
            path_file = os.path.join(*args, file)
            open_file = open(path_file, 'r')
            print(f'{file} \n {open_file.read()}')
    return log_reading_func


@log_reading_decorator
def get_files(get_path):
    file_list = os.listdir(get_path)
    return file_list


get_path = '/home/ubuntu18/PycharmProjects/project1/src/Py_Basic/hw8pic/'
get_files(get_path)
