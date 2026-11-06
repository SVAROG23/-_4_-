import pytest
from math_utils import add_numbers, divide_numbers

# Тест 1: Проверяем правильность сложения
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

# Тест 2: Проверяем правильность деления
def test_divide_numbers():
    assert divide_numbers(10, 2) == 5.0
# Тест 3: Проверяем, что при делении на ноль программа выдает нужную ошибку
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)

