'''
Implement Quick Sort to sort an array of strings.
'''


def quick_sort(arr):
    """
    Sort the array using Quick Sort algorithm.
    
    :param arr: List of strings to be sorted.
    :return: Sorted list of strings.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    arr = ["banana", "apple", "orange", "kiwi", "grape"]
    sorted_arr = quick_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    # Output: Sorted array: ['apple', 'banana', 'grape', 'kiwi', 'orange']
    