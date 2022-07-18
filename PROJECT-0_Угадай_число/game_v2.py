"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def number_calculation(number: int = 1) -> int:
    """Фукция находит загаданное число методом бисекции

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lim_min = 1
    lim_max = 101
    
    while True:
        count += 1
        predict_number = (lim_min + lim_max) // 2  # первая итерация нахождения предполагаемого числа делением отрезка пополам
        
        if predict_number > number:
            lim_max = predict_number  # смещение верхней границы отрезка поиска числа
            
        elif predict_number < number:
            lim_min = predict_number  # смещение нижней границы отрезка поиска числа
             
        else:
            break  # выход из цикла в случае нахождения загаданного числа
    
    return count


def score_game(number_calculation) -> int:
    """За какое количство попыток в среднем за 1000 подходов функция найдет заданное число

    Args:
        number_calculation ([type]): функция нахождения заданного числа методом бисекции

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(number_calculation(number))   # формируем список с количеством попыток 

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_calculation)

