'''
Bubble Sort: Repeatedly swap adjacent elements if they are in the wrong order.
Sort any array using buble sort
'''

def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Returns:
        list: A sorted list of integers.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the list must be integers")
    n = len(arr)

    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Sorted array is:", sorted_arr)
    # Output: Sorted array is: [11, 12, 22, 25, 34, 64, 90]