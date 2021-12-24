import numpy as np


def binary_divination(number: int = 1) -> int:
    """ Используем бинарнй поиск
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    attempt_counter = 0   # счетчик попыток
    min_num = 1  # минимум для поиска
    max_num = 101  # максимум для поиска
    
    while True:
        attempt_counter += 1 
        divination_num = (max_num + min_num) // 2   # ищем среднее

        if number > divination_num:
            min_num = divination_num  
        elif number < divination_num:
            max_num = divination_num  
        else:
            break

    # Ваш код заканчивается здесь

    return attempt_counter

def score_game(binary_divination) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_divination(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
    # RUN
    score_game(binary_divination)