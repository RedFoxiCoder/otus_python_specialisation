"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x**2 for x in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
  if n == 0 or n == 1:
     return False
  elif n>1:
   for i in range(2,n):
            if (n%i) == 0:
               return False
   return True

def filter_numbers(lst: list, num_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if num_type == 'odd':
       return [x for x in lst if x%2 !=0]
    elif num_type == 'even':
       return [x for x in lst if x%2 ==0]
    elif num_type == 'prime':
       return list(filter(is_prime, lst))
    
print(filter_numbers([0, 1, 2, 3, 5, 7, 11], EVEN))
print(filter_numbers([0, 1, 2, 3, 5, 7, 11], ODD))
print(filter_numbers([0, 1, 2, 3, 5, 7, 11], PRIME))


