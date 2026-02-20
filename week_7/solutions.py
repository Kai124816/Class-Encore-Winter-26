import doctest

# Problem 1
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
    longest_streak = 0  # best streak we've seen so far across the whole list
    streak = 0          # current streak we're actively counting

    for num in nums:
        if num > 0:
            streak += 1         # extend the current streak
        else:
            # The streak just broke — check if it was the best we've seen
            if streak > longest_streak:
                longest_streak = streak
            streak = 0          # reset and start counting fresh

    # The loop above only updates longest_streak when a streak BREAKS.
    # If the list ends on a positive number, the final streak never broke,
    # so we need this final max() to catch it.
    return max(streak, longest_streak)


# Problem 2
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
    len_dict = {}               # start with an empty dictionary

    for word in words:
        # len(word) counts the characters; store it under the word as the key.
        # If the same word appears more than once, we just overwrite the entry
        # with the same value — no harm done.
        len_dict[word] = len(word)

    return len_dict


# Problem 3
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
    # An empty list of centroids is trivially stable — nothing can differ
    if len(old_centroids) == 0:
        return True

    num_centroids = len(old_centroids)
    points_per_centroid = len(old_centroids[0])  # how many coords each centroid has

    # Check every centroid one by one
    for i in range(num_centroids):
        # Check every coordinate inside that centroid
        for j in range(points_per_centroid):
            if old_centroids[i][j] != new_centroids[i][j]:
                # Found a mismatch — no need to check further
                return False

    # If we made it through all centroids without finding a mismatch, they match
    return True


# Problem 4
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
    # Can't compute an average with no data
    if len(grades) == 0:
        return []

    num_grades = len(grades)

    # First pass: add up all the grades to get the total
    avg = 0
    for student, grade in grades.items():
        avg += grade

    avg /= num_grades   # divide total by count to get the mean

    # Second pass: collect every student who scored strictly above the mean
    above_avg = []
    for student, grade in grades.items():
        if grades[student] > avg:
            above_avg.append(student)

    return above_avg


# Problem 5
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
    # Check every number against the threshold.
    # The moment we find one that fails, we can immediately return False —
    # there's no need to keep checking the rest of the list.
    for num in a:
        if num <= threshold:
            return False

    # If we never returned False inside the loop, every number passed.
    # Note: if the list is empty the loop never runs, so we return True here.
    # An empty list vacuously satisfies "all elements are greater" — but the
    # docstring says the list must have length > 0, so the caller is responsible
    # for not passing an empty list.
    return True


# Problem 6
def evens_greater(l1: list[int]) -> bool:
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
        if num % 2 == 0:    # num % 2 == 0 means the number divides evenly by 2
            even_sum += num
        else:
            odd_sum += num

    # Strict greater-than: if both sums are 0 (empty list), this returns False
    if even_sum > odd_sum:
        return True
    return False


# Problem 7 (Challenge)
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

    # Outer loop: visit each sublist one by one
    for sublist in lists:
        # Inner loop: visit each number inside that sublist
        for num in sublist:
            if num > 0:             # only keep strictly positive numbers
                flattened.append(num)

    return flattened


# Problem 8 (Challenge)
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
    # Seed our "current best" with the very first student so we always
    # have something valid to compare against
    best_pair = [students[0], scores[0]]    # [name, score]

    # Start at index 1 since we already stored index 0 as the initial best
    for i in range(1, len(students)):
        if scores[i] > best_pair[1]:
            # Found a new high score — update both the name and the score
            best_pair[0] = students[i]
            best_pair[1] = scores[i]

    return best_pair[0]


# Problem 9 (Challenge)
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

    # Seed greatest and second using the first two elements.
    # We need to figure out which of the two is larger before we start.
    if l1[0] >= l1[1]:
        greatest = l1[0]
        second   = l1[1]
    else:
        greatest = l1[1]
        second   = l1[0]

    # Now scan the rest of the list starting at index 2
    for i in range(2, len(l1)):
        num = l1[i]
        if num > greatest:
            # New overall champion — the old greatest drops to second place
            temp     = greatest
            greatest = num
            second   = temp
        elif num > second:
            # Not the best, but beats second place — update second only
            second = num

    return [greatest, second]


# Problem 10 (Challenge)
def compute_centroid(points: list[list[float]]) -> list[float]:
    """Given a list of points (each point is a list of coordinates), 
    return a single point representing the mean of all points.
    >>> compute_centroid([[1, 2], [3, 4], [5, 6]])
    [3.0, 4.0]
    >>> compute_centroid([[0, 0, 0], [10, 10, 10]])
    [5.0, 5.0, 5.0]
    """
    num_points         = len(points)
    coords_per_point   = len(points[0])   # how many dimensions each point has

    # Start the centroid as a list of zeros — one zero per dimension
    centroid = [0 for i in range(coords_per_point)]

    # Add up the coordinates dimension-by-dimension across all points
    for point in points:
        for i in range(coords_per_point):
            centroid[i] += point[i]

    # Divide each summed coordinate by the number of points to get the mean
    for i in range(coords_per_point):
        centroid[i] /= num_points

    return centroid


if __name__ == "__main__":
    import doctest
    doctest.testmod()