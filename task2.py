import math

def convert_types(_data: list):
    data = _data.copy()
    for i in range(len(data)):
        if isinstance(data[i], str):
            try:
                data[i] = float(data[i])
            except ValueError:
                continue
        else:
            try:
                data[i] = str(data[i])
            except ValueError:
                continue
    return data

def swap_values(a, b):
    a, b = b, a
    return a, b

def bool_transformation(value=False):
    if value:
        return True
    else:
        return False

def compound_operations(a, b):
    result_list = []
    result_list.append(a+b)
    result_list.append(a - b)
    result_list.append(a*b)
    result_list.append(a / b)
    result_list.append(a % b)
    result_list.append(a ** b)
    return result_list

def check_type(a, _type):
    try:
        if isinstance(a, _type):
            return True
    except TypeError:
        if type(a).__name__ == _type:
            return True
        else:
            return False


def logical_and(a, b):
    if a:
        if b:
            return True
    return False

def logical_or(a, b, c):
    if a:
        return True
    if b:
        return True
    if c:
        return True
    return False

def between(value, low, high,):
    if low < value <= high:
        return True
    return False

def print_even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
    return ""

def countdown_while(n):
    while n >= 1:
        print(n)
        n -= 1
    return ""

def skip_multiplies(n, multiplier):
    for i in range(1, n+1):
        if i % multiplier == 0:
            continue
        else:
            print(i)
    return ""

def if_elif_else_chain(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"


def abs_value(x):
    return math.sqrt(x**2)

def binary_representation(n:int):
    res = ""
    if n == 0:
        return 0
    while n > 0:
        res += str(n % 2)
        n //= 2
    return int(res[::-1])

def custom_round(number, ndigits):
    number = str(number)
    stuff = False
    res = ''
    for x in number:
        res += x
        if stuff:
            ndigits -= 1
        if ndigits == 0:
            return float(res)
        if x in [".", ","]:
            stuff = True
    return float(number)


def find_max_min(_list):
    max = None
    min = None
    for x in _list:
        if max == None:
            max = x
        if min == None:
            min = x
        if x < min:
            min = x
        if x > max:
            max = x
    return max, min


def all_true(_list):
    for x in _list:
        if not x:
            return False
    return True

def any_true(_list):
    for x in _list:
        if x:
            return True
    return False

def custom_enumerate(sequence, start=0):
    res = []
    num = start
    for i in range(start, len(sequence)):
        res.append((num, sequence[i]))
        num+=1
    return res

def custom_filter(func, iterable):
    res = []
    for x in iterable:
        if func(x):
            res.append(x)
    return res

def custom_map(func, iterable):
    res = []
    for x in iterable:
        res.append(func(x))
    return res


def custom_zip(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        item1 = list1[i] if i < len(list1) else None
        item2 = list2[i] if i < len(list2) else None
        result.append((item1, item2))
    return result

def custom_reversed(sequence):
    res = []
    for i in range(len(sequence)-1, -1, -1):
        res.append(sequence[i])
    return res

def custom_sorted(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def custom_sum(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

def count_vowels(text):
    counter = 0
    for x in text:
        if x.lower() in ["a", "e", "i", "o", "u"]:
            counter += 1
    return counter

def power(base, exp):
    res = base
    if exp == 0:
        return 1
    for _ in range(exp-1):
        res *= base
    return res

def is_prime(n):
    half = n // 2
    for i in range(2, half+1):
        if n%i==0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibichi(n):
    a, b = 0, 1
    i = 2
    if n == 0:
        return 0
    while i <= n:
        a, b = b, a + b
        i += 1
    return b


print(f"Convert_types: {convert_types([1, "2", "hello", 3.5])}")
print(f"Swap_values: {swap_values(1, 3.5)}")
print(f"bool_transformation: {bool_transformation(5)}")
print(f"Compound_operations: {compound_operations(2, 3)}")
print(f"Check_type: {check_type(True, "bool")}")
print(f"logical_and: {logical_and(False, True)}")
print(f"logical_or: {logical_or(False, True, False)}")
print(f"between: {between(3.5, 1, 3.5)}")
print(f"print_even_numbers: {print_even_numbers(10)}")
print(f"countdown_while: {countdown_while(3)}")
print(f"skip_multiplies: {skip_multiplies(10, 3)}")
print(f"if_elif_else_chain: {if_elif_else_chain(3)}")
print(f"abs_value: {abs_value(-3.5)}")
print(f"binary_representation: {binary_representation(0)}")
print(f"custom_round: {custom_round(3.504242401, 5)}")
print(f"find_max_min: {find_max_min([3, 7, 1, 9, 2])}")
print(f"all_true: {all_true([3, 7, 1, 9, 2])}")
print(f"any_true: {any_true([False, None, 0, 0])}")
print(f"custom_enumerate: {custom_enumerate([3, 7, 1, 9, 2])}")
print(f"custom_filter: { custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])}")
print(f"custom_map: { custom_map(lambda x: x * 2, [1, 2, 3, 4, 5])}")
print(f"custom_zip: { custom_zip([1, 2, 3, 4, 5], ["a", "b", "c"])}")
print(f"custom_reversed: { custom_reversed([1, 2, 3, 4, 5])}")
print(f"custom_sorted: { custom_sorted([1, 2, 3, 5, 4])}")
print(f"custom_sum: { custom_sum([1, 2, 3, 5, 4])}")
print(f"count_vowels: {count_vowels('hello')}")
print(f"pow: {power(2, 3)}")
print(f"is_prime: {is_prime(10)}")
print(f"factorial: {factorial(10)}")
print(f"fibichi: {fibichi(10)}")


