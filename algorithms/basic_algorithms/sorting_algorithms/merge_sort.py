'''
Merge Sort: Divide the array into smaller chunks, sort each chunk, and merge them back together.
'''

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Returns:
        list: A sorted list of integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    
    Returns:
        list: A merged and sorted list of integers.
    """
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted array is:", sorted_arr)
    # Output: Sorted array is: [3, 9, 10, 27, 38, 43, 82]