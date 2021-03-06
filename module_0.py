import numpy as np
from statistics import mean

range_size = 100                              # Устанавливаем размер диапазона.
number = np.random.randint(1, range_size +1)  # Случайное число из диапазона.


def guess_number(secret_number):
    '''Функция реализует алгоритм поиска случайно заданного числа из заданного
    диапазона. Она необходима для проверки эффективности этого алгортма. 
    Функция принимает 1 аргумент - загаданное число, возвращает количество 
    попыток, которое и является критерием эффективности алгоритма. 
    Алгоритм: первое прогнозное значение берется из середины диапазона, далее
    прогноз изменяется в большую или меньшую сторону в зависимости от того 
    больше загаданное число прогноза или меньше. Шаг изменения прогноза 
    уменьшается вдвое  с каждой итерацией, что позволяет каждый раз вдвое 
    уменьшать диапазон, в котором находится загаданное число .'''
    
    count = 1                         # Счетчик = 1, первая попытка вне цикла.
    predict = range_size // 2         # Первый прогноз из середины диапазона. 
    step = predict                    # Шаг равен половине диапазона.                   
                                      
    while secret_number != predict:   # Убеждаемся, что не угадали. 
        count += 1
        step -= step // 2             # Шаг изменения уменьшаем вдвое
        if secret_number > predict:
            predict += step           # Прогноз меньше, увеличиваем его на шаг.    
        elif secret_number < predict:
            predict -= step           # Прогноз больше, уменьшаем его на шаг.
            
    print(f"Вы угадали число {secret_number} за {count} попыток.")        
    return count


def function_quality(func):
    '''Функция определяет эффективность работы АЛГОРИТМА ПОИСКА ЗАГАДАННОГО 
    ЧИСЛА. В качестве аргумента принимает функцию реализующую такой алгоритм. 
    Возвращает максимальное и среднее количество попыток необходимое алгоритму
    для определения загаданного числа. Функция запускает алгоритм для каждого 
    числа из указанного диапазона и собирает их в список.'''
    
    count_list = list(map(func, range(1, range_size + 1))) 
    count_mean = mean(count_list)
    count_max = max(count_list)
    
    print(f"""Ваш алгоритм угадывает число максимум за {count_max} попыток,
    а его средняя эффективность {count_mean} попыток""")
    return count_max, count_mean


function_quality(guess_number)


"""Вывод: алгоритм поиска загаданного числа реализованный в функции 
guess_number гораздо эффективнее алгоритма случайных попыток и алгоритма 
последовательного перебора каждого числа начиная с первого в заданном 
диапазоне."""
