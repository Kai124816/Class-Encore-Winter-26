import doctest
import csv

# Problem 1
def clamp(v: int, bound_lower: int, bound_upper: int) -> int:
    """Return value v clamped to be no less than bound_lower
    and no greater than bound_upper.
    """
    if v < bound_lower:
        return bound_lower
    elif v > bound_upper:
        return bound_upper
    return v

def clamped_sum(li: list[int], bound_lower: int, bound_upper: int) -> int:
    """Sum of li values clamped between bound_lower and bound_upper.
    >>> clamped_sum([-8, 5, 9, 25], 0, 10) # doctest: +SKIP
    24
    >>> clamped_sum([-8, 5, 25], 5, 10) # doctest: +SKIP
    20
    """
    pass

# Problem 2
def longest_increase(l1: list[int]) -> int:
    """
    Find the length of the longest streak of strictly increasing numbers.

    Args:
        l1: A list of integers.

    Returns:
        The length of the longest increasing sequence.

    >>> longest_increase([1, 2, 3, 1, 2]) # doctest: +SKIP
    3
    >>> longest_increase([5, 4, 3, 2, 1]) # doctest: +SKIP
    1
    >>> longest_increase([]) # doctest: +SKIP
    0
    """
    pass

# Problem 3
FORBIDDEN_WORDS = {"coffee": "<hot beverage>", "tea": "<hot beverage>",
"chocolate": "<sweet candy>", "caramel": "<sweet candy>"}

def censor(text: list[str]) -> list[str]:
    """Copy with any word in FORBIDDEN_WORDS replaced.
    >>> censor(["We", "are", "out", "of", "chocolate"]) # doctest: +SKIP
    ['We', 'are', 'out', 'of', '<sweet candy>']
    >>> censor(["Do", "you", "prefer", "coffee", "or", "tea"]) # doctest: +SKIP
    ['Do', 'you', 'prefer', '<hot beverage>', 'or', '<hot beverage>']
    """
    pass

# Problem 4
def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    Identify the minimum value associated with each unique name in a list of pairs.

    Args:
        li: A list of (name, value) tuples.

    Returns:
        A list of tuples containing each unique name and its smallest seen value.

    >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)]) # doctest: +SKIP
    [('apple', 7), ('orange', 12)]
    >>> smallest_each([("tensor", 100), ("tensor", 50), ("tensor", 150)]) # doctest: +SKIP
    [('tensor', 50)]
    """
    pass

# Problem 5
def longest_contains_a(words: list[str]) -> str:
    """
    Find the longest string in a list that contains the character 'a'.

    Args:
        words: A list of strings to search through.

    Returns:
        The longest string containing 'a'. Returns an empty string if 
        none are found or the list is empty.

    >>> longest_contains_a(["apple", "banana", "cherry", "date"]) # doctest: +SKIP
    'banana'
    >>> longest_contains_a(["sky", "dry", "fly"]) # doctest: +SKIP
    ''
    """
    pass

# Problem 6
def return_averages(test_scores: dict[str, list[int]]) -> str:
    """
    Find the student with the highest average test score.

    Args:
        test_scores: A dictionary where keys are student names (str) and 
                     values are lists of scores (int).

    Returns:
        The name of the student with the highest mean score.

    >>> return_averages({"Alice": [90, 95, 100], "Bob": [80, 85, 90]}) # doctest: +SKIP
    'Alice'
    >>> return_averages({"Michael": [72, 100], "Thomas": [92, 81]}) # doctest: +SKIP
    'Thomas'
    """
    pass

# Problem 7 (Challenge)
def partition(pivot: int, li: list[int]) -> tuple[list[int], list[int]]:
    """Returns two lists (small, big)
    where small contains elements of li with value less than pivot
    and big contains elements at least as large as pivot
    in the same order as li.
    >>> partition(3, [0, 1, 2, 3, 4, 5]) # doctest: +SKIP
    ([0, 1, 2], [3, 4, 5])
    >>> partition(0, [7, -7, 8, -9, 0]) # doctest: +SKIP
    ([-7, -9], [7, 8, 0])
    """
    pass

# Problem 8 (Challenge)
def contains_peak(nums: list[int]) -> bool:
    """
    Determine if a list contains at least one 'peak'.
    
    A peak is an element greater than its immediate neighbors. 
    Boundaries only need to be greater than their single neighbor.

    Args:
        nums: A list of integers.

    Returns:
        True if at least one peak exists, False otherwise.

    >>> contains_peak([1, 2, 3, 2, 1]) # doctest: +SKIP
    True
    >>> contains_peak([1, 2, 3]) # doctest: +SKIP
    True
    >>> contains_peak([5, 4, 3]) # doctest: +SKIP
    True
    >>> contains_peak([]) # doctest: +SKIP
    False
    """
    pass
        
# Problem 9 (Challenge)
def average_price(entries: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """
    Calculate the mean price for each unique product in a list of entries.

    Args:
        entries: A list of (product_name, price) tuples.

    Returns:
        A list of (product_name, average_price) tuples, with averages 
        rounded to one decimal place.

    >>> average_price([("banana", 1.0), ("apple", 2.0), ("banana", 1.5), ("apple", 3.0)]) # doctest: +SKIP
    [('banana', 1.2), ('apple', 2.5)]
    >>> average_price([("pear", 2.2222)]) # doctest: +SKIP
    [('pear', 2.2)]
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()