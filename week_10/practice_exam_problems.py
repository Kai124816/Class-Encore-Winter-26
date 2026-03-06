import doctest

# FINAL EXAM

# =============================================================================
# SECTION 1: WRITE YOUR OWN CODE  (6 problems, 10 points each)
# =============================================================================

# Problem 1
def score(word: str, values: dict[str, int]) -> int:
    """Sum of letter values in word, taken from values,
    and counting zero for letters that are not in the values table.
    >>> score("this is easy", {'i': 5, 'e': 2}) # doctest: +SKIP
    12
    >>> score("I struck out", {'w': 8, 'x': 9, 'q': 10}) # doctest: +SKIP
    0
    """
    pass


# Problem 2
def match_at(m: list[int], n: list[int]) -> int:
    """Smallest i such that m[i] == n[i],
    or -1 if there is no such i.
    >>> match_at([1, 2, 3], [3, 2, 1]) # doctest: +SKIP
    1
    >>> match_at([1, 2, 5, 3], [5, 3, 5]) # doctest: +SKIP
    2
    >>> match_at([1, 2, 5, 3], [3, 5, 1]) # doctest: +SKIP
    -1
    """
    pass


# Problem 3
def most(collection: list[tuple[str, int]]) -> str:
    """Which element of the non-empty collection of (key, count) pairs
    has the greatest total count? (All counts are positive.)
    >>> most([("dogs", 3), ("cats", 5), ("dogs", 3)]) # doctest: +SKIP
    'dogs'
    >>> most([("dogs", 3), ("cats", 7), ("dogs", 3)]) # doctest: +SKIP
    'cats'
    """
    assert len(collection) > 0


# Problem 4
def l_count(letter: str, word: str) -> int:
    """Number of times letter appears in word
    (using recursion only, with no other looping)
    >>> l_count("m", "mimosa") # doctest: +SKIP
    2
    >>> l_count("x", "mimosa") # doctest: +SKIP
    0
    >>> l_count("m", "") # doctest: +SKIP
    0
    """

# Problem 5
def odd_even(li: list[int]) -> tuple[list[int], list[int]]:
    """Separates li into (odds, evens) where odds is a list
    containing the odd elements of li and evens is the list
    containing the even elements of li.
    >>> odd_even([5, 3, 2, 0, 1, 6]) # doctest: +SKIP
    ([5, 3, 1], [2, 0, 6])
    >>> odd_even([3, 5, 3, 3, 7]) # doctest: +SKIP
    ([3, 5, 3, 3, 7], [])
    """
    pass


# Problem 6  (Challenge)
"""
Problem Description:
Finish recursive function “requires”, which determines whether taking some
course X requires taking another course Y. For example, to take CS 211, you must satisfy
the requirement for Math 112, because Math 112 is a pre-requisite for CS 210, and CS 210
is a pre-requisite for CS 211.
"""

PRE_REQS = {
"Math 232": ["Math 231"], 
"Math 231": ["Math 112"],
"CS 212": ["CS 211"], 
"CS 211": ["CS 210"], 
"CS 210": ["Math 112"],
"CS 313": ["Math 232", "CS 212"],
"DSCI 102": ["DSCI 101", "Math 101"] 
}

def requires(course: str, other: str) -> bool:
    """Does taking one course require taking other course?
    >>> requires("Math 232", "Math 112") # doctest: +SKIP
    True
    >>> requires("DSCI 102", "Math 112") # doctest: +SKIP
    False
    """


# =============================================================================
# SECTION 2: MULTIPLE CHOICE  (10 questions, 2 points each)
#
# Replace None with the letter of the best answer (e.g., ANSWER_1 = 'A')
# =============================================================================

# ------------------------------------------------------------------------------
# Question 1
# What is the output of the following code?
#
#   d = {"x": 10, "y": 20, "z": 30}
#   total = 0
#   for v in d.values():
#       total += v
#   print(total)
#
# A) {"x": 10, "y": 20, "z": 30}
# B) 0
# C) 60
# D) Error: dictionaries are not iterable
# E) None
# ------------------------------------------------------------------------------
ANSWER_1 = None


# ------------------------------------------------------------------------------
# Question 2
# What does the following function return when called as mystery([3, 1, 4, 1, 5])?
#
#   def mystery(lst):
#       result = []
#       for item in lst:
#           if item not in result:
#               result.append(item)
#       return result
#
# A) [3, 1, 4, 5]
# B) [1, 3, 4, 5]
# C) [3, 1, 4, 1, 5]
# D) [1]
# E) Error
# ------------------------------------------------------------------------------
ANSWER_2 = None


# ------------------------------------------------------------------------------
# Question 3
# What is the output of the following code?
#
#   words = ["apple", "banana", "cherry"]
#   result = {w: len(w) for w in words if len(w) > 5}
#   print(result)
#
# A) {'apple': 5, 'banana': 6, 'cherry': 6}
# B) {'banana': 6, 'cherry': 6}
# C) ['banana', 'cherry']
# D) Error: invalid syntax
# E) {}
# ------------------------------------------------------------------------------
ANSWER_3 = None


# ------------------------------------------------------------------------------
# Question 4
# Which of the following correctly describes the difference between
# a list and a tuple in Python?
#
# A) Lists can contain only integers; tuples can contain any type
# B) Lists are mutable; tuples are immutable
# C) Lists are ordered; tuples are unordered
# D) Lists use curly braces; tuples use square brackets
# E) There is no difference; they are interchangeable
# ------------------------------------------------------------------------------
ANSWER_4 = None


# ------------------------------------------------------------------------------
# Question 5
# What is the output of the following code?
#
#   def f(x, y=2):
#       return x ** y
#
#   print(f(3))
#   print(f(3, 3))
#
# A) 9 \n 27
# B) 6 \n 9
# C) 9 \n 9
# D) Error: missing required argument
# E) None \n None
# ------------------------------------------------------------------------------
ANSWER_5 = None


# ------------------------------------------------------------------------------
# Question 6
# What is the result of the following expression?
#
#   "Python"[1:4]
#
# A) 'Pyt'
# B) 'yth'
# C) 'ytho'
# D) 'Python'
# E) Error: string index out of range
# ------------------------------------------------------------------------------
ANSWER_6 = None


# ------------------------------------------------------------------------------
# Question 7
# Find the bug in the following function:
#
#   def count_above(nums, threshold):
#       count = 0
#       for i in range(len(nums)):
#           if nums[i] > threshold:
#               count + 1      # <-- line A
#       return count
#
# A) The loop should use "for num in nums" instead of range indexing
# B) The accumulator on line A should be "count += 1"
# C) The condition should be ">=" instead of ">"
# D) count should be initialized to None, not 0
# E) There is no bug; the function is correct
# ------------------------------------------------------------------------------
ANSWER_7 = None


# ------------------------------------------------------------------------------
# Question 8
# What is the output of the following code?
#
#   pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
#   for num, letter in pairs:
#       print(letter * num)
#
# A) a \n bb \n ccc
# B) 1a \n 2b \n 3c
# C) ('a', 1) \n ('b', 2) \n ('c', 3)
# D) Error: cannot unpack non-sequence
# E) a \n b \n c
# ------------------------------------------------------------------------------
ANSWER_8 = None


# ------------------------------------------------------------------------------
# Question 9
# What is the output of the following code?
#
#   def append_double(lst):
#       lst.append(lst[-1] * 2)
#
#   numbers = [1, 2, 3]
#   append_double(numbers)
#   print(numbers)
#
# A) [1, 2, 3]
# B) [1, 2, 3, 6]
# C) [2, 4, 6]
# D) None
# E) Error: list index out of range
# ------------------------------------------------------------------------------
ANSWER_9 = None


# ------------------------------------------------------------------------------
# Question 10
# Which of the following best describes what this code does?
#
#   data = ["hello", "world", "foo", "bar"]
#   result = sorted(data, key=len)
#   print(result)
#
# A) Sorts the list alphabetically in ascending order
# B) Sorts the list by word length from shortest to longest
# C) Returns the length of each word in a new list
# D) Sorts the list by word length from longest to shortest
# E) Error: sorted() does not accept a key argument
# ------------------------------------------------------------------------------
ANSWER_10 = None


# =============================================================================
# DO NOT MODIFY BELOW THIS LINE
# =============================================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()