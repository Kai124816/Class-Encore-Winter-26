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
    >>> clamped_sum([-8, 5, 9, 25], 0, 10)
    24
    >>> clamped_sum([-8, 5, 25], 5, 10)
    20
    """
    acc = 0
    for num in li:
        acc += clamp(num, bound_lower, bound_upper)
    return acc

# Problem 2
def longest_increase(l1: list[int]) -> int:
    """
    Find the length of the longest streak of strictly increasing numbers.

    Args:
        l1: A list of integers.

    Returns:
        The length of the longest increasing sequence.

    >>> longest_increase([1, 2, 3, 1, 2])
    3
    >>> longest_increase([5, 4, 3, 2, 1])
    1
    >>> longest_increase([])
    0
    """
    if len(l1) == 0:
        return 0
    
    longest = 1
    curr_streak = 1
    for i in range(1,len(l1)):
        if l1[i] > l1[i - 1]:
            curr_streak += 1
        else:
            if curr_streak > longest:
                longest = curr_streak
            curr_streak = 1
    return longest

# Problem 3
FORBIDDEN_WORDS = {"coffee": "<hot beverage>", "tea": "<hot beverage>",
"chocolate": "<sweet candy>", "caramel": "<sweet candy>"}

def censor(text: list[str]) -> list[str]:
    """Copy with any word in FORBIDDEN_WORDS replaced.
    >>> censor(["We", "are", "out", "of", "chocolate"])
    ['We', 'are', 'out', 'of', '<sweet candy>']
    >>> censor(["Do", "you", "prefer", "coffee", "or", "tea"])
    ['Do', 'you', 'prefer', '<hot beverage>', 'or', '<hot beverage>']
    """
    new_text = []
    for word in text:
        if word in FORBIDDEN_WORDS:
            new_text.append(FORBIDDEN_WORDS[word])
        else:
            new_text.append(word)
    return new_text


# Problem 4
def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    Identify the minimum value associated with each unique name in a list of pairs.

    Args:
        li: A list of (name, value) tuples.

    Returns:
        A list of tuples containing each unique name and its smallest seen value.

    >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])
    [('apple', 7), ('orange', 12)]
    >>> smallest_each([("tensor", 100), ("tensor", 50), ("tensor", 150)])
    [('tensor', 50)]
    """
    smallest = {}
    for name, value in li:
        if name not in smallest:
            smallest[name] = value
        elif name in smallest and smallest[name] > value:
            smallest[name] = value
    
    return list(smallest.items())

# Problem 5
def longest_contains_a(words: list[str]) -> str:
    """
    Find the longest string in a list that contains the character 'a'.

    Args:
        words: A list of strings to search through.

    Returns:
        The longest string containing 'a'. Returns an empty string if 
        none are found or the list is empty.

    >>> longest_contains_a(["apple", "banana", "cherry", "date"])
    'banana'
    >>> longest_contains_a(["sky", "dry", "fly"])
    ''
    """
    longest = ""
    for string in words:
        if string.count("a") and len(string) > len(longest):
            longest = string
    return longest

# Problem 6
def return_averages(test_scores: dict[str, list[int]]) -> str:
    """
    Find the student with the highest average test score.

    Args:
        test_scores: A dictionary where keys are student names (str) and 
                     values are lists of scores (int).

    Returns:
        The name of the student with the highest mean score.

    >>> return_averages({"Alice": [90, 95, 100], "Bob": [80, 85, 90]})
    'Alice'
    >>> return_averages({"Michael": [72, 100], "Thomas": [92, 81]})
    'Thomas'
    """
    highest_avg = 0
    best_student = ""
    for student, scores in test_scores.items():
        combined_score = 0
        for score in scores:
            combined_score += score
        avg = combined_score / len(scores)
        if avg > highest_avg or best_student == "":
            highest_avg = avg
            best_student = student
    return best_student

# Problem 7 (Challenge)
def partition(pivot: int, li: list[int]) -> tuple[list[int], list[int]]:
    """Returns two lists (small, big)
    where small contains elements of li with value less than pivot
    and big contains elements at least as large as pivot
    in the same order as li.
    >>> partition(3, [0, 1, 2, 3, 4, 5])
    ([0, 1, 2], [3, 4, 5])
    >>> partition(0, [7, -7, 8, -9, 0])
    ([-7, -9], [7, 8, 0])
    """
    less_than = []
    greater_than = []
    for num in li:
        if num < pivot:
            less_than.append(num)
        else:
            greater_than.append(num)
    return less_than, greater_than


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

    >>> contains_peak([1, 2, 3, 2, 1])
    True
    >>> contains_peak([1, 2, 3])
    True
    >>> contains_peak([5, 4, 3])
    True
    >>> contains_peak([])
    False
    """
    length = len(nums)
    if length == 0:
        return False
    if length == 1:
        return True
    
    for i in range(length):
        if i == 0 and nums[i] > nums[1]:
            return True
        if i == (length - 1) and nums[i] > nums[i - 1]:
            return True
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return True
    return False
        

# Problem 9 (Challenge)
def average_price(entries: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """
    Calculate the mean price for each unique product in a list of entries.

    Args:
        entries: A list of (product_name, price) tuples.

    Returns:
        A list of (product_name, average_price) tuples, with averages 
        rounded to one decimal place.

    >>> average_price([("banana", 1.0), ("apple", 2.0), ("banana", 1.5), ("apple", 3.0)])
    [('banana', 1.2), ('apple', 2.5)]
    >>> average_price([("pear", 2.2222)])
    [('pear', 2.2)]
    """
    total_appearance_dict = {}
    total_price_dict = {}
    for product, price in entries:
        if product in total_appearance_dict:
            total_appearance_dict[product] += 1
            total_price_dict[product] += price
        else:
            total_appearance_dict[product] = 1
            total_price_dict[product] = price

    average_prices = []
    for key in total_appearance_dict.keys():
        total_appearances = total_appearance_dict[key]
        total_price = total_price_dict[key]
        average_price = total_price / total_appearances
        average_prices.append((key, round(average_price, 1)))
    return average_prices

if __name__ == "__main__":
    import doctest
    doctest.testmod()