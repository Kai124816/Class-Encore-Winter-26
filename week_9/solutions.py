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

    >>> fibonacci(0) 
    0
    >>> fibonacci(1) 
    1
    >>> fibonacci(6) 
    8
    >>> fibonacci(10) 
    55
    """
    if n <= 1:
        return n
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

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

    >>> count_vowels("")
    0
    >>> count_vowels("rhythm") 
    0
    >>> count_vowels("hello") 
    2
    >>> count_vowels("aeiou") 
    5
    >>> count_vowels("programming") 
    3
    """
    if len(s) == 0:
        return 0
    elif s[0] in "aeiou":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
    
# Problem 3
def flatten(lst):
    """
    Returns a new flat list containing all the integers in a nested list using recursion.
    The input may contain integers or other lists (which may themselves be nested).

    Parameters:
        lst (list): A possibly nested list of integers and lists.

    Returns:
        list: A flat list of all integers in lst, in order.

    >>> flatten([]) 
    []
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> flatten([1, [2, 3], 4])
    [1, 2, 3, 4]
    >>> flatten([[1, [2]], [3, [4, [5]]]]) 
    [1, 2, 3, 4, 5]
    """
    if len(lst) == 0:
        return lst
    
    result = []
    for el in lst:
        if isinstance(el, list):
            result += flatten(el)
        else:
            result.append(el)
    return result

# Problem 4
YUM = "y"
POISON = "p"
def safe_to_eat(food) -> bool:
    """True if there is NO poison in food.
    food may be either a str or a list of foods
    >>> safe_to_eat([])
    True
    >>> safe_to_eat([YUM, [[[[POISON]]]]])
    False
    >>> safe_to_eat([[YUM, YUM], YUM, YUM])
    True
    >>> safe_to_eat([[YUM, POISON], YUM, YUM])
    False
    """
    for el in food:
        if isinstance(el, list):
            if not safe_to_eat(el):
                return False
        elif el == POISON:
            return False
    return True


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

    >>> second_largest([1, 2]) 
    1
    >>> second_largest([3, 1, 4, 1, 5, 9, 2, 6]) 
    6
    >>> second_largest([10, 10, 9, 8]) 
    9
    >>> second_largest([-1, -5, -3]) 
    -3
    """
    largest = lst[0]
    length = len(lst)
    
    for i in range(1, length):
        if lst[i] > largest:
            largest = lst[i]

    second = None
    
    for i in range(length):
        if lst[i] != largest:
            if not second:
                second = lst[i]
            elif lst[i] > second:
                second = lst[i]
    
    return second

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

    >>> zip_lists([], [])
    []
    >>> zip_lists([1, 2, 3], []) 
    []
    >>> zip_lists([1, 2, 3], ["a", "b", "c"]) 
    [(1, 'a'), (2, 'b'), (3, 'c')]
    >>> zip_lists([1, 2], ["a", "b", "c", "d"]) 
    [(1, 'a'), (2, 'b')]
    """
    shorter_length = min(len(lst1), len(lst2))
    zipped = []
    for i in range(shorter_length):
        combo = (lst1[i], lst2[i])
        zipped.append(combo)
    return zipped


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

    >>> chunk_list([], 3) 
    []
    >>> chunk_list([1, 2, 3, 4, 5], 2) 
    [[1, 2], [3, 4], [5]]
    >>> chunk_list([1, 2, 3, 4, 6], 3) 
    [[1, 2, 3], [4, 6]]
    >>> chunk_list([1, 2, 3], 5) 
    [[1, 2, 3]]
    """
    if len(lst) == 0:
        return []
    
    chunks = []
    curr_chunk = []
    for i in range(len(lst)):
        if i % size == 0 and i != 0:
            chunks.append(curr_chunk)
            curr_chunk = []
        curr_chunk.append(lst[i])

    chunks.append(curr_chunk)

    return chunks


# ============================================================
# DICTIONARY PROBLEMS (8-10)
# ============================================================

# Problem 8
def total_cost(purchases: list[tuple[str, int]], prices: dict[str, int]) -> int:
    """Sum of costs of purchases, where
    ("item", n) in purchases means n units of item,
    "item": k in prices means each unit of item costs k cybercoins
    >>> total_cost([("apple", 2), ("banana", 3)], { "pizza": 12, "apple": 2, "banana": 1 })
    7
    >>> total_cost([], {"yacht": 99_000_000, "apple": 2})
    0
    """
    acc = 0
    for p in purchases:
        item = p[0]
        units = p[1]
        if item in prices:
            acc += prices[item] * units
    return acc

# Problem 9
def group_by_length(words):
    """
    Given a list of strings, returns a dictionary mapping each word length
    to a list of words of that length, in the order they appear.

    Parameters:
        words (list[str]): A list of strings.

    Returns:
        dict[int, list[str]]: A dictionary mapping lengths to lists of words.

    >>> group_by_length([]) 
    {}
    >>> group_by_length(["hi", "ok"]) 
    {2: ['hi', 'ok']}
    >>> group_by_length(["cat", "dog", "ox", "elephant", "rat"]) 
    {3: ['cat', 'dog', 'rat'], 2: ['ox'], 8: ['elephant']}
    """
    length_dict = {}

    for word in words:
        length = len(word)
        if length in length_dict:
            length_dict[length].append(word)
        else:
            length_dict[length] = [word]
    return length_dict

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

    >>> most_common_of_length([], 3) 
    ''
    >>> most_common_of_length(["cat", "dog", "cat"], 3) 
    'cat'
    >>> most_common_of_length(["cat", "dog", "dog", "cat", "dog"], 3) 
    'dog'
    >>> most_common_of_length(["hi", "hello", "hey", "hi"], 3) 
    'hey'
    >>> most_common_of_length(["cat", "dog", "elephant"], 10) 
    ''
    >>> most_common_of_length(["go", "cat", "dog", "go", "cat", "cat"], 3) 
    'cat'
    """
    words_of_len = {}
    contains_word_of_len = False

    for word in lst:
        if len(word) == length:
            contains_word_of_len = True
            if word in words_of_len:
                words_of_len[word] += 1
            else:
                words_of_len[word] = 1
    
    if not contains_word_of_len:
        return ''
    
    list_of_keys = list(words_of_len.keys())
    most_common = list_of_keys[0]

    for i in range(1, len(list_of_keys)):
        word = list_of_keys[i]
        if words_of_len[word] > words_of_len[most_common]:
            most_common = word

    return most_common
    

# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()