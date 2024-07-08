import time
from functools import lru_cache

CACHE_FACTORIAL = {}


# @lru_cache()
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     if n in CACHE_FACTORIAL:
#         return CACHE_FACTORIAL[n]
#     print(f"Вычисление факториала для числа {n}...")
#     time.sleep(3)
#     result = n * factorial(n - 1)
#     CACHE_FACTORIAL[n] = result
#     return result
#
#
# number = 5
# print(f"Факториал числа {number}: {factorial(number)}")
# print(f"Факториал числа {number} (из кэша): {factorial(number)}")
# print(f"Результат - {CACHE_FACTORIAL}")


@lru_cache(maxsize=None)
def sum_positive_recursive(nums):
    if not nums:
        return 0
    else:
        head, *tail = nums
        if head > 0:
            return head + sum_positive_recursive(tuple(tail))
        else:
            return sum_positive_recursive(tuple(tail))


numbers = [1, -2, 3, 4, -5, 6, 7]

print(f"Сумма положительных чисел в списке {numbers}: {sum_positive_recursive(tuple(numbers))}")
print(f"Сумма положительных чисел в списке {numbers} (из кэша): {sum_positive_recursive(tuple(numbers))}")
