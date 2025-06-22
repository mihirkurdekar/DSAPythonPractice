'''
Insertion Sort: Insert each element into its proper position in the sorted portion.
'''
def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    
    Returns:
        list: A sorted list of integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print("Sorted array is:", sorted_arr)
    # Output: Sorted array is: [5, 6, 11, 12, 13]