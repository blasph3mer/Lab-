# Task 1: Sum of Squares
def task1(nums):
    return sum(x**2 for x in nums)


# Task 2: Filter and Sum
def task2(nums):
    avg = sum(nums) / len(nums)
    return sum(x for x in nums if x >= avg)


# Task 3: Sort by Frequency
def task3(nums):
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    return sorted(nums, key=lambda x: (-freq_dict[x], x))


# Task 4: Find Missing Number
def task4(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)


# Task 5: Longest Consecutive Sequence
def task5(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


# Task 6: Rotate Array
def task6(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


# Task 7: Array of Products
def task7(nums):
    result = []
    product = 1
    for num in nums:
        result.append(product)
        product *= num
    product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= product
        product *= nums[i]
    return result


# Task 8: Maximum Subarray Sum
def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Task 9: Spiral Order Matrix
def task9(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


# Task 10: K Closest Points to Origin
def task10(points, k):
    return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
