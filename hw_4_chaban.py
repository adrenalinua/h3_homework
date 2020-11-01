def validate_password(val_symb, val_even_letter, val_odd_degit):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    str_list = ['Password']
    if val_symb is True:
        pass
    else:
        str_list.append('Cодержит запрещенные символы')
    if val_even_letter is False:
        pass
    else:
        str_list.append('Cодержит нечетное количество букв')
    if val_odd_degit is True:
        pass
    else:
        str_list.append('Содержит четное количество цифр')
    print(str_list)
    return bool(str_list == ['Password'])


def _validate_symbols(input_str):
    """   Проверяет строку на наличие запрещенных символов
    Подсказка: у строк есть метод, проверяющий наличие только був и цифр
    Возвращает True\False
    """
    validate_symbols = input_str.isalnum()
    return validate_symbols


def _validate_letters_even(input_str):
    """
    Проверяет строку на четное количество букв
    Возвращает True\False
    """
    num_letters = len([i for i in input_str if i.isalpha()])
    return bool(num_letters % 2)


def _validate_numbers_odd(input_str):
    """
    Проверяет строку на нечетное количество цифр
    Возвращает True\False
    """
    num_digit = len([i for i in input_str if i.isdigit()])
    return bool(num_digit % 2)


if __name__ == '__main__':
    input_str = 'aa555'
    val_symb = _validate_symbols(input_str)
    val_even_letter = _validate_letters_even(input_str)
    val_odd_digit = _validate_numbers_odd(input_str)
    print(validate_password(val_symb, val_even_letter, val_odd_digit))
