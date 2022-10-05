# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fibonacci_list(number: int) -> list:
    fib_list = [-1, 1, 0, 1, 1]
    for i in range(3, number+1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        fib_list.insert(0, fib_list[1] - fib_list[0])
    return fib_list


number = 0
while number < 2:
    number = int(input("Введите натуральное число, большее 2: "))
    if number < 2:
        print("Ошибка ввода! Повторите ввод")
fib_list = fibonacci_list(number)
print(fib_list)
