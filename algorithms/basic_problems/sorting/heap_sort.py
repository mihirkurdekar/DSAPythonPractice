'''
Given an array of integers, sort the array in descending order using Heap Sort.

'''

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

def heap_sort(arr):
    """
    Sort the array using Heap Sort algorithm in descending order.

    :param arr: List of integers to be sorted.
    :return: Sorted list of integers in descending order.
    """
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr[::-1]  # Return the sorted array in descending order


# Example usage

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array in descending order: {sorted_arr}")
    # Output: Sorted array in descending order: [13, 12, 11, 7, 6, 5]
    