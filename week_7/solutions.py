import doctest

#Problem 1
def longest_streak_of_positives(nums: list[int]) -> int:
    """Given a list of integers, return the length of the longest
    consecutive streak of positive numbers (> 0). Returns 0 if
    there are no positive numbers or the list is empty.
    >>> longest_streak_of_positives([1, 2, -1, 3, 4, 5, -2, 6])
    3
    >>> longest_streak_of_positives([-1, -2, -3])
    0
    >>> longest_streak_of_positives([])
    0
    >>> longest_streak_of_positives([1, 2, 3, 4])
    4
    """
    longest_streak = 0
    streak = 0
    for num in nums:
        if num > 0:
            streak += 1
        else:
            if streak > longest_streak:
                longest_streak = streak
            streak = 0
    
    return max(streak, longest_streak)

#Problem 2
def word_lengths(words: list[str]) -> dict[str, int]:
    """Given a list of words, return a dictionary mapping each word to
    its length.
    >>> word_lengths(["cat", "elephant", "ox"])
    {'cat': 3, 'elephant': 8, 'ox': 2}
    >>> word_lengths([])
    {}
    >>> word_lengths(["hi", "hi", "bye"])
    {'hi': 2, 'bye': 3}
    """
    len_dict = {}
    for word in words:
        len_dict[word] = len(word)
    return len_dict

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
    if len(old_centroids) == 0:
        return True 
    
    num_centroids = len(old_centroids)
    points_per_centroid = len(old_centroids[0])
    for i in range(num_centroids):
        for j in range(points_per_centroid):
            if old_centroids[i][j] != new_centroids[i][j]:
                return False
    return True

#Problem 4
def above_average(grades: dict[str, float]) -> list[str]:
    """Given a dictionary mapping student names to numeric grades,
    return a sorted list of the names of students whose grade is
    strictly above the average grade. Return an empty list if
    grades is empty.
    >>> above_average({"Alice": 90, "Bob": 70, "Carol": 80})
    ['Alice']
    >>> above_average({"Alice": 85, "Bob": 85})
    []
    >>> above_average({})
    []
    """
    if len(grades) == 0:
        return []
    
    num_grades = len(grades)
    avg = 0
    for student, grade in grades.items():
        avg += grade
    
    avg /= num_grades
    above_avg = []
    for student, grade in grades.items():
        if grades[student] > avg:
            above_avg.append(student)
    return above_avg

#Problem 5
def all_greater(a: list[int], threshold: int) -> bool:
    """Returns True if list a has a length greater than 0
    and every element in a is strictly greater than the threshold
    >>> all_greater([2, 3, 3], 3)
    False
    >>> all_greater([6,7,8], 5)
    True
    >>> all_greater([3], 3)
    False
    >>> all_greater([0], 10)
    False
    """
    for num in a:
        if num <= threshold:
            return False
    return True

#Problem 6
def evens_greater(l1:list[int]) -> bool:
    """Returns true if the sum of the even numbers in 
    the list is greater than the sum of the odd numbers.
    >>> evens_greater([2, 4, 1, 3])
    True
    >>> evens_greater([1, 3, 5, 2])
    False
    >>> evens_greater([2, 2, 3, 3])
    False
    >>> evens_greater([])
    False
    """
    even_sum = 0
    odd_sum = 0

    for num in l1:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    if even_sum > odd_sum:
        return True
    return False

#Problem 7 (Challenge)
def flatten_positive(lists: list[list[int]]) -> list[int]:
    """Given a list of lists of integers, return a single flat list
    containing only the positive integers (> 0) from all sublists,
    in the order they appear.
    >>> flatten_positive([[1, -2, 3], [0, 4], [-5, 6]])
    [1, 3, 4, 6]
    >>> flatten_positive([[], [1, 2], []])
    [1, 2]
    >>> flatten_positive([[-1, -2], [-3]])
    []
    """
    flattened = []
    for list in lists:
        for num in list:
            if num > 0:
                flattened.append(num)
    return flattened
        

#Problem 8 (Challenge)
def best_student(students: list[str], scores: list[int]) -> str:
    """Given parallel lists where element i is a student and scores[i]
    is their score, return the name of the student with the highest
    score. You may assume the lists are non-empty and the same length.
    Ties may be broken any way you like.
    >>> best_student(["Alice", "Bob", "Carol"], [72, 95, 88])
    'Bob'
    >>> best_student(["Alice"], [100])
    'Alice'
    >>> best_student(["Alice", "Bob"], [87, 85])
    'Alice'
    """
    best_pair = [students[0], scores[0]]
    for i in range(1,len(students)):
        if scores[i] > best_pair[1]:
            best_pair[0] = students[i]
            best_pair[1] = scores[i]
    return best_pair[0]
                
#Problem 9 (Challenge)
def top_two(l1: list[int]) -> list[int]:
    """Given a list of integers, return a list containing the two
    largest values in descending order. You may assume the list
    has at least two elements and all values are unique.
    >>> top_two([3, 1, 4, 1, 5, 9, 2, 6])
    [9, 6]
    >>> top_two([10, 20])
    [20, 10]
    >>> top_two([5, 3, 8, 1])
    [8, 5]
    """
    if len(l1) < 2:
        return l1
    
    if l1[0] >= l1[1]:
        greatest = l1[0]
        second = l1[1]
    else:
        greatest = l1[1]
        second = l1[0]

    for i in range(2, len(l1)):
        num = l1[i]
        if num > greatest:
            temp = greatest
            greatest = num
            second = temp
        elif num > second:
            second = num
    return [greatest, second]

#Problem 10 (Challenge)
def compute_centroid(points: list[list[float]]) -> list[float]:
    """Given a list of points (each point is a list of coordinates), 
    return a single point representing the mean of all points.
    >>> compute_centroid([[1, 2], [3, 4], [5, 6]])
    [3.0, 4.0]
    >>> compute_centroid([[0, 0, 0], [10, 10, 10]])
    [5.0, 5.0, 5.0]
    """
    num_centroids = len(points)
    coords_per_centroid = len(points[0])
    centroid = [0 for i in range(coords_per_centroid)]
    for point in points:
        for i in range(coords_per_centroid):
            centroid[i] += point[i]

    for i in range(coords_per_centroid):
        centroid[i] /= num_centroids
    
    return centroid 
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()