# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import math
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


def product_pairs(list) -> list:
    new_list = []
    for i in range(0, math.ceil(len(list)/2)):
        new_list.append(list[i]*list[-i - 1])
    return new_list


n = int(input(" Введите количество элементов списка: "))
border_min = int(input("Введите нижнюю границу значений элементов списка: "))
border_max = int(input(" Введите верхнюю границу значений элементов списка: "))
list = fill_list(n, border_min, border_max)
product = product_pairs(list)
print(f'{list} => {product};')
