from typing import List, Generator, Tuple, Dict, Any
import re
import statistics

# Завдання 1: Інтерполяція(математичний метод, який використовується для оцінки значень функції у проміжках між відомими даними.) відсутніх значень
def interpolate_missing(values: List[float]) -> List[float]:
    if not values:
        return values
    
    n = len(values)
    for i in range(n):
        if values[i] is None:
            left = right = i
            # Знаходимо найближче значення, що не дорівнює None, зліва
            while left >= 0 and values[left] is None:
                left -= 1
            # Знаходимо найближче значення, що не дорівнює None, справа
            while right < n and values[right] is None:
                right += 1
            
            if left >= 0 and right < n:
                # Інтерполюемо між лівим і правим значенням
                values[i] = (values[left] + values[right]) / 2
            elif left >= 0:
                # Доступне лише ліве значення
                values[i] = values[left]
            elif right < n:
                # Доступне лише праве значення
                values[i] = values[right]
    return values

# Завдання 2: Генератор ряду Фібоначчі
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Завдання 3: Обробка пакетів даних
def process_batches(data: List[int], batch_size: int) -> List[int]:
    max_values = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        max_values.append(max(batch))
    return max_values

# Завдання 4: Кодування та декодування рядків
def encode_string(s: str) -> str:
    encoded = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded.append(f"{count}{s[i - 1]}")
            else:
                encoded.append(s[i - 1])
            count = 1
    return ''.join(encoded)

def decode_string(s: str) -> str:
    decoded = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = int(s[i])
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
                count = count * 10 + int(s[i])
            i += 1
            decoded.append(s[i] * count)
        else:
            decoded.append(s[i])
        i += 1
    return ''.join(decoded)

# Завдання 5: Поворот матриці
def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated

# Завдання 6: Пошук за регулярним виразом
def regex_search(strings: List[str], pattern: str) -> List[str]:
    regex = re.compile(pattern)
    return [s for s in strings if regex.search(s)]

# Завдання 7: Злиття відсортованих масивів
def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Завдання 8: Перевірка числа на простоту
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Завдання 9: Групування за ключем
def group_by_key(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Any]]:
    grouped = {}
    for d in data:
        k = d[key]
        v = d.get('value', None)
        if k not in grouped:
            grouped[k] = []
        grouped[k].append(v)
    return grouped

# Завдання 10: Видалення викидів
def remove_outliers(data: List[int]) -> List[int]:
    if len(data) < 2:
        return data
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    return [x for x in data if lower_bound <= x <= upper_bound]

# Приклади
print(interpolate_missing([1, None, None, 4]))  
print([num for num in fibonacci(5)])  
print(process_batches([1, 2, 3, 4, 5, 6], 2))  
encoded = encode_string("aaabbc")
print(encoded)  
print(decode_string(encoded))  
matrix = [
    [1, 2],
    [3, 4]
]
print(rotate_matrix(matrix))  
print(regex_search(["test", "test123", "none"], "test\d+")) 
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  
print(is_prime(11))  
data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))  
print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))  
