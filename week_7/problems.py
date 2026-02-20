import doctest

#Problem 1
def longest_streak_of_positives(nums: list[int]) -> int:
    """Given a list of integers, return the length of the longest
    consecutive streak of positive numbers (> 0). Returns 0 if
    there are no positive numbers or the list is empty.
    >>> longest_streak_of_positives([1, 2, -1, 3, 4, 5, -2, 6]) # doctest: +SKIP
    3
    >>> longest_streak_of_positives([-1, -2, -3]) # doctest: +SKIP
    0
    >>> longest_streak_of_positives([]) # doctest: +SKIP
    0
    >>> longest_streak_of_positives([1, 2, 3, 4]) # doctest: +SKIP
    4
    """
    pass

#Problem 2
def word_lengths(words: list[str]) -> dict[str, int]:
    """Given a list of words, return a dictionary mapping each word to
    its length.
    >>> word_lengths(["cat", "elephant", "ox"]) # doctest: +SKIP
    {'cat': 3, 'elephant': 8, 'ox': 2}
    >>> word_lengths([]) # doctest: +SKIP
    {}
    >>> word_lengths(["hi", "hi", "bye"]) # doctest: +SKIP
    {'hi': 2, 'bye': 3}
    """
    result = {}
    for word in words:
        length = len(word)
        result[word] = length
        result[word] += 1

#Problem 3
def is_stable(old_centroids: list[int], new_centroids: list[int]) -> bool:
    """True if both lists of centroids contain the same coordinates in the same order.
    >>> is_stable([[1, 1]], [[1, 1]])
    True
    >>> is_stable([[1, 1]], [[1, 2]])
    False
    >>> is_stable([[1, 1], [2, 2], [3, 3]], [[1, 1], [2, 2], [3, 3]])
    True
    >>> is_stable([[1, 1], [2, 2]], [[2, 2], [1, 1]])
    False
    >>> is_stable([], [])
    True
    """
    

#Problem 4
def above_average(grades: dict[str, float]) -> list[str]:
    """Given a dictionary mapping student names to numeric grades,
    return a sorted list of the names of students whose grade is
    strictly above the average grade. Return an empty list if
    grades is empty. 
    >>> above_average({"Alice": 90, "Bob": 70, "Carol": 80}) # doctest: +SKIP
    ['Alice']
    >>> above_average({"Alice": 85, "Bob": 85}) # doctest: +SKIP
    []
    >>> above_average({}) # doctest: +SKIP
    []
    """
    pass

#Problem 5
def all_greater(a: list[int], threshold: int) -> bool:
    """Returns True if list a has a length greater than 0
    and every element in a is greater than the threshold
    >>> all_greater([2, 3, 3], 3) # doctest: +SKIP
    False
    >>> all_greater([6,7,8], 5) # doctest: +SKIP
    True
    >>> all_greater([2], 3) # doctest: +SKIP
    False
    >>> all_greater([0], 10) # doctest: +SKIP
    False
    """
    pass

#Problem 6
def evens_greater(l1:list[int]) -> bool:
    """Returns true if the sum of the even numbers in 
    the list is greater than the sum of the odd numbers.
    >>> evens_greater([2, 4, 1, 3]) # doctest: +SKIP
    True
    >>> evens_greater([1, 3, 5, 2]) # doctest: +SKIP
    False
    >>> evens_greater([2, 2, 3, 3]) # doctest: +SKIP
    False
    >>> evens_greater([]) # doctest: +SKIP
    False
    """
    pass

#Problem 7 (Challenge)
def flatten_positive(lists: list[list[int]]) -> list[int]:
    """Given a list of lists of integers, return a single flat list
    containing only the positive integers (> 0) from all sublists,
    in the order they appear.
    >>> flatten_positive([[1, -2, 3], [0, 4], [-5, 6]]) # doctest: +SKIP
    [1, 3, 4, 6]
    >>> flatten_positive([[], [1, 2], []]) # doctest: +SKIP
    [1, 2]
    >>> flatten_positive([[-1, -2], [-3]]) # doctest: +SKIP
    []
    """
    flattened = []
    for list in lists: #Iterates through sub lists
        pass #Finish this function

#Problem 8 (Challenge)
def best_student(students: list[str], scores: list[int]) -> str:
    """Given parallel lists where element i is a student and scores[i]
    is their score, return the name of the student with the highest
    score. You may assume the lists are non-empty and the same length.
    Ties may be broken any way you like.
    >>> best_student(["Alice", "Bob", "Carol"], [72, 95, 88]) # doctest: +SKIP
    'Bob'
    >>> best_student(["Alice"], [100]) # doctest: +SKIP
    'Alice'
    >>> best_student(["Alice", "Bob"], [87, 85]) # doctest: +SKIP
    'Alice'
    """
    pass
                
#Problem 9 (Challenge)
def top_two(l1: list[int]) -> list[int]:
    """Given a list of integers, return a list containing the two
    largest values in descending order. You may assume the list
    has at least two elements and all values are unique.
    >>> top_two([3, 1, 4, 1, 5, 9, 2, 6]) # doctest: +SKIP
    [9, 6]
    >>> top_two([10, 20]) # doctest: +SKIP
    [20, 10]
    >>> top_two([5, 3, 8, 1]) # doctest: +SKIP
    [8, 5]
    """
    pass

#Problem 10 (Challenge)
def compute_centroid(points: list[list[float]]) -> list[float]:
    """Given a list of points (each point is a list of coordinates), 
    return a single point representing the mean of all points.
    >>> compute_centroid([[1, 2], [3, 4], [5, 6]]) # doctest: +SKIP
    [3.0, 4.0]
    >>> compute_centroid([[0, 0, 0], [10, 10, 10]]) # doctest: +SKIP
    [5.0, 5.0, 5.0]
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()