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

    >>> factorial(0) # doctest: +SKIP
    1
    >>> factorial(1) # doctest: +SKIP
    1
    >>> factorial(5) # doctest: +SKIP
    120
    >>> factorial(7) # doctest: +SKIP
    5040
    """
    # YOUR CODE HERE
    pass


def sum_digits(n):
    """
    Returns the sum of all digits in a non-negative integer n using recursion.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The sum of the digits of n.

    >>> sum_digits(0) # doctest: +SKIP
    0
    >>> sum_digits(5) # doctest: +SKIP
    5
    >>> sum_digits(123) # doctest: +SKIP
    6
    >>> sum_digits(9999) # doctest: +SKIP
    36
    """
    # YOUR CODE HERE
    pass


def reverse_string(s):
    """
    Returns the reverse of a string s using recursion.

    Parameters:
        s (str): Any string.

    Returns:
        str: The reversed string.

    >>> reverse_string("") # doctest: +SKIP
    ''
    >>> reverse_string("a") # doctest: +SKIP
    'a'
    >>> reverse_string("hello") # doctest: +SKIP
    'olleh'
    >>> reverse_string("racecar") # doctest: +SKIP
    'racecar'
    """
    # YOUR CODE HERE
    pass


def count_occurrences(lst, target):
    """
    Returns the number of times target appears in lst using recursion.
    Do NOT use the built-in list .count() method.

    Parameters:
        lst (list): A list of elements.
        target: The value to search for.

    Returns:
        int: The number of times target appears in lst.

    >>> count_occurrences([], 5) # doctest: +SKIP
    0
    >>> count_occurrences([1, 2, 3], 4) # doctest: +SKIP
    0
    >>> count_occurrences([1, 2, 2, 3, 2], 2) # doctest: +SKIP
    3
    >>> count_occurrences(["a", "b", "a", "c", "a"], "a") # doctest: +SKIP
    3
    """
    # YOUR CODE HERE
    pass


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

    >>> power(2, 0) # doctest: +SKIP
    1
    >>> power(2, 1) # doctest: +SKIP
    2
    >>> power(2, 10) # doctest: +SKIP
    1024
    >>> power(3, 4) # doctest: +SKIP
    81
    """
    # YOUR CODE HERE
    pass


def is_palindrome(s):
    """
    Returns True if the string s is a palindrome, False otherwise, using recursion.
    A palindrome reads the same forwards and backwards.
    Assume s contains only lowercase letters (no spaces or punctuation).

    Parameters:
        s (str): A string of lowercase letters.

    Returns:
        bool: True if s is a palindrome, False otherwise.

    >>> is_palindrome("") # doctest: +SKIP
    True
    >>> is_palindrome("a") # doctest: +SKIP
    True
    >>> is_palindrome("racecar") # doctest: +SKIP
    True
    >>> is_palindrome("hello") # doctest: +SKIP
    False
    >>> is_palindrome("madam") # doctest: +SKIP
    True
    """
    # YOUR CODE HERE
    pass


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

    >>> remove_duplicates([]) # doctest: +SKIP
    []
    >>> remove_duplicates([1, 2, 3]) # doctest: +SKIP
    [1, 2, 3]
    >>> remove_duplicates([1, 2, 2, 3, 1, 4]) # doctest: +SKIP
    [1, 2, 3, 4]
    >>> remove_duplicates(["a", "b", "a", "c", "b"]) # doctest: +SKIP
    ['a', 'b', 'c']
    """
    # YOUR CODE HERE
    pass


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

    >>> rotate_list([], 3) # doctest: +SKIP
    []
    >>> rotate_list([1, 2, 3, 4, 5], 0) # doctest: +SKIP
    [1, 2, 3, 4, 5]
    >>> rotate_list([1, 2, 3, 4, 5], 1) # doctest: +SKIP
    [5, 1, 2, 3, 4]
    >>> rotate_list([1, 2, 3, 4, 5], 3) # doctest: +SKIP
    [3, 4, 5, 1, 2]
    >>> rotate_list([1, 2, 3], 6) # doctest: +SKIP
    [1, 2, 3]
    """
    # YOUR CODE HERE
    pass


# ============================================================
# DICTIONARY PROBLEMS (9-10)
# ============================================================

def k_times(li: list[str], k: int) -> list[str]:
    """Return a list of items that appear exactly k times in the input list.

    >>> k_times([], 1) # doctest: +SKIP
    []
    >>> k_times(["a", "b", "c"], 1) # doctest: +SKIP
    ['a', 'b', 'c']
    >>> k_times(["a", "a", "b", "b", "c"], 2) # doctest: +SKIP
    ['a', 'b']
    >>> k_times(["a", "a", "a", "b", "b", "c"], 2) # doctest: +SKIP
    ['b']
    >>> k_times(["a", "b", "c"], 5) # doctest: +SKIP
    []
    >>> k_times(["a", "a", "a"], 3) # doctest: +SKIP
    ['a']
    """
    return

CLASSES = {"dog": "mammal", "t-rex": "reptile", "salmon": "fish",
"cat": "mammal", "godzilla": "reptile", "minnow": "fish"}

def count_by_category(li: list[str], categories: dict[str, str]) -> dict[str, int]:
    """Returns count of each category of element in li.
    If an element of li does not appear in categories, it is not counted.
    >>> count_by_category(["dog", "cat", "toaster", "minnow", "bicycle"], CLASSES) # doctest: +SKIP
    {'mammal': 2, 'fish': 1}
    >>> count_by_category(['cat', 'cat', 'cat', 'godzilla'], CLASSES) # doctest: +SKIP
    {'mammal': 3, 'reptile': 1}
    """


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)