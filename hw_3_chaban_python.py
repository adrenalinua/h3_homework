def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = list(filter(lambda x: '/catalog/' in x, url_list))
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    a = len(input_str)
    if a % 2 == 0:
        output_str = input_str[a//2-1:a//2+1]
    else:
        output_str = input_str[a//2-1:a//2+2]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = {}
    for element in input_str:
        output_dict[element] = input_str.count(element)
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    a = len(str1)//2
    result_str = str1[:a] + str2 + str1[a:]
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    a = [i for i in range(101)]
    even_int_list = []
    for i in a:
        if i % 2 == 0:
            even_int_list.append(i)
    return even_int_list


if __name__ == '__main__':
    url_list = ['/home/ubuntu18/PycharmProjects/project1/src/',
                '/home/ubuntu18/PycharmProjects/catalog/src/',
                '/home/ubuntu18/PycharmProjects/project1/catalog/',
                '/home/ubuntu18/catalog2/']
    input_str = '/home/ubuntu18/catalog/'
    str1 = 'aaaaaaaa'
    str2 = 'bbbbbbbb'
    key = input('1) Дописать функцию, которая принимает список URL,'
                'а возвращает список только тех URL, в которых есть /catalog/\n'
                '2) Дописать функцию, которая вернет Х символов из середины строки'
                '(2 для четного кол-ва символов, 3 - для нечетного).\n'
                '3) Дописать функцию, которая считает сколько раз каждая из букв '
                'встречается в строке, разложить буквы в словарь парами'
                '{буква:количество упоминаний в строке}\n'
                '4) Дописать функцию, которая будет принимать 2 строки и вставлять вторую'
                'в середину первой\n'
                '5) Сгенерировать список из диапазона чисел от 0 до 100 и записать'
                'в результирующий список только четные числа.\n''\n'' = \n')
    while True:
        if key == '1':
            print(f" HW_1: {catalog_finder(url_list)}.")
        elif key == '2':
            print(f" HW_2: {get_str_center(input_str)}")
        elif key == '3':
            print(f" HW_3: {count_symbols(input_str)}")
        elif key == '4':
            print(f" HW_4: {mix_strings(str1, str2)}")
        elif key == '5':
            print(f" HW_5: {even_int_generator()}")
        break
