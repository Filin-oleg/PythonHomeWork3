#Напишите программу, которая будет преобразовывать десятичное число в двоичное.


def input_number(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не натуральное число! Повторите ввод")
    return number


def descimal_to_binary(k: int) -> str:
    bin_k = f'{k % 2}'
    while k // 2 != 0:
        k = k // 2
        bin_k = f'{k % 2}' + bin_k
    bin_k = int(bin_k)
    return bin_k

descimal_number = input_number("Введите натуральное число: ")
binary_number = descimal_to_binary(descimal_number)
print(f"Введенное Вами десятичное число {descimal_number} в двоичном формате => {binary_number}")