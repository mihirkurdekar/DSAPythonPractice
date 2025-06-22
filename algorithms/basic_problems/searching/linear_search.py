'''
Implement Linear Search to find an element in an unsorted array of integers.
'''

def linear_search(arr, target):
    """
    Perform linear search on an array to find the index of the target element.
    
    :param arr: List of integers.
    :param target: Integer to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# Example usage
if __name__ == "__main__":
    arr = [4, 2, 7, 1, 3]
    target = 3
    index = linear_search(arr, target)
    
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")