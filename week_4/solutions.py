# Problem 1
def sum_vals(val_dict: dict) -> int:
    """
    Sum all of the dictionary's values.

    >>> sum_vals({'a': 1, 'b': 2, 'c': 3})
    6
    >>> sum_vals({'apple': 10, 'banana': 5})
    15
    """
    sum = 0
    for key, value in val_dict.items():
        sum += value
    return sum

# Problem 2
def square_list(l1: list[int]) -> list[int]:
    """
    Takes in a list and returns a new list with all of the values squared.

    >>> square_list([1, 2, 3])
    [1, 4, 9]
    >>> square_list([-2, 0, 5])
    [4, 0, 25]
    """
    squares = []
    for num in l1:
        sqrd = num * num
        squares.append(sqrd)
    return squares
    

# Problem 3
def count_dict(l1: list[str]) -> dict:
    """
    Returns a dictionary where keys are list items and values are their frequency.

    >>> count_dict(['a', 'b', 'a', 'c', 'b', 'a'])
    {'a': 3, 'b': 2, 'c': 1}
    >>> count_dict([])
    {}
    """
    count = {}
    for el in l1:
        if el not in count:
            count[el] = 1
        else:
            count[el] += 1
    return count

# Problem 4
def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    """
    Returns a list of elements that appear in both list1 and list2.

    >>> common_elements([1, 2, 3], [2, 3, 4])
    [2, 3]
    >>> common_elements([10, 20], [30, 40])
    []
    """
    common = []
    for num in list1:
        if num in list2:
            common.append(num)
    return common

# Problem 5
def word_count(sentence: list[str]) -> dict[str, int]:
    """
    Returns a dictionary mapping each word to the number of times it appears.

    >>> word_count(["apple", "banana", "apple", "cherry"])
    {'apple': 2, 'banana': 1, 'cherry': 1}
    """
    count_words = {}
    for word in sentence:
        if word not in count_words:
            count_words[word] = 1
        else:
            count_words[word] += 1
    return count_words

# Problem 6
def filter_greater(li: list[int], threshold: int) -> list[int]:
    """
    Returns a list of all elements greater than the given threshold.

    >>> filter_greater([1, 5, 10, 2], 4)
    [5, 10]
    >>> filter_greater([10, 20, 30], 50)
    []
    """
    greater_than = []
    for num in li:
        if num > threshold:
            greater_than.append(num)
    return greater_than

# Problem 7 (Challenge)
def filter_greater_keys(d: dict[str, int], threshold: int) -> list[str]:
    """
    Returns a list of dictionary keys with values >= the threshold.

    >>> filter_greater_keys({'math': 90, 'art': 75, 'science': 85}, 85)
    ['math', 'science']
    >>> filter_greater_keys({'a': 1, 'b': 2}, 5)
    []
    """
    greater_keys = []
    for key in d.keys():
        if d[key] >= threshold:
            greater_keys.append(key)
    return greater_keys

# Problem 8 (Challenge)
def filter_evens(li: list[int]) -> list[int]:
    """
    Returns a list of all even integers from the input list.

    >>> filter_evens([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> filter_evens([1, 3, 5])
    []
    """
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return evens
        

# Problem 9 (Challenge)
def most_frequent_word(sentence: list[str]) -> str:
    """
    Returns the element that appears most frequently in the list.

    >>> most_frequent_word(["a", "b", "a", "c", "a", "b"])
    'a'
    >>> most_frequent_word(["dog", "cat", "dog"])
    'dog'
    """
    if len(sentence) == 0:
        return ""
    
    freq_dict = {}
    for word in sentence:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    
    most_frequent = sentence[0]
    for key in freq_dict.keys():
        if freq_dict[key] > freq_dict[most_frequent]:
            most_frequent = key
    return most_frequent

if __name__ == "__main__":
    import doctest
    doctest.testmod()