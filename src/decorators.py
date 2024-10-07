import functools
import logging


def log(filename=None):
    """
    Декоратор log, который  автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """
    if filename:
        logging.basicConfig(
            filename=filename, level=logging.INFO, format="%(asctime)s - %(message)s", encoding="utf-8"
        )
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Начало выполнения функции: {func.__name__}, Inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"Функция {func.__name__} завершена успешно, Результат: {result}")
                return result
            except Exception as e:
                logging.error(
                    f"Функция {func.__name__} завершилась с ошибкой: {type(e).__name__}, Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper

    return decorator


"""Пример использования декоратора"""


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)


# Пример функции, которая вызывает ошибку
@log()
def faulty_function(x, y):
    return x / y


# Вызываем faulty_function для проверки логирования ошибки
try:
    faulty_function(1, 0)
except ZeroDivisionError:
    pass
