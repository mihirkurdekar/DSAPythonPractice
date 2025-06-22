'''
Binary Search: Divide the array in half and search for the element in one of the two halves.
'''

def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using binary search.
    
    Args:
        arr (list): The sorted list of integers to search through.
        target (int): The integer value to search for.
    
    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30
    index = binary_search(arr, target)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")
    # Output: Element found at index: 2