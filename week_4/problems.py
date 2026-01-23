# Problem 1
def sum_vals(val_dict: dict) -> int:
    """
    Sum all of the dictionary's values. 

    >>> sum_vals({'a': 1, 'b': 2, 'c': 3}) # doctest: +SKIP
    6
    >>> sum_vals({'apple': 10, 'banana': 5}) # doctest: +SKIP
    15
    """
    return

# Problem 2
def square_list(l1: list[int]) -> list[int]:
    """
    Takes in a list and returns a new list with all of the values squared.

    >>> square_list([1, 2, 3]) # doctest: +SKIP
    [1, 4, 9]
    >>> square_list([-2, 0, 5]) # doctest: +SKIP
    [4, 0, 25]
    """
    return

# Problem 3
def count_dict(l1: list[str]) -> dict:
    """
    Returns a dictionary where keys are list items and values are their frequency.

    >>> count_dict(['a', 'b', 'a', 'c', 'b', 'a']) # doctest: +SKIP
    {'a': 3, 'b': 2, 'c': 1}
    >>> count_dict([]) # doctest: +SKIP
    {}
    """
    return

# Problem 4
def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    """
    Returns a list of elements that appear in both list1 and list2.

    >>> common_elements([1, 2, 3], [2, 3, 4]) # doctest: +SKIP
    [2, 3]
    >>> common_elements([10, 20], [30, 40]) # doctest: +SKIP
    []
    """
    return 

# Problem 5
def word_count(sentence: list[str]) -> dict[str, int]:
    """
    Returns a dictionary mapping each word to the number of times it appears.

    >>> word_count(["apple", "banana", "apple", "cherry"]) # doctest: +SKIP
    {'apple': 2, 'banana': 1, 'cherry': 1}
    """
    return

# Problem 6
def filter_greater(li: list[int], threshold: int) -> list[int]:
    """
    Returns a list of all elements greater than the given threshold.

    >>> filter_greater([1, 5, 10, 2], 4) # doctest: +SKIP
    [5, 10]
    >>> filter_greater([10, 20, 30], 50) # doctest: +SKIP
    []
    """
    return 

# Problem 7 (Challenge)
def filter_greater_keys(d: dict[str, int], threshold: int) -> list[str]:
    """
    Returns a list of dictionary keys with values >= the threshold.

    >>> filter_greater_keys({'math': 90, 'art': 75, 'science': 85}, 85) # doctest: +SKIP
    ['math', 'science']
    >>> filter_greater_keys({'a': 1, 'b': 2}, 5) # doctest: +SKIP
    []
    """
    return 

# Problem 8 (Challenge)
def filter_evens(li: list[int]) -> list[int]:
    """
    Returns a list of all even integers from the input list.

    >>> filter_evens([1, 2, 3, 4, 5, 6]) # doctest: +SKIP
    [2, 4, 6]
    >>> filter_evens([1, 3, 5]) # doctest: +SKIP
    []
    """
    return

# Problem 9 (Challenge)
def most_frequent_word(sentence: list[str]) -> str:
    """
    Returns the element that appears most frequently in the list.

    >>> most_frequent_word(["a", "b", "a", "c", "a", "b"]) # doctest: +SKIP
    'a'
    >>> most_frequent_word(["dog", "cat", "dog"]) # doctest: +SKIP
    'dog'
    """
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()