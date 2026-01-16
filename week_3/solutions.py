
# Problem 1
def good_sum(li: list[int], threshold: int) -> int:
    """Returns the sum of all numbers in li that are strictly greater than threshold.

    >>> good_sum([1, 2, 4, 7], 3) 
    11
    >>> good_sum([1, 2, 3], 3) 
    0
    """
    acc = 0
    for num in li:
        if num > threshold:
            acc += num
    return acc

# Problem 2
def sum_of_lengths(li: list[str]) -> int:
    """Returns the sum of the lengths of all strings in the list.

    >>> sum_of_lengths(["hello", "CS", "Python"]) 
    13
    >>> sum_of_lengths([]) 
    0
    """
    acc = 0
    for word in li:
        acc += len(word)
    return acc

# Problem 3
def sum_even(nums: list[int]) -> int:
    """Returns the sum of all even numbers in nums.

    >>> sum_even([1, 2, 3, 4]) 
    6
    >>> sum_even([1, 3, 5]) 
    0
    """
    acc = 0
    for number in nums:
        if number % 2 == 0:
            acc += number
    return acc
    
# Problem 4
def find_longest_string(strings: list[str]) -> str:
    """Returns the longest string in a list. If the list is empty, returns None.

    >>> find_longest_string(["hello", "CS", "Python"]) 
    'Python'
    >>> find_longest_string([]) 
    ''
    """
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

# Problem 5
def has_even_sum(nums: list[int]) -> bool:
    """Determines whether the sum of numbers in the list is even.

    >>> has_even_sum([1, 2, 3, 4]) 
    True
    >>> has_even_sum([1, 2, 2]) 
    False
    """
    acc = 0
    for num in nums:
        acc += num
    return acc % 2 == 0

# Problem 6
VOWELS = 'aeiouAEIOU'
def is_vowel(char: str) -> bool:
    """Checks if a single character is a vowel.
    
    >>> is_vowel('a') 
    True
    >>> is_vowel('z') 
    False
    """
    return char in VOWELS

def num_vowels(word: str) -> int:
    """Counts the number of vowels in a string. 
    Use the is_vowel function to determine if 
    a character is a vowel or not.

    >>> num_vowels("Python")
    1
    >>> num_vowels("Apple") 
    2
    """
    count = 0
    for letter in word:
        if is_vowel(letter):
            count += 1
    return count
    

# Problem 7 (Challenge)
def is_palindrome(word: str) -> bool:
    """Determines whether or not a string is a palindrome.

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("python") 
    False
    """
    length = len(word)
    middle = length // 2
    for i in range(middle):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Problem 8 (Challenge)
def smallest_even(nums: list[int]) -> int:
    """Finds the smallest even number in a list of non-negative integers.
    If there are no even numbers, returns -1.
    >>> smallest_even([1, 2, 4, 8]) 
    2
    >>> smallest_even([3, 5, 7]) 
    -1
    """
    smallest = max(nums)
    for number in nums:
        if number % 2 == 0 and number < smallest:
            smallest = number

    if smallest % 2 != 0:
        return -1
    else:
        return smallest

# Problem 9 (Challenge)
def how_many_targets(words: list[str], target: str) -> int:
    """Returns the number of times a target string appears in a list.

    >>> how_many_targets(["hello", "CS", "Python", "CS"], "CS") 
    2
    >>> how_many_targets(["a", "b", "c"], "z") 
    0
    """
    count = 0
    for word in words: 
        if word == target: 
            count += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()