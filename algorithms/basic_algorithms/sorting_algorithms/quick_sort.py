'''
Quick Sort: Select a pivot element, partition the array around it, and recursively sort the subarrays.
'''

def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
    
    Returns:
        list: A sorted list of integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = quick_sort(arr)
    print("Sorted array is:", sorted_arr)
    # Output: Sorted array is: [3, 9, 10, 27, 38, 43, 82]