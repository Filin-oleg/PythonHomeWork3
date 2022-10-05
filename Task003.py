# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


import random


def fill_list(n: int, border_min: int, border_max: int) -> list:
    if border_min < border_max:
        min, max = border_min, border_max
    else:
        min, max = border_max, border_min
    list = [round(random.randint(min, max) + random.random(), 5)]
    for i in range(1, n):
        list.append(round(random.randint(min, max) + random.random(), 5))
        i += 1
    return list


def difference_fractional(list) -> float:
    min = max = list[0] % 1
    for i in range(1, len(list)):
        if list[i] % 1 < min:
            min = list[i] % 1
        elif list[i] % 1 > max:
            max = list[i] % 1
        else:
            continue
    diff = round(max - min, 5)
    return diff


n = int(input(" Введите количество элементов списка: "))
border_min = int(input("Введите нижнюю границу значений элементов списка: "))
border_max = int(input(" Введите верхнюю границу значений элементов списка: "))
list = fill_list(n, border_min, border_max)
diff = difference_fractional(list)
print(f"{list}")
print(f"Разница между максимальным и минимальным значением дробной части элементов = {diff};")
