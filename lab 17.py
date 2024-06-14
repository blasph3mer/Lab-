import itertools
import math

# Task 1: Number Generator
def number_generator(numbers):
    for number in numbers:
        yield number

# Task 2: Even Number Generator
def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# Task 3: Odd Number Generator
def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

# Task 4: Fibonacci Generator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5: Prime Number Generator
def prime_number_generator(limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# Task 6: Pre-order Traversal of a Binary Tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

# Task 7: In-order Traversal of a Binary Tree
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

# Task 8: Post-order Traversal of a Binary Tree
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

# Task 9: DFS Traversal of a Graph
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

# Task 10: BFS Traversal of a Graph
def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])

# Task 11: Dictionary Keys Generator
def dict_keys_generator(d):
    for key in d.keys():
        yield key

# Task 12: Dictionary Values Generator
def dict_values_generator(d):
    for value in d.values():
        yield value

# Task 13: Dictionary Items Generator
def dict_items_generator(d):
    for item in d.items():
        yield item

# Task 14: File Lines Generator
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 15: File Words Generator
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16: String Characters Generator
def string_chars_generator(s):
    for char in s:
        yield char

# Task 17: Unique Elements Generator
def unique_elements_generator(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem

# Task 18: Reverse List Generator
def reverse_list_generator(lst):
    for elem in reversed(lst):
        yield elem

# Task 19: Cartesian Product Generator
def cartesian_product_generator(lst1, lst2):
    for elem1 in lst1:
        for elem2 in lst2:
            yield (elem1, elem2)

# Task 20: Permutations Generator
def permutations_generator(lst):
    for perm in itertools.permutations(lst):
        yield perm

# Task 21: Combinations Generator
def combinations_generator(lst):
    for r in range(1, len(lst) + 1):
        for comb in itertools.combinations(lst, r):
            yield comb

# Task 22: Tuple List Generator
def tuple_list_generator(lst):
    for tup in lst:
        yield tup

# Task 23: Parallel Lists Generator
def parallel_lists_generator(*lists):
    for elems in zip(*lists):
        yield elems

# Task 24: Flatten List Generator
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

# Task 25: Nested Dictionary Generator
def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

# Task 26: Powers of Two Generator
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

# Task 27: Powers of Base Generator
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Task 28: Squares Generator
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

# Task 29: Cubes Generator
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

# Task 30: Factorials Generator
def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)

# Task 31: Collatz Sequence Generator
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

# Task 32: Geometric Progression Generator
def geometric_progression_generator(initial, ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= ratio

# Task 33: Arithmetic Progression Generator
def arithmetic_progression_generator(initial, difference, limit):
    term = initial
    while term <= limit:
        yield term
        term += difference

# Task 34: Running Sum Generator
def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

# Task 35: Running Product Generator
def running_product_generator(numbers):
    total = 1
    for number in numbers:
        total *= number
        yield total
