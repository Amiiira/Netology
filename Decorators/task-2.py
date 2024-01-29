'''
Доработать параметризованный декоратор logger в коде ниже. 
Должен получиться декоратор, который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. 
Путь к файлу должен передаваться в аргументах декоратора. 
Функция test_2 в коде ниже также должна отработать без ошибок.
'''

import os
from functools import wraps
import datetime


def timecheck(format_date_time="%Y/%m/%d"):
    def logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            start = start.strftime(format_date_time)

            with open(new_function.log_path, 'a', encoding="utf8") as file:
                file.write(f"\n Дата и время вызова: {start}\n имя функции: {old_function.__name__}\n аргументы: {args}, {kwargs}\n возвращаемое значение: {result}\n")
            
            return result
        
        return new_function

    return logger

def path_setter(path):
    def decorator(old_function):
        old_function.log_path = path
        return old_function
    return decorator


def test_2():
    paths = ('Decorators/log_1.log', 'Decorators/log_2.log', 'Decorators/log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @path_setter(path)
        @timecheck(format_date_time='%Y-%m-%d %H:%M:%S')
        def hello_world():
            return 'Hello World'

        @path_setter(path)
        @timecheck(format_date_time='%Y-%m-%d %H:%M:%S')
        def summator(a, b=0):
            return a + b

        @path_setter(path)
        @timecheck(format_date_time='%Y-%m-%d %H:%M:%S')
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'

    print('Test passed')


if __name__ == '__main__':
    test_2()
