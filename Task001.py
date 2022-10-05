# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random


def fill_list(n: int, border_min: int, border_max: int) -> list:
    if border_min < border_max:
        min, max = border_min, border_max
    else:
        min, max = border_max, border_min
    list = [random.randint(min, max)]
    for i in range(1, n):
        list.append(random.randint(min, max))
        i += 1
    return list


def sum_odd_position(user_list) -> int:
    sum_odd = 0
    for i in range(1, len(user_list)):
        if i % 2 != 0:
            sum_odd += user_list[i]
    return sum_odd


# Если условием задачи под нечетными позициями понимать нужно позиции не индексов элеметов, а сами элементы
# списка, то функция будет выглядеть так.


# def sum_odd_position(user_list) -> int:
#    sum_odd = 0
#    for i in range(0, len(user_list)):
#        if i % 2 == 0:
#            sum_odd += user_list[i]
#    return sum_odd


n = int(input(" Введите количество элементов списка: "))
border_min = int(input("Введите нижнюю границу значений элементов списка: "))
border_max = int(input(" Введите верхнюю границу значений элементов списка: "))
list = fill_list(n, border_min, border_max)
sum_odd = sum_odd_position(list)
print(f"Сумма элементов списка {list}, стоящих на нечётной позиции = {sum_odd};")