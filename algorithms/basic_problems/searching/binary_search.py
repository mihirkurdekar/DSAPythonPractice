'''
Given a sorted array of integers, find the index of a target element using Binary Search.
'''

def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    
    :param arr: List of sorted integers.
    :param target: Integer to search for in the array.
    :return: Index of the target element if found, otherwise -1.
    """
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
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print(f"Element {target} not found in the array.")