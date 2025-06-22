'''
Given an array of integers, sort the array using Merge Sort.
'''

def merge_sort(arr):
    """
    Sort the array using Merge Sort algorithm.
    
    :param arr: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    
    :param left: First sorted list.
    :param right: Second sorted list.
    :return: Merged sorted list.
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
    
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    # Output: Sorted array: [3, 9, 10, 27, 38, 43, 82]