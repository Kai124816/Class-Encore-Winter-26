import doctest

# ============================================================
# RECURSION PROBLEMS (1-4)
# ============================================================

# Problem 1
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    The Fibonacci sequence is defined as:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    >>> fibonacci(0) # doctest: +SKIP
    0
    >>> fibonacci(1) # doctest: +SKIP
    1
    >>> fibonacci(6) # doctest: +SKIP
    8
    >>> fibonacci(10) # doctest: +SKIP
    55
    """
    # YOUR CODE HERE
    pass

# Problem 2
def count_vowels(s):
    """
    Returns the number of vowels (a, e, i, o, u) in the string s using recursion.
    Assume s contains only lowercase letters.
    Do NOT use a loop.

    Parameters:
        s (str): A string of lowercase letters.

    Returns:
        int: The number of vowels in s.

    >>> count_vowels("") # doctest: +SKIP
    0
    >>> count_vowels("rhythm") # doctest: +SKIP
    0
    >>> count_vowels("hello") # doctest: +SKIP
    2
    >>> count_vowels("aeiou") # doctest: +SKIP
    5
    >>> count_vowels("programming") # doctest: +SKIP
    3
    """
    # YOUR CODE HERE
    pass

# Problem 3
def flatten(lst):
    """
    Returns a new flat list containing all the integers in a nested list using recursion.
    The input may contain integers or other lists (which may themselves be nested).

    Parameters:
        lst (list): A possibly nested list of integers and lists.

    Returns:
        list: A flat list of all integers in lst, in order.

    >>> flatten([]) # doctest: +SKIP
    []
    >>> flatten([1, 2, 3]) # doctest: +SKIP
    [1, 2, 3]
    >>> flatten([1, [2, 3], 4]) # doctest: +SKIP
    [1, 2, 3, 4]
    >>> flatten([[1, [2]], [3, [4, [5]]]]) # doctest: +SKIP
    [1, 2, 3, 4, 5]
    """
    # YOUR CODE HERE
    pass

# Problem 4
YUM = "y"
POISON = "p"
def safe_to_eat(food) -> bool:
    """True if there is NO poison in food.
    food may be either a str or a list of foods
    >>> safe_to_eat([]) # doctest: +SKIP
    True
    >>> safe_to_eat([YUM, [[[[POISON]]]]]) # doctest: +SKIP
    False
    >>> safe_to_eat([[YUM, YUM], YUM, YUM]) # doctest: +SKIP
    True
    >>> safe_to_eat([[YUM, POISON], YUM, YUM]) # doctest: +SKIP
    False
    """
    pass

# ============================================================
# LIST PROBLEMS (5-7)
# ============================================================

# Problem 5
def second_largest(lst: list[int]) -> int:
    """
    Returns the second largest unique value in a list of integers.
    You may assume the list has at least two distinct values.
    Do NOT use sort() or sorted().

    Parameters:
        lst (list): A list of integers with at least two distinct values.

    Returns:
        int: The second largest unique value in lst.

    >>> second_largest([1, 2]) # doctest: +SKIP
    1
    >>> second_largest([3, 1, 4, 1, 5, 9, 2, 6]) # doctest: +SKIP
    6
    >>> second_largest([10, 10, 9, 8]) # doctest: +SKIP
    9
    >>> second_largest([-1, -5, -3]) # doctest: +SKIP
    -3
    """
    # YOUR CODE HERE
    pass

# Problem 6
def zip_lists(lst1: list, lst2: list) -> list:
    """
    Takes two lists and returns a list of tuples pairing elements at the same index.
    If the lists are different lengths, stop at the shorter one.
    Do NOT use the built-in zip() function.

    Parameters:
        lst1 (list): A list of elements.
        lst2 (list): A list of elements.

    Returns:
        list: A list of (element_from_lst1, element_from_lst2) tuples.

    >>> zip_lists([], []) # doctest: +SKIP
    []
    >>> zip_lists([1, 2, 3], []) # doctest: +SKIP
    []
    >>> zip_lists([1, 2, 3], ["a", "b", "c"]) # doctest: +SKIP
    [(1, 'a'), (2, 'b'), (3, 'c')]
    >>> zip_lists([1, 2], ["a", "b", "c", "d"]) # doctest: +SKIP
    [(1, 'a'), (2, 'b')]
    """
    # YOUR CODE HERE
    pass

# Problem 7
def chunk_list(lst:list, size:int) -> list[list]:
    """
    Splits a list into consecutive chunks of a given size.
    The last chunk may be smaller if the list doesn't divide evenly.
    The original list should not be modified.

    Parameters:
        lst (list): A list of elements.
        size (int): A positive integer chunk size.

    Returns:
        list: A list of lists, each of length `size` (except possibly the last).

    >>> chunk_list([], 3) # doctest: +SKIP
    []
    >>> chunk_list([1, 2, 3, 4, 5], 2) # doctest: +SKIP
    [[1, 2], [3, 4], [5]]
    >>> chunk_list([1, 2, 3, 4, 6], 3) # doctest: +SKIP
    [[1, 2, 3], [4, 6]]
    >>> chunk_list([1, 2, 3], 5) # doctest: +SKIP
    [[1, 2, 3]]
    """
    # YOUR CODE HERE
    pass


# ============================================================
# DICTIONARY PROBLEMS (8-10)
# ============================================================

# Problem 8
def total_cost(purchases: list[tuple[str, int]], prices: dict[str, int]) -> int:
    """Sum of costs of purchases, where
    ("item", n) in purchases means n units of item,
    "item": k in prices means each unit of item costs k cybercoins
    >>> total_cost([("apple", 2), ("banana", 3)], { "pizza": 12, "apple": 2, "banana": 1 }) # doctest: +SKIP
    7
    >>> total_cost([], {"yacht": 99_000_000, "apple": 2}) # doctest: +SKIP
    0
    """
    pass

# Problem 9
def group_by_length(words):
    """
    Given a list of strings, returns a dictionary mapping each word length
    to a list of words of that length, in the order they appear.

    Parameters:
        words (list[str]): A list of strings.

    Returns:
        dict[int, list[str]]: A dictionary mapping lengths to lists of words.

    >>> group_by_length([]) # doctest: +SKIP
    {}
    >>> group_by_length(["hi", "ok"]) # doctest: +SKIP
    {2: ['hi', 'ok']}
    >>> group_by_length(["cat", "dog", "ox", "elephant", "rat"]) # doctest: +SKIP
    {3: ['cat', 'dog', 'rat'], 2: ['ox'], 8: ['elephant']}
    """
    # YOUR CODE HERE
    pass

# Problem 10
def most_common_of_length(lst: list[str], length: int) -> str:
    """
    Returns the string of the given length that appears most frequently
    in lst. If multiple strings of that length are tied, return the one
    that appears first in the list. If no string of that length exists
    in lst, return the empty string "".

    Parameters:
        lst (list[str]): A list of strings.
        length (int): The target string length to filter by.

    Returns:
        str: The most frequent string of the given length, or "" if none found.

    >>> most_common_of_length([], 3) # doctest: +SKIP
    ''
    >>> most_common_of_length(["cat", "dog", "cat"], 3) # doctest: +SKIP
    'cat'
    >>> most_common_of_length(["cat", "dog", "dog", "cat", "dog"], 3) # doctest: +SKIP
    'dog'
    >>> most_common_of_length(["hi", "hello", "hey", "hi"], 3) # doctest: +SKIP
    'hey'
    >>> most_common_of_length(["cat", "dog", "elephant"], 10) # doctest: +SKIP
    ''
    >>> most_common_of_length(["go", "cat", "dog", "go", "cat", "cat"], 3) # doctest: +SKIP
    'cat'
    """
    # YOUR CODE HERE
    pass


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()