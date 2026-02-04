# Problem 1
def sum_second_half(l1: list[int]) -> int:
    """
    Returns the sum of the elements in the second half of the list. 
    """
    acc = 0  # Initialize an 'accumulator' to keep track of the running total
    list_length = len(l1)
    
    # Calculate the starting index. // performs integer division (flooring), 
    # which correctly handles the "middle" for both even and odd lengths.
    start = (list_length // 2)

    # Loop from the middle index to the very end of the list
    for i in range(start, list_length):
        acc += l1[i]  # Add the value at the current index to our total
    return acc

# Problem 2
def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries into one, summing values for shared keys.
    """
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    merged = {}  # Create a new dictionary to store the result

    # First, copy all entries from the first dictionary into the result
    for key in d1_keys:
        merged[key] = d1[key]

    # Next, look at the second dictionary
    for key in d2_keys:
        if key in merged:
            # If the key already exists (from d1), add the new value to the existing one
            merged[key] += d2[key]
        else:
            # If the key is new, simply create the entry
            merged[key] = d2[key]
    
    return merged

# Problem 3
def appears_once(l1: list[str]) -> list[str]:
    """
    Returns a list of strings that appear exactly once in the input list.
    """
    once = []
    counts = {} # This dictionary will store: {string: number_of_occurrences}
    
    # Step 1: Count how many times every string appears
    for el in l1:
        if el not in counts:
            counts[el] = 1
        else:
            counts[el] += 1
    
    # Step 2: Iterate through our counts and pick keys with a count of exactly 1
    for key in counts.keys():
        if counts[key] == 1:
            once.append(key)
    
    return once

# Problem 4
def shorter_first(a: list[str], b: list[str]) -> list[str]:
    """
    Compares elements at each index i and returns a list of the shorter strings.
    """
    # Find the length of the smaller list so we don't go "out of bounds"
    shortest_len = min(len(a), len(b))
    shortest = []

    for i in range(shortest_len):
        # Compare the length of the string in list 'a' vs list 'b'
        if len(a[i]) < len(b[i]):
            shortest.append(a[i])
        else:
            # If b[i] is shorter OR they are equal, b[i] is chosen
            shortest.append(b[i])
    return shortest

# Problem 5
def matches(x_l: list[str], y_l: list[str]) -> list[bool]:
    """
    Compares two lists of equal length and returns a list of booleans.
    """
    same = []
    # Use a range-based loop to access the same index in both lists simultaneously
    for i in range(len(x_l)):
        if x_l[i] == y_l[i]:
            same.append(True)
        else:
            same.append(False)
    return same

# Problem 6
def all_greater(a: list[int], b: list[int]) -> bool:
    """
    Returns True if lists are same length and a[i] > b[i] for all i.
    """
    a_length = len(a)
    b_length = len(b)
    
    # Guard Clause: If lengths differ, the condition is immediately failed
    if(a_length != b_length):
        return False
    
    for i in range(a_length):
        # "Early Return" strategy: If we find even one pair that fails 
        # the 'strictly greater' rule, we can stop and return False immediately.
        if a[i] <= b[i]:
            return False
            
    # If the loop finishes without returning False, every element passed the test
    return True

# Problem 7
def combine(keys: list[str], values: list[int]) -> dict:
    """
    Creates a dictionary from keys and values, summing values for duplicate keys.
    """
    combined = {}
    # Iterate through indices so we can grab the key and value at the same position
    for i in range(len(keys)):
        current_key = keys[i]
        current_val = values[i]
        
        if current_key not in combined:
            combined[current_key] = current_val
        else:
            # Add to the existing total for this key
            combined[current_key] += current_val
    return combined

# Problem 8
def vecmax(a: list[int], b: list[int]) -> list[int]:
    """
    Returns a new list containing the maximum value at each index.
    """
    only_max = []
    for i in range(len(a)):
        # Traditional if/else to determine which number is larger
        if a[i] > b[i]:
            only_max.append(a[i])
        else:
            only_max.append(b[i])
    return only_max

# Problem 9
def max_key(d1: dict) -> str:
    """
    Returns the key associated with the largest integer value.
    """
    keys = d1.keys()
    m_key = "" # This will store the key of the largest value found so far

    for key in keys:
        # Initialize m_key with the first key we see
        if m_key == "":
            m_key = key
        # If the current key's value is bigger than our current record holder...
        elif d1[key] > d1[m_key]:
            m_key = key # Update the record holder
            
    return m_key

if __name__ == "__main__":
    import doctest
    doctest.testmod()