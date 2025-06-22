# Problem: Given an array of integers, find the longest subarray with a given sum.
# Example: arr = [1, 4, 20, 3, 10, 5], target_sum = 33
# Output: [20, 3, 10] (longest subarray with sum 33)

def longest_subarray_with_sum(arr, target_sum):
    # This function finds the longest subarray with a given sum in an array of integers.
    n = len(arr)
    max_length = 0
    current_sum = 0
    start = 0
    subarray = []
    # Iterate through the array using a sliding window approach
    for end in range(n):
        # Add the current element to the current sum
        current_sum += arr[end]
        # Shrink the window from the left until the current sum is less than or equal to target_sum
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1

        # If the current sum equals the target sum, check if this is the longest subarray found
        if current_sum == target_sum:
            # Check if the current subarray is longer than the previously found subarray
            if (end - start + 1) > max_length:
                max_length = end - start + 1
                subarray = arr[start:end + 1]

    return subarray if subarray else None

# Example usage
if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    target_sum = 33
    result = longest_subarray_with_sum(arr, target_sum)
    print("Longest subarray with sum", target_sum, "is:", result)