"""
INTRODUCTION TO DOCTESTS:
1. Lines starting with '>>>' show the function call being tested.
2. The line immediately following it shows the expected return value.
3. To run these tests, simply run the file. If there are any errors with your tests
they will show up in the terminal.
4. Note: The '# doctest: +SKIP' tag is currently preventing these tests from 
   running. Once you write your code, you can remove that tag to check your work.
"""

# Problem 1
def good_sum(li: list[int], threshold: int) -> int:
    """Returns the sum of all numbers in li that are strictly greater than threshold.

    >>> good_sum([1, 2, 4, 7], 3) # doctest: +SKIP
    11
    >>> good_sum([1, 2, 3], 3) # doctest: +SKIP
    0
    """
    return

# Problem 2
def sum_of_lengths(li: list[str]) -> int:
    """Returns the sum of the lengths of all strings in the list.

    >>> sum_of_lengths(["hello", "CS", "Python"]) # doctest: +SKIP
    13
    >>> sum_of_lengths([]) # doctest: +SKIP
    0
    """
    return

# Problem 3
def sum_even(nums: list[int]) -> int:
    """Returns the sum of all even numbers in nums.

    >>> sum_even([1, 2, 3, 4]) # doctest: +SKIP
    6
    >>> sum_even([1, 3, 5]) # doctest: +SKIP
    0
    """
    return
    
# Problem 4
def find_longest_string(strings: list[str]) -> str:
    """Returns the longest string in a list. If the list is empty, returns None.

    >>> find_longest_string(["hello", "CS", "Python"]) # doctest: +SKIP
    'Python'
    >>> find_longest_string([]) # doctest: +SKIP
    ''
    """
    return

# Problem 5
def has_even_sum(nums: list[int]) -> bool:
    """Determines whether the sum of numbers in the list is even.

    >>> has_even_sum([1, 2, 3, 4]) # doctest: +SKIP
    True
    >>> has_even_sum([1, 2, 2]) # doctest: +SKIP
    False
    """
    return

# Problem 6
VOWELS = 'aeiouAEIOU'
def is_vowel(char: str) -> bool:
    """Checks if a single character is a vowel.
    
    >>> is_vowel('a') # doctest: +SKIP
    True
    >>> is_vowel('z') # doctest: +SKIP
    False
    """
    return char in VOWELS

def num_vowels(word: str) -> int:
    """Counts the number of vowels in a string.

    >>> num_vowels("Python") # doctest: +SKIP
    1
    >>> num_vowels("Apple") # doctest: +SKIP
    2
    """
    return

# Problem 7 (Challenge)
def is_palindrome(word: str) -> bool:
    """Determines whether or not a string is a palindrome.

    >>> is_palindrome("racecar") # doctest: +SKIP
    True
    >>> is_palindrome("python") # doctest: +SKIP
    False
    """
    length = len(word)
    middle = length // 2
    return

# Problem 8 (Challenge)
def smallest_even(nums: list[int]) -> int:
    """Finds the smallest even number in a list of non-negative integers.
    If there are no even numbers, returns -1.
    >>> smallest_even([1, 2, 4, 8]) # doctest: +SKIP
    2
    >>> smallest_even([3, 5, 7]) # doctest: +SKIP
    -1
    """
    smallest = max(nums)
    #Hint: All you need to do is write a for loop

    if smallest % 2 != 0:
        return -1
    else:
        return smallest

# Problem 9 (Challenge)
def how_many_targets(words: list[str], target: str) -> int:
    """Returns the number of times a target string appears in a list.

    >>> how_many_targets(["hello", "CS", "Python", "CS"], "CS") # doctest: +SKIP
    2
    >>> how_many_targets(["a", "b", "c"], "z") # doctest: +SKIP
    0
    """
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()