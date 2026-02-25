def deep_reverse(l1):
    # Base case: if it's not a list, just return the element as is
    if not isinstance(l1, list):
        return l1
    
    # Base case: empty list
    if len(l1) == 0:
        return []

    # Recursive step: 
    # 1. Take the last element and deep_reverse it
    # 2. Wrap it in a list [ ] so we can concatenate
    # 3. Add the deep_reverse of the rest of the list
    return [deep_reverse(l1[-1])] + deep_reverse(l1[:-1])

# Test Case
my_nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(deep_reverse(my_nested_list))
# Output: [[9, 8, 7], [6, 5, 4], [3, 2, 1]]