import re

# Task 1:
def task1(input_string):
    regex_pattern = r'^[a-z0-9]+$'
    return bool(re.match(regex_pattern, input_string))

# Task 2:
def task2(input_string):
    regex_pattern = r'[A-Z]'
    return bool(re.search(regex_pattern, input_string))

# Task 3:
def task3(input_string):
    regex_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(regex_pattern, input_string))

# Task 4:
def task4(input_string):
    regex_pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(regex_pattern, input_string))

# Task 5:
def task5(input_string):
    regex_pattern = r'^\d{5}(?:-\d{4})?$'
    return bool(re.match(regex_pattern, input_string))

# Task 6:
def task6(input_string):
    regex_pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(regex_pattern, input_string))

# Task 7:
def task7(input_string):
    regex_pattern = r'^(?:4|5|6)(?:\d{3}-?){3}\d{3,4}$'
    return bool(re.match(regex_pattern, input_string.replace('-', '')))

# Task 8:
def task8(input_string):
    regex_pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(regex_pattern, input_string))

# Task 9:
def task9(input_string):
    regex_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(regex_pattern, input_string))

# Task 10:
def task10(input_string):
    regex_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(regex_pattern, input_string))
