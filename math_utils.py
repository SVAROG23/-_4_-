def add_numbers(a, b):
    "Складывает два числа."
    return a + b

def divide_numbers(a, b):
    "Делит a на b. Если b равно нулю, вызывает ошибку."
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b
