'''
Linear Search: Iterate through the array and check each element.
'''

def linear_search(arr, target):
    """
    Searches for a target value in an array using linear search.
    
    Args:
        arr (list): The list of integers to search through.
        target (int): The integer value to search for.
    
    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    for index, value in enumerate(arr):
        if value == target:
            return index
    
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30
    index = linear_search(arr, target)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    # Output: Element found at index: 2