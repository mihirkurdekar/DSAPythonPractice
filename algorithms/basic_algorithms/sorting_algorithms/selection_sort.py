'''
Selection Sort: Select the smallest element from the unsorted portion and swap it with the first unsorted element.
'''

def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    
    Returns:
        list: A sorted list of integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    n = len(arr)
    
    for i in range(n):
        # Assume the minimum is the first element of the unsorted portion
        min_index = i
        for j in range(i+1, n):
            # Update min_index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array is:", sorted_arr)
    # Output: Sorted array is: [11, 12, 22, 25, 64]