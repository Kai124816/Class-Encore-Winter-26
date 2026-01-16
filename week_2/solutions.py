#Finish the following functions

#1 
def sum_of_range(a:int, b:int) -> int:
    """Write a function that takes in two numbers a and b
    and returns the sum of all the numbers from a to b (not including b).
    Ex: sum_of_range(3,6) -> 12
    """
    acc = 0
    for i in range(a, b):
        acc += i
    return acc

#2
def largest_num(a:int, b:int, c:int) -> int:
    """Takes in three numbers (a, b, c) and returns
    the largest one.
    Ex: largest_num(1, 2, 0) -> 2
    """
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

#3
def repeat_string(text: str, n: int) -> str:
    """Takes a string and an integer n, and returns the 
    string repeated n times.
    Ex: repeat_string("Hi", 3) -> "HiHiHi"
    """
    result = ""
    for i in range(n):
        result += text
    return result
#4 
def celsius_to_fahrenheit(c: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    Ex: celsius_to_fahrenheit(0) -> 32.0
    """
    return

#5 
def sum_list(l: list) -> int:
    """Sums a list of integers"""
    sum = 0
    for num in l:
        sum += num
    return sum       

#6
def is_even(n: int) -> bool:
    """Takes an integer n and returns True if the 
    number is even, and False if it is odd.
    Ex: is_even(7) -> False
    """
    if n % 2 == 0:
        return True
    else:
        return False

#7 (Challenge)
def find_average(numbers: list) -> float:
    """Takes a list of numbers and returns their average.
    Hint: sum of all numbers divided by the count of numbers.
    Ex: find_average([10, 20, 30]) -> 20.0
    """
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)


#8 (Challenge)
def multiply_all(nums: list[int]) -> int:
    """Return the product of all numbers in nums.
    If the list is empty, return 1."""
    acc = 1
    for num in nums:
        acc *= num
    return acc

