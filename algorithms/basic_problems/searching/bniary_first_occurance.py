'''
Given a sorted array of integers, find the first occurrence of a target element using Binary Search.
'''

def binary_first_occurrence(arr, target):
    """
    Perform binary search on a sorted array to find the first occurrence of the target element.
    
    :param arr: List of sorted integers.
    :param target: Integer to search for in the array.
    :return: Index of the first occurrence of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return first_occurrence

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    index = binary_first_occurrence(arr, target)
    
    if index != -1:
        print(f"First occurrence of element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")