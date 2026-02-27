# ============================================================
# RECURSION PROBLEMS (1-6)
# ============================================================

def factorial(n):
    """
    Returns the factorial of a non-negative integer n using recursion.
    The factorial of n is defined as n * (n-1) * ... * 1, and factorial(0) = 1.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_digits(n):
    """
    Returns the sum of all digits in a non-negative integer n using recursion.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The sum of the digits of n.

    >>> sum_digits(0)
    0
    >>> sum_digits(5)
    5
    >>> sum_digits(123)
    6
    >>> sum_digits(9999)
    36
    """
    if n < 10:
        return n
    
    digit = n % 10
    new_n = n // 10
    return digit + sum_digits(new_n)


def reverse_string(s):
    """
    Returns the reverse of a string s using recursion.

    Parameters:
        s (str): Any string.

    Returns:
        str: The reversed string.

    >>> reverse_string("")
    ''
    >>> reverse_string("a")
    'a'
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("racecar")
    'racecar'
    """
    if len(s) <= 1:
        return s
    last_char = s[-1]
    new_s = s[:-1]
    return last_char + reverse_string(new_s)


def count_occurrences(lst, target):
    """
    Returns the number of times target appears in lst using recursion.
    Do NOT use the built-in list .count() method.

    Parameters:
        lst (list): A list of elements.
        target: The value to search for.

    Returns:
        int: The number of times target appears in lst.

    >>> count_occurrences([], 5)
    0
    >>> count_occurrences([1, 2, 3], 4)
    0
    >>> count_occurrences([1, 2, 2, 3, 2], 2)
    3
    >>> count_occurrences(["a", "b", "a", "c", "a"], "a")
    3
    """
    if len(lst) == 0:
        return 0
    new_lst = lst[1:]
    if lst[0] == target:
        return 1 + count_occurrences(new_lst, target)
    else:
        return count_occurrences(new_lst, target)


def power(base, exp):
    """
    Returns base raised to the power of exp using recursion.
    Assume exp is a non-negative integer.
    Do NOT use the ** operator or the built-in pow() function.

    Parameters:
        base (int or float): The base number.
        exp (int): A non-negative integer exponent.

    Returns:
        int or float: base raised to the power of exp.

    >>> power(2, 0)
    1
    >>> power(2, 1)
    2
    >>> power(2, 10)
    1024
    >>> power(3, 4)
    81
    """
    if exp == 0:
        return 1
    new_exp = exp - 1
    return base * power(base, new_exp)


def is_palindrome(s):
    """
    Returns True if the string s is a palindrome, False otherwise, using recursion.
    A palindrome reads the same forwards and backwards.
    Assume s contains only lowercase letters (no spaces or punctuation).

    Parameters:
        s (str): A string of lowercase letters.

    Returns:
        bool: True if s is a palindrome, False otherwise.

    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("madam")
    True
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    new_s = s[1:-1]
    return is_palindrome(new_s)


# ============================================================
# LIST PROBLEMS (7-8)
# ============================================================

def remove_duplicates(lst):
    """
    Returns a new list with all duplicate values removed, keeping only the
    first occurrence of each element. The original list should not be modified.

    Parameters:
        lst (list): A list of elements.

    Returns:
        list: A new list with duplicates removed, preserving original order.

    >>> remove_duplicates([])
    []
    >>> remove_duplicates([1, 2, 3])
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates(["a", "b", "a", "c", "b"])
    ['a', 'b', 'c']
    """
    no_dups = []
    for el in lst:
        if el not in no_dups:
            no_dups.append(el)
    return no_dups


def rotate_list(lst, k):
    """
    Returns a new list that is the original list rotated to the right by k positions.
    Rotating right by 1 moves the last element to the front.
    The original list should not be modified.

    Parameters:
        lst (list): A list of elements.
        k (int): A non-negative integer number of positions to rotate.

    Returns:
        list: A new list rotated to the right by k positions.

    >>> rotate_list([], 3)
    []
    >>> rotate_list([1, 2, 3, 4, 5], 0)
    [1, 2, 3, 4, 5]
    >>> rotate_list([1, 2, 3, 4, 5], 1)
    [5, 1, 2, 3, 4]
    >>> rotate_list([1, 2, 3, 4, 5], 3)
    [3, 4, 5, 1, 2]
    >>> rotate_list([1, 2, 3], 6)
    [1, 2, 3]
    """
    length = len(lst)
    rotated = [0 for i in range(length)]
    for i in range(length):
        new_index = (i + k) % length
        rotated[new_index] = lst[i]
    return rotated


# ============================================================
# DICTIONARY PROBLEMS (9-10)
# ============================================================

def k_times(li: list[str], k: int) -> list[str]:
    """Return a list of items that appear exactly k times in the input list.

    >>> k_times([], 1)
    []
    >>> k_times(["a", "b", "c"], 1)
    ['a', 'b', 'c']
    >>> k_times(["a", "a", "b", "b", "c"], 2)
    ['a', 'b']
    >>> k_times(["a", "a", "a", "b", "b", "c"], 2)
    ['b']
    >>> k_times(["a", "b", "c"], 5)
    []
    >>> k_times(["a", "a", "a"], 3)
    ['a']
    """
    new_list = []
    count_dict = {}
    for el in li:
        if el in count_dict:
            count_dict[el] += 1
        else:
            count_dict[el] = 1
    
    for el in count_dict.keys():
        if count_dict[el] == k:
            new_list.append(el)
    return new_list

CLASSES = {"dog": "mammal", "t-rex": "reptile", "salmon": "fish",
"cat": "mammal", "godzilla": "reptile", "minnow": "fish"}

def count_by_category(li: list[str], categories: dict[str, str]) -> dict[str, int]:
    """Returns count of each category of element in li.
    If an element of li does not appear in categories, it is not counted.

    >>> count_by_category(["dog", "cat", "toaster", "minnow", "bicycle"], CLASSES)
    {'mammal': 2, 'fish': 1}
    >>> count_by_category(['cat', 'cat', 'cat', 'godzilla'], CLASSES)
    {'mammal': 3, 'reptile': 1}
    """
    count_dict = {}

    for animal in li: 
        if animal in categories:
            animal_category = categories[animal]
            if animal_category in count_dict:
                count_dict[animal_category] += 1
            else:
                count_dict[animal_category] = 1
    return count_dict


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)