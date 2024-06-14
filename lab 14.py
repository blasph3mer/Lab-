# Task 1: Основні операції з логічними значеннями
def check_truth(a, b, c):
    # Повертає результат виразу (a and b) або c
    return (a and b) or c

# Task 2: Логічна еквівалентність
def logical_equivalence(a, b):
    # Повертає True, якщо a дорівнює b
    return a == b

# Task 3: Виключне або (XOR)
def xor(a, b):
    # Повертає True, якщо рівно один з аргументів True
    return a != b

# Task 4: Умовне вітання
def greet(condition):
    # Повертає привітання на основі умови
    return "Hello, World!" if condition else "Goodbye, World!"

# Task 5: Вкладені умови
def nested_condition(x, y, z):
    # Повертає "All same" якщо всі три числа рівні
    if x == y == z:
        return "All same"
    # Повертає "All different" якщо всі числа різні
    elif x != y and x != z and y != z:
        return "All different"
    # Повертає "Neither" в інших випадках
    else:
        return "Neither"

# Task 6: Лічильник True
def count_true(bool_list):
    # Повертає кількість значень True у списку
    return bool_list.count(True)

# Task 7: Парність бінарного представлення
def parity(n):
    # Підраховує кількість одиниць у бінарному поданні
    binary_representation = bin(n)[2:]  # Перетворюємо число в бінарний вигляд
    count_ones = binary_representation.count('1')
    # Повертає True, якщо кількість одиниць парна
    return count_ones % 2 == 0

# Task 8: Голосування більшості
def majority_vote(a, b, c):
    # Перевіряє, чи більше половини значень True
    return sum([a, b, c]) > 1

# Task 9: Перемикач логічного значення
def switch(value):
    # Повертає протилежне значення
    return not value

# Task 10: Імітація тернарного оператора
def ternary_check(condition, true_value, false_value):
    # Повертає true_value, якщо умова виконується, і false_value, якщо ні
    return true_value if condition else false_value

# Task 11: Перевірка комбінації
def validate(x, y, z):
    # Повертає True, якщо x True або y і z True
    return x or (y and z)

# Task 12: Ланцюжок умов
def chain_check(a, b, c):
    # Повертає "Increasing", якщо числа у строго зростаючому порядку
    if a < b < c:
        return "Increasing"
    # Повертає "Decreasing", якщо числа у строго спадному порядку
    elif a > b > c:
        return "Decreasing"
    # Повертає "Neither" в інших випадках
    else:
        return "Neither"

# Task 13: Фільтрація True значень
def filter_true(bool_list):
    # Повертає новий список з тільки True значень
    return [value for value in bool_list if value]

# Task 14: Умовний мультиплексор
def multiplexer(a, b, c, n):
    # Повертає подвоєне значення n, якщо a True
    if a:
        return n * 2
    # Повертає потроєне значення n, якщо b True
    elif b:
        return n * 3
    # Повертає n - 5, якщо c True
    elif c:
        return n - 5
    # Повертає n без змін, якщо жоден з перших трьох не True
    else:
        return n

# Приклади використання функцій

print(check_truth(True, False, True))  
print(logical_equivalence(True, True))  
print(xor(True, False))  
print(greet(True))  
print(nested_condition(3, 3, 3))  
print(count_true([True, False, True, False, True]))  
print(parity(3))  
print(majority_vote(True, True, False))  
print(switch(True))  
print(ternary_check(True, "Yes", "No"))  
print(validate(True, False, True))  
print(chain_check(1, 2, 3))  
print(filter_true([True, False, True, False]))  
print(multiplexer(False, False, True, 10))  
