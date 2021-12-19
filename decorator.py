import logging
import time


def timer(func):
    """Выводит время выполнения декорируемой функции"""
    def wrapper_time(n):
        logging.basicConfig(filename="decorator.log",
                            level=logging.INFO, format='%(asctime)s s:%(message)s')
        logging.info(f"Program started ")
        start_time = time.time()
        func(n)
        logging.info(
            f"Program End! --- {(time.time() - start_time)} seconds ---")
    return wrapper_time


def slow_wodn(func):
    """Перед вызовом ждет 2 секунды"""
    def wrapper_down(n):
        time.sleep(2)
        func(n)
    return wrapper_down


@slow_wodn
@timer
def resheto_eratosfena(n: int):
    """Выводит все простые числа  <=n"""
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    print(*list(filter(lambda x: x != 0, numbers)))
    

resheto_eratosfena(100)
